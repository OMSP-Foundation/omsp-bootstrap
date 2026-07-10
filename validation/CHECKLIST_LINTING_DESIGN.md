---
Artifact-ID: OMSP-VAL-CHECKLIST-LINTING-0001
Title: Validation Checklist Linting Design
Version: 1.0.0
Status: Active
Owner: OMSP Engineering Council
Baseline: Sprint-2
Related-Issue: WP-0028 / #56
---

# Validation Checklist Linting Design

## 1. Purpose

This design defines how OMSP validation checklists and readiness evidence can be linted consistently without transferring approval authority to automation.

## 2. Scope

Linting covers:

- checklist metadata;
- checklist item identity and outcome values;
- evidence references;
- applicability and exception handling;
- pull-request checklist completeness;
- baseline and release readiness checklist completeness;
- machine-readable lint findings.

Linting does not decide whether a system, artifact, baseline, or release is approved.

## 3. Checklist Model

Each governed checklist must declare:

- stable Artifact ID;
- title and version;
- status and owner;
- checklist type;
- related issue or work package;
- target artifact, baseline, release, or pull request;
- reviewer or accountable role;
- completion state.

Each checklist item must include:

- stable rule or item ID;
- requirement statement;
- applicability state;
- outcome;
- evidence reference when required;
- exception reference when waived or deferred;
- reviewer note for non-pass outcomes.

## 4. Outcome Vocabulary

Allowed outcomes are:

- `pass` — requirement satisfied with sufficient evidence;
- `fail` — requirement not satisfied;
- `not-applicable` — requirement does not apply and rationale is recorded;
- `deferred` — requirement remains open under an approved exception;
- `not-evaluated` — evaluation has not been completed.

`not-evaluated` cannot satisfy a baseline or release gate.

## 5. Lint Rule Families

### 5.1 Metadata Rules

- required metadata fields exist;
- Artifact ID format is valid;
- checklist type is recognized;
- owner and accountable role are explicit;
- target reference is resolvable.

### 5.2 Item Structure Rules

- item IDs are unique;
- outcome values use the controlled vocabulary;
- required text is non-empty;
- duplicate normative checks are rejected within one checklist.

### 5.3 Evidence Rules

- `pass` requires evidence when the rule is evidence-bearing;
- evidence references identify a repository artifact, CI run, review, decision, or external controlled record;
- broken or ambiguous references produce lint findings;
- evidence presence does not imply evidence adequacy.

### 5.4 Exception Rules

- `not-applicable` requires rationale;
- `deferred` requires an exception or decision reference, owner, and expiry/review point;
- waivers cannot be created implicitly by tooling;
- expired exceptions fail baseline and release readiness checks.

### 5.5 Pull Request Rules

- applicable PR checklist sections are present;
- changed governed artifacts identify related issues and validation evidence;
- unresolved required checklist items block readiness;
- automation reports completeness but does not approve the PR.

### 5.6 Baseline and Release Rules

- every required readiness section is evaluated;
- failed or not-evaluated release-gate items block readiness;
- deferred items require accountable approval references;
- checklist completion and human approval remain separate records.

## 6. Severity and Enforcement

| Severity | Meaning | Default effect |
| --- | --- | --- |
| `info` | advisory consistency signal | report only |
| `warning` | incomplete or weak evidence | report; may require review |
| `error` | rule violation | fail checklist lint |
| `gate` | baseline/release readiness violation | block readiness until resolved or explicitly approved |

Promotion from advisory to blocking enforcement requires a governed change to the rule registry.

## 7. Finding Contract

Each finding contains:

- rule ID;
- severity;
- checklist path;
- item ID when applicable;
- concise message;
- evidence or exception reference when relevant;
- remediation guidance;
- deterministic fingerprint for deduplication.

## 8. Human Accountability Boundary

Automation may parse, compare, validate structure, detect missing evidence, and generate reports. Accountable humans remain responsible for:

- judging evidence adequacy;
- accepting risk;
- approving exceptions;
- approving baselines;
- approving releases;
- approving material validation conclusions.

## 9. Implementation Path

1. Validate rule registry and result schema.
2. Add checklist parser for Markdown and future structured formats.
3. Run in advisory mode on pull requests.
4. Measure false positives and rule stability.
5. Promote selected rules to required gates through governance review.
6. Integrate results with Traceability Engine reports.
