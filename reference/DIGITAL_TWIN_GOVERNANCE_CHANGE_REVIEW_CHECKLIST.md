# Digital Twin Governance Change and Review Checklist

- Artifact ID: `OMSP-REFERENCE-TWIN-GOVERNANCE-VALIDATION-0001`
- Version: `0.1.0`
- Status: `review`

## Authority and scope

- [ ] Artifact type and authority class are explicit.
- [ ] Approval status is explicit.
- [ ] Accountable human role is identified.
- [ ] Repository acceptance is not presented as operational authorization.
- [ ] Configuration, observation, state, and derived-value authority remain distinct.

## Safety boundaries

- [ ] Output cannot reasonably be mistaken for a certified instruction.
- [ ] Approved procedures remain external authorities unless explicitly controlled.
- [ ] Stop-use and escalation conditions are documented.
- [ ] Missing, stale, conflicted, and indeterminate data remain visible.
- [ ] Human override and disposition remain explicit.
- [ ] No vessel-control or autonomous-command capability is implied.

## AI assistance

- [ ] AI-assisted content is identifiable where material.
- [ ] Evidence and assumptions remain traceable.
- [ ] Generated or simulated data is labeled.
- [ ] Restricted AI outputs received human review.
- [ ] AI did not approve configuration, resolve safety-critical ambiguity, or issue commands.

## Change impact

- [ ] Initiating issue and reason are recorded.
- [ ] Affected artifacts, identifiers, and dependencies are listed.
- [ ] Semantic compatibility impact is assessed.
- [ ] Authority and safety impact is assessed.
- [ ] Migration, supersession, or rollback path is documented.
- [ ] Historical evidence remains reproducible.
- [ ] Versioning is appropriate for the change.

## Review depth

- [ ] Change is classified as editorial, model, safety-relevant, or implementation-critical.
- [ ] Reviewer independence matches the risk class.
- [ ] Safety-relevant changes have explicit disposition.
- [ ] Implementation-critical changes include separate system assurance evidence.
- [ ] Unresolved interoperability or safety defects are treated as failures.

## Presentation and provenance

- [ ] Authority, source, time, quality, and freshness are visible.
- [ ] Conflicts and limitations are not hidden by summaries or confidence scores.
- [ ] Derived values list inputs, method version, assumptions, and execution time.
- [ ] Corrections preserve original evidence and audit history.
- [ ] Consumer-facing language is advisory where authority is advisory.

## Acceptance result

Record one result for every applicable item:

- `pass`
- `fail`
- `indeterminate`
- `not-applicable`

Merge requires all mandatory authority-separation, provenance, human-accountability, AI-boundary, and safety-presentation items to pass. A disclaimer cannot convert a known defect into a pass.
