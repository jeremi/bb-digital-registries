---
description: Operational contracts and the draft Consultation HTTP binding.
---

# 9 Service Interfaces

## 9.1 Operational contracts

[Registry Core](05-api-families/registry-core.md#api-family-discovery) requires each exposed Registry service to publish its family classifications, endpoint, and a link to its machine-readable operational contract. HTTP operations use OpenAPI, or a protocol-native machine-readable description where the selected binding defines one.

Family classifications identify a service's broad capabilities. The linked contract defines exact operations, parameters, schemas, outcomes, and access requirements. Catalogue descriptions link to these details without reproducing them. A static published description and contract are sufficient; discovery does not require a new runtime service.

[Coverage and Limitations](12-other-resources.md#121-coverage-and-limitations) records binding availability. [Requirement Maturity](04-conformance.md#41-requirement-maturity) defines conformance status.

## 9.2 Abstract Consultation operations

[Consultation](05-api-families/consultation.md) defines the independently selectable Retrieve, Lookup, List, and Search capabilities and their [shared Record representation](05-api-families/consultation.md#retrieve-representation).

## 9.3 Consultation HTTP binding

The [canonical OpenAPI](../api/openapi.yaml) defines the synchronous HTTPS/JSON binding, including inputs, schemas, status codes, Problem Details, headers, and security. Its version is `1.0.0-draft`, with `/v1` as the HTTP compatibility line. It uses API Design Guide and ruleset `0.2.0-draft`; the BB requirements remain DRAFT.

### Scope and deployment contract

The server URL identifies the deployment root, optionally including a stable prefix such as `/registry`. The major version precedes each collection: `/v1/households` or, with that prefix, `/registry/v1/households`.

One API can expose multiple collections. Its contract associates each collection with a Registry, membership scope, selected capabilities, and operation schemas. Registry metadata supplies authority and service context. A Record retains its `(registryId, recordId)` identity across collections and views within that Registry.

A deployment publishes a concrete OpenAPI contract containing its selected operations, service and authentication endpoints, versioned JSON Schemas for `data` and the complete response, selectors, searches, supported filters and ordering, source currency, access policy, and continuation policy. Family classifications describe operations; Consultation and Write may share a resource URI with separate methods, request and response schemas, and permissions. The [OpenAPI examples](../api/examples/README.md) illustrate concrete collections, domain schemas, and response payloads.

### Operations and inputs

| HTTP operation, relative to the deployment root | Successful body | Input contract |
|---|---|---|
| `GET /v1/records/{recordId}` | Record | Record Identifier encoded as one path segment. |
| `POST /v1/records:lookup` | Record | JSON object with `selector` and `values`. |
| `GET /v1/records` | Page | Optional `pageSize`, `cursor`, and declared public filter or sort parameters. |
| `POST /v1/records:search` | Page | JSON object with `search`, `criteria`, and optional `pageSize`, `cursor`, and declared `sort`. |

`records` is the canonical reference name. Deployments publish concrete collection paths, such as `/v1/businesses`; the suffixes `:lookup` and `:search` address operations on that collection. IDs such as `lookup` and `search` remain valid in the item path.

The binding also exposes the guide's unversioned `/health` operation. Lookup and Search are synchronous reads returning `200`. Their criteria remain in the request body. Lookup uses a declared unique key within its documented scope; Search uses declared typed criteria. The concrete contract defines comparison and normalization rules and rejects unsupported inputs.

### Representation and schema context

Retrieve and Lookup return `{recordId, data}`. List and Search return `{items, pageInfo}`, with each item using the same Record schema for the declared view. Empty and single-result collections retain the Page shape.

The endpoint and published contract provide Registry and schema context. Additional source metadata follows [Registry Core](05-api-families/registry-core.md#common-record-context). A schema linked with `rel="describedby"` describes the complete response, including its envelope. A separate summary view has its own declared schema and field meanings.

### Outcomes, errors, and caching

The OpenAPI defines HTTP outcomes and RFC 9457 Problem Details. Retrieve and Lookup use `404 record-not-available` for unknown Records and Records outside the collection. Protected Records use the same outcome where [protected-existence handling](05-api-families/consultation.md#retrieve-functional-requirements) applies. Invalid continuations fail explicitly.

Protected reads and errors use `Cache-Control: no-store`. Deployments may declare caching for public or isolated representations. Optional conditional Retrieve evaluates authorization before returning `304`; its ETag validates the selected HTTP representation.

### Pagination

List and Search use forward opaque cursors under [Consultation requirement #7](05-api-families/consultation.md#pagination-contract). The first request selects an effective `pageSize`, defaulting to 20 and bounded to 100 in the canonical contract. A continuation repeats the original criteria, search name where applicable, sorting, and view with the cursor. Omitting `pageSize` retains the bound value; supplying a different value produces `400 invalid-cursor`.

Cursors bind the operation, Registry, collection, query, view, effective page size, and applicable access context. The deployment declares expiry and rejects malformed, expired, or mismatched cursors, including continuations whose query or view semantics it can no longer preserve. A short or empty Page can carry a non-null `nextCursor` when source processing advances. Traversal completes at `nextCursor: null`.

Optional `pageInfo.total` is the exact count of the full permitted query at the documented page evaluation time, before applying the continuation boundary. Services omit it when unavailable. OpenAPI defines the cursor format, limits, and error responses.

### Record references

The [Core representation rules](05-api-families/registry-core.md#structured-values-and-references) govern nested data and related Records. The reusable `RecordReference` schema carries `recordId` and, where the field schema leaves the target Registry open, required `registryId`. A field with a fixed target Registry permits omission of `registryId` and accepts an explicit value only when it matches that target.

When a related read is offered, the field binding identifies its target collection, read operation, and operational contract, including how the reference supplies the operation's inputs. Consumers follow that binding and the target's access requirements. Record Identifiers remain opaque; reference identity is independent of the target's current availability.

Optional client-selected expansion declares its supported paths, bounds, source currency, and disclosure behavior in the deployment contract. The [OpenAPI examples](../api/examples/README.md) demonstrate concrete nested schemas and references.

### Design choices and guide alignment

The [read API design decisions](12-other-resources/read-api-design-decisions.md) record the binding choices and the shared guide refinements.

## 9.4 Protocol options for additional capabilities

The following standards provide implementation options. The table does not establish a required specification, version, or profile.

| Capability | Protocol options |
|---|---|
| Provisioning and general HTTP operations | OpenAPI |
| Additional Consultation Existence Check, Revision History, and Record Match | OpenAPI |
| GIS Query | OGC API Features |
| Wallet-mediated Evidence | OpenID for Verifiable Credential Issuance and Presentation; W3C Verifiable Credentials |
| Direct Evidence | OpenAPI with a signed credential or attestation format |
| Write | OpenAPI |
| Notification | OpenAPI webhooks for HTTP push; AsyncAPI for event-driven bindings |
| Aggregate Data | OpenAPI; SDMX for statistical exchange |
| Access Transparency | OpenAPI |
| Identity Federation | No protocol option selected; profile ownership and binding remain subject to cross-BB agreement with the Identity team |
