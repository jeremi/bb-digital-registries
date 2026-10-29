---
title: Source References
---

# Source References

This format migration uses the Digital Registries upstream `main` tree at commit [`8588a219df9a8406e66c4392d0bef664b34e4e30`](https://github.com/GovStackWorkingGroup/bb-digital-registries/tree/8588a219df9a8406e66c4392d0bef664b34e4e30) as its sole content source.
The original `spec/`, `api/`, `examples/`, and `test/` trees remain unchanged as a source archive.

The active narrative pages link to their original pages through the [upstream narrative inventory](upstream-narrative-inventory.md).
The chapter 8 API references preserve the exact embedded source-contract filenames and bytes:

- [`GovStack_Digital_registries_BB_Data_API_template-1.3.0.json`](../assets/GovStack_Digital_registries_BB_Data_API_template-1.3.0.json)
- [`GovStack_Digital_registries_BB_Database_API_template-1.3.0.yaml`](../assets/GovStack_Digital_registries_BB_Database_API_template-1.3.0.yaml)

The frozen root `api/` directory also contains files with these names.
The [upstream narrative inventory](upstream-narrative-inventory.md#source-ambiguities-and-unresolved-links) records the material difference between the embedded and root Database API YAML files.
The active [`api.yml`](api.yml) projection uses byte-identical embed copies stored at [`upstream-api/data-api.json`](upstream-api/data-api.json) and [`upstream-api/database-api.yaml`](upstream-api/database-api.yaml).

The active `assets/` directory is a byte-for-byte copy of the files under the frozen [`spec/.gitbook/assets/`](https://github.com/GovStackWorkingGroup/bb-digital-registries/tree/8588a219df9a8406e66c4392d0bef664b34e4e30/spec/.gitbook/assets) directory.

The target structure follows the GovStack Specification Framework proposal at commit [`7322f977a6a74127240cbab5ed9d5ad84b9d5c29`](https://github.com/GovStackWorkingGroup/specification-framework/commit/7322f977a6a74127240cbab5ed9d5ad84b9d5c29).
