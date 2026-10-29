---
title: Preserved Upstream Findings
---

# Preserved Upstream Findings

These are inherited ambiguities and missing contracts, not redesign decisions. The migration preserves the stated behaviour and records uncertainty rather than inventing a resolution. Original source bytes remain available for review.

## Missing or incomplete bindings

The ledger records 32 missing or incomplete upstream bindings or format contracts. Some concern API operations; others concern consumed interfaces or file formats. Empty API IDs remain explicit draft gaps, not valid named bindings.

### 1. DRS-30

The Digital Registry enables an authorised API client to publish a registry database.

**Gap:** Neither source OpenAPI document defines an operation that publishes a registry database.

**Requirement file:** `requirements/manage-registries.md`.

### 2. DRS-5

The Digital Registry exposes an event-based subscription API for registry data.

**Gap:** Neither source OpenAPI document defines a subscription operation.

**Requirement file:** `requirements/configure-api-services.md`.

### 3. DRS-5

The Digital Registry applies field-level masking dynamically when returning registry data through an API service.

**Gap:** The behaviour applies across data-returning operations, while the format permits exactly one api_operation_id and the source does not identify one operation as the complete contract.

**Requirement file:** `requirements/configure-api-services.md`.

### 4. DRS-5

The Digital Registry automatically creates the required API services for a registry database.

**Gap:** The source templates define no generic operation for batch create, batch delete or archive; the only batch-create operation, GDB-MCTS-create-entries, is fixed to the example registry path /data/mcts/createEntries.

**Requirement file:** `requirements/configure-api-services.md`.

### 5. DRS-31

The Digital Registry enables an authorised API client to modify the API services of a registry database.

**Gap:** Neither source OpenAPI document defines an operation for API-service configuration.

**Requirement file:** `requirements/configure-api-services.md`.

### 6. DRS-31

The Digital Registry enables an authorised API client to hide an API service.

**Gap:** Neither source OpenAPI document defines an operation for API-service configuration.

**Requirement file:** `requirements/configure-api-services.md`.

### 7. DRS-31

The Digital Registry enables an authorised API client to delete an API service.

**Gap:** Neither source OpenAPI document defines an operation for API-service configuration.

**Requirement file:** `requirements/configure-api-services.md`.

### 8. DRS-31

The Digital Registry enables an authorised API client to copy an API service.

**Gap:** Neither source OpenAPI document defines an operation for API-service configuration.

**Requirement file:** `requirements/configure-api-services.md`.

### 9. DRS-31

The Digital Registry enables an authorised API client to create a custom API service.

**Gap:** Neither source OpenAPI document defines an operation for API-service configuration.

**Requirement file:** `requirements/configure-api-services.md`.

### 10. DRS-34

The Digital Registry makes the OpenAPI service description of every API service and API-service version available to client systems.

**Gap:** Neither source OpenAPI document defines an operation or endpoint that publishes service descriptions.

**Requirement file:** `requirements/configure-api-services.md`.

### 11. DRS-6

The Digital Registry provides an API through which an authorised operator manages user rights for a registry database and its data.

**Gap:** Neither source OpenAPI document defines an operation for managing user rights.

**Requirement file:** `requirements/access-control.md`.

### 12. DRS-9

The Digital Registry exposes a configured database view through a custom read API operation.

**Gap:** Neither source OpenAPI document defines an operation for a custom database view.

**Requirement file:** `requirements/records-optional-database-views.md`.

### 13. DRS-7

The Digital Registry writes database log evidence to an external blockchain for additional integrity protection.

**Gap:** The source identifies no blockchain protocol, network or operation to which this consumed interaction can bind.

**Requirement file:** `requirements/audit-and-personal-data.md`.

### 14. DRS-15

The Digital Registry encrypts information in transit between Building Blocks under the rules of the Information Mediator Building Block.

**Gap:** The source cites the Information Mediator Building Block without a versioned publication identifier or section.

**Requirement file:** `requirements/audit-and-personal-data.md`.

### 15. DRS-18

The Digital Registry requires an application to know the database encryption key before the application reads encrypted data through the API.

**Gap:** The `read` operation is the matching data-read operation, but its source request contract defines no encryption-key parameter or other proof-of-knowledge field.

**Requirement file:** `requirements/audit-and-personal-data.md`.

### 16. DRS-19

The Digital Registry sends mapped data to an API of an external registry database.

**Gap:** The source identifies no external registry API contract or operation for the consumed interaction.

**Requirement file:** `requirements/data-exchange.md`.

### 17. DRS-19

The Digital Registry supports webhook triggers for multi-registry orchestration of automated exchanges.

**Gap:** The source does not say whether webhook triggers are received, published, or observed through another component.

**Requirement file:** `requirements/data-exchange.md`.

### 18. DRS-14

The Digital Registry links an owner identifier to an external registry.

**Gap:** The source identifies no external registry API contract or linking operation.

**Requirement file:** `requirements/owner-identifiers.md`.

### 19. DRS-24

The Digital Registry imports registry data from JSON, CSV and XLS files.

