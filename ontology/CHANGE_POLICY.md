---
Artifact-ID: OMSP-ONTOLOGY-CHANGE-POLICY-0001
Title: Ontology Change Policy
Version: 1.0.0
Status: Active
Owner: OMSP Engineering Council
Baseline: Sprint-2
Related-Issue: WP-0023 / #49
---

# Ontology Change Policy

## Change Classes

- **Additive:** adds a new concept or relation without changing existing meaning.
- **Compatible refinement:** clarifies an existing definition without changing valid prior use.
- **Deprecation:** keeps an identity addressable while prohibiting new use.
- **Breaking:** changes identity, meaning, domain, range or constraints in a way requiring migration.

## Required Change Evidence

Every material change must record the issue, affected IDs, compatibility class, impacted artifacts, migration guidance, validation results and accountable review decision.

## Lifecycle Rules

Ontology identities are never silently reassigned. Deprecated identities remain in the registry with replacement guidance. Retirement requires proof that active repository and downstream references have migrated.

## Authority Boundary

Automated validation may detect malformed identifiers, missing references, duplicate identities and invalid relation endpoints. Semantic approval and baseline authority remain human governance decisions.
