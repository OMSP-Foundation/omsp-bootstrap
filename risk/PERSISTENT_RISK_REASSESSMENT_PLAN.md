---
Artifact-ID: OMSP-RISK-REASSESSMENT-0001
Title: Persistent Risk Reassessment Plan for RR-001–RR-005
Version: 0.1.0
Status: Review
Owner: OMSP Engineering Council
Created: 2026-07-10
Last-Updated: 2026-07-10
Sprint: Sprint-6
Work-Package: WP-0059
Traceability:
  - ISSUE-144
  - OMSP-RELEASE-BASELINE-0001
  - OMSP-BASELINE-APPROVAL-050-0001
---

# Persistent Risk Reassessment Plan for RR-001–RR-005

## Purpose

This plan governs the Sprint-6 reassessment of the five residual risks carried forward from the `v0.5.0` Production Baseline Candidate. The risks are deferred for evidence generation; they are not accepted for unrestricted production use.

## Decision Boundary

Automation may collect evidence, execute tests and recommend a disposition. It cannot accept residual risk, close a risk, authorize production deployment, approve publication or declare OMSP production-safe. Final disposition requires an accountable human decision recorded against an immutable source revision.

## Rating Scale

- Likelihood: Low, Medium, High
- Impact: Low, Medium, High, Critical
- Overall rating: derived through governance review; automation does not assign acceptance authority.

## Reassessment Matrix

| ID | Current Rating | Evidence Gap | Required Validation | Accountable Owner | Review Trigger | Escalation Threshold | Closure Criterion | Carry-Forward Rule |
|---|---|---|---|---|---|---|---|---|
| RR-001 | High | No governed pilot/production environment, deployment control or environment approval evidence | Define controlled pilot environment; enforce protected deployment approvals; record rollback, access and separation-of-duty evidence | Platform Operations Owner | Before pilot activation; any deployment-target or privilege-model change | Any unapproved deployment path, privileged bypass or environment-boundary failure | Approved environment record, protected deployment path, tested rollback and named activation authority | Carry forward as blocking when any environment or approval evidence is missing |
| RR-002 | High | No signed provenance, signed release artifact or immutable signed audit evidence | Produce verifiable artifact provenance; sign release package and attest source commit; validate signature and tamper-detection workflow | Release & Supply-Chain Owner | Before pilot package approval; any signing-key or provenance format change | Missing/invalid signature, unverifiable source binding, key compromise or mutable approval evidence | Independent verification succeeds for source, package and approval record; key custody is approved | Carry forward as blocking when provenance cannot be independently verified |
| RR-003 | Medium | No remote telemetry, alert delivery, paging, SLO evidence or long-term evidence store | Integrate remote health/audit sink; exercise alert delivery; define retention and response objectives; verify redaction | Operations & Observability Owner | Before pilot activation; material monitoring, retention or incident-routing change | Missing critical signal, alert delivery failure, privacy leak or evidence loss beyond objective | Critical signals are remotely retained, alerts are delivered and acknowledged, retention/redaction tests pass | Carry forward with restricted pilot scope only when compensating manual monitoring is explicitly approved |
| RR-004 | Medium | No vulnerability intelligence integration or repository-history secret scan | Run dependency/action vulnerability intelligence; scan full repository history for secrets; govern findings and exceptions | Security Owner | Before pilot package approval; dependency/action change; new critical advisory | Critical exploitable finding, exposed credential, unowned exception or stale vulnerability evidence | No unresolved critical finding or exposed credential; exceptions have owner, expiry and approval | Carry forward as blocking for production; pilot exception requires explicit time-bounded approval |
| RR-005 | High | No load, capacity, availability, endurance, backup-restore or external disaster-recovery qualification | Define workload profile; run load/endurance tests; measure recovery objectives; exercise external backup restore and disaster recovery | Reliability & Recovery Owner | Before pilot exit; architecture, workload or recovery-topology change | Unsafe degradation, unmet recovery objective, unrecoverable evidence or data loss | Approved performance envelope, availability evidence, successful restore and external recovery exercise | Carry forward as blocking when pilot exit evidence or recovery objectives are unmet |

## Risk-by-Risk Rationale

### RR-001 — Deployment Environment and Approval

- Cause: the baseline contains tooling and workflows but no governed deployment target or protected environment activation path.
- Consequence: evidence generated in CI could be mistaken for authority to operate in production.
- Existing controls: read-only workflows, documented approval boundaries, release-readiness record and human approval requirement.
- Target horizon: controlled pilot environment definition and activation gate in Sprint-6.

### RR-002 — Provenance and Audit Integrity

- Cause: checksums exist, but provenance, release artifacts and audit evidence are not cryptographically signed.
- Consequence: source-to-package identity and approval records cannot be independently protected against tampering.
- Existing controls: SHA-256 manifests, immutable commit references and governed approval records.
- Target horizon: signed pilot package and independent verification evidence in Sprint-6.

### RR-003 — Remote Observability and Evidence Retention

- Cause: observability evidence is generated locally or as CI artifacts without remote operational alerting and durable retention.
- Consequence: failures may not be detected or escalated within an approved response objective, and evidence may expire.
- Existing controls: structured JSONL events, health records, redaction and recovery runbook.
- Target horizon: remote pilot telemetry, alert test and retention evidence in Sprint-6.

### RR-004 — Vulnerability and Historical Secret Intelligence

- Cause: current security checks inspect workflow configuration and committed content but do not query current vulnerability intelligence or scan repository history.
- Consequence: known vulnerable components or previously committed credentials may remain undetected.
- Existing controls: workflow inventory, permission checks, action-reference checks, current-tree secret patterns and SBOM evidence.
- Target horizon: full-history secret scan and vulnerability evidence in Sprint-6.

### RR-005 — Performance, Availability and External Recovery

- Cause: the demonstrator and recovery drill are functional but not workload-, availability- or external-infrastructure-qualified.
- Consequence: pilot success may not predict sustained operation or recoverability under realistic failure conditions.
- Existing controls: deterministic demonstrator, recovery drill, incident runbook and retained evidence.
- Target horizon: workload qualification, endurance evidence and external recovery exercise in Sprint-6.

## Governance Cadence

- Scheduled review: at Sprint-6 midpoint and before pilot activation or pilot exit, whichever occurs first.
- Event-driven review: any escalation threshold, control failure, material architecture change, security incident or evidence-integrity concern.
- Decision options: mitigate, transfer, time-bounded accept for controlled pilot, carry forward, close.
- Approval forum: OMSP Engineering Council with the named accountable owner and independent reviewer for security- or safety-relevant evidence.

## Required Decision Record

Every disposition must record:

- risk ID and current rating;
- evidence identifiers and immutable source revision;
- control effectiveness conclusion;
- decision and rationale;
- accountable approver and decision date;
- validity period or next review trigger;
- linked issue, pull request, artifact and release/pilot decision.

## Pilot and Production Rules

- Pilot activation is blocked when RR-001 or RR-002 lacks required evidence.
- Pilot activation requires an explicit disposition for all five risks.
- Pilot exit cannot be represented as production readiness while RR-001, RR-002 or RR-005 remains unresolved.
- Any pilot exception must be scoped, time-bounded, owned and revocable.
- Production release requires a new accountable decision; Sprint-5 approval cannot be reused as production authorization.
