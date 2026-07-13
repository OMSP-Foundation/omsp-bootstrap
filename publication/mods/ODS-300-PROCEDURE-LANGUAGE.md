---
Artifact-ID: OMSP-MODS-ODS-0300
Title: ODS-300 — Operational Procedure Language Standard (Draft)
Version: 0.1.0
Status: Draft
Owner: toss-cengiz
Baseline: Sprint-7
Classification: Public
Related-Issue: WP-0079 / #200
Traceability:
  - ISSUE-200
  - OMSP-MODS-SPEC-0001
  - OMSP-MODS-ODS-0100
  - OMSP-PLANNING-GOLDEN-PATH-0001
  - OMSP-REFERENCE-SCENARIO-0001
  - OMSP-PLANNING-REBASELINE-0001
---

# ODS-300 — Operational Procedure Language Standard (Draft)

> **Status: Draft.** This section is subject to revision by the first
> conformance test: the first golden-path output instance produced in
> Sprint 9 (WP-0087) is the first conformance test of these rules, and its
> findings feed back into this document (WP-0075 §4 / WP-0079).

## 1. Purpose and Scope

ODS-300 defines the **procedural step language** used in rendered
operational content: inspection sequences, procedure steps, and decision
points. It is part of the MODS Specification
([`MODS_SPECIFICATION.md`](MODS_SPECIFICATION.md), `OMSP-MODS-SPEC-0001`).
Its first application is the inspection sequence of the golden-path
scenario section (ODS-100-R-04.3).

Derivation discipline: all normative content of ODS-300 is derived from
governed repository artifacts — primarily the step-and-decision contract of
[`reference/OPERATIONAL_SCENARIO_MODEL.md`](../../reference/OPERATIONAL_SCENARIO_MODEL.md)
(`OMSP-REFERENCE-SCENARIO-0001`) §7 and the golden-path definition
[`planning/WP-0074-GOLDEN-PATH-DEFINITION.md`](../../planning/WP-0074-GOLDEN-PATH-DEFINITION.md)
§8. This standard asserts **no facts about external documentation
standards**; no external-standard claim is normative here.

Rule identifiers follow the pattern `ODS-300-R-NN` and are stable: a
withdrawn rule number is never reused.

## 2. Scenario-Model Compatibility Mapping (binding)

ODS-300 step language must be able to express **every** step and decision
field of `OMSP-REFERENCE-SCENARIO-0001` §7. The mapping below is normative:
no source field may be dropped by a renderer. A scenario field with no
value renders per ODS-300-R-09 (explicit unknown), never by omission.

| `OMSP-REFERENCE-SCENARIO-0001` §7 field | ODS-300 construct | Rule |
| --- | --- | --- |
| Sequence and stable step ID | Step number + rendered stable step ID | ODS-300-R-03 |
| Responsible actor | Actor label on every step | ODS-300-R-03 |
| Action or observation | Step statement (imperative, single action/observation) | ODS-300-R-01, ODS-300-R-02 |
| Required inputs and referenced evidence | Inputs/evidence line of the step block | ODS-300-R-10 |
| Affected systems, equipment, interfaces or compartments | Equipment/system reference line of the step block | ODS-300-R-10 |
| Entry and completion criteria | Entry-criterion and completion-criterion fields | ODS-300-R-04 |
| Hazards and safeguards | Hazard/safeguard callout attached to the step | ODS-300-R-06 |
| Expected observation or state change | Expected-observation field | ODS-300-R-04 |
| Failure, ambiguity and escalation handling | Escalation block of the step | ODS-300-R-06 |
| Human confirmation mandatory (yes/no) | Human-confirmation marker | ODS-300-R-05 |
| Decision point: available branches | Decision-point construct: branch list | ODS-300-R-07 |
| Decision point: decision authority | Decision-point construct: authority field | ODS-300-R-07 |
| Decision point: required evidence | Decision-point construct: evidence field | ODS-300-R-07 |
| Decision point: time sensitivity | Decision-point construct: time-sensitivity field | ODS-300-R-07 |
| Decision point: fallback behavior | Decision-point construct: fallback field | ODS-300-R-07 |
| Unknown/conflicting evidence routes to a conservative human-reviewed branch | Mandatory conservative default branch | ODS-300-R-08 |

