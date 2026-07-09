---
Artifact-ID: OMSP-REL-SPRINT1-VERSION-PROPOSAL-0001
Title: OMSP Sprint-1 Version Update Proposal
Version: 1.0.0
Status: Draft
Owner: OMSP Engineering Council
Baseline: Sprint-1
Classification: Public
Related-Issue: WP-0020 / #42
---

# OMSP Sprint-1 Version Update Proposal

## 1. Purpose

This document proposes the versioning approach for the Sprint-1 OMSP foundation baseline and release package.

It is a proposal only. It does not approve or publish a release.

## 2. Proposed Version

| Field | Proposed Value |
| --- | --- |
| Foundation Baseline | `Sprint-1` |
| Release Candidate | `v0.1.0-foundation-sprint-1` |
| Artifact Version Pattern | `1.0.0` for Sprint-1 governed foundation artifacts |
| Repository Tag | Proposed after human approval |
| Release Status | Draft pending human approval |

## 3. Rationale

Sprint-1 promotes foundational OMSP documents from bootstrap placeholders into governed v1.0 artifacts.

A release candidate version such as `v0.1.0-foundation-sprint-1` keeps repository-level maturity distinct from individual artifact maturity:

- artifact `1.0.0` means the artifact is ready as a governed foundation artifact;
- repository release `v0.1.0` means the overall platform foundation remains early and evolving;
- `foundation-sprint-1` identifies the release package scope.

## 4. Versioning Rules

- Governed artifact versions must be recorded in artifact metadata.
- Repository-level release tags must be created only after human approval.
- Draft release notes must not imply a published release.
- Baseline identifiers should remain stable once approved.
- Follow-up fixes after approval may require patch-level release notes or a new baseline decision.

## 5. Proposed Tagging Sequence

After human baseline and release approval:

1. Confirm all required Sprint-1 PRs are merged or explicitly deferred.
2. Confirm `develop` contains the approved baseline candidate.
3. Create baseline approval record update.
4. Create release tag, proposed: `v0.1.0-foundation-sprint-1`.
5. Publish release notes using the approved release package.

## 6. Open Questions

- Should repository-level releases use semantic versioning from the start?
- Should baseline identifiers and release tags always be separate?
- Should baseline approval produce a signed or manually approved record later?
- Should future release packages include generated traceability matrices?

## 7. Recommendation

Use `baseline:Sprint-1` as the baseline identifier and reserve `v0.1.0-foundation-sprint-1` as the release candidate tag pending human approval.

## 8. Maintenance

This proposal is maintained by the OMSP Engineering Council.

Material changes require issue-backed Work Package, reviewed pull request, version metadata update, and baseline update when applicable.
