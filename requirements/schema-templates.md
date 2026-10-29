---
title: Use Registry Schema Templates
description: |
  Authorised users create registries from reusable, versioned templates and exchange those templates.
realises: [registry-administration]
conformance: EXTENSION
extension: schema-templates
requirements:
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to create a registry from a schema template.
    documentation: |
      Source: DRS-20.
    test: resources/testing.md#drs-20
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to share a registry schema template with other users of the same system instance.
    documentation: |
      Source: DRS-20 calls this an internal marketplace.
    test: resources/testing.md#drs-20
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: FILE
    statement: The Digital Registry exports a registry schema template.
    documentation: |
      Constraint: a complete template contains the full registry, its schema, its views, and its API configuration.
      Source conflict: spec/6-functional-requirements.md:260 includes views in a full registry template, while DRS-9 makes database views OPTIONAL; the source does not say what a template contains when the Database Views extension is not claimed.
      Format gap: the source defines no registry-template package format.
      Source: DRS-20.
    test: resources/testing.md#drs-20
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: FILE
    statement: The Digital Registry imports a registry schema template.
    documentation: |
      Constraint: a complete template contains the full registry, its schema, its views, and its API configuration.
      Source conflict: spec/6-functional-requirements.md:260 includes views in a full registry template, while DRS-9 makes database views OPTIONAL; the source does not say what a template contains when the Database Views extension is not claimed.
      Format gap: the source defines no registry-template package format.
      Source: DRS-20.
    test: resources/testing.md#drs-20
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to share a registry schema template through a marketplace.
    documentation: |
      Source: DRS-20. The source does not define a marketplace protocol or say whether the marketplace is part of the Digital Registry.
    test: resources/testing.md#drs-20
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry maintains versions of registry schema templates in a template repository.
    documentation: |
      Source: DRS-20.
    test: resources/testing.md#drs-20
  - id: null
    status: DRAFT
    level: RECOMMENDED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry provides domain templates for Health, Business, and Farmer registries.
    documentation: |
      Source: DRS-20 explicitly marks domain templates optional within the optional template functionality. The format represents this nested source OPTIONAL feature as RECOMMENDED within the Schema Templates extension.
    test: resources/testing.md#drs-20
---

DRS-20 makes schema templates optional as a whole. The functionality is therefore an independently claimable extension, and all non-optional DRS-20 behaviour is required for a solution that claims it.
