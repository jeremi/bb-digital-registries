---
title: Owner Identifiers
description: |
  Registry operators may identify fields that link personal data to its owner.
realises: [accountability, governed-access]
conformance: CORE
requirements:
  - id: null
    status: DRAFT
    level: RECOMMENDED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator mark a field as `PersonalDataID`, the identifier of the data owner.
    documentation: |
      Optionality mapping: DRS-14 marks this field-level capability OPTIONAL. In the framework, a behaviour that improves the core and may be skipped is represented by a RECOMMENDED requirement.
      Source: DRS-14, opening sentence.
    test: resources/testing.md#drs-14
  - id: null
    status: DRAFT
    level: RECOMMENDED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator configure multiple owner identifiers, including national, passport and local identifiers.
    documentation: |
      Optionality mapping: this is nested under the OPTIONAL DRS-14 capability and remains RECOMMENDED.
      Source: DRS-14, first bullet.
    test: resources/testing.md#drs-14
  - id: null
    status: DRAFT
    level: RECOMMENDED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator configure validation rules for owner identifiers.
    documentation: |
      Optionality mapping: this is nested under the OPTIONAL DRS-14 capability and remains RECOMMENDED.
      Source: DRS-14, second bullet.
    test: resources/testing.md#drs-14
  - id: null
    status: DRAFT
    level: RECOMMENDED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: CONSUMED_API
    contract: null
    statement: The Digital Registry links an owner identifier to an external registry.
    documentation: |
      Contract gap: the source names no external registry contract or linking operation.
      Optionality mapping: this is nested under the OPTIONAL DRS-14 capability and remains RECOMMENDED.
      Source: DRS-14, third bullet.
    test: resources/testing.md#drs-14
  - id: null
    status: DRAFT
    level: RECOMMENDED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry prevents a configured immutable owner identifier from being changed.
    documentation: |
      Evidence: field policy and records showing rejection of an attempted change.
      Optionality mapping: this is nested under the OPTIONAL DRS-14 capability and remains RECOMMENDED.
      Source: DRS-14, fourth bullet.
    test: resources/testing.md#drs-14
---

# Owner Identifiers

DRS-14 makes owner-identifier marking optional. The nested identifier types, validation, external linking and immutable-enforcement statements remain source-scoped recommendations; they are not silently promoted to core obligations.
