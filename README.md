# GovStack Digital Registries Building Block

This repository contains the Digital Registries Building Block specification, interface contracts, conformance tests, and implementation examples.

## Specification status

The `3.0.0-alpha.2` specification defines a domain-neutral Registry Core with mandatory Consultation Retrieve and additional optional capability families. Its requirements are classified as DRAFT and do not establish a GovStack certification claim.

Start with the [Digital Registries Building Block Specification](spec/README.md).

### Alpha coverage

The alpha publishes the proposed scope, terminology, Base Registry Profile, DRAFT Core and Retrieve requirements, conceptual Record model, workflow, verification intent, and migration from the previous `DRS-1` through `DRS-37` requirements.

It does not publish a canonical OpenAPI contract or executable conformance suite. No implementation can claim conformance with this alpha.

## Repository structure

| Path | Contents | Current status |
|---|---|---|
| `spec/` | Human-readable specification published through GitBook | 3.0.0-alpha.2 draft |
| `api/` | Machine-readable service contracts | Previous generated CRUD contracts retained as legacy; no 3.0.0-alpha.2 contract published |
| `test/` | Conformance and contract tests | Previous generated CRUD tests retained as legacy; draft scenarios are documented in `spec/11-testing.md` |
| `examples/` | Product and integration examples | Historical examples; not evidence of 3.0.0-alpha.2 conformance |

## Publication

GitBook publishes content from the `spec/` directory according to `.gitbook.yaml`. The navigation source is [spec/SUMMARY.md](spec/SUMMARY.md).
