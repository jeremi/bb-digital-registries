---
title: Discover Registry Services
description: |
  An API consumer identifies a Registry, its responsible authority and authoritative scope, and locates the Registry services and machine-readable contracts available to that consumer.
realises: [registry-discovery]
conformance: CORE
requirements:
  - id:
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: FILE
    contract: resources/registry-core-model.md#registry-metadata
    statement: The Digital Registry publishes a machine-readable Registry metadata document that contains a globally unique and stable Registry Identifier, a human-readable Registry name, the identity of the Registry Authority, a description of its authoritative scope, and a reference to the Digital Registries specification version, and makes the publication URI and access conditions available to intended API consumers.
    documentation: |
      Purpose: An adopter can determine which Registry and authority stand behind a service, what information that authority accepts responsibility for, and which specification version the description references.
      Prerequisite: The Registry Authority and authoritative scope have been established by the adopting organisation.
      Evidence: The published metadata document, its publication URI and access conditions, and evidence that the Registry Identifier is not shared with another Registry or changed between service revisions.
      Verification: Access the metadata as an intended consumer, validate that all required values are present, check that the description states the authoritative scope, and review the Registry Identifier evidence.
    test: resources/testing.md#core-1
  - id:
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: FILE
    contract: resources/registry-core-model.md#service-declarations
    statement: For every Digital Registries service exposed to an intended metadata audience, the Digital Registry publishes a current machine-readable service description associated with the Registry that identifies the service, its supported API families from the Digital Registries API Families concept scheme, its endpoint, and a link to a machine-readable operational contract in the format defined by the applicable binding.
    documentation: |
      Purpose: An API consumer can discover relevant Registry services and follow their contracts to determine the supported operations and invocation details.
      Prerequisite: The Registry publishes at least one service under the capability model and makes the metadata and contract access conditions available to intended consumers.
      Constraint: The description is part of the Registry metadata document. HTTP operations use OpenAPI; another protocol uses a protocol-native machine-readable description where its binding defines one. Its declarations reflect the families and endpoints available for that Registry to the metadata's intended audience and stay current when those services change. Each linked contract describes the advertised endpoint and contains operations belonging to every declared family. Unrelated internal services are outside this requirement's scope.
      Verification: For every service exposed to an intended audience, verify its Registry association, service identifier, valid family classifications, endpoint, resolvable machine-readable contract, and consistency with the published service inventory, including different Registry contexts when an endpoint is shared.
    test: resources/testing.md#core-7
  - id:
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: getApiCatalog
    statement: At each HTTP service origin, the Digital Registry offers the API catalog operation to locate the Registry metadata document and every exposed service contract through service-meta and service-desc links.
    documentation: |
      Purpose: An API consumer can locate the Registry metadata and operational contracts from the origin through which it accesses a Registry service.
      Prerequisite: The Registry publishes at least one HTTP service and its metadata and contract access conditions are available to the intended consumer.
      Constraint: The operation is served over HTTPS at `/.well-known/api-catalog` at the origin root, outside any deployment routing prefix, as RFC 9727 requires, returns an `application/linkset+json` representation defined by the binding, and locates the metadata document and each exposed service contract. A missing required service description or contract fails verification.
      Verification: Request the API catalog at every HTTP service origin, check its response media type, follow the service-meta link to the metadata document, check that every exposed contract has a service-desc link, and compare the result with the published service inventory.
    test: resources/testing.md#core-7
  - id:
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: headApiCatalog
    statement: At each HTTP service origin, the Digital Registry offers the API catalog HEAD operation to return the catalog response headers without a body, including the Link header with the api-catalog relation required for HEAD requests.
    documentation: |
      Purpose: An API consumer checks discovery availability and locates the API catalog without transferring the catalog representation.
      Prerequisite: The Registry publishes at least one HTTP service and its metadata and contract access conditions are available to the intended consumer.
      Constraint: The operation is served over HTTPS at `/.well-known/api-catalog` at the origin root, outside any deployment routing prefix, as RFC 9727 requires, and exposes the headers defined by the API catalog binding without a response body.
      Verification: Send HEAD to the API catalog at every HTTP service origin and check the response status, absence of a body, and Link header with the api-catalog relation required by the binding.
    test: resources/testing.md#core-7-head
---

# Discovery workflow (informative)

The requirement front matter defines conformance. In the typical discovery workflow, an intended API consumer starts at an HTTP service origin, follows the API catalog to the Registry metadata document, and uses the service descriptions and linked operational contracts to understand the services available to that audience. The [Registry metadata model](../resources/registry-core-model.md#registry-metadata) describes the documents and their association with a Registry.
