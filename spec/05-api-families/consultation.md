---
description: Read capabilities for permitted Registry information.
---

# Consultation

> **Status:** Retrieve is DRAFT and part of the target Base Registry Profile. Existence Check, List, Search, Revision History, Record Match, and GIS Query are informative and not claimable in this release.

## Purpose and applicability

Consultation enables an API Consumer operating under an applicable access and disclosure policy to obtain a permitted representation of Registry information. It applies when a consumer needs current information from the authoritative source rather than a portable signed assertion or a derived statistic.

Retrieve is the minimum read capability. It lets a consumer that already knows a Record Identifier obtain the current permitted representation without requiring the Registry to expose enumeration or discovery by personal or domain attributes.

Consultation inherits the shared [Registry Core model and requirements](registry-core.md). In this family, the current revision means the latest accepted revision of the Record. It is not necessarily an active Record; the declared lifecycle state and applicable disclosure policy determine whether and how it is returned.

Consultation provides a common capability framework for domain-specific registries. The applicable registry or sector profile defines the Record schema, semantic model, lifecycle vocabulary, permitted representations, and any domain-specific query or matching semantics. This specification does not require a generic query layer over arbitrary stored fields.

## Capability patterns

| Pattern | Outcome |
|---|---|
| `consultation.retrieve` | Returns the current permitted representation of one Record identified by its stable Record Identifier. |
| Existence Check | Indicates whether a Record exists only when the consumer is permitted to learn that fact. |
| List | Returns a bounded, paginated collection under an applicable domain profile, optionally filtered by declared attributes. |
| Search | Finds Records using predicates declared by the applicable registry or sector profile. |
| Revision History | Returns permitted revision metadata or a permitted historical representation of one Record. |
| Record Match | Returns possible matching Records with confidence information under a domain-specific matching profile. It does not make an authoritative identity or acceptance decision. |
| GIS Query | Applies domain-defined spatial predicates to geometric attributes maintained by the Registry. |

## Capability boundary

Consultation returns live Registry information. [Evidence](evidence.md) produces a signed assertion with its own validity and status. [Aggregate Data](aggregate-data.md) returns derived statistics rather than Record representations.

Consultation is read-only. It does not create a Record, accept a new revision, change lifecycle state, or perform an approval decision. The Retrieve requirements define permitted representations and protected-existence handling. An adopter selecting Existence Check, List, Search, Revision History, Match, or GIS Query needs an applicable profile that defines disclosure, bounded results, query limits, and result interpretation for that capability.

## Retrieve representation

A successful Retrieve returns the [common Record context](registry-core.md#common-record-context) together with the domain data that the API Consumer is permitted to receive. The representation can omit or redact domain data and additional protected provenance, but the resulting projection remains unambiguous and valid against its declared representation schema.

The Base Registry Profile retrieves the current revision. Revision History is a separate informative Consultation capability and is not claimable in this release.

## Retrieve functional requirements

The following DRAFT requirements define the Consultation capability in the target Base Registry Profile. They do not establish a certification claim in this release.

### #1 Retrieve the current Record by identifier (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-1`

`KF: Consultation`

Given an unambiguous Registry context, a valid Record Identifier, and a request permitted by applicable policy, an implementation returns the current permitted representation of that Record without modifying the Record.

**Purpose:** An API Consumer that already knows a Record Identifier can obtain authoritative Registry information without using search or enumeration.

**Prerequisite:** A permitted consumer context and an accessible Record fixture exist.

**Verification:** Retrieve a known Record by identifier, verify the Registry and Record identifiers, current revision, lifecycle state, representation format, schema, semantic model, minimum provenance, and permitted domain data, and confirm that a subsequent Retrieve returns the same revision when no intervening change occurred.

### #2 Apply disclosure rules to the returned representation (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-2`

`KF: Consultation`

An implementation returns only the Record fields and metadata permitted for the API Consumer and request context. The resulting projection remains valid against its declared representation schema.

**Purpose:** Retrieve does not become an entitlement to the complete stored Record. The same Registry can expose different valid representations under different disclosure policies, including a public representation where applicable.

**Prerequisite:** At least two test consumer contexts have different disclosure entitlements for the same Record.

**Verification:** Retrieve the same Record using both consumer contexts and verify that each receives only its permitted projection, each projection validates against its declared schema, and omitted values are not exposed through errors or metadata returned to the consumer.

### #3 Hide protected Record existence (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-3`

`KF: Consultation`

For an API Consumer that is not authorised to learn whether a protected Record exists, an implementation returns an outcome that is indistinguishable under the published Retrieve contract from the outcome for an unknown Record Identifier. This includes the same status or protocol outcome, security-relevant response metadata, stable error type, response structure, and non-Record-specific values. Per-request trace or correlation values may differ when they are generated independently of Record existence. The response contains no Record-specific data.

**Purpose:** An unauthorised consumer cannot enumerate protected Record Identifiers through the Retrieve contract.

**Prerequisite:** An unknown Record Identifier and a protected Record Identifier are available as test fixtures for the same consumer context.

**Verification:** Retrieve both identifiers using that consumer context and compare the status or protocol outcome, security-relevant response metadata, error type, response structure, non-Record-specific values, and data fields. Verify that any differing trace or correlation values are independent of Record existence and that neither response exposes Record-specific data.

## Selecting additional Consultation capabilities

An adopter may need Consultation capabilities beyond Retrieve. These capabilities are not part of the Base Registry Profile and are not claimable in this release. An adopter should select them only when they serve a defined consumer need and an applicable registry or sector profile supplies the required domain semantics.

| Capability | Select when | The applicable profile needs to define |
|---|---|---|
| Existence Check | A consumer needs to determine whether a Record exists without receiving its representation. | When existence may be disclosed and how protected and unknown Records are treated consistently. |
| List | A consumer is permitted to browse a defined collection of Records. | Collection membership, filters, ordering, bounded pagination, collection metadata, and disclosure rules. |
| Search | A consumer needs to find Records without already knowing their Record Identifiers. | Searchable domain concepts, predicates, result limits, and zero-match, multiple-match, and truncated-result outcomes. |
| Revision History | A consumer needs permitted information about earlier revisions of a known Record. | Whether revision enumeration or historical representations are available, stable revision identifiers, ordering, retention, lifecycle interpretation, and disclosure or erasure rules for historical data. |
| Record Match | A consumer supplies incomplete or variable domain information that may correspond to more than one Record. | Permitted inputs, matching rules, confidence interpretation, disclosure of possible matches, and ambiguous or no-match outcomes. A match is not an authoritative identity, eligibility, or acceptance decision. |
| GIS Query | A spatial Registry exposes Records through geographic relationships. | Supported spatial predicates, coordinate and geometry semantics, spatial and result bounds, and disclosure of protected Records or locations. |

For every selected capability, disclosure applies to both Record content and result metadata. The applicable profile needs to ensure that counts, ordering, page boundaries, confidence values, suggestions, and geometries do not reveal information that the consumer is not permitted to learn.

## Binding status

This release defines the abstract Retrieve operation but does not specify an HTTP binding or publish a canonical OpenAPI contract. An adopter prototyping Retrieve can use synchronous HTTP described by OpenAPI. A spatial Registry evaluating GIS Query can consider OGC API Features. These implementation choices do not create a GovStack capability claim.

See [Service Interfaces](../09-service-interfaces.md), [Workflows](../10-workflows.md), and [Testing](../11-testing.md).

## Example

A licensing service retrieves the current permitted representation of a business registration by its Record Identifier. The Registry returns only the fields and metadata that service is authorised to receive.
