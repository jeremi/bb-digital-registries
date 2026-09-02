---
description: Signed assertions derived from authoritative Registry information.
---

# Evidence

> **Status:** Informative and not claimable in this release. No Evidence requirements, credential profile, contract, or tests are published.

## Purpose and applicability

Evidence enables a Registry Authority to issue a signed assertion derived from authoritative Registry information without disclosing the underlying Record. It applies when a fact needs to be portable, independently verifiable, or more narrowly disclosed than a live Record representation.

## Delivery modes

| Mode | Outcome |
|---|---|
| Direct attestation | A verifier requests a defined assertion and receives a signed result directly from the issuer. |
| Wallet-mediated credential | The issuer delivers a credential to a holder-controlled wallet for later presentation to a verifier. |
| Status and trust metadata | A verifier obtains the information needed to evaluate issuer trust, proof validity, schema, and current Evidence status. |

Evidence can express a narrowly scoped fact, including a yes-or-no assertion, or a defined set of claims. An adopting authority that includes Evidence in its deployment needs to define claim minimisation, subject binding, validity, status, revocation or supersession, and verifier trust discovery.

## Capability boundary

[Consultation](consultation.md) returns current Registry information. Evidence produces a signed assertion whose validity and status are interpreted under an Evidence profile. A Wallet can hold and present a credential but is not the authoritative source. An E-Signature service can perform cryptographic operations, while the Registry Authority remains responsible for the meaning of the assertion.

## Binding status

This release does not specify an Evidence binding, credential format, or status mechanism. An adopter evaluating wallet-mediated Evidence can consider OpenID for Verifiable Credential Issuance and Presentation with the W3C Verifiable Credentials model. Direct delivery can be described through an OpenAPI operation returning a signed attestation. These choices do not create a GovStack capability claim.

## Example

A professional Registry issues proof that a licence is currently valid without disclosing the practitioner's address or the complete licence Record.
