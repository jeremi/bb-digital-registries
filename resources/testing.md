---
title: Verification Procedures
---

# Verification Procedures

These are finite manual verification plans for the migrated upstream requirements. They have not been executed against a deployed implementation. Existing upstream Cucumber fixtures remain unchanged under `test/openAPI/`; preservation and authoring checks do not establish runtime conformance.

Run the repository checks with `uv run python -m unittest discover -s tools -p 'test_*.py'` and `uv run python tools/validate_migration.py`. Validate the authoring projection with `uv run openapi-spec-validator resources/api.yml`.

For missing standardized bindings, use an implementation's declared contract only to assess the upstream behaviour. That does not fill the common-contract gap or prove compatibility with an official compiler.

<a id="drs-1"></a>
## DRS-1

**Fixture**

- A fresh Digital Registry instance.
- One account authorised to create registries and one account without that permission.
- A sample schema with one text field.
- Metadata values for domain, owner department, retention policy, and each classification: Open, Restricted, and Confidential.

**Actions**

1. With the authorised account, create a registry through the web user interface with a database name, unique short code, the sample schema, all required metadata, Draft lifecycle state, and a row-store default profile.
2. Repeat with distinct short codes, the remaining classifications, and column-store and document-store default profiles.
3. Progress one registry from Draft to Published and then to Archived.
4. Attempt to create another registry using the first registry's short code.
5. Attempt the same creation and lifecycle changes with the account that lacks permission.

**Expected results**

- Each permitted creation stores and displays the submitted name, unique short code, schema, domain, owner department, retention policy, classification, lifecycle state, and default indexing and storage profile.
- Row store, column store, and document store are accepted as profile choices.
- The tested registry progresses in order from Draft to Published to Archived.
- The duplicate short code is rejected without creating another registry.
- The account without permission cannot create a registry or change its lifecycle state.

<a id="drs-2"></a>
## DRS-2

**Fixture**

- An authorised registry administrator.
- Four registries in one instance: Parent, Child, Payment, and Tag.
- Parent and Payment records with known identifiers, including one Parent with two matching Payment records.
- Separate disposable relationships configured for cascade delete, restrict delete, and orphan tolerance.

**Actions**

1. Confirm that all four registries coexist in the same instance.
2. Configure a strict foreign key between Child and Parent, selecting the linked database and fields.
3. Configure a soft UUID reference from Payment to Parent without a foreign-key constraint.
4. Configure a parent-child graph edge between Parent and Child and a many-to-many graph edge between Parent and Tag.
5. Inspect the relationship definitions and record the database identifiers and field identifiers used by each link.
6. Browse Payment data in the user interface and select the Parent identifier for the record that has two matching Payment records.
7. Exercise cascade delete, restrict delete, and orphan tolerance on their disposable relationships.

**Expected results**

- The system retains all registries in one instance and exposes all three relationship kinds.
- Each relationship records the selected databases and fields, with identifiers at database and field levels.
- Selecting the linked identifier opens the corresponding Parent record and exposes all corresponding linked Payment records.
- Cascade delete removes the configured dependent record, restrict delete blocks deletion while a restricted reference exists, and orphan tolerance permits the configured orphan outcome.
- The procedure does not decide whether a single relationship may combine integrity rules, because DRS-2 does not define that point.

<a id="drs-3"></a>
## DRS-3

**Fixture**

- An authorised registry administrator and a draft registry schema.
- Representative values for Text, Number, Boolean, Date/time, Date, Time, File, List or Array or Edit grid, and List of Values or Catalog.
- A file-type allow-list containing PDF and DOC.
- If the solution declares a RECOMMENDED DRS-3 feature met, representative JSON object grouping, multilingual UTF-8 text, latitude and longitude, and polygon or boundary values for that feature.

**Actions**

1. Add a named field of every required core type through the user interface.
2. Configure the File field to accept PDF and DOC, then attempt an allowed file and a file type outside the allow-list.
3. Store multiple values in the List, Array, or Edit-grid field.
4. Configure and store key-value choices in the List of Values or Catalog field.
5. For each RECOMMENDED feature declared met, configure and exercise its JSON object or block-container grouping, UTF-8 multilingual content, GeoPoint, or GeoShape behaviour.
6. For UTF-8, inspect the documented database or cluster encoding in addition to storing and retrieving multilingual text.

**Expected results**

- Every core field retains its name, type, and representative value.
- The File field accepts configured types and rejects or prevents selection of a type outside the configuration.
- The collection field retains all submitted values, and the catalog field retains both keys and values.
- A declared JSON object or block-container feature groups fields visually.
- A declared UTF-8 feature has UTF-8 database or cluster configuration and round-trips multilingual text unchanged.
- Declared GeoPoint and GeoShape features round-trip latitude and longitude and polygon or boundary values respectively.
- A RECOMMENDED feature not declared met is reported as not tested, not failed.

<a id="drs-4"></a>
## DRS-4

**Fixture**

