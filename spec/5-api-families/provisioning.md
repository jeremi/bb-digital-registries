---
description: Programmatic configuration and publication of a Registry service.
---

# Provisioning

> **Status:** Informative and not claimable in this release. No Provisioning requirements, contract, or tests are published.

## Purpose and applicability

Provisioning configures a Registry service and publishes its externally visible contracts. It is useful where schemas, capabilities, bindings, or controlled bulk data flows are administered programmatically.

Many authoritative registries do not need this family. Their authority and schema may be established by law, governance, or an operational process outside an API.

## Candidate capability areas

| Area | Outcome |
|---|---|
| Metadata administration | Creates or revises the Registry's machine-readable identity and capability declarations through an administrative interface. Registry Core separately requires publication of the current service metadata. |
| Schema lifecycle | Publishes, revises, or retires a representation schema under defined compatibility rules. |
| Interface publication | Declares supported families, sub-patterns, bindings, and access conditions. |
| Bulk transfer | Initiates a controlled import or export of data and metadata. |

These areas do not require dynamic database creation, a no-code builder, an administrative user interface, or a particular storage engine. Provisioning manages metadata programmatically; it does not make the Core publication requirement optional. It also does not perform the legal or governance act that establishes a Registry Authority.

## Data and policy considerations

A complete profile needs to address administrative authorisation, schema compatibility, publication lifecycle, bulk-operation validation, provenance, and failure recovery. Those decisions are not defined in this release.

## Candidate binding

Synchronous HTTP described by OpenAPI is a candidate for administrative operations. Long-running bulk work may require an asynchronous job or messaging pattern. No binding is selected in this release.

## Example

A programme administrator publishes a revised benefit-record schema and its compatibility metadata before applications begin sending Records that use the revision.
