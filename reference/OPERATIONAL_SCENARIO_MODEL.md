---
Artifact-ID: OMSP-REFERENCE-SCENARIO-0001
Title: Operational Scenario Model
Version: 1.0.0
Status: Review
Owner: OMSP Engineering Council
Approvers:
  - Accountable Maintainer
Created: 2026-07-10
Last-Updated: 2026-07-10
Sprint: Sprint-4
Work-Package: WP-0042
Traceability:
  - ISSUE-76
  - OMSP-PLAN-SPRINT-0004
  - OMSP-REFERENCE-VESSEL-0001
  - OMSP-REFERENCE-CONFIG-0001
  - OMSP-REFERENCE-EQUIPMENT-0001
---

# Operational Scenario Model

## 1. Objective

This artifact defines a reusable, governed structure for maritime operational scenarios. A scenario represents a bounded description of actors, context, preconditions, triggers, steps, decisions, expected outcomes, hazards, evidence and human-authority boundaries.

Scenarios are descriptive and analytical. They do not replace approved procedures, manufacturer instructions, command judgement, seamanship, emergency plans or regulatory requirements.

## 2. Scenario Classes

Each scenario must declare one primary class:

- **normal** — expected operation with required systems and information available;
- **degraded** — operation with reduced capability, uncertain information or unavailable equipment;
- **emergency** — immediate threat to people, vessel, environment or navigation safety;
- **maintenance** — controlled inspection, isolation, service or restoration activity;
- **validation** — evidence-gathering exercise that does not authorize live operational control.

A degraded or emergency scenario must never be treated as an automatic continuation of a normal scenario. Entry, escalation and termination conditions must be explicit.

## 3. Stable Identity

Recommended identities are:

- scenario definition: `scenario:<namespace>:<slug>:<version>`;
- scenario execution or exercise: `scenario-run:<scenario-id>:<timestamp-or-run-id>`;
- actor role: `actor-role:<namespace>:<slug>`;
- decision point: `decision:<scenario-id>:<local-id>`;
- step: `scenario-step:<scenario-id>:<sequence>`;
- hazard: `hazard:<namespace>:<slug>`;
- outcome: `outcome:<scenario-id>:<local-id>`.

Scenario identifiers remain stable across display-name changes. A changed operational meaning, authority boundary or sequence creates a new version.

## 4. Scenario Record Contract

Every scenario records:

- stable identifier, version, lifecycle state and scenario class;
- title, objective and applicability;
- vessel design, configuration or vessel-instance scope;
- actors and accountable human authority;
- preconditions and required evidence;
- initiating trigger and trigger confidence;
- assumptions, unknowns and exclusions;
- ordered steps and decision points;
- referenced systems, equipment roles, interfaces and procedures;
- hazards, safeguards and escalation criteria;
- expected, alternate and unacceptable outcomes;
- observations and evidence expected during validation;
- stop, abort and termination conditions;
- provenance, confidence and known limitations.

Missing data must be represented as `unknown`, `not-applicable` or `not-verified`; omission must not imply a safe or available state.

## 5. Actors and Authority

Actors may include:

- master or skipper;
- officer of the watch or helm operator;
- crew member;
- passenger or external person;
- shore support or service technician;
- vessel system or equipment role;
- monitoring or advisory software;
- emergency service or port authority.

Every action must identify whether the actor is responsible, supporting, consulted or informed. Human command authority must be explicit. Software may observe, record, calculate, warn or recommend, but it must not be assigned command authority by this model.

## 6. Preconditions and Triggers

Preconditions state what must be true before the scenario can begin. They include:

- configuration applicability;
- crew competence or role availability;
- environmental and location assumptions;
- system and equipment availability;
- required documents or procedures;
- communication and power availability;
- unresolved unknowns or limitations.

Triggers may be observed, reported, inferred or simulated. Trigger source, timestamp, confidence and validation status must be recorded. An inferred trigger cannot silently become a verified event.

