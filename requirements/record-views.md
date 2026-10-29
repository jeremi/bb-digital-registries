---
title: Record Views and Operator Data Handling
description: |
  Registry operators view, search, edit, import, export and share registry records.
realises: [record-management, governed-access, accountability]
conformance: CORE
requirements:
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry presents a main grid view through which an authorised operator can see all registry data.
    documentation: |
      Source: DRS-21, item 1.1.
    test: resources/testing.md#drs-21
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry presents a detail view of a registry record to an authorised operator.
    documentation: |
      Source: DRS-21, item 1.2 and item 2.
    test: resources/testing.md#drs-21
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry opens an image document associated with a registry record in the user interface.
    documentation: |
      Source: DRS-21, item 3.
    test: resources/testing.md#drs-21
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator download a non-image document associated with a registry record.
    documentation: |
      Source: DRS-21, item 3.
    test: resources/testing.md#drs-21
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry presents a data log view of changes (create, update and delete) with the data before and after each change.
    documentation: |
      Source: DRS-21, item 4 (spec/6-functional-requirements.md:273).
    test: resources/testing.md#drs-21
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry presents a data read view with information about who has looked at or exported the data.
    documentation: |
      Source: DRS-21, item 5 (spec/6-functional-requirements.md:274).
    test: resources/testing.md#drs-21
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry stores the data and the data reader information of the data read view in the log registry.
    documentation: |
      Evidence: log-registry entries holding the data and the reader information for a representative look at and export of the data.
      Source: DRS-21, item 5 (spec/6-functional-requirements.md:274).
    test: resources/testing.md#drs-21
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator edit record data inline in the main grid.
    documentation: |
      Source: DRS-22, item 1.
    test: resources/testing.md#drs-22
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator edit record data in a record-detail view.
    documentation: |
      Source: DRS-22, item 2.1.
    test: resources/testing.md#drs-22
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator upload a document to a registry record.
    documentation: |
      Source: DRS-22, item 2.2.
    test: resources/testing.md#drs-22
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator remove a document from a registry record.
    documentation: |
      Source: DRS-22, item 2.2.
    test: resources/testing.md#drs-22
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry presents blinded or encrypted record fields in the record-detail edit view.
    documentation: |
      The source does not define how the edit view represents `blinded/encrypted` fields; the migration retains the term.
      Source: DRS-22, item 2.3.
    test: resources/testing.md#drs-22
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator delete registry data through the user interface.
    documentation: |
      Source: DRS-22, paragraph after item 2.
    test: resources/testing.md#drs-22
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry records every change made to registry data through an operator view.
    documentation: |
      Evidence: audit records for data edited, documents added or removed, and data deleted through the user interface.
      Source: DRS-22, final sentence.
    test: resources/testing.md#drs-22
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator filter records by search criteria applied to field content.
    documentation: |
      Source: DRS-23, filtering bullet.
    test: resources/testing.md#drs-23
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry provides full-text search over registry data to an authorised operator.
    documentation: |
      Source: DRS-23, full-text search bullet.
    test: resources/testing.md#drs-23
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator order records by each data field.
    documentation: |
      Source: DRS-23, ordering bullet.
    test: resources/testing.md#drs-23
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator choose to import information into a registry database.
    documentation: |
      Source: DRS-24 (spec/6-functional-requirements.md:298).
    test: resources/testing.md#drs-24
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: FILE
    statement: The Digital Registry imports registry data from JSON, CSV and XLS files.
    documentation: |
      Format gap: the source names the three file formats but defines no schema, profile or validation rules for them.
      Source: DRS-24.
    test: resources/testing.md#drs-24
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator select or filter registry data and choose to export it.
    documentation: |
      Source: DRS-25 (spec/6-functional-requirements.md:302).
    test: resources/testing.md#drs-25
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: FILE
    statement: The Digital Registry exports selected or filtered registry data to CSV, XLS and JSON files.
    documentation: |
      Format gap: the source names the three file formats but defines no schema, profile or validation rules for them.
      Source ambiguity: the source writes `CSV/XLS, JSON`; the slash does not say whether both CSV and XLS are required, and this statement reads it as requiring all three formats.
      Source: DRS-25.
    test: resources/testing.md#drs-25
  - id: null
    key: sharing-channels
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    select:
      min: 1
    statement: The Digital Registry lets an authorised user share registry data by email or through a unique and secure URL.
    documentation: |
      The source joins the two channels with `or`; at least one is required; offering both is not required.
      Source: DRS-27, opening sentences (spec/6-functional-requirements.md:321).
  - id: null
    key: sharing-channels-email
    option_of: sharing-channels
    status: DRAFT
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised user share registry data by email.
    documentation: |
      Source: DRS-27, opening sentences (spec/6-functional-requirements.md:321).
    test: resources/testing.md#drs-27
  - id: null
    key: sharing-channels-secure-url
    option_of: sharing-channels
    status: DRAFT
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised user share registry data through a unique and secure URL.
    documentation: |
      The statements on time-bound, consent-required, role-restricted and QR-code sharing links presuppose this channel; see the source ambiguities.
      Source: DRS-27, opening sentences (spec/6-functional-requirements.md:321).
    test: resources/testing.md#drs-27
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised user select shared data at record level and field level.
    documentation: |
      Source: DRS-27, sharing-scope sentence.
    test: resources/testing.md#drs-27
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator turn data sharing off in the authorisation module.
    documentation: |
      Source: DRS-27, authorisation-module sentence.
    test: resources/testing.md#drs-27
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised user share data with an anonymous recipient.
    documentation: |
      Constraint: the source classifies data shared with anonymous users as Open Data.
      Source: DRS-27, anonymous-sharing sentences.
    test: resources/testing.md#drs-27
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised user limit the validity of a secure sharing link to a defined time period.
    documentation: |
      Source: DRS-27, item 1.
    test: resources/testing.md#drs-27
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised user require consent before a recipient accesses a sharing link.
    documentation: |
      Source: DRS-27, item 2.
    test: resources/testing.md#drs-27
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised user restrict a sharing link to recipients with specified roles.
    documentation: |
      Source: DRS-27, item 3.
    test: resources/testing.md#drs-27
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry provides a QR code for a sharing link.
    documentation: |
      Source: DRS-27, item 4.
    test: resources/testing.md#drs-27
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: FILE
    statement: The Digital Registry applies a watermark to data downloaded through a sharing link.
    documentation: |
      The source does not define the watermark content or file types.
      Source: DRS-27, item 5.
    test: resources/testing.md#drs-27
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry provides a view-only sharing mode that prevents export.
    documentation: |
      Source: DRS-27, item 6.
    test: resources/testing.md#drs-27
---

# Record Views and Operator Data Handling

This functionality preserves the operator-facing record tasks in DRS-21 through DRS-25 and DRS-27. File-format obligations are separated from user-interface obligations. The source does not bind import, export or sharing to an API operation, so none is invented here.