- An authorised registry administrator.
- A draft registry with one text field and one record.
- A compatible schema change and a known breaking schema change.

**Actions**

1. Publish the draft through the web user interface and record the resulting schema and API-service version.
2. Apply the compatible change and publish again.
3. Inspect the earlier schema version and use its data through both the earlier and later versions.
4. Submit the known breaking change for change-impact analysis.
5. Delete a disposable schema version through the user interface and then attempt to use its same-version API service.

**Expected results**

- Each publish reveals the database to users and creates a new version of both the schema and API services.
- The earlier schema remains available to authorised users.
- Data stored under the earlier version remains usable under both tested versions. The evidence records the solution's compatibility or migration mechanism because DRS-4 does not define one.
- The breaking change is identified automatically and a warning is shown before or during the analyst's change workflow.
- Deleting the schema version also removes its same-version API services.

<a id="drs-5"></a>
## DRS-5

**Fixture**

- An authorised registry administrator and an account without API-configuration permission.
- A draft registry with fields and sample records.
- One database view, used only by the custom-read step; that step depends on the recorded DRS-5/DRS-9 source conflict (DRS-5 requires view-based custom read services, DRS-9 marks views OPTIONAL).
- The solution's documented subscription operation, because the source OpenAPI documents contain no subscription operation.
- If dynamic field masking is declared met, two callers whose policies produce masked and unmasked views of one field.

**Actions**

1. Configure API services for the registry through the user interface and publish it.
2. Discover and exercise generated create, read, update, delete, batch create, batch update, batch delete, exists (checks whether matching data exists), update-or-create, archive, and schema-introspection services. Record the solution's operations for batch create, batch delete and archive, because the source templates define no generic operation for them.
3. Compare introspection output with the published tables, fields, types, and relationships.
4. Hide or disable one disposable service, delete another, copy a third, and create a custom read service from the prepared view (this step depends on the recorded DRS-5/DRS-9 source conflict).
5. Use the documented subscription operation and produce create, update, and delete changes for a subscribed record.
6. Change the dynamic database structure, publish again, and compare the generated API data structure before and after publication.
7. If dynamic masking is declared met, read the protected field as both policy contexts.
8. Repeat API-configuration actions with the account that lacks permission.

**Expected results**

- Publishing generates each required service, and every exercised service performs its named operation. The exists service reports whether matching data exists.
- Schema introspection matches the published schema.
- Hidden or disabled, deleted, and copied services exhibit their respective configured states. A custom view-based service does so where the solution offers database views; the source makes views OPTIONAL in DRS-9 but requires the service in DRS-5, and the result records that conflict.
- The subscription delivers the tested create, update, and delete changes through the solution-supplied operation. The result cannot establish a shared operation binding until the source contract defines one.
- Republish regenerates the API data structure from the changed database structure.
- When masking is declared met, the protected caller receives the dynamically masked value and the permitted caller receives the unmasked value. Otherwise the RECOMMENDED item is reported as not tested.
- The account without permission cannot change API-service configuration.

<a id="drs-6"></a>
## DRS-6

**Fixtures**

1. Create two registries with linked records and fields classified as public and restricted.
2. Create an administrator, an operator, an ordinary authenticated user, an anonymous client, two groups, and roles that grant disjoint rights.
3. Configure representative RBAC, ABAC, PBAC, consent, delegated-access, data-minimisation, cross-registry-template, and record-value conditions. Include `CaseStatus=APPROVED` as one field condition.

**Actions and expected results**

1. Attempt registry creation and administration as the administrator and ordinary user. The authorised action succeeds, the unauthorised action is denied, and the denied action changes nothing.
2. Exercise each API service with rights varied independently at service, record, and field scope. Each response follows the scope-specific decision and returns no denied field.
3. Repeat a data read through the user interface and the API with an allowed and denied actor. Both boundaries enforce the same configured data-access decision.
4. Manage the same user right through the rights-management UI and API. The resulting policies are equivalent. If the candidate cannot bind the API action to a published operation, record the binding gap rather than passing the API check.
5. For RBAC, ABAC, PBAC, consent, and delegated access, run one allowed and one denied request per policy kind. The decision log identifies the policy inputs used.
6. Apply a cross-registry access template to the second registry. Its resulting rights match the template without altering unrelated rights.
7. Request a record containing more fields than the caller needs. The response contains only the fields permitted by the minimisation rule.
8. Read otherwise identical records with approved and non-approved case status. The conditionally restricted field appears only for the approved record.
9. Assign rights directly to one user and through one group. Confirm that a group contains users, a role contains rights, and both assignment paths affect access as configured.
10. Exercise the `Any logged-in user` and `Anonymous` roles with authenticated and unauthenticated clients. Each role is selectable and produces the configured decision.

<a id="drs-7"></a>
## DRS-7

**Fixtures**

1. Create a registry with a schema and one record containing personal data linked to an owner.
2. Create an analyst, the data owner, a second owner, and an unauthorised user.

**Actions and expected results**

