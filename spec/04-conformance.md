---
description: Draft minimum conformance and capability model for Digital Registries.
---

# 4 Conformance

## 4.1 Requirement maturity

All requirements in the 3.0.0-alpha.2 specification are classified as DRAFT. They do not create a certification obligation.

Each requirement follows the GovStack Requirements Model. Requirement identifiers are permanently reserved even while the requirement is DRAFT. Cross-family requirements are defined under [Registry Core](05-api-families/registry-core.md#registry-core-functional-requirements), while family-specific requirements are defined on the applicable API-family page.

## 4.2 Inherited cross-functional requirements

This specification extends `govstack-cfr-2.1.0`. Every parent requirement applies with its original classifier and applicability conditions unless a Digital Registries requirement explicitly identifies a permitted extension or replacement under the GovStack Requirements Model.

This release defines no Registry-specific cross-functional extension or replacement. It does not impose a jurisdiction-specific security framework, a universal legal basis for data processing, or one deletion policy on every type of Registry.

## 4.3 Target Base Registry Profile

The provisional name for the target minimum conformance claim is the **Base Registry Profile**. Its formal treatment as a profile, and the conditional applicability of additional capabilities, depend on equivalent support in the GovStack Common Requirements Framework. It is not claimable in this alpha because its requirements are DRAFT and no canonical contract or executable test suite is published.

Once approved, an implementation claiming this profile:

1. satisfies the [Registry Core requirements](05-api-families/registry-core.md#registry-core-functional-requirements);
2. implements the [Consultation Retrieve](05-api-families/consultation.md#retrieve-functional-requirements) sub-pattern;
3. identifies the Digital Registries specification version it implements;
4. returns records in an identified representation format under an identified schema and published semantic model; and
5. satisfies the applicable `govstack-cfr-2.1.0` requirements.

Retrieve does not imply public access or disclosure of the complete stored record. It means that an authorised API consumer can request a record by its stable identifier and receive the current permitted representation or a policy-appropriate unsuccessful outcome.

## 4.4 Additional capability claims

After the Common Requirements Framework supports conditional capability applicability, an approved Digital Registries release may allow an implementation to claim additional families and Consultation sub-patterns. Once claimed, every applicable REQUIRED requirement, operation, contract, and test for that capability becomes part of its conformance claim.

Capabilities described only for architectural context, without approved requirements, contracts, and tests, are not claimable in this release.

## 4.5 Adaptors

An existing registry does not need to replace its internal software to conform. An adaptor may translate an existing interface into the operations, metadata, outcomes, and bindings required by a claimed profile. Conformance applies to the resulting external behaviour.
