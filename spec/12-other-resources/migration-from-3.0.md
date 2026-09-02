---
description: Disposition of requirements from the previous 3.0.0-alpha.1 draft.
---

# Migration from the 3.0.0-alpha.1 Draft

## Purpose

The 3.0.0-alpha.2 revision replaces the previous flat `DRS-1` through `DRS-37` requirement set. This ledger preserves traceability and explains whether each concept is retained, moved, inherited, converted to guidance, or retired.

The old identifiers are not reused. New DRAFT requirements use the `govstack-bb-digital-registries-fr-*` namespaces.

The earlier draft also elevated `govstack-cfr-data#req-4` and `govstack-cfr-data#req-7` from RECOMMENDED to REQUIRED. Those elevations are not carried forward. The inherited requirements apply with their `govstack-cfr-2.1.0` classifiers and applicability conditions.

## Requirement disposition

| Previous requirement | Disposition |
|---|---|
| DRS-1 Create Registries | Registry identity, authority, classification, and lifecycle metadata inform Registry Core. Registry creation and schema configuration move to optional Provisioning. Storage-profile choices are retired. |
| DRS-2 Multiple Databases | Mandatory multi-database, foreign-key, graph, and UI-navigation behaviour is retired. Relationships belong to the selected semantic model or implementation guidance. |
| DRS-3 Database Schema | Schema declaration and validation are retained conceptually. Schema authoring and field configuration move to optional Provisioning. The fixed field-type and UI-widget catalogue is retired. |
| DRS-4 Publishing and Versioning | Schema lifecycle and compatibility remain relevant to future Provisioning. Schema publication is decoupled from automatic endpoint-version generation. Deletion of old schemas is not carried forward. |
| DRS-5 APIs | Split across Consultation, Write, Notification, and Provisioning. Automatic creation, copying, hiding, and deletion of CRUD endpoints is retired. |
| DRS-6 Authorisation and Access Control | General authentication and access control inherit from GovStack CFR. Policy-based permitted representations are retained in Consultation. RBAC, ABAC, PBAC, consent, and anonymous-role internals are not prescribed. |
| DRS-7 Logging and Auditing | Record revision and provenance inform Registry Core. Principal-facing access history moves to Access Transparency. Generic security logging inherits from CFR. Blockchain is not a conformance mechanism. |
| DRS-8 Personal Data Usage | Access-event concepts move to Access Transparency. The fixed `PersonalDataID` log structure and optional device fingerprint are not retained. |
| DRS-9 Database Views | Saved views may inform optional List or Search. Open-data publication requires an explicit disclosure policy and is not equated with anonymous access. |
| DRS-10 Export Schema | Moves to optional Provisioning. File formats will be defined by an applicable binding or guide. |
| DRS-11 Import Schema | Moves to optional Provisioning. File formats will be defined by an applicable binding or guide. |
| DRS-12 Service Usage Statistics | Generic monitoring inherits from CFR. Administrative analytics are implementation guidance. Logging every search term is not a default requirement. |
| DRS-13 Personal Data Field | Sensitivity and classification metadata remain relevant through CFR and declared schemas. UI-specific field marking is retired. |
| DRS-14 Personal Data Identifier | Stable identifier concepts are retained, while Record, foundational, functional, and domain identifiers are distinguished. Federation behaviour is tracked under the candidate Identity Federation family pending a cross-BB ownership decision. |
| DRS-15 Secret Field | Classification, encryption, and transport security inherit from CFR. Policy-driven redaction is retained in Consultation. The credit-card and mandatory Information Mediator examples are removed. |
| DRS-16 Read Schema in UI | Machine-readable schema declaration is retained. Administrative UI presentation is implementation guidance. |
| DRS-17 Field Properties and Triggers | Validation constraints inform schemas and optional Provisioning. UI widgets, database relationships, and embedded trigger scripting are implementation choices. |
| DRS-18 Per-Database Encryption Key | Retired. Applications must not need a Registry encryption key to read data. Cryptography, key management, and rotation inherit from CFR. |
| DRS-19 Automated Data Exchange | Change events move to Notification. Cross-system orchestration and mapping tools belong to neighbouring BBs or implementation guidance. |
| DRS-20 Schema Templates | Registry templates and marketplaces are implementation guidance, not interoperability requirements. |
| DRS-21 View Data | Record access moves to Consultation and audit visibility to Access Transparency. Grid, detail, and document views are implementation choices. |
| DRS-22 Edit Data | Record mutation moves to Write. Deletion inherits CFR lifecycle rules where applicable. Editing UI behaviour is implementation guidance. |
| DRS-23 Search Helpers | Filtering, full-text search, and ordering move to optional List and Search sub-patterns. UI behaviour is not retained. |
| DRS-24 Import Data | Bulk import moves to optional Provisioning or an applicable Write profile. CSV and spreadsheet UI behaviour is guidance. |
| DRS-25 Export Data | Bulk export moves to optional Provisioning or Consultation profiles. General portability inherits from CFR. |
| DRS-26 Statistical Queries | Moves to optional Aggregate Data. Dashboards and report designers are implementation guidance. |
| DRS-27 Share Data | Controlled disclosure informs Consultation, Evidence, and consent integration. Email, links, QR codes, watermarks, and anonymous sharing are implementation choices. |
| DRS-28 Create Registry by API | Duplicate of the provisioning aspect of DRS-1. Moves to optional Provisioning. |
| DRS-29 Multiple Registries by API | Duplicate of DRS-2. Mandatory multi-tenancy is retired. |
| DRS-30 Publish Registry by API | Duplicate of DRS-4. Moves to optional Provisioning. |
| DRS-31 Modify APIs | Duplicate of DRS-5. Only abstract capability declaration is retained; generated-API product behaviour is retired. |
| DRS-32 Schema and API Discovery | Machine-readable contract and capability discovery are retained as design goals. Full schema administration is optional Provisioning. The [Registry Core metadata model](../05-api-families/registry-core.md#registry-metadata) establishes a minimal conceptual DCAT composition, while its serialisation and validation remain unspecified in this release. |
| DRS-33 Applicant CRUD | Split across mandatory Consultation Retrieve, optional Consultation sub-patterns, and optional Write. The Applicant CRUD framing is retired. |
| DRS-34 Swagger Service List | Machine-readable service contracts are retained. Swagger UI and live production examples are not conformance requirements. Protocol-native bindings depend on the GovStack framework update. |
| DRS-35 Personal Data Usage API | Duplicate of DRS-8. Moves to Access Transparency and is generalised from a person-specific identifier to a Record Principal. |
| DRS-36 Statistical Queries API | Moves to optional Aggregate Data. |
| DRS-37 Data Owner Access Log | Duplicate of DRS-8 and DRS-35. Moves to Access Transparency and is generalised to a Record Principal. |

## Replacement index

The following DRAFT requirements carry forward the interoperability intent that remains in the Base Registry Profile. A previous requirement can map to more than one replacement because the earlier product-oriented clauses combined several concerns.

| Current target | Principal predecessors |
|---|---|
| `fr-core#req-1` Registry metadata | DRS-1, DRS-32, DRS-34 |
| `fr-core#req-2` Record identification | DRS-14, DRS-33 |
| `fr-core#req-3` Record Identifier preservation | DRS-14, DRS-33 |
| `fr-core#req-4` Schema, semantic-model, and representation-format identification | DRS-3, DRS-4, DRS-16, DRS-17, DRS-32, DRS-34 |
| `fr-core#req-5` Revision and lifecycle-state identification | DRS-4, DRS-7, DRS-14 |
| `fr-core#req-6` Minimum provenance | DRS-7, DRS-21, DRS-33 |
| `fr-consultation#req-1` Retrieve by identifier | DRS-5, DRS-21, DRS-33 |
| `fr-consultation#req-2` Permitted representation | DRS-6, DRS-15, DRS-21, DRS-27, DRS-33 |
| `fr-consultation#req-3` Protected-existence handling | DRS-6, DRS-15, DRS-33 |

Concepts moved to capability families without requirements in this release retain no normative force. Provisioning carries DRS-1, DRS-3, DRS-4, DRS-10, DRS-11, DRS-17, DRS-24, DRS-28, and DRS-30. Consultation List or Search carries DRS-9 and DRS-23. Write carries DRS-22 and relevant parts of DRS-24. Notification carries DRS-19. Aggregate Data carries DRS-26 and DRS-36. Access Transparency carries DRS-8, DRS-35, and DRS-37. Evidence carries the relevant disclosure aspects of DRS-27. The candidate Identity Federation family tracks relevant identifier-federation aspects of DRS-14 and DRS-27 pending agreement with the Identity team on profile ownership.

All remaining retired or guidance-only clauses have the exact disposition recorded in the table above.

## Legacy service contracts and tests

The previous artifacts are not suitable as contracts for this release:

- there is no Retrieve-by-Identifier operation; `POST /read` performs search-by-example;
- embedded API versions disagree with filenames and with one another;
- JSON, YAML, documentation, and tests disagree on endpoint names and casing;
- tests send an Information Mediator-specific header while the contracts declare different security metadata;
- examples and fixtures assume one postpartum-care schema; and
- tests do not cover authorisation-sensitive errors, redaction, lifecycle states, revisions, or provenance.

Their behavioural intent is preserved where useful in the workflow and testing chapters. The old paths and schemas have no conformance effect in this release.
