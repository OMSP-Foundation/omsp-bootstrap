---
Artifact-ID: OMSP-GOV-PLAYBOOK-0001
Title: OMSP Engineering Playbook
Version: 1.1.0
Status: Active
Owner: OMSP Engineering Council
Baseline: Sprint-1
Classification: Public
Related-Issue: WP-0012 / #34
---

# OMSP Engineering Playbook

## 1. Purpose

This playbook defines the official engineering lifecycle for OMSP Foundation repositories. It governs how work is planned, implemented, reviewed, merged, released, and baselined from Sprint-1 onward.

The playbook is intended to make engineering work:

- traceable from idea to baseline;
- reviewable before integration;
- consistent across repositories;
- compatible with AI-assisted development;
- safe for long-lived governance, release, and architecture artifacts.

## 2. Scope

This playbook applies to all OMSP Foundation repositories unless a repository-specific governance document explicitly extends it.

It covers:

- Work Package lifecycle;
- issue and sprint governance;
- branch and commit rules;
- pull request review and merge rules;
- baseline and release governance;
- documentation and traceability requirements;
- AI-assisted engineering boundaries.

## 3. Engineering Principles

OMSP engineering work follows these principles:

- **Knowledge First**: important decisions must be documented before they become implicit practice.
- **Model First**: architecture, lifecycle, and domain models guide implementation.
- **Artifact First**: durable artifacts are preferred over transient conversation or memory.
- **Evidence Driven**: changes must be supported by commits, PRs, reviews, checks, and links.
- **Review First**: work is not considered complete until it has passed the required review path.
- **Automation by Default**: repeatable validation should be automated where practical.
- **Traceability Always**: every meaningful change must be traceable to a Work Package, issue, PR, or baseline.

## 4. Core Terms

### 4.1 Work Package

A Work Package is a bounded unit of engineering work with a clear objective, deliverables, acceptance criteria, branch, and completion path.

A Work Package may produce code, documentation, governance artifacts, architecture artifacts, tests, CI changes, or release assets.

### 4.2 Issue

An issue is the authoritative planning and tracking record for a Work Package. It must describe the objective, deliverables, acceptance criteria, branch, target branch, and relevant labels.

### 4.3 Sprint

A sprint is a time-bounded execution window containing a selected backlog of Work Packages. A sprint must have a goal, scope, completion criteria, and release or baseline target.

### 4.4 Baseline

A baseline is an approved snapshot of repository state and governance artifacts. Baselines are created only after required Work Packages are merged and reviewed.

### 4.5 Release

A release is a packaged and communicated version of the system or repository. Releases may be created from baselines and must be traceable to the merged work that produced them.

## 5. Work Package Lifecycle

Every Work Package follows this lifecycle unless explicitly waived by the Engineering Council.

```text
Backlog
  ↓
Issue
  ↓
Feature Branch
  ↓
Implementation
  ↓
Focused Commits
  ↓
Draft Pull Request
  ↓
Self-Check
  ↓
Architecture / Governance Review
  ↓
Ready for Review → issue moves to Testing
  ↓
Testing Gate (omsp-tester) — fail returns to Implementation
  ↓
CTO Gate (omsp-cto) — TDD-compliance review
  ↓
Auto-Merge → develop
  ↓
Issue Closed
  ↓
Baseline / Release Update when applicable
```

### 5.1 Backlog

Backlog items may begin as ideas, risks, missing artifacts, or improvement requests. Before work starts, the item must be promoted into an issue with enough detail to guide execution.

### 5.2 Issue Creation

Each Work Package issue must include:

- objective;
- deliverables;
- acceptance criteria;
- source or motivation;
- branch name;
- target branch;
- labels;
- milestone when applicable.

### 5.3 Branch Creation

A feature branch must be created from the current target integration branch, normally `develop`.

Branch names must follow:

```text
feature/wp-xxxx-short-name
```

Example:

```text
feature/wp-0012-engineering-playbook-v1
```

### 5.4 Implementation

Implementation must stay within the Work Package scope. If material new scope is discovered, create or update an issue rather than silently expanding the branch.

### 5.5 Commit Discipline

Commits should be focused and reviewable. A Work Package should normally use a small number of meaningful commits rather than many noisy commits.

Commit messages must follow Conventional Commits.

Examples:

```text
docs(governance): promote engineering playbook to v1.0
ci(validation): add markdown validation workflow
chore(release): prepare v0.1.0-bootstrap
```

