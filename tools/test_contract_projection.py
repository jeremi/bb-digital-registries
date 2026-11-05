#!/usr/bin/env python3
"""Regression tests for generated minimal concrete contract projections."""

from copy import deepcopy
from pathlib import Path
import tempfile
import unittest

from jsonschema import ValidationError
import yaml

try:
    from tools import project_contract
except (
    ModuleNotFoundError
):  # Direct `python tools/test_contract_projection.py` execution.
    import project_contract


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "api/openapi.yaml"
RETRIEVE_ONLY = ROOT / "api/examples/retrieve-only.openapi.yaml"
RETRIEVE_LOOKUP = ROOT / "api/examples/retrieve-lookup.openapi.yaml"


def operations(document):
    return {
        operation["operationId"]: (route, method, operation)
        for route, path_item in document["paths"].items()
        for method, operation in path_item.items()
        if method in project_contract.HTTP_METHODS
    }


class ContractProjectionTests(unittest.TestCase):
    def test_generated_profiles_match_the_unified_owner(self) -> None:
        expected = (
            (RETRIEVE_ONLY, ["retrieveRecord"]),
            (RETRIEVE_LOOKUP, ["retrieveRecord", "lookupRecord"]),
        )
        for output, operation_ids in expected:
            with self.subTest(output=output.name):
                self.assertRegex(output.read_text(), r"description: \|[-+]?\n")
                self.assertEqual(
                    yaml.safe_load(output.read_text()),
                    project_contract.project_contract(
                        SOURCE,
                        output,
                        operation_ids,
                        baseline_retrieve=True,
                    ),
                )

    def test_minimal_profiles_offer_only_the_selected_operations(self) -> None:
        expected = (
            (RETRIEVE_ONLY, {"retrieveRecord"}),
            (RETRIEVE_LOOKUP, {"retrieveRecord", "lookupRecord"}),
        )
        for contract, operation_ids in expected:
            with self.subTest(contract=contract.name):
                document = project_contract.load_document(contract)
                registry_operations = {
                    operation_id
                    for operation_id, (_, _, operation) in operations(document).items()
                    if project_contract.CONSULTATION_EXTENSION in operation
                    or project_contract.WRITE_EXTENSION in operation
                }
                self.assertEqual(registry_operations, operation_ids)
                self.assertEqual(
                    [
                        path
                        for path in document["paths"]
                        if path in project_contract.CORE_PATHS
                    ],
                    list(project_contract.CORE_PATHS),
                )
                self.assertNotIn("/v1/capabilities", document["paths"])
                self.assertFalse(
                    any(
                        project_contract.WRITE_EXTENSION in operation
                        for _, _, operation in operations(document).values()
                    )
                )
                retrieve = operations(document)["retrieveRecord"][2]
                self.assertNotIn(
                    "conditional-read",
                    retrieve[project_contract.CONSULTATION_EXTENSION].get(
                        "features", []
                    ),
                )
                self.assertNotIn("304", retrieve["responses"])
                self.assertEqual(
                    retrieve["responses"]["200"],
                    {"$ref": "#/components/responses/Record"},
                )
                self.assertNotIn(
                    {"$ref": "#/components/parameters/IfNoneMatch"},
                    retrieve["parameters"],
                )
                self.assertNotIn("StrongRecord", document["components"]["responses"])
                self.assertFalse(
                    document["components"]["headers"]["ETag"].get("required", False)
                )
                self.assertEqual(
                    document[project_contract.PROJECTION_EXTENSION]["preset"],
                    "baseline-retrieve",
                )
                self.assertIn(
                    "This generated baseline projection\nomits that feature",
                    document["info"]["description"],
                )
                project_contract.validate_contract(contract)

    def test_projection_preserves_closed_metadata_and_recursive_schemas(self) -> None:
        source = project_contract.load_document(SOURCE)
        projected = project_contract.project_contract(
            SOURCE, RETRIEVE_ONLY, ["retrieveRecord"]
        )
        source_operation = operations(source)["retrieveRecord"][2]
        projected_operation = operations(projected)["retrieveRecord"][2]
        self.assertEqual(projected_operation, source_operation)
        self.assertEqual(
            projected_operation[project_contract.CONSULTATION_EXTENSION],
            source_operation[project_contract.CONSULTATION_EXTENSION],
        )

        recursive_source = {
            "openapi": "3.1.2",
            "info": {"title": "Recursive Registry", "version": "1.0.0"},
            "paths": {
                "/records/{recordId}": {
                    "get": {
                        "operationId": "readTree",
                        "x-govstack-digital-registries": {
                            "registry": "https://registry.example/registries/trees",
                            "collection": "trees",
                            "capability": "retrieve",
                            "view": "tree-public",
                        },
                        "parameters": [
                            {
                                "name": "recordId",
                                "in": "path",
                                "required": True,
                                "schema": {
                                    "type": "string",
                                    "minLength": 1,
                                    "maxLength": 512,
                                },
                            }
                        ],
                        "responses": {
                            "200": {
                                "description": "Tree",
                                "content": {
                                    "application/json": {
                                        "schema": {"$ref": "#/components/schemas/Node"}
                                    }
                                },
                            }
                        },
                    }
                }
            },
            "components": {
                "schemas": {
                    "Node": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": ["name"],
                        "properties": {
                            "name": {"type": "string"},
                            "children": {
                                "type": "array",
                                "items": {"$ref": "#/components/schemas/Node"},
                            },
                        },
                    }
                }
            },
        }
        with tempfile.TemporaryDirectory() as directory:
            source_path = Path(directory) / "source.yaml"
            output_path = Path(directory) / "projected.yaml"
            source_path.write_text(yaml.safe_dump(recursive_source, sort_keys=False))
            recursive_projection = project_contract.project_contract(
                source_path, output_path, ["readTree"]
            )
            project_contract.validate_document(recursive_projection, output_path)
            node = recursive_projection["components"]["schemas"]["Node"]
            self.assertFalse(node["additionalProperties"])
            self.assertEqual(
                node["properties"]["children"]["items"]["$ref"],
                "#/components/schemas/Node",
            )

    def test_projection_keeps_subschema_parents_and_rebases_input_schema_refs(
        self,
    ) -> None:
        source = project_contract.load_document(SOURCE)
        operation = operations(source)["retrieveRecord"][2]
        operation[project_contract.CONSULTATION_EXTENSION]["inputSchema"] = (
            "./schemas/record.yaml#/$defs/Input"
        )
        operation["responses"]["200"] = {
            "description": "Record",
            "content": {
                "application/json": {
                    "schema": {"$ref": "#/components/schemas/Record/properties/data"}
                }
            },
        }
        with tempfile.TemporaryDirectory() as directory:
            source_path = Path(directory) / "api" / "openapi.yaml"
            output_path = Path(directory) / "api" / "examples" / "projection.yaml"
            source_path.parent.mkdir(parents=True)
            output_path.parent.mkdir(parents=True)
            source_path.write_text(yaml.safe_dump(source, sort_keys=False))
            projected = project_contract.project_contract(
                source_path, output_path, ["retrieveRecord"]
            )
        self.assertIn("Record", projected["components"]["schemas"])
        metadata = operations(projected)["retrieveRecord"][2][
            project_contract.CONSULTATION_EXTENSION
        ]
        self.assertEqual(metadata["inputSchema"], "../schemas/record.yaml#/$defs/Input")

    def test_validation_rejects_unknown_metadata_and_unbounded_record_ids(self) -> None:
        projected = project_contract.project_contract(
            SOURCE, RETRIEVE_ONLY, ["retrieveRecord"]
        )
        operation = operations(projected)["retrieveRecord"][2]
        operation[project_contract.CONSULTATION_EXTENSION]["unexpected"] = True
        with self.assertRaises(ValidationError):
            project_contract.validate_document(projected, RETRIEVE_ONLY)

        projected = project_contract.project_contract(
            SOURCE, RETRIEVE_ONLY, ["retrieveRecord"]
        )
        record_id = projected["components"]["schemas"]["RecordId"]
        record_id.pop("maxLength", None)
        with self.assertRaisesRegex(ValueError, "finite minLength and maxLength"):
            project_contract.validate_document(projected, RETRIEVE_ONLY)

    def test_validation_accepts_narrower_and_rejects_wider_cursor_bounds(self) -> None:
        output = ROOT / "api/examples/list-projection.openapi.yaml"
        projected = project_contract.project_contract(SOURCE, output, ["listRecords"])
        projected["components"]["schemas"]["Cursor"]["maxLength"] = 2048
        project_contract.validate_document(projected, output)
        projected["components"]["schemas"]["Cursor"]["maxLength"] = 4097
        with self.assertRaisesRegex(ValueError, "no wider than 4096"):
            project_contract.validate_document(projected, output)

    def test_projection_accepts_concrete_operation_ids_and_refuses_unknown_ones(
        self,
    ) -> None:
        source = project_contract.load_document(SOURCE)
        renamed = deepcopy(source)
        operations(renamed)["retrieveRecord"][2]["operationId"] = "retrievePerson"
        with tempfile.TemporaryDirectory() as directory:
            source_path = Path(directory) / "concrete.yaml"
            output_path = Path(directory) / "projection.yaml"
            source_path.write_text(yaml.safe_dump(renamed, sort_keys=False))
            projected = project_contract.project_contract(
                source_path, output_path, ["retrievePerson"]
            )
            self.assertEqual(
                {
                    operation_id
                    for operation_id, (_, _, operation) in operations(projected).items()
                    if project_contract.CONSULTATION_EXTENSION in operation
                },
                {"retrievePerson"},
            )
            with self.assertRaisesRegex(ValueError, "Unknown operationId"):
                project_contract.project_contract(
                    source_path, output_path, ["retrieveRecord"]
                )

    def test_validation_accepts_independent_contracts_with_local_recursive_refs(
        self,
    ) -> None:
        contract = {
            "openapi": "3.1.2",
            "info": {"title": "Independent Registry", "version": "1.0.0"},
            "paths": {
                "/records/{recordId}": {
                    "get": {
                        "operationId": "retrieveIndependentRecord",
                        project_contract.CONSULTATION_EXTENSION: {
                            "registry": "urn:example:registry:independent",
                            "collection": "records",
                            "capability": "retrieve",
                            "view": "record-public",
                        },
                        "parameters": [
                            {
                                "name": "recordId",
                                "in": "path",
                                "required": True,
                                "schema": {
                                    "type": "string",
                                    "minLength": 1,
                                    "maxLength": 512,
                                    "pattern": "^[^/?#\\s]+$",
                                },
                            }
                        ],
                        "responses": {
                            "200": {
                                "description": "Record",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "./domain.yaml#/$defs/Record"
                                        }
                                    }
                                },
                            }
                        },
                    }
                }
            },
        }
        domain = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$defs": {
                "Record": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["recordId", "data"],
                    "properties": {
                        "recordId": {"type": "string"},
                        "data": {"$ref": "#/$defs/Node"},
                    },
                },
                "Node": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {"child": {"$ref": "#/$defs/Node"}},
                },
            },
        }
        with tempfile.TemporaryDirectory() as directory:
            contract_path = Path(directory) / "contract.yaml"
            domain_path = Path(directory) / "domain.yaml"
            contract_path.write_text(yaml.safe_dump(contract, sort_keys=False))
            domain_path.write_text(yaml.safe_dump(domain, sort_keys=False))
            project_contract.validate_contract(contract_path)

            malformed = deepcopy(contract)
            operation = operations(malformed)["retrieveIndependentRecord"][2]
            operation[project_contract.CONSULTATION_EXTENSION]["unexpected"] = True
            contract_path.write_text(yaml.safe_dump(malformed, sort_keys=False))
            with self.assertRaises(ValidationError):
                project_contract.validate_contract(contract_path)

            create_contract = {
                "openapi": "3.1.2",
                "info": {"title": "Independent Create API", "version": "1.0.0"},
                "paths": {
                    "/records": {
                        "post": {
                            "operationId": "createIndependentRecord",
                            project_contract.WRITE_EXTENSION: {
                                "registry": "urn:example:registry:independent",
                                "collection": "records",
                                "capability": "create",
                                "inputSchema": "./domain.yaml#/$defs/Record",
                                "idempotencyReplayWindow": 86400,
                            },
                            "requestBody": {
                                "required": True,
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "./domain.yaml#/$defs/Record"
                                        }
                                    }
                                },
                            },
                            "responses": {"201": {"description": "Created"}},
                        }
                    }
                },
            }
            contract_path.write_text(yaml.safe_dump(create_contract, sort_keys=False))
            project_contract.validate_contract(contract_path)

            operation = operations(create_contract)["createIndependentRecord"][2]
            operation[project_contract.WRITE_EXTENSION]["unexpected"] = True
            contract_path.write_text(yaml.safe_dump(create_contract, sort_keys=False))
            with self.assertRaises(ValidationError):
                project_contract.validate_contract(contract_path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
