#!/usr/bin/env python3
"""Project and validate a concrete subset of the unified Registry contract.

Projection keeps selected operations and the component references they can reach. It
does not flatten schemas, so recursive models and closed metadata retain their exact
semantics.
"""

from __future__ import annotations

import argparse
from collections import deque
from copy import deepcopy
import os
from pathlib import Path
from urllib.parse import unquote, urldefrag

from jsonschema import Draft202012Validator, FormatChecker
from openapi_spec_validator import validate
import yaml


ROOT = Path(__file__).resolve().parents[1]
CONSULTATION_EXTENSION = "x-govstack-digital-registries"
WRITE_EXTENSION = "x-govstack-digital-registries-write"
PROJECTION_EXTENSION = "x-govstack-contract-projection"
HTTP_METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}
CORE_PATHS = ("/health", "/.well-known/api-catalog")
COMPONENT_CATEGORIES = {
    "schemas",
    "responses",
    "parameters",
    "examples",
    "requestBodies",
    "headers",
    "securitySchemes",
    "links",
    "callbacks",
    "pathItems",
}


class LiteralBlockDumper(yaml.SafeDumper):
    """Render multiline strings as reviewable YAML literal blocks."""


def _represent_string(dumper: yaml.SafeDumper, value: str):
    style = "|" if "\n" in value else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style=style)


LiteralBlockDumper.add_representer(str, _represent_string)


def load_document(path: Path) -> dict:
    value = yaml.safe_load(path.read_text())
    if not isinstance(value, dict):
        raise ValueError(f"OpenAPI document must be an object: {path}")
    return value


def dump_document(document: dict) -> str:
    return yaml.dump(
        document,
        Dumper=LiteralBlockDumper,
        sort_keys=False,
        allow_unicode=True,
    )


def _operations(document: dict):
    for route, path_item in document.get("paths", {}).items():
        if not isinstance(path_item, dict):
            continue
        for method, operation in path_item.items():
            if method in HTTP_METHODS and isinstance(operation, dict):
                yield route, method, operation


def _component_reference(reference: str) -> tuple[str, str] | None:
    prefix = "#/components/"
    if not reference.startswith(prefix):
        return None
    parts = reference[len(prefix) :].split("/")
    if len(parts) < 2 or parts[0] not in COMPONENT_CATEGORIES:
        raise ValueError(f"Unsupported component reference: {reference}")
    return tuple(part.replace("~1", "/").replace("~0", "~") for part in parts[:2])


