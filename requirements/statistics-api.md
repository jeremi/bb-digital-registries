---
title: Statistical Queries API
description: |
  Authorised clients query registration and programme data for statistical use.
realises: [analytics, governed-access]
conformance: EXTENSION
extension: statistics-api
requirements:
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: null
    statement: The Digital Registry exposes registration data through a statistical-query API.
    documentation: |
      Binding gap: the source API descriptions contain no operation identified as the statistical-query API required by DRS-36.
      Source: DRS-36, item 1.1.
    test: resources/testing.md#drs-36
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: null
    statement: The Digital Registry exposes programme data through a statistical-query API.
    documentation: |
      Binding gap: the source API descriptions contain no operation identified as the statistical-query API required by DRS-36.
      Source: DRS-36, item 1.2.
    test: resources/testing.md#drs-36
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: null
    statement: The Digital Registry's statistical-query API accepts date and time ranges as query parameters.
    documentation: |
      Binding gap: the source API descriptions contain no operation identified as the statistical-query API required by DRS-36.
      Constraint: a query may combine these parameters (spec/6-functional-requirements.md:407 'querying data with multiple parameters').
      Source: DRS-36, item 2.1.
    test: resources/testing.md#drs-36
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: null
    statement: The Digital Registry's statistical-query API accepts a registered programme as a query parameter.
    documentation: |
      Binding gap: the source API descriptions contain no operation identified as the statistical-query API required by DRS-36.
      Constraint: a query may combine these parameters (spec/6-functional-requirements.md:407 'querying data with multiple parameters').
      Source: DRS-36, item 2.2.
    test: resources/testing.md#drs-36
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry limits statistical-query API results to data the caller is authorised to access.
    documentation: |
      Evidence: access-control policy and request-and-response records showing that unauthorised data is omitted or access is denied.
      Source: DRS-36, item 3.
    test: resources/testing.md#drs-36
---

# Statistical Queries API

DRS-36 marks this whole functionality OPTIONAL. It is independent of the required external-analytics extraction operation in DRS-26. The source gives no operation identifier for the statistical-query API, so the API requirements remain explicitly unbound drafts.
