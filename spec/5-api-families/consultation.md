---
description: Read capabilities for permitted Registry information.
---

# Consultation

> **Status:** Retrieve is part of the target Base Registry Profile. List, Search, Record Match, and GIS Query are informative and not claimable in this release.

## Purpose and applicability

Consultation enables an authorised API Consumer to obtain a permitted representation of Registry information. It applies when a consumer needs current information from the authoritative source rather than a portable signed assertion or a derived statistic.

Retrieve is the minimum read capability. It lets a consumer that already knows a Record Identifier obtain the current permitted representation without requiring the Registry to expose enumeration or discovery by personal or domain attributes.

## Capability patterns

| Pattern | Outcome |
|---|---|
| `consultation.retrieve` | Returns the current permitted representation of one Record identified by its stable Record Identifier. |
| List | Returns a bounded, paginated collection, optionally filtered by declared attributes. |
| Search | Finds Records using declared attribute predicates. |
| Record Match | Returns possible matching Records with confidence information under a declared matching profile. It does not make an authoritative identity or acceptance decision. |
| GIS Query | Applies spatial predicates to geometric attributes maintained by the Registry. |

## Capability boundary

Consultation returns live Registry information. [Evidence](evidence.md) produces a signed assertion with its own validity and status. [Aggregate Data](aggregate-data.md) returns derived statistics rather than Record representations.

The Retrieve requirements define permitted representations and protected-existence handling. Later List, Search, Match, and GIS Query profiles will need their own disclosure, pagination, query-limit, and result-interpretation rules.

## Bindings and current coverage

Synchronous HTTP described by OpenAPI is the candidate general binding. OGC API Features is a candidate additional binding for GIS Query. This release defines only the abstract Retrieve operation and does not publish a canonical HTTP contract.

See [Functional Requirements](../6-functional-requirements.md#63-consultation-retrieve), [Service Interfaces](../9-service-interfaces.md), [Workflows](../10-workflows.md), and [Testing](../11-testing.md).

## Example

A licensing service retrieves the current permitted representation of a business registration by its Record Identifier. The Registry returns only the fields and metadata that service is authorised to receive.
