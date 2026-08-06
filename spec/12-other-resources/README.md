---
description: Coverage, decisions, migration material, and references.
---

# 12 Other Resources

## 12.1 Coverage and limitations

The 3.0.0-alpha.2 specification provides a minimum Registry model and DRAFT requirements. It does not provide a certification-ready API contract.

| Included in this release | Not specified in this release |
|---|---|
| Registry scope and exclusions | Final capability-discovery format |
| Base Registry Profile | Canonical HTTP path and JSON schema |
| Registry Core DRAFT requirements | Retrieval of historical revisions |
| Consultation Retrieve DRAFT requirements | Optional-family requirements and tests |
| Conceptual external data model | Named multi-family conformance profiles |
| Retrieve workflow and verification intent | Domain-specific semantic models |
| Complete disposition of previous DRS requirements | Jurisdiction-specific governance or legal compliance |

## 12.2 Specification decisions

- The specification defines the external service behaviour of a Digital Registries implementation for records under a Registry Authority's declared scope. It does not prescribe a database platform.
- The proposed Base Registry Profile consists of Registry Core plus Consultation Retrieve.
- Retrieve returns a permitted representation and does not imply public or complete-record access.
- List, Search, Record Match, and GIS Query are distinct optional Consultation sub-patterns.
- Additional API families remain informative until each has requirements, a contract, and tests.
- Internal storage, administrative UI, deployment topology, multi-tenancy, and automatic API generation are implementation choices.
- Domain data models are selected and declared by the Registry Authority rather than standardised by the Building Block.
- Authentication protecting Registry APIs is distinct from the optional Identity Federation family.

## 12.3 Migration and history

- [Migration from the 3.0.0-alpha.1 Draft](migration-from-3.0.md) records the disposition of every previous DRS requirement.
- [Release Notes](../1-version-history/release-notes.md) preserve detailed historical contributors and changes.
- [Historical Key Decision Log](historical/key-decision-log.md) and [Historical Future Considerations](historical/future-considerations.md) are retained as working-group history. They are not part of conformance for this release.

The OpenAPI files under `api/legacy/generated-crud/` and Cucumber scenarios under `test/openAPI/` describe the previous generated CRUD interface. They are legacy artifacts and are not service contracts or conformance tests for this release.

## 12.4 Reference architecture and implementation guidance

Actors, organisational responsibilities, domain governance, semantic choices, and multi-Building-Block deployment patterns belong in a Registry Reference Architecture or implementation guide. They are useful to adopters but do not alter the technical conformance contract in this specification.

See [References](references.md) for standards and related GovStack material.
