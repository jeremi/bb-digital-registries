---
description: Draft Registry Core and Consultation Retrieve requirements.
---

# 6 Functional Requirements

## 6.1 Reading the requirements

This release contains only requirements that support the target Base Registry Profile. Additional families are described in [Key Functionalities](5-key-functionalities.md) but have no requirements or conformance effect in this release.

Each requirement follows the GovStack Requirements Model. `DRAFT` means that the requirement is available for review but is not included in certification. Requirement identifiers are permanently reserved even while the requirement is DRAFT.

## 6.2 Registry Core

Registry Core requirements apply globally rather than to one Key Functionality.

### #1 Publish Registry service metadata

`govstack-bb-digital-registries-fr-core#req-1`

`DRAFT EXTENSIBLE AUDITABLE`

An implementation publishes machine-readable service metadata containing a globally unique and stable Registry Identifier, a human-readable Registry name, the identity of the Registry Authority, the Digital Registries specification version, and the GovStack CFR version it implements.

**Purpose:** An adopter can determine which Registry and authority stand behind a service and which complete set of requirements applies.

**Prerequisite:** The Registry Authority and authoritative scope have been established by the adopting organisation.

**Verification:** Inspect the published service metadata, validate that all required values are present, and review evidence that the Registry Identifier is not shared with another Registry or changed between service revisions.

### #2 Identify each returned Record

`govstack-bb-digital-registries-fr-core#req-2`

`DRAFT EXTENSIBLE OBSERVABLE`

Every returned Record representation includes the Registry Identifier and a Record Identifier that is unique within that Registry. Together, the two identifiers uniquely identify the Record.

**Purpose:** Consumers can distinguish Records from different Registries and refer to one Record without depending on mutable domain attributes.

**Prerequisite:** A Record has been accepted into the Registry.

**Verification:** Retrieve two distinct Record fixtures and verify that each response carries the expected Registry Identifier and a different Record Identifier.

### #3 Preserve Record Identifiers

`govstack-bb-digital-registries-fr-core#req-3`

`DRAFT EXTENSIBLE AUDITABLE`

An implementation keeps a Record Identifier unchanged throughout that Record's lifecycle and revisions and never reassigns the identifier to a different Record.

**Purpose:** A Record reference remains unambiguous after changes, retirement, archival, or deletion.

**Prerequisite:** The implementation has a documented Record Identifier lifecycle policy.

**Verification:** Review the identifier policy and evidence showing that successive revisions retain the same identifier, distinct Records do not share an identifier, and retired identifiers are not returned to the allocation pool.

### #4 Identify the Record schema and semantic model

`govstack-bb-digital-registries-fr-core#req-4`

`DRAFT EXTENSIBLE OBSERVABLE`

Every returned Record representation identifies a resolvable machine-readable schema and the published semantic model that govern its domain data.

**Purpose:** Consumers can validate the structure of a representation and interpret its domain meaning without knowledge of the implementation's internal storage.

**Prerequisite:** The Registry Authority has selected the applicable schema and semantic model.

**Verification:** Retrieve a Record, resolve the declared schema, validate the representation, and resolve the semantic-model identifier to its published definition.

### #5 Identify the current revision and lifecycle state

`govstack-bb-digital-registries-fr-core#req-5`

`DRAFT EXTENSIBLE OBSERVABLE`

Every returned Record representation identifies its current revision and a lifecycle state permitted by the representation's declared schema.

**Purpose:** Consumers can distinguish the current representation from earlier revisions and interpret its declared state.

**Prerequisite:** The selected representation schema defines the supported lifecycle-state vocabulary.

**Verification:** Retrieve fixtures in each lifecycle state exposed through Consultation, validate each state against the declared schema, and verify that each response identifies a current revision.

### #6 Provide minimum Record provenance

`govstack-bb-digital-registries-fr-core#req-6`

`DRAFT EXTENSIBLE OBSERVABLE`

Every returned Record representation identifies the Registry Authority as the responsible source and provides the time at which the current revision was recorded.

**Purpose:** A consumer can assess the institutional source and currency of the authoritative information.

**Prerequisite:** The Registry captures provenance for each accepted revision.

**Verification:** Retrieve a Record and verify that the representation contains the Registry Authority identifier and recording time. Additional protected provenance details are outside this minimum requirement.

## 6.3 Consultation Retrieve

The following requirements link to the Consultation Key Functionality intended for the Base Registry Profile.

### #1 Retrieve the current Record by identifier

`govstack-bb-digital-registries-fr-consultation#req-1`

`DRAFT EXTENSIBLE OBSERVABLE`

`KF: Consultation`

Given a valid Record Identifier and an authorised request, an implementation returns the current permitted representation of that Record without modifying the Record.

**Purpose:** An API consumer that already knows a Record Identifier can obtain authoritative Registry information without using search or enumeration.

**Prerequisite:** An authorised API consumer and an accessible Record fixture exist.

**Verification:** Retrieve a known Record by identifier, verify the Registry and Record identifiers, current revision, lifecycle state, schema, semantic model, minimum provenance, and permitted domain data, and confirm that a subsequent Retrieve returns the same revision when no intervening change occurred.

### #2 Apply disclosure rules to the returned representation

`govstack-bb-digital-registries-fr-consultation#req-2`

`DRAFT EXTENSIBLE OBSERVABLE`

`KF: Consultation`

An implementation returns only the Record fields and metadata permitted for the authenticated API consumer and request context.

**Purpose:** Retrieve does not become an entitlement to the complete stored Record.

**Prerequisite:** At least two test consumers have different disclosure entitlements for the same Record.

**Verification:** Retrieve the same Record using both consumers and verify that each receives only its permitted projection and that omitted values are not exposed through errors or metadata returned to the consumer.

### #3 Hide protected Record existence

`govstack-bb-digital-registries-fr-consultation#req-3`

`DRAFT EXTENSIBLE OBSERVABLE`

`KF: Consultation`

For an API consumer that is not authorised to learn whether a protected Record exists, an implementation returns an error response that is indistinguishable under the published Retrieve contract from the response for an unknown Record Identifier. This includes the same status or error category, security-relevant headers, stable problem type or code, response schema, and non-Record-specific problem values. Per-request correlation values may differ when they are generated independently of Record existence. The response contains no Record-specific data.

**Purpose:** An unauthorised consumer cannot enumerate protected Record Identifiers through the Retrieve error contract.

**Prerequisite:** An unknown Record Identifier and a protected Record Identifier are available as test fixtures for the same consumer.

**Verification:** Retrieve both identifiers as that consumer and compare the status or error category, security-relevant headers, problem type or code, response schema, non-Record-specific problem values, and data fields. Verify that any differing correlation values are independent of Record existence and that neither response exposes Record-specific data.

## 6.4 Deferred capabilities

No requirement identifier is assigned to Provisioning, additional Consultation sub-patterns, Evidence, Write, Notification, Aggregate Data, Access Transparency, or Identity Federation in this release.
