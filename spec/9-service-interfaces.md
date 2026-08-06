---
description: Abstract operation and proposed HTTP binding for Consultation Retrieve.
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
| Success output | Current permitted Record representation described in [Data Structures](8-data-structures.md). |
| Unsuccessful output | Problem response without protected Record data and with the protected-existence handling required by `fr-consultation#req-3`. |
| Excluded behaviour | List, Search, Record Match, GIS Query, historical-revision retrieval, and individual stored-field retrieval. |

## 9.3 Proposed HTTP binding

The initial binding is synchronous HTTP over HTTPS and will be described by an OpenAPI contract. The contract will use the shared GovStack API components for problem details and other cross-BB structures once those components and their consumption rules are ratified.

No canonical OpenAPI file is published in this release. A future contract needs to define:

- resource path and API versioning;
- exact Registry and Record metadata property names;
- schema resolution and content negotiation;
- conditional retrieval and revision identifiers;
- policy-compliant mapping of unknown, unauthorised, inactive, and superseded outcomes; and
- contract examples that do not assume a person registry.

## 9.4 Candidate bindings for later capabilities

The following standards are informative candidates for capabilities that are not claimable in this release. This table does not establish a required version or profile.

| Capability | Candidate specification |
|---|---|
| Provisioning and general HTTP operations | OpenAPI |
| Consultation Retrieve, List, Search, and Record Match | OpenAPI |
| GIS Query | OGC API Features |
| Wallet-mediated Evidence | OpenID for Verifiable Credential Issuance and Presentation; W3C Verifiable Credentials |
| Direct Evidence | OpenAPI with a signed credential or attestation format |
| Write | OpenAPI |
| Notification | OpenAPI webhooks for HTTP push; AsyncAPI for event-driven bindings |
| Aggregate Data | OpenAPI; SDMX for statistical exchange |
| Access Transparency | OpenAPI |
| Identity Federation | OpenID Connect Core and Discovery |