## 7. Steps and Decisions

Each step records:

- sequence and stable step ID;
- responsible actor;
- action or observation;
- required inputs and referenced evidence;
- affected systems, equipment, interfaces or compartments;
- entry and completion criteria;
- hazards and safeguards;
- expected observation or state change;
- failure, ambiguity and escalation handling;
- whether human confirmation is mandatory.

Decision points record available branches, decision authority, required evidence, time sensitivity and fallback behavior. Unknown or conflicting evidence must route to a conservative human-reviewed branch.

## 8. Hazards and Constraints

Hazards must be linked to the steps or conditions in which they arise. Recommended fields include:

- hazard identity and description;
- affected people, vessel, environment or third parties;
- severity and likelihood classification source;
- initiating conditions;
- prevention, detection and mitigation controls;
- residual uncertainty;
- stop or escalation threshold;
- related procedure, requirement or evidence.

The model does not assign regulatory risk acceptance. Safety acceptance remains an accountable human and organizational decision.

## 9. Outcomes and Evidence

Outcomes are classified as:

- expected;
- acceptable alternate;
- degraded but controlled;
- aborted safely;
- unacceptable;
- unknown.

Expected outcomes must be observable or evidentially testable. Scenario completion does not prove equipment fitness, seaworthiness or procedural adequacy unless governed evidence explicitly supports that conclusion.

## 10. Procedure and Artifact Traceability

Scenarios should link to:

- vessel configuration and system identifiers;
- equipment classes, designs, configuration items or installed instances;
- typed interfaces and dependencies;
- approved procedures and checklists;
- requirements, hazards and constraints;
- training or competence artifacts;
- observations, logs and validation records;
- change records and review decisions.

Relations should distinguish `references`, `requires`, `observes`, `affects`, `mitigates`, `escalates-to`, `validated-by` and `derived-from`.

## 11. Hanse 460 Mapping Rules

Hanse 460 examples in this package apply only to `vessel-design:hanse:460` and `configuration:vessel-design:hanse:460:reference-0.1.0`. They are design-family mappings, not vessel-specific operating instructions.

The examples must not assert:

- installed manufacturer or model;
- as-built system availability;
- approved limits or alarm thresholds;
- crew competence;
- vessel-specific emergency procedures;
- safe execution on a physical vessel.

Before vessel-instance use, configuration, equipment, interfaces, procedures and human approval must be verified.

## 12. Scenario State Lifecycle

Recommended lifecycle states are:

- draft;
- review;
- approved-reference;
- approved-training;
- approved-vessel-specific;
- retired.

Promotion requires review evidence and defined authority. A reference scenario cannot automatically become an approved vessel-specific procedure.

## 13. Validation Rules

A conforming scenario must satisfy:

- unique stable identities and immutable version meaning;
- explicit scenario class and applicability;
- explicit accountable human authority;
- traceable actors, systems, equipment roles and procedures;
- explicit preconditions, triggers, assumptions and unknowns;
- ordered steps with entry and completion criteria;
- decision authority and fallback behavior;
- hazards, safeguards and escalation paths;
- observable outcomes and evidence expectations;
- stop and abort conditions;
- no conflation of design-family reference with vessel-instance fact;
- no autonomous command or safety approval granted to software.

## 14. Safety Boundary

This model does not:

- provide navigational, emergency or maintenance instructions for live use;
- replace official manuals, procedures or command judgement;
- certify safety, compliance, seaworthiness or crew competence;
- authorize autonomous operation or control;
- prove that referenced equipment exists or is functional;
- determine whether continuing an operation is safe.

When scenario content conflicts with approved instructions or the responsible human's judgement, approved instructions and human authority prevail.

## 15. Downstream Use

WP-0043 may use scenario identities and expected observations to define digital-twin state and observation records. WP-0044 may select bounded scenarios for a non-operational validation demonstrator. Downstream work must preserve provenance, uncertainty, authority and stop conditions.