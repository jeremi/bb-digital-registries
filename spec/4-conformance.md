---
description: Draft minimum conformance and future capability model for Digital Registries.
---

# 4 Conformance

## 4.1 Requirement maturity

All requirements in the 3.0.0-alpha.2 specification are classified as DRAFT. They do not create a certification obligation.

## 4.2 Target Base Registry Profile

The provisional name for the target minimum conformance claim is the **Base Registry Profile**. Its formal treatment as a profile, and the conditional applicability of additional capabilities, depend on equivalent support in the GovStack Common Requirements Framework. It is not claimable in this alpha because its requirements are DRAFT and no canonical contract or executable test suite is published.

Once approved, an implementation claiming this profile:

1. satisfies the Registry Core requirements;
2. implements the Consultation Retrieve sub-pattern;
3. identifies the Digital Registries specification version it implements;
4. returns records under an identified schema and published semantic model; and
5. satisfies the applicable GovStack Cross-Functional Requirements.

Retrieve does not imply public access or disclosure of the complete stored record. It means that an authorised API consumer can request a record by its stable identifier and receive the current permitted representation or a policy-appropriate error response.

## 4.3 Future additional capability claims

After the Common Requirements Framework supports conditional capability applicability, an approved Digital Registries release may allow an implementation to claim additional families and Consultation sub-patterns. Once claimed, every applicable REQUIRED requirement, operation, contract, and test for that capability becomes part of its conformance claim.

Capabilities described only for architectural context, without approved requirements, contracts, and tests, are not claimable in this release.

## 4.4 Adaptors

An existing registry does not need to replace its internal software to conform. An adaptor may translate an existing interface into the operations, metadata, outcomes, and bindings required by a claimed profile. Conformance applies to the resulting external behaviour.