def _references(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key in {"$ref", "inputSchema"} and isinstance(child, str):
                yield child
            elif isinstance(child, str) and child.startswith("#/components/"):
                # Registry extensions use JSON References as metadata values, for
                # example inputSchema. Keep their targets in a projection too.
                yield child
            else:
                yield from _references(child)
    elif isinstance(value, list):
        for child in value:
            yield from _references(child)


def _effective_security(document: dict, selected_operations: list[dict]) -> set[str]:
    schemes = set()
    for operation in selected_operations:
        requirements = operation.get("security", document.get("security", []))
        for requirement in requirements:
            schemes.update(requirement)
    return schemes


def _apply_baseline_retrieve(operation: dict) -> None:
    """Remove the canonical optional conditional-read selection for a read baseline."""
    metadata = operation.get(CONSULTATION_EXTENSION, {})
    if metadata.get("capability") != "retrieve":
        return
    features = list(metadata.get("features", []))
    if "conditional-read" not in features:
        return
    features.remove("conditional-read")
    if features:
        metadata["features"] = features
    else:
        metadata.pop("features", None)

    original_parameters = operation.get("parameters", [])
    operation["parameters"] = [
        parameter
        for parameter in original_parameters
        if parameter.get("$ref") != "#/components/parameters/IfNoneMatch"
    ]
    if len(operation["parameters"]) == len(original_parameters):
        raise ValueError(
            "The baseline-retrieve preset expected the canonical IfNoneMatch parameter"
        )
    responses = operation["responses"]
    if "304" not in responses:
        raise ValueError(
            "The baseline-retrieve preset expected the canonical 304 response"
        )
    responses.pop("304")
    if responses.get("200") != {"$ref": "#/components/responses/StrongRecord"}:
        raise ValueError(
            "The baseline-retrieve preset expected the canonical StrongRecord response"
        )
    responses["200"] = {"$ref": "#/components/responses/Record"}


def _apply_baseline_description(projected: dict) -> None:
    description = projected["info"]["description"]
    owner_text = (
        "This combined reference contract selects conditional-read on Retrieve. Read-only "
        "deployment\nprofiles can omit that feature and its validator."
    )
    baseline_text = (
        "The unified owner selects conditional-read on Retrieve. This generated baseline "
        "projection\nomits that feature and its validator."
    )
    if owner_text not in description:
        raise ValueError(
            "The baseline-retrieve preset could not identify the canonical feature description"
        )
    projected["info"]["description"] = description.replace(owner_text, baseline_text, 1)


def _reachable_components(
    document: dict, roots: dict, selected_operations: list[dict]
) -> dict:
    requested = deque()
    for reference in _references(roots):
        component = _component_reference(reference)
        if component is not None:
            requested.append(component)
    requested.extend(
        ("securitySchemes", name)
        for name in _effective_security(document, selected_operations)
    )

    source_components = document.get("components", {})
    projected = {}
    visited = set()
    while requested:
        category, name = requested.popleft()
        identity = (category, name)
        if identity in visited:
            continue
        visited.add(identity)
        try:
            value = deepcopy(source_components[category][name])
        except KeyError as error:
            raise ValueError(
                f"Missing referenced component #/components/{category}/{name}"
            ) from error
        projected.setdefault(category, {})[name] = value
        for reference in _references(value):
            component = _component_reference(reference)
            if component is not None:
                requested.append(component)
    return projected


def _rebase_external_references(value, source: Path, output: Path):
    if isinstance(value, dict):
        rebased = {}
        for key, child in value.items():
            if key in {"$ref", "inputSchema"} and isinstance(child, str):
                target, fragment = urldefrag(child)
                if target and not target.startswith(
                    ("/", "http://", "https://", "file:")
                ):
                    absolute = (source.parent / unquote(target)).resolve()
                    relative = os.path.relpath(absolute, output.parent.resolve())
                    child = Path(relative).as_posix()
                    if fragment:
                        child += f"#{fragment}"
                rebased[key] = child
            else:
                rebased[key] = _rebase_external_references(child, source, output)
        return rebased
    if isinstance(value, list):
        return [_rebase_external_references(child, source, output) for child in value]
    return value


def project_contract(
    source: Path,
    output: Path,
    operation_ids: list[str],
    *,
    baseline_retrieve: bool = False,
) -> dict:
    """Return a deterministic OpenAPI projection for the selected operation IDs."""
    if not operation_ids:
        raise ValueError("At least one --operation-id is required")
    if len(set(operation_ids)) != len(operation_ids):
        raise ValueError("Operation IDs must not be repeated")

    document = load_document(source)
    indexed = {}
    for route, method, operation in _operations(document):
        operation_id = operation.get("operationId")
        if operation_id in indexed:
            raise ValueError(f"Duplicate operationId in source: {operation_id}")
        if operation_id is not None:
            indexed[operation_id] = (route, method, operation)
    missing = [
        operation_id for operation_id in operation_ids if operation_id not in indexed
    ]
    if missing:
        raise ValueError(f"Unknown operationId(s): {', '.join(missing)}")

    projected_paths = {}
    selected_operations = []
    for route in CORE_PATHS:
        if route not in document.get("paths", {}):
            continue
        source_path_item = document["paths"][route]
        path_item = projected_paths.setdefault(route, {})
        for key, value in source_path_item.items():
            if key not in HTTP_METHODS or isinstance(value, dict):
                path_item[key] = deepcopy(value)
            if key in HTTP_METHODS and isinstance(value, dict):
                selected_operations.append(path_item[key])
    for operation_id in operation_ids:
        route, method, operation = indexed[operation_id]
        source_path_item = document["paths"][route]
        path_item = projected_paths.setdefault(route, {})
        for key in ("summary", "description", "servers", "parameters"):
            if key in source_path_item:
                path_item[key] = deepcopy(source_path_item[key])
        path_item[method] = deepcopy(operation)
        if baseline_retrieve:
            _apply_baseline_retrieve(path_item[method])
        selected_operations.append(path_item[method])

    projected = {
        key: deepcopy(document[key])
        for key in (
            "openapi",
            "info",
            "jsonSchemaDialect",
            "servers",
            "security",
            "externalDocs",
            "x-govstack-api-guide",
        )
        if key in document
    }
    projected[PROJECTION_EXTENSION] = {
        "source": Path(
            os.path.relpath(source.resolve(), output.parent.resolve())
        ).as_posix(),
        "operationIds": list(operation_ids),
    }
    if baseline_retrieve:
        projected[PROJECTION_EXTENSION]["preset"] = "baseline-retrieve"
        _apply_baseline_description(projected)
    used_tags = {
        tag for operation in selected_operations for tag in operation.get("tags", [])
    }
    if "tags" in document:
        projected["tags"] = [
            deepcopy(tag) for tag in document["tags"] if tag.get("name") in used_tags
        ]
    projected["paths"] = projected_paths
    components = _reachable_components(document, projected, selected_operations)
    if components:
        projected["components"] = components
    return _rebase_external_references(projected, source, output)


def _json_pointer(document: dict, fragment: str):
    value = document
    for token in fragment.removeprefix("/").split("/") if fragment else ():
        token = token.replace("~1", "/").replace("~0", "~")
        value = value[token]
    return value


def _resolve(document: dict, path: Path, value: dict) -> tuple[dict, Path, dict]:
    seen = set()
    while isinstance(value, dict) and "$ref" in value:
        reference = value["$ref"]
        target, fragment = urldefrag(reference)
        identity = (path.resolve(), reference)
        if identity in seen:
            raise ValueError(
                f"Reference cycle while resolving scalar contract metadata: {reference}"
            )
        seen.add(identity)
        if target:
            if target.startswith(("http://", "https://", "file:")):
                raise ValueError(
                    f"Concrete validation only resolves local references: {reference}"
                )
            path = (path.parent / unquote(target)).resolve()
            document = load_document(path)
        value = _json_pointer(document, fragment)
    return document, path, value


def _validate_record_identifier_bounds(document: dict, path: Path) -> None:
    for _, _, operation in _operations(document):
        for raw_parameter in operation.get("parameters", []):
            parameter_document, parameter_path, parameter = _resolve(
                document, path, raw_parameter
            )
            if parameter.get("in") != "path" or parameter.get("name") != "recordId":
                continue
            _, _, schema = _resolve(
                parameter_document, parameter_path, parameter["schema"]
            )
            minimum = schema.get("minLength")
            maximum = schema.get("maxLength")
            if (
                not isinstance(minimum, int)
                or isinstance(minimum, bool)
                or minimum < 1
                or not isinstance(maximum, int)
                or isinstance(maximum, bool)
                or maximum < minimum
            ):
                raise ValueError(
                    "Concrete recordId schemas need finite minLength and maxLength bounds"
                )


def _validate_cursor_bounds(document: dict, path: Path) -> None:
    for _, _, operation in _operations(document):
        for raw_parameter in operation.get("parameters", []):
            parameter_document, parameter_path, parameter = _resolve(
                document, path, raw_parameter
            )
            if parameter.get("name") != "cursor":
                continue
            _, _, schema = _resolve(
                parameter_document, parameter_path, parameter["schema"]
            )
            minimum = schema.get("minLength")
            maximum = schema.get("maxLength")
            if (
                not isinstance(minimum, int)
                or isinstance(minimum, bool)
                or minimum < 1
                or not isinstance(maximum, int)
                or isinstance(maximum, bool)
                or maximum < minimum
                or maximum > 4096
            ):
                raise ValueError(
                    "Concrete cursor schemas need finite bounds no wider than 4096 characters"
                )


def validate_document(document: dict, path: Path) -> None:
    """Validate one concrete subset without requiring absent reference operations."""
    validate(document, base_uri=path.resolve().as_uri())
    operation_ids = []
    registry_operations = 0
    extension_schemas = {
        CONSULTATION_EXTENSION: ROOT
        / "api/extensions/x-govstack-digital-registries.schema.json",
        WRITE_EXTENSION: ROOT
        / "api/extensions/x-govstack-digital-registries-write.schema.json",
    }
    for _, _, operation in _operations(document):
        operation_id = operation.get("operationId")
        if operation_id is not None:
            operation_ids.append(operation_id)
        selected = [name for name in extension_schemas if name in operation]
        if len(selected) > 1:
            raise ValueError(
                f"{operation_id} declares both Registry operation extensions"
            )
        if selected:
            registry_operations += 1
            schema_path = extension_schemas[selected[0]]
            Draft202012Validator(
                load_document(schema_path), format_checker=FormatChecker()
            ).validate(operation[selected[0]])
    if len(operation_ids) != len(set(operation_ids)):
        raise ValueError("Concrete contract repeats an operationId")
    if registry_operations == 0:
        raise ValueError("Concrete contract selects no Registry operation")
    _validate_record_identifier_bounds(document, path)
    _validate_cursor_bounds(document, path)


def validate_contract(path: Path) -> None:
    validate_document(load_document(path), path)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", type=Path)
    parser.add_argument("output", nargs="?", type=Path)
    parser.add_argument("--operation-id", action="append", default=[])
    parser.add_argument("--baseline-retrieve", action="store_true")
    parser.add_argument("--validate", dest="validate_path", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _parser()
    args = parser.parse_args(argv)
    if args.validate_path is not None:
        if (
            args.source is not None
            or args.output is not None
            or args.operation_id
            or args.baseline_retrieve
        ):
            parser.error("--validate cannot be combined with projection arguments")
        validate_contract(args.validate_path)
        print(f"Validated {args.validate_path}")
        return 0
    if args.source is None or args.output is None:
        parser.error("SOURCE and OUTPUT are required for projection")
    projected = project_contract(
        args.source,
        args.output,
        args.operation_id,
        baseline_retrieve=args.baseline_retrieve,
    )
    args.output.write_text(dump_document(projected))
    validate_contract(args.output)
    print(f"Generated and validated {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
