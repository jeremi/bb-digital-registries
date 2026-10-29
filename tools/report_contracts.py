#!/usr/bin/env python3
"""Record paired validation without repairing divergent upstream contract copies."""

from __future__ import annotations

import hashlib
from importlib.metadata import version
import json
from pathlib import Path
import sys

from openapi_spec_validator import validate
import yaml

from build_api_projection import BASE, SOURCES
from validate_migration import baseline_files

ROOT = Path(__file__).resolve().parents[1]


def validation_result(contents: bytes, path: Path) -> dict:
    try:
        validate(yaml.safe_load(contents), base_uri=path.resolve().as_uri())
    except Exception as error:
        # Validator failures are evidence in the paired report, not ignored successes.
        message = str(error).split(" within ", 1)[0].splitlines()[0]
        return {
            "valid": False,
            "error_type": type(error).__name__,
            "summary": message.replace(str(ROOT), "${REPOSITORY}")[:240],
        }
    return {"valid": True}


def report(root: Path = ROOT) -> dict:
    baseline = baseline_files(root)
    originals = sorted(
        name
        for name in baseline
        if name.startswith("api/") and name.endswith((".json", ".yaml"))
    )
    originals += [source for source, _ in SOURCES.values()]
    entries = []
    for name in originals:
        before = baseline[name]
        after = (root / name).read_bytes()
        entries.append(
            {
                "file": name,
                "sha256": hashlib.sha256(before).hexdigest(),
                "bytes_unchanged": before == after,
                "baseline": validation_result(before, root / name),
                "migrated": validation_result(after, root / name),
            }
        )
    projection = validation_result(
        (root / "resources/api.yml").read_bytes(), root / "resources/api.yml"
    )
    return {
        "source_commit": BASE,
        "validator": f"openapi-spec-validator {version('openapi-spec-validator')}",
        "original_contracts": entries,
        "authoring_projection": projection,
    }


if __name__ == "__main__":
    result = report()
    if not all(
        item["bytes_unchanged"] and item["baseline"] == item["migrated"]
        for item in result["original_contracts"]
    ):
        raise SystemExit("Upstream contract bytes or validation results changed.")
    if not result["authoring_projection"]["valid"]:
        raise SystemExit("The generated authoring projection does not validate.")
    target = ROOT / "resources/contract-validation.json"
    if "--check" in sys.argv[1:]:
        if json.loads(target.read_text()) != result:
            raise SystemExit("Recorded paired contract validation is stale.")
    else:
        target.write_text(json.dumps(result, indent=2) + "\n")
    print(
        "Original contract bytes and paired validation outcomes are unchanged; authoring projection validates."
    )
