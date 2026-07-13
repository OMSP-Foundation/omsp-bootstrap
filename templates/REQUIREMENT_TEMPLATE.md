---
Artifact-ID: OMSP-TEMPLATE-REQUIREMENT-0001
Title: Requirement Template
Version: 1.0.0
Status: Active
Owner: OMSP Engineering Council
Baseline: Sprint-6
Classification: Public
Related-Issue: WP-0071 / #191
---

# Requirement Template

Copy the block below into a new governed artifact, replace every
`<placeholder>`, and delete guidance comments. A requirement is a governed
statement of a necessary capability, behavior, quality, or constraint
(`OMSP-CONCEPT-REQUIREMENT`, a `Constraint` in the ontology). One artifact
may hold one requirement or a coherent set for a single subject.

```markdown
---
Artifact-ID: OMSP-REQ-<DOMAIN>-<NNNN>
Title: <short requirement title>
Version: 0.1.0
Status: Draft
Owner: <accountable role or person>
Baseline: <sprint or baseline context>
Classification: Public
Related-Issue: WP-<XXXX> / #<NN>
Traceability:
  - <upstream artifact or issue this derives from>
---

# <Requirement title>

## 1. Statement

<The requirement, one testable sentence using "shall".
Example: "The vessel model shall record every battery bank with
chemistry, nominal voltage, and rated capacity.">

## 2. Rationale

<Why this requirement exists; the operational or engineering need.>

## 3. Classification

| Field | Value |
| --- | --- |
| Type | Functional / Quality / Interface / Constraint / Safety |
| Priority | Must / Should / Could |
| MODS layer | <MODS Spec / MDS / Core Ops / VDM / Scenario Library / QRH — if applicable> |

## 4. Acceptance Criteria

- [ ] <Objective, checkable criterion 1>
- [ ] <Criterion 2>

## 5. Verification Method

<How conformance is demonstrated: Inspection / Analysis / Demonstration /
Test — and by which evidence artifact. Evidence links via the `verifies`
relation (Evidence → Requirement).>

## 6. Assumptions and Constraints

<Known assumptions, environmental limits, dependencies. Write "None known."
if empty — do not delete the section.>

## 7. Traceability

- Derives from: <vision/mission/standard/parent requirement>
- Constrains: <artifacts or models this requirement limits>
- Verified by: <evidence artifact(s), when they exist>
```

Rules:

- The statement must be singular and testable; split compound requirements.
- Safety-relevant requirements must reference
  `reference/DIGITAL_TWIN_GOVERNANCE_AND_SAFETY_BOUNDARIES.md` and never
  imply certification or seaworthiness authority.
- Status moves Draft → Review → Active through issue-backed review only.