### 5.6 Pull Request Creation

A pull request must be opened before integration. PRs should start as Draft PRs unless the work is already complete and self-checked.

The PR body must include:

- summary;
- related issue;
- changed artifacts;
- validation evidence;
- acceptance criteria checklist;
- review notes or known limitations.

### 5.7 Self-Check

Before marking a PR ready for review, the author must verify:

- scope matches the issue;
- acceptance criteria are addressed;
- changed files are intentional;
- documentation is updated where required;
- CI or manual validation has been performed;
- no unrelated changes are included.

### 5.8 Review

Review must evaluate correctness, consistency, governance impact, and traceability. For governance or architecture artifacts, review must also check terminology, lifecycle alignment, and baseline impact.

Review is a two-stage gate:

1. **Testing Gate (omsp-tester).** Before the sprint starts, every sprint issue receives a test-scenario checklist (`<!-- omsp-test-checklist -->` comment). When a PR opens, the linked issue moves to the **Testing** status on the GitHub Project. The tester executes the checklist against the PR branch and issues an evidence-based verdict: **fail** → test-report comment + `gate:test-failed` label + issue returns to In Progress; **pass** → test-report comment + `gate:tester-approved` label + issue moves to In Review.
2. **CTO Gate (omsp-cto).** After the tester gate, the CTO reviews TDD compliance (test checklist existed before implementation, scenarios cover the acceptance criteria, evidence is genuine) plus architecture and governance impact, and applies `gate:cto-approved`.

### 5.9 Merge

Approved Work Packages merge into `develop` unless the issue explicitly defines a different target branch.