1. Change the schema, then create, read, update, and delete record data. The audit log contains a corresponding event for every action and no unexplained gap.
2. In the analyst UI, search for each event by its available identifiers and time. Every event is visible and discoverable.
3. Confirm that at least one of the two `owner-log-visibility` options is provided: the owner API (`DPU`) or the owner UI. For each provided option, the owner sees the identity of each reader or processor and the matching events for the owner's data, but not the second owner's events. If neither option is provided, the variation point is unmet.
4. Inspect the log-integrity design and verify a representative chain. Alter a copied log entry and confirm that integrity verification detects the change.
5. If external-blockchain logging is implemented, correlate a database log entry with its external transaction evidence and verify that a changed entry no longer matches. If it is omitted, record the RECOMMENDED requirement as unmet without failing core conformance.

<a id="drs-8"></a>
## DRS-8

**Fixtures**

1. Create a registry with a `PersonalData` field, a unique and unchangeable `PersonalDataID`, and two owners.
2. Create an analyst, each owner, and readers with distinct IDs, names or initials, roles, organisations, and locations.
3. Configure one read for which law requires a legal justification, one consent-governed read, and one read to which neither condition applies.

**Actions and expected results**

1. Read personal data through the UI and through the API. The log table contains one event for every read boundary.
2. Inspect each personal-data event. It is tagged `PersonalData` and includes log ID, record ID, field ID, unique and unchangeable `PersonalDataID`, reader ID, reader name or initial, read time, viewer role, organisation, and location (the `(optional)` marker is read as scoping only the device fingerprint).
3. Confirm that the legally governed event includes the legal justification and the consent-governed event includes the consent reference. The unrelated event need not contain those conditional values.
4. As the analyst, open the personal-data report and see all recorded personal-data reads. As each owner, see only that owner's events. The unauthorised user and other owner cannot retrieve them.
5. Call `DPU` with the configured owner identifier and database identifier. The response contains that owner's usage events for that registry. The upstream scenarios in [`data_my_personal_data_usage.feature`](../test/openAPI/features/data_my_personal_data_usage.feature) provide positive and invalid-user or invalid-database examples.
6. Read the personal-data report through each exposed boundary. A new report-read event appears in the log table.
7. If device-fingerprint logging is implemented, confirm that a representative read event contains the viewer device fingerprint. If it is omitted, record the RECOMMENDED requirement as unmet without failing core conformance.

<a id="drs-9"></a>
## DRS-9

If the `database-views` extension is not claimed, record this functionality as not applicable. If it is claimed, use these checks.

**Fixtures**

1. Create records with fields and rows that a view includes and excludes.
2. Create an authorised operator, an ordinary authenticated user, and an anonymous client with distinct view rights.

**Actions and expected results**

1. Create a view in the UI. Its result contains exactly the selected registry data.
2. Expose the view as Open Data. The anonymous client can read it under the configured anonymous rights.
3. Expose the view through a custom read API and retrieve the same selection. If no source operation binds the API, record the known binding gap rather than inventing one.
4. Attempt to update and delete data through the view and its API. Both mutations are rejected and source data remains unchanged.
5. Deny view access to the ordinary user through rights management. The user's UI and API reads are denied, while the authorised operator remains allowed.

<a id="drs-10"></a>
## DRS-10

**Fixture**

- An authorised registry administrator and a registry schema containing every core DRS-3 field type.
- The solution's declaration of whether the required `JSON/YAML` wording is met by JSON, YAML, or both.
- If XLS export is declared met, an XLS reader capable of inspecting every exported schema element.

**Actions**

1. Export the schema in every JSON or YAML format the solution declares as satisfying the required source wording.
2. Record the exact exported file profile, because the source defines no schema export file format, and compare each exported file field by field with the source schema.
3. If XLS export is declared met, export and inspect the XLS file in the same way.

**Expected results**

- Every declared required format produces a parseable file containing the complete schema without changed names, types, properties, or relationships.
- The result records whether JSON, YAML, or both were tested, because DRS-10 does not resolve the slash notation.
- A declared XLS export produces an XLS file with the same schema content; otherwise that RECOMMENDED item is reported as not tested.

<a id="drs-11"></a>
## DRS-11

**Fixture**

- An authorised registry administrator and an empty registry instance.
- JSON and YAML representations of the same schema, including every core DRS-3 field type and one relationship.
- The solution's declaration of whether the required `JSON/YAML` wording is met by JSON, YAML, or both.
- If XLS import is declared met, an equivalent XLS schema file.

**Actions**

1. Import every JSON or YAML format the solution declares as satisfying the required source wording.
2. Record the exact accepted file profile, because the source defines no schema import file format, then read the resulting schema and compare all names, types, properties, and relationships with the input.
3. If XLS import is declared met, import the XLS file and make the same comparison.

**Expected results**

- Every declared required format creates the complete intended schema without changed names, types, properties, or relationships.
- The result records whether JSON, YAML, or both were tested, because DRS-11 does not resolve the slash notation.
- A declared XLS import creates the same schema from XLS; otherwise that RECOMMENDED item is reported as not tested.

