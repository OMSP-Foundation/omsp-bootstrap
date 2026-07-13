---
Artifact-ID: OMSP-TEMPLATE-VALIDATION-0001
Title: Validation Record Template
Version: 1.0.0
Status: Active
Owner: OMSP Engineering Council
Baseline: Sprint-6
Classification: Public
Related-Issue: WP-0071 / #191
---

# Validation Record Template

Copy the block below to record a validation of governed work, following
`validation/VALIDATION_FRAMEWORK.md` (`OMSP-VAL-VALIDATION-0001`).
Validation asks "did we build the right thing"; verification evidence
("did we build it correctly") is referenced, not repeated.

```markdown
---
Artifact-ID: OMSP-VAL-RECORD-<NNNN>
Title: <validation record title>
Version: 0.1.0
Status: Draft
Owner: <accountable reviewer>
Baseline: <sprint or baseline context>
Classification: Public
Related-Issue: WP-<XXXX> / #<NN>
---

# Validation Record: <target>

## 1. Target and Intended Use

| Field | Value |
| --- | --- |
| Validated artifact(s) | <paths or Artifact-IDs> |
| Work Package | WP-<XXXX> / #<NN> |
| Intended use | <what downstream work relies on this> |

## 2. Validation Checks

Per VALIDATION_FRAMEWORK §6 — state a finding for each check:

| Check | Finding |
| --- | --- |
| Intent alignment | <supports the WP objective and mission? evidence> |
| Downstream usability | <usable without ambiguous interpretation?> |
| Governance alignment | <authority, review, AI boundaries respected?> |
| Architecture alignment | <no conflicting component boundaries?> |
| Knowledge-first alignment | <explicit, modelable, traceable, reusable?> |
| Evidence sufficiency | <enough evidence for acceptance?> |
| Risk and exception visibility | <limitations and follow-ups documented?> |

## 3. Verification Evidence Referenced

- <validator output, CI run, review record — links or paths>

## 4. Outcome

| Field | Value |
| --- | --- |
| Outcome | Validated / Validated with Exceptions / Not Validated / Deferred |
| Exceptions | <list, or "None"> |
| Follow-up issues | <#NN references, or "None"> |

## 5. Accountability

<Named human reviewer and date. AI may have assisted with analysis and
consistency checks but did not approve this outcome.>
```

Rules:

- An outcome of `Validated with Exceptions` requires every exception to have
  a follow-up reference or an explicit acceptance note.
- Scenario Library entries must reach `Validated` before any QRH item may
  derive from them.
