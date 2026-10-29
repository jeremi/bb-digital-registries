---
title: Configure API Services
description: |
  Authorised users and API clients configure and discover the services exposed for each registry database.
realises: [registry-administration, governed-access]
conformance: CORE
requirements:
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to configure API services for each registry database through the web user interface.
    documentation: |
      Channel: section 6.1 (Administrative/Analyst Functions) groups these as Analyst functions, DRS-28 to DRS-32 give the API counterparts, and resources/decision-log.md records that a user interface is needed for analysts.
      Source: DRS-5.
    test: resources/testing.md#drs-5
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry automatically creates the required API services for a registry database.
    documentation: |
      Constraint: the generated services cover create, read, update, delete, an exists service that checks whether matching data exists, and update or create.
      Constraint: DRS-5 additionally requires batch create, batch update, batch delete, archive, and machine-readable schema introspection of tables, fields, types, and relationships.
      Binding: the template operations create, read, update, delete, exists, update-or-create and updateEntries correspond to create, read, update, delete, exists, update-or-create and batch update; getDatabase returns the database schema.
      Binding gap: the source templates define no generic operation for batch create, batch delete or archive; the only batch-create operation, GDB-MCTS-create-entries, is fixed to the example registry path /data/mcts/createEntries.
      Source: DRS-5 and DRS-31. Section 4.1 additionally describes auto-generated REST, GraphQL, and OpenAPI services, but the source OpenAPI contracts define REST operations only.
    test: resources/testing.md#drs-5
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to hide or disable an API service.
    documentation: |
      Source: DRS-5.
    test: resources/testing.md#drs-5
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to delete an API service.
    documentation: |
      Source: DRS-5.
    test: resources/testing.md#drs-5
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to copy an API service.
    documentation: |
      Source: DRS-5.
    test: resources/testing.md#drs-5
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry enables an authorised user to create a custom read API service from a registry database view.
    documentation: |
      Source conflict: DRS-5 (REQUIRED) requires view-based custom read API services, while DRS-9 marks database views OPTIONAL and describes a view as the base for a custom API (spec/6-functional-requirements.md:155-159). This core requirement therefore depends on a capability the source makes optional; the migration keeps both clauses.
      Source: DRS-5.
    test: resources/testing.md#drs-5
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: null
    statement: The Digital Registry exposes an event-based subscription API for registry data.
    documentation: |
      Constraint: event publication itself is retained in requirements/operate-registry-services.md (publish/subscribe domain events).
      Source: DRS-5. Section 4.1 describes domain events for create, update, and delete operations and mediated subscription for consumers outside the trust boundary.
      Binding gap: neither source OpenAPI document defines a subscription operation.
    test: resources/testing.md#drs-5
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry regenerates the API data structure from the current dynamic database structure whenever the database is published.
    documentation: |
      Source: DRS-5 and DRS-31.
    test: resources/testing.md#drs-5
  - id: null
    status: DRAFT
    level: RECOMMENDED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: null
    statement: The Digital Registry applies field-level masking dynamically when returning registry data through an API service.
    documentation: |
      Source: DRS-5 explicitly marks dynamic field-level masking optional and cross-references DRS-9. Section 4.1 also names policy-based masking and redaction for sensitive attributes. The format represents this source OPTIONAL feature as RECOMMENDED in the core functionality.
      Binding gap: the behaviour applies across data-returning operations, while the format permits exactly one api_operation_id and the source does not identify one operation as the complete contract.
    test: resources/testing.md#drs-5
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: null
    statement: The Digital Registry enables an authorised API client to modify the API services of a registry database.
    documentation: |
      Source: DRS-31.
      Binding gap: neither source OpenAPI document defines an operation for API-service configuration.
    test: resources/testing.md#drs-31
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: null
    statement: The Digital Registry enables an authorised API client to hide an API service.
    documentation: |
      Source: DRS-31.
      Binding gap: neither source OpenAPI document defines an operation for API-service configuration.
    test: resources/testing.md#drs-31
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: null
    statement: The Digital Registry enables an authorised API client to delete an API service.
    documentation: |
      Source: DRS-31.
      Binding gap: neither source OpenAPI document defines an operation for API-service configuration.
    test: resources/testing.md#drs-31
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: null
    statement: The Digital Registry enables an authorised API client to copy an API service.
    documentation: |
      Source: DRS-31.
      Binding gap: neither source OpenAPI document defines an operation for API-service configuration.
    test: resources/testing.md#drs-31
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: null
    statement: The Digital Registry enables an authorised API client to create a custom API service.
    documentation: |
      Source: DRS-31.
      Binding gap: neither source OpenAPI document defines an operation for API-service configuration.
    test: resources/testing.md#drs-31
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: getDatabase
    statement: The Digital Registry returns a registry database schema to an authorised API client.
    documentation: |
      Source: DRS-32.
    test: resources/testing.md#drs-32
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: getDatabase
    statement: The Digital Registry returns the list of API services available for a registry database to an authorised API client.
    documentation: |
      Constraint: the service list is the genericServices field of the response; the source calls these possible services and marks visibility with isVisible.
      Source: DRS-32.
    test: resources/testing.md#drs-32
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: FILE
    contract: resources/api.yml
    statement: The Digital Registry provides an OpenAPI service description for every API service and API-service version.
    documentation: |
      Constraint: the service description includes every field description and example value.
      Source: DRS-34 calls this a Swagger service list. It says example values should be real "if possible", without defining a verifiable condition, so that phrase is preserved here as source guidance rather than a conformance constraint.
    test: resources/testing.md#drs-34
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: null
    statement: The Digital Registry makes the OpenAPI service description of every API service and API-service version available to client systems.
    documentation: |
      Source: DRS-34, spec/6-functional-requirements.md:386 'Client systems must be able to see all API service descriptions'.
      Binding gap: neither source OpenAPI document defines an operation or endpoint that publishes service descriptions.
    test: resources/testing.md#drs-34
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry visualises every API service and API-service version described by its OpenAPI service description.
    documentation: |
      Source: DRS-34 calls the visualisation Swagger.
    test: resources/testing.md#drs-34
---

The source refers to marking fields as secret (DRS-15) and as PersonalDataID (DRS-14) from DRS-5. Those field classifications remain governed by their own legacy requirements. In particular, this migration does not use the DRS-5 cross-reference to turn the explicitly optional DRS-14 feature into a core requirement.
