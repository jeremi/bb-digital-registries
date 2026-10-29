---
title: Database Views
description: |
  Registry operators define read-only selections of registry data for governed reuse.
realises: [record-management, governed-access]
conformance: EXTENSION
extension: database-views
requirements:
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator create a view as a selection of data from a registry database.
    documentation: |
      Source: DRS-9, heading and first bullet.
    test: resources/testing.md#drs-9
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator expose a database view as Open Data to the `Anonymous` role.
    documentation: |
      Source: DRS-9, second bullet.
    test: resources/testing.md#drs-9
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: null
    statement: The Digital Registry exposes a configured database view through a custom read API operation.
    documentation: |
      Binding gap: the source API descriptions contain no operation for a custom database view.
      Source: DRS-9, third bullet.
    test: resources/testing.md#drs-9
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry prevents a database view from changing or deleting registry data.
    documentation: |
      Source: DRS-9, fourth bullet.
    test: resources/testing.md#drs-9
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry applies its user-rights management policies to access a database view.
    documentation: |
      Evidence: view-access policy and audit records showing an allowed and a denied access decision.
      Source: DRS-9, fifth bullet.
    test: resources/testing.md#drs-9
---

# Database Views

DRS-9 marks the whole functionality OPTIONAL. It is therefore an independently claimable extension, not a core obligation. A view is read-only and remains subject to the same rights-management system as other registry access.
