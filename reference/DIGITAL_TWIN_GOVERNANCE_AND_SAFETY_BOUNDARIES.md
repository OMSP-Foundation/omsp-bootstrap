# Digital Twin Governance and Safety Boundaries

- Artifact ID: `OMSP-REFERENCE-TWIN-GOVERNANCE-0001`
- Version: `0.1.0`
- Status: `review`
- Scope: OMSP digital-twin documentation artifacts and future runtime implementations

## 1. Purpose

This policy defines authority, approval, accountability, escalation, change-control, and safety boundaries for OMSP digital-twin artifacts.

Digital-twin outputs are evidence-bearing representations and advisory products. They are not certified operational instructions, approved procedures, navigation commands, emergency orders, or substitutes for accountable human judgment.

## 2. Governing principles

1. Human command authority remains explicit and non-delegable.
2. Configuration facts, observations, state assertions, and derived values remain separate authority classes.
3. Provenance, uncertainty, quality, freshness, and conflicts remain visible.
4. Missing data is never replaced with an undisclosed default.
5. Safety-critical ambiguity causes escalation or stop-use, not silent inference.
6. AI-assisted content is always reviewable, attributable, and subordinate to human approval.
7. No artifact gains operational authority through format, automation, repetition, or model confidence alone.

## 3. Authority classes

### 3.1 Configuration authority

Configuration facts describe vessel design, selected options, or verified installed state.

Permitted authority levels:

- `reference`: design-family or illustrative information;
- `declared`: supplied by an accountable owner but not independently verified;
- `observed`: supported by inspection or captured evidence;
- `verified`: reviewed against controlled evidence by an authorized reviewer;
- `approved`: accepted through the applicable configuration-control process.

Observations and derived values cannot automatically promote a configuration claim to `verified` or `approved`.

### 3.2 Observation authority

An observation records what a source reported at a time. It does not prove configuration, fitness, correctness, or operational safety.

Observation authority must remain tied to:

- source identity and source class;
- event, receipt, and processing times;
- quality and freshness;
- calibration or competence context when available;
- correction and supersession history.

### 3.3 State authority

A state assertion or current-state view is a time-bounded interpretation produced under a declared policy. It must identify the observations used, exclusions applied, conflicts retained, and projection time.

State is not configuration and is not an instruction.

### 3.4 Derived-value authority

A derived value is advisory unless a separate controlled process explicitly grants another role. It must retain input identities, method and version, assumptions, execution time, quality, limitations, and unresolved conflicts.

## 4. Human accountability

Every operationally relevant artifact must identify an accountable human role.

Only an authorized human may:

- accept or reject an advisory output;
- resolve evidence conflicts for operational use;
- approve a configuration change;
- invoke an approved procedure;
- authorize continuation, pause, or abort of an activity;
- determine whether external expert, manufacturer, class, flag, insurer, or emergency support is required.

Software may monitor, record, compare, project, flag, summarize, and advise. It may not silently assume command authority.

## 5. Safety-critical disclaimer

All OMSP digital-twin artifacts and outputs must carry a scope-appropriate disclaimer stating that they are not certified operational instructions unless a separate approved process explicitly establishes such status.

A disclaimer must not be used to excuse a known modeling defect. Defects affecting traceability, authority, provenance, visibility, or safety boundaries are merge-blocking.

## 6. Escalation and stop-use rules

Use of an artifact or output must stop or be escalated when any of the following applies:

- source or target identity cannot be resolved;
- required provenance is missing;
- data is stale beyond the declared policy;
- conflicting evidence is unresolved and materially relevant;
- a value is inferred from missing data without explicit approval;
- the applicable configuration version is unknown;
- an advisory output could be mistaken for a command;
- accountable human authority is absent;
- a safety-critical condition exceeds the documented model scope;
- an AI-generated statement cannot be traced to evidence;
- a runtime behaves outside its approved test and operating envelope.

The required response is one or more of:

- mark the result `indeterminate`;
- suppress operational presentation;
- request human review;
- revert to approved procedures and primary evidence;
- isolate or disable the affected function;
- record the event and preserve evidence;
- escalate to the appropriate accountable authority.

## 7. AI-assistance boundaries

AI may assist with drafting, classification, mapping, anomaly flagging, summarization, and candidate inference generation.

AI must not:

- approve configuration facts;
- create undisclosed evidence;
- conceal uncertainty or conflicts;
- issue navigation or emergency commands;
- override approved procedures;
- certify seaworthiness, compliance, or risk acceptance;
- resolve safety-critical ambiguity without accountable human review;
- present generated content as manufacturer, regulatory, or class authority.

AI-produced content must be labeled, attributable to the generating process where practical, and reviewed according to impact.

## 8. Approval levels

- `draft`: incomplete and not approved for reliance;
- `review`: ready for controlled review;
- `accepted-reference`: approved as a reference artifact within stated limitations;
- `approved-implementation`: approved for a defined implementation context and test envelope;
- `operationally-authorized`: separately authorized by the competent organization for a defined use, vessel, environment, and period.

Repository merge does not by itself create `approved-implementation` or `operationally-authorized` status.

## 9. Change control

Every material change must identify:

- changed artifact and version;
- reason and initiating issue;
- affected identifiers and dependencies;
- authority or safety impact;
- migration or compatibility implications;
- validation evidence;
- reviewer and approver roles;
- rollback or supersession path.

Breaking semantic changes require a version change and explicit impact review. Historical evidence must remain reproducible.

## 10. Review policy

Review depth is risk-based:

- editorial: clarity with no semantic effect;
- model: schema, identity, provenance, or interoperability effect;
- safety-relevant: authority, escalation, human role, or operational interpretation effect;
- implementation-critical: runtime, control path, cybersecurity, timing, or integration effect.

Safety-relevant and implementation-critical changes require independent review from the author and explicit recorded disposition.

## 11. Presentation rules

Interfaces and reports must visibly distinguish:

- verified or approved configuration;
- raw observations;
- projected state;
- derived advisory values;
- stale, missing, conflicted, simulated, and human-reported data;
- model limitations and applicable version;
- accountable human action required.

Color, ranking, confidence score, or polished language must never substitute for authority metadata.

## 12. Incident and correction handling

Errors must be corrected through an append-only or otherwise auditable process. Original evidence, prior outputs, affected versions, correction reason, and reviewer disposition must remain recoverable.

A safety-relevant error requires impact assessment across dependent artifacts and any implementation that consumed the affected output.

## 13. Non-goals

This policy does not provide certification, legal compliance, classification approval, flag-state acceptance, seaworthiness assessment, emergency procedure approval, cybersecurity accreditation, or operational authorization.
