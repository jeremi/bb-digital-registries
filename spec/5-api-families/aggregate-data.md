---
description: Approved statistics derived from Registry Records.
---

# Aggregate Data

> **Status:** Informative and not claimable in this release. No Aggregate Data requirements, statistical model, contract, or tests are published.

## Purpose and applicability

Aggregate Data provides approved statistics derived from Registry Records, such as counts, distributions, or time series. It applies when the Registry itself publishes statistical outputs. In other deployments, a national statistics service or open-data platform can own that responsibility instead.

## Candidate capability areas

| Area | Outcome |
|---|---|
| Aggregate query | Returns an approved result for declared dimensions, measures, population, and time scope. |
| Dataset metadata | Describes definitions, units, provenance, release policy, and applicable disclosure controls. |
| Published release | Returns an identified statistical release or revision. |

## Capability boundary

Aggregate Data is not Record-level [Consultation](consultation.md), a mandatory analytics engine, or a dashboard. It is not automatically public. Aggregation is not itself anonymisation, and a complete profile needs to address disclosure thresholds, suppression, legal controls, revisions, and indicators of applied protection.

## Candidate bindings

Synchronous HTTP described by OpenAPI is a candidate general binding. SDMX is a candidate semantic and interchange standard where outputs need to participate in national or international statistical ecosystems. This release selects neither binding.

## Example

A vehicle Registry publishes quarterly counts by vehicle class and region under a statistical release policy that suppresses disclosive small cells.
