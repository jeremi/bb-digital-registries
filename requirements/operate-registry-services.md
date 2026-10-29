---
title: Operate Registry Services
description: Operators and clients use the additional platform, API and workflow behaviours explicitly described outside the DRS list.
realises:
- registry-administration
- record-management
- governed-access
- accountability
- data-exchange
- analytics
conformance: CORE
requirements:
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: USER_INTERFACE
  statement: The Digital Registry enables an analyst to deprecate and archive registry versions.
  documentation: 'Constraint: Upstream section 4.1 lists publishing, deprecating and archiving registry versions as core analyst functions.

    Source: KF-LIFECYCLE-2.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: USER_INTERFACE
  statement: The Digital Registry enables an analyst to configure deduplication and data-quality controls.
  documentation: 'Constraint: Preserve the broader controls named in upstream section 4.1, in addition to the field validation rules in DRS-3 and DRS-17.

    Source: KF-LIFECYCLE-5.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: AUDITABLE
  mutability: EXTENSIBLE
  interaction: INTERNAL
  statement: The Digital Registry supports logical deletion and archival of registry records.
  documentation: 'Constraint: Upstream section 4.1 requires soft deletion and archival; the elevated source CFR still permits hard deletion when mandated by law.

    Evidence: storage state and audit records for a logically deleted record and an archived record.

    Source: KF-DATA-9.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: USER_INTERFACE
  statement: The Digital Registry enables an analyst to apply policy-based masking and redaction to sensitive record attributes.
  documentation: 'Constraint: This retains the core analyst data-management function from chapter 4. The separately optional dynamic API field masking in DRS-5 is retained without resolving the source overlap.

    Source: KF-DATA-11.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry exposes generated GraphQL services for its registries.
  documentation: 'Constraint: The source lists REST, GraphQL and OpenAPI service generation but supplies no GraphQL endpoint or machine-readable GraphQL contract. No endpoint is invented by this migration. The source writes `REST/GraphQL/OpenAPI` (spec/4-key-digital-functionalities.md:40); the slashes do not say whether GraphQL is required alongside REST, and this statement reads the item as requiring generated GraphQL services.

    Source: KF-INTEROP-12.'
  test: resources/testing.md#supplementary
  api_operation_id: null
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: EVENT
  statement: The Digital Registry publishes create, update and delete domain events through publish/subscribe messaging.
  documentation: 'Constraint: The source identifies these three event types for downstream consumers but does not define channel names or event payload schemas.

    Source: KF-INTEROP-14.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: EVENT
  statement: The Digital Registry accepts external and cross-domain event subscriptions only through mediated services exposed by the Information Mediator or an Information Mediator-managed Event Gateway.
  documentation: 'Constraint: This preserves the external-consumer boundary in source chapter 4, where external or cross-domain consumers must subscribe via mediated services (spec/4-key-digital-functionalities.md:66). The mediation component remains outside the Registry system under test.

    Source: KF-APPLICANT-6-EXTERNAL.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: EVENT
  statement: The Digital Registry applies RBAC or ABAC policy, tenant isolation and audit controls to direct internal event-bus subscriptions.
  documentation: 'Condition: consumers are inside the same trust boundary and direct internal subscriptions are offered.

    Constraint: the source permits this direct route; the migration does not make offering it mandatory.

    Source: KF-APPLICANT-6-INTERNAL.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: USER_INTERFACE
  statement: The Digital Registry shows registry usage, performance and data-quality statistics to an analyst.
  documentation: 'Constraint: The required monitoring outcome is retained alongside DRS-12 optional detailed service-usage recording; the source distinction is not silently redefined.

    Source conflict: chapter 4 item 15 (spec/4-key-digital-functionalities.md:46) requires viewing statistics on registry usage, while DRS-12 (spec/6-functional-requirements.md:173) makes service usage statistics optional.

    Source: KF-MONITORING-15.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: AUDITABLE
  mutability: EXTENSIBLE
  interaction: INTERNAL
  statement: The Digital Registry synchronizes published database-schema versions and their generated API service versions.
  documentation: 'Constraint: Upstream chapter 8 states that publication generates a service version and that database-schema and API versions are in sync.

    Evidence: version records showing that publishing a schema change produced the matching API service version.

    Source: API-VERSION-SYNCHRONISATION.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: FILE
  statement: The Digital Registry describes its generated API endpoints using the upstream naming convention.
  documentation: 'Constraint: The source convention is /{information type}/{registry acronym or code}/{version}/{API method as a name}. Its examples include /api/data/cr/1.0/create and /api/v1/database/modify; the embedded contracts use /data and /database prefixes. These source differences are retained, not resolved into redesigned paths.

    Source: API-ENDPOINT-CONVENTION.'
  test: resources/testing.md#supplementary
  contract: resources/service-apis.md
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: FILE
  statement: The Digital Registry provides OpenAPI 3 descriptions of its REST APIs with YAML descriptions and JSON request and response bodies.
  documentation: 'Constraint: This is the format stated by upstream chapter 8. The same chapter embeds JSON and YAML artifacts, while api/readme.txt prefers JSON definitions. All original representations remain unchanged; the authoring projection uses OpenAPI 3.0.0 and does not upgrade the wire contract.

    Source: API-DESCRIPTION-FORMAT.'
  test: resources/testing.md#supplementary
  contract: resources/service-apis.md
