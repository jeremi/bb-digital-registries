---
description: Authorised creation and revision of Registry Records.
---

# Write

> **Status:** Informative and not claimable in this release. No Write requirements, transition model, contract, or tests are published.

## Purpose and applicability

Write creates a Record or accepts a new authoritative revision. It applies when the Registry exposes mutation to authorised external actors rather than receiving all changes through internal administration or offline processes.

## Capability patterns

| Pattern | Outcome |
|---|---|
| Direct write | An actor authorised for the relevant transition commits a final change without a Registry-managed approval workflow. |
| Governed write | A proposed change becomes authoritative only after the required review or approval process. |
| Correction | A subject or authorised actor requests correction through the governed path defined for that Registry. |

An adopting authority that includes Write in its deployment needs to define accepted transitions, validation, transition-specific authorisation, idempotency, concurrency, provenance, correction, retirement, and any legally defined deletion behaviour.

## Capability boundary

The Registry Authority remains responsible for accepted transitions and the resulting authoritative state. A Registration, Workflow, or sector-specific service can own intake and approval and then submit an approved result. Write does not require the Registry to implement a general workflow engine.

## Binding status

This release does not specify a Write binding or job model. An adopter evaluating implementation options can use synchronous HTTP described by OpenAPI for immediate changes and an asynchronous status pattern for governed or long-running changes, but those choices do not create a GovStack capability claim.

## Example

After completing its approval process, a land-transfer service submits the approved ownership change. The land Registry validates the transition and records a new authoritative revision.
