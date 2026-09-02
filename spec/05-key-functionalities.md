---
description: Capability families provided by the Digital Registries Building Block.
---

# 5 Key Functionalities: API Families

The Digital Registries Building Block groups its externally visible capabilities into eight families. A family describes an adopter outcome and a coherent trust boundary. It does not prescribe an internal module, product architecture, or transport.

Only **Consultation Retrieve** is part of the target Base Registry Profile. The other Consultation sub-patterns and seven other families are informative in this release. They are not claimable because they do not yet have approved requirements, contracts, and tests.

<figure><img src=".gitbook/assets/api-families.svg" alt="Digital Registries Building Block capability families"><figcaption>Registry Core provides the shared foundation. The target Base Registry Profile adds Consultation Retrieve.</figcaption></figure>

## 5.1 Reading capability requirements

Requirements are placed with the capability to which they apply. Shared requirements are defined under [Registry Core](05-api-families/registry-core.md), while family-specific requirements are defined on the applicable family page.

Each requirement follows the GovStack Requirements Model. `DRAFT` means that the requirement is available for review but is not included in certification. Requirement identifiers are permanently reserved even while the requirement is DRAFT.

This organisation and the capability-specific requirement namespaces are provisional pending resolution of [GovStack CFR issue #7](https://github.com/GovStackWorkingGroup/cfr-architecture/issues/7) on optional capabilities and conformance profiles.

This release contains only requirements that support the target Base Registry Profile. Informative capability descriptions do not create requirements or have conformance effect.

## 5.2 Registry Core

Registry Core provides the identity, metadata, Record reference, semantic, lifecycle, and provenance foundation shared by every API family. It is not itself an API family. Every family-specific profile inherits the [Registry Core model and requirements](05-api-families/registry-core.md) rather than restating them.

## 5.3 Family catalogue

| Family | Adopter outcome | Capability patterns | Status in this release |
|---|---|---|---|
| [Consultation](05-api-families/consultation.md) | Obtain a permitted representation of Registry information. | Retrieve, Existence Check, List, Search, Revision History, Record Match, GIS Query | Retrieve is in the target Base Registry Profile; other patterns are informative. |
| [Provisioning](05-api-families/provisioning.md) | Configure a Registry service and publish its externally visible contracts. | Metadata administration, schemas, capability publication, bulk transfer | Informative |
| [Evidence](05-api-families/evidence.md) | Obtain a signed assertion derived from authoritative Registry information. | Direct attestation, wallet-mediated credential, status | Informative |
| [Write](05-api-families/write.md) | Create a Record or accept a new authoritative revision. | Direct write, governed write, correction | Informative |
| [Notification](05-api-families/notification.md) | Inform authorised subscribers that Registry state changed. | Subscribe, filter, deliver, retry, replay | Informative |
| [Aggregate Data](05-api-families/aggregate-data.md) | Obtain approved statistics derived from Registry Records. | Aggregate query, dataset metadata, published release | Informative |
| [Access Transparency](05-api-families/access-transparency.md) | Obtain a permitted view of access to a related Record. | Access-history consultation | Informative |
| [Identity Federation](05-api-families/identity-federation.md) | Authenticate a person represented by a sectoral Registry Record to a Relying Service and release authorised claims. | Profile ownership and binding to be decided with the Identity team | Informative; cross-BB ownership unresolved |

## 5.4 Selecting families

An adopter selects capabilities from the Registry's institutional responsibilities, domain model, and consumer needs, not from the feature list of a particular product. Useful questions include:

- Does the Registry expose only current Records, or also search, historical revisions, mutation, events, evidence, statistics, or subject authentication?
- Which actors can invoke each capability, and what may each actor learn?
- Does the Registry own an approval process, or accept an approved result from another service?
- Does the consumer need live Registry information, a portable proof, or notification that state changed?
- Which sector semantic model and protocol binding fit the participating systems?

Each family page states its boundary and maturity. A registry or sector profile supplies the domain-specific schemas, lifecycle vocabulary, query semantics, and other constraints needed by its selected capabilities. A capability without published requirements, a binding, and tests cannot be included in a GovStack conformance claim for this release.
