#!/usr/bin/env python3
"""Regression tests for a migration that preserves the official upstream baseline."""

from __future__ import annotations

import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from openapi_spec_validator import validate
import yaml

from build_api_projection import ALIASES, METHODS, build_projection, projection_errors
from validate_migration import (
    ROOT,
    binding_errors,
    markdown_references,
    read_frontmatter,
    requirement_errors,
    source_errors,
    validate_repository,
)


def contract(paths: dict, security_name: str = "apiKey") -> dict:
    return {
        "openapi": "3.0.0",
        "info": {"title": "Upstream fixture", "version": "1.3.0"},
        "paths": paths,
        "components": {
            "schemas": {"Record": {"type": "object"}},
            "securitySchemes": {
                security_name: {"type": "apiKey", "in": "header", "name": "X-Key"}
            },
        },
    }


class ProjectionTests(unittest.TestCase):
    def setUp(self):
        self.data = contract(
            {
                "/records": {
                    "get": {
                        "operationId": "read",
                        "security": [{"apiKey": []}],
                        "responses": {
                            "200": {
                                "description": "Record",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "#/components/schemas/Record"
                                        }
                                    }
                                },
                            }
                        },
                    }
                }
            }
        )
        self.database = contract(
            {
                "/database/{id}": {
                    "get": {"responses": {"200": {"description": "Schema"}}},
                    "delete": {"responses": {"200": {"description": "Deleted"}}},
                },
                "/database/modify": {
                    "post": {"responses": {"200": {"description": "Saved"}}}
                },
                "/databases": {"get": {"responses": {"200": {"description": "List"}}}},
            }
        )

    def test_projection_does_not_mutate_source_documents(self):
        before = copy.deepcopy((self.data, self.database))
        build_projection(self.data, self.database)
        self.assertEqual((self.data, self.database), before)

    def test_projection_preserves_existing_ids_and_names_only_four_missing_operations(
        self,
    ):
        result = build_projection(self.data, self.database)
        self.assertEqual(result["paths"]["/records"]["get"]["operationId"], "read")
        for (method, path), alias in ALIASES.items():
            self.assertEqual(result["paths"][path][method]["operationId"], alias)
        self.assertEqual(projection_errors(result, self.data, self.database), [])

    def test_refs_and_security_keep_their_source_document_context(self):
        result = build_projection(self.data, self.database)
        operation = result["paths"]["/records"]["get"]
        schema = operation["responses"]["200"]["content"]["application/json"]["schema"]
        self.assertEqual(
            schema["$ref"], "upstream-api/data-api.json#/components/schemas/Record"
        )
        self.assertEqual(operation["security"], [{"data__apiKey": []}])
        self.assertEqual(
            result["components"]["securitySchemes"]["data__apiKey"],
            {"$ref": "upstream-api/data-api.json#/components/securitySchemes/apiKey"},
        )

    def test_projection_rejects_path_collisions_instead_of_overwriting(self):
        self.database["paths"]["/records"] = {"get": {"responses": {}}}
        with self.assertRaisesRegex(ValueError, "overlapping path"):
            build_projection(self.data, self.database)

    def test_projection_rejects_unexpected_missing_operation_ids(self):
        del self.data["paths"]["/records"]["get"]["operationId"]
        with self.assertRaisesRegex(ValueError, "unassigned upstream operation"):
            build_projection(self.data, self.database)

    def test_projection_guard_detects_changed_endpoints_schemas_and_permissions(self):
        for mutation in ("endpoint", "schema", "security"):
            result = build_projection(self.data, self.database)
            if mutation == "endpoint":
                result["paths"]["/invented"] = result["paths"].pop("/records")
            elif mutation == "schema":
                result["paths"]["/records"]["get"]["responses"]["200"][
                    "description"
                ] = "Changed"
            else:
                result["paths"]["/records"]["get"]["security"] = []
            with self.subTest(mutation=mutation):
                self.assertTrue(projection_errors(result, self.data, self.database))


