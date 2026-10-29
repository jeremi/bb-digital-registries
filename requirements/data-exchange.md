---
title: Automated Data Exchange
description: |
  Registry operators configure conditional exchanges between registries and external systems.
realises: [data-exchange]
conformance: CORE
requirements:
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator configure an automated exchange by mapping input and output registry fields.
    documentation: |
      Constraint: the mapping includes a query part and an answer part.
      Source: DRS-19, opening sentence and items 4 and 5.
    test: resources/testing.md#drs-19
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry runs a configured exchange after each configured time interval until every corresponding record has been processed.
    documentation: |
      Constraint: the automation runs as a loop and finishes when all corresponding records have been processed.
      Source: DRS-19, item 1.
    test: resources/testing.md#drs-19
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry processes one record at a time during an automated exchange.
    documentation: |
      Source: DRS-19, item 2.
    test: resources/testing.md#drs-19
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator configure exchange conditions that combine field comparisons with `AND` and `OR` operators.
    documentation: |
      The source calls these business rules in the Rules Engine and gives `field A = 123` as an example.
      Source: DRS-19, item 3.
    test: resources/testing.md#drs-19
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry copies mapped data to another registry database in the same system instance.
    documentation: |
      Source: DRS-19, item 4.1.
    test: resources/testing.md#drs-19
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: CONSUMED_API
    contract: null
    statement: The Digital Registry sends mapped data to an API of an external registry database.
    documentation: |
      Contract gap: the source requires an external API exchange but names no API contract or operation.
      Source: DRS-19, item 4.2 and expected outcome.
    test: resources/testing.md#drs-19
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: null
    statement: The Digital Registry supports webhook triggers for multi-registry orchestration of automated exchanges.
    documentation: |
      Source ambiguity: DRS-19 names `Webhook triggers (Multi-Registry Orchestration )` (spec/6-functional-requirements.md:249) but does not say whether the Digital Registry receives a webhook, publishes one, or observes it through another component. The statement keeps the source wording and leaves the interaction unresolved.
      Source: DRS-19, item 6.
    test: resources/testing.md#drs-19
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry supports many-to-one and one-to-many field mappings in an automated exchange.
    documentation: |
      Source: DRS-19, item 4 and the paragraph after item 6 (spec/6-functional-requirements.md:243 'mapping (input, output) registry data fields', :251 'from many to one and one to many'). Processing one record at a time (spec/6-functional-requirements.md:241) is retained as a separate requirement.
    test: resources/testing.md#drs-19
  - id: null
    status: DRAFT
    level: RECOMMENDED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator configure a transformation of mapped data into another format.
    documentation: |
      Optionality mapping: the source says that a mapping `may have` a transformation option. The framework represents this skippable behaviour as RECOMMENDED.
      The source example transforms `est` to `EST`.
      Source ambiguity: spec/6-functional-requirements.md:251 'Mapping may have a transformation option' sits in a REQUIRED block without an (Optional) tag; the migration keeps 'may' as a nonblocking recommendation.
      Source: DRS-19, paragraph after item 6.
    test: resources/testing.md#drs-19
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry activates a configured automated exchange when its configured conditions evaluate to true.
    documentation: |
      Source: DRS-19, expected outcome.
    test: resources/testing.md#drs-19
---

# Automated Data Exchange

DRS-19 combines scheduling, record-by-record processing, rule evaluation, field mapping, internal transfer, calls to external APIs, webhook triggers and optional transformation configuration. These are separate requirements because they cross different test boundaries. No unlisted external contract or webhook operation is inferred.