<a id="drs-12"></a>
## DRS-12

If the `service-usage-statistics` extension is not claimed, record this functionality as not applicable. If it is claimed, use these checks.

**Fixtures**

1. Select every exposed API service at least once and identify one UI search and one API search that return known records.

**Actions and expected results**

1. Invoke every API service in the fixture. Usage storage contains a distinct, attributable record for every invocation.
2. Run the UI search and API search. Usage storage contains both events and distinguishes their boundary.
3. Repeat one invocation and each search. Counts or event rows increase exactly once per action, with no missing or duplicate usage event.

<a id="drs-13"></a>
## DRS-13

This is a RECOMMENDED core behaviour. If it is omitted, record the recommendation as unmet without failing core conformance.

**Fixtures**

1. Create a registry schema with one ordinary field and one field that contains personal data.

**Actions and expected results**

1. Mark the personal field as a `PersonalData` log object and publish the schema. The marker persists and the ordinary field remains unmarked.
2. Read both fields. The personal-data log identifies the marked field as personal data and does not misclassify the ordinary field.

<a id="drs-14"></a>
## DRS-14

These are RECOMMENDED core behaviours. Record each omitted recommendation as unmet without failing core conformance.

**Fixtures**

1. Create national, passport, and local owner identifiers with known-valid and known-invalid values.
2. Provide a stand-in external registry that records identifier-link requests.

**Actions and expected results**

1. Mark a field as `PersonalDataID`. The marker identifies that field as the data owner's identifier.
2. Configure all three identifier kinds for one owner. The registry retains each identifier without replacing another.
3. Apply an identifier validation rule. The valid value is accepted and the invalid value is rejected without changing the prior value.
4. Link an identifier to the stand-in external registry. The recorded call identifies the intended owner and identifier. If the source contract remains unspecified, record the binding gap.
5. Mark an identifier immutable, then attempt to change it through every exposed mutation boundary. Every attempt is rejected and the stored value remains unchanged.

<a id="drs-15"></a>
## DRS-15

**Fixtures**

1. Create a registry with a normal field and a secret field containing representative card data.
2. Configure a Building Block exchange through the Information Mediator path used by the candidate deployment.

**Actions and expected results**

1. Mark the card-data field as secret. The marker persists after publication.
2. Inspect storage evidence for the secret and normal values. The secret value is not present at rest in plaintext, and authorised use still returns the correct decrypted value.
3. Capture the Building Block exchange at the transport boundary. The information is encrypted in transit and the integration evidence identifies the applicable Information Mediator rules. If no versioned rule can be identified, record the contract gap.

<a id="drs-16"></a>
## DRS-16

**Fixture**

- An authorised registry administrator.
- A published schema with named fields, types, properties, and one relationship.

**Actions**

1. Open the registry schema through the web user interface.
2. Compare the displayed schema with the published schema definition.

**Expected results**

- The interface displays the correct fields, types, properties, and relationship for the selected registry schema.

<a id="drs-17"></a>
## DRS-17

**Fixture**

- An authorised registry administrator and an account without schema-configuration permission.
- A draft schema with text, number, array, catalog, encrypted, and foreign-key fields.
- Sample records that meet and violate required, unique, minimum, and maximum rules.
- Trigger cases for identifier creation, field merging, prefix, suffix, conditional logic, upper case, lower case, and JavaScript transformation.

**Actions**

1. Configure API-related required, unique, maximum, minimum, and blinded or encrypted properties.
2. Configure user-interface field mask and format, read-only, personal-data, enum selection, blinded or encrypted, multiple-value or array, foreign-key, and trigger properties.
3. On the multiple-value field, configure array type plus Required, Unique, maximum, and minimum validation and a foreign key to another registry in the instance.
4. Create and change records that exercise each validation rule and each configured trigger action.
5. Exercise trigger conditions once when false and once when true.
6. Attempt to change these field properties with the account that lacks permission.

**Expected results**

- The schema retains every configured API-related and user-interface-related property.
- Required, unique, minimum, and maximum rules accept conforming values and reject violating values at their configured boundaries.
- Blinded or encrypted, read-only, mask, format, personal-data, enum, multiple-value, and foreign-key properties produce their configured visible behaviour.
- Multiple values are retained as an array and obey their validation and foreign-key settings.
- Every listed trigger performs its configured action on record creation or change only when its condition is true; the false case does not perform the action.
- The JavaScript result records the solution's execution environment and safeguards, because DRS-17 does not define them.
- The account without permission cannot change field properties.

<a id="drs-18"></a>
## DRS-18

**Fixtures**

1. Create two registries with different records and configure a distinct encryption key for each.
2. Create an authorised operator, an application with the first key, an application with the second key, and an application with no key.

**Actions and expected results**

