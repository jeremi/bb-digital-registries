---
description: Sectoral subject authentication and authorised claim release.
---

# Identity Federation

> **Status:** Informative and not claimable in this release. Cross-Building-Block ownership is unresolved. No Identity Federation requirements, claim profile, protocol profile, or tests are published.

## Purpose and applicability

Identity Federation enables a sectoral Registry containing Records about people, or a service acting for its authority, to authenticate the person represented by a Registry Record to a Relying Service and release authorised claims. It applies to sector populations such as farmers, students, health-service users, or licensed professionals.

## Cross-Building-Block ownership

GovStack has not decided whether an Identity Federation profile for a functional sector identity is defined by Digital Registries, by the Identity Building Block, or jointly. The current [Identity Building Block description](https://github.com/GovStackWorkingGroup/bb-identity/blob/main/spec/2-description.md) scopes that Building Block to foundational identity while also discussing integration with functional identities. That provides context for the discussion but does not settle profile ownership.

Until the Digital Registries and Identity teams agree the boundary, this page records only the candidate capability outcome. It does not assign specification ownership or establish a protocol binding.

## Profile considerations

Any eventual profile needs to define the relationship between the authenticated subject and the Registry Record, the lifecycle of the functional identifier, authorised claim release, subject-identifier policy, suspension or termination of the sector relationship, assurance expectations, and issuer topology.

The functional identifier remains issued and lifecycle-managed by the responsible Registry Authority. The eventual profile also needs to define the use of issuer-scoped and pairwise subject identifiers where required to limit correlation.

## Capability boundary

Identity Federation is an outward-facing service to a Relying Service. It is separate from authentication and authorisation used to protect Registry APIs. It does not issue or replace foundational identity. An Identity service can provide upstream authentication or identity proofing without taking ownership of the sectoral identifier.

## Binding status

This release does not select a protocol binding for Identity Federation. OpenID Connect can be evaluated during the cross-Building-Block discussion, but this specification does not adopt it for this family or create a GovStack capability claim.

## Example

A professional Registry authenticates a licensed practitioner to a continuing-education service and releases an authorised claim that identifies the relevant professional sector.
