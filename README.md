# Digital Registries Building Block Specification

This is a format-only authoring migration of **official `main` at `8588a219df9a8406e66c4392d0bef664b34e4e30`**, labelled **3.0-alpha; June 2026**. The version history also uses `3.0.0-alpha`, retained in the authoring metadata. This migration publishes no release and imports no later draft or uncommitted Registry changes.

Start with the [overview](introduction/overview.md), [scope](introduction/scope.md), and [conformance explanation](resources/conformance.md). The structured requirements preserve all 37 DRS entries, the two elevated cross-functional requirements, and the additional required behaviour stated in the other upstream chapters. The [narrative inventory](resources/upstream-narrative-inventory.md) records the two chapter 4 items that are not carried as separate required statements.

[Migration record](resources/format-migration.md) explains the source boundary, optionality mapping and draft identifiers. [Source findings](resources/source-findings.md) records unresolved upstream clauses and contract bindings. [API source notes](resources/contract-source-notes.md) explains the generated [authoring entrypoint](resources/api.yml) and the exact original templates it projects. [Verification procedures](resources/testing.md) distinguishes executable preservation checks from manual implementation assessment.

The original `spec/`, `api/`, `examples/` and `test/` trees remain byte-for-byte unchanged as source and implementation artifacts. Original publication navigation is retained there as historical source, not as the active requirement catalogue. The original repository README and GitBook configuration are preserved under `resources/history/`.

The [official source snapshot](https://github.com/GovStackWorkingGroup/bb-digital-registries/tree/8588a219df9a8406e66c4392d0bef664b34e4e30) is the sole content baseline. The shared renderer is separate tooling and does not change that baseline or establish implementation conformance.
