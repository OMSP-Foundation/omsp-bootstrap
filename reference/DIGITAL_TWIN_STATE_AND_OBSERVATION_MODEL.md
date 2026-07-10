---
Artifact-ID: OMSP-REFERENCE-TWIN-STATE-0001
Title: Digital Twin State and Observation Model
Version: 1.0.0
Status: Review
Owner: OMSP Engineering Council
Approvers:
  - Accountable Maintainer
Created: 2026-07-10
Last-Updated: 2026-07-10
Sprint: Sprint-4
Work-Package: WP-0043
Traceability:
  - ISSUE-77
  - OMSP-REFERENCE-VESSEL-0001
  - OMSP-REFERENCE-EQUIPMENT-0001
  - OMSP-REFERENCE-SCENARIO-0001
---

# Digital Twin State and Observation Model

## 1. Objective

This artifact defines how OMSP represents observations, current and historical operating state, derived values, data quality and provenance without confusing runtime evidence with governed configuration facts.

The model is descriptive and advisory. It does not verify a vessel configuration, certify equipment condition, authorize operation, replace approved procedures or issue control commands.

## 2. Information Layers

The model separates six layers:

1. **Configuration fact** — governed claim about design, configuration or installed equipment supported by accountable evidence.
2. **Observation** — immutable record of something reported, measured or received at a time.
3. **State assertion** — time-bounded interpretation of one or more observations.
4. **Current state view** — computed projection of the latest eligible state assertions at a declared evaluation time.
5. **Historical state** — retained sequence of observations, assertions and supersession relationships.
6. **Derived value** — reproducible output calculated from identified inputs and a versioned method.

An observation, state assertion or derived value cannot automatically promote a configuration fact.

## 3. Stable Identity Rules

| Entity | Identifier pattern |
| --- | --- |
| Observation | `observation:<subject-id>:<property>:<event-id>` |
| State assertion | `state:<subject-id>:<property>:<assertion-id>` |
| Current state view | `state-view:<scope-id>:<evaluation-time>` |
| Derived value | `derived:<subject-id>:<property>:<derivation-id>` |
| Data source | `source:<authority>:<local-id>` |
| Quality assessment | `quality:<record-id>:<assessment-id>` |
| Conflict set | `conflict:<subject-id>:<property>:<conflict-id>` |

Identifiers remain stable across storage location and display-name changes.

## 4. Observation Contract

Every observation records:

- stable identifier;
- subject entity identifier;
- observed property or event type;
- value and unit, or explicit no-value reason;
- event time, receipt time and optional processing time;
- source identity, source type and acquisition channel;
- observation authority class;
- quality indicators and confidence;
- configuration applicability where known;
- provenance and transformation history;
- security and integrity status where available;
- related scenario, system, equipment, interface and procedure identifiers;
- limitations, warnings and unresolved conflicts.

Observations are append-only. Corrections create a new record linked by `corrects` or `supersedes`; the original remains historical evidence.

## 5. Time Semantics

Three timestamps are distinct:

- **event time** — when the reported phenomenon occurred;
- **receipt time** — when OMSP received the record;
- **processing time** — when a transformation or assessment was performed.

Late-arriving data may revise a current state projection but must not rewrite history. Clock source, timezone, synchronization quality and timestamp precision should remain visible.

## 6. Source and Authority Classes

Recommended observation source classes are:

- direct-sensor;
- equipment-controller;
- vessel-network;
- human-report;
- imported-log;
- external-service;
- simulation;
- test-fixture;
- derived-process;
- unknown.

Recommended authority classes are:

- observed;
- human-reported;
- imported;
- simulated;
- derived;
- proposed;
- unknown.

None of these equals `verified-design` or `verified-as-built` configuration authority.

## 7. Data Quality Model

Quality is multi-dimensional and must not be reduced to a single unexplained score. The record should include, where relevant:

