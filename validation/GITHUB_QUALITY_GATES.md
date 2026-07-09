---
Artifact-ID: OMSP-VAL-GITHUB-QUALITY-GATES-0001
Title: OMSP GitHub Quality Gates
Version: 1.0.0
Status: Active
Owner: OMSP Engineering Council
Baseline: Sprint-1
Classification: Public
Related-Issue: WP-0019 / #41
---

# OMSP GitHub Quality Gates

## 1. Purpose

This document defines the practical GitHub quality gates used by OMSP documentation and repository governance work.

It connects GitHub workflows, PR checklist expectations, repository structure checks, validation evidence, and human review boundaries.

## 2. Scope

This quality gate set applies to:

- Markdown documentation changes;
- governed artifact changes;
- PR checklist completion;
- link validation;
- repository structure validation concepts;
- Sprint-1 documentation and governance work.

## 3. GitHub Quality Gate Model

The Sprint-1 GitHub quality gate model includes:

| Gate | Mechanism | Purpose |
| --- | --- | --- |
| Markdown Validation | `.github/workflows/markdown.yml` | Check Markdown quality and governed artifact front matter markers. |
| Link Check | `.github/workflows/link-check.yml` and `.lychee.toml` | Check Markdown links on PRs and pushes. |
| PR Checklist | `.github/PULL_REQUEST_TEMPLATE.md` | Make review expectations visible to authors and reviewers. |
| Repository Structure Concept | `validation/REPOSITORY_STRUCTURE_VALIDATION.md` | Define expected repository directories and structure checks. |
| Human Review | GitHub PR review and issue/PR comments | Preserve accountable review and approval boundaries. |

## 4. Markdown Validation Workflow

Markdown validation runs on pull requests and pushes to `develop` when Markdown files or Markdown workflow configuration changes.

It performs:

- Markdown linting;
- governed artifact YAML front matter smoke check for `canon/`, `governance/`, `architecture/`, and `validation/` directories.

The front matter smoke check is intentionally lightweight in Sprint-1. It checks whether governed Markdown artifacts start with YAML front matter markers. Future validation may enforce full metadata schema rules.

## 5. Link Check Workflow

Link check runs on pull requests and pushes to `develop` when Markdown files, link-check workflow configuration, or `.lychee.toml` changes.

It checks Markdown links using the repository link-check configuration.

The workflow also supports manual execution through `workflow_dispatch`.

## 6. PR Checklist Alignment

The PR template makes these expectations visible:

- linked issue;
- changed artifacts;
- acceptance criteria mapping;
- Markdown validation expectation;
- link check expectation;
- governed artifact metadata expectation;
- repository structure impact;
- validation or verification evidence;
- AI assistance boundary.

PR authors should complete the checklist honestly. Reviewers may use incomplete checklist items as review findings.

## 7. Repository Structure Validation Concept

Repository structure validation is documented as a concept rather than fully automated in Sprint-1.

The concept identifies expected top-level directories, required or optional files, and future automation opportunities.

Future automation should not invent missing structure or approve structural changes. It should report findings and leave final authority to human reviewers.

## 8. Quality Gate Outcomes

| Outcome | Meaning |
| --- | --- |
| Pass | Workflow/checklist item is satisfied. |
| Fail | Workflow/checklist item failed or is missing required evidence. |
| Deferred | Item is intentionally deferred with rationale and follow-up. |
| Not Applicable | Item does not apply to the PR. |

## 9. Evidence Rules

GitHub quality gate evidence may include:

- workflow run results;
- PR checklist entries;
- PR description;
- changed file list;
- reviewer comments;
- issue comments;
- follow-up issue references;
- baseline or release notes where applicable.

Evidence must be traceable and must not be invented after the fact.

## 10. AI Assistance Boundaries

AI may assist by:

- drafting PR checklist content;
- checking documentation structure;
- identifying missing metadata;
- summarizing workflow failures;
- suggesting follow-up issues.

AI must not:

- approve PRs as accountable authority;
- invent workflow results;
- override repository maintainers;
- declare baseline or release readiness;
- bypass human review.

## 11. Maintenance

This document is maintained by the OMSP Engineering Council.

Material changes require issue-backed Work Package, reviewed pull request, version metadata update, and baseline update when applicable.