class MigrationValidationTests(unittest.TestCase):
    def requirement(self, **changes):
        return {
            "id": None,
            "status": "DRAFT",
            "level": "REQUIRED",
            "observability": "OBSERVABLE",
            "mutability": "EXTENSIBLE",
            "interaction": "SERVICE_API",
            "api_operation_id": "read",
            "statement": "The Digital Registry reads a permitted record.",
            "test": "resources/testing.md#drs-33",
            **changes,
        }

    def test_authoring_draft_preserves_null_ids_and_explicit_classifiers(self):
        self.assertEqual(requirement_errors(self.requirement()), [])
        for mutation in (
            {"id": "33"},
            {"status": "PUBLISHED"},
            {"level": "OPTIONAL"},
            {"interaction": "UNKNOWN"},
            {"statement": ""},
        ):
            with self.subTest(mutation=mutation):
                self.assertTrue(requirement_errors(self.requirement(**mutation)))

    def test_optional_nested_feature_stays_nonblocking(self):
        self.assertEqual(requirement_errors(self.requirement(level="RECOMMENDED")), [])

    def test_api_binding_must_exist_or_have_an_exact_explained_source_gap(self):
        req = self.requirement()
        self.assertEqual(binding_errors("requirements/read.md", req, {"read"}, []), [])
        self.assertTrue(binding_errors("requirements/read.md", req, set(), []))
        req["api_operation_id"] = None
        gap = {
            "file": "requirements/read.md",
            "statement": req["statement"],
            "reason": "Upstream has no published operation for this behavior.",
        }
        self.assertEqual(binding_errors("requirements/read.md", req, set(), [gap]), [])
        self.assertTrue(binding_errors("requirements/other.md", req, set(), [gap]))
        self.assertTrue(
            binding_errors("requirements/read.md", req, set(), [{**gap, "reason": ""}])
        )

    def test_required_source_choice_is_a_variation_with_unlevelled_options(self):
        variation = self.requirement(key="sharing-method", select={"min": 1})
        for field in ("interaction", "test", "api_operation_id"):
            variation.pop(field)
        self.assertEqual(requirement_errors(variation), [])
        option = self.requirement(
            key="sharing-email",
            option_of="sharing-method",
            interaction="USER_INTERFACE",
        )
        option.pop("level")
        option.pop("api_operation_id")
        self.assertEqual(requirement_errors(option), [])
        self.assertTrue(requirement_errors({**option, "level": "REQUIRED"}))
        self.assertTrue(requirement_errors({**variation, "interaction": "INTERNAL"}))

    def test_unknown_webhook_direction_is_an_explicit_draft_exception(self):
        unresolved = self.requirement(interaction=None)
        unresolved.pop("api_operation_id")
        self.assertTrue(requirement_errors(unresolved))
        self.assertEqual(
            requirement_errors(unresolved, allow_unresolved_interaction=True), []
        )
        self.assertTrue(
            requirement_errors(
                {**unresolved, "interaction": "MADE_UP"},
                allow_unresolved_interaction=True,
            )
        )

    def test_auditable_requirement_lists_its_evidence(self):
        req = self.requirement(observability="AUDITABLE")
        self.assertTrue(requirement_errors(req))
        self.assertEqual(
            requirement_errors(
                {**req, "documentation": "Evidence: Versioned model evidence."}
            ),
            [],
        )

    def test_source_gap_cannot_hide_a_fabricated_operation_identifier(self):
        req = self.requirement(api_operation_id="invented")
        gap = {
            "file": "requirements/read.md",
            "statement": req["statement"],
            "reason": "Not in source.",
        }
        self.assertTrue(binding_errors("requirements/read.md", req, set(), [gap]))

    def test_angle_bracket_link_destination_may_contain_parentheses(self):
        text = (
            "![Components](<../assets/image (1) (1).png>) and [Scope](scope.md#covered)"
        )
        self.assertEqual(
            markdown_references(text),
            ["../assets/image (1) (1).png", "scope.md#covered"],
        )

    def test_link_destination_may_be_followed_by_a_title(self):
        text = '[x](<a b> "t") and [y](a.md "t")'
        self.assertEqual(markdown_references(text), ["a b", "a.md"])

    def test_source_guard_detects_deletion_changes_and_unapproved_root_edits(self):
        baseline = {
            "spec/source.md": b"Original",
            "api/contract.json": b"{}",
            "README.md": b"Old",
        }
        migrated = {**baseline, "README.md": b"New"}
        self.assertEqual(source_errors(baseline, migrated), [])
        for candidate in (
            {**migrated, "spec/source.md": b"Reworded"},
            {
                key: value
                for key, value in migrated.items()
                if not key.startswith("api/")
            },
        ):
            self.assertTrue(source_errors(baseline, candidate))


