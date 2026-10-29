#!/usr/bin/env python3
"""Validate the authoring structure and preservation of official upstream content."""

from __future__ import annotations

from collections import Counter
import hashlib
import io
from pathlib import Path
import re
import subprocess
import sys
import tarfile
from urllib.parse import unquote, urlsplit

import yaml

from build_api_projection import BASE, METHODS, generate

ROOT = Path(__file__).resolve().parents[1]
ROOT_EDITS = {"README.md", ".gitbook.yaml", ".gitignore"}
INTERACTIONS = {
    "SERVICE_API",
    "CONSUMED_API",
    "PROTOCOL",
    "EVENT",
    "USER_INTERFACE",
    "DEVICE",
    "FILE",
    "INTERNAL",
}


def baseline_files(root: Path = ROOT) -> dict[str, bytes]:
    archive = subprocess.run(
        ["git", "--no-optional-locks", "-C", str(root), "archive", BASE],
        check=True,
        capture_output=True,
    ).stdout
    with tarfile.open(fileobj=io.BytesIO(archive)) as tree:
        return {
            member.name: tree.extractfile(member).read()
            for member in tree
            if member.isfile()
        }


def source_errors(baseline: dict[str, bytes], migrated: dict[str, bytes]) -> list[str]:
    return [
        f"upstream source changed or missing: {name}"
        for name, contents in sorted(baseline.items())
        if name not in ROOT_EDITS and migrated.get(name) != contents
    ]


def read_frontmatter(path: Path) -> dict:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", path.read_text(), re.S)
    if not match:
        raise ValueError(f"{path.name}: missing YAML front matter")
    result = yaml.safe_load(match.group(1))
    if not isinstance(result, dict):
        raise ValueError(f"{path.name}: front matter must be a mapping")
    return result


def requirement_errors(
    requirement: dict, *, allow_unresolved_interaction: bool = False
) -> list[str]:
    if not isinstance(requirement, dict):
        return ["requirement must be a mapping"]
    errors = []
    if "id" not in requirement or requirement["id"] not in (None, ""):
        errors.append("migrated authoring requirement must retain an empty formal id")
    if requirement.get("status") != "DRAFT":
        errors.append("migration does not approve or publish upstream requirements")
    variation = "select" in requirement
    option = "option_of" in requirement
    classifiers = {
        "observability": {"OBSERVABLE", "AUDITABLE"},
        "mutability": {"IMMUTABLE", "EXTENSIBLE", "REPLACEABLE", "INAPPLICABLE"},
    }
    if option:
        if "level" in requirement:
            errors.append("an option inherits its level from the variation point")
    else:
        classifiers["level"] = {"REQUIRED", "RECOMMENDED"}
    if variation:
        if any(
            field in requirement
            for field in ("interaction", "test", "api_operation_id", "option_of")
        ):
            errors.append("a variation point has no interaction, test or API operation")
        minimum = requirement.get("select", {}).get("min")
        if not isinstance(minimum, int) or isinstance(minimum, bool) or minimum < 1:
            errors.append("a required source choice selects at least one option")
    elif not (allow_unresolved_interaction and requirement.get("interaction") is None):
        classifiers["interaction"] = INTERACTIONS
    for field, values in classifiers.items():
        value = requirement.get(field)
        if not isinstance(value, str) or value not in values:
            errors.append(f"invalid or missing {field}")
    statement = requirement.get("statement")
    if not isinstance(statement, str) or not statement.strip() or "\n" in statement:
        errors.append("requirement needs a single nonempty statement")
    if not variation and (
        not isinstance(requirement.get("test"), str) or not requirement["test"]
    ):
        errors.append("requirement needs a finite verification reference")
    if requirement.get(
        "observability"
    ) == "AUDITABLE" and "Evidence:" not in requirement.get("documentation", ""):
        errors.append("an auditable requirement must list its evidence")
    return errors


def binding_errors(
    file: str, requirement: dict, operation_ids: set[str], gaps: list[dict]
) -> list[str]:
    if requirement.get("interaction") != "SERVICE_API":
        return []
    operation_id = requirement.get("api_operation_id")
    if operation_id:
        return (
            []
            if operation_id in operation_ids
            else [f"unknown API operation: {operation_id}"]
        )
    for gap in gaps:
        if (
            gap.get("file") == file
            and gap.get("statement") == requirement.get("statement")
            and isinstance(gap.get("reason"), str)
            and gap["reason"].strip()
        ):
            return []
    return ["missing API binding without an exact, explained upstream gap"]


