---
Artifact-ID: OMSP-OPERATIONS-OBSERVABILITY-0001
Title: Operational Observability and Audit Model
Version: 0.1.0
Status: Review
Owner: OMSP Engineering Council
Approvers:
  - Accountable Maintainer
Created: 2026-07-10
Last-Updated: 2026-07-10
Sprint: Sprint-5
Work-Package: WP-0053
Traceability:
  - ISSUE-87
---

# Operational Observability and Audit Model

## Purpose

This model defines structured operational signals and audit evidence for the Sprint-5 OMSP toolchain. It makes quality-gate decisions and component outcomes traceable without granting automation operational, release or risk-acceptance authority.

## Event Contract

Events are newline-delimited JSON and contain:

- `schema_version`, `event_id` and `event_type`;
- `observed_at` and `correlation_id`;
- repository, source commit, workflow run and actor;
- severity and outcome;
- redacted diagnostic details and evidence references;
- an explicit `operational-evidence-only` authority label.

The implemented event types are `quality_gate.check.completed` and `quality_gate.decision.recorded`. Event identifiers are derived from canonical event content so equivalent inputs produce equivalent identifiers.

## Correlation and Traceability

One workflow execution uses one correlation identifier. Every event links to the repository, immutable source commit, GitHub Actions run and actor. Quality-gate component evidence digests are retained in event details. The audit stream must be append-only evidence and must not be manually rewritten to change an operational outcome.

## Health Model

The generated health record reports:

- `healthy` when the integrated quality gate passed;
- `degraded` when any blocking component failed;
- total and failed check counts;
- blocking failure names;
- the accountable signal owner and response expectation.

A health signal is diagnostic. It does not approve a merge, release, publication, deployment or residual-risk decision.

## Ownership and Response Expectations

The OMSP Engineering Council owns toolchain health definitions. A critical decision event or degraded health record requires accountable triage before release or external publication. The operator should preserve the failed workflow run, quality-gate report, audit stream and relevant component evidence before corrective work or rerun.

Repeated or unexplained nondeterministic failures are release blockers. Infrastructure failures may be rerun only after being classified and recorded; deterministic failures require a source correction.

## Privacy and Redaction

Audit evidence must not contain passwords, tokens, authorization headers, private keys or cloud access-key patterns. Sensitive key names are replaced with `[REDACTED]`, and recognized secret-like values are removed from free text. The audit stream should contain identifiers and minimum diagnostic context rather than full source documents, personal data or unrestricted command output.

Redaction reduces exposure risk but is not a substitute for secret prevention, repository-history scanning or access control.

## Retention

CI evidence is retained for 30 days by the workflow. Release, incident or approved-baseline evidence should be copied to the governed evidence store according to the applicable retention decision. Retention extensions require a documented purpose, owner and privacy review. Expired routine CI evidence may be removed without reusing event identifiers.

## Incident Evidence

For a suspected security, integrity or operational incident, preserve:

- source commit and workflow-run identifiers;
- correlation identifier and audit JSONL;
- health record and quality-gate report;
- component reports, package manifests and checksums;
- operator actions, reruns and disposition references.

Do not place secrets or unnecessary personal data in incident notes. Credential exposure requires rotation and access review outside this diagnostic workflow.

## Authority Boundary

Automation may emit events, calculate health, redact known patterns and retain evidence. It cannot declare the platform production-safe, approve an exception, close an incident, accept risk, authorize publication or approve release readiness. Those decisions remain with named accountable humans.

## Known Limitations

The MVP does not provide a remote log backend, metrics time series, distributed tracing, alert delivery, cryptographic log signing, legal-hold automation or comprehensive data-loss prevention. It observes the integrated quality gate only; broader production services require additional telemetry and ownership definitions.