1. Inspect both database configurations. Each database has its own unique configured key and the keys differ.
2. Enter the key in the UI and revisit the configuration. The UI blinds the stored key and does not disclose it in page source or ordinary responses.
3. Store and retrieve encrypted data in each database. Evidence shows the database's own key is used for encryption and decryption, and swapping keys does not decrypt the other database's data.
4. Call `read` with an application that knows the correct key, the wrong key, and no key. Only the correct-key case reads encrypted data. The source `read` contract exposes no key parameter, so retain the request evidence and record that binding gap.
5. View the encrypted record as an authorised operator. The UI displays the decrypted data without displaying the key.

<a id="drs-19"></a>
## DRS-19

**Fixtures**

1. Create source records that exercise true and false conditions, and same-instance destinations that exercise one-to-one, many-to-one, and one-to-many mappings.
2. Provide a stand-in external registry API that records calls and returns known responses.
3. Configure input and output mappings with query and answer parts, a short interval, grouped `AND` and `OR` rules, and a webhook trigger.

**Actions and expected results**

1. Start the interval automation. It processes one corresponding record at a time, loops until all corresponding records are processed, and stops without duplicating a completed record.
2. Run records that make the grouped conditions true and false. Only true conditions activate an exchange, with `AND` and `OR` producing the configured results.
3. Send mapped data to a second database in the same instance. The destination fields equal the configured output mapping and unrelated fields remain unchanged.
4. Send mapped data to the stand-in external API. The recorded request contains the mapped output and the registry records the configured answer mapping. Record the contract gap because the source names no external API contract.
5. Exercise many-to-one and one-to-many mappings. The number and content of destination records match each configured cardinality.
6. Activate the webhook trigger. Exactly one configured exchange starts. Record whether the deployment receives, publishes, or observes the webhook because the source leaves that boundary ambiguous.
7. If transformation is implemented, configure `est` to `EST` and confirm the destination contains `EST`. If it is omitted, record the RECOMMENDED requirement as unmet without failing core conformance.

<a id="drs-20"></a>
## DRS-20

**Fixture**

- A solution that claims the Schema Templates extension.
- An authorised template administrator and an account without template-management permission.
- A source registry containing a schema, API configuration, and sample template metadata, plus views where the solution also claims the Database Views extension (DRS-20 includes views in a full template while DRS-9 makes views OPTIONAL; the source does not say what a template contains otherwise).
- A second clean instance or isolated tenant for import.
- If the nested domain-template recommendation is declared met, Health, Business, and Farmer templates.

**Actions**

1. Create a template from the source registry and use it to create another registry.
2. Share the template with another user in the same instance and confirm that user can discover and use it through the internal marketplace.
3. Export the template, inspect its package contents, and import it into the clean instance or tenant. Record the package format used, because the source defines no registry-template package format.
4. Share the template through the solution's marketplace workflow and record the workflow used, because DRS-20 does not define a marketplace protocol.
5. Create a second version of the template, then retrieve and use both versions from the template repository.
6. If domain templates are declared met, create registries from the Health, Business, and Farmer templates.
7. Attempt template creation, sharing, export, and import with the account that lacks permission.

**Expected results**

- A registry created from the template contains the intended registry definition, schema, views (where the Database Views extension is claimed), and API configuration.
- Internal sharing makes the same template available to the selected user in the instance.
- Export and import preserve the full registry, schema, views (where the Database Views extension is claimed), API configuration, and template metadata.
- The marketplace workflow shares the template by the documented solution mechanism without implying a shared GovStack marketplace protocol.
- Both template versions remain distinguishable and usable in the versioned repository.
- When domain templates are declared met, all three named domains create their corresponding registry structures. Otherwise the RECOMMENDED item is reported as not tested.
- The account without permission cannot manage or transfer templates.

<a id="drs-21"></a>
## DRS-21

**Fixtures**

1. Create records whose combined grid and detail fields cover all registry data, with one image and one non-image document.
2. Create known create, update, delete, read, and export events using two readers.

**Actions and expected results**

1. Open the main grid and each detail view. Every registry data element is reachable and each selected grid record opens the matching detail record.
2. Open the image document. It renders in the UI. Open the non-image document. It is offered as a download with unchanged content.
3. Open the data log view. It shows the create, update, and delete changes and the before-and-after data for each change that has both states.
4. Open the data read view. It shows information about who looked at or exported the data.
5. Inspect the log registry. It stores the data and the data reader information for the looks and exports performed in the fixtures.

<a id="drs-22"></a>
## DRS-22

**Fixtures**

1. Create one editable record with an ordinary field, a blinded or encrypted field, and two documents.
2. Create an authorised operator and a read-only user.

**Actions and expected results**

1. Edit the ordinary field inline in the main grid and through the detail view. Each saved value is returned by a fresh read.
2. Upload one document and remove another in the detail view. The resulting document set and contents match the actions.
3. Inspect the blinded or encrypted field in edit mode. The UI applies the configured protection and does not reveal protected content to the read-only user.
4. Delete the record as the authorised operator. It is no longer available through the operator view.
5. Attempt each mutation as the read-only user. Every action is denied and data remains unchanged.
6. Inspect the audit log. Every successful edit, document addition or removal, and deletion has a corresponding event; denied attempts do not appear as successful changes.

