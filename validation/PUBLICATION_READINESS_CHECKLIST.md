---
Artifact-ID: OMSP-VAL-PUBLICATION-READINESS-0001
Title: Publication Readiness Checklist
Version: 1.0.0
Status: Active
Owner: OMSP Engineering Council
Baseline: Sprint-2
Classification: Public
Related-Issue: WP-0027 / #54
---

# Publication Readiness Checklist

## Package Identity

- [ ] Package ID and version are unique.
- [ ] Publication channel is explicitly declared.
- [ ] Source repository and immutable commit are recorded.
- [ ] Manifest validates against `schemas/publication-package.schema.json`.

## Artifact Eligibility

- [ ] Every included artifact has Artifact ID, version, status and source path.
- [ ] Preview artifacts retain visible non-authoritative labelling.
- [ ] Baseline artifacts are included by an approved baseline manifest.
- [ ] Release artifacts are included by an approved release scope.
- [ ] Superseded, Deprecated or Retired artifacts are excluded or explicitly justified.

## Dependencies and Traceability

- [ ] Required dependencies are included or resolvable as external references.
- [ ] Exclusions have rationale.
- [ ] No unresolved required dependency remains.
- [ ] Validation and traceability reports are attached.

## Integrity and Reproducibility

- [ ] Package can be regenerated from the recorded commit.
- [ ] Manifest and artifact checksums are generated.
- [ ] Generated navigation matches the manifest inventory.
- [ ] Tool versions and generation timestamp are recorded.

## Approval Boundary

- [ ] Preview output is not represented as approved.
- [ ] Baseline publication has an accountable human approval reference.
- [ ] Release publication has an accountable human release approval reference.
- [ ] Automated success is not used as approval evidence by itself.

## Publication and Recovery

- [ ] Target channel and destination are correct.
- [ ] Existing approved output is not overwritten without governed versioning.
- [ ] Rollback or withdrawal procedure is documented.
- [ ] Publication evidence record will be retained.