def anchors(path: Path) -> set[str]:
    text = path.read_text()
    result = set(re.findall(r"\bid=[\"']([^\"']+)[\"']", text))
    counts: Counter = Counter()
    for heading in re.findall(r"(?m)^#{1,6}\s+(.+)$", text):
        heading = re.sub(r"<[^>]+>", "", heading)
        heading = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        suffix = f"-{counts[heading]}" if counts[heading] else ""
        result.add(heading + suffix)
        counts[heading] += 1
    return result


def markdown_references(text: str) -> list[str]:
    return [
        angled or bare
        for angled, bare in re.findall(
            r"!?\[[^\]]*\]\((?:<([^\n>]+)>|([^\n)>]+?))"
            r'(?:\s+"[^"\n]*")?\)',
            text,
        )
    ]


def reference_errors(
    root: Path, origin: str, reference: str, root_relative: bool = False
) -> list[str]:
    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc or reference.startswith("govstack:"):
        return []
    start = root if root_relative else (root / origin).parent
    target = (start / unquote(parsed.path)).resolve() if parsed.path else root / origin
    if not target.is_relative_to(root.resolve()):
        return [f"reference leaves the repository: {reference}"]
    if not target.exists():
        return [f"missing reference: {reference}"]
    if (
        parsed.fragment
        and target.suffix == ".md"
        and unquote(parsed.fragment) not in anchors(target)
    ):
        return [f"missing reference fragment: {reference}"]
    return []


