---
title: Access Control
description: |
  Registry operators govern who can administer registries and access registry data.
realises: [governed-access]
conformance: CORE
requirements:
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry enforces authorisation for creating and managing registry databases.
    documentation: |
      Evidence: access-control policy and an audit record showing an allowed and a denied administrative action.
      Source: DRS-6, item 1.
    test: resources/testing.md#drs-6
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry enforces authorisation for API use at service, record and data-field scope.
    documentation: |
      Evidence: access-control policy and audit records showing decisions at each of the three scopes.
      Source: DRS-6, item 2.
    test: resources/testing.md#drs-6
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry enforces authorisation for access to registry data.
    documentation: |
      Evidence: access-control policy and audit records showing an allowed and a denied data-access decision.
      Source: DRS-6, item 3.
    test: resources/testing.md#drs-6
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: SERVICE_API
    contract: resources/api.yml
    api_operation_id: null
    statement: The Digital Registry provides an API through which an authorised operator manages user rights for a registry database and its data.
    documentation: |
      Binding gap: the source API descriptions contain no operation for managing user rights.
      Source: DRS-6, analyst rights-management paragraph.
    test: resources/testing.md#drs-6
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry provides a user interface through which an authorised operator manages user rights for a registry database and its data.
    documentation: |
      Source: DRS-6, analyst rights-management paragraph.
    test: resources/testing.md#drs-6
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry evaluates role-based access-control rules.
    documentation: |
      Evidence: policy configuration and audit records for role-based decisions.
      Source: DRS-6, RBAC bullet.
    test: resources/testing.md#drs-6
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry evaluates attribute-based access-control rules.
    documentation: |
      Evidence: policy configuration and audit records for attribute-based decisions.
      Constraint: spec/6-functional-requirements.md:120 says ABAC logic 'could be used' for APIs, schemas, data fields, record filters and users; the scope list is source guidance, not a REQUIRED constraint.
      Source: DRS-6, ABAC bullets.
    test: resources/testing.md#drs-6
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry evaluates policy-based access-control rules.
    documentation: |
      Evidence: policy configuration and audit records for policy-based decisions.
      Source: DRS-6, PBAC bullet.
    test: resources/testing.md#drs-6
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry evaluates consent-based access-control rules.
    documentation: |
      Evidence: consent policy and audit records for an access decision governed by consent.
      Source: DRS-6, consent-based access bullet.
    test: resources/testing.md#drs-6
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry evaluates delegated-access rules for guardians, parents and representatives.
    documentation: |
      Evidence: delegated-access policy and audit records for each source role.
      Source: DRS-6, delegated access bullet.
    test: resources/testing.md#drs-6
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator configure cross-registry access templates.
    documentation: |
      Source: DRS-6, cross-registry access templates bullet.
    test: resources/testing.md#drs-6
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry applies data-minimisation rules that return only the fields required by an authorised request.
    documentation: |
      Evidence: minimisation policy and request-and-response records showing omitted non-required fields.
      Source: DRS-6, data minimization rules bullet.
    test: resources/testing.md#drs-6
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: AUDITABLE
    mutability: EXTENSIBLE
    interaction: INTERNAL
    statement: The Digital Registry applies dynamic field restrictions whose conditions are evaluated against record values.
    documentation: |
      Evidence: a configured condition and request-and-response records showing that the field is returned only when the condition holds.
      The source example is `CaseStatus=APPROVED`.
      Source: DRS-6, condition-based dynamic restrictions bullet.
    test: resources/testing.md#drs-6
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry provides an `Any logged-in user` role.
    documentation: |
      Source: DRS-6, logged-in-user role bullet.
    test: resources/testing.md#drs-6
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry provides an `Anonymous` user role.
    documentation: |
      Source: DRS-6, anonymous role bullet.
    test: resources/testing.md#drs-6
  - id: null
    status: DRAFT
    level: REQUIRED
    observability: OBSERVABLE
    mutability: EXTENSIBLE
    interaction: USER_INTERFACE
    statement: The Digital Registry lets an authorised operator assign rights to an individual user and to a group of users.
    documentation: |
      Constraint: a group is a set of users in a role, and a role is a set of rights.
      Source: DRS-6, per-user and per-group bullets.
    test: resources/testing.md#drs-6
---

# Access Control

This functionality carries the complete access-control surface stated in DRS-6. It does not prescribe an identity provider or a policy language. The source uses both RBAC and ABAC as named controls and separately introduces PBAC, consent, delegation, cross-registry templates and conditional field restrictions; each remains independently assessable here.
