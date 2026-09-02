---
description: Verification approach for the Base Registry Profile.
---

# 11 Testing

## 11.1 Test maturity

The requirements and tests in this release are DRAFT. The scenarios below define deterministic verification intent. No executable conformance suite is published for this release.

Legacy Cucumber tests under `test/openAPI` exercise the previous generated CRUD interface. They are retained as migration evidence and are not a conformance suite for this release.

## 11.2 Required fixtures

An implementation being evaluated provides non-production fixtures for:

- machine-readable Registry metadata;
- two distinct current Records in the same Registry;
- a current Record accessible to two consumers with different disclosure rights;
- evidence of the identifier lifecycle across successive revisions and retired Records;
- an unknown Record Identifier;
- a protected Record whose existence must not be disclosed; and
- each lifecycle state the Registry exposes through Retrieve.

Testers use synthetic fixtures rather than real personal or confidential data.

## 11.3 Requirement traceability

| Requirement | Verification item | Expected result |
|---|---|---|
| `fr-core#req-1` | Inspect machine-readable Registry metadata and identifier evidence | Globally unique and stable Registry Identifier, Registry name, Registry Authority, and Digital Registries specification version are present. |
| `fr-core#req-2` | Retrieve two distinct Records | Each response includes the Registry Identifier and a different Record Identifier; each identifier pair is unique. |
| `fr-core#req-3` | Inspect the identifier policy and lifecycle evidence | A Record Identifier remains unchanged across revisions and lifecycle states, is not shared, and is not reassigned after retirement. |
| `fr-core#req-4` | Validate a retrieved representation | The representation format conveyed by the binding matches the representation, schema and semantic-model references resolve, and schema validation succeeds. |
| `fr-core#req-5` | Retrieve fixtures across exposed lifecycle states | Each response identifies the current revision and a lifecycle state permitted by its declared schema. |
| `fr-core#req-6` | Retrieve a known accessible Record | Registry Authority identifier and recording time are present. |
| `fr-consultation#req-1` | Retrieve a known accessible Record | Current permitted representation is returned with required Record context. |
| `fr-consultation#req-2` | Retrieve the same Record as two consumers | Each response contains only the projection permitted to that consumer. |
| `fr-consultation#req-3` | Retrieve unknown and protected identifiers as the same consumer | Status or protocol outcome, security-relevant response metadata, stable error type, response structure, and non-Record-specific values match; any differing trace or correlation values are independent of Record existence; neither response contains Record-specific data. |

The abbreviated references in this table use the full `govstack-bb-digital-registries` namespaces defined under [Registry Core](05-api-families/registry-core.md#registry-core-functional-requirements) and [Consultation](05-api-families/consultation.md#retrieve-functional-requirements).

## 11.4 Behaviour scenarios

```gherkin
Feature: Retrieve the current permitted Registry Record

  Scenario: Authorised consumer retrieves a current Record
    Given a current Record with a stable Record Identifier
    And an API Consumer authorised to receive its standard representation
    When the consumer retrieves the Record by that identifier
    Then the Registry returns the current permitted representation
    And the representation identifies its Registry, revision, lifecycle state, representation format, schema, semantic model, Registry Authority, and recording time
    And the retrieval does not modify the Record

  Scenario: Consumers receive different permitted representations
    Given two API Consumers with different disclosure entitlements
    When each consumer retrieves the same Record
    Then each response contains only the fields and metadata permitted for that consumer

  Scenario: A protected Record cannot be enumerated through errors
    Given a consumer that is not authorised to know whether a protected Record exists
    And an unknown Record Identifier
    When the consumer requests the protected and unknown Record Identifiers
    Then both responses use the same status or protocol outcome
    And both responses use the same security-relevant response metadata, stable error type, response structure, and non-Record-specific values
    And any differing trace or correlation values are generated independently of Record existence
    And neither response contains Record-specific data
```

## 11.5 Evidence retained for audit

Verification evidence identifies the Digital Registries specification version tested. It also includes fixture definitions, requests, responses, schema-validation results, identifier-lifecycle evidence, and a traceability report mapping every evaluated requirement to a pass or fail result.

No fixed response-time threshold, container technology, administrative user interface, Information Mediator header, or test tool is part of the target Base Registry Profile.