def validate_repository(root: Path = ROOT) -> tuple[list[str], dict]:
    errors = []
    baseline = baseline_files(root)
    migrated = {
        name: (root / name).read_bytes() for name in baseline if (root / name).is_file()
    }
    errors.extend(source_errors(baseline, migrated))
    for original, archive in {
        "README.md": "resources/history/upstream-repository-readme.md",
        ".gitbook.yaml": "resources/history/upstream-gitbook.yml",
    }.items():
        path = root / archive
        if not path.is_file() or path.read_bytes() != baseline[original]:
            errors.append(f"missing exact root-file archive: {archive}")
    try:
        metadata = yaml.safe_load((root / "metadata.yml").read_text())
        toc = yaml.safe_load((root / "toc.yml").read_text())["toc"]
        authors = yaml.safe_load((root / "authors.yml").read_text())["authors"]
        manifest = yaml.safe_load(
            (root / "resources/requirement-migration.yml").read_text()
        )
        projection = yaml.safe_load((root / "resources/api.yml").read_text())
    except (OSError, KeyError, TypeError, yaml.YAMLError) as error:
        return sorted(errors + [f"missing or malformed migration input: {error}"]), {}
    if metadata.get("urn") != "govstack:spec:bb:registries":
        errors.append(
            "existing GovStack Registries publication identity must be retained"
        )
    if manifest.get("source_commit") != BASE:
        errors.append(
            "migration manifest must identify the official upstream main commit"
        )
    if not authors or any(
        not item.get("name") or not item.get("roles") for item in authors
    ):
        errors.append("source authors and roles must be retained")
    if any(item.get("urn") for item in authors):
        errors.append(
            "this migration must not invent unverified person registration identifiers"
        )
    capabilities = {item["id"] for item in metadata.get("capabilities", [])}
    extensions = {item["id"] for item in metadata.get("extensions", [])}
    if extensions != {
        "database-views",
        "service-usage-statistics",
        "schema-templates",
        "statistics-api",
    }:
        errors.append(
            "optional whole functionalities must retain four independent extensions"
        )
    if any(item.get("requires") for item in metadata.get("extensions", [])):
        errors.append(
            "migration must not introduce dependencies between upstream optional functionalities"
        )
    operations = {
        operation["operationId"]
        for item in projection["paths"].values()
        for method, operation in item.items()
        if method in METHODS
    }
    gaps = manifest.get("binding_gaps", [])
    statements: Counter = Counter()
    requirements = []
    realised = set()
    used_extensions = set()
    for path in sorted((root / "requirements").glob("*.md")):
        file = path.relative_to(root).as_posix()
        try:
            document = read_frontmatter(path)
        except (ValueError, yaml.YAMLError) as error:
            errors.append(f"{file}: {error}")
            continue
        if not document.get("title") or not document.get("description"):
            errors.append(f"{file}: missing functionality title or description")
        realised.update(document.get("realises", []))
        if (
            not document.get("realises")
            or not set(document["realises"]) <= capabilities
        ):
            errors.append(f"{file}: unknown or missing capability references")
        conformance = document.get("conformance")
        if conformance == "EXTENSION":
            if document.get("extension") not in extensions:
                errors.append(f"{file}: unknown extension")
            used_extensions.add(document.get("extension"))
        elif conformance != "CORE" or document.get("extension"):
            errors.append(f"{file}: invalid core/extension classification")
        if not document.get("requirements"):
            errors.append(f"{file}: empty functionality")
        for requirement in document.get("requirements", []):
            unresolved_interaction = any(
                gap.get("file") == file
                and gap.get("statement") == requirement.get("statement")
                and gap.get("kind") == "unresolved-interaction"
                and gap.get("reason")
                for gap in gaps
            )
            errors.extend(
                f"{file}: {message}"
                for message in requirement_errors(
                    requirement,
                    allow_unresolved_interaction=bool(unresolved_interaction),
                )
            )
            errors.extend(
                f"{file}: {message}"
                for message in binding_errors(file, requirement, operations, gaps)
            )
            if requirement.get("applies_when") or requirement.get("applies_when_all"):
                errors.append(
                    f"{file}: migration must not invent option/extension conditions"
                )
            statement = requirement.get("statement", "")
            statements[(file, statement)] += 1
            requirements.append((file, requirement))
            for field in ("contract", "test"):
                if requirement.get(field):
                    errors.extend(
                        f"{file}: {message}"
                        for message in reference_errors(
                            root, file, requirement[field], root_relative=True
                        )
                    )
    if realised != capabilities:
        errors.append("every declared capability must be realised by a functionality")
    if used_extensions != extensions:
        errors.append("every optional extension must have a functionality")
    choices = {
        item["key"]: item
        for _, item in requirements
        if "select" in item and item.get("key")
    }
    keys = [item["key"] for _, item in requirements if item.get("key")]
    if len(keys) != len(set(keys)):
        errors.append("choice and option keys must be unique")
    for _, item in requirements:
        if "option_of" in item and item["option_of"] not in choices:
            errors.append("option references an unknown variation point")
    for key, point in choices.items():
        options = [item for _, item in requirements if item.get("option_of") == key]
        if len(options) < 2 or point["select"]["min"] > len(options):
            errors.append(f"{key}: invalid choice cardinality")
    mapped = set()
    mapping = manifest.get("legacy_requirements", {})
    expected_drs = {f"DRS-{number}" for number in range(1, 38)}
    if set(mapping) != expected_drs:
        errors.append("all 37 original DRS blocks must be mapped exactly once")
    all_mappings = {**mapping, **manifest.get("supplementary_requirements", {})}
    for source, record in all_mappings.items():
        if not record.get("targets"):
            errors.append(f"{source}: no mapped requirements")
        for target in record.get("targets", []):
            key = (target.get("file"), target.get("statement"))
            if statements[key] != 1:
                errors.append(
                    f"{source}: target does not resolve to exactly one requirement: {key}"
                )
            mapped.add(key)
    for key in statements:
        if key not in mapped:
            errors.append(f"unmapped requirement: {key}")
    for gap in gaps:
        key = (gap.get("file"), gap.get("statement"))
        if statements[key] != 1 or not gap.get("reason"):
            errors.append(
                f"unresolved-source gap does not identify an exact requirement: {key}"
            )
    active_pages = ["README.md"]
    for section, pages in toc.items():
        for name in pages:
            file = f"{section}/{name}"
            if not (root / file).is_file():
                errors.append(f"toc.yml: missing page {file}")
            else:
                active_pages.append(file)
    if {file for file, _ in requirements} - set(active_pages):
        errors.append("toc.yml must include every functionality file")
    for file in active_pages:
        text = (root / file).read_text()
        for reference in markdown_references(text):
            errors.extend(
                f"{file}: {message}"
                for message in reference_errors(root, file, reference)
            )
        if any(
            marker in text
            for marker in (
                "3.0.0-alpha.2",
                "consultation-retrieve",
                "x-govstack-digital-registries",
                "/.well-known/api-catalog",
            )
        ):
            errors.append(
                f"{file}: contains local-draft concepts outside the official baseline"
            )
    errors.extend(generate(root, check=True))
    protected_hash = hashlib.sha256()
    for name, contents in sorted(baseline.items()):
        if name not in ROOT_EDITS:
            protected_hash.update(name.encode() + b"\0" + contents)
    return sorted(set(errors)), {
        "source_commit": BASE,
        "protected_upstream_files": len(baseline) - len(ROOT_EDITS),
        "protected_content_digest": protected_hash.hexdigest(),
        "functionalities": len(set(file for file, _ in requirements)),
        "requirements": len(requirements),
        "legacy_drs_blocks": len(mapping),
        "extensions": len(extensions),
        "documented_source_gaps": len(gaps),
        "formal_requirement_ids_issued": 0,
    }


if __name__ == "__main__":
    import json

    failures, summary = validate_repository()
    if failures:
        print("\n".join(failures), file=sys.stderr)
        raise SystemExit(1)
    print(json.dumps(summary, indent=2))
