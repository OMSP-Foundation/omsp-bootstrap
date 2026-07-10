# Digital Twin Validation Demonstrator Checklist

- Artifact ID: `OMSP-REFERENCE-TWIN-DEMO-VALIDATION-0001`
- Version: `0.1.0`
- Status: `review`

## Artifact integrity

- [ ] Demonstrator narrative is present.
- [ ] Replay manifest parses as JSON.
- [ ] Traceability matrix is present.
- [ ] Known limitations are present.
- [ ] Artifact IDs and versions are explicit.

## Reference resolution

- [ ] Hanse 460 reference configuration resolves.
- [ ] Vessel design identifier resolves.
- [ ] Navigation and monitoring system identifiers resolve.
- [ ] Equipment/interface model is referenced without installed-equipment claims.
- [ ] Navigation-data degradation scenario resolves.
- [ ] State and observation model semantics are applied.

## Observation integrity

- [ ] Every observation has a stable identity.
- [ ] Event, receipt and processing times are visible.
- [ ] Source identity and source class are visible.
- [ ] Authority and quality metadata are visible.
- [ ] Observations remain distinct from configuration facts.
- [ ] Original evidence is not overwritten.

## Data-quality behavior

- [ ] Fresh valid data may contribute to current state.
- [ ] Stale data is excluded or explicitly marked stale.
- [ ] Missing values include reason codes.
- [ ] Missing values are not replaced with fabricated defaults.
- [ ] Conflicting observations remain preserved together.
- [ ] Human reports remain distinguishable from machine observations.

## Current-state projection

- [ ] Projection policy has a stable identifier and version.
- [ ] Projection time is explicit.
- [ ] Projection rules are declared.
- [ ] The expected current-state view can be reproduced from the manifest.
- [ ] Unresolved conflicts remain visible in the projected result.
- [ ] Indeterminate state is allowed when evidence is insufficient.

## Derived-value provenance

- [ ] Derived value has a stable identity.
- [ ] All input identities are listed.
- [ ] Method identity and version are listed.
- [ ] Assumptions are listed.
- [ ] Execution time is listed.
- [ ] Result quality and unresolved limitations are visible.
- [ ] Derived output is marked advisory rather than authoritative.

## Scenario and authority

- [ ] Scenario applicability is design-family reference only.
- [ ] Accountable human authority is explicit.
- [ ] Software performs only monitoring, recording, projection or advisory functions.
- [ ] No control action is emitted.
- [ ] No approved operational procedure is implied.

## Scope and claims

- [ ] No physical vessel is represented.
- [ ] No installed equipment is asserted.
- [ ] No live telemetry is represented.
- [ ] No runtime performance claim is made.
- [ ] No certification, seaworthiness or risk-acceptance claim is made.
- [ ] No autonomous navigation or vessel-control claim is made.

## Acceptance result

Record one result for every item:

- `pass`
- `fail`
- `indeterminate`
- `not-applicable`

The demonstrator is acceptable for merge only when all mandatory integrity, provenance, visibility, human-authority and safety-boundary items are `pass`. Any unresolved model-interoperability defect is a `fail`, not a documentation caveat.
