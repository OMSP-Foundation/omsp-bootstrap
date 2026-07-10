---
Artifact-ID: OMSP-REFERENCE-TWIN-STATE-VALIDATION-0001
Title: Digital Twin State and Observation Validation Checklist
Version: 1.0.0
Status: Review
Owner: OMSP Engineering Council
Created: 2026-07-10
Last-Updated: 2026-07-10
Sprint: Sprint-4
Work-Package: WP-0043
Traceability:
  - ISSUE-77
  - OMSP-REFERENCE-TWIN-STATE-0001
---

# Digital Twin State and Observation Validation Checklist

## 1. Record Identity

- [ ] Every observation has a unique stable identifier.
- [ ] Every state assertion, derived value, conflict set and current-state view has a stable identifier.
- [ ] Every subject identifier resolves to a governed vessel, system, subsystem, equipment, interface or scenario entity.
- [ ] Display-name changes do not change stable identities.

## 2. Information-Class Separation

- [ ] Configuration facts, observations, state assertions and derived values are stored as distinct classes.
- [ ] No observation is labeled as verified configuration evidence.
- [ ] No state projection silently updates a design or as-built configuration record.
- [ ] Simulated, imported, observed and human-reported records remain distinguishable.

## 3. Time Semantics

- [ ] Event time and receipt time are recorded separately.
- [ ] Processing time is recorded for transformed or derived records.
- [ ] Timestamp timezone or offset is explicit.
- [ ] Timestamp precision and clock-quality limitations are visible where relevant.
- [ ] Late-arriving observations do not erase prior historical views.

## 4. Source and Provenance

- [ ] Every observation identifies its source.
- [ ] Source type and authority class are explicit.
- [ ] Acquisition channel is recorded where known.
- [ ] Transformations identify input records, methods and versions.
- [ ] Human-entered records identify an accountable actor where required.
- [ ] Corrections preserve the original record and use explicit links.

## 5. Data Quality

- [ ] Quality is represented by explicit dimensions or states.
- [ ] Unknown quality is not treated as good quality.
- [ ] Calibration status is visible when applicable.
- [ ] Plausibility and consistency assessments identify their method.
- [ ] Integrity, signature or checksum status is visible when available.
- [ ] Confidence does not replace provenance.

## 6. Missing Data

- [ ] Missing values are explicit rather than represented as zero or false.
- [ ] Every missing value has a reason code.
- [ ] `not-applicable` is distinguishable from `not-observed`.
- [ ] Redacted data is distinguishable from unavailable data.
- [ ] Missing safety-relevant properties are surfaced to consumers.

## 7. Stale Data

- [ ] Freshness is evaluated against a declared property-specific policy.
- [ ] The evaluation time is recorded.
- [ ] Stale values remain available historically.
- [ ] Stale values cannot silently populate a current-state view.
- [ ] Consumers receive an explicit stale warning.

## 8. Conflicting Data

- [ ] Competing observations are retained.
- [ ] Conflict sets identify all competing record IDs.
- [ ] Conflict-detection rules are documented.
- [ ] Selected records, when any, include rationale and authority.
- [ ] Unresolved conflicts remain visible in current-state views.
- [ ] Safety impact is recorded for safety-relevant conflicts.

## 9. State Assertions

- [ ] Every assertion identifies supporting observations.
- [ ] Assertion validity intervals are explicit.
- [ ] Human and machine-generated assertions are distinguishable.
- [ ] Assertion method and version are recorded.
- [ ] Supersession does not delete prior assertions.
- [ ] Confidence and quality state are explicit.

## 10. Current-State Views

- [ ] Every view has a declared scope and evaluation time.
- [ ] The selection policy and version are recorded.
- [ ] Included and excluded record IDs are traceable.
- [ ] Missing, stale and conflicting properties are listed.
- [ ] Derived inputs remain traceable.
- [ ] Human-review status is explicit.
- [ ] Re-evaluation creates a new view rather than mutating history.

## 11. Historical State

- [ ] Event-time and processing-time order can be reconstructed.
- [ ] Consumers can distinguish what was known then from what is now believed about then.
- [ ] Corrections and backfills retain receipt and processing context.
- [ ] Retention or deletion policies do not silently break provenance chains.

## 12. Derived Values

- [ ] Every derived value identifies all input records.
- [ ] Algorithm, rule or model ID and version are recorded.
- [ ] Parameters, assumptions and exclusions are recorded.
- [ ] Units and uncertainty propagation are explicit.
- [ ] Derived values are never relabeled as direct observations.
- [ ] Reproduction information is sufficient for review.

## 13. Scenario and Safety Integration

- [ ] Scenario consumers can distinguish live, historical, simulated and human-reported inputs.
- [ ] Degraded quality is visible to the accountable human operator.
- [ ] The model does not issue vessel-control commands.
- [ ] The model does not authorize navigation, maintenance or emergency actions.
- [ ] Safety-relevant state remains reviewable and source-traceable.
- [ ] AI or automation cannot promote authority without accountable human evidence.

## 14. Acceptance Evidence

- [ ] `DIGITAL_TWIN_STATE_AND_OBSERVATION_MODEL.md` is present.
- [ ] `digital-twin-state-observation.examples.json` is valid JSON.
- [ ] Examples include observed/simulated input, missing data, conflict handling, state assertion, derived value and current-state view.
- [ ] Package documentation records limitations and downstream use.
- [ ] Branch is based on current `develop`.
- [ ] Pull request targets `develop` and closes ISSUE-77.
