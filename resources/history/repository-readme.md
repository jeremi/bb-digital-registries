# GovStack Digital Registries Building Block

This repository contains the Digital Registries Building Block specification and supporting API, test, and implementation material.

## Specification status

The `3.0.0-alpha.2` specification defines a mandatory, domain-neutral Registry Core with machine-readable metadata and discovery, plus at least one declared capability. All capability families are optional.

The current draft defines six independently optional Consultation capabilities over logical Collections: Retrieve, Lookup, List, Search, Revision List, and Revision Retrieve. Operations can separately declare conditional reads, field selection, complete traversal, snapshot traversal, recorded-time, effective-time, or purpose binding; caller capability discovery is optional. A [canonical OpenAPI contract](api/openapi.yaml) describes their HTTP binding. This draft does not establish an implementation conformance claim.

The [illustrative business Registry contract](api/examples/business-registry.openapi.yaml), [business schema](api/examples/business-registry.schema.json), and [request/response fixtures](api/examples/consultation-exchanges.json) show a concrete adopter mapping.

Start with the [Digital Registries Building Block Specification](spec/README.md). See [Requirement Maturity](spec/04-conformance.md#41-requirement-maturity) for conformance status and [Coverage and Limitations](spec/12-other-resources.md#121-coverage-and-limitations) for published material and open work.

## Repository structure

| Path | Contents | Current status |
|---|---|---|
| `spec/` | Human-readable specification published through GitBook | 3.0.0-alpha.2 draft |
| `api/` | Machine-readable service contracts | DRAFT Consultation OpenAPI contract and concrete adopter example; previous generated CRUD contracts retained as legacy |
| `tools/` | Draft artifact validation | Contract and example checks; does not exercise a Registry implementation |
| `test/` | Legacy interface tests | Previous generated CRUD tests retained as legacy; draft implementation scenarios are documented in `spec/11-testing.md` |
| `examples/` | Product and integration examples | Historical examples; not evidence of 3.0.0-alpha.2 conformance |

## Publication

GitBook publishes content from the `spec/` directory according to `.gitbook.yaml`. The navigation source is [spec/SUMMARY.md](spec/SUMMARY.md).