<a id="drs-23"></a>
## DRS-23

**Fixtures**

1. Create records with distinguishable values in every field and a text phrase that occurs in only one record.

**Actions and expected results**

1. Apply a field-content criterion. The result includes every matching record and no non-matching record.
2. Run a full-text search for the unique phrase. It returns the intended record.
3. Sort ascending and descending by every data field. Each result follows the field's defined ordering, including equal values and empty values.

<a id="drs-24"></a>
## DRS-24

**Fixtures**

1. Prepare equivalent JSON, CSV, and XLS files containing new records, plus a malformed file in each format.

**Actions and expected results**

1. Import each valid file. A fresh registry read returns all expected values with no duplicate records.
2. Import each malformed file. The import fails visibly, identifies the invalid input, and does not partially create data unless the candidate explicitly documents and reports partial-import semantics.
3. Record the exact accepted file profile because the source names formats but defines no schema or validation contract.
4. In the analyst UI, choose the import action for a registry database and complete one import. The UI offers the action and the imported data appears in the registry.

<a id="drs-25"></a>
## DRS-25

**Fixtures**

1. Create records for which a filter selects a strict subset and a field selection omits at least one field.

**Actions and expected results**

1. Export the selected or filtered data separately as CSV, XLS, and JSON.
2. Parse each output with an independent format parser. Every file contains exactly the selected records and fields, with values matching the registry.
3. Record the exact produced file profile because the source names formats but defines no schema or validation contract.
4. In the analyst UI, select a subset of records, then filter records, and choose the export action for each. The UI offers the action and the export contains exactly that selection or filter result.
5. Record whether CSV and XLS are both produced; the source writes `CSV/XLS, JSON` and does not say whether both are required.

<a id="drs-26"></a>
## DRS-26

**Fixtures**

1. Create people and service records across multiple dates, then change selected data elements to produce audit events.
2. Identify registry fields from which to build a custom report and an authorised external analytics client.

**Actions and expected results**

1. Generate the standard reports. They include all registered items and can be filtered to details of people, details of services, registration changes over time, and changes to data elements from audit logs.
2. Build a report from selected registry fields. Its columns, filters, and values match the configuration.
3. Analyze the collected data in at least two different ways, using the available reports or other analysis functions. Each result is reproducible from the fixture.
4. Call `list` as the external analytics client and reconcile the extracted records to the source registry. An unauthorised client is denied. Record that the binding to `list` is an interpretation and that the DRS-26 header reads `should ... (REQUIRED)`.
5. If custom dashboards are implemented, build a dashboard from registry data and reconcile every displayed measure to the source records. If omitted, record the RECOMMENDED requirement as unmet without failing core conformance.

<a id="drs-27"></a>
## DRS-27

**Fixtures**

1. Create a record with shareable and restricted fields, an authorised sender, anonymous recipient, consented recipient, non-consented recipient, allowed role, and denied role.

**Actions and expected results**

1. Confirm that at least one of the two `sharing-channels` options is provided: email, or a unique and secure URL. If neither is provided, the variation point is unmet. Share through each provided channel; each works and exposes only the selected record and fields.
2. Turn sharing off in the authorisation module and repeat. No new share is created and existing behaviour follows the documented disablement semantics.
3. Create an anonymous share. It is accessible without authentication and is identified as Open Data by the registry.
4. Actions 4 to 7 apply to sharing links. A candidate that provides email only records them as untestable and notes that the source presupposes a link in items 1 to 4. Create a time-bound link, use it before and after expiry, and confirm that only the pre-expiry access succeeds.
5. Create a consent-required link. The non-consented recipient is denied, and the consented recipient is allowed.
6. Create a role-restricted link. The allowed role succeeds, and the denied role fails without disclosure.
7. Generate the QR code and resolve it. It identifies the intended sharing link without exposing additional data in the code.
8. Download through a share that permits export. The downloaded file contains a visible or machine-verifiable watermark.
9. Open a view-only share. The data is readable, but export and direct download are unavailable or denied.

<a id="drs-28"></a>
## DRS-28

**Fixture**

- An authorised API client and a client without registry-creation permission.
- A create request containing a database name, short name, and a DRS-3 schema.
- The `modifyDatabase` operation from `resources/api.yml`, whose request defines `code`, `schema`, `groupName` and `catalogName` but no database-name field.

**Actions**

1. Send the create request through `modifyDatabase` with the authorised client.
2. Read the resulting registry schema and compare it with the request.
3. Repeat the create request with the client that lacks permission.

**Expected results**

- The authorised request creates one registry with the submitted name, short name, and schema. Record how the database name is conveyed, because the bound request defines no database-name field.
- The read-back schema matches the request.
- The client without permission cannot create a registry.

<a id="drs-29"></a>
## DRS-29

**Fixture**