- id: null
  status: DRAFT
  level: REQUIRED
  observability: AUDITABLE
  mutability: EXTENSIBLE
  interaction: INTERNAL
  statement: The Digital Registry stores changes made through the analyst workflow in a Change Log database.
  documentation: 'Constraint: Preserve the dedicated Change Log database and completed-change log outcome stated by source workflow 9.1.2.

    Evidence: Change Log database entries for a change completed through the analyst workflow.

    Source: WF-9.1.2-CHANGE-LOG.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: AUDITABLE
  mutability: EXTENSIBLE
  interaction: INTERNAL
  statement: The Digital Registry records all applicant-workflow processing events in a dedicated audit registry.
  documentation: 'Constraint: This retains the dedicated audit registry named by source workflow 9.2.1, beyond the generic log obligations in DRS-7.

    Evidence: audit-registry entries for each processing event of a representative applicant workflow.

    Source: WF-9.2.1-AUDIT-REGISTRY.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry enables an authorised API client to create or modify a database schema.
  documentation: 'Constraint: The binding is the unchanged upstream Database API operation, identified only by a metadata alias. Workflow 9.1.3 assumes a connected client or script, Information Mediator participation, internet access and power. Its sandbox exception permits anonymous schema processing only where anonymous editing has explicitly been enabled for the database; other unauthorised schema processing is denied.

    Source: API-DATABASE-modifyDatabase.'
  test: resources/testing.md#supplementary
  api_operation_id: modifyDatabase
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry enables an authorised API client to read a database schema.
  documentation: 'Constraint: The binding is the unchanged upstream Database API operation, identified only by a metadata alias. Workflow 9.1.3 assumes a connected client or script, Information Mediator participation, internet access and power. Its sandbox exception permits anonymous schema processing only where anonymous editing has explicitly been enabled for the database; other unauthorised schema processing is denied.

    Source: API-DATABASE-getDatabase.'
  test: resources/testing.md#supplementary
  api_operation_id: getDatabase
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry enables an authorised API client to delete a database schema and all data in it.
  documentation: 'Constraint: The binding is the unchanged upstream Database API operation, identified only by a metadata alias. Workflow 9.1.3 assumes a connected client or script, Information Mediator participation, internet access and power. Its sandbox exception permits anonymous schema processing only where anonymous editing has explicitly been enabled for the database; other unauthorised schema processing is denied. The source API does not explain how deleting all schema data is implemented.

    Source: API-DATABASE-deleteDatabase.'
  test: resources/testing.md#supplementary
  api_operation_id: deleteDatabase
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry enables an authorised API client to list the registry databases and their information.
  documentation: 'Constraint: The binding is the unchanged upstream Database API operation, identified only by a metadata alias. Workflow 9.1.3 assumes a connected client or script, Information Mediator participation, internet access and power. Its sandbox exception permits anonymous schema processing only where anonymous editing has explicitly been enabled for the database; other unauthorised schema processing is denied.

    Source: API-DATABASE-listDatabases.'
  test: resources/testing.md#supplementary
  api_operation_id: listDatabases
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry applies the applicant workflow access outcomes to its create operation.
  documentation: 'Constraint: Workflow 9.2.1 assumes an authenticated applicant and an authorised client and applicant with network access and power. It permits processing when authorised, permits anonymous processing only for databases explicitly allowing that anonymous use, and denies processing without authorisation. The source also states that all authenticated users can read data; its precedence relative to the authorisation restriction is not defined. Both source statements are retained for later substantive review, not converted into an additional access grant.

    Source: WF-9.2.1-create.'
  test: resources/testing.md#supplementary
  api_operation_id: create
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry applies the applicant workflow access outcomes to its read operation.
  documentation: 'Constraint: Workflow 9.2.1 assumes an authenticated applicant and an authorised client and applicant with network access and power. It permits processing when authorised, permits anonymous processing only for databases explicitly allowing that anonymous use, and denies processing without authorisation. The source also states that all authenticated users can read data; its precedence relative to the authorisation restriction is not defined. Both source statements are retained for later substantive review, not converted into an additional access grant.

    Source: WF-9.2.1-read.'
  test: resources/testing.md#supplementary
  api_operation_id: read
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry applies the applicant workflow access outcomes to its update operation.
  documentation: 'Constraint: Workflow 9.2.1 assumes an authenticated applicant and an authorised client and applicant with network access and power. It permits processing when authorised, permits anonymous processing only for databases explicitly allowing that anonymous use, and denies processing without authorisation. The source also states that all authenticated users can read data; its precedence relative to the authorisation restriction is not defined. Both source statements are retained for later substantive review, not converted into an additional access grant.

    Source: WF-9.2.1-update.'
  test: resources/testing.md#supplementary
  api_operation_id: update
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry applies the applicant workflow access outcomes to its delete operation.
  documentation: 'Constraint: Workflow 9.2.1 assumes an authenticated applicant and an authorised client and applicant with network access and power. It permits processing when authorised, permits anonymous processing only for databases explicitly allowing that anonymous use, and denies processing without authorisation. The source also states that all authenticated users can read data; its precedence relative to the authorisation restriction is not defined. Both source statements are retained for later substantive review, not converted into an additional access grant.

    Source: WF-9.2.1-delete.'
  test: resources/testing.md#supplementary
  api_operation_id: delete
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry applies the applicant workflow access outcomes to its update-or-create operation.
  documentation: 'Constraint: Workflow 9.2.1 assumes an authenticated applicant and an authorised client and applicant with network access and power. It permits processing when authorised, permits anonymous processing only for databases explicitly allowing that anonymous use, and denies processing without authorisation. The source also states that all authenticated users can read data; its precedence relative to the authorisation restriction is not defined. Both source statements are retained for later substantive review, not converted into an additional access grant.

    Source: WF-9.2.1-update-or-create.'
  test: resources/testing.md#supplementary
  api_operation_id: update-or-create
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry applies the applicant workflow access outcomes to its exists operation.
  documentation: 'Constraint: Workflow 9.2.1 assumes an authenticated applicant and an authorised client and applicant with network access and power. It permits processing when authorised, permits anonymous processing only for databases explicitly allowing that anonymous use, and denies processing without authorisation. The source also states that all authenticated users can read data; its precedence relative to the authorisation restriction is not defined. Both source statements are retained for later substantive review, not converted into an additional access grant.

    Source: WF-9.2.1-exists.'
  test: resources/testing.md#supplementary
  api_operation_id: exists
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry provides the upstream reference operation list.
  documentation: 'Constraint: The preserved template binds this operation to GET /data/{registryName}/{versionNumber}. Chapter 8 describes generated per-registry APIs and a postpartum-care example dataset. Preserve its reference-binding applicability; the example registry name is not an invented requirement for every deployment. The operation inputs, results, schemas and access declarations remain those of the selected original contract.

    Source: API-TEMPLATE-list.'
  test: resources/testing.md#supplementary
  api_operation_id: list
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry provides the upstream reference operation create.
  documentation: 'Constraint: The preserved template binds this operation to POST /data/{registryName}/{versionNumber}/create. Chapter 8 describes generated per-registry APIs and a postpartum-care example dataset. Preserve its reference-binding applicability; the example registry name is not an invented requirement for every deployment. The operation inputs, results, schemas and access declarations remain those of the selected original contract.

    Source: API-TEMPLATE-create.'
  test: resources/testing.md#supplementary
  api_operation_id: create
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry provides a batch-create operation for entries of a registry database.
  documentation: 'Contract gap: the only batch-create operation in the source, GDB-MCTS-create-entries, is fixed to the example registry path /data/mcts/createEntries, so it is not a generic operation and is not bound here. The source defines no operation that batch-creates entries for an arbitrary registry database.

    Source: API-TEMPLATE-GDB-MCTS-create-entries; spec/8-service-apis.md.'
  test: resources/testing.md#supplementary
  api_operation_id: null
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry provides the upstream reference operation exists.
  documentation: 'Constraint: The preserved template binds this operation to POST /data/{registryName}/{versionNumber}/exists. Chapter 8 describes generated per-registry APIs and a postpartum-care example dataset. Preserve its reference-binding applicability; the example registry name is not an invented requirement for every deployment. The operation inputs, results, schemas and access declarations remain those of the selected original contract.

    Source: API-TEMPLATE-exists.'
  test: resources/testing.md#supplementary
  api_operation_id: exists
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry provides the upstream reference operation read.
  documentation: 'Constraint: The preserved template binds this operation to POST /data/{registryName}/{versionNumber}/read. Chapter 8 describes generated per-registry APIs and a postpartum-care example dataset. Preserve its reference-binding applicability; the example registry name is not an invented requirement for every deployment. The operation inputs, results, schemas and access declarations remain those of the selected original contract.

    Source: API-TEMPLATE-read.'
  test: resources/testing.md#supplementary
  api_operation_id: read
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry provides the upstream reference operation update.
  documentation: 'Constraint: The preserved template binds this operation to PUT /data/{registryName}/{versionNumber}/update. Chapter 8 describes generated per-registry APIs and a postpartum-care example dataset. Preserve its reference-binding applicability; the example registry name is not an invented requirement for every deployment. The operation inputs, results, schemas and access declarations remain those of the selected original contract.

    Source: API-TEMPLATE-update.'
  test: resources/testing.md#supplementary
  api_operation_id: update
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry provides the upstream reference operation updateEntries.
  documentation: 'Constraint: The preserved template binds this operation to PUT /data/{registryName}/{versionNumber}/updateEntries. Chapter 8 describes generated per-registry APIs and a postpartum-care example dataset. Preserve its reference-binding applicability; the example registry name is not an invented requirement for every deployment. The operation inputs, results, schemas and access declarations remain those of the selected original contract.

    Source: API-TEMPLATE-updateEntries.'
  test: resources/testing.md#supplementary
  api_operation_id: updateEntries
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry provides the upstream reference operation update-or-create.
  documentation: 'Constraint: The preserved template binds this operation to POST /data/{registryName}/{versionNumber}/updateOrCreate. Chapter 8 describes generated per-registry APIs and a postpartum-care example dataset. Preserve its reference-binding applicability; the example registry name is not an invented requirement for every deployment. The operation inputs, results, schemas and access declarations remain those of the selected original contract.

    Source: API-TEMPLATE-update-or-create.'
  test: resources/testing.md#supplementary
  api_operation_id: update-or-create
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry provides the upstream reference operation delete.
  documentation: 'Constraint: The preserved template binds this operation to DELETE /data/{registryName}/{versionNumber}/{id}/delete. Chapter 8 describes generated per-registry APIs and a postpartum-care example dataset. Preserve its reference-binding applicability; the example registry name is not an invented requirement for every deployment. The operation inputs, results, schemas and access declarations remain those of the selected original contract.

    Source: API-TEMPLATE-delete.'
  test: resources/testing.md#supplementary
  api_operation_id: delete
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry provides the upstream reference operation readValue.
  documentation: 'Constraint: The preserved template binds this operation to GET /data/{registryName}/{versionNumber}/{uuid}/readValue/{field}.{ext}. Chapter 8 describes generated per-registry APIs and a postpartum-care example dataset. Preserve its reference-binding applicability; the example registry name is not an invented requirement for every deployment. The operation inputs, results, schemas and access declarations remain those of the selected original contract.

    Source: API-TEMPLATE-readValue.'
  test: resources/testing.md#supplementary
  api_operation_id: readValue
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry provides the upstream reference operation DPU.
  documentation: 'Constraint: The preserved template binds this operation to GET /data/mypersonalDataUsage. Chapter 8 describes generated per-registry APIs and a postpartum-care example dataset. Preserve its reference-binding applicability; the example registry name is not an invented requirement for every deployment. The operation inputs, results, schemas and access declarations remain those of the selected original contract.

    Source: API-TEMPLATE-DPU.'
  test: resources/testing.md#supplementary
  api_operation_id: DPU
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry provides the upstream reference operation getDatabase.
  documentation: 'Constraint: The preserved template binds this operation to GET /database/{id}. Chapter 8 describes generated per-registry APIs and a postpartum-care example dataset. Preserve its reference-binding applicability; the example registry name is not an invented requirement for every deployment. The operation inputs, results, schemas and access declarations remain those of the selected original contract.

    Source: API-TEMPLATE-getDatabase.'
  test: resources/testing.md#supplementary
  api_operation_id: getDatabase
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry provides the upstream reference operation deleteDatabase.
  documentation: 'Constraint: The preserved template binds this operation to DELETE /database/{id}. Chapter 8 describes generated per-registry APIs and a postpartum-care example dataset. Preserve its reference-binding applicability; the example registry name is not an invented requirement for every deployment. The operation inputs, results, schemas and access declarations remain those of the selected original contract.

    Source: API-TEMPLATE-deleteDatabase.'
  test: resources/testing.md#supplementary
  api_operation_id: deleteDatabase
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry provides the upstream reference operation modifyDatabase.
  documentation: 'Constraint: The preserved template binds this operation to POST /database/modify. Chapter 8 describes generated per-registry APIs and a postpartum-care example dataset. Preserve its reference-binding applicability; the example registry name is not an invented requirement for every deployment. The operation inputs, results, schemas and access declarations remain those of the selected original contract.

    Source: API-TEMPLATE-modifyDatabase.'
  test: resources/testing.md#supplementary
  api_operation_id: modifyDatabase
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: SERVICE_API
  statement: The Digital Registry provides the upstream reference operation listDatabases.
  documentation: 'Constraint: The preserved template binds this operation to GET /databases. Chapter 8 describes generated per-registry APIs and a postpartum-care example dataset. Preserve its reference-binding applicability; the example registry name is not an invented requirement for every deployment. The operation inputs, results, schemas and access declarations remain those of the selected original contract.

    Source: API-TEMPLATE-listDatabases.'
  test: resources/testing.md#supplementary
  api_operation_id: listDatabases
  contract: resources/api.yml
- id: null
  status: DRAFT
  level: REQUIRED
  observability: AUDITABLE
  mutability: EXTENSIBLE
  interaction: INTERNAL
  statement: The Digital Registry supports multiple tenants that create and manage registry databases.
  documentation: 'Constraint: Chapter 4 describes a multi-tenant platform. This statement retains that property without inventing a tenant-identifier format or additional isolation rules; the source explicitly conditions direct event subscriptions on tenant isolation elsewhere.

    Evidence: configuration and audit records showing registry databases created and managed by two different tenants.

    Source: KF-PLATFORM.'
  test: resources/testing.md#supplementary
- id: null
  status: DRAFT
  level: REQUIRED
  observability: OBSERVABLE
  mutability: EXTENSIBLE
  interaction: USER_INTERFACE
  statement: The Digital Registry provides backward-compatibility guidance when an analyst publishes a changed registry schema and API version.
  documentation: 'Constraint: Source chapter 4 requires compatibility guidance, in addition to DRS-4 breaking-change detection and warnings.

    Source: KF-LIFECYCLE-4.'
  test: resources/testing.md#supplementary
---

The YAML requirements retain the source obligations identified in the migration ledger. The supporting descriptions and contracts remain under `resources/`.
