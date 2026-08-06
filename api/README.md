# API artifacts

The JSON and YAML files under `legacy/generated-crud/` describe the generated CRUD interface from earlier Digital Registries releases. They are retained for migration analysis and are not service contracts for the 3.0.0-alpha.2 specification.

The `gitbook-copies/` subdirectory contains additional copies previously embedded as publication assets. They remain separated from current API artifacts because their content is not identical in every case.

In particular, the legacy interface does not provide the `consultation.retrieve` operation, which retrieves a Record directly by its stable Record Identifier. Its `POST /read` operation performs search-by-example instead.

No canonical OpenAPI contract for the 3.0.0-alpha.2 specification is published. An implementation therefore cannot claim API-contract conformance with this alpha.
