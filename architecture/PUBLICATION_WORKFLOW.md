---
Artifact-ID: OMSP-ARCH-PUBLICATION-WORKFLOW-0001
Title: OMSP Publication Engine Workflow
Version: 1.0.0
Status: Active
Owner: OMSP Engineering Council
Baseline: Sprint-2
Classification: Public
Related-Issue: WP-0027 / #54
---

# OMSP Publication Engine Workflow

## 1. Purpose

This artifact defines how governed OMSP artifacts become preview, baseline, or release publication packages without changing their governance status or bypassing accountable human approval.

## 2. Publication Principles

- Publication is packaging and distribution, not approval.
- Source artifact status remains authoritative.
- Draft and Review content must never appear as approved baseline or release content.
- Every package must be reproducible from a repository commit.
- Every included artifact must retain Artifact ID, version, status, provenance, and integrity metadata.

## 3. Publication Channels

| Channel | Eligible source status | Authority meaning | Human approval required |
| --- | --- | --- | --- |
| Preview | Proposed, Draft, Review, Active | Non-authoritative evaluation output | No, but must be labelled preview |
| Baseline | Active and explicitly baselined | Controlled approved snapshot | Yes |
| Release | Active and included in approved release scope | Versioned public distribution | Yes |

## 4. Workflow

```text
Discover candidates
  -> validate metadata and traceability
  -> classify publication channel
  -> resolve dependencies
  -> assemble package manifest
  -> generate package
  -> validate integrity and status labels
  -> human readiness review
  -> publish to approved channel
  -> record publication evidence
```

## 5. Candidate Discovery

The Publication Engine may discover artifacts through repository paths, registries, baseline manifests, or release scope declarations. Discovery does not imply eligibility.

Each candidate must expose:

- Artifact ID;
- version;
- lifecycle status;
- owner;
- source path and commit;
- dependency references;
- publication classification.

## 6. Eligibility Rules

### 6.1 Preview

Preview packages may include non-Active artifacts only when each output visibly carries `Publication-Channel: Preview` and the original lifecycle status.

### 6.2 Baseline

Baseline packages may include only artifacts listed in an approved baseline manifest. A successful automated check cannot create baseline authority.

### 6.3 Release

Release packages require an approved release scope, immutable version identifier, release notes, integrity data, and accountable human release approval.

## 7. Package Structure

```text
package/
  manifest.json
  README.md
  artifacts/
  evidence/
  integrity/
    checksums.sha256
```

The manifest is the authoritative package inventory. Generated navigation or rendered documents are derivative views.

## 8. Status Preservation

Publication must not rewrite `Draft`, `Review`, or `Active` into a stronger governance status. Package channel and artifact lifecycle status are separate fields.

## 9. Dependency Handling

Dependencies are classified as:

- included;
- external reference;
- excluded with rationale;
- unresolved blocker.

A baseline or release package must fail readiness validation when a required dependency is unresolved.

## 10. Publication Evidence

Publication evidence records must include source commit, manifest hash, validation report, channel, target, timestamp, tool version, and human approval reference when required.

## 11. Failure and Recovery

Failed assembly or validation must not modify an approved publication target. Republish operations must use a new evidence record and preserve previous package history.

## 12. Human Authority Boundary

Automation may assemble, validate, compare, and publish after authorization. It cannot approve a baseline, authorize a release, or decide that unresolved governance findings are acceptable.
