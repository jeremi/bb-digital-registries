#!/usr/bin/env python3
"""Validate the current Consultation contracts and their concrete examples.

Run from the repository root:
  uv run --with-requirements tools/requirements-api.txt python tools/validate_consultation.py

This checks artifacts and schema acceptance/rejection, not deployed authorization,
source matching, cursor integrity/expiry, bounded work, or disclosure behavior.
It reads only explicitly named current artifacts and their local dependencies.
"""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urldefrag, urljoin, urlparse

from jsonschema import Draft202012Validator, FormatChecker
from openapi_spec_validator import validate
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012
import yaml


API = Path(__file__).resolve().parents[1] / "api"
CANONICAL = API / "openapi.yaml"
BUSINESS = API / "examples/business-registry.openapi.yaml"
BINDING = API / "examples/business-registry.schema.json"
HOUSEHOLD = API / "examples/household-registry.openapi.yaml"
BIRTH = API / "examples/birth-registration.openapi.yaml"
RELATIONSHIPS = API / "examples/relationship-examples.schema.json"
OPENAPI_DOCUMENTS = (CANONICAL, BUSINESS, HOUSEHOLD, BIRTH)
SCHEMA_DOCUMENTS = (BINDING, RELATIONSHIPS)
DOCUMENTS: dict[str, dict] = {}


def load_local(uri: str) -> Resource:
    """Resolve shipped references without network access or legacy inspection."""
    parsed = urlparse(uri)
    if parsed.scheme != "file" or parsed.netloc:
        raise ValueError(f"Only local contract references are permitted: {uri}")
    source = Path(unquote(parsed.path)).resolve()
    if not source.is_relative_to(API) or source.is_relative_to(API / "legacy"):
        raise ValueError("Contract reference leaves current API artifacts")
    if uri not in DOCUMENTS:
        DOCUMENTS[uri] = yaml.safe_load(source.read_text())
    return Resource.from_contents(DOCUMENTS[uri], default_specification=DRAFT202012)


REGISTRY = Registry(retrieve=load_local)


def document(path: Path) -> dict:
    return load_local(path.as_uri()).contents


def validator(path: Path, pointer: str) -> Draft202012Validator:
    return Draft202012Validator(
        {"$ref": path.as_uri() + "#" + pointer},
        registry=REGISTRY,
        format_checker=FormatChecker(),
    )


def pointer_key(key: str) -> str:
    return str(key).replace("~", "~0").replace("/", "~1")


def nodes(value, pointer=""):
    if isinstance(value, dict):
        yield pointer, value
        for key, child in value.items():
            yield from nodes(child, pointer + "/" + pointer_key(key))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from nodes(child, pointer + "/" + str(index))


def resolve_object(path: Path, value: dict) -> tuple[Path, dict]:
    """Resolve OpenAPI Reference Objects while preserving the correct file base."""
    while "$ref" in value:
        reference, fragment = urldefrag(value["$ref"])
        path = (path.parent / reference).resolve() if reference else path
        value = document(path)
        for token in fragment.lstrip("/").split("/") if fragment else []:
            value = value[token.replace("~1", "/").replace("~0", "~")]
    return path, value


