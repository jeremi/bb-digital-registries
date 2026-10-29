---
title: Represent Registry Data
description: Registry implementers retain the minimum data fields and resource relationships specified by the upstream model.
realises:
- registry-administration
- record-management
- accountability
conformance: CORE
requirements:
- id: null
  status: DRAFT
  level: REQUIRED
  observability: AUDITABLE
  mutability: EXTENSIBLE
  interaction: INTERNAL
  statement: The Digital Registry includes the upstream minimum field Database ID in its data model.
  documentation: 'Constraint: Field: Database ID. Type: integer. Meaning: Unique identifier of a database.. Required status: Required. Preserve this as a minimum model property from chapter 7, without inventing a new JSON key or changing the original API schemas.

    Evidence: data-model documentation showing the Database ID property.

    Source: DATA-7.2-FIELD-1.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: AUDITABLE
  mutability: EXTENSIBLE
  interaction: INTERNAL
  statement: The Digital Registry includes the upstream minimum field Database name in its data model.
  documentation: 'Constraint: Field: Database name. Type: varchar. Meaning: Name that will define the database content. Name is public.. Required status: Required. Preserve this as a minimum model property from chapter 7, without inventing a new JSON key or changing the original API schemas.

    Evidence: data-model documentation showing the Database name property.

    Source: DATA-7.2-FIELD-2.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: AUDITABLE
  mutability: EXTENSIBLE
  interaction: INTERNAL
  statement: The Digital Registry includes the upstream minimum field Schema ID in its data model.
  documentation: 'Constraint: Field: Schema ID. Type: integer. Meaning: Database schema ID. Required status: Required. Preserve this as a minimum model property from chapter 7, without inventing a new JSON key or changing the original API schemas.

    Evidence: data-model documentation showing the Schema ID property.

    Source: DATA-7.2-FIELD-3.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: AUDITABLE
  mutability: EXTENSIBLE
  interaction: INTERNAL
  statement: The Digital Registry includes the upstream minimum field Database schema in its data model.
  documentation: 'Constraint: Field: Database schema. Type: json object. Meaning: Database schema. See example in Chapters 7.3.1 and 7.3.2.. Required status: Required. Preserve this as a minimum model property from chapter 7, without inventing a new JSON key or changing the original API schemas.

    Evidence: data-model documentation showing the Database schema property.

    Source: DATA-7.2-FIELD-4.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: AUDITABLE
  mutability: EXTENSIBLE
  interaction: INTERNAL
  statement: The Digital Registry includes the upstream minimum field Version in its data model.
  documentation: 'Constraint: Field: Version. Type: numeric. Meaning: Database version. Each change in schema will produce the next version of the database and API services.. Required status: Required. Preserve this as a minimum model property from chapter 7, without inventing a new JSON key or changing the original API schemas.

    Evidence: data-model documentation showing the Version property.

    Source: DATA-7.2-FIELD-5.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: AUDITABLE
  mutability: EXTENSIBLE
  interaction: INTERNAL
  statement: The Digital Registry includes the upstream minimum field Data ID in its data model.
  documentation: 'Constraint: Field: Data ID. Type: integer. Meaning: Data element unique identifier.. Required status: Required. Preserve this as a minimum model property from chapter 7, without inventing a new JSON key or changing the original API schemas.

    Evidence: data-model documentation showing the Data ID property.

    Source: DATA-7.2-FIELD-6.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: AUDITABLE
  mutability: EXTENSIBLE
  interaction: INTERNAL
  statement: The Digital Registry includes the upstream minimum field Registry number in its data model.
  documentation: 'Constraint: Field: Registry number. Type: varchar. Meaning: Additional registry identifier. Unique identifier in the registry.. Required status: Required. Preserve this as a minimum model property from chapter 7, without inventing a new JSON key or changing the original API schemas.

    Evidence: data-model documentation showing the Registry number property.

    Source: DATA-7.2-FIELD-7.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: AUDITABLE
  mutability: EXTENSIBLE
  interaction: INTERNAL
  statement: The Digital Registry includes the upstream minimum field Field type in its data model.
  documentation: 'Constraint: Field: Field type. Type: varchar. Meaning: Field type: datetime, date, boolean, text, number, file.. Required status: Required. Preserve this as a minimum model property from chapter 7, without inventing a new JSON key or changing the original API schemas.

    Evidence: data-model documentation showing the Field type property.

    Source: DATA-7.2-FIELD-8.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: AUDITABLE
  mutability: EXTENSIBLE
  interaction: INTERNAL
  statement: The Digital Registry includes the upstream minimum field Field value in its data model.
  documentation: 'Constraint: Field: Field value. Type: datetime, date, boolean, text, number. Meaning: Field value, data stored in the field.. Required status: Required. Preserve this as a minimum model property from chapter 7, without inventing a new JSON key or changing the original API schemas.

    Evidence: data-model documentation showing the Field value property.

    Source: DATA-7.2-FIELD-9.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: AUDITABLE
  mutability: EXTENSIBLE
  interaction: INTERNAL
  statement: The Digital Registry includes the upstream minimum field Audit log old value in its data model.
  documentation: 'Constraint: Field: Audit log old value. Type: datetime, date, boolean, text, number. Meaning: Field value before change.. Required status: Required. Preserve this as a minimum model property from chapter 7, without inventing a new JSON key or changing the original API schemas.

    Evidence: data-model documentation showing the Audit log old value property.

    Source: DATA-7.2-FIELD-10.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: AUDITABLE
  mutability: EXTENSIBLE
  interaction: INTERNAL
  statement: The Digital Registry includes the upstream minimum field Audit log new value in its data model.
  documentation: 'Constraint: Field: Audit log new value. Type: datetime, date, boolean, text, number. Meaning: Field value after the change.. Required status: Required. Preserve this as a minimum model property from chapter 7, without inventing a new JSON key or changing the original API schemas.

    Evidence: data-model documentation showing the Audit log new value property.

    Source: DATA-7.2-FIELD-11.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: AUDITABLE
  mutability: EXTENSIBLE
  interaction: INTERNAL
  statement: The Digital Registry represents the relationships in the upstream Registry resource model.
  documentation: 'Constraint: The source diagram gives Database-to-Data as one to zero-or-many, Data-to-Audit-Log as one to one-or-many, Database-to-Schema as one to one-or-many, and Schema-to-Data as one to one-or-many. These are model constraints, not a mandate for a particular database technology.

    Evidence: data-model documentation showing each of the four stated relationships and their cardinalities.

    Source: DATA-7.1-RELATIONSHIPS.'
  test: resources/testing.md#supplementary
---

The YAML requirements retain the source obligations identified in the migration ledger. The supporting descriptions and contracts remain under `resources/`.
