---
description: Interoperable read access to Registry Records.
---

# Consultation

> **Status:** DRAFT requirements and HTTP binding, for review and implementation trials.

## Purpose and capability model

Consultation defines read access to Registry Records for independently implemented services and API Consumers. A service selects one or more capabilities and publishes its operational contract through [Registry Core metadata](registry-core.md#api-family-discovery). Consumers use that contract to determine available operations and their inputs.

| Capability | Input | Successful result |
|---|---|---|
| `consultation.retrieve` | Record Identifier | One Record |
| `consultation.lookup` | Declared exact selector and its complete key | One Record |
| `consultation.list` | Declared collection and supported public filters | Page of Records |
| `consultation.search` | Declared search and typed criteria | Page of Records |

Shared requirements apply to every selected capability; operation requirements apply when that capability is selected. Each operation applies to a declared collection with an unambiguous Registry context, representation schema, and access policy.

## Common read contract

A read preserves the source Records. Current information is the information accepted by the authoritative source and available under the service's declared currency contract, including replication or cache delay. Domain schemas define the meaning of status and validity fields.

<a id="retrieve-representation"></a>

**Record representation.** A Record contains `recordId` and `data`. The identifier is stable, unique within its Registry, and never reassigned. Registry context and the selected representation schema are unambiguous from the published contract, request context, or response. Retrieve and Lookup return one Record; List and Search use the same Record shape for each item in a Page.

The `data` schema defines domain fields, structured values, references, and their meanings. A declared view selects the information represented by that schema. Revision, lifecycle, and provenance metadata are optional in the baseline; profiles can require source-backed metadata with defined semantics.

**Example: Record representation.** Examples on this page use the [illustrative business Registry binding](../../api/examples/business-registry.openapi.yaml), which defines the domain fields, status values, and query names. Its published contract selects the Registry and the `business-public` view. A Record response contains:

```json
{
  "recordId": "r_42",
  "data": {
    "legalName": "Example Ltd",
    "registrationStatus": "DISSOLVED"
  }
}
```

**Consumer behavior.** Consumers retain Registry context when storing or forwarding Record references, treat Record Identifiers as opaque, and interpret `data` using the declared schema. They accept additional response-envelope members and use only the inputs supported by the published contract.

## Domain models and service declarations

Implementations should reuse suitable schemas and vocabularies, including [Schema.org](https://schema.org/), [EU SEMIC Core Vocabularies](https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/solution/core-vocabularies), [PublicSchema](https://publicschema.org/), and models defined or adopted by national or sector authorities.

A domain profile records reusable agreements about schemas, terminology, and query semantics. A service contract applies those agreements to the operations it exposes. An implementation can adopt an existing profile or publish a concrete domain binding directly. Both preserve the shared Consultation behavior.

The published service contract supplies the following information for its selected capabilities and applicable representation features, directly or through versioned references:

| Topic | Declared information |
|---|---|
| Registry and capabilities | Registry association and implemented operations for each collection, linked from Core metadata. |
| Representation | JSON Schemas for the Record view and responses; adopted models and versions; mappings, local constraints, and extensions. |
| Field meanings | Meaning, units, code lists, and omitted, null, or empty values, preserving the semantics of adopted models. |
| Lookup and Search | Names, typed inputs, required components, comparison and normalization rules, uniqueness scope, and matching semantics. |
| Collections | Names, membership, operation paths, supported filters and sorting, deterministic order, page-size limits, and cursor expiry. |
| Access and currency | Authentication requirements, permitted views, and source currency, including material replication or cache delay. |

An API can expose several collections, such as individuals, households, and land parcels. Each collection selects Records within a declared Registry; different collections can belong to the same Registry or to different Registries. The contract associates each operation with its collection and response schema. Record identity remains the pair of Registry Identifier and Record Identifier across collections and views.

Domain references identify their target Record and Registry. When a target read is offered, the field binding identifies its collection, operational contract, operation, and mapping from the reference to the required inputs. Consumers use that binding to resolve the reference. Embedded data declares its ownership and currency; embedded collections declare bounds, completeness, and overflow outcomes. The [Core representation conventions](registry-core.md#structured-values-and-references) provide the shared model, and OpenAPI supplies reusable reference schemas.

Published schema versions remain resolvable while their contracts are supported. The service identifies changes to schemas, queries, and views through its contract version, following the API design guide's compatibility rules.

## Read requirements

<a id="retrieve-functional-requirements"></a>

### #1 Retrieve the current Record by identifier (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-1`

`KF: Consultation`

Given a valid Record Identifier for a Record in the selected collection and a permitted request, Retrieve returns the current representation of that Record. An unknown identifier or a Record outside that collection receives the binding's unavailable-Record outcome, subject to protected-existence handling.

**Verification:** Retrieve a known source fixture and check its identity, schema, currency, and declared metadata. Confirm that the source Record is unchanged; exercise an unknown identifier and, where applicable, an identifier belonging to another collection.

### #2 Apply disclosure rules to the returned representation (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-2`

`KF: Consultation`

For every selected read, the service returns a schema-valid representation containing only the Records, fields, metadata, and result information permitted for the consumer and request context. Disclosure applies to references, embedded data, counts, errors, and continuation information.

**Verification:** Exercise each selected read with fixtures for the service's applicable access policies. Check representation validity and permitted information, including different entitlements where offered.

### #3 Hide protected Record existence (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-3`

`KF: Consultation`

When policy protects Record existence, Retrieve and Lookup return the same unresolved outcome for unknown and protected Records. Equivalence covers protocol status, security-relevant metadata, error type, response structure, and non-Record-specific values. Trace and correlation values are generated independently of Record existence; the outcome contains no Record-specific data.

**Verification:** Compare protected and unknown fixtures under the same consumer context for each selected operation. Check equivalent outcomes and independent trace values.

### #4 Resolve a Record by a declared exact selector (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-4`

`KF: Consultation`

Lookup accepts a published selector and all required key components. The key can be composite. Its declared comparison and normalization rules resolve at most one Record within the uniqueness scope. A permitted unique match in the selected collection returns that Record; zero matches in the collection produce the unresolved outcome. A source uniqueness violation produces a failure governed by disclosure policy.

Invalid, incomplete, or unsupported inputs are rejected. A selector can derive key components from verified consumer context when its contract defines that mode; a fully context-derived selector accepts an empty caller-supplied `values` object.

**Verification:** Exercise known, unknown, incomplete, incorrectly typed, and unsupported inputs, plus a source uniqueness violation. Verify comparison rules, composite keys where supported, and protected-existence handling.

### #5 List a bounded Record collection (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-5`

`KF: Consultation`

List returns a bounded Page of permitted Records from its declared collection, applying supported filters and ordering. Zero and single-result collections retain the Page shape. Unsupported filters or sorting produce a validation error.

**Verification:** Use fixtures with zero, one, and multiple results, including tied sort values where applicable. Check membership, schemas, order, size bounds, and rejection of unsupported inputs.

### #6 Search using declared criteria (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-6`

`KF: Consultation`

Search accepts a published search name and its typed criteria. It applies the declared matching rules to the selected collection and returns a bounded Page of permitted matching Records, retaining the Page shape for zero or one result. Unsupported searches, unknown criteria, and invalid inputs produce a validation error.

**Verification:** Execute declared searches with valid and invalid inputs. Check matching results, empty Pages, applicable disclosure contexts, and use of the binding's protected request locations for personal criteria.

<a id="pagination-contract"></a>

### #7 Continue bounded result pages (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-7`

`KF: Consultation`

List and Search use a declared deterministic order with a unique tie-breaker. Each request performs bounded source work, returns a bounded Page, and applies current authorization. Continuation preserves the collection, query, and view and advances traversal to explicit completion. Invalid continuation produces an error.

A completed traversal over unchanged data and access conditions contains each permitted matching Record once.

Pagination observes live data: source changes can move, add, or remove Records and cause repeated results. A profile can define stronger snapshot guarantees. Disclosure policy governs counts, page sizes, and continuation patterns, including short or empty advancing Pages.

Consumers treat cursors as opaque and return them unchanged with the original query inputs. They follow the completion signal, including when an intermediate Page is empty. The [HTTP binding](#http-binding) defines the continuation fields and fixed page-size policy.

**Verification:** Traverse unchanged multi-page fixtures to completion, checking complete membership without duplicates, identity, order, size bounds, progress, and termination. Exercise malformed, expired, and mismatched cursors, source changes, and applicable access changes. Check permitted page patterns and any total against the full permitted query.

## HTTP binding

The [canonical OpenAPI](../../api/openapi.yaml) defines the HTTPS/JSON contract, version `1.0.0-draft`, using API design guide and ruleset `0.2.0-draft`. It uses `records` as the reference collection name. Deployments publish concrete collection names, selected operations, Registry associations, and schemas in OpenAPI.

| Capability | Request | Successful body |
|---|---|---|
| Retrieve | `GET /v1/records/{recordId}` | `{recordId, data}` |
| Lookup | `POST /v1/records:lookup` with `{selector, values}` | `{recordId, data}` |
| List | `GET /v1/records` with pagination and supported public query parameters | `{items, pageInfo}` |
| Search | `POST /v1/records:search` with `{search, criteria}` and pagination controls | `{items, pageInfo}` |

The major API version precedes collection paths. An OpenAPI server URL identifies the deployment root, optionally including a stable routing prefix, such as `https://example.org/registry`. API-family classifications are declared in Core metadata and operation tags. A shared API can therefore expose:

```http
GET /v1/individuals/{recordId}
GET /v1/households/{recordId}
GET /v1/land-parcels/{recordId}
POST /v1/households:lookup
POST /v1/households:search
```

These are illustrative collection names; the published contract defines the supported paths. The `:lookup` and `:search` suffixes distinguish collection methods from item identifiers, including valid IDs such as `lookup` and `search`.

Lookup and Search are synchronous reads returning `200`; selector and search values remain in the request body. The binding also defines the operational `/health` endpoint. [API composition](registry-core.md#api-composition) describes how collections and families share an API.

**Example: exact Lookup.** The business binding names its collection `businesses`. To resolve a business by its declared registration-number key, send this body to `POST /v1/businesses:lookup`:

```json
{
  "selector": "byRegistrationNumber",
  "values": {
    "registrationNumber": "BR-000042"
  }
}
```

For the permitted match, the `200` response is the Record shown above.

**Example: Search and collection result.** To find businesses with a declared registration status, send this body to `POST /v1/businesses:search`:

```json
{
  "search": "byRegistrationStatus",
  "criteria": {
    "registrationStatus": "DISSOLVED"
  },
  "pageSize": 20
}
```

With one permitted match and traversal complete, the `200` response is:

```json
{
  "items": [
    {
      "recordId": "r_42",
      "data": {
        "legalName": "Example Ltd",
        "registrationStatus": "DISSOLVED"
      }
    }
  ],
  "pageInfo": {
    "nextCursor": null
  }
}
```

List uses the same Page shape for its declared collection.

**Continuation.** The first request selects `pageSize`, defaulting to 20 and bounded to 100 in the canonical contract. A continuation repeats the original criteria, search name where applicable, sorting, and view with the cursor. It can omit `pageSize` to retain the bound value or supply that same value. Cursors bind the operation, Registry, collection, query, view, effective size, and applicable access context. The service rejects continuations whose declared semantics it can no longer preserve.

A non-null `pageInfo.nextCursor` enables continuation; `null` marks completion. Optional `pageInfo.total` is the exact count of the full permitted query at the documented page evaluation time, before applying the continuation boundary. Services omit an unavailable total.

**Outcomes.** OpenAPI defines the status codes and Problem Details for each operation. Retrieve and Lookup share `404 record-not-available` for unknown Records, Records outside the selected collection, and Records whose existence is protected. Structural input errors, invalid query parameters, and invalid pagination controls use `400`. Structurally valid Lookup and Search bodies with unknown selector or search names or invalid domain values use `422`. Malformed, expired, or mismatched cursors use `400 invalid-cursor`. Authentication, authorization, source failures, caching, and optional conditional Retrieve follow the declared OpenAPI responses and the API design guide.

## Conformance

Evaluation identifies the service, specification and contract versions, selected capabilities, and any adopted domain profile. The service satisfies the common read contract, declaration rules, HTTP binding, and the requirements applicable to each selected capability.

| Selected capability | Applicable Consultation requirements |
|---|---|
| Retrieve | #1, #2; also #3 when existence is protected |
| Lookup | #2, #4; also #3 when existence is protected |
| List | #2, #5, #7 |
| Search | #2, #6, #7 |

Consumers follow the shared representation rules and the input, outcome, and continuation contracts for the capabilities they use. Verification checks published contracts and observable exchanges under the stated fixture conditions. The [OpenAPI examples](../../api/examples/README.md) and [artifact validation](../../api/README.md#validation) support review; deployed behavior is evaluated separately.
