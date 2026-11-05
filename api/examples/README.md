# API example artifacts

The [API example guide](../../resources/api-examples/README.md) describes the
illustrative Consultation and Write contracts, schemas, fixtures, and discovery
documents in this directory. Domain choices in these examples add no requirements
to the shared contracts.

The Write example uses Merge Patch for its concrete Update operation. The canonical
contract also illustrates how a separately selected JSON Patch format is represented
in governed input. This does not require a deployment to support both formats.

`combined-journeys.json` supplies domain-neutral static Read and Write lifecycle
fixtures for the artifact gate. It does not represent traffic captured from a
deployed Registry.

Run the repository's [API validation commands](../README.md#validation) to check
the shipped artifacts. These checks do not execute a Registry implementation.

The [vendored schema dependencies](publicschema/README.md) retain their source
provenance, attribution, licences, and reproducible offline mirror.
