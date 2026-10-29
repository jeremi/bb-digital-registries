---
title: Service Usage Statistics
description: |
  Registry operators retain usage records for API services and searches.
realises: [analytics, accountability]
conformance: EXTENSION
extension: service-usage-statistics
requirements:
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry records usage information for every API service invocation.
    documentation: |
      Evidence: usage records produced by invocations of each exposed API service.
      Source: DRS-12, first nested bullet.
    test: resources/testing.md#drs-12
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry records every search made through the registry user interface.
    documentation: |
      Evidence: usage records produced by searches through the user interface.
      Source: DRS-12, second nested bullet.
    test: resources/testing.md#drs-12
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry records every search made through a registry API.
    documentation: |
      Evidence: usage records produced by searches through the API.
      Source: DRS-12, second nested bullet.
    test: resources/testing.md#drs-12
---

# Service Usage Statistics

DRS-12 marks the whole functionality OPTIONAL. A solution that claims this extension records both API service use and searches made at the two named boundaries.
