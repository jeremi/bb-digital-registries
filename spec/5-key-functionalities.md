---
description: Capability families provided by the Digital Registries Building Block.
---

# 5 Key Functionalities: API Families

The Digital Registries Building Block groups its externally visible capabilities into eight families. A family describes an adopter outcome and a coherent trust boundary. It does not prescribe an internal module, product architecture, or transport.

Only **Consultation Retrieve** is part of the target Base Registry Profile. The other Consultation sub-patterns and seven other families are informative in this release. They are not claimable because they do not yet have approved requirements, contracts, and tests.

<figure><img src=".gitbook/assets/api-families.svg" alt="Digital Registries Building Block capability families"><figcaption>Registry Core provides the shared foundation. The target Base Registry Profile adds Consultation Retrieve.</figcaption></figure>

## 5.1 Family catalogue

| Family | Adopter outcome | Capability patterns | Status in this release |
|---|---|---|---|
| [Consultation](5-api-families/consultation.md) | Obtain a permitted representation of Registry information. | Retrieve, List, Search, Record Match, GIS Query | Retrieve is in the target Base Registry Profile; other patterns are informative. |
| [Provisioning](5-api-families/provisioning.md) | Configure a Registry service and publish its externally visible contracts. | Service metadata, schemas, capability publication, bulk transfer | Informative |
| [Evidence](5-api-families/evidence.md) | Obtain a signed assertion derived from authoritative Registry information. | Direct attestation, wallet-mediated credential, status | Informative |
| [Write](5-api-families/write.md) | Create a Record or accept a new authoritative revision. | Direct write, governed write, correction | Informative |
| [Notification](5-api-families/notification.md) | Inform authorised subscribers that Registry state changed. | Subscribe, filter, deliver, retry, replay | Informative |
| [Aggregate Data](5-api-families/aggregate-data.md) | Obtain approved statistics derived from Registry Records. | Aggregate query, dataset metadata, published release | Informative |
| [Access Transparency](5-api-families/access-transparency.md) | Obtain a permitted view of access to a related Record. | Access-history consultation | Informative |
| [Identity Federation](5-api-families/identity-federation.md) | Authenticate a person represented by a sectoral Registry Record to a Relying Service and release authorised claims. | OpenID Provider and claim release | Informative |

## 5.2 Selecting families

An adopter selects capabilities from the Registry's institutional responsibilities and consumer needs, not from the feature list of a particular product. Useful questions include:

- Does the Registry expose only current Records, or also search, mutation, events, evidence, statistics, or subject authentication?
- Which actors can invoke each capability, and what may each actor learn?
- Does the Registry own an approval process, or accept an approved result from another service?
- Does the consumer need live Registry information, a portable proof, or notification that state changed?
- Which sector semantic model and protocol binding fit the participating systems?

Each family page states its boundary and maturity. Candidate operations and bindings on informative pages are design inputs, not implementation obligations.
