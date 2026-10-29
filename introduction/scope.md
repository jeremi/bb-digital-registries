---
title: Scope
---

# Scope

## Subject and applicability

This document specifies the Digital Registries Building Block, a generic, domain-agnostic software component for creating and administering registry structures and for securely maintaining, exchanging, and auditing authoritative registry records.

It applies to software solutions claiming conformance to the Digital Registries Building Block specification.
A conformant solution meets the core of this document.
It may also claim one or more extensions and meets every requirement of each extension it claims:

- **Database Views:** governed, read-only selections of registry data;
- **Schema Templates:** reusable, versioned registry templates and template exchange;
- **Service Usage Statistics:** retained API-service and registry-search usage information; and
- **Statistical Queries API:** authorised statistical queries through an API.

Each extension requires the core and does not require another extension.
The migration derives these extensions from the upstream requirements explicitly labelled optional.
Some source clauses cross this boundary, for example a required view-based custom API and a full registry template that includes views; the [overview](overview.md#core-and-extensions) lists them and the [source findings](../resources/source-findings.md#cross-clause-ambiguities) record them unresolved.

## Relationships

The Digital Registries Building Block operates within the GovStack architecture and inherits the applicable GovStack cross-functional architecture and security requirements.
The source specification also raises the data-protection and logical-deletion requirements identified in its cross-functional chapter from recommended to required for Digital Registries.

It commonly works with the Registration, Foundational ID, Workflow, Information Mediator, and Consent and Authorisation components described in the [overview](overview.md#place-in-larger-systems).
Those relationships do not place the counterpart components inside the Digital Registries system under test.

## Covered

This specification covers:

- registry lifecycle administration, including registry and schema creation, publication, versioning, and administrative configuration;
- record management through authorised user and service interfaces;
- policy-based access to registries, records, and fields;
- audit logs and reports about changes and personal-data use;
- registry-facing data exchange, generated APIs, and events;
- registry usage, reporting, and statistical functions;
- the minimum registry data fields and resource relationships stated by the upstream data model;
- the two data protections that the upstream cross-functional chapter elevates from recommended to required;
- the required platform, API, and workflow behaviours stated outside DRS-1 through DRS-37;
- the Digital Registries side of interactions with authorised client systems and other Building Blocks; and
- the resource model, API source contracts, and workflows retained in the active resources.

The active requirement files define the conformance obligations for these areas.
The narrative resources explain the upstream context but do not create additional conformance requirements by themselves.

## Not covered

| Excluded | Owned by |
|---|---|
| Applicant-facing capture of new registration requests and the procedural lifecycle for processing them | The Registration Building Block or the adopting government's sectoral application |
| Business-process orchestration tied to registry data | The Workflow Building Block or the adopting government's process system |
| Unique identification and identity proofing of entities | The Foundational ID Building Block and the adopting government's identity policy |
| Cross-organisation transport, mediation, and counterpart behaviour | The Information Mediator and the counterpart system's specification |
| Consent policy and the legal basis for access | The Consent and Authorisation component and the adopting government |
| Domain-specific registry semantics, legal effects, retention rules, and decisions about who may create or use a registry | The adopting government and the responsible registry authority |
| The internal database architecture or storage technology used by a conformant implementation | The implementation |
| Electricity and network availability assumed by the source workflows | The deployment environment; these remain workflow prerequisites rather than software-conformance requirements |

The upstream text states both that the Building Block does not contain data-capture and workflow functionality and that administrators can enter and update registry records through its administrative interface.
This scope preserves that distinction: applicant-facing registration capture and procedural workflow are outside the boundary, while authorised administrative record management is covered.

## Ownership

The Registries and Registration Working Group owns this specification.
Change requests are handled in the [Digital Registries Building Block repository](https://github.com/GovStackWorkingGroup/bb-digital-registries).
