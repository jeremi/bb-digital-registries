---
description: Abstract operation and binding status for Consultation Retrieve.
---

# 9 Service Interfaces

## 9.1 Current coverage

This release defines the semantics of one operation, `consultation.retrieve`. It does not define an HTTP path or exact JSON property names.

The previous generated CRUD OpenAPI files are legacy artifacts. They are not contracts for this release and do not contain a Retrieve-by-Identifier operation.

## 9.2 Abstract Retrieve operation

| Element | Definition |
|---|---|
| Operation identifier | `consultation.retrieve` |
| Purpose | Obtain the current permitted representation of one Record. |
| Required input | Record Identifier. |
| Request context | Authentication and authorisation information required by the deployment and inherited CFR requirements. |
| Success output | Current permitted Record representation described under [Consultation](05-api-families/consultation.md#retrieve-representation), including the [common Record context](05-api-families/registry-core.md#common-record-context). |
| Unsuccessful outcome | Outcome without protected Record data and with the protected-existence handling required by `fr-consultation#req-3`. |
| Excluded behaviour | Existence Check, List, Search, Revision History, Record Match, GIS Query, and individual stored-field retrieval. |

## 9.3 Binding status

No canonical OpenAPI contract is published in this release, so an implementation-specific HTTP interface cannot be used to establish a GovStack capability claim. An adopter prototyping Retrieve can use synchronous HTTP over HTTPS and describe that interface with OpenAPI.

An HTTP contract used by an adopter needs to define:

- resource path and API versioning;
- exact Registry and Record metadata property names;
- schema resolution and content negotiation;
- conditional retrieval and revision identifiers;
- policy-compliant mapping of unknown, unauthorised, inactive, and superseded outcomes; and
- contract examples that do not assume a person registry.

## 9.4 Protocol options for additional capabilities

The following standards can help an adopter evaluate implementation options for capabilities that are not claimable in this release. The table does not establish a required specification, version, or profile.

| Capability | Protocol options |
|---|---|
| Provisioning and general HTTP operations | OpenAPI |
| Consultation Retrieve, Existence Check, List, Search, Revision History, and Record Match | OpenAPI |
| GIS Query | OGC API Features |
| Wallet-mediated Evidence | OpenID for Verifiable Credential Issuance and Presentation; W3C Verifiable Credentials |
| Direct Evidence | OpenAPI with a signed credential or attestation format |
| Write | OpenAPI |
| Notification | OpenAPI webhooks for HTTP push; AsyncAPI for event-driven bindings |
| Aggregate Data | OpenAPI; SDMX for statistical exchange |
| Access Transparency | OpenAPI |
| Identity Federation | No protocol option selected; profile ownership and binding remain subject to cross-BB agreement with the Identity team |
