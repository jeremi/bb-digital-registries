---
description: Permitted outward views of access to Registry Records.
---

# Access Transparency

> **Status:** Informative and not claimable in this release. No Access Transparency requirements, entitlement model, event schema, contract, or tests are published.

## Purpose and applicability

Access Transparency enables an entitled Record Principal to obtain a permitted view of access to a related Record. It applies where law or policy grants a person or organisation an access-history right.

A Record Principal can be a subject, owner, title holder, director, beneficiary, or credential holder. The relationship alone does not create a universal entitlement. The adopting jurisdiction defines the applicable right, delegation rules, and period for which the relationship is relevant.

## Capability areas

| Area | Outcome |
|---|---|
| Access-history retrieval | Returns permitted entries for a Record and time range. |
| Filtering and pagination | Narrows a potentially large history by declared criteria. |
| Entry interpretation | Describes the accessing organisation or permitted actor category, time, operation, and declared purpose where disclosure allows. |

## Capability boundary

Internal security and audit logging is a cross-functional concern. Access Transparency is the outward-facing service derived from permitted audit information. Its representation can omit actor identities or operational details where disclosure would create a privacy, security, or investigation risk.

An adopting authority that includes Access Transparency in its deployment needs to define entitlement, relationship verification, delegation, outward event vocabulary, retention, correction handling, and disclosure restrictions.

## Binding status

This release does not specify an Access Transparency binding, outward event schema, or API contract. An adopter evaluating implementation options can use synchronous HTTP described by OpenAPI, but that choice does not create a GovStack capability claim.

## Example

A company director requests the permitted access history for the company's registration Record and sees which organisations consulted it during a defined period.