class RepositoryIntegrationTests(unittest.TestCase):
    def test_checked_in_migration_preserves_official_upstream_and_all_source_ids(self):
        errors, summary = validate_repository()
        self.assertEqual(errors, [])
        self.assertEqual(
            summary["source_commit"], "8588a219df9a8406e66c4392d0bef664b34e4e30"
        )
        self.assertEqual(summary["legacy_drs_blocks"], 37)
        self.assertEqual(summary["extensions"], 4)
        self.assertEqual(summary["formal_requirement_ids_issued"], 0)
        self.assertGreater(summary["protected_upstream_files"], 100)

    def test_no_requirement_binds_an_example_registry_operation(self):
        projection = yaml.safe_load((ROOT / "resources/api.yml").read_text())
        paths = {
            operation["operationId"]: path
            for path, item in projection["paths"].items()
            for method, operation in item.items()
            if method in METHODS
        }
        bound = [
            (file.name, requirement["api_operation_id"])
            for file in sorted((ROOT / "requirements").glob("*.md"))
            for requirement in read_frontmatter(file)["requirements"]
            if requirement.get("api_operation_id")
        ]
        example_bound = [
            (name, operation_id)
            for name, operation_id in bound
            if operation_id.startswith("GDB-MCTS-")
            or paths[operation_id].startswith("/data/mcts/")
        ]
        self.assertEqual(example_bound, [])

    def test_projection_validates_through_its_authoring_location(self):
        path = ROOT / "resources/api.yml"
        validate(yaml.safe_load(path.read_bytes()), base_uri=path.as_uri())

    def test_recorded_source_contract_failures_are_unchanged_and_not_hidden(self):
        from report_contracts import report

        actual = report()
        recorded = json.loads((ROOT / "resources/contract-validation.json").read_text())
        self.assertEqual(actual, recorded)
        failures = [
            item
            for item in actual["original_contracts"]
            if not item["baseline"]["valid"]
        ]
        self.assertEqual(len(failures), 2)
        self.assertTrue(
            all(item["bytes_unchanged"] for item in actual["original_contracts"])
        )
        self.assertTrue(
            all(
                item["baseline"] == item["migrated"]
                for item in actual["original_contracts"]
            )
        )
        self.assertTrue(actual["authoring_projection"]["valid"])

    def test_cli_reports_verified_source_and_exits_without_errors(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "tools/validate_migration.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertEqual(json.loads(result.stdout)["legacy_drs_blocks"], 37)

    def test_cli_rejects_changed_upstream_bytes(self):
        scratch = ROOT / ".verification-tmp"
        scratch.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=scratch) as directory:
            fixture = Path(directory) / "repository"
            shutil.copytree(
                ROOT,
                fixture,
                ignore=shutil.ignore_patterns(
                    ".git", ".venv", ".verification-tmp", "__pycache__", ".ruff_cache"
                ),
            )
            git_dir = subprocess.run(
                [
                    "git",
                    "--no-optional-locks",
                    "-C",
                    str(ROOT),
                    "rev-parse",
                    "--absolute-git-dir",
                ],
                capture_output=True,
                text=True,
                check=True,
            ).stdout.strip()
            (fixture / ".git").write_text(f"gitdir: {git_dir}\n")
            source = fixture / "spec/6-functional-requirements.md"
            source.write_bytes(source.read_bytes() + b"\nChanged upstream source.\n")
            result = subprocess.run(
                [sys.executable, str(fixture / "tools/validate_migration.py")],
                cwd=fixture,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(
                "upstream source changed or missing: spec/6-functional-requirements.md",
                result.stderr,
            )
            self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
