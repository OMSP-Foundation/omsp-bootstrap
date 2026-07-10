---
Artifact-ID: OMSP-CICD-QUALITY-GATE-0001
Title: CI/CD Quality Gate Integration
Version: 0.1.0
Status: Review
Owner: OMSP Engineering Council
Approvers:
  - Accountable Maintainer
Created: 2026-07-10
Last-Updated: 2026-07-10
Sprint: Sprint-5
Work-Package: WP-0052
Traceability:
  - ISSUE-86
---

# CI/CD Quality Gate Integration

## Purpose

The integrated quality gate provides one stable pull-request check that executes the Sprint-5 validator, tests, repository generator, generated-output validation, publication preview and security baseline. It produces a deterministic evidence report while preserving human approval boundaries.

## Required Check Contract

The workflow job name is `quality-gate / required`. Repository administrators should configure this exact check as required for the protected `develop` branch. The workflow has read-only repository permissions and cannot merge, approve, publish externally, create releases or deploy.

## Blocking Checks

The integrated gate treats these checks as blocking:

- all Python unit tests;
- governed artifact validation;
- security and supply-chain blocking findings;
- repository generator execution;
- validation of generated repository output;
- publication preview assembly.

A non-zero exit code blocks the gate. Individual stdout, stderr, command, exit code and available evidence digests are retained in `quality-gate-report.json`.

## Advisory Findings

Advisory findings remain inside component reports, particularly security warnings for inherited tag-pinned actions or workflow-permission migration debt. A green integrated gate means no implemented blocking rule failed; it does not mean advisory findings were accepted or resolved.

## Evidence and Retention

Every workflow run uploads the complete `build/` directory as `quality-gate-evidence` for 30 days. The job summary exposes the decision, passed-check count and blocking check names. Evidence is traceable to the workflow run and source commit through GitHub Actions metadata.

## Approval Boundary

A passing quality gate cannot:

- approve or merge a pull request;
- waive required reviews;
- accept security or operational risk;
- approve a baseline or release;
- authorize external publication or production deployment.

Protected-branch review requirements and accountable human decisions remain separate from automation.

## Recovery and Rerun Guidance

For deterministic code or content failures, fix the source and push a new commit. For infrastructure or transient runner failures, rerun the failed job from GitHub Actions and retain both attempts. Do not bypass the required check, edit evidence manually or classify a deterministic failure as transient without review.

When a report is missing, inspect the failing step logs. When a component report exists, use its rule IDs, paths and messages to identify the corrective action. Repeated nondeterministic failures are release blockers until investigated.

## Branch and Release Gates

Pull requests into `develop` should require `quality-gate / required` plus accountable review. Release preparation must additionally confirm that advisory findings have approved dispositions, immutable source revision is selected, release scope is approved and WP-0056 readiness evidence is complete.

## Known Limitations

The MVP runs component checks sequentially and does not configure GitHub branch protection automatically. Evidence retention is limited to the configured Actions artifact period. External deployment environments, signed attestations, vulnerability databases and release approvals remain outside this workflow.
