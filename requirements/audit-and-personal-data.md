---
title: Audit and Personal Data Protection
description: |
  Registry operators and data owners inspect accountable use of registry data, while sensitive data is protected.
realises: [accountability, governed-access]
conformance: CORE
requirements:
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry records every registry schema change in its audit log.
    documentation: |
      Evidence: audit records for a created, modified and removed schema element.
      Source: DRS-7, item 1.1.
    test: resources/testing.md#drs-7
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry records every create, read, update and delete operation on registry data in its audit log.
    documentation: |
      Evidence: an audit record for each of the four data-processing operations.
      Source: DRS-7, item 1.2.
    test: resources/testing.md#drs-7
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator view and search the audit log.
    documentation: |
      Source: DRS-7, item 1.3.
    test: resources/testing.md#drs-7
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry protects change-log integrity by chaining log entries.
    documentation: |
      Evidence: architecture and cryptographic design evidence, plus an integrity-verification result for a representative log chain.
      The source calls for the `highest level of integrity` but gives chaining as its only concrete mechanism; no measurable comparative level is introduced by the migration.
      Source: DRS-7, item 2.
    test: resources/testing.md#drs-7
  - id: null
    status: DRAFT
    level: RECOMMENDED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: CONSUMED_API
    contract: null
    statement: The Digital Registry writes database log evidence to an external blockchain for additional integrity protection.
    documentation: |
      Evidence: configuration and blockchain transaction evidence that can be correlated with database log entries.
      Contract gap: the source names no blockchain protocol, network or operation.
      Optionality mapping: DRS-7 marks this nested behaviour optional; the framework represents a skippable quality improvement as RECOMMENDED.
      Source: DRS-7, item 3.
    test: resources/testing.md#drs-7
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry records every read request made through its user interface or APIs.
    documentation: |
      Evidence: audit records corresponding to representative user-interface and API reads.
      The source calls the storage location a log table.
      Source: DRS-8, item 1 and first nested bullet.
    test: resources/testing.md#drs-8
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: For a personal-data read, the Digital Registry records a log entry tagged `PersonalData` with the log ID, record ID, field ID, unique and unchangeable `PersonalDataID`, reader ID, reader name or initial, and time of the read.
    documentation: |
      Evidence: a personal-data read log containing every named element.
      Source: DRS-8, Personal Data log structure bullets.
    test: resources/testing.md#drs-8
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry presents all personal-data read logs to an authorised operator.
    documentation: |
      Constraint: only an authorised operator may use this view to see all personal-data read logs.
      Source: DRS-8, Personal Data report visibility bullet.
    test: resources/testing.md#drs-8
  - id: null
    key: owner-log-visibility
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    select:
      min: 1
    statement: The Digital Registry lets a data owner see who has processed the owner's personal data, through an API or a user interface, as a standard function for all registries.
    documentation: |
      Constraint: a data owner is a physical person whose personal data is stored in the registry, and an owner sees only the owner's own personal-data usage.
      Source: DRS-7 item 1.4 (spec/6-functional-requirements.md:131); DRS-8 Personal Data report visibility bullet; DRS-37 items 1 to 3 (spec/6-functional-requirements.md:416-418).
  - id: null
    key: owner-log-visibility-api
    option_of: owner-log-visibility
    status: DRAFT
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: DPU
    statement: The Digital Registry returns to a data owner, through an API, the identity of each party that read or processed personal data the owner owns and the matching event logs.
    documentation: |
      Constraint: access is selected by the unique identifier of the data owner (`PersonalDataID`).
      Source: DRS-37 item 3 (spec/6-functional-requirements.md:418); DRS-8 report API bullets.
    test: resources/testing.md#drs-37
  - id: null
    key: owner-log-visibility-ui
    option_of: owner-log-visibility
    status: DRAFT
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry presents a data owner with the identity of each party that read or processed personal data the owner owns and with the matching event logs.
    documentation: |
      Constraint: access is selected by `PersonalDataID`.
      Source: DRS-37 item 3 (spec/6-functional-requirements.md:418); DRS-8 Personal Data report visibility bullet.
    test: resources/testing.md#drs-37
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: DPU
    statement: For one registry, the Digital Registry returns a personal-data usage report selected by the configured unique identifier of the data owner.
    documentation: |
      Constraint: the service is read-only, and its input is configurable by an authorised operator.
      Source: DRS-8 report API bullets; DRS-35 item 1; DRS-37 item 3.
    test: resources/testing.md#drs-35
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry records every read of a personal-data usage report in its audit log.
    documentation: |
      Evidence: an audit record corresponding to a representative report read through each exposed report boundary.
      The source calls the storage location a log table.
      Source: DRS-8, report-read logging bullet.
    test: resources/testing.md#drs-8
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: When law requires a legal justification for a personal-data read, the Digital Registry records that legal justification with the read event.
    documentation: |
      Evidence: configuration identifying the applicable condition and a matching personal-data read log.
      Source: DRS-8, legal-justification bullet.
    test: resources/testing.md#drs-8
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: When consent applies to a personal-data read, the Digital Registry records the consent reference with the read event.
    documentation: |
      Evidence: a consent-governed personal-data read log that identifies the applicable consent.
      Source: DRS-8, consent-reference bullet.
    test: resources/testing.md#drs-8
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry records the data viewer's role, organisation and location with a personal-data read event.
    documentation: |
      Evidence: a representative personal-data read log containing all three attributes.
      Optionality mapping: DRS-8 ends the bullet with `(optional)` after the device fingerprint; this statement reads the marker as scoping only the device fingerprint, so role, organisation and location stay required.
      Source: DRS-8, final bullet excluding the separately optional device fingerprint (spec/6-functional-requirements.md:153).
    test: resources/testing.md#drs-8
  - id: null
    status: DRAFT
    level: RECOMMENDED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry records the viewer device fingerprint with a personal-data read event.
    documentation: |
      Evidence: a representative personal-data read log containing a device fingerprint.
      Optionality mapping: DRS-8 marks the device fingerprint optional; the framework represents this skippable additional log attribute as RECOMMENDED.
      Source: DRS-8, final bullet.
    test: resources/testing.md#drs-8
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator mark a registry field as secret.
    documentation: |
      The source example is a credit-card-number field.
      Source: DRS-15, opening sentence and first bullet.
    test: resources/testing.md#drs-15
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry encrypts secret field data while the data is at rest.
    documentation: |
      Evidence: storage design and configuration, plus verification that representative secret field data is not stored in plaintext.
      Source: DRS-15, first bullet.
    test: resources/testing.md#drs-15
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: PROTOCOL
    contract: null
    statement: The Digital Registry encrypts information in transit between Building Blocks under the rules of the Information Mediator Building Block.
    documentation: |
      Evidence: integration configuration and a transport trace showing encrypted communication.
      Contract gap: the source cites the Information Mediator Building Block but gives no versioned publication identifier or section.
      Source: DRS-15, second bullet.
    test: resources/testing.md#drs-15
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator add a unique encryption key for each database.
    documentation: |
      Constraint: the source states that each database has a unique encryption key defined by the analyst.
      Source: DRS-18, opening sentence and second bullet.
    test: resources/testing.md#drs-18
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry uses the configured database encryption key to encrypt and decrypt data for that database.
    documentation: |
      Evidence: encryption configuration and a controlled encryption-and-decryption verification for one database.
      Source: DRS-18, first bullet.
    test: resources/testing.md#drs-18
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry blinds the configured database encryption key in the user interface.
    documentation: |
      Source: DRS-18, third bullet.
    test: resources/testing.md#drs-18
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: read
    statement: The Digital Registry requires an application to know the database encryption key before the application reads encrypted data through the API.
    documentation: |
      The source states that applications `must know` the encryption key. This migration retains that contract without redesigning key handling.
      Contract gap: the `read` operation request defines no field for the encryption key that the source says applications must know (spec/6-functional-requirements.md:234).
      Source: DRS-18, fourth bullet.
    test: resources/testing.md#drs-18
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator configure the unique data-owner identifier accepted as input to the personal-data usage report API.
    documentation: |
      Source: DRS-35, item 1.
    test: resources/testing.md#drs-35
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry decrypts encrypted registry data for display in the user interface.
    documentation: |
      Source: DRS-18, fourth bullet.
    test: resources/testing.md#drs-18
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: When a registry schema stores personal data, the Digital Registry lets an authorised operator link that personal data to its owner.
    documentation: |
      Condition: the registry schema is designed to store personal data.
      Source: DRS-35, item 2.
    test: resources/testing.md#drs-35
---

# Audit and Personal Data Protection

This functionality consolidates the overlapping audit and personal-data obligations in DRS-7, DRS-8, DRS-15, DRS-18, DRS-35 and DRS-37 without duplicating shared behaviour. The source makes personal-data field tagging and owner-identifier tagging optional in DRS-13 and DRS-14, while requiring personal-data logs, owner linking and owner reports here. That cross-clause ambiguity is preserved rather than resolved by adding a hidden dependency.

The database-key requirements retain the source contract, including application knowledge of a key and user-interface decryption. This format migration does not endorse or redesign that security model.
