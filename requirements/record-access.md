---
title: Record Access
description: |
  Client systems process authorised registry records through OpenAPI services.
realises: [record-management, governed-access]
conformance: CORE
requirements:
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: list
    statement: The Digital Registry provides an OpenAPI operation through which an authorised client searches registry records.
    documentation: |
      Source: DRS-33, applicant search bullet.
    test: resources/testing.md#drs-33
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: create
    statement: The Digital Registry provides an OpenAPI operation through which an authorised client creates a registry record.
    documentation: |
      Source: DRS-33, applicant create bullet.
    test: resources/testing.md#drs-33
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: read
    statement: The Digital Registry provides an OpenAPI operation through which an authorised client reads a registry record.
    documentation: |
      Source: DRS-33, applicant read bullet.
    test: resources/testing.md#drs-33
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: update
    statement: The Digital Registry provides an OpenAPI operation through which an authorised client updates a registry record.
    documentation: |
      Source: DRS-33, applicant update bullet.
    test: resources/testing.md#drs-33
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: delete
    statement: The Digital Registry provides an OpenAPI operation through which an authorised client deletes a registry record.
    documentation: |
      Source: DRS-33, applicant delete bullet.
    test: resources/testing.md#drs-33
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: update-or-create
    statement: The Digital Registry provides an OpenAPI operation through which an authorised client creates or updates a registry record.
    documentation: |
      Source: DRS-33, applicant create-or-update bullet.
    test: resources/testing.md#drs-33
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry authorises client systems and users before they process registry records.
    documentation: |
      Evidence: access-control policy and audit records showing allowed and denied client and user requests.
      Source: DRS-33, authorisation paragraph.
    test: resources/testing.md#drs-33
---

# Record Access

DRS-33 describes CRUD and search operations exposed to client systems. The operation identifiers above are the matching operations in the source Data API. The source also contains the domain-specific `GDB-MCTS-create-entries` operation and the distinct `updateEntries` operation, but DRS-33 does not require those behaviours, so this migration does not bind them by inference.
