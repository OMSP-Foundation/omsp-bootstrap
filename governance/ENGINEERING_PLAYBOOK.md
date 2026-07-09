---
Artifact-ID: OMSP-GOV-PLAYBOOK-0001
Title: OMSP Engineering Playbook
Version: 0.1.0
Status: Draft
Owner: OMSP Engineering Council
Baseline: Sprint-0
Classification: Public
---

# OMSP Engineering Playbook

## 1. Purpose

This playbook defines the official engineering workflow for OMSP Foundation repositories.

## 2. Engineering Principles

- Knowledge First
- Model First
- Artifact First
- Evidence Driven
- Review First
- Automation by Default

## 3. Work Package Lifecycle

```text
Backlog
  ↓
Issue
  ↓
Feature Branch
  ↓
Implementation
  ↓
1–3 Commit
  ↓
Draft Pull Request
  ↓
Architecture Review
  ↓
Ready for Review
  ↓
Approval
  ↓
Merge → develop
  ↓
Issue Closed
  ↓
Baseline Update
```

## 4. Branch Strategy

- `main` is the protected release branch.
- `develop` is the integration branch.
- Feature work uses `feature/wp-xxxx-short-name`.
- Release work uses `release/x.y.z`.
- Hotfix work uses `hotfix/short-name`.

## 5. Commit Convention

OMSP uses Conventional Commits.

Examples:

```text
docs(governance): establish OMSP engineering playbook
ci(validation): add markdown validation workflow
chore(release): prepare v0.1.0-bootstrap
```

## 6. Pull Request Policy

Every change must be delivered through a pull request. Pull requests begin as Draft PRs and become Ready for Review after self-check.

## 7. Definition of Done

A Work Package is done only when:

- Issue exists.
- Feature branch exists.
- Implementation is committed.
- Draft PR is opened.
- Review is complete.
- PR is merged into `develop`.
- Related issue is closed.
- Traceability is preserved.

## 8. Sprint Lifecycle

Each sprint has a defined backlog, completion criteria, and release target. Sprint-0 establishes the bootstrap foundation.

## 9. Baseline Management

Baselines are created only after all required Work Packages are merged and reviewed.

## 10. AI Assisted Development

AI may draft, analyze, review, and validate artifacts. AI may not approve baselines or override human governance.