**Gap:** The source names file types but defines no schema, profile or validation contract for imported data files.

**Requirement file:** `requirements/record-views.md`.

### 20. DRS-25

The Digital Registry exports selected or filtered registry data to CSV, XLS and JSON files.

**Gap:** The source names file types but defines no schema, profile or validation contract for exported data files.

**Requirement file:** `requirements/record-views.md`.

### 21. DRS-10

The Digital Registry exports a registry database schema as a JSON or YAML file.

**Gap:** The source defines no schema export or import file format.

**Requirement file:** `requirements/transfer-schemas.md`.

### 22. DRS-10

The Digital Registry exports a registry database schema as an XLS file.

**Gap:** The source defines no schema export or import file format.

**Requirement file:** `requirements/transfer-schemas.md`.

### 23. DRS-11

The Digital Registry imports a registry database schema from a JSON or YAML file.

**Gap:** The source defines no schema export or import file format.

**Requirement file:** `requirements/transfer-schemas.md`.

### 24. DRS-11

The Digital Registry imports a registry database schema from an XLS file.

**Gap:** The source defines no schema export or import file format.

**Requirement file:** `requirements/transfer-schemas.md`.

### 25. DRS-20

The Digital Registry exports a registry schema template.

**Gap:** The source defines no registry-template package format.

**Requirement file:** `requirements/schema-templates.md`.

### 26. DRS-20

The Digital Registry imports a registry schema template.

**Gap:** The source defines no registry-template package format.

**Requirement file:** `requirements/schema-templates.md`.

### 27. DRS-36

The Digital Registry exposes registration data through a statistical-query API.

**Gap:** Neither source OpenAPI document identifies an operation as the statistical-query API required by DRS-36.

**Requirement file:** `requirements/statistics-api.md`.

### 28. DRS-36

The Digital Registry exposes programme data through a statistical-query API.

**Gap:** Neither source OpenAPI document identifies an operation as the statistical-query API required by DRS-36.

**Requirement file:** `requirements/statistics-api.md`.

### 29. DRS-36

The Digital Registry's statistical-query API accepts date and time ranges as query parameters.

**Gap:** Neither source OpenAPI document identifies an operation as the statistical-query API required by DRS-36.

**Requirement file:** `requirements/statistics-api.md`.

### 30. DRS-36

The Digital Registry's statistical-query API accepts a registered programme as a query parameter.

**Gap:** Neither source OpenAPI document identifies an operation as the statistical-query API required by DRS-36.

**Requirement file:** `requirements/statistics-api.md`.

### 31. Chapter 4, Interoperability item 12

The Digital Registry exposes generated GraphQL services for its registries.

**Gap:** The upstream chapter requires GraphQL services but supplies no GraphQL endpoint or operation binding.

**Requirement file:** `requirements/operate-registry-services.md`.

### 32. API-TEMPLATE-GDB-MCTS-create-entries

The Digital Registry provides a batch-create operation for entries of a registry database.

**Gap:** The only batch-create operation in the source, GDB-MCTS-create-entries, is fixed to the example registry path /data/mcts/createEntries, so it is not a generic operation and no operation is bound.

**Requirement file:** `requirements/operate-registry-services.md`.

## Cross-clause ambiguities