- validity;
- completeness;
- freshness;
- timestamp confidence;
- source trust classification;
- calibration status;
- plausibility;
- consistency with related observations;
- resolution and precision;
- transformation loss;
- integrity or signature status.

Recommended quality states are `good`, `suspect`, `bad`, `unknown`, `stale`, `missing` and `conflicting`.

## 8. Missing and Stale Data

Missing data must be represented explicitly with a reason such as:

- not-observed;
- source-unavailable;
- channel-failure;
- not-applicable;
- intentionally-redacted;
- unsupported-property;
- unknown.

Staleness is evaluated against a property-specific freshness policy. A stale value remains historical evidence but must not be silently presented as current. The policy identifier and evaluation time must be recorded.

## 9. Conflicting Data

Conflicting observations are retained together in a conflict set. Conflict handling must record:

- competing record identifiers;
- conflict type;
- detection rule;
- affected state views;
- selected record, if any;
- selection rationale and accountable decision maker;
- unresolved status and safety impact.

A selection for display or analysis does not delete or invalidate the competing record.

## 10. State Assertions

A state assertion records:

- subject and property;
- asserted value or state class;
- valid-from and optional valid-to;
- supporting observation identifiers;
- assertion method and version;
- authority and confidence;
- quality status;
- conflict status;
- creation time and responsible actor;
- superseded-by relationship when replaced.

Human assertions and machine-generated assertions remain distinguishable.

## 11. Current State View

A current state view is a reproducible projection evaluated at a declared time. It must record:

- scope and evaluation time;
- selection policy and version;
- included and excluded records;
- stale and missing properties;
- unresolved conflicts;
- derived values used;
- warnings and confidence;
- whether a human reviewed the projection.

A current state view is not a mutable fact table. Re-evaluation creates a new view.

## 12. Historical State

Historical state retains the event-time and processing-time order of observations and assertions. Backfilled or corrected records preserve their original receipt and processing context. Consumers must be able to reconstruct what was known at a past time separately from what is now believed about that past time.

## 13. Derived Values

Every derived value records:

- stable identifier;
- input record identifiers;
- algorithm or rule identifier and version;
- parameters and units;
- execution time;
- output value;
- propagated quality and uncertainty;
- assumptions and exclusions;
- software or human actor responsible;
- reproducibility information.

Derived values cannot obscure their inputs or be relabeled as direct observations.

## 14. Scenario Integration

Operational scenarios may consume observations and state views only within their declared applicability. Scenario evidence must preserve the difference between:

- live observation;
- historical observation;
- simulated input;
- human report;
- derived assessment;
- configuration reference.

Scenario software remains advisory and must expose stale, missing, suspect and conflicting inputs to the accountable human operator.

## 15. Safety and Authority Boundary

This model does not:

- verify vessel seaworthiness or equipment fitness;
- certify sensor accuracy or calibration;
- authorize navigation, maintenance or emergency action;
- automatically alter configuration records;
- conceal degraded data quality;
- issue direct vessel-control commands;
- grant AI or automation final decision authority.

Safety-relevant state must remain reviewable by accountable humans and traceable to source evidence.

## 16. Validation Rules

A conforming implementation should ensure:

- every record has a stable identifier and valid subject;
- configuration facts and runtime observations are stored as distinct classes;
- event, receipt and processing times are distinguishable;
- source, authority and provenance are explicit;
- quality dimensions and missing-data reasons are visible;
- stale records cannot silently populate current state;
- conflicting observations are retained and linked;
- current views are reproducible and time-scoped;
- derived values identify all inputs and method versions;
- corrections preserve original records;
- human and machine assertions are distinguishable;
- no lifecycle promotion occurs without accountable evidence.

## 17. Known Limitations

This artifact does not select a production database, streaming platform, message protocol, time-series engine, sensor standard, cybersecurity framework or user interface. Example records are illustrative and do not represent a physical Hanse 460 or live vessel telemetry.
