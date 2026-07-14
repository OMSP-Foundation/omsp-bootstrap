---
Artifact-ID: OMSP-TEMPLATE-ADR-0001
Title: Architecture Decision Record Template
Version: 1.0.1
Status: Active
Owner: OMSP Engineering Council
Baseline: Sprint-6
Classification: Public
Related-Issue: WP-0071 / #191
---

# Architecture Decision Record (ADR) Template

Copy the block below for every material technology, format, tool, or
structure decision. Docs-as-code rule: such decisions are not made without
an ADR. ADRs are `Decision` artifacts in the ontology and live in
`governance/` as `ADR-NNNN-<slug>.md` (example:
`governance/ADR-0001-REPOSITORY-TOPOLOGY.md`).
Before assigning a number, check the highest existing ADR number across
`governance/` and open PR branches, and take the next one — parallel work
streams once produced two ADR-0003s (#240).

```markdown
---
Artifact-ID: OMSP-GOV-ADR-<NNNN>
Title: ADR-<NNNN> <decision title>
Version: 1.0.0
Status: Draft
Owner: OMSP Foundation Governance
Baseline: <sprint or baseline context>
Classification: Public
Related-Issue: WP-<XXXX> / #<NN>
---

# ADR-<NNNN>: <Decision title>

## Status

<Draft / Accepted (by whom, date) / Superseded by ADR-<NNNN>.
Acceptance is always an accountable human record.>

## Context

<The problem, the forces at play, and the options considered — including
the ones rejected. State the decision criteria explicitly.>

## Decision

<The decision, in one or two sentences, active voice. Include re-evaluation
triggers if the decision is conditional.>

## Consequences

<Positive outcomes, accepted costs and risks, and what becomes easier or
harder. Note migration implications if the decision is later reversed.>

## Alternatives Considered

- <Option B — why rejected>
- <Option C — why rejected>
```

Rules:

- One decision per ADR; a new decision on the same subject supersedes the
  old ADR (set `Superseded-By` metadata on the old record) rather than
  editing it.
- ADR numbering is sequential and never reused.
