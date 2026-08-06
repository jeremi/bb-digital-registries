---
description: Base Registry Profile interaction and outcomes.
---

# 10 Workflows

## 10.1 Retrieve the current permitted Record representation

This workflow describes externally observable behaviour. It does not prescribe internal services, databases, policy engines, gateways, or deployment topology.

### Actors

- **API Consumer:** requests a Record it is authorised to use.
- **Registry implementation:** resolves the current Record revision and returns the permitted representation.
- **Access decision service:** optional component used by the implementation to evaluate access and disclosure policy.

### Preconditions

1. The Registry publishes the identity metadata required by Registry Core.
2. The API Consumer has the credentials and request context required by the deployment.
3. The current Record representation identifies its schema, semantic model, revision, lifecycle state, and minimum provenance.
4. The implementation can determine the permitted representation for the API Consumer and request context.

### Interaction

1. The API Consumer requests the current representation using a Record Identifier.
2. The Registry authenticates the caller and evaluates access and disclosure policy.
3. If the policy permits access, the Registry resolves the current revision and lifecycle state.
4. The Registry constructs the permitted representation, including the Record context required by Registry Core.
5. The Registry returns the permitted representation or the applicable problem response.

### Outcomes

| Condition | Observable outcome |
|---|---|
| Current Record is accessible | Current permitted representation is returned. |
| Consumer has narrower disclosure rights | A valid filtered or redacted representation is returned. |
| Identifier is unknown | The implementation returns its unknown-identifier problem response. |
| Consumer may not learn whether a protected Record exists | The response is indistinguishable under the published contract from the unknown-identifier response, including security-relevant headers and non-Record-specific problem values. Independently generated correlation values may differ, and no Record-specific data is returned. |

### Postconditions

- The Record is not modified by the operation.
- The returned representation identifies the same Record Identifier requested by the consumer.
- A successful response identifies the Registry, current revision, lifecycle state, schema, semantic model, Registry Authority, and recording time.
