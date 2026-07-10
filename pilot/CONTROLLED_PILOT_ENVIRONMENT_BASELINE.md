---
Artifact-ID: OMSP-PILOT-ENV-0001
Title: Controlled Pilot Environment and Access-Control Baseline
Version: 0.1.0
Status: Draft
Owner: OMSP Engineering Council
Created: 2026-07-10
Last-Updated: 2026-07-10
Sprint: Sprint-6
Work-Package: WP-0061
Traceability:
  - ISSUE-149
  - OMSP-RISK-RR-001
  - OMSP-SPRINT6-PLAN-0001
---

# Controlled Pilot Environment and Access-Control Baseline

## Purpose

This artifact defines the minimum governed environment, identity, deployment, rollback and evidence controls required before OMSP may enter a controlled pilot. It is a provider-neutral control baseline, not evidence that a pilot environment has already been provisioned or approved.

## Authority Boundary

This baseline does not authorize production deployment, unrestricted external access, physical-vessel operation, certification, autonomous control or residual-risk acceptance. Pilot activation requires a separate accountable human approval bound to an immutable source revision and a completed validation record.

## Environment Classes

| Environment | Purpose | Data Class | External Access | Deployment Authority |
|---|---|---|---|---|
| development | engineering and local validation | synthetic only | restricted | contributors through normal PR workflow |
| integration | automated cross-component validation | synthetic or sanitized | restricted | CI service identity |
| controlled-pilot | approved pilot execution and evidence generation | approved pilot dataset only | allowlisted and monitored | pilot release manager after human approval |
| production | unrestricted operational service | not defined | prohibited in Sprint-6 | not authorized |

No controlled-pilot resource may share credentials, mutable storage, privileged identities or deployment targets with development resources. No resource may be represented as production-equivalent unless a separate evidence-backed decision explicitly says so.

## Trust Zones

1. **Source and build zone** — protected repository revisions, CI runners and generated build evidence.
2. **Artifact zone** — immutable pilot packages, checksums, provenance and approval records.
3. **Pilot execution zone** — isolated runtime, approved configuration and synthetic or sanitized inputs.
4. **Observability zone** — remote logs, metrics, audit events and alert-delivery evidence.
5. **Recovery zone** — isolated backup and restore material outside the primary pilot failure domain.
6. **Administrative zone** — privileged access path, break-glass control and approval records.

Traffic between zones must be explicitly allowed, authenticated, logged and limited to required protocols. Default-deny applies to inbound administration and cross-zone access.

## Required Resource Inventory

Before activation, the environment record must identify:

- source repository and immutable revision;
- build and CI identities;
- artifact storage location and retention owner;
- pilot runtime components and network boundaries;
- configuration and secret stores;
- telemetry, alerting and evidence stores;
- backup and recovery targets;
- administrative access endpoints;
- accountable owners and deputies;
- deletion and decommissioning procedure.

Unknown, unowned or shared privileged resources block pilot activation.

## Identity and Access-Control Model

| Role | Permitted Actions | Prohibited Actions | Approval Requirement |
|---|---|---|---|
| contributor | propose source and documentation changes | direct pilot deployment, secret access | reviewed PR |
| CI service | build, validate and publish candidate evidence | human approval, risk acceptance | protected workflow identity |
| pilot operator | start, stop and observe approved pilot runs | alter source, bypass gates, approve own changes | approved runbook and scoped access |
| pilot release manager | bind approved revision to pilot package and deploy | unilateral risk acceptance or production promotion | accountable approval record |
| security reviewer | review identity, secret and scan evidence | deploy or modify runtime | independent review |
| incident commander | pause, abort, revoke access and coordinate recovery | silently resume after abort | documented incident authority |
| approver | approve or reject pilot activation and risk disposition | originate implementation evidence | independent accountable decision |
| break-glass custodian | authorize emergency privileged access | routine administration | two-person approval except immediate safety containment |

### Mandatory Controls

- unique human identities; shared human accounts are prohibited;
- multi-factor authentication for privileged roles;
- least privilege and time-bounded elevation;
- separation between implementation, review and approval;
- service identities scoped to one environment and purpose;
- quarterly access review, plus event-driven review after role changes or incidents;
- immediate revocation for departed or compromised identities;
- all privileged actions correlated to an actor, reason, revision and ticket;
- deny-by-default access for external networks.

## Break-Glass Access

Break-glass access is permitted only for containment, recovery or prevention of material evidence loss.

Required process:

1. declare the incident or urgent condition;
2. identify requester and approving custodian;
3. issue a time-limited credential or elevation;
4. record reason, scope and expected duration;
5. capture all privileged activity;
6. revoke access immediately after use;
7. rotate exposed credentials;
8. complete retrospective review within one business day.

Unreviewed or persistent break-glass access blocks pilot continuation.

## Secrets and Configuration Baseline

- secrets must not be stored in source, issue text, logs or generated evidence;
- pilot secrets must be isolated from development and future production credentials;
- secret retrieval must use authenticated workload or operator identity;
- secrets must be redacted before telemetry export;
- configuration must be revisioned, reviewable and linked to the pilot package;
- emergency configuration changes require retrospective review and a replacement immutable baseline;
- suspected exposure triggers revocation, rotation, incident handling and pilot pause.

## Deployment Gate

A pilot deployment may proceed only when all of the following are true:

- immutable source revision and candidate package are identified;
- required CI and quality gates pass;
- environment inventory is complete and approved;
- access-control matrix is validated;
- rollback package and procedure are available;
- telemetry and audit capture are active;
- no unresolved critical security finding exists;
- RR-001 and RR-002 have an explicit pilot disposition;
- accountable human pilot-activation approval is recorded.

Automation may report gate status but cannot approve activation.

## Change Control

Normal changes require an issue, Work Package branch, reviewed PR, passing checks and an updated immutable pilot package. Direct mutation of a running pilot is prohibited except for documented emergency containment. Emergency changes must be captured, reviewed and reconciled before resumption.

## Rollback and Access-Revocation Drill

Before activation, a validation exercise must demonstrate:

- rollback to the previous approved package;
- preservation of audit and telemetry evidence;
- revocation of a privileged operator;
- invalidation or rotation of affected credentials;
- restoration of service within declared pilot objectives;
- prevention of automatic restart after an abort decision.

A failed drill blocks pilot activation until remediated and repeated.

## Pause and Abort Conditions

Pilot activity must pause or abort when:

- privileged access cannot be attributed;
- telemetry or audit capture is materially unavailable;
- an unauthorized configuration or revision is detected;
- a secret or signing credential may be exposed;
- rollback cannot be executed;
- environment isolation is violated;
- a high-severity incident exceeds the approved pilot risk boundary;
- an accountable human decision orders suspension.

## Evidence Package

The WP-0061 evidence package must contain:

- completed resource inventory;
- approved access-control matrix;
- identity and privilege review results;
- configuration and secret-handling validation;
- deployment gate record;
- rollback and access-revocation drill results;
- exceptions and unresolved findings;
- RR-001 reassessment;
- accountable activation approval or rejection.

## RR-001 Reassessment Rule

RR-001 remains open until a concrete pilot environment is provisioned, inventoried, validated and approved. Completion of this design baseline alone may reduce uncertainty but cannot close RR-001. Production-environment approval remains outside this Work Package.
