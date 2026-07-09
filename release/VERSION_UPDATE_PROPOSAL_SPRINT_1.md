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
| Preferred Release Candidate Tag | `v0.1.0-foundation-sprint-1` |
| Short Release Tag Option | `v0.1.0` |
| Artifact Version Pattern | `1.0.0` for Sprint-1 governed foundation artifacts |
| Repository Tag | Proposed after human approval |
| Release Status | Draft pending human approval |

## 3. Rationale

Sprint-1 promotes foundational OMSP documents from bootstrap placeholders into governed v1.0 artifacts.

A release candidate version such as `v0.1.0-foundation-sprint-1` keeps repository-level maturity distinct from individual artifact maturity:

- artifact `1.0.0` means the artifact is ready as a governed foundation artifact;
- repository release `v0.1.0` means the overall platform foundation remains early and evolving;
- `foundation-sprint-1` identifies the release package scope.

## 4. Tag Format Options

| Option | Example | Pros | Cons | Recommendation |
| --- | --- | --- | --- | --- |
| Descriptive foundation tag | `v0.1.0-foundation-sprint-1` | Explicitly identifies scope and sprint baseline. | Longer tag name. | Preferred for first foundation release. |
| Short semantic tag | `v0.1.0` | Simple and conventional. | Less explicit about foundation/sprint scope. | Acceptable if release notes and baseline record carry full context. |

## 5. Versioning Rules

- Governed artifact versions must be recorded in artifact metadata.
- Repository-level release tags must be created only after human approval.
- Draft release notes must not imply a published release.
- Baseline identifiers should remain stable once approved.
- Follow-up fixes after approval may require patch-level release notes or a new baseline decision.
- If a short semantic tag is selected, release notes must explicitly identify the Sprint-1 foundation baseline scope.

## 6. Proposed Tagging Sequence

After human baseline and release approval:

1. Confirm all required Sprint-1 PRs are merged or explicitly deferred.
2. Confirm `develop` contains the approved baseline candidate.
3. Create baseline approval record update.
4. Select final repository tag:
   - preferred: `v0.1.0-foundation-sprint-1`;
   - alternative: `v0.1.0`.
5. Create the approved release tag.
6. Publish release notes using the approved release package.

## 7. Open Questions

- Should repository-level releases use semantic versioning from the start?
- Should baseline identifiers and release tags always be separate?
- Should baseline approval produce a signed or manually approved record later?
- Should future release packages include generated traceability matrices?
- Should the first release optimize for descriptive traceability or shorter semantic-version convention?

## 8. Recommendation

Use `baseline:Sprint-1` as the baseline identifier.

Use `v0.1.0-foundation-sprint-1` as the preferred first release tag because it is explicit and traceable.

Use `v0.1.0` only if human release reviewers prefer a shorter semantic-version tag and confirm that release notes and baseline records carry the Sprint-1 foundation context.

## 9. Maintenance

This proposal is maintained by the OMSP Engineering Council.

Material changes require issue-backed Work Package, reviewed pull request, version metadata update, and baseline update when applicable.
