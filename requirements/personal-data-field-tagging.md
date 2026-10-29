---
title: Personal Data Field Tagging
description: |
  Registry operators may identify fields that contain personal data.
realises: [accountability, governed-access]
conformance: CORE
requirements:
  - id: null
    status: DRAFT
    level: RECOMMENDED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator mark a field as a `PersonalData` log object that contains personal data.
    documentation: |
      Optionality mapping: DRS-13 marks this field-level capability OPTIONAL. In the framework, a behaviour that improves the core and may be skipped is represented by a RECOMMENDED requirement.
      Source: DRS-13.
    test: resources/testing.md#drs-13
---

# Personal Data Field Tagging

The source makes this marking optional while DRS-8 and DRS-37 require personal-data logs and reports that depend on personal-data identification. The migration preserves both statements and records the cross-clause ambiguity without making this recommendation a hidden core dependency.
