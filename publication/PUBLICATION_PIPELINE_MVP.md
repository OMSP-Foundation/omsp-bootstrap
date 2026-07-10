---
Artifact-ID: OMSP-PUBLICATION-PIPELINE-0001
Title: Documentation Publication Pipeline MVP
Version: 0.1.0
Status: Review
Owner: OMSP Engineering Council
Approvers:
  - Accountable Maintainer
Created: 2026-07-10
Last-Updated: 2026-07-10
Sprint: Sprint-5
Work-Package: WP-0050
Traceability:
  - ISSUE-84
---

# Documentation Publication Pipeline MVP

## Purpose

The MVP assembles deterministic OMSP publication packages from governed Markdown artifacts while preserving source identity, version and lifecycle status. It supports `preview`, `baseline` and `release` channels without allowing packaging automation to create approval authority.

## Package Structure

```text
package/
  manifest.json
  README.md
  artifacts/
  integrity/checksums.sha256
```

The manifest records package identity, channel, source repository and commit, approval evidence, artifact metadata, source paths and SHA-256 content digests.

## Channel Rules

- `preview` may include Proposed, Draft, Review or Active artifacts and is visibly labelled non-authoritative;
- `baseline` and `release` require an explicit `approval_evidence` reference;
- approved channels reject Proposed, Draft and Review artifacts;
- source lifecycle status is copied into the manifest and never rewritten by the pipeline.

## Execution

```bash
python tooling/omsp_publish.py tests/publication/preview-request.json build/publication-preview
python -m unittest tests/test_omsp_publish.py
```

## Integrity and Reproducibility

Artifacts are copied in stable path order. The manifest is emitted with sorted JSON keys, and `integrity/checksums.sha256` records every copied artifact plus the manifest. Equivalent repository content, request content and tool version produce equivalent package files.

The package is assembled in a temporary sibling directory and replaces the requested output only after successful validation and assembly. A failed build therefore does not partially modify the target package.

## Rollback and Deprecation

Published packages are immutable evidence records and should not be edited in place. Rollback means restoring a previously approved package reference or publishing a new corrective package with a new evidence record. Deprecation and retirement decisions must identify the affected package, reason, replacement or migration guidance, and accountable human decision reference.

## Authority Boundary

Successful assembly and checksum validation prove only that the implemented packaging rules passed. They do not approve content, create a baseline, authorize release, accept residual risk or authorize production deployment. Baseline and release authority remain with named accountable humans.

## Known Limitations

The MVP packages governed Markdown files only. It does not yet resolve the artifact registry, evaluate full dependency closure, sign packages, publish to an external target, generate archives, verify remote commits or manage package retention. External publication remains a separately authorized operation.
