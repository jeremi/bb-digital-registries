---
description: Cross-functional requirements inherited by Digital Registries.
---

# 7 Cross-Functional Requirements

`govstack-bb-digital-registries-3.0.0-alpha.2 extends govstack-cfr-2.1.0`

Every requirement from `govstack-cfr-2.1.0` applies according to its classifier and any applicability condition stated in that requirement, without being repeated in this specification.

The inherited requirements cover, among other concerns:

- authentication, authorisation, transport security, encryption, secrets, and security logging;
- API documentation, observability, availability, deployment, and maintainability;
- Unicode, timestamps, data formats, validation, portability, provenance, retention, and sensitivity classification; and
- use and publication of appropriate domain schemas and standards.

This release defines no additional Registry-specific cross-functional requirement. In particular, it does not impose a jurisdiction-specific security framework, a universal legal basis for data processing, or one deletion policy on every type of Registry.

Registry-specific behaviour that produces direct business value, such as the permitted representation returned by Consultation, remains in [Functional Requirements](6-functional-requirements.md) rather than being hidden in this chapter.