A PR carrying both `gate:tester-approved` and `gate:cto-approved` with all other checks green is merged automatically by the `approval-gate-merge` workflow. Merge authority for this test-gated path is explicitly delegated by the project owner (decision recorded in issue #212); the owner retains override at all times by removing a gate label, closing the PR, or disabling the workflow. All other merge paths remain human-only.

### 5.10 Closure

The related issue may be closed only after the PR is merged and traceability is preserved.

## 6. Branch Strategy

OMSP uses the following branch model:

- `main` is the protected release branch.
- `develop` is the integration branch.
- `feature/wp-xxxx-short-name` is used for Work Package implementation.
- `release/x.y.z` is used for release preparation.
- `hotfix/short-name` is used for urgent corrections.

### 6.1 `main`

`main` represents the stable release line. Direct commits to `main` are not allowed except by explicitly approved emergency governance procedure.

### 6.2 `develop`

`develop` is the integration branch for reviewed and approved work. Sprint work normally targets `develop`.

### 6.3 Feature Branches

Feature branches must be linked to a Work Package issue. They should be deleted after merge unless needed for audit or release operations.

### 6.4 Release Branches

Release branches stabilize a candidate release. Only release preparation, documentation, versioning, and approved fixes should occur on release branches.

### 6.5 Hotfix Branches

Hotfix branches are reserved for urgent production or governance corrections. Hotfix work must still preserve issue and PR traceability.

## 7. Pull Request Policy

Every meaningful change must be delivered through a pull request.

### 7.1 Required PR Metadata

Each PR must include:

- related issue number;
- summary of change;
- files or artifacts changed;
- validation performed;
- risk notes if applicable;
- acceptance criteria status.

### 7.2 Draft PRs

Draft PRs are used for early visibility and collaboration. A Draft PR may be incomplete, but it must not be merged.

### 7.3 Ready for Review

A PR may be marked Ready for Review only after the author completes the self-check and confirms that the branch is reviewable.

### 7.4 Review Expectations

Reviewers should check:

- alignment with issue scope;
- artifact quality and consistency;
- naming and lifecycle consistency;
- validation evidence;
- missing edge cases or governance gaps;
- whether baseline or release records must be updated.

### 7.5 Merge Rules

A PR may be merged only when:

- acceptance criteria are satisfied;
- required checks pass or are explicitly waived;
- required review is complete — for test-gated PRs this means both `gate:tester-approved` and `gate:cto-approved` labels (see 5.8–5.9);
- conflicts are resolved;
- target branch is correct;
- the PR preserves traceability to the issue.

### 7.6 Merge Method

The preferred merge method is the method configured by repository maintainers. When uncertain, use the repository default and preserve a clear PR title.

### 7.7 Post-Merge Actions

After merge:

- verify the issue can be closed;
- update sprint status;
- update baseline or release records if required;
- ensure follow-up work is captured as new issues.

## 8. Definition of Done

A Work Package is done only when:

- issue exists and describes the work;
- feature branch exists;
- implementation is committed;
- PR is opened;
- self-check is complete;
- review is complete;
- PR is merged into the target branch;
- related issue is closed;
- traceability is preserved;
- baseline or release artifacts are updated when applicable.

Documentation-focused Work Packages must also ensure that terminology, version metadata, and related governance artifacts are consistent.

## 9. Sprint Lifecycle

Each sprint has a defined backlog, completion criteria, and release or baseline target.

### 9.1 Sprint Planning

Sprint planning must identify:

- sprint goal;
- selected Work Packages;
- expected deliverables;
- target branch or release path;
- risks and dependencies;
- completion criteria.

### 9.2 Sprint Execution

During execution:

- work proceeds through issues and feature branches;
- progress is visible through issue and PR state;
- scope changes are recorded;
- blocked work is labeled or commented;
- governance changes are reviewed before merge.

### 9.3 Sprint Review

Sprint review confirms:

- which Work Packages merged;
- which acceptance criteria were satisfied;
- which items moved forward;
- which baseline or release actions are required;
- which follow-up issues must be opened.

### 9.4 Sprint Closure

A sprint may be closed when its required Work Packages are either completed, deferred, or explicitly removed from scope.

## 10. Baseline Management

Baselines are controlled snapshots of repository state.

### 10.1 Baseline Preconditions

A baseline may be created only when:

- required Work Packages are merged;
- governance and architecture artifacts are consistent;
- release notes or baseline notes are prepared if applicable;
- open risks are documented;
- approval is recorded by the appropriate human owner.

### 10.2 Baseline Naming

Baseline names should be stable and meaningful.

Examples:

```text
Sprint-0 Bootstrap Baseline
Sprint-1 Governance Baseline
v0.1.0-bootstrap
```

### 10.3 Baseline Authority

AI may help draft baseline content, validate consistency, and identify gaps. AI may not approve a baseline or override human governance decisions.

## 11. Release Governance

Releases must be traceable to reviewed and merged work.

A release must include:

- release identifier;
- source branch or tag;
- included Work Packages or PRs;
- notable changes;
- known limitations;
- approval or publication record.

Release branches must be kept narrow and should not become general development branches.

## 12. Labels and Milestones

Labels should make issue and PR state easy to understand.

Recommended label categories:

- work type: `documentation`, `governance`, `ci`, `architecture`, `bug`, `feature`;
- workflow state: `blocked`, `ready-for-review`, `needs-decision`;
- sprint: `sprint-0`, `sprint-1`, and future sprint labels;
- risk or priority where needed.

Milestones should group work by sprint, release, or baseline target.

## 13. Traceability Rules

Traceability must be preserved across the following chain:

```text
Issue → Branch → Commit(s) → Pull Request → Merge → Baseline/Release
```

Minimum traceability expectations:

- issue references branch name;
- branch name references Work Package ID where available;
- PR references issue number;
- commits use meaningful messages;
- baseline or release notes reference merged PRs or Work Packages.

## 14. Documentation Governance

Documentation is an engineering artifact and must be reviewed with the same discipline as code.

Documentation changes must check:

- metadata accuracy;
- version and status correctness;
- terminology consistency;
- relationship to existing governance artifacts;
- whether the change updates Sprint, baseline, or release behavior.

## 15. AI Assisted Development

AI may assist with:

- drafting issues;
- creating branch and PR content;
- drafting documentation;
- analyzing diffs;
- identifying inconsistencies;
- preparing review checklists;
- summarizing sprint or baseline state.

AI must not:

- approve baselines;
- approve releases;
- override human governance;
- silently expand scope;
- claim validation that was not performed;
- merge work without explicit human instruction.

AI-generated work must remain reviewable and traceable through normal engineering workflow.

## 16. Exceptions

Exceptions to this playbook must be explicit, documented, and approved by the appropriate human owner.

An exception record should include:

- what rule is being waived;
- why the exception is needed;
- duration or scope of the exception;
- risk and mitigation;
- approving owner.

## 17. Maintenance

This playbook is maintained by the OMSP Engineering Council.

Updates require:

- issue-backed Work Package;
- feature branch;
- PR into the appropriate target branch;
- review for governance consistency;
- version metadata update when the lifecycle changes materially.

Minor editorial corrections may update patch-level metadata. Material lifecycle changes must update minor or major version metadata according to governance impact.