- **DRS-2:** The source uses database and database table interchangeably when describing relationships.
- **DRS-1:** The source lists the default indexing and storage profile as `row store / column store / document store` without saying whether all three must be offered.
- **DRS-2:** The source says links can be a foreign key, a soft link or a graph relationship, while only the foreign key is backed by `must`; the migration requires all three and the source does not say whether all are mandatory.
- **DRS-2:** The source says it `should be possible` to open another database by clicking the record ID, while the example that follows is tagged REQUIRED.
- **DRS-2:** The source lists cascade delete, restrict delete, and orphan tolerance without saying whether a relationship selects one rule or may combine them.
- **DRS-3:** UTF-8 database or cluster encoding is listed among field types even though its wording describes a storage encoding.
- **DRS-4:** The source requires old-version data to remain usable under later versions but does not define compatibility or migration rules.
- **DRS-5:** Section 4.1 names generated REST, GraphQL, and OpenAPI services, while the source API contracts define REST operations only.
- **DRS-5 and DRS-14:** DRS-5 says an analyst must be able to mark a field as PersonalDataID, while its DRS-14 cross-reference marks that feature optional.
- **DRS-10 and DRS-11:** The notation JSON/YAML does not say whether both formats are required or whether one format is sufficient. The migrated statements keep the source `JSON or YAML` wording; whether one format suffices remains open.
- **DRS-17:** The source names JavaScript field transformation without defining its execution environment or security constraints.
- **DRS-20:** The source requires marketplace sharing but does not define a registry-template package format or marketplace protocol.
- **DRS-19:** `Mapping may have a transformation option` sits in a REQUIRED block without an (Optional) tag; the migration keeps `may` as a nonblocking recommendation.
- **DRS-20 and DRS-9:** DRS-20 includes views in a full registry template, while DRS-9 makes database views OPTIONAL; the source does not say what a template contains when the Database Views extension is not claimed.
- **DRS-34:** The source asks for real examples "if possible" without a condition that makes the phrase verifiable.
- **DRS-5 and DRS-9:** DRS-5 requires an analyst to create custom read API services from views, while DRS-9 marks the whole database-view functionality optional.
- **DRS-5 and DRS-9:** DRS-5 labels dynamic field-level masking optional and cross-references DRS-9, but DRS-9 describes database views and does not define field-level masking.
- **DRS-7:** The source requires the `highest level of integrity` for change logs but defines no comparative level or measurable threshold; it names log chaining as the only concrete mechanism.
- **DRS-8, DRS-13, DRS-14, DRS-35, and DRS-37:** DRS-13 and DRS-14 make personal-data and owner-identifier field tagging optional, while DRS-8, DRS-35 and DRS-37 require logs, owner linking and owner reports that depend on those concepts.
- **DRS-8:** The conditions under which law requires a legal justification or consent applies are not defined by the source.
- **DRS-18:** The source requires applications to know a database encryption key and states that the user interface decrypts data, but does not define key transport, custody or rotation.
- **DRS-19:** `Webhook triggers` does not say whether the Digital Registry receives a webhook, publishes one, or observes it through another component.
- **DRS-26 and DRS-36:** DRS-26 requires APIs that extract data for external analytics, while DRS-36 makes a statistical-query API optional; the source does not define the boundary between those APIs.
- **DRS-27:** The source joins email delivery and a unique secure URL with `or`, so it does not require both sharing mechanisms.
- **DRS-27:** The source classifies data shared anonymously as Open Data without defining publication, licensing or withdrawal consequences.
- **DRS-7 and DRS-37:** DRS-7 item 1.4 gives a data owner the option to see who has processed the owner's data without naming a channel, while DRS-37 item 3 says the logs are visible `via API or via User Interface`; the either/or does not require both, so the migration models a variation point that needs at least one of the two options.
- **DRS-8:** The marker `(optional)` ends the final bullet `Data viewer's role, org, location, Device fingerprint (optional)` and the source does not say whether it scopes only the device fingerprint or all four items; the migration reads it as scoping the device fingerprint and keeps role, organisation and location required.
- **DRS-27:** DRS-27 items 1 to 4 (time-bound, consent-required, role-restricted and QR-code sharing) are written as link features, so they presuppose a sharing link even though the opening sentence allows email delivery alone.
- **DRS-26:** The block header reads `should have the ability to (REQUIRED)`, so the source does not settle whether `should` makes the listed abilities recommendations or requirements; the migration keeps them REQUIRED, and the analytics extraction statement stays bound to `list` as the closest operation.
- **DRS-24 and DRS-25:** DRS-25 writes `CSV/XLS, JSON`, and the slash does not say whether both CSV and XLS are required; DRS-24 lists JSON, CSV and XLS with commas. The migrated export statement keeps all three formats.
- **Chapter 4, Interoperability item 12:** spec/4-key-digital-functionalities.md:40 writes `REST/GraphQL/OpenAPI`, and the slash does not say whether GraphQL is required alongside REST.
- **Chapter 4 item 16 and DRS-26:** Chapter 4 item 16 (spec/4-key-digital-functionalities.md:47), `Generate dashboards and administrative reports`, sits under a chapter described as core required functions, while DRS-26 marks custom dashboards as an option; the migration keeps the dashboard statement RECOMMENDED.
- **Workflow 9.1.3:** spec/9-workflows.md:112-113 postconditions 2 and 3 conflict: postcondition 2, labelled a simplification for the GovStack Sandbox instance, lets a non-authorised developer process the schema of databases where anonymous editing is allowed, while postcondition 3 says a user with no authorization cannot create or change any schema.
- **Chapter 4 item 15 and DRS-12:** Chapter 4 item 15 (spec/4-key-digital-functionalities.md:46) requires viewing statistics on registry usage, performance and data quality, while DRS-12 makes service usage statistics optional; the migration keeps the monitoring statement REQUIRED and the DRS-12 recording statements optional.
- **Chapter 8:** Chapter 8 calls its listed APIs `a minimal set of functionality that should be provided by any implementation` (spec/8-service-apis.md:9) and says the Building Block `is expected to host` them (spec/8-service-apis.md:31); the migration maps them to REQUIRED, and the `should` and `expected` wording does not settle the level.
- **Chapter 4 item 13:** Item 13, `Integrate with external systems through the Information Mediator BB` (spec/4-key-digital-functionalities.md:41), does not say whether every external integration must pass through the Information Mediator; the migration does not carry it as a separate statement because mediation is outside the system under test.

Additional narrative, model and workflow issues are preserved in the [complete narrative inventory](upstream-narrative-inventory.md). The workflow statements about broad authenticated reads and anonymous sandbox processing do not supply a consistent precedence rule with the source authorization restrictions. The migration retains those source conditions and does not grant additional production access.

The two invalid alternative Database contracts remain invalid in the same way in the [paired validation report](contract-validation.json). Neither this record nor a successful migration check claims deployed conformance.
