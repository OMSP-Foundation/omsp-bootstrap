---
Artifact-ID: OMSP-TEMPLATE-WORK-PACKAGE-0001
Title: Work Package Template
Version: 1.0.0
Status: Active
Owner: OMSP Engineering Council
Baseline: Sprint-6
Classification: Public
Related-Issue: WP-0071 / #191
---

# Work Package Template

Copy the block below into `planning/WP-<XXXX>-<SLUG>.md` when a Work Package
needs a governed definition beyond its GitHub issue (the issue remains the
tracking authority; this artifact records scope and traceability). Check the
highest existing WP number across issues, branches, and planning files before
assigning a new one — retired numbers (WP-0060–0068) are never reused.

```markdown
---
Artifact-ID: OMSP-PLANNING-WP-<XXXX>
Title: WP-<XXXX> <work package title>
Version: 0.1.0
Status: Draft
Owner: <accountable person>
Baseline: <sprint>
Classification: Public
Related-Issue: WP-<XXXX> / #<NN>
Traceability:
  - <upstream artifact or roadmap issue>
---

# WP-<XXXX> — <Title>

## 1. Objective

<One paragraph: what this WP achieves and why now.>

## 2. User Value

<Who benefits and how — the visible product outcome this enables.
Governance-only work needs an explicit justification here.>

## 3. Scope

Included:

- <item>

Out of scope:

- <item — with where it goes instead>

## 4. Deliverables

1. <artifact path or outcome>

## 5. Acceptance Criteria

- [ ] <criterion mapped to a deliverable>
- [ ] Validator and quality gate pass on changed paths.
- [ ] Human review and approval by the accountable owner.

## 6. Affected Artifacts

| Artifact | Change |
| --- | --- |
| <path> | New / Modified / Superseded / Deleted |

## 7. Evidence Produced

<What reviewable evidence this WP leaves behind: validator output, validation
records, disposition tables, demo output. Evidence is required for baseline
inclusion.>

## 8. Validation Plan

<How fitness-for-purpose will be judged (VALIDATION_FRAMEWORK §6), and by
whom.>

## 9. Risks and Notes

<Known risks with mitigations, or "None known." Reference RISK records for
material risks.>

## 10. Branch and Issue

- Branch: `feature/wp-<XXXX>-<slug>`
- Issue: #<NN>
```

Rules:

- A Work Package without `User Value` or `Evidence Produced` is incomplete —
  these two sections are the re-baseline gate for all post-audit work.
- Lifecycle: `Backlog → Issue → Branch → Commit → Draft PR → Review → Merge
  → Baseline Update` per `governance/ENGINEERING_PLAYBOOK.md`.
