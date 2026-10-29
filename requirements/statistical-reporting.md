---
title: Statistical Reporting
description: |
  Registry operators inspect standard and field-configurable analyses of registry data.
realises: [analytics]
conformance: CORE
requirements:
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry produces standard statistical reports for a registry.
    documentation: |
      Source: DRS-26, item 1.
    test: resources/testing.md#drs-26
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry shows statistics for all registered items and lets a user filter those statistics by multiple criteria.
    documentation: |
      The source examples are details of registered people, details of registered services, changes in registrations of people or services over time, and details of changes to data elements from audit logs.
      Source: DRS-26, item 1.1.
    test: resources/testing.md#drs-26
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets a user generate a report configured from fields registered in the registry.
    documentation: |
      Source: DRS-26, item 1.2.
    test: resources/testing.md#drs-26
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an analyst or user analyze data collected in the system in various ways.
    documentation: |
      This preserves the general analysis capability stated separately from the report examples in the source.
      Source: DRS-26, item 2 (spec/6-functional-requirements.md:315).
    test: resources/testing.md#drs-26
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: list
    statement: The Digital Registry provides an API operation that extracts registry records for analysis in an external data-analytics system.
    documentation: |
      Constraint: the API exposes data for external analysis, such as with Tableau.
      Binding interpretation: the source names no extraction operation; `list` is the operation that returns registry records and is the closest match, and no export-specific parameters are inferred.
      Source conflict: the DRS-26 header reads `should have the ability to (REQUIRED)`, so the source does not settle whether this item is a recommendation or a requirement; the migration keeps it REQUIRED.
      The source requires an analytics extraction API here while DRS-36 separately makes statistical queries through an API optional. This requirement does not require the statistical query behaviour of DRS-36.
      Source: DRS-26, item 2.2.
    test: resources/testing.md#drs-26
  - id: null
    status: DRAFT
    level: RECOMMENDED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator build a custom dashboard for analysing data within a registry database.
    documentation: |
      Optionality mapping: DRS-26 labels custom dashboards as an option. The framework represents this skippable additional analysis behaviour as RECOMMENDED.
      Source conflict: chapter 4 item 16 (spec/4-key-digital-functionalities.md:47), `Generate dashboards and administrative reports`, sits under a chapter of core functions, while DRS-26 (spec/6-functional-requirements.md:316) marks custom dashboards as an option.
      Source: DRS-26, item 2.1.
    test: resources/testing.md#drs-26
---

# Statistical Reporting

The required functionality preserves standard reports, filtering, field-configured reports and extraction of registry records for an external analytics system. The optional custom-dashboard subclause remains a RECOMMENDED behaviour in the same core functionality. DRS-26 and DRS-36 use overlapping API language with different conformance levels; this migration records the ambiguity without making either one depend on the other.
