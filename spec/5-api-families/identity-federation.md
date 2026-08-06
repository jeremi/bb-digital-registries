---
description: Sectoral subject authentication and authorised claim release.
---

# Identity Federation

> **Status:** Informative and not claimable in this release. No Identity Federation requirements, claim profile, protocol profile, or tests are published.

## Purpose and applicability

Identity Federation enables a sectoral Registry containing Records about people, or a service acting for its authority, to authenticate the person represented by a Registry Record to a Relying Service and release authorised claims. It applies to sector populations such as farmers, students, health-service users, or licensed professionals.

## Registry-specific concerns

A profile needs to define the relationship between the authenticated subject and the Registry Record, the lifecycle of the functional identifier, authorised claim release, subject-identifier policy, suspension or termination of the sector relationship, assurance expectations, and issuer topology.

The functional identifier remains issued and lifecycle-managed by the responsible Registry Authority. OpenID Connect transports authentication and claims; it does not create or govern that identifier. An applicable OpenID Connect binding also follows its rules for issuer-scoped subject identifiers. A later profile can define when pairwise subject identifiers are used to limit correlation.

## Capability boundary

Identity Federation is an outward-facing service to a Relying Service. It is separate from authentication and authorisation used to protect Registry APIs. It does not issue or replace foundational identity. An Identity service can provide upstream authentication or identity proofing without taking ownership of the sectoral identifier.

## Candidate binding

OpenID Connect Core and Discovery are the candidate protocol specifications. The protocol's existing operations remain authoritative; a Registry profile would add only Registry-specific claims, assurance, subject-binding, and lifecycle rules.

## Example

A professional Registry authenticates a licensed practitioner to a continuing-education service and releases an authorised claim that identifies the relevant professional sector.
