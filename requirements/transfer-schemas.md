---
title: Transfer Registry Schemas
description: |
  Authorised users exchange registry schemas as JSON, YAML, or XLS files.
realises: [registry-administration]
conformance: CORE
requirements:
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: FILE
    statement: The Digital Registry exports a registry database schema as a JSON or YAML file.
    documentation: |
      Format gap: the source defines no schema export/import file format; the databaseSchema object of the database API and the Appendix 2 example show a JSON schema shape but are not declared as the export or import format.
      Source: DRS-10. The slash in "JSON/YAML" does not say whether every implementation must export both formats or may support one of them; this migration preserves that ambiguity.
    test: resources/testing.md#drs-10
  - id: null
    status: DRAFT
    level: RECOMMENDED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: FILE
    statement: The Digital Registry exports a registry database schema as an XLS file.
    documentation: |
      Format gap: the source defines no schema export/import file format; the databaseSchema object of the database API and the Appendix 2 example show a JSON schema shape but are not declared as the export or import format.
      Source: DRS-10 explicitly marks XLS export optional. The format represents this source OPTIONAL feature as RECOMMENDED in the core functionality.
    test: resources/testing.md#drs-10
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: FILE
    statement: The Digital Registry imports a registry database schema from a JSON or YAML file.
    documentation: |
      Format gap: the source defines no schema export/import file format; the databaseSchema object of the database API and the Appendix 2 example show a JSON schema shape but are not declared as the export or import format.
      Source: DRS-11. The slash in "JSON/YAML" does not say whether every implementation must import both formats or may support one of them; this migration preserves that ambiguity.
    test: resources/testing.md#drs-11
  - id: null
    status: DRAFT
    level: RECOMMENDED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: FILE
    statement: The Digital Registry imports a registry database schema from an XLS file.
    documentation: |
      Format gap: the source defines no schema export/import file format; the databaseSchema object of the database API and the Appendix 2 example show a JSON schema shape but are not declared as the export or import format.
      Source: DRS-11 explicitly marks XLS import optional. The format represents this source OPTIONAL feature as RECOMMENDED in the core functionality.
    test: resources/testing.md#drs-11
---

Section 4.1 lists schema import and export as registry lifecycle-management functions. DRS-10 and DRS-11 define the available file formats.
