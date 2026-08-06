---
description: Purpose, scope, architecture, and exclusions of the Digital Registries Building Block.
---

# 2 Description and Scope

## 2.1 Purpose

The GovStack Common Terminology defines the general concept of a Registry. A Digital Registries implementation exposes records for which a named authority accepts responsibility within a defined scope. Examples include business registrations, land titles, vehicle registrations, professional licences, programme enrolments, and civil events.

The Digital Registries Building Block defines the external behaviour that allows applications and other Building Blocks to use those records consistently. It separates that interoperability contract from the implementation's database technology, internal modules, administrative tools, and deployment model.

In this context, authoritative does not mean that a Record is necessarily complete or error-free. It means that a named Registry Authority is institutionally responsible for maintaining it within the declared scope.

## 2.2 Scope

This specification covers:

- identification and description of a registry;
- stable identification and lifecycle representation of registry records;
- retrieval of the current permitted representation of a record;
- declaration of schemas, semantic models, supported capabilities, and protocol bindings;
- registry-specific revision and provenance information; and
- optional capabilities for provisioning, additional consultation patterns, evidence, writing, notifications, aggregate data, access transparency, and identity federation.

The same specification can be applied to registries containing records about persons, organisations, places, assets, or events. Domain-specific meaning remains in a declared semantic model rather than being fixed by this Building Block.

## 2.3 Architectural approach

The specification separates four concerns:

1. **Operations** describe what an API consumer can ask the registry to do.
2. **Common metadata** identifies the registry, record, revision, lifecycle state, schema, and provenance relevant to an operation.
3. **Semantic models** define the meaning of domain data.
4. **Bindings** map operations to HTTP, event-driven messaging, or an established industry protocol.

This separation lets an existing national registry, a commercial product, an open-source platform, or an adaptor conform to the same external contract without sharing an internal architecture.

## 2.4 Deployment and composition

An implementation may operate one registry or many registries. It may be centralised or distributed, and may use relational, document, graph, event-sourced, or other storage approaches. These choices do not affect conformance unless they change externally observable behaviour.

A Registry can operate independently. Where other GovStack Building Blocks are deployed, they can provide complementary capabilities such as citizen-facing intake, workflow orchestration, organisational data exchange, consent management, digital signatures, wallets, identity services, or geospatial processing.

## 2.5 Boundaries with neighbouring Building Blocks

A Registry can integrate with neighbouring Building Blocks without transferring its responsibility for authoritative records.

| Neighbouring Building Block | Boundary |
|---|---|
| Registration | Registration can collect submissions and manage an intake process. The Registry accepts an approved result, a governed change request, or declared state transitions according to its Write profile. |
| Workflow | Workflow coordinates a process across components. The Registry controls which record transitions it accepts and remains responsible for the resulting authoritative state. |
| Information Mediator | Information Mediator can provide cross-organisation addressing, routing, and transport controls. The Registry owns its operations, disclosure decisions, and records. |
| Consent | Consent can provide evidence or policy signals used in a disclosure decision. The Registry enforces the decision applicable to each request and supports other lawful bases where relevant. |
| E-Signature | E-Signature can perform signing operations. The Registry remains responsible for the meaning, issuance, status, and lifecycle of Registry Evidence. |
| Wallet | A Wallet can hold and present credentials issued through Evidence. The Registry remains the source of the asserted facts and is not required to operate a Wallet. |
| Identity | Identity can authenticate users or provide foundational identity services. A sectoral Registry remains responsible for its functional identifiers. Identity Federation does not replace API access control. |
| GIS | GIS can provide geospatial processing and visualisation. A spatial Registry remains responsible for its records and can expose an OGC-aligned GIS Query capability. |

These integrations are optional unless a selected capability profile states otherwise.

## 2.6 Out of scope

This specification does not prescribe:

- the legal act or governance process that establishes a Registry Authority;
- a universal domain data model;
- a database management system or storage topology;
- a no-code registry builder, administrative web interface, or form designer;
- mandatory multi-tenancy or automatic generation of CRUD APIs;
- the citizen-facing intake and approval process for registration;
- a general-purpose workflow, rules, analytics, reporting, or data-exchange platform;
- a national foundational identifier; or
- jurisdiction-specific legal compliance or security control frameworks.

Reference architectures and implementation guides may explain how these concerns are addressed in particular domains or jurisdictions without making them part of base Registry conformance.
