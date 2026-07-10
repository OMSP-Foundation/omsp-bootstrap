---
Artifact-ID: OMSP-GENERATOR-REPOSITORY-0001
Title: Repository Generator MVP
Version: 0.1.0
Status: Review
Owner: OMSP Engineering Council
Approvers:
  - Accountable Maintainer
Created: 2026-07-10
Last-Updated: 2026-07-10
Sprint: Sprint-5
Work-Package: WP-0049
Traceability:
  - ISSUE-83
---

# Repository Generator MVP

## Purpose

The MVP creates a small, deterministic OMSP repository skeleton from a versioned JSON profile. Generated governance content remains Draft and does not become authoritative without accountable human review.

## Input Profile

Required fields are `repository_name`, `title` and `owner`. `artifact_prefix` is optional. Repository names must be lowercase and filesystem-safe.

## Generated Structure

- `README.md`;
- `governance/GOVERNANCE.md`;
- `planning/README.md`;
- `validation/README.md`;
- `.omsp/repository-profile.json`;
- `.gitignore`.

## Execution

```bash
python tooling/omsp_generate_repo.py tests/generator/repository-profile.json build/example --dry-run
python tooling/omsp_generate_repo.py tests/generator/repository-profile.json build/example --report build/generator-report.json
python -m unittest tests/test_omsp_generate_repo.py
python tooling/omsp_validate.py build/example
```

## Safety and Overwrite Rules

Dry-run is side-effect free. Existing files with different content are marked `blocked`; write mode refuses the entire operation before changing files. `--force` permits explicit overwrite. Identical files are reported as `unchanged`.

## Reproducibility

Templates are embedded in the versioned generator. Paths and file ordering are deterministic. Given the same profile and generator version, generated file content is equivalent.

## Validation Boundary

Generated output should be checked by the OMSP validator, but successful generation or validation does not approve governance, baseline, release, security, operational use or production readiness.

## Known Limitations

The MVP provides one built-in repository profile and does not yet support external template packs, schema evaluation, license selection, Git initialization, remote repository creation, secret provisioning, plugin execution or migrations. `--force` is intentionally explicit and should be used only after reviewing the dry-run report.