- An authorised API client.
- Three distinct registry create requests with unique names, short names, and schemas.
- The `modifyDatabase` operation from `resources/api.yml`.

**Actions**

1. Submit all three requests through `modifyDatabase` to the same system instance.
2. List the registries in that instance and read back each schema.

**Expected results**

- All three registry databases coexist in the same instance.
- Each registry retains the name, short name, and schema from its own request without overwriting either of the others.

<a id="drs-30"></a>
## DRS-30

**Fixture**

- An authorised API client, a client without publish permission, and a draft registry not visible to ordinary users.
- The solution's documented registry-publish operation, because neither source OpenAPI document defines one.

**Actions**

1. Invoke the documented publish operation with the authorised client.
2. Attempt to discover or access the registry as an ordinary permitted registry user.
3. Repeat against another draft registry with the client that lacks publish permission.

**Expected results**

- The authorised API request publishes the registry and reveals it to users who are permitted to see published registries.
- The client without publish permission cannot publish the second registry.
- The procedure records the implementation-specific operation used and does not claim a shared API binding until the source contract defines one.

<a id="drs-31"></a>
## DRS-31

**Fixture**

- An authorised API client and a client without API-configuration permission.
- A draft registry, a changed version of its schema, and one disposable custom API service.
- The solution's documented operations for modifying, hiding, deleting, copying, and creating custom API services, because neither source OpenAPI document defines them.

**Actions**

1. Use the documented configuration operation to modify the services of the draft registry.
2. Publish the registry and exercise generated create, read, update, delete, exists, and update-or-create services.
3. Change the dynamic database structure, publish again, and compare the generated API data structure before and after publication.
4. Through the documented operations, hide one service, delete a disposable service, copy another service, and create the prepared custom service.
5. Repeat each configuration action with the client that lacks permission.

**Expected results**

- The authorised client can modify the registry's service configuration through the documented solution operations.
- Publication automatically creates all required data services, and each exercised service performs its named operation.
- Republish regenerates the API data structure from the changed database structure.
- Hidden, deleted, copied, and custom services exhibit their respective configured states.
- The client without permission cannot change API-service configuration.
- The procedure records every implementation-specific configuration operation and does not claim a shared API binding until the source contract defines one.

<a id="drs-32"></a>
## DRS-32

**Fixture**

- An authorised API client and a client without schema-read permission.
- A published registry with a known schema and several available API services.
- The `getDatabase` operation from `resources/api.yml`.
- The `genericServices` field of the `getDatabase` response, which the source describes as the list of possible API services for the database, each with `isVisible`.

**Actions**

1. Call `getDatabase` for the published registry and compare the returned schema with the known schema.
2. Read `genericServices` from the same `getDatabase` response and compare the listed services and their `isVisible` flags with the registry's published service configuration.
3. Repeat both reads with the client that lacks permission.

**Expected results**

- `getDatabase` returns the complete schema of the requested registry.
- `genericServices` lists every service available for that database and no service from another database.
- The client without permission cannot read the protected schema or service list.
- The procedure does not bind the requirement to `listDatabases`, which lists databases rather than their services.

<a id="drs-33"></a>
## DRS-33

**Fixtures**

1. Create an authorised API client, an unauthorised client, and a registry with known records.

**Actions and expected results**

1. As the authorised client, exercise `list`, `create`, `read`, `update`, `delete`, and `update-or-create`. Reconcile every response and resulting state to the requested operation.
2. Repeat each operation as the unauthorised client. Every request is denied and registry state remains unchanged.
3. Run the matching pinned upstream feature scenarios in [`data_list.feature`](../test/openAPI/features/data_list.feature), [`data_create.feature`](../test/openAPI/features/data_create.feature), [`data_read.feature`](../test/openAPI/features/data_read.feature), [`data_update.feature`](../test/openAPI/features/data_update.feature), [`data_delete.feature`](../test/openAPI/features/data_delete.feature), and [`data_update_or_create.feature`](../test/openAPI/features/data_update_or_create.feature). Record results without treating these source scenarios as coverage of authorisation unless the harness actually exercises denied clients.

<a id="drs-34"></a>
## DRS-34

**Fixture**

- A registry with at least two published API-service versions.
- At least one request and response field per operation, each with a description and example value.
- Access to the solution's OpenAPI description and its Swagger or equivalent visualisation.
- A client system with no administrative access to the registry.

**Actions**

1. Parse the OpenAPI description and enumerate every documented API service and version.
2. Compare that enumeration with the published API-service inventory.
3. Inspect every request and response field for a description and example value.
4. Open the visualisation and navigate to every service and version found in the OpenAPI description.
5. As the client system, retrieve the OpenAPI description of every service and version. Record the solution's retrieval mechanism, because neither source OpenAPI document defines an operation or endpoint that publishes service descriptions.
6. Where the solution marks an example as safely executable, run it and record whether it succeeds. Do not substitute production personal data merely to make an example real.

**Expected results**

