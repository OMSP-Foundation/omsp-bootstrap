---
Artifact-ID: OMSP-TEMPLATE-RISK-0001
Title: Risk Template
Version: 1.0.0
Status: Active
Owner: OMSP Engineering Council
Baseline: Sprint-6
Classification: Public
Related-Issue: WP-0071 / #191
---

# Risk Template

Copy the block below into a new governed risk record and replace every
`<placeholder>`. Risk identification and assessment method will be
standardized by ODS-500 (risk assessment standard); until ODS-500 is Active,
this template is the working format. Program-level residual risks use the
`RR-NNN` numbering already established (RR-001…RR-005).

```markdown
---
Artifact-ID: OMSP-RISK-<DOMAIN>-<NNNN>
Title: <short risk title>
Version: 0.1.0
Status: Draft
Owner: <accountable role or person>
Baseline: <sprint or baseline context>
Classification: Public
Related-Issue: WP-<XXXX> / #<NN>
---

# <Risk-ID>: <Risk title>

## 1. Risk Statement

<Condition → consequence form. Example: "If battery-bank capacity data is
entered without a source class, then scenario calculations may produce
plausible but wrong endurance figures.">

## 2. Context and Category

| Field | Value |
| --- | --- |
| Category | Technical / Operational / Safety / Governance / Schedule / Supply-chain |
| Affected artifacts | <paths or Artifact-IDs> |
| Threat/Error link | <TEM threat or error class, if applicable> |

## 3. Assessment

| Field | Value | Scale |
| --- | --- | --- |
| Likelihood | <1–5> | 1 rare … 5 almost certain |
| Impact | <1–5> | 1 negligible … 5 critical |
| Risk level | <L×I> | 1–6 low / 8–12 medium / 15–25 high |

## 4. Mitigation

- <Mitigation action 1 — with owning Work Package or issue>
- <Action 2>

## 5. Residual Risk

<What remains after mitigation, and why it is (or is not) acceptable.
Residual-risk acceptance is an accountable human decision — record who
accepted it and where (issue/PR/baseline note).>

## 6. Review

| Field | Value |
| --- | --- |
| Review trigger | <date, sprint, baseline, or event> |
| Last reviewed | <date> |
| Disposition | Open / Mitigated / Accepted / Closed |
```

Rules:

- Safety-category risks can never be closed by automation or AI assessment;
  closure requires accountable human review with evidence.
- A risk without a review trigger is incomplete — always set one.
