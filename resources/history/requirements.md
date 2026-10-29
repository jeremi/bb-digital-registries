---
title: Archived requirements
description: Nonnormative archive of the requirement blocks replaced by the framework-format migration.
---

# Archived Requirements

This file is a nonnormative historical archive. The blocks below preserve the 15 DRAFT requirements in the committed `3.0.0-alpha.2` baseline; they do not define current conformance requirements and their legacy identifiers do not identify the current unnumbered drafts. [Revised requirement blocks](#revised-requirement-blocks) preserves the later old-layout wording that the current drafts also carry.

Current draft targets are recorded in [the requirement migration ledger](../requirement-migration.yml) by functionality filename and exact statement because DRAFT requirements have no identifiers.

## Registry Core functional requirements

### #1 Publish Registry metadata (DRAFT EXTENSIBLE AUDITABLE)

`govstack-bb-digital-registries-fr-core#req-1`

`KF: Registry Core`

An implementation publishes machine-readable Registry metadata containing a globally unique and stable Registry Identifier, a human-readable Registry name, the identity of the Registry Authority, a description of its authoritative scope, and a reference identifying the Digital Registries specification version used to describe the implementation. The publication URI and access conditions are made available to the intended API consumers.

**Purpose:** An adopter can determine which Registry and authority stand behind a service, what information that authority accepts responsibility for, and which specification version the description references.

**Prerequisite:** The Registry Authority and authoritative scope have been established by the adopting organisation.

**Verification:** Access the metadata as an intended consumer, validate that all required values are present, check that the description states the authoritative scope, and review evidence that the Registry Identifier is not shared with another Registry or changed between service revisions.

### #2 Identify each returned Record (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-core#req-2`

`KF: Registry Core`

Every returned Record representation includes a Record Identifier that is unique within an unambiguous Registry context. The applicable binding defines how the consumer determines the Registry Identifier from the request, published contract and service metadata, or the representation itself. Together, the two identifiers uniquely identify the Record.

**Purpose:** Consumers can distinguish Records from different Registries and refer to one Record without depending on mutable domain attributes.

**Prerequisite:** A Record has been accepted into the Registry.

**Verification:** Obtain two distinct Record fixtures through an implemented capability that returns Records and verify their different Record Identifiers and the Registry context established by the binding. If a service spans multiple Registries, verify that identical local identifiers in those Registries remain distinguishable.

### #3 Preserve Record Identifiers (DRAFT EXTENSIBLE AUDITABLE)

`govstack-bb-digital-registries-fr-core#req-3`

`KF: Registry Core`

An implementation keeps a Record Identifier unchanged throughout that Record's lifecycle and revisions and never reassigns the identifier to a different Record. An adaptor over an existing source can satisfy this by declaring that it inherits the source's identifier policy, when that policy meets these conditions.

**Purpose:** A Record reference remains unambiguous after changes, retirement, archival, or deletion.

**Prerequisite:** The implementation has a documented Record Identifier lifecycle policy, which can be the source system's policy adopted by an adaptor.

**Verification:** Review the identifier policy and evidence showing that successive revisions retain the same identifier, distinct Records do not share an identifier, and retired identifiers are not returned to the allocation pool.

### #4 Identify the representation schema and field meanings (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-core#req-4`

`KF: Registry Core`

Every returned Record representation has an unambiguously identified, resolvable machine-readable schema and documented field meanings. The applicable binding identifies its representation format and how the consumer selects the schema. A formal semantic-model reference is provided when required by the selected capability or profile.

**Purpose:** Consumers can decode, validate, and interpret a representation without knowledge of internal storage.

**Prerequisite:** The implementation has published the applicable representation format, schema, and domain documentation.

**Verification:** Obtain a Record representation through an implemented capability, identify its format and schema using only the published contract and response context, and validate it. Check adopted model versions, mappings, and extensions where used. Check the documentation for field meanings, units, code lists, and absence semantics, including whether nested objects are components, Record references, or embedded representations. For references, verify the target Registry context and any declared read binding. For embedded collections, verify the declared bounds and completeness semantics. Resolve a formal semantic-model reference when the selected contract requires one.

### #5 Describe provided revision and lifecycle metadata (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-core#req-5`

`KF: Registry Core`

When an implemented capability exposes revision or lifecycle metadata, it defines those fields in the representation schema and returns values with the declared source semantics. A capability or profile requiring those fields supplies its additional guarantees; baseline Record reads do not require them.

**Purpose:** Consumers can interpret available revision and lifecycle information without inferring guarantees that the source does not provide.

**Prerequisite:** The selected contract exposes revision or lifecycle metadata. Otherwise, this requirement's metadata scenarios are not applicable.

**Verification:** Compare the provided metadata with source fixtures and the declared schema. Verify the meaning of revisions and exposed lifecycle states. Check that a representation validator is not presented as a source revision unless the source contract establishes that equivalence.

### #6 Describe provided Record provenance (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-core#req-6`

`KF: Registry Core`

The Registry context identifies the responsible Registry Authority through published metadata. When additional Record provenance is exposed, the contract defines its meaning and the implementation returns values supported by the source. A revision recording time is required only when the selected capability or profile requires it; retrieval time is not substituted for recording time.

**Purpose:** A consumer can identify the institutional source and interpret available provenance without fabricated source facts.

**Prerequisite:** Registry metadata identifies the authority. Additional provenance fixtures are required only for fields exposed by the selected contract.

**Verification:** Resolve the Record's Registry context to its published authority. For every additional provenance field exposed by the contract, compare its value and meaning with source evidence. Verify that unavailable optional provenance is omitted rather than inferred from the adapter's response time.

### #7 Publish service discovery metadata (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-core#req-7`

`KF: Registry Core`

For each service exposed through the Digital Registries capability model, an implementation publishes a machine-readable service description associated with the Registry. The description identifies the service, its supported API families from the Digital Registries API Families concept scheme, its endpoint, and a link to its machine-readable operational contract. HTTP operations use OpenAPI, or a protocol-native machine-readable description where the selected binding defines one. The description is part of the Registry metadata document, and the origin hosting an HTTP service locates that document and each contract through `/.well-known/api-catalog` as defined under [discovery publication](#discovery-publication). Declarations reflect the families and endpoints available for that Registry to the metadata's intended audience and are kept current when those services change.

**Purpose:** An API Consumer can discover relevant Registry services and follow their contracts to determine the supported operations and invocation details.

**Prerequisite:** The Registry publishes at least one service under the capability model and makes the metadata and contract access conditions available to intended consumers.

**Verification:** Request `/.well-known/api-catalog` at each HTTP service origin, check the `application/linkset+json` response, and follow its `service-meta` link to the metadata document as an intended consumer. For every service exposed to that audience, verify its Registry association, service identifier, valid family classifications, endpoint, and resolvable machine-readable contract, and check that the linkset carries a `service-desc` link to that contract. Check that the contract describes the advertised endpoint and contains operations belonging to each declared family. Check declarations against the implementation's published service inventory, including different Registry contexts when an endpoint is shared. A missing required service description or contract fails this check; unrelated internal services are outside its scope.

### #8 Declare the Registry context of each operation (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-core#req-8`

`KF: Registry Core`

Every Consultation operation in a published OpenAPI contract declares its Registry Identifier, collection, capability, and view with the `x-govstack-digital-registries` extension, valid against the [extension schema](../../api/extensions/x-govstack-digital-registries.schema.json). The Registry Identifier equals the identifier of a Registry described in the published Registry metadata, and the collection equals the collection segment of the operation path. Operations of one collection that declare the same view use the same Record schema.

**Purpose:** A consumer or validator can determine from the contract alone which Registry and authority a Record read belongs to and which representation it returns.

**Prerequisite:** At least one Consultation capability is selected, and the Registry metadata and OpenAPI contract are published.

**Verification:** Validate the extension of every Consultation operation against the schema. Check that its Registry Identifier resolves to a Registry in the published metadata and that its collection matches the path. Compare the response schemas of operations that share a collection and view and confirm they are identical.

## Consultation requirements

### #1 Retrieve the current Record by identifier (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-1`

`KF: Consultation`

Given a valid Record Identifier for a Record in the selected collection and a permitted request, Retrieve returns the current representation of that Record. An unknown identifier or a Record outside that collection receives the binding's unavailable-Record outcome, subject to protected-existence handling.

**Prerequisite:** Retrieve is selected and the collection declares its Registry context and view.

**Verification:** Retrieve a known source fixture and check its identity, schema, currency documentation, and declared metadata. Confirm that the source Record is unchanged; exercise an unknown identifier and, where applicable, an identifier belonging to another collection.

### #2 Apply disclosure rules to the returned representation (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-2`

`KF: Consultation`

For every selected read, the service returns a representation valid against the declared view schema and containing only the Records, fields, metadata, and result information permitted for the consumer and request context. Disclosure applies to references, embedded data, counts, errors, and continuation information. Withholding applies to optional fields of the declared view; it does not substitute another schema.

**Prerequisite:** The access policy for the declared view is documented.

**Verification:** Exercise each selected read with fixtures for the service's applicable access policies. Check representation validity and permitted information, including different entitlements where offered.

### #3 Hide protected Record existence (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-3`

`KF: Consultation`

When policy protects Record existence, Retrieve and Lookup return the same unresolved outcome for unknown and protected Records. Equivalence covers protocol status, security-relevant metadata, error type, response structure, and non-Record-specific values. Trace and correlation values are generated independently of Record existence; the outcome contains no Record-specific data. A Lookup failure caused by a source uniqueness violation on a protected key is indistinguishable from the unresolved outcome.

**Prerequisite:** The access policy declares which Records or keys have protected existence.

**Verification:** Compare protected and unknown fixtures under the same consumer context for each selected operation, including a uniqueness violation on a protected key where Lookup is selected. Check equivalent outcomes and independent trace values.

### #4 Resolve a Record by a declared exact selector (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-4`

`KF: Consultation`

Lookup accepts a published selector and all required key components. The key can be composite. Its declared comparison and normalization rules resolve at most one Record within the uniqueness scope. A permitted unique match in the selected collection returns that Record; zero matches in the collection produce the unresolved outcome. A source uniqueness violation produces a failure governed by disclosure policy.

Invalid, incomplete, or unsupported inputs are rejected. A **context-derived Lookup** derives some or all key components from verified consumer context, such as the authenticated subject, when its selector contract defines that mode; a fully context-derived selector accepts an empty caller-supplied `values` object.

**Prerequisite:** Lookup is selected and each selector declares its key components, comparison rules, uniqueness scope, and any context-derived components.

**Verification:** Exercise known, unknown, incomplete, incorrectly typed, and unsupported inputs, plus a source uniqueness violation. Verify comparison rules, composite keys where supported, context-derived components where declared, and protected-existence handling.

### #5 List a bounded Record collection (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-5`

`KF: Consultation`

List returns a bounded Page of permitted Records from its declared collection, applying its supported equality filters and ordering. Filters address declared non-personal fields only. Zero and single-result collections retain the Page shape. Unsupported filters or sorting produce a validation error.

**Prerequisite:** List is selected and the collection declares its order, tie-breaker, filters, and sorting.

**Verification:** Use fixtures with zero, one, and multiple results, including tied sort values where applicable. Check membership, schemas, order, size bounds, and rejection of unsupported inputs.

### #6 Search using declared criteria (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-6`

`KF: Consultation`

Search accepts a published search name and its typed criteria. It applies the declared matching rules to the selected collection and returns a bounded Page of permitted matching Records, retaining the Page shape for zero or one result. Unsupported searches, unknown criteria, and invalid inputs produce a validation error.

**Prerequisite:** Search is selected and each search declares its criteria schema and matching rules.

**Verification:** Execute declared searches with valid and invalid inputs. Check matching results, empty Pages, applicable disclosure contexts, and use of the binding's protected request locations for personal criteria.

<a id="pagination-contract"></a>

### #7 Continue bounded result pages (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-7`

`KF: Consultation`

List and Search use a declared deterministic order with a unique tie-breaker. Each request performs bounded source work, returns a bounded Page, and applies current authorization. Continuation preserves the collection, query, and view and advances traversal to explicit completion. Invalid continuation produces an error.

A completed traversal over unchanged data and access conditions contains each permitted matching Record once.

Pagination observes live data: source changes can move, add, or remove Records and cause repeated results. A profile can define stronger snapshot guarantees. Disclosure policy governs counts, page sizes, and continuation patterns, including short or empty advancing Pages.

Consumers treat cursors as opaque and return them unchanged with the original query inputs. They follow the completion signal, including when an intermediate Page is empty. The [HTTP binding](#http-binding) defines the continuation fields and fixed page-size policy.

**Prerequisite:** List or Search is selected and the collection declares its cursor expiry and page-size bounds.

**Verification:** Traverse unchanged multi-page fixtures to completion, checking complete membership without duplicates, identity, order, size bounds, progress, and termination. Exercise malformed, expired, and mismatched cursors, source changes, and applicable access changes. Check permitted page patterns and any total against the full permitted query.


## Revised requirement blocks

The blocks in this section preserve later old-layout requirement text that followed the committed baseline. They revise Registry Core #8 and Consultation #1, #2, #3, #6, and #7, and add Consultation #8 through #18. The baseline blocks above remain unchanged. Each heading names its family so that the revised blocks stay distinct from the baseline blocks with the same number. Links inside these blocks keep their source-relative form. These blocks are equally nonnormative.

## Revised Registry Core functional requirements

### Registry Core #8 Declare the Registry context of each operation (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-core#req-8`

`KF: Registry Core`

Every Collection-scoped Consultation operation in a published OpenAPI contract declares its Registry Identifier, Collection, capability, and view with the `x-govstack-digital-registries` extension, valid against the [extension schema](../../api/extensions/x-govstack-digital-registries.schema.json). The Registry Identifier equals the identifier of a Registry described in the published Registry metadata, and the Collection equals `{collectionId}` in the operation path or its fixed concrete value. Operations of one Collection that declare the same view use the same Record schema; a history operation can declare its separate history view. The optional `features` array lists only the read features implemented by that operation, with their capability applicability and dependencies. An operation selecting `purpose-bound` includes a valid `purpose` declaration with its trusted binding. Caller capability discovery follows its separate cross-Collection schema and references the declared operations.

**Purpose:** A consumer or validator can determine from the contract alone which Registry, logical Collection, and authority a Record read belongs to, which representation it returns, and which optional guarantees it supports.

**Prerequisite:** At least one Consultation capability is selected, and the Registry metadata and OpenAPI contract are published.

**Verification:** Validate the extension of every Collection-scoped Consultation operation against the schema. Check that its Registry Identifier resolves to a Registry in the published metadata and that its Collection matches the path. Compare the response schemas of operations that share a Collection and view and confirm they are identical. Check each selected feature against its operation inputs, responses, and declared guarantees; validate any required purpose object and trusted binding. Omission establishes no optional feature claim. Validate caller capability discovery under its own requirement and schema.

## Revised Consultation requirements

### Consultation #1 Retrieve a Record by identifier (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-1`

`KF: Consultation`

Given a valid Record Identifier for a Record in the selected Collection and a permitted request, Retrieve returns the latest representation available under the declared currency contract by default. When the operation declares a temporal feature and the request supplies its selector, Retrieve returns the source-backed representation selected by that temporal context and echoes the applied context. Temporal override is always explicit; omission selects the latest representation. An unknown identifier, a Record outside that Collection, or unavailable protected history receives the binding's unavailable-Record outcome, subject to protected-existence handling.

**Prerequisite:** Retrieve is selected and the collection declares its Registry context and view.

**Verification:** Retrieve a known source fixture without a temporal selector and check its latest identity, schema, currency documentation, and declared metadata. Where temporal features are selected, repeat with explicit supported selectors and compare the echoed context and representation with source history. Confirm that the source Record is unchanged; exercise an unknown identifier and, where applicable, an identifier belonging to another Collection.

### Consultation #2 Apply disclosure rules to the returned representation (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-2`

`KF: Consultation`

For every selected read, the service returns a representation valid against the declared view schema and containing only the Records, fields, metadata, and result information permitted for the consumer and request context. Disclosure applies to references, embedded data, counts, errors, and continuation information. Withholding and optional consumer field selection operate within the declared view schema; neither substitutes another schema nor grants additional disclosure rights.

**Prerequisite:** The access policy for the declared view is documented.

**Verification:** Exercise each selected read with fixtures for the service's applicable access policies. Check representation validity and permitted information, including different entitlements where offered.

### Consultation #3 Hide protected Record existence (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-3`

`KF: Consultation`

When policy protects Record or revision existence, Retrieve, Lookup, Revision List, and Revision Retrieve return the same unresolved outcome for unknown and protected resources. Revision List does not reveal whether its parent Record exists. Revision Retrieve does not reveal whether the parent Record or the named revision is the unavailable resource. Equivalence covers protocol status, security-relevant metadata, error type, response structure, and non-Record-specific values. Trace and correlation values are generated independently of existence; the outcome contains no Record-specific or revision-specific data. A Lookup failure caused by a source uniqueness violation on a protected key is indistinguishable from the unresolved outcome.

The service evaluates protected-existence policy before returning `409 history-not-available`. That diagnostic applies only after the caller is permitted to know the parent Record and requested history context, and only when the source cannot return source-backed retained history. It never distinguishes an unknown resource from a protected one.

**Prerequisite:** The access policy declares which Records, selector keys, and retained revisions have protected existence for every selected applicable operation.

**Verification:** Compare protected and unknown fixtures under the same consumer context for each selected operation, including a uniqueness violation on a protected key where Lookup is selected. For revision operations, separately vary parent Record and Revision Identifier presence and protection. Check equivalent outcomes and independent trace values, then make source history unavailable for a caller permitted to know the parent and verify `409 history-not-available` only in that post-protection case.

### Consultation #6 Search using declared criteria (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-6`

`KF: Consultation`

Search accepts a published search name and its typed criteria. It applies the independently selected reusable comparison semantics and any domain-specific rules declared by that search to the selected Collection, then returns a bounded Page of permitted matching Records, retaining the Page shape for zero or one result. A successful query with zero permitted matches returns `200` with an empty `items` array, including when source matches exist but disclosure policy filters all of them. A search contract can support equality, range, set-membership, prefix, or another named typed semantic without implementing the others. Unsupported searches, operators, criteria, and invalid inputs produce a validation error.

**Prerequisite:** Search is selected and each search declares its criteria schema, applicable reusable semantics, combination rules, and any domain-specific matching rules.

**Verification:** Execute declared searches with valid and invalid inputs. Check matching results, a true zero-result Page, and a `200` empty Page whose source matches are all protected or withheld. For temporal Search, distinguish a successful empty Page from `409 temporal-state-not-available` when the source cannot evaluate the requested historical query. Check applicable disclosure contexts and use of the binding's protected request locations for personal criteria.

### Consultation #7 Continue bounded result pages (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-7`

`KF: Consultation`

List, Search, and Revision List use a declared deterministic default order with a unique tie-breaker. Each request returns a bounded Page and applies current authorization. Continuation preserves the Collection, operation, query, view, effective field selection where supported, and parent `recordId` for Revision List, and advances traversal to an explicit completion signal. Invalid continuation produces `400 invalid-cursor`. The contract declares resource limits, timeout behavior, and any limits on the traversable result set.

Baseline pagination supports browsing under the declared source consistency and limit policy. It does not establish a complete export or a snapshot. An operation selecting `complete-traversal` additionally guarantees each permitted matching Record once when source data and access conditions remain unchanged.

Live pagination can observe source changes that move, add, or remove Records and cause omissions or repeats. An operation selecting `snapshot-traversal` fixes source membership, order, and represented data at one declared evaluation point. Disclosure policy governs counts, page sizes, and continuation patterns, including short or empty advancing Pages. Response bounds and timeout controls do not require a particular database pagination technique or a page-size-proportional bound on source work.

Consumers treat cursors as opaque and return them unchanged with the original query inputs. They follow the completion signal, including when an intermediate Page is empty. The [HTTP binding](#http-binding) defines the continuation fields and fixed page-size policy.

**Prerequisite:** List, Search, or Revision List is selected and the contract declares cursor expiry, page-size bounds, resource limits, deterministic order, unique tie-breaker, and traversal consistency. Revision List also declares its parent Record binding.

**Verification:** Traverse multi-page fixtures and check identity, declared order, size bounds, progress, termination, and the published consistency and limit policy. Exercise malformed, expired, and mismatched cursors, source changes, applicable access changes, and the declared timeout outcome. For Revision List, obtain a cursor under parent Record A and replay it under parent Record B; verify `400 invalid-cursor` without returning either Record's history. Check permitted page patterns and any total against the full permitted query. Exhaustive membership and snapshot checks apply only to the corresponding selected features.

### Consultation #8 Support declared conditional reads (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-8`

`KF: Consultation`

An operation selecting `conditional-read` returns a representation ETag on successful Retrieve responses and accepts `If-None-Match`. It evaluates current authorization before returning a bodyless `304` with the matching ETag. The validator identifies the permitted representation, including effective field selection where supported; it is not a source revision identifier. An operation without this feature need not support conditional GET.

**Prerequisite:** Retrieve selects `conditional-read` and declares `If-None-Match`, `200` and `304` responses, and their ETag headers.

**Verification:** Retrieve a permitted representation, repeat with its validator, and check the bodyless `304`. Change the represented data or selected fields and check validator behavior. Revoke access before a conditional request and verify that authorization is applied before any `304` response.

### Consultation #9 Select declared response fields (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-9`

`KF: Consultation`

An operation selecting `field-selection` accepts a non-empty, duplicate-free list of declared top-level `data` field names. It returns only the selected fields that disclosure policy permits, together with any mandatory `data` fields documented by the view. `recordId` and the `data` object remain present even when no selected field can be disclosed. Selectable fields are optional in the view schema so default and selected responses validate against the same schema. Omission of the input uses the declared default field set. Unknown selections and invalid inputs are rejected. Pagination preserves the effective field set.

**Prerequisite:** The operation selects `field-selection` and publishes its allowed field names, default field set, mandatory fields if any, selection bounds, and omission semantics.

**Verification:** Select one and several supported fields, check schema validity and retained identity, and compare default and selected responses under applicable disclosure policies. Reject empty, duplicate, unknown, and incorrectly typed selections. Check field-selection mismatch on continuation where pagination is selected.

### Consultation #10 Provide complete traversal (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-10`

`KF: Consultation`

An operation selecting `complete-traversal` returns each permitted matching Record once when the declared traversal is followed to completion over unchanged source data and access conditions. It does not silently omit results because of an internal result window or limit. A limit that prevents complete traversal produces a declared failure rather than a completion signal. This feature does not imply a source snapshot or a bound on database work.

**Prerequisite:** List or Search selects `complete-traversal` and publishes its traversal availability and failure conditions.

**Verification:** Traverse unchanged multi-page fixtures, including tied sort values and filtered-out source candidates, and compare the complete set with the permitted query. Check for missing or repeated Records and exercise limits that prevent completion.

### Consultation #11 Preserve a traversal snapshot (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-11`

`KF: Consultation`

An operation selecting `snapshot-traversal` also selects `complete-traversal`. The first request fixes source membership, ordering, and represented data at one declared snapshot evaluation point. Every continuation uses that snapshot while applying current authorization and disclosure policy. The contract defines how the snapshot evaluation point is identified, its availability and expiry, and its failure outcome. An unavailable or expired snapshot produces `400 invalid-cursor`; the service never silently switches to live data or another snapshot.

**Prerequisite:** List or Search selects both traversal features and declares the snapshot semantics and availability policy.

**Verification:** Establish a snapshot, then insert, change, and remove source fixtures between Pages. Check unchanged snapshot membership, ordering, and source values under unchanged access conditions. Exercise expiry and lost snapshot state, and revoke access between Pages to verify current authorization.

### Consultation #12 List retained Record revisions (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-12`

`KF: Consultation`

Revision List returns a bounded `RevisionPage` for one Record in one Collection. Each item is a `RecordRevision` containing a stable `recordId` equal to the parent path identifier, the declared history view, and a required `revision.revisionId`; `revision.recordedAt` is included only when supported by the source. The contract declares revision order, tie-breaker, retention, known and unknown gap semantics, schema-version interpretation, and unavailable-history outcomes. A history view can normalize older source schemas into its declared schema while preserving source values and meanings. When a retained revision cannot be mapped faithfully, the operation returns its declared explicit failure instead of returning an arbitrary raw schema or fabricating values. A result never presents omitted or unavailable history as complete.

**Prerequisite:** Revision List is selected, the source retains distinguishable revisions, and the operation declares a history view and pagination contract.

**Verification:** List retained revisions for fixtures with several revisions, a single revision, a documented gap, and history outside the retention boundary. Check stable Record identity, source-backed revision identity and time, declared order, schema interpretation, current authorization on every Page, and protected unavailable outcomes.

### Consultation #13 Retrieve one retained Record revision (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-13`

`KF: Consultation`

Revision Retrieve resolves a declared Revision Identifier for one Record in one Collection and returns that source-backed `RecordRevision` with `recordId` equal to the parent path identifier. Record and Revision Identifiers are opaque and are not reconstructed from timestamps. An unknown, expired, removed, outside-retention, protected, or otherwise unavailable revision produces the declared unavailable outcome. The service does not substitute the latest Record, a nearby revision, or a fabricated representation.

**Prerequisite:** Revision Retrieve is selected and its source can address retained revisions by stable identifiers.

**Verification:** Retrieve known retained revisions represented under applicable schema versions. Exercise unknown, removed, outside-retention, protected, and Record-mismatched revision identifiers and verify the declared unavailable outcome without fallback or existence disclosure.

### Consultation #14 Select by recorded time (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-14`

`KF: Consultation`

A Retrieve, Lookup, List, or Search operation selecting `recorded-time` accepts `recordedAsOf`, a date-time cutoff for information accepted by the source. The returned representation is based only on source knowledge accepted no later than that cutoff, subject to the source's declared recording semantics, corrections, retention, and gaps. A `TemporalRecord` or `TemporalRecordPage`, including an empty Page, echoes the applied `recordedAsOf` context. Omitting this coordinate selects the latest available source knowledge while still applying any supplied `effectiveAt`; it makes no historical-knowledge claim. Revision operations instead identify history directly by Record and Revision Identifiers and do not accept this selector.

**Prerequisite:** The operation selects `recorded-time` and documents the source event that establishes acceptance, timestamp precision, timezone treatment, inclusivity, retention, and unavailable-history outcome.

**Verification:** Select cutoffs before, at, and after accepted source revisions, including a correction and any declared gap. Compare the result and echoed context with source evidence. Distinguish a proven absent item (`404 record-not-available`), a successful Search with zero permitted matches (`200` with empty `items` and echoed temporal context), and a source unable to evaluate the requested historical selection (`409 temporal-state-not-available`). Verify that request time, adapter ingestion time, event occurrence time, and registration date are not substituted unless the source contract explicitly defines one as its acceptance time.

### Consultation #15 Select by effective time (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-15`

`KF: Consultation`

A Retrieve, Lookup, List, or Search operation selecting `effective-time` accepts `effectiveAt`, a date or date-time at which the source declares information applicable. The contract defines whether it accepts dates, instants, or both, plus boundary, timezone, overlap, correction, and no-applicable-state semantics. A `TemporalRecord` or `TemporalRecordPage`, including an empty Page, echoes the applied `effectiveAt` context. Omitting this coordinate uses the operation's declared default applicability without overriding any supplied `recordedAsOf`; it makes no explicit effective-time claim. Revision operations instead identify history directly by Record and Revision Identifiers and do not accept this selector.

Event occurrence and registration dates are domain facts, not automatically effective-time coordinates. A source can define either as effective time for a particular field or history model, but the service does not infer that equivalence.

**Prerequisite:** The operation selects `effective-time` and the source has a declared applicability model supporting the accepted selector precision.

**Verification:** Exercise date and instant boundaries supported by the contract, overlapping or corrected applicability where possible, and a point with no applicable state. Distinguish a proven absent item (`404 record-not-available`), a successful Search with zero permitted matches (`200` with empty `items` and echoed temporal context), and a source unable to evaluate the requested historical selection (`409 temporal-state-not-available`). Compare the result and echoed context with source evidence and confirm that occurrence or registration dates are not silently substituted.

### Consultation #16 Publish reusable Search semantics (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-16`

`KF: Consultation`

Each named Search publishes a versioned typed criteria schema and independently declares the comparison semantics it supports. Reusable semantics are equality, range, set-membership, and prefix. Each selected semantic defines applicable fields and types, normalization and collation, inclusive or exclusive bounds where relevant, empty and null treatment, repeated-value treatment, and how criteria combine. A Search can publish additional domain-specific semantics, but support for one semantic does not imply support for another, fuzzy matching, full-text search, or a universal query language.

**Prerequisite:** Search is selected and the contract publishes at least one named typed Search.

**Verification:** For every declared Search and semantic, exercise matching and non-matching typed boundaries, invalid operators or fields, normalization, empty and null cases, and criterion combination. Verify that undeclared semantics are rejected and that the implementation does not advertise a broader query language than it supports.

### Consultation #17 Discover caller-available Consultation operations (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-17`

`KF: Consultation`

When caller capability discovery is offered, `GET /v1/capabilities` returns one bounded `CallerCapabilities` document filtered for the authenticated caller and current trusted request context, including a verified purpose when one is present. It can omit operations whose required purpose is absent from that context; discovery itself does not select `purpose-bound` or create a new purpose input. The document contains at most 64 Collections, each with at most 16 operations. `collectionId` is unique within the document, and each `(contract, operationId)` pair is unique. Each Collection entry identifies its `collectionId` and `registry`. Each operation entry requires its `operationId`, capability annotation, view, and version-specific HTTPS `contract`; it can additionally publish bounded `readableFields`, selector and named Search identifiers, feature annotations, and purpose requirements. `readableFields` describes fields the caller can receive under current policy. It is distinct from `field-selection`, does not advertise a `fields` input, and need not be present even when readable fields exist.

Known discovery annotations agree with the linked operation's Collection, capability, view, selected features, and purpose declaration. Capability and feature annotations in `CallerCapabilities` are extensible for forward-compatible advisory discovery: a client skips an operation entry whose capability annotation it does not understand and ignores unknown feature annotations on an otherwise understood entry. The normative `x-govstack-digital-registries` extension in the linked versioned operation remains closed to the capability and feature values defined by that contract version. Unknown discovery metadata never grants authority, adds an operation, or widens fields. The identifiers point into the contract; the response does not reproduce their complete schemas. Contradictory duplicates or known metadata produce the declared explicit validation failure; the service does not silently merge them. The response uses `Cache-Control: no-store`. If the caller-available description exceeds a declared array or document bound, the service returns its declared explicit error instead of truncating entries, silently omitting authorized capabilities, or substituting an empty array. `collections: []` is reserved for the valid case where no operation is visible to that caller.

The document is advisory. It does not grant authority, replace authorization at invocation time, promise access to any particular Record, require disclosure of every readable field, or define a reusable profile model. An omitted operation or field establishes only that it is not disclosed as available in that response.

**Prerequisite:** The service offers caller capability discovery and publishes its bounded response schema and authentication requirements.

**Verification:** Request discovery under callers and trusted contexts with different permissions. Validate bounds, unique Collection identifiers and `(contract, operationId)` pairs, contract agreement, `readableFields`, selectors, searches, known features, purpose requirements, and `no-store`; confirm that `readableFields` does not imply `field-selection`. Submit an unknown capability annotation and verify that the entry is skipped; submit an unknown advisory feature and verify that it is ignored without granting authority. Confirm that the linked operation extension still rejects unknown capability and feature values. Submit contradictory duplicates and contradictory known metadata and exceed every declared bound, verifying explicit failures without merge, truncation, or silent omission. Then verify that every discovered operation still performs current authorization and that no record-level permission can be inferred.

### Consultation #18 Enforce declared purpose binding (DRAFT EXTENSIBLE OBSERVABLE)

`govstack-bb-digital-registries-fr-consultation#req-18`

`KF: Consultation`

A Record or history operation selecting `purpose-bound` declares a `purpose` object with `required: true`, a non-empty unique `allowedPurposes` list of controlled bounded non-whitespace codes or absolute URIs, and one trusted `binding`. `access-token-claim` also requires the `claim` name. `trusted-authorization-context` obtains the value from the deployment's authentication and authorization boundary. Purpose is not accepted from a query parameter or request body. A missing, untrusted, malformed, or unallowed purpose is rejected before Record information is disclosed.

The effective purpose is bound to cursors, conditional validators, current and historical reads, temporal selection, and the service's audit evidence. A continuation or validator cannot be replayed under another purpose. The contract documents how multiple values and purpose changes are handled.

Declared purpose is distinct from consent, legal or institutional authority, and actual downstream use. One does not prove the others. This feature supplements the inherited authentication and authorization contract; operations that do not select it retain their inherited security requirements and do not acquire a universal purpose parameter.

**Prerequisite:** The operation selects `purpose-bound`, the deployment has a trusted purpose binding, and its controlled allowed values and audit treatment are documented.

**Verification:** Exercise missing, malformed, untrusted, allowed, and disallowed purpose contexts; reuse a cursor and conditional validator under another purpose; and compare current, historical, and temporal behavior. Check rejection before disclosure and verify the recorded effective purpose without treating it as evidence of consent, authority, or downstream use.
