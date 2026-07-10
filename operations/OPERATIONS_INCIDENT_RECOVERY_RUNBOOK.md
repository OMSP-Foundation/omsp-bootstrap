---
Artifact-ID: OMSP-OPERATIONS-RUNBOOK-0001
Title: Operations, Incident and Recovery Runbook
Version: 0.1.0
Status: Review
Owner: OMSP Engineering Council
Approvers:
  - Accountable Maintainer
Created: 2026-07-10
Last-Updated: 2026-07-10
Sprint: Sprint-5
Work-Package: WP-0055
Traceability:
  - ISSUE-89
---

# Operations, Incident and Recovery Runbook

## Purpose

This runbook defines routine operation, incident response, evidence preservation, rollback, recovery and post-incident expectations for the Sprint-5 OMSP toolchain. It applies to validation, generation, publication, security, quality-gate, observability and demonstrator workflows.

## Routine Operation

Before merge, publication or release preparation, confirm that the source commit is immutable, required checks are green, evidence artifacts are available, security warnings have accountable disposition and human approval requirements remain satisfied. Never replace a failed run with an undocumented rerun.

## Failure Classification

- **S1 Critical:** suspected credential exposure, unauthorized publication, evidence tampering, integrity loss or unsafe release decision. Stop affected workflows, preserve evidence and escalate immediately to the Accountable Maintainer and Security Owner.
- **S2 High:** deterministic required-check failure, repeated nondeterministic failure, corrupted package or unavailable recovery evidence. Block merge/release and assign Engineering Council triage.
- **S3 Moderate:** transient runner or external service failure with intact evidence and no integrity concern. Classify before rerun and retain both attempts.
- **S4 Low:** advisory warning, documentation defect or non-blocking observability gap. Track with owner and due date.

Automation may suggest a severity from evidence but cannot close an incident, accept risk or downgrade severity without accountable review.

## Incident Flow

1. Detect and record the source commit, workflow run, correlation ID, actor and affected artifact.
2. Contain by stopping publication, release or merge activity when integrity or security is uncertain.
3. Preserve quality-gate reports, audit JSONL, health records, manifests, checksums, logs and operator actions.
4. Classify severity and assign Incident Commander, Technical Lead, Communications Owner and Evidence Custodian.
5. Diagnose using deterministic reproduction where safe; do not modify preserved evidence.
6. Recover through source correction, rollback to a previously verified package, credential rotation or runner rerun as applicable.
7. Validate recovery with the integration demonstrator and required quality gate.
8. Obtain accountable approval before resuming publication, release or deployment-related activity.
9. Complete post-incident review and track corrective actions.

## Recovery Paths

### Deterministic Validation or Quality-Gate Failure

Correct the governed source, create a new commit and rerun all required checks. Do not rerun unchanged deterministic failures to obtain a different result.

### Transient Runner Failure

Record the infrastructure classification, preserve the failed attempt and rerun the failed workflow. Repeated transient classification requires S2 escalation.

### Publication Integrity Failure

Quarantine the package, compare manifest and checksum evidence, rebuild from the immutable source commit and publish only to preview until accountable approval. Approved packages are not edited in place.

### Security or Credential Incident

Stop affected workflows, revoke or rotate credentials, review access, preserve redacted evidence and inspect repository history outside this baseline workflow. Resume only after Security Owner approval.

### Rollback and Restore

Select the last verified immutable package and source commit, verify checksums and approval evidence, record the rollback decision and restore consumers to that package. Rollback does not erase the failed release or incident record.

### Disaster Recovery

Restore repository content from the authoritative Git history and reconstruct generated repositories, publication previews, security reports and audit evidence from documented inputs. Long-term artifact-store restoration remains an external operational dependency.

## Recovery Exercise

Run `python tooling/omsp_recovery_drill.py --source-commit "$(git rev-parse HEAD)"`. The drill executes the end-to-end demonstrator, verifies expected evidence, simulates a blocked incident state and writes a recovery record proving that the clean demonstrator can be rerun successfully. The drill is evidence only and cannot authorize production resumption.

## Service Expectations

S1 acknowledgement is immediate and release activity remains stopped. S2 requires same-day accountable triage. S3 should be classified before rerun. S4 requires an owner and planned disposition. These targets are governance expectations, not automated service-level guarantees.

## Communications

Incident communications must state impact, affected revisions, current containment, evidence location, owner and next decision point. Do not include secrets, unrestricted logs or unnecessary personal data. External statements require accountable approval.

## Post-Incident Review Template

Record incident ID, severity, timeline, detection source, impact, root cause, contributing conditions, containment, recovery, evidence references, decisions and approvers, lessons, corrective actions, owners and due dates. Reviews must distinguish confirmed facts from hypotheses.

## Authority Boundary

Automation may preserve evidence, run recovery drills and report readiness signals. It cannot declare recovery complete, close an incident, accept residual risk, approve rollback, authorize publication or certify production safety.

## Known Limitations

The runbook does not implement paging, remote log storage, credential rotation, repository-history scanning, production deployment rollback, legal hold, backup infrastructure or disaster-recovery hosting. Those capabilities require external systems and named operational owners.
