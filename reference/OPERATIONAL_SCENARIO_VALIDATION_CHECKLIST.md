---
Artifact-ID: OMSP-REFERENCE-SCENARIO-VALIDATION-0001
Title: Operational Scenario Validation Checklist
Version: 1.0.0
Status: Review
Owner: OMSP Engineering Council
Created: 2026-07-10
Last-Updated: 2026-07-10
Sprint: Sprint-4
Work-Package: WP-0042
Traceability:
  - ISSUE-76
  - OMSP-REFERENCE-SCENARIO-0001
---

# Operational Scenario Validation Checklist

## Identity and Scope

- [ ] Scenario has a unique stable identifier and explicit version.
- [ ] Scenario class is one of normal, degraded, emergency, maintenance or validation.
- [ ] Applicability identifies vessel design, configuration or vessel instance.
- [ ] Design-family examples are not presented as vessel-specific procedures.
- [ ] Lifecycle state and approval authority are explicit.

## Actors and Authority

- [ ] Every actor has a defined role and responsibility.
- [ ] Accountable human command authority is named.
- [ ] Software roles are limited to observation, recording, calculation, warning or recommendation.
- [ ] No software actor is granted command, risk acceptance or safety approval authority.
- [ ] Escalation to the responsible human is explicit.

## Preconditions and Triggers

- [ ] Preconditions are testable or explicitly unknown.
- [ ] Configuration and equipment applicability are referenced.
- [ ] Required procedures and evidence are identified.
- [ ] Trigger source, timestamp, confidence and verification state are recorded.
- [ ] Inferred triggers remain distinguishable from observed or human-reported events.
- [ ] Missing data is not interpreted as a satisfactory condition.

## Steps and Decisions

- [ ] Steps have stable identifiers and deterministic ordering.
- [ ] Each step identifies responsible actor, action and completion criteria.
- [ ] Affected systems, equipment roles, interfaces or compartments are traceable.
- [ ] Human confirmation requirements are explicit.
- [ ] Decision points identify authority, evidence, branches and fallback behavior.
- [ ] Unknown or conflicting evidence routes to conservative human review.
- [ ] Stop, abort and escalation conditions are visible.

## Hazards and Safeguards

- [ ] Hazards are linked to relevant conditions or steps.
- [ ] Affected people, vessel, environment or third parties are identified where applicable.
- [ ] Prevention, detection and mitigation controls are recorded.
- [ ] Residual uncertainty is visible.
- [ ] Risk classification source and authority are explicit if risk ratings are used.
- [ ] Scenario content does not claim regulatory risk acceptance.

## Outcomes and Evidence

- [ ] Expected and alternate outcomes are explicitly classified.
- [ ] Unacceptable and unknown outcomes are representable.
- [ ] Outcomes are observable or evidentially testable.
- [ ] Evidence expectations include source, time, actor and provenance.
- [ ] Scenario completion is not treated as proof of seaworthiness or equipment fitness.

## Traceability

- [ ] Vessel configuration and system identifiers resolve to governed artifacts.
- [ ] Equipment and interface references align with `OMSP-REFERENCE-EQUIPMENT-0001`.
- [ ] Procedure, checklist, requirement, hazard and evidence links are typed.
- [ ] Asserted, sourced, observed and inferred relations remain distinguishable.
- [ ] Changes in operational meaning produce a new scenario version.

## Safety Boundary

- [ ] Scenario states that approved procedures and human judgement prevail.
- [ ] Scenario is not written as live navigational, emergency or maintenance instruction.
- [ ] No autonomous operation or vessel control is authorized.
- [ ] No installed equipment existence or functional state is assumed without evidence.
- [ ] No certification, compliance, competence or seaworthiness claim is made.
- [ ] Emergency examples cannot delay or replace approved emergency action.

## Example Coverage

- [ ] At least one normal scenario is represented.
- [ ] At least one degraded scenario is represented.
- [ ] At least one emergency scenario is represented.
- [ ] Hanse 460 mappings remain at design-family reference level.
- [ ] Example unknowns, limitations and human-authority boundaries are explicit.

## Review Result

- Reviewer:
- Review date:
- Artifact version:
- Result: `pass` / `pass-with-actions` / `fail`
- Open actions:
- Evidence references:
- Approval authority: