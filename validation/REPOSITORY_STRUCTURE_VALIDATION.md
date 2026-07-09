---
Artifact-ID: OMSP-VAL-REPOSITORY-STRUCTURE-0001
Title: OMSP Repository Structure Validation
Version: 1.0.0
Status: Active
Owner: OMSP Engineering Council
Baseline: Sprint-1
Classification: Public
Related-Issue: WP-0019 / #41
---

# OMSP Repository Structure Validation

## 1. Purpose

This document defines the Sprint-1 repository structure validation concept for OMSP.

It describes expected repository structure, review expectations, and future automation opportunities.

## 2. Scope

This concept applies to the `OMSP-Foundation/omsp-bootstrap` repository and provides a pattern for future OMSP repositories.

It is intentionally concept-level in Sprint-1. It should guide reviews before strict automation is introduced.

## 3. Expected Top-Level Structure

| Path | Purpose | Status |
| --- | --- | --- |
| `.github/` | GitHub workflows, PR templates, and repository automation. | Required |
| `canon/` | Canon identity, mission, terminology, and ontology overview artifacts. | Required |
| `governance/` | Governance, engineering standards, decision and review policies. | Required |
| `architecture/` | Platform and architecture artifacts. | Required |
| `validation/` | Validation, verification, quality gates, readiness checklists, evidence examples. | Required |
| `README.md` | Repository entry point. | Recommended |

## 4. Governed Artifact Expectations

Governed Markdown artifacts in `canon/`, `governance/`, `architecture/`, and `validation/` should:

- start with YAML front matter;
- include an `Artifact-ID`;
- include `Title`, `Version`, `Status`, `Owner`, `Baseline`, `Classification`, and `Related-Issue` fields;
- use stable file names;
- preserve issue and PR traceability.

## 5. Workflow Expectations

GitHub workflows should:

- run on pull requests targeting `develop` where practical;
- run on pushes to `develop` where practical;
- use read-only permissions unless write access is required;
- expose validation expectations clearly;
- fail only when the check is mature enough to be actionable;
- document known limitations.

## 6. PR Template Expectations

The PR template should make repository quality gates visible by asking authors to document:

- summary;
- related issue;
- changed artifacts;
- acceptance criteria;
- quality gate expectations;
- validation or verification evidence;
- review focus areas;
- AI assistance boundaries.

## 7. Structure Review Checks

Reviewers should check:

- new files are placed in the right directory;
- new governed artifacts include metadata;
- workflow files belong under `.github/workflows/`;
- PR template changes belong under `.github/`;
- validation artifacts belong under `validation/`;
- examples are clearly marked as examples;
- future automation ideas are tracked as issues rather than hidden assumptions.

## 8. Future Automation Concept

Future repository structure validation automation may check:

- required top-level directories exist;
- governed Markdown files start with YAML front matter;
- required metadata fields are present;
- artifact IDs match the required pattern;
- PR templates contain required sections;
- workflow names and triggers follow repository expectations;
- example files are stored under explicit example directories.

Automation must report findings. It must not approve repository structure authority or override human review.

## 9. Evidence Rules

Repository structure evidence may include:

- changed file list;
- workflow results;
- PR checklist entries;
- reviewer comments;
- issue comments;
- follow-up issue references.

## 10. Maintenance

This concept is maintained by the OMSP Engineering Council.

Material changes require issue-backed Work Package, reviewed pull request, version metadata update, and baseline update when applicable.