- The OpenAPI description covers every published API service and service version.
- Every described field has a field description and example value.
- The visualisation exposes every service and version from the OpenAPI description.
- The client system can retrieve the description of every service and version; the result records the implementation-specific retrieval mechanism and does not claim a shared API binding.
- Safely executable examples behave as documented. Examples not marked executable remain inspected examples, because DRS-34's "if possible" wording does not define a mandatory condition.

<a id="drs-35"></a>
## DRS-35

**Fixtures**

1. Create a personal-data registry with two owners and known usage events, plus an analyst and an unauthorised user.

**Actions and expected results**

1. Configure which unique owner identifier the personal-data usage API accepts. The chosen identifier persists and is used by subsequent queries.
2. Link every personal-data record to its owner. An owner identifier resolves to that owner's data and not the other owner's data.
3. Call `DPU` with the configured owner identifier and database identifier. The response contains the matching usage events. Invalid owner and database inputs fail as illustrated by [`data_my_personal_data_usage.feature`](../test/openAPI/features/data_my_personal_data_usage.feature).
4. Repeat as the unauthorised user. Access is denied without disclosing whether another owner's data exists.

<a id="drs-36"></a>
## DRS-36

If the `statistics-api` extension is not claimed, record this functionality as not applicable. If it is claimed, use these checks.

**Fixtures**

1. Create registration and programme records spanning multiple date and time ranges and at least two registered programmes.
2. Create clients authorised for all data, one programme only, and no statistical data.

**Actions and expected results**

1. Query registration data and programme data separately. Each response contains the requested data kind.
2. Query by date and time range. Boundary values are handled consistently and only in-range data is returned.
3. Query by registered programme. Only records for the selected programme are returned.
4. Combine the range and programme parameters. The result satisfies both filters.
5. Repeat with each client. Results contain only authorised data, and the unauthorised client is denied without data leakage.
6. Record the operation binding gap because the source API descriptions do not identify a statistical-query operation.

<a id="drs-37"></a>
## DRS-37

**Fixtures**

1. Create two physical-person owners, personal-data fields marked by an analyst, and read and processing events by distinguishable actors.

**Actions and expected results**

1. Confirm that at least one of the two `owner-log-visibility` options is provided: the owner UI or the owner API (`DPU`). If neither is provided, the variation point is unmet.
2. For each provided option, act as the first owner. In the UI, open the personal-data report; through the API, call `DPU` with the first owner's unique identifier and database identifier. The result identifies who read or processed that owner's data and does not include the second owner's events. If both options are provided, the API result matches the UI result.
3. Attempt each provided boundary as the second owner and an unauthorised user for the first owner's identifier. Access is denied or restricted to the caller's own events without disclosing the first owner's log.
4. Confirm that events for unmarked ordinary data are not misrepresented as personal-data events. Record the source ambiguity if the candidate lacks the RECOMMENDED field-tagging capability on which this required report relies.

<a id="supplementary"></a>
## Supplementary upstream chapters

**Fixtures:** two registry-schema versions; representative records with each of the eleven minimum fields; administrator, authorised applicant, denied caller and explicitly enabled anonymous sandbox contexts; an event broker and external/internal consumers; the selected original API templates and the deployment's declared bindings.

**Actions and expected results:**

1. Create registries for multiple tenants. Publish schema changes, deprecate and archive versions, and inspect compatibility guidance and synchronized generated service versions. Compare the observable outcomes with the source workflow, retaining its network, power and authorisation preconditions.
2. Configure deduplication, data-quality controls, masking and redaction; demonstrate the policy effects in the analyst interface. Demonstrate logical deletion and archival, respecting the inherited exception for legally mandated hard deletion.
3. Inspect generated REST and GraphQL services and API descriptions. Exercise every operation bound in the authoring projection with fixtures valid under its original request schema, check the documented response schema, and compare deployment parameter substitutions with the original template. Record unsupported or unspecified bindings rather than guessing an endpoint.
4. Create, update and delete a record and observe the corresponding domain events. Check external subscriptions through the named mediator boundary, and test any offered direct internal route with role/attribute policy, tenant isolation and audit controls. Record missing event contracts as source gaps.
5. Exercise schema CRUD and applicant data operations for authorised, denied and explicitly enabled anonymous contexts. Verify denial where neither an explicit nor an anonymous grant applies. Record the source's unresolved broad authenticated-read wording and authorisation wording; this migration supplies no new precedence rule.
6. Inspect the dedicated change-log database and audit registry after the workflows. Compare recorded processing events with the actions performed. Inspect usage, performance and data-quality statistics for the analyst.
7. Inspect model evidence for all eleven required fields, their types and meanings, and the four original relationship/cardinality statements. Compare the model with the preserved source table and diagram rather than inventing JSON names.
8. Review inherited data-protection evidence and deletion policy against the two elevated source CFR requirements. Demonstrate logical record preservation, or the documented legal basis for mandated hard deletion. Record evidence and unresolved source ambiguities without treating an authoring check as runtime certification.