class ConsultationContractTests(unittest.TestCase):
    def test_required_format_checkers_are_available(self):
        self.assertIn("iri", FormatChecker().checkers,
                      "Install tools/requirements-api.txt so Registry IRI formats are asserted")

    def test_openapi_and_local_schema_documents(self):
        for path in OPENAPI_DOCUMENTS:
            with self.subTest(path=path.name):
                validate(document(path), base_uri=path.as_uri())
        for path in SCHEMA_DOCUMENTS:
            Draft202012Validator.check_schema(document(path))
        for schema in document(CANONICAL)["components"]["schemas"].values():
            Draft202012Validator.check_schema(schema)

    def test_all_inline_schema_and_media_examples(self):
        count = 0
        for path in (*OPENAPI_DOCUMENTS, *SCHEMA_DOCUMENTS):
            for pointer, node in nodes(document(path)):
                if isinstance(node.get("examples"), list):
                    for example in node["examples"]:
                        with self.subTest(file=path.name, pointer=pointer):
                            validator(path, pointer).validate(example)
                        count += 1
                if "schema" in node:
                    examples = []
                    if "example" in node:
                        examples.append(node["example"])
                    if isinstance(node.get("examples"), dict):
                        examples.extend(e["value"] for e in node["examples"].values() if "value" in e)
                    for example in examples:
                        with self.subTest(file=path.name, pointer=pointer):
                            validator(path, pointer + "/schema").validate(example)
                        count += 1
        self.assertGreater(count, 30, "The current request, response and domain examples must be exercised")

    def test_published_exchanges_use_actual_operation_schemas(self):
        spec = document(BUSINESS)
        operations = {
            operation["operationId"]: (path, method, operation)
            for path, item in spec["paths"].items()
            for method, operation in item.items()
            if method in ("get", "post")
        }
        exchanges = json.loads((API / "examples/consultation-exchanges.json").read_text())["exchanges"]
        for exchange in exchanges:
            path, method, operation = operations[exchange["operationId"]]
            base = "/paths/" + pointer_key(path) + "/" + method
            with self.subTest(exchange=exchange["name"]):
                if "request" in exchange:
                    validator(BUSINESS, base + "/requestBody/content/application~1json/schema").validate(exchange["request"])
                response_path, response = resolve_object(BUSINESS, operation["responses"][str(exchange["status"])])
                media = "application/json" if exchange["status"] < 400 else "application/problem+json"
                schema = response["content"][media]["schema"]
                Draft202012Validator(
                    {**schema, "$ref": urljoin(response_path.as_uri(), schema["$ref"])},
                    registry=REGISTRY,
                    format_checker=FormatChecker(),
                ).validate(exchange["response"])
                if exchange["status"] >= 400:
                    self.assertEqual(exchange["response"]["status"], exchange["status"])

    def test_exact_selectors_reject_incomplete_or_undeclared_keys(self):
        check = validator(BINDING, "/$defs/BusinessLookupRequest")
        valid = {"selector": "byJurisdictionNumber", "values": {"jurisdictionCode": "AA", "localNumber": "00000042"}}
        check.validate(valid)
        invalid = [
            {"selector": "byJurisdictionNumber", "values": {"localNumber": "00000042"}},
            {"selector": "byJurisdictionNumber", "values": {"jurisdictionCode": "AA", "localNumber": 42}},
            {"selector": "byRegistrationNumber", "values": {"registrationNumber": "br-000042"}},
            {"selector": "byRegistrationNumber", "values": {"registrationNumber": "BR-000042\n"}},
            {"selector": "byJurisdictionNumber", "values": {"jurisdictionCode": "AA\n", "localNumber": "00000042"}},
            {"selector": "byJurisdictionNumber", "values": {"jurisdictionCode": "AA", "localNumber": "00000042\n"}},
            {"selector": "byRegistrationNumber", "values": valid["values"]},
            {"selector": "byRegistrationNumber", "values": {"registrationNumber": "BR-000042", "legalName": "Example Ltd"}},
            {"selector": "byUnknownKey", "values": {"key": "42"}},
            {"selector": "byRegistrationNumber", "values": {}},
            {**valid, "pageSize": 1},
        ]
        for value in invalid:
            with self.subTest(value=value):
                self.assertFalse(check.is_valid(value))
        # A different deployment can bind a context-only selector with values:{}.
        validator(CANONICAL, "/components/schemas/LookupRequest").validate({"selector": "byVerifiedCaller", "values": {}})

    def test_declared_search_rejects_unbounded_and_undeclared_inputs(self):
        check = validator(BINDING, "/$defs/BusinessSearchRequest")
        valid = {"search": "byRegistrationStatus", "criteria": {"registrationStatus": "DISSOLVED"}}
        check.validate(valid)
        invalid = [
            {**valid, "filter": "registrationStatus eq 'DISSOLVED'"},
            {**valid, "sort": "recordId"},
            {**valid, "search": "anyExpression"},
            {**valid, "criteria": {"registrationStatus": "DISSOLVED", "legalName": "Example Ltd"}},
            {**valid, "criteria": {"registrationStatus": None}},
            {**valid, "pageSize": 0},
            {**valid, "pageSize": 101},
            {**valid, "cursor": ""},
            {**valid, "cursor": "opaqueCursor\n"},
            {**valid, "cursor": None},
        ]
        for value in invalid:
            with self.subTest(value=value):
                self.assertFalse(check.is_valid(value))

        self.assertFalse(validator(CANONICAL, "/components/schemas/Sort").is_valid("recordId\n"))

    def test_fixed_view_and_additive_envelope(self):
        check = validator(BINDING, "/$defs/BusinessRecord")
        record = {"recordId": "r_42", "data": {"legalName": "Example Ltd", "registrationStatus": "DISSOLVED"}}
        check.validate(record)
        check.validate({**record, "additionalEnvelopeMetadata": "future declared field"})
        self.assertFalse(check.is_valid({**record, "recordId": "r_42\n"}))
        for data in ({"registrationStatus": "DISSOLVED"}, {**record["data"], "undeclaredPrivateField": "value"}, {**record["data"], "legalName": 42}):
            self.assertFalse(check.is_valid({**record, "data": data}))

    def test_custom_methods_preserve_opaque_identifier_routes(self):
        bindings = ((CANONICAL, "records"), (BUSINESS, "businesses"),
                    (HOUSEHOLD, "households"), (BIRTH, "birth-registrations"))
        for contract, collection in bindings:
            spec = document(contract)
            collection_path = "/v1/" + collection
            retrieve_path = collection_path + "/{recordId}"
            self.assertEqual(spec["servers"][0]["url"], "https://{gatewayHost}")
            self.assertIn("get", spec["paths"][retrieve_path])
            for source_id in ("lookup", "lookups", "search"):
                with self.subTest(contract=contract.name, recordId=source_id):
                    validator(CANONICAL, "/components/schemas/RecordId").validate(source_id)
                    requested_path = collection_path + "/" + source_id
                    # Compare path templates before method dispatch: literal paths can
                    # shadow a Retrieve template even when they only declare POST.
                    matches = []
                    for path in spec["paths"]:
                        pattern = "".join("[^/]+" if part.startswith("{") else re.escape(part)
                                          for part in re.split(r"(\{[^{}]+\})", path))
                        if re.fullmatch(pattern, requested_path):
                            matches.append(path)
                    self.assertEqual(matches, [retrieve_path])
            if contract in (CANONICAL, BUSINESS):
                for suffix in ("lookup", "search"):
                    self.assertIn("post", spec["paths"][collection_path + ":" + suffix])
        concrete_operations = [operation["operationId"]
                               for contract in (BUSINESS, HOUSEHOLD, BIRTH)
                               for path, item in document(contract)["paths"].items()
                               if path.startswith("/v1/")
                               for method, operation in item.items()
                               if method in ("get", "post")]
        self.assertEqual(len(concrete_operations), len(set(concrete_operations)),
                         "Collection operations must remain unique when composing these examples into one API")

    def test_page_completion_and_bounds(self):
        check = validator(BINDING, "/$defs/BusinessPage")
        check.validate({"items": [], "pageInfo": {"nextCursor": "opaqueContinuation"}})
        check.validate({"items": [], "pageInfo": {"nextCursor": None, "total": 0}})
        for page_info in ({}, {"nextCursor": ""}, {"nextCursor": "invalid+cursor"},
                          {"nextCursor": "opaqueCursor\n"},
                          {"nextCursor": "a" * 4097}, {"hasMore": False},
                          {"nextCursor": None, "total": 1.5}):
            self.assertFalse(check.is_valid({"items": [], "pageInfo": page_info}))
        item = {"recordId": "r_42", "data": {"legalName": "Example Ltd", "registrationStatus": "DISSOLVED"}}
        self.assertFalse(check.is_valid({"items": [item] * 101, "pageInfo": {"nextCursor": None}}))
        exchanges = json.loads((API / "examples/consultation-exchanges.json").read_text())["exchanges"]
        search_id = document(BUSINESS)["paths"]["/v1/businesses:search"]["post"]["operationId"]
        pages = [e for e in exchanges if e["operationId"] == search_id]
        first, final = pages
        self.assertEqual(first["response"]["items"], [])
        self.assertEqual(first["response"]["pageInfo"]["nextCursor"], final["request"]["cursor"])
        self.assertEqual(first["request"]["search"], final["request"]["search"])
        self.assertEqual(first["request"]["criteria"], final["request"]["criteria"])
        self.assertNotIn("pageSize", final["request"], "Example must exercise omission reusing the bound size")
        self.assertLessEqual(len(final["response"]["items"]), first["request"]["pageSize"])
        self.assertIsNone(final["response"]["pageInfo"]["nextCursor"])

    def test_error_examples_match_http_status_and_namespace(self):
        for name, response in document(CANONICAL)["components"]["responses"].items():
            media = response.get("content", {}).get("application/problem+json")
            if not media:
                continue
            examples = [media["example"]] if "example" in media else [e["value"] for e in media["examples"].values()]
            for example in examples:
                with self.subTest(response=name):
                    self.assertTrue(example["type"].startswith("https://govstack.global/problems/digital-registries/"))
                    self.assertNotIn("code", example)
                    self.assertNotIn("timestamp", example)
                    for item in document(CANONICAL)["paths"].values():
                        for method, operation in item.items():
                            if method not in ("get", "post"):
                                continue
                            for status, declared in operation["responses"].items():
                                if declared.get("$ref") == "#/components/responses/" + name:
                                    self.assertEqual(example["status"], int(status))

    def test_relationship_fixtures_use_concrete_schemas(self):
        fixtures = json.loads((API / "examples/relationship-exchanges.json").read_text())["examples"]
        for fixture in fixtures:
            with self.subTest(fixture=fixture["name"]):
                validator(RELATIONSHIPS, "/$defs/" + fixture["schema"]).validate(fixture["value"])
                if "contract" in fixture:
                    contract = API / "examples" / fixture["contract"]
                    self.assertIn(contract, OPENAPI_DOCUMENTS)
                    matches = [(path, method, operation)
                               for path, item in document(contract)["paths"].items()
                               for method, operation in item.items()
                               if method in ("get", "post") and operation["operationId"] == fixture["operationId"]]
                    self.assertEqual(len(matches), 1)
                    path, method, operation = matches[0]
                    status = str(fixture["status"])
                    media = operation["responses"][status]["content"]["application/json"]
                    pointer = "/paths/" + pointer_key(path) + "/" + method + "/responses/" + status + "/content/application~1json/schema"
                    validator(contract, pointer).validate(fixture["value"])
                    self.assertEqual(media["example"], fixture["value"], "Operation example and response fixture must agree")
        for contract, collection in ((HOUSEHOLD, "households"), (BIRTH, "birth-registrations")):
            operation = document(contract)["paths"]["/v1/" + collection + "/{recordId}"]["get"]
            parameters = [resolve_object(contract, p)[1] for p in operation["parameters"]]
            self.assertFalse(any(p["in"] == "query" for p in parameters), "These Retrieve contracts serve their declared fixed views")

    def test_reference_context_rejects_ambiguous_or_conflicting_targets(self):
        fixed = validator(RELATIONSHIPS, "/$defs/IndividualReference")
        explicit = validator(RELATIONSHIPS, "/$defs/UnscopedRecordReference")
        target = "https://registry.example/registries/individuals"
        fixed.validate({"recordId": "person_42"})
        fixed.validate({"recordId": "person_42", "registryId": target})
        explicit.validate({"recordId": "person_42", "registryId": target})
        explicit.validate({"recordId": "r_7", "registryId": "urn:example:registry:external"})
        explicit.validate({"recordId": "r_7", "registryId": "urn:example:registre:état-civil"})
        for value in ({"recordId": "person_42", "registryId": "https://registry.example/registries/other"},
                      {"registryId": target}, {"recordId": ""},
                      {"recordId": "person_42", "href": "https://registry.example/person_42"}):
            with self.subTest(fixed_target=value):
                self.assertFalse(fixed.is_valid(value))
        for value in ({"recordId": "person_42"}, {"registryId": target},
                      {"recordId": "person_42", "registryId": "/registries/individuals"},
                      {"recordId": "person_42", "registryId": "urn:example:invalid registry"},
                      {"recordId": "person_42", "registryId": "https://registry.example/%invalid"},
                      {"recordId": "person_42", "registryId": 42}):
            with self.subTest(unscoped_target=value):
                self.assertFalse(explicit.is_valid(value))

    def test_household_nested_types_and_profile_bounds(self):
        check = validator(RELATIONSHIPS, "/$defs/HouseholdRecord")
        record = deepcopy(document(RELATIONSHIPS)["$defs"]["HouseholdRecord"]["examples"][0])
        check.validate(record)
        check.validate({**record, "additionalEnvelopeMetadata": "future declared field"})
        invalid_data = [
            {**record["data"], "address": "12 Example Street"},
            {**record["data"], "address": {"addressLines": [12], "locality": "Example Town"}},
            {**record["data"], "address": {"addressLines": ["Line"] * 4, "locality": "Example Town"}},
            {**record["data"], "address": {"addressLines": ["Line"], "locality": "Example Town", "postalCode": 120}},
            {**record["data"], "memberships": {}},
            {**record["data"], "memberships": [{"membershipId": "m_1", "role": "MEMBER", "individualRef": "person_42"}]},
            {**record["data"], "memberships": [{"role": "MEMBER", "individualRef": {"recordId": "person_42"}}]},
            {**record["data"], "memberships": [{"membershipId": "m_1", "role": 1, "individualRef": {"recordId": "person_42"}}]},
            {**record["data"], "memberships": [{"membershipId": "m_" + str(i), "role": "MEMBER", "individualRef": {"recordId": "person_" + str(i)}} for i in range(21)]},
            {**record["data"], "include": "individuals"},
        ]
        for data in invalid_data:
            with self.subTest(data=data):
                self.assertFalse(check.is_valid({**record, "data": data}))

    def test_registration_snapshots_do_not_require_parent_references(self):
        parent_check = validator(RELATIONSHIPS, "/$defs/ParentAtRegistration")
        parent_check.validate({"nameAtRegistration": "Alex Example"})
        parent_check.validate({"nameAtRegistration": "Robin Example", "individualRef": {"recordId": "person_57"}})
        for value in ({"individualRef": {"recordId": "person_57"}},
                      {"nameAtRegistration": "Robin Example", "individualRef": None},
                      {"nameAtRegistration": "Robin Example", "individualRef": {"recordId": "person_57", "registryId": "urn:example:wrong-registry"}},
                      {"nameAtRegistration": 57}):
            self.assertFalse(parent_check.is_valid(value))
        record_check = validator(RELATIONSHIPS, "/$defs/BirthRegistrationRecord")
        record = deepcopy(document(RELATIONSHIPS)["$defs"]["BirthRegistrationRecord"]["examples"][0])
        record_check.validate(record)
        self.assertEqual(set(record), {"recordId", "data"}, "The example must not require source metadata enrichment")
        self.assertFalse(record_check.is_valid({**record, "data": {**record["data"], "parents": [{"nameAtRegistration": "Example"}] * 5}}))
        self.assertFalse(record_check.is_valid({**record, "data": {**record["data"], "dateOfBirth": "2020-02-30"}}))


if __name__ == "__main__":
    unittest.main(verbosity=2)
