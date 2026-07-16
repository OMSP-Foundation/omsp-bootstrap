---
Artifact-ID: OMSP-EXAMPLE-MARITIME-SAMPLE-REGISTER-0001
Title: Maritime Sample Fictional Source Register
Version: 0.1.0
Status: Draft
Owner: toss-cengiz
Baseline: Sprint-8
Classification: Public
Related-Issue: WP-0083 / #204
Depends-On:
  - OMSP-EXAMPLE-MARITIME-SAMPLE-0001
Traceability:
  - ISSUE-204
  - OMSP-PLANNING-GOLDEN-PATH-0001
---

# Maritime Sample Fictional Source Register

## 1. Purpose and fictionality declaration (binding)

This register exists so that the fictional sample package of
`examples/maritime-sample/` passes the **same** mechanical
model-integrity validation (`tooling/validate_model_integrity.py`,
WP-0083 / #204) as the real Hanse 460 model — with no special-case code
and no emptied check. It mirrors the machine-consumed table structure of
`reference/HANSE_460_SOURCE_REGISTER.md` (§2.2 source entries and the §7
document-reference mapping).

**Every entry in this register is fictional.** The `source:fixture:*`
and `document:fixture:*` identifiers below exist only to exercise the
validators; they name no real publication, vendor, document or vessel
and carry **no evidence value**. Nothing here supports any engineering,
safety or certification claim (see the package README §2).

## 2. Source Record

### 2.2 Register entries

| Source ID | Title | Owner | Class | Retrieved | Applicability |
| --- | --- | --- | --- | --- | --- |
| `source:fixture:design-summary:2026-07-14` | Fictional design summary | Fictional designer | `sourced-secondary` | 2026-07-14 | Fictional example-yacht sample configuration |
| `source:fixture:storage-datasheet:2026-07-14` | Fictional storage datasheet | Fictional vendor | `sourced-manufacturer` | 2026-07-14 | Fictional storage datasheet; sample use only |
| `source:fixture:panel-datasheet:2026-07-14` | Fictional panel datasheet | Fictional vendor | `sourced-manufacturer` | 2026-07-14 | Fictional panel datasheet; sample use only |
| `source:fixture:tank-datasheet:2026-07-14` | Fictional tank datasheet | Fictional vendor | `sourced-manufacturer` | 2026-07-14 | Fictional tank datasheet; sample use only |
| `source:fixture:pump-datasheet:2026-07-14` | Fictional pump datasheet | Fictional vendor | `sourced-manufacturer` | 2026-07-14 | Fictional pump datasheet; sample use only |

No source locations are recorded: fictional sources have none.

## 4.3 Capture attempts without access

None — the fictional package declares no inaccessible sources.

## 7. Document-Reference Mapping

The mapping rules of `reference/HANSE_460_SOURCE_REGISTER.md` §7 apply
unchanged (single-source rule; they are not repeated here).

| Document ID | Register source ID |
| --- | --- |
| `document:fixture:electrical-notes:1.0` | `source:fixture:design-summary:2026-07-14` |
| `document:fixture:freshwater-notes:1.0` | `source:fixture:design-summary:2026-07-14` |
