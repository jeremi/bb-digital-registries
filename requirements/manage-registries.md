---
title: Manage Registries
description: |
  Authorised users and API clients create, relate, inspect, publish, version, and remove registry schemas.
realises: [registry-administration]
conformance: CORE
requirements:
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to create a registry schema through the web user interface.
    documentation: |
      Channel: section 6.1 (Administrative/Analyst Functions) groups these as Analyst functions, DRS-28 to DRS-32 give the API counterparts, and resources/decision-log.md records that a user interface is needed for analysts.
      Constraint: each created registry schema records a database name; a unique short code or name; the structured schema defined by DRS-3; the domain, owner department, retention policy, and an Open, Restricted, or Confidential classification; a Draft, Published, or Archived lifecycle state; and a default indexing and storage profile selected from row store, column store, and document store.
      Source ambiguity: spec/6-functional-requirements.md:26 lists 'row store / column store / document store' as the default indexing and storage profile without saying whether all three must be offered; the migration keeps the wording and records the open question.
      Source: DRS-1 and section 4.1, Registry lifecycle management, item 1.
    test: resources/testing.md#drs-1
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to progress a registry through Draft, Published, and Archived lifecycle states.
    documentation: |
      Source: DRS-1 lists the lifecycle as Draft to Published to Archived. Section 4.1 also names publishing and archiving registry versions.
    test: resources/testing.md#drs-1
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to create multiple registry databases in one system instance through the web user interface.
    documentation: |
      Channel: section 6.1 (Administrative/Analyst Functions) groups these as Analyst functions, DRS-28 to DRS-32 give the API counterparts, and resources/decision-log.md records that a user interface is needed for analysts.
      Source: DRS-2.
    test: resources/testing.md#drs-2
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to configure the databases and fields connected by a registry relationship.
    documentation: |
      Constraint: supported relationship kinds are a strict foreign key, a soft UUID reference without a foreign-key constraint, and a graph relationship with parent-child and many-to-many edges.
      Source ambiguity: spec/6-functional-requirements.md:31-34 says 'Links can be' foreign key, soft link or graph, while only the foreign key is backed by 'must' (spec/6-functional-requirements.md:39); the migration requires all three and records that the source does not say whether all are mandatory.
      Source: DRS-2.
    test: resources/testing.md#drs-2
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry opens records in a related database when a user selects a linked record identifier while browsing registry data.
    documentation: |
      Constraint: all corresponding records from the related database are opened.
      Source tension: spec/6-functional-requirements.md:37 says it 'should be possible' to open another database by clicking the record ID, while the example at spec/6-functional-requirements.md:39 is tagged REQUIRED.
      Source: DRS-2. The mother, child, and payment registries in the source are an illustrative example rather than an additional constraint.
    test: resources/testing.md#drs-2
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry identifies linked registry data at both database and field levels.
    documentation: |
      Evidence: schema documentation showing the database identifiers and field identifiers used for registry relationships.
      Source: DRS-2 requires at least two levels of identifiers, described there as database ID and field ID.
    test: resources/testing.md#drs-2
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry supports cascade delete, restrict delete, and orphan tolerance as reference-integrity rules for linked databases.
    documentation: |
      Source: DRS-2. The source lists the three rules but does not say whether a relationship selects exactly one rule or may combine them.
    test: resources/testing.md#drs-2
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to add fields to a registry schema.
    documentation: |
      Source: DRS-3.
    test: resources/testing.md#drs-3
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to assign a name to each registry schema field.
    documentation: |
      Source: DRS-3, item 1.
    test: resources/testing.md#drs-3
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to select a supported type for each registry schema field.
    documentation: |
      Constraint: the core supported types are Text; Number; Boolean; Date/time; Date; Time; File with configurable file extensions or types; List, Array, or Edit grid for a sub-table or array of values inside a field; and List of Values or Catalog holding a value and key.
      Constraint: the optional JSON object or Block container, UTF-8 encoding, GeoPoint, and GeoShape features are represented by RECOMMENDED requirements in this core functionality.
      Source: DRS-3, item 2.
    test: resources/testing.md#drs-3
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to publish a registry database through the web user interface.
    documentation: |
      Channel: section 6.1 (Administrative/Analyst Functions) groups these as Analyst functions, DRS-28 to DRS-32 give the API counterparts, and resources/decision-log.md records that a user interface is needed for analysts.
      Constraint: publishing reveals the database to users.
      Source: DRS-4 and section 4.1, Registry lifecycle management, items 2 to 4.
    test: resources/testing.md#drs-4
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry creates a new version of the registry schema and its API services for each publish request.
    documentation: |
      Source: DRS-4.
    test: resources/testing.md#drs-4
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry makes earlier versions of a registry schema available to authorised users.
    documentation: |
      Source: DRS-4.
    test: resources/testing.md#drs-4
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry keeps data stored under an earlier database version usable under both that version and later versions.
    documentation: |
      Source: DRS-4. The source does not define the compatibility or migration rules that make the data usable in a later version.
    test: resources/testing.md#drs-4
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to delete a registry schema version through the web user interface.
    documentation: |
      Channel: section 6.1 (Administrative/Analyst Functions) groups this as an Analyst function, spec/4-key-digital-functionalities.md:17 says the Administrator/Analyst uses a web user interface, and resources/decision-log.md records that a user interface is needed for analysts; DRS-28 to DRS-32 define no API counterpart for deleting a schema version.
      Constraint: deleting a schema version also deletes the API services of the same version.
      Source: DRS-4.
    test: resources/testing.md#drs-4
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry identifies breaking changes in a registry schema automatically.
    documentation: |
      Source: DRS-4, Change impact analysis.
    test: resources/testing.md#drs-4
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry warns an authorised user about identified breaking changes in a registry schema.
    documentation: |
      Source: DRS-4, Change impact analysis.
    test: resources/testing.md#drs-4
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry displays a registry database schema in the web user interface.
    documentation: |
      Source: DRS-16.
    test: resources/testing.md#drs-16
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to configure API-related properties of a registry schema field.
    documentation: |
      Constraint: configurable API-related properties are required, unique, maximum, minimum, and blinded or encrypted.
      Source: DRS-17, item 1.
    test: resources/testing.md#drs-17
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to configure user-interface-related properties of a registry schema field.
    documentation: |
      Constraint: configurable user-interface-related properties are field mask and format, read-only, personal data, enum list selection, blinded or encrypted, multiple value or array, and triggers.
      Constraint: a user can add more values (for example a multi select from a catalog list) to the same multiple-value field.
      Constraint: the source nests the following under multiple value or array: an array type, Required, Unique, maximum, and minimum validation options, and foreign keys to link other databases in the same ecosystem. See the example schema in [Appendix 2](../assets/appendix2.json).
      Constraint: trigger actions include creating identifiers, merging fields, adding a prefix, adding a suffix, applying conditional logic, transforming text to upper or lower case, and JavaScript transformation.
      Constraint: a trigger may be conditioned on one or more conditions being true.
      Source: DRS-17, item 2. The source does not define the execution environment or security constraints for the listed JavaScript transformation.
    test: resources/testing.md#drs-17
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry activates configured field-content triggers when a record is created or changed.
    documentation: |
      Source: DRS-17 defines a trigger as record-level automation.
    test: resources/testing.md#drs-17
  - id: null
    status: DRAFT
    level: RECOMMENDED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to configure a JSON object or block-container field that groups fields visually.
    documentation: |
      Source: DRS-3, field type 9, explicitly marked optional. The format represents a source OPTIONAL feature as RECOMMENDED in the core functionality.
    test: resources/testing.md#drs-3
  - id: null
    status: DRAFT
    level: RECOMMENDED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry uses UTF-8 as the database or cluster encoding for multilingual registry content.
    documentation: |
      Evidence: database or cluster configuration showing UTF-8 encoding, together with a multilingual storage and retrieval check.
      Source: DRS-3, field type 11, explicitly marked optional. Although the source lists this among field types, its wording describes database or cluster encoding rather than a field type. The format represents a source OPTIONAL feature as RECOMMENDED in the core functionality.
    test: resources/testing.md#drs-3
  - id: null
    status: DRAFT
    level: RECOMMENDED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to configure a GeoPoint field that holds latitude and longitude.
    documentation: |
      Source: DRS-3, field type 12, explicitly marked optional. The format represents a source OPTIONAL feature as RECOMMENDED in the core functionality.
    test: resources/testing.md#drs-3
  - id: null
    status: DRAFT
    level: RECOMMENDED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to configure a GeoShape field that holds a polygon or boundary.
    documentation: |
      Source: DRS-3, field type 13, explicitly marked optional. The format represents a source OPTIONAL feature as RECOMMENDED in the core functionality.
    test: resources/testing.md#drs-3
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: modifyDatabase
    statement: The Digital Registry enables an authorised API client to create a registry database.
    documentation: |
      Constraint: the request supplies a database name, a short name, and the database schema defined by DRS-3.
      Contract gap: the bound request defines code, schema, groupName and catalogName but no database-name field (spec/6-functional-requirements.md:334 'Name of the database').
      Source: DRS-28.
    test: resources/testing.md#drs-28
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: modifyDatabase
    statement: The Digital Registry enables an authorised API client to create multiple registry databases in one system instance.
    documentation: |
      Source: DRS-29.
    test: resources/testing.md#drs-29
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: null
    statement: The Digital Registry enables an authorised API client to publish a registry database.
    documentation: |
      Constraint: publishing reveals the database to users.
      Source: DRS-30.
      Binding gap: neither source OpenAPI document defines an operation that publishes a registry database.
    test: resources/testing.md#drs-30
---

The Digital Registry manages registry schemas over their lifecycle. Section 4.1 also names deprecation and archival, backward-compatibility guidance, validation rules, deduplication, and data-quality controls as lifecycle-management functions. The legacy requirements do not define separate verifiable behaviour for all of those names, so this migration records them here without inventing additional constraints.

DRS-2 uses database and database table interchangeably when describing relationships. This migration preserves that source usage and does not decide whether relationships may address another storage abstraction.
