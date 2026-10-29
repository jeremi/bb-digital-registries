---
title: Format-only Migration from Official Main
---

# Format-only Migration from Official Main

The sole content baseline is official `GovStackWorkingGroup/bb-digital-registries` `main` at `8588a219df9a8406e66c4392d0bef664b34e4e30`. Its landing page says **3.0-alpha; June 2026**, and its version history also uses **3.0.0-alpha**. No later draft commits or uncommitted content are imported.

The target uses the agreed [functionalities and extensions model](https://github.com/GovStackWorkingGroup/specification-framework/pull/1), [requirements, options and interaction model](https://github.com/GovStackWorkingGroup/specification-framework/pull/2), and corresponding [BB template](https://github.com/GovStackWorkingGroup/bb-template/pull/21), together with the introductory structure from [template PR 19](https://github.com/GovStackWorkingGroup/bb-template/pull/19). The pinned framework revisions are `d7728fa1c30dd4919afbc63f603580a7ddf0920e` and `7322f977a6a74127240cbab5ed9d5ad84b9d5c29`.

## Preservation boundary

The original `spec/`, `api/`, `examples/`, `test/`, CI configuration, licence, and other original files remain unchanged. Only the repository entrypoint, publication navigation configuration and local tool ignore entries change at original paths. The original README and GitBook configuration are archived exactly under `resources/history/`. `tools/validate_migration.py` compares every protected original byte directly with the pinned Git object, so using a different local draft as the content source cannot silently replace the upstream snapshot.

Active authoring is at root: `metadata.yml`, `authors.yml`, `toc.yml`, `introduction/`, `requirements/`, `resources/`, and `assets/`. The original `spec/` is a frozen source archive. Assets are also copied without byte changes to their authoring location; this is intentional preservation during migration.

The [narrative inventory](upstream-narrative-inventory.md) accounts for every original Markdown page. The [machine-readable ledger](requirement-migration.yml) maps every DRS identifier and the additional normative source clauses to exact active statements. Original DRS IDs remain source lookup keys, not invented permanent framework requirement IDs.

## Requirement transformation

Compound DRS blocks are split into independently verifiable statements with one system-under-test subject and interaction type. Their field lists, conditions, constraints, examples and applicability are retained. The two chapter-5 CFR elevations retain their REQUIRED level and original mutability. Required behaviour from chapters 4, 7, 8 and 9 is carried into structured requirements rather than silently becoming informative body text. Two chapter 4 items are not carried as separate required statements, and the [narrative inventory](upstream-narrative-inventory.md#narrative-behaviour-not-bound-by-drs-1-through-drs-37) records why: integration through the Information Mediator (item 13), whose mediation is outside the system under test, and dashboards (item 16), which keep the RECOMMENDED level of the DRS-26 custom-dashboard option. Network access, power and actor setup from workflows remain verification prerequisites, not a requirement to implement external infrastructure.

The optionality policy is explained in [Conformance](conformance.md): four independent optional functionalities become extensions; optional variants remain nonblocking RECOMMENDED requirements with their source qualification. Source overlaps and ambiguities remain explicit. No conflict is resolved by silently deleting an obligation or changing an access rule.

All framework IDs remain empty and lifecycle remains DRAFT. This migration does not approve requirements, create conformance claims, register people or publish a release. Current-major author names and roles are retained in `authors.yml`; [Conformance](conformance.md) explains that the affiliation and first-version credits, which the file cannot carry, remain in the frozen `spec/README.md`. Unverified person URNs remain unassigned.

## API and validation boundary

[API source notes](contract-source-notes.md) explains the exact embedded templates chosen for the generated authoring projection and its four metadata-only Database operation aliases. It also identifies divergent alternatives and preserves their existing validation failures. No endpoint, request schema, response schema or permission is repaired or redesigned.

A requirement whose source has no common operation or complete contract retains an explicit [source gap](source-findings.md). The local migration validator requires an exact explained ledger entry for it, and rejects fabricated operation identifiers. Such a preserved draft gap is not strict compiler completeness. The inspected central compiler is not executed here; official compiler compatibility remains unverified.

Run the executable repository checks and consult the [manual procedures](testing.md). Static preservation, schema and navigation evidence do not establish deployed behaviour. The original runtime test suite is retained, and no deployment has been supplied for executing it in this migration.
