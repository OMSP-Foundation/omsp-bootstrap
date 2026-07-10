---
Artifact-ID: OMSP-PILOT-ENV-VALIDATION-0001
Title: Controlled Pilot Environment Validation Record
Version: 0.1.0
Status: Template
Owner: OMSP Engineering Council
Created: 2026-07-10
Last-Updated: 2026-07-10
Sprint: Sprint-6
Work-Package: WP-0061
Traceability:
  - ISSUE-149
  - OMSP-PILOT-ENV-0001
  - OMSP-RISK-RR-001
---

# Controlled Pilot Environment Validation Record

## Validation Target

- Environment identifier:
- Provider / location:
- Immutable source revision:
- Pilot package digest:
- Validation date:
- Validator:
- Accountable approver:

## Resource Inventory

| Resource | Trust Zone | Owner | Data Class | Privileged Identity | Evidence Reference | Result |
|---|---|---|---|---|---|---|
| | | | | | | not-tested |

## Access-Control Validation

| Control | Test Method | Evidence | Result | Finding |
|---|---|---|---|---|
| Unique human identities | account inventory review | | not-tested | |
| MFA for privileged roles | authentication evidence | | not-tested | |
| Least privilege | permission diff and negative test | | not-tested | |
| Separation of duties | role-conflict review | | not-tested | |
| Time-bounded elevation | expiry test | | not-tested | |
| External default deny | network access test | | not-tested | |
| Privileged action audit | correlated action test | | not-tested | |
| Access revocation | revoke and retry test | | not-tested | |

## Secrets and Configuration Validation

| Control | Evidence | Result | Finding |
|---|---|---|---|
| No secrets in source or logs | | not-tested | |
| Pilot credentials isolated | | not-tested | |
| Secret retrieval authenticated | | not-tested | |
| Telemetry redaction active | | not-tested | |
| Configuration bound to revision | | not-tested | |
| Rotation procedure exercised | | not-tested | |

## Deployment Gate

- [ ] Immutable revision identified.
- [ ] Required CI and quality gates passed.
- [ ] Resource inventory complete.
- [ ] Access-control matrix approved.
- [ ] Rollback package available.
- [ ] Telemetry and audit capture active.
- [ ] No unresolved critical security finding.
- [ ] RR-001 pilot disposition recorded.
- [ ] RR-002 pilot disposition recorded.
- [ ] Accountable human activation decision recorded.

## Rollback and Revocation Drill

| Step | Expected Result | Actual Result | Evidence | Status |
|---|---|---|---|---|
| Deploy approved pilot package | expected revision active | | | not-tested |
| Roll back to prior package | prior approved revision restored | | | not-tested |
| Revoke privileged operator | subsequent access denied | | | not-tested |
| Rotate affected credential | old credential rejected | | | not-tested |
| Preserve audit evidence | complete correlated record retained | | | not-tested |
| Abort pilot run | no automatic restart | | | not-tested |

## Findings and Exceptions

| ID | Severity | Description | Owner | Due Date | Disposition |
|---|---|---|---|---|---|
| | | | | | open |

## RR-001 Reassessment

- Current rating:
- Evidence gained:
- Remaining gap:
- Proposed disposition: `open`, `mitigated-for-pilot`, `accepted-for-pilot`, or `closed`
- Production applicability: not assessed by this record

## Decision

- [ ] Approved for controlled pilot activation.
- [ ] Rejected pending remediation.
- [ ] Suspended due to unresolved blocking condition.

Decision rationale:

Approval scope:

This decision does not authorize production deployment, unrestricted external publication, physical-vessel operation, certification or autonomous control.

Approver name:

Approval date:

Immutable approval record reference:
