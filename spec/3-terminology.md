---
description: Terms with a specific meaning in this specification.
---

# 3 Terminology

This specification uses the [GovStack Common Terminology](https://specs.govstack.global/architecture/2-common-terminology). The following terms have a specific meaning for Digital Registries.

| Term | Definition |
|---|---|
| API Consumer | A system authorised to invoke a Registry service interface. |
| API Family | A coherent group of operations that provides one Registry capability. |
| Authoritative Source | A source for which a named authority accepts responsibility within a declared domain and scope. Authoritative does not imply error-free. |
| Binding | A mapping of abstract operations to a transport or established protocol. |
| Capability Claim | A declaration that an implementation supports a specified API family, sub-pattern, and binding and meets the requirements attached to that claim. |
| Conformance Profile | A defined combination of core requirements and capability claims. |
| Functional Identifier | An identifier issued and lifecycle-managed for a sector-specific purpose, such as a farmer, student, health, or professional identifier. |
| Lifecycle State | The current state of a Record under the vocabulary defined by its declared representation schema. |
| Permitted Representation | The record data and metadata an API consumer is authorised to receive. It may be filtered or redacted and need not contain the complete stored record. |
| Record | The Registry's representation of an entity, place, asset, or event within its declared scope. |
| Record Identifier | A stable identifier assigned to a record within a Registry. |
| Record Principal | A person or organisation with a recognised relationship to a record, such as its subject, owner, title holder, director, or credential holder. |
| Record Revision | A representation of a record at a defined point in its change history. |
| Registry Authority | The institution accountable for the Registry and its declared authoritative scope. |
| Registry Core | Behaviour and metadata required of every conformant Registry implementation. |
| Registry Identifier | A globally unique and stable identifier for a Registry. |
| Registry Operator | The organisation that operates an implementation on behalf of, or as, the Registry Authority. |
| Relying Service | A service that relies on authentication or claims provided through the Identity Federation family. |
| Schema | A machine-readable definition of the structure and validation constraints of records or messages. |
| Semantic Model | The vocabulary and domain meaning of data carried in a Registry record. |
| Sub-pattern | An independently claimable capability within an API family. |