## 3. Step Writing Rules

**ODS-300-R-01 — Imperative mood.** Every action step is written in the
imperative mood ("Check the main battery switch position"), addressed to
the responsible actor. Observation steps state the observation to be made
in the imperative ("Observe the battery-monitor voltage reading").

**ODS-300-R-02 — One action or observation per step.** Each step contains
exactly one action or one observation. Compound instructions are split into
separate steps.

**ODS-300-R-03 — Step identity and responsible actor.** Every step renders
its sequence number, its stable step ID (per the identity pattern of
`OMSP-REFERENCE-SCENARIO-0001` §3), and a responsible-actor label. A step
without an actor label is non-conformant.

**ODS-300-R-04 — Entry, completion, expected observation.** Every step
renders an entry criterion, a completion criterion, and an expected
observation or state change. These fields may be brief, but they may not be
absent; an unestablished criterion renders per ODS-300-R-09.

**ODS-300-R-05 — Human-confirmation marker.** A step for which human
confirmation is mandatory carries an explicit, visually distinct marker
(rendered text form in v0.1: `[HUMAN CONFIRMATION REQUIRED]`). The marker's
graphic treatment is an ODS-200 concern; its presence and text are governed
here.

**ODS-300-R-06 — Hazards, failure and escalation block.** Every step
renders its associated hazards and safeguards, and an escalation block
stating how failure or ambiguity in the step is handled and to whom it
escalates. Steps with no identified hazard state so explicitly.

## 4. Decision Points

**ODS-300-R-07 — Decision-point construct (first-class).** Decision points
are rendered as a first-class construct, distinct from steps, containing
all five fields: available branches, decision authority, required evidence,
time sensitivity, and fallback behavior. A decision rendered as a plain
step is non-conformant.

**ODS-300-R-08 — Conservative human-review branch (mandatory default).**
Every decision point includes a branch for unknown or conflicting evidence,
and that branch routes to a conservative human-reviewed outcome. This
branch is present even when the source scenario declares no other fallback:
unknown or conflicting evidence never routes to an automated or optimistic
continuation.

## 5. Evidence and Source Rules

**ODS-300-R-09 — Unknown rendering.** `unknown` and `<to-be-sourced>`
values in steps are rendered visibly as such — never hidden, dropped, or
replaced with a guessed value. (Document-level evidence listing:
ODS-100-R-07.)

**ODS-300-R-10 — Step source tracing.** Every step references at least one
equipment role (model element) and at least one source reference
(source-register entry) — or carries an explicit `unknown` evidence marker
where the source is not yet established. A step with neither is
non-conformant. Source: WP-0074 §11.3.

## 6. Reserved Subtopics (not drafted in v0.1)

The following ODS-300 subtopics are **Reserved**. They carry no normative
content in v0.1 and are drafted in later Work Packages (see
`OMSP-MODS-SPEC-0001` §4):

### 6.1 Challenge–response checklist language (QRH-facing) — Reserved

### 6.2 Role assignment schemes beyond the actor label — Reserved

### 6.3 Condition blocks and conditional procedures — Reserved

### 6.4 Step granularity metrics and limits — Reserved

## 7. Conformance

Conformance to ODS-300 is checked with
[`MODS_RENDERER_CONFORMANCE_CHECKLIST.md`](MODS_RENDERER_CONFORMANCE_CHECKLIST.md)
(`OMSP-MODS-CONFORMANCE-0001`). The first conformance test is the Sprint-9
golden-path output instance (WP-0087).
