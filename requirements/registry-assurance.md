---
title: Apply Registry Assurance
description: Institutions retain the two explicitly elevated upstream cross-functional data protections.
realises:
- governed-access
- accountability
conformance: CORE
requirements:
- id: null
  status: DRAFT
  level: REQUIRED
  observability: AUDITABLE
  mutability: EXTENSIBLE
  interaction: INTERNAL
  statement: The Digital Registry complies with high-quality data-protection principles.
  documentation: 'Constraint: Upstream chapter 5 elevates govstack-bb-registries-cfr-data#req-4 from RECOMMENDED EXTENSIBLE AUDITABLE to REQUIRED EXTENSIBLE AUDITABLE. The inherited requirement is referenced at https://specs.govstack.global/architecture/6-cross-functional-requirements/6.6-data#id-4-comply-with-high-quality-data-protection-principles-recommended-extensible-auditable-previously-5 .

    Evidence: data-protection documentation mapping each inherited principle to the implementation, with supporting configuration.

    Source: CFR-DATA-4.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: AUDITABLE
  mutability: REPLACEABLE
  interaction: INTERNAL
  statement: The Digital Registry preserves logical records when deleting records unless hard deletion is mandated by law.
  documentation: 'Constraint: Upstream chapter 5 elevates govstack-bb-registries-cfr-data#req-7 from RECOMMENDED REPLACEABLE AUDITABLE to REQUIRED REPLACEABLE AUDITABLE. The original inherited reference remains in resources/cross-functional-requirements.md.

    Evidence: storage state for a logically deleted record, and documentation of any legally mandated hard-deletion case.

    Source: CFR-DATA-7.'
  test: resources/testing.md#supplementary
---

The YAML requirements retain the source obligations identified in the migration ledger. The supporting descriptions and contracts remain under `resources/`.
