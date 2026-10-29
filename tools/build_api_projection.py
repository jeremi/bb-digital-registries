#!/usr/bin/env python3
"""Build a framework authoring view of the contracts embedded by upstream chapter 8."""

from __future__ import annotations

import copy
from pathlib import Path
import posixpath
import sys
from urllib.parse import urlsplit

import yaml

BASE = "8588a219df9a8406e66c4392d0bef664b34e4e30"
ROOT = Path(__file__).resolve().parents[1]
METHODS = {"get", "post", "put", "patch", "delete", "head", "options", "trace"}
ALIASES = {
    ("get", "/database/{id}"): "getDatabase",
    ("delete", "/database/{id}"): "deleteDatabase",
    ("post", "/database/modify"): "modifyDatabase",
    ("get", "/databases"): "listDatabases",
}
SOURCES = {
    "data": (
        "spec/.gitbook/assets/GovStack_Digital_registries_BB_Data_API_template-1.3.0.json",
        "resources/upstream-api/data-api.json",
    ),
    "database": (
        "spec/.gitbook/assets/GovStack_Digital_registries_BB_Database_API_template-1.3.0.yaml",
        "resources/upstream-api/database-api.yaml",
    ),
}


def qualify_refs(value, reference: str):
    if isinstance(value, list):
        return [qualify_refs(item, reference) for item in value]
    if not isinstance(value, dict):
        return copy.deepcopy(value)
    result = {}
    for key, item in value.items():
        if key == "$ref" and isinstance(item, str):
            if item.startswith("#"):
                result[key] = reference + item
            elif not urlsplit(item).scheme and not item.startswith("/"):
                result[key] = posixpath.join(posixpath.dirname(reference), item)
            else:
                result[key] = item
        else:
            result[key] = qualify_refs(item, reference)
    return result


def qualify_security(requirements: list, namespace: str) -> list:
    return [
        {f"{namespace}__{key}": copy.deepcopy(scopes) for key, scopes in item.items()}
        for item in requirements
    ]


def build_projection(data: dict, database: dict) -> dict:
    """Copy operations; preserve wire contracts and add only documented authoring metadata."""
    result = {
        "openapi": "3.0.0",
        "info": {
            "title": "Digital Registries upstream API authoring projection",
            "version": "1.3.0",
            "description": (
                "Generated from the two contracts embedded by upstream chapter 8. "
                "Paths, operations and schemas retain their source meaning. "
                "Four Database operation identifiers are authoring aliases, not endpoint changes."
            ),
        },
        "x-upstream-commit": BASE,
        "x-authoring-projection": True,
        "paths": {},
        "components": {"securitySchemes": {}},
        "x-operation-id-aliases": [],
    }
    seen_ids = set()
    for namespace, source in (("data", data), ("database", database)):
        reference = f"upstream-api/{'data-api.json' if namespace == 'data' else 'database-api.yaml'}"
        for name in source.get("components", {}).get("securitySchemes", {}):
            result["components"]["securitySchemes"][f"{namespace}__{name}"] = {
                "$ref": f"{reference}#/components/securitySchemes/{name}"
            }
        for path, original_path in source.get("paths", {}).items():
            if path in result["paths"]:
                raise ValueError(
                    f"overlapping path in selected upstream contracts: {path}"
                )
            path_item = qualify_refs(original_path, reference)
            for method, operation in path_item.items():
                if method not in METHODS:
                    continue
                operation_id = operation.get("operationId")
                if not operation_id:
                    operation_id = (
                        ALIASES.get((method, path)) if namespace == "database" else None
                    )
                    if not operation_id:
                        raise ValueError(
                            f"unassigned upstream operation: {method.upper()} {path}"
                        )
                    operation["operationId"] = operation_id
                    result["x-operation-id-aliases"].append(
                        {
                            "operationId": operation_id,
                            "source": reference,
                            "method": method,
                            "path": path,
                        }
                    )
                if operation_id in seen_ids:
                    raise ValueError(f"duplicate operation identifier: {operation_id}")
                seen_ids.add(operation_id)
                if "security" in operation:
                    operation["security"] = qualify_security(
                        operation["security"], namespace
                    )
                elif "security" in source:
                    operation["security"] = qualify_security(
                        source["security"], namespace
                    )
                if "servers" not in operation and "servers" in source:
                    operation["servers"] = copy.deepcopy(source["servers"])
            result["paths"][path] = path_item
    return result


def projection_errors(actual: dict, data: dict, database: dict) -> list[str]:
    return (
        []
        if actual == build_projection(data, database)
        else [
            "API authoring projection differs from the selected upstream operation copies"
        ]
    )


def generate(root: Path = ROOT, check: bool = False) -> list[str]:
    documents = {}
    errors = []
    for name, (source, destination) in SOURCES.items():
        contents = (root / source).read_bytes()
        target = root / destination
        if check:
            if not target.exists() or target.read_bytes() != contents:
                errors.append(
                    f"{destination}: differs from selected upstream source {source}"
                )
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(contents)
        documents[name] = yaml.safe_load(contents)
    projected = build_projection(documents["data"], documents["database"])
    target = root / "resources/api.yml"
    if check:
        if not target.exists():
            errors.append("resources/api.yml: missing authoring projection")
        else:
            errors.extend(
                projection_errors(yaml.safe_load(target.read_bytes()), **documents)
            )
    else:
        target.write_text(
            yaml.safe_dump(projected, sort_keys=False, allow_unicode=True)
        )
    return errors


if __name__ == "__main__":
    errors = generate(check="--check" in sys.argv[1:])
    if errors:
        print("\n".join(errors), file=sys.stderr)
        raise SystemExit(1)
    print("API authoring projection matches the selected upstream contracts.")
