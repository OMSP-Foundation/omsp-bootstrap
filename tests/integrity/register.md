# Integrity Fixture Source Register (fictional)

Fictional mini source register for the WP-0083 / #204 model-integrity
fixtures (`tests/integrity/`, see `tests/integrity/README.md`). It uses
the same machine-consumed table structure as
`reference/HANSE_460_SOURCE_REGISTER.md` (§2.2 source entries, §4.3
inaccessible sources, §7 document-reference mapping) so that
`tooling/validate_model_integrity.py` parses it mechanically — nothing
is hard-coded. **All identifiers are fictional and carry no evidence
value.**

## 2.2 Register entries

| Source ID | Title | Owner | Class | Retrieved | Applicability |
| --- | --- | --- | --- | --- | --- |
| `source:fixture:itest:design-summary:2026-07-16` | Fictional design summary | Fictional designer | `sourced-secondary` | 2026-07-16 | Fictional itest configuration |
| `source:fixture:itest:vendor-datasheet:2026-07-16` | Fictional vendor datasheet | Fictional vendor | `sourced-manufacturer` | 2026-07-16 | Fictional vendor datasheet; fixture use only |

## 4.3 Capture attempts without access

| Attempted source | Location (text) | Result |
| --- | --- | --- |
| Fictional blocked vendor portal (`source:fixture:itest:blocked-portal:2026-07-16`) | fictional-portal.example (text, no link) | Login-gated in the fixture story; declared inaccessible |

## 7. Document-Reference Mapping

The row mapping `document:fixture:itest:blocked-manual:1.0` to the
inaccessible source deliberately violates mapping rule 3 of
`reference/HANSE_460_SOURCE_REGISTER.md` §7; the violation fires only
when an instance cites that document (negative fixture n7).

| Document ID | Register source ID |
| --- | --- |
| `document:fixture:itest:design-notes:1.0` | `source:fixture:itest:design-summary:2026-07-16` |
| `document:fixture:itest:blocked-manual:1.0` | `source:fixture:itest:blocked-portal:2026-07-16` |
