---
title: Service APIs
description: >-
  This section provides a reference for APIs that should be implemented by this
  Building Block.
---

# Service APIs

The APIs defined here establish a blueprint for how the Building Block will interact with other Building Blocks. Additional APIs may be implemented by the Building Block, but the listed APIs define a minimal set of functionality that should be provided by any implementation of this Building Block.

The [GovStack non-functional requirements document](https://govstack.gitbook.io/specification/v/1.0/architecture-and-nonfunctional-requirements/6-onboarding) provides additional information on how 'adaptors' may be used to translate an existing API to the patterns described here. This section also provides guidance on how candidate products are tested and how GovStack validates a product's API against the API specifications defined here.

The tests for the Digital Registries Building Block can be found in [the preserved upstream test suite](https://github.com/GovStackWorkingGroup/bb-digital-registries/tree/8588a219df9a8406e66c4392d0bef664b34e4e30/test/openAPI).

The Digital Registries Building Block may contain multiple registries/databases. The dynamic nature of the database structure requires a standard set of automatically generated APIs for all databases hosted on the platform. The system generates default API method endpoints automatically after each publication of the database schema. A new API service version is generated after each schema publish. Database schema version and API versions are in sync.

The naming convention and structure of the API endpoint are the following:

/{information type}/{registry acronym or code}/{version}/{API method as a name}.

Example 1: ​/api/data​/cr​/1.0​/create

Example 2: ​/api/v1/database/modify

Each registry contains a unique set of data and the Building Block enables an Analyst to change the data storage structure/schema on the fly. In the following example API descriptions are generated for one example dataset for the Postpartum Infant Care Program registry, where the Caretaker and infant child are registered and a registration ID is issued.

![Example registry database logical data model.](../assets/Logical%20datamodel%20MCTS%20%281%29.JPG)

![Example registry database JSON schema.](../assets/image4%20%281%29%20%281%29%20%281%29.png)

Digital Registries Building Block is expected to host the following API services for each database hosted on the platform.

The API is built using a representational state transfer ([REST](https://restfulapi.net/)) software architectural style and described in [Open API 3 standard](https://swagger.io/specification/) using [YAML](https://yaml.org/) (a human-readable data-serialization language). Request and response body is in [JSON](https://www.json.org/json-en.html) (lightweight data-interchange format).

The active authoring projection is [`api.yml`](api.yml).
It uses byte-identical copies of the chapter 8 embed contracts at [`upstream-api/data-api.json`](upstream-api/data-api.json) and [`upstream-api/database-api.yaml`](upstream-api/database-api.yaml), with metadata-only operation identifiers and reference rebasing in the projection.
The tables below preserve the methods, paths, order, duplication, and source-contract selection that the upstream chapter embedded.

## Administrative/Analyst Functions

| Method | Path | Source contract |
|---|---|---|
| `GET` | `/data/{registryName}/{versionNumber}` | [`GovStack_Digital_registries_BB_Data_API_template-1.3.0.json`](../assets/GovStack_Digital_registries_BB_Data_API_template-1.3.0.json) |
| `POST` | `/data/{registryName}/{versionNumber}/read` | [`GovStack_Digital_registries_BB_Data_API_template-1.3.0.json`](../assets/GovStack_Digital_registries_BB_Data_API_template-1.3.0.json) |
| `PUT` | `/data/{registryName}/{versionNumber}/update` | [`GovStack_Digital_registries_BB_Data_API_template-1.3.0.json`](../assets/GovStack_Digital_registries_BB_Data_API_template-1.3.0.json) |
| `PUT` | `/data/{registryName}/{versionNumber}/updateEntries` | [`GovStack_Digital_registries_BB_Data_API_template-1.3.0.json`](../assets/GovStack_Digital_registries_BB_Data_API_template-1.3.0.json) |
| `POST` | `/data/{registryName}/{versionNumber}/updateOrCreate` | [`GovStack_Digital_registries_BB_Data_API_template-1.3.0.json`](../assets/GovStack_Digital_registries_BB_Data_API_template-1.3.0.json) |

## Applicant Functions

| Method | Path | Source contract |
|---|---|---|
| `POST` | `/data/{registryName}/{versionNumber}/exists` | [`GovStack_Digital_registries_BB_Data_API_template-1.3.0.json`](../assets/GovStack_Digital_registries_BB_Data_API_template-1.3.0.json) |
| `DELETE` | `/data/{registryName}/{versionNumber}/{id}/delete` | [`GovStack_Digital_registries_BB_Data_API_template-1.3.0.json`](../assets/GovStack_Digital_registries_BB_Data_API_template-1.3.0.json) |
| `GET` | `/data/{registryName}/{versionNumber}/{uuid}/readValue/{field}.{ext}` | [`GovStack_Digital_registries_BB_Data_API_template-1.3.0.json`](../assets/GovStack_Digital_registries_BB_Data_API_template-1.3.0.json) |
| `GET` | `/data/mypersonalDataUsage` | [`GovStack_Digital_registries_BB_Data_API_template-1.3.0.json`](../assets/GovStack_Digital_registries_BB_Data_API_template-1.3.0.json) |
| `GET` | `/database/{id}` | [`GovStack_Digital_registries_BB_Database_API_template-1.3.0.yaml`](../assets/GovStack_Digital_registries_BB_Database_API_template-1.3.0.yaml) |
| `DELETE` | `/database/{id}` | [`GovStack_Digital_registries_BB_Database_API_template-1.3.0.yaml`](../assets/GovStack_Digital_registries_BB_Database_API_template-1.3.0.yaml) |
| `POST` | `/database/modify` | [`GovStack_Digital_registries_BB_Database_API_template-1.3.0.yaml`](../assets/GovStack_Digital_registries_BB_Database_API_template-1.3.0.yaml) |
| `GET` | `/databases` | [`GovStack_Digital_registries_BB_Database_API_template-1.3.0.yaml`](../assets/GovStack_Digital_registries_BB_Database_API_template-1.3.0.yaml) |
| `GET` | `/data/{registryName}/{versionNumber}` | [`GovStack_Digital_registries_BB_Data_API_template-1.3.0.json`](../assets/GovStack_Digital_registries_BB_Data_API_template-1.3.0.json) |
| `POST` | `/data/mcts/createEntries` | [`GovStack_Digital_registries_BB_Data_API_template-1.3.0.json`](../assets/GovStack_Digital_registries_BB_Data_API_template-1.3.0.json) |
| `POST` | `/data/{registryName}/{versionNumber}/read` | [`GovStack_Digital_registries_BB_Data_API_template-1.3.0.json`](../assets/GovStack_Digital_registries_BB_Data_API_template-1.3.0.json) |
