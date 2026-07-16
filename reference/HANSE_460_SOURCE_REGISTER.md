---
Artifact-ID: OMSP-REFERENCE-SOURCE-0001
Title: Hanse 460 Reference Source Register
Version: 0.3.0
Status: Review
Owner: OMSP Engineering Council
Approvers:
  - Accountable Maintainer
Created: 2026-07-10
Last-Updated: 2026-07-16
Sprint: Sprint-9
Work-Package: WP-0092
Traceability:
  - ISSUE-74
  - ISSUE-202
  - ISSUE-253
  - EPIC-172
  - OMSP-REFERENCE-CONFIG-0001
  - OMSP-PLANNING-GOLDEN-PATH-0001
---

# Hanse 460 Reference Source Register

## 1. Purpose

This register records the evidence context used by the Hanse 460 reference
configuration and the golden-path electrical slice. It prevents secondary
data, inaccessible manufacturer pages and unverified assumptions from being
represented as controlled design facts.

Version 0.2.0 extends the register for WP-0081 (Sprint-8): source capture for
the golden-path input classes (`OMSP-PLANNING-GOLDEN-PATH-0001` §4.1–§4.2),
authority-class coverage declarations, and the document-reference mapping
convention consumed by downstream model validation (WP-0083).

Version 0.3.0 (WP-0092, Sprint-9, issue #253) captures the **owner-held
Hanse 460 document set** made available on 2026-07-16 as a local archive:
the factory electrical circuit-diagram and wiring-harness drawings, the
Owner's Manual 460 V11 (EN), the H460.25 EU specification (2025) and the
core electrical vendor manuals of the golden-path slice. This is a
**register-capture-only** change: document identities, extraction
locations and conflict assessments are recorded here; transcription of
technical values into the instance models (`reference/hanse460/`) is
downstream work and has deliberately not been performed. Per §5, the
copyrighted documents themselves are **not** copied into the repository;
only identity and location metadata are recorded.

## 2. Source Record

### 2.1 Class vocabulary

The `Class` column uses the `authority_class` vocabulary of
`schemas/provenance.schema.json` verbatim: `reference`,
`sourced-secondary`, `sourced-manufacturer`, `verified-design`,
`verified-as-built`. No other spelling (including the pre-0.2.0 shorthand
`Secondary`) is valid in this register. `unknown` is a value status, not a
source class: a source entry is never classified `unknown`; instead, an
inaccessible source produces an explicit declaration in §4.3 and the
affected values remain `unknown`.

Source IDs follow the machine contract
`^source:[a-z0-9][a-z0-9:._-]*$` (`schemas/provenance.schema.json`,
`source_id`).

### 2.2 Register entries

| Source ID | Title | Owner | Class | Retrieved | Applicability |
| --- | --- | --- | --- | --- | --- |
| `source:secondary:wikipedia:hanse-brand:2026-07-10` | Hanse (yacht brand) | Wikipedia contributors | `sourced-secondary` | 2026-07-10 | Hanse 460 design-family summary |
| `source:secondary:wikipedia:hanse-brand:2026-07-15` | Hanse (yacht brand) — re-verification | Wikipedia contributors | `sourced-secondary` | 2026-07-15 | Re-verification of the 2026-07-10 capture; page last edited 2024-05-27; no change to previously transcribed values |
| `source:manufacturer:hanseyachts-com:hanse-460-product-page:2026-07-15` | Hanse 460 — The 46 foot sailboat from Hanse (product page) | HanseYachts AG | `sourced-manufacturer` | 2026-07-15 | Hanse 460 design family, marketing-level claims only; page offers no technical documents ("No documents found") |
| `source:manufacturer:hanseyachts-com:hanse-460-historical-page:2026-07-15` | Hanse 460 2021-2026 (historical models page) | HanseYachts AG | `sourced-manufacturer` | 2026-07-15 | Hanse 460 design family; model production span; marketing-level claims only; no technical documents offered |
| `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` | Hanse 460 Specification and Pricelist (US market, valid from 2021.11.12) | New Wave Yachts (dealer-hosted copy of a HanseYachts AG document) | `sourced-secondary` | 2026-07-15 | Hanse 460 US-market standard specification and option list; manufacturer-authored content on a dealer channel — see §4.2 for the classification rationale and promotion path |
| `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | Circuit Diagram Hanse 460, drawing H20B-7215-100-010, rev. 03 | Hanse Yachts AG (Ladebower Chaussee 11, Greifswald) | `sourced-manufacturer` | 2026-07-16 | Hanse 460 series electrical circuit diagram (54 sheets); series drawing, "gültig ab Serien-Nr." field carries no serial value in the title block — not hull-specific; reference vessel delivery set, hull identity not yet recorded in the register |
| `source:manufacturer:owner-held:h20b-7215-100-020-02:2026-07-16` | Circuit Diagram Hanse 460 US-Version, drawing H20B-7215-100-020, rev. 02 | Hanse Yachts AG | `sourced-manufacturer` | 2026-07-16 | Hanse 460 **US-version** circuit diagram (52 sheets); series drawing; captured for cross-reference only — the reference configuration is EU-market, so US-variant content must not be applied to it without an explicit variant assessment |
| `source:manufacturer:owner-held:h20b-7220-100-010-01:2026-07-16` | WI Kabelbaum Rumpf (wiring-harness installation, hull), drawing H20B-7220-100-010-01 | Hanse Yachts AG | `sourced-manufacturer` | 2026-07-16 | Hanse 460 (H460) hull wiring-harness routing (2 sheets); series drawing, "gültig ab Serien-Nr." field carries no serial value; reference vessel delivery set, hull identity not yet recorded in the register |
| `source:manufacturer:owner-held:h20b-7220-200-010-07:2026-07-16` | WI Kabelbaum Deck (wiring-harness installation, deck), drawing H20B-7220-200-010-07 | Hanse Yachts AG | `sourced-manufacturer` | 2026-07-16 | Hanse 460 (H460) deck wiring-harness routing (3 sheets); series drawing; reference vessel delivery set, hull identity not yet recorded in the register |
| `source:manufacturer:owner-held:h20b-7220-200-020-02:2026-07-16` | WI Kabelbaum T-Top (wiring-harness installation, T-top), drawing H20B-7220-200-020-02 | Hanse Yachts AG | `sourced-manufacturer` | 2026-07-16 | Hanse 460 (H460) T-top wiring-harness routing (1 sheet, incl. solar cable positions); series drawing; reference vessel delivery set, hull identity not yet recorded in the register |
| `source:manufacturer:owner-held:owners-manual-460-en-v11:2026-07-16` | Owner's Manual Sailing Yacht "Hanse 460", English, V11 (May 2024) | HanseYachts AG | `sourced-manufacturer` | 2026-07-16 | Hanse 460 model-generic owner's ("Owner's Safety") manual — the internal file name carries the suffix "allg" (allgemein/general), i.e. not hull-specific; reference vessel delivery set, hull identity not yet recorded in the register |
| `source:manufacturer:owner-held:h460.25-spec-eu-2025-04-03:2026-07-16` | Hanse 460 Specification, EU version, model year 2025 (H460.25_SPEC_EU_20250403; document states "Valid from 2025.04.04") | HanseYachts AG | `sourced-manufacturer` | 2026-07-16 | Hanse 460 EU-market standard specification, model year 2025; design family, no hull applicability; **a different document from the 2021 US specification/pricelist (§3.3)** — see §4.2 |
| `source:manufacturer:owner-held:mastervolt-chargemaster-plus-manual-10000016594-03:2026-07-16` | ChargeMaster Plus 12/35-3, 12/50-3, 24/20-3, 24/30-3 — User and Installation Manual, doc. 10000016594/03 | Mastervolt (Amsterdam, NL) | `sourced-manufacturer` | 2026-07-16 | Vendor manual for the battery-charger product family present in the owner-held delivery set; which of the covered models is installed is not yet confirmed as-built |
| `source:manufacturer:owner-held:victron-multiplus-compact-manual-v12:2026-07-16` | Manual MultiPlus Compact 12\|2000\|80-50 120V, 24\|2000\|50-50 120V (Version 12, 11 April 2016) | Victron Energy B.V. (Almere, NL) | `sourced-manufacturer` | 2026-07-16 | Vendor manual for the MultiPlus Compact inverter/charger; **this manual edition covers the 120 V AC-output models** while the reference configuration is an EU 230 V vessel — the installed model and the correct manual edition require as-built confirmation before any value transcription |
| `source:manufacturer:owner-held:lifos-105-battery-instructions-8546:2026-07-16` | Lifos 105 — User Manual / battery instructions, Lithium Iron Phosphate Battery (LiFePO4), doc. 8546 (revision not stated in document) | Lifos (UK) | `sourced-manufacturer` | 2026-07-16 | Vendor instructions for the Lifos 105 (105 Ah LiFePO4) battery present in the owner-held delivery set; installed battery model (Lifos 105 vs. Lifos Go 105Ah, see §4.4) and bank composition not yet confirmed as-built |
| `source:manufacturer:owner-held:simarine-pico-manual-1.5:2026-07-16` | PICO and PICOone Battery and Tank Monitoring System — User Manual, Revision 1.5 (EN/DE) | SIMARINE | `sourced-manufacturer` | 2026-07-16 | Vendor manual for the Simarine Pico battery/tank monitoring display present in the owner-held delivery set; installed variant (PICO vs. PICOone) and shunt configuration not yet confirmed as-built |
| `source:manufacturer:owner-held:victron-isolation-transformer-7000w-manual-03:2026-07-16` | Manual Isolation transformer 7000W \| 230V \| 32A (Version 03, 05 October 2010; EN/NL/FR/DE/ES) | Victron Energy B.V. | `sourced-manufacturer` | 2026-07-16 | Vendor manual for the Victron 7000 W / 230 V / 32 A isolation transformer present in the owner-held delivery set; whether this or the WhisperPower unit (next row) is installed is not yet confirmed as-built |
| `source:manufacturer:owner-held:whisperpower-wp-gi-3600-manual:2026-07-16` | User Manual WP-GI — WhisperPower Galvanic Isolation-transformer (archive file name indicates the 3600 model; revision not stated in document) | WhisperPower BV (Drachten, NL) | `sourced-manufacturer` | 2026-07-16 | Vendor manual for the WhisperPower WP-GI galvanic isolation transformer present in the owner-held delivery set; installed unit not yet confirmed as-built |
| `source:manufacturer:owner-held:aquasignal-series-34-manual-9420110500:2026-07-16` | Operating Manual for Navigation Lights Series AQUA SIGNAL 34 (LED; internal document file 9420110500; revision not stated in document) | Aqua Signal | `sourced-manufacturer` | 2026-07-16 | Vendor operating manual for the Aqua Signal Series 34 LED navigation lights present in the owner-held delivery set; installed light positions/models not yet confirmed as-built |
| `source:manufacturer:owner-held:aquasignal-series-40-50-mounting:2026-07-16` | aqua signal 40 / 41 / 42 / 50 — Mounting Instructions for Navigation Lights (internal document file 40_02_GB; revision not stated in document) | Aqua Signal | `sourced-manufacturer` | 2026-07-16 | Vendor mounting instructions for Aqua Signal series 40/41/42/50 navigation lights (a DE-language copy exists in the archive); applicability to the reference vessel not yet confirmed as-built — the series targets vessels of 20 m and more |

Source locations (recorded as text, not hyperlinks, to keep the register
independent of link availability):

- `source:secondary:wikipedia:hanse-brand:2026-07-10` and
  `source:secondary:wikipedia:hanse-brand:2026-07-15` —
  `https://en.wikipedia.org/wiki/Hanse_(yacht_brand)`
- `source:manufacturer:hanseyachts-com:hanse-460-product-page:2026-07-15` —
  `https://hanseyachts.com/us/sailing-yachts/hanse-460/`
- `source:manufacturer:hanseyachts-com:hanse-460-historical-page:2026-07-15` —
  `https://hanseyachts.com/us/historical-models/hanse-460/`
- `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` —
  `https://www.newwaveyachts.com/pdf_sheets/Hanse%20460%20Specification%20and%20Pricelist.pdf`
  (PDF, 13 pages; footer: "All measurements/figures are approximate. Errors
  and omissions excepted. Specification and material can be changed without
  notice. Valid from 2021.11.12."; "Boat according to US specifications.")

All `source:manufacturer:owner-held:*:2026-07-16` entries are PDF files in
the owner-held local archive (root folder `Hanse/`, provided by the
accountable maintainer on 2026-07-16; not stored in this repository, §5).
Locations are archive-relative paths; identity details (title block,
cover, revision) are quoted from the documents themselves:

- `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` —
  `Technical Documents Electrical/General/H20B-7215-100-010-03.pdf`;
  cover sheet: "circuit diagram Hanse 460", drawing no. H20B-7215-100-010,
  rev. 03 ("changes AC panel, battery protection, many changes" at rev 01,
  "changes solar panels; bathing platform" at rev 02, "bp alarm added,
  watermaker updated" at rev 03), title-block date 21.06.2021, drawn/
  checked/approved JTaubert, sheet 1 of 54. Cover sheet also states the
  drawing-wide cable-color code and the default cable cross-section
  ("All cable cross-sections unless otherwise noted: 1,5mm²") —
  extraction location for these defaults: cover sheet (sheet 1).
- `source:manufacturer:owner-held:h20b-7215-100-020-02:2026-07-16` —
  `Technical Documents Electrical/General/H20B-7215-100-020-02.pdf`;
  cover sheet: "Circuit Diagram Hanse 460 US-Version", drawing no.
  H20B-7215-100-020, rev. 02, title-block date 03.08.2021, drawn
  D.Westphal, checked B.Gladrow, approved T.Stein, sheet 1 of 52.
- `source:manufacturer:owner-held:h20b-7220-100-010-01:2026-07-16` —
  `Technical Documents Electrical/General/H20B-7220-100-010-01_17022023.pdf`;
  title block: "WI Kabelbaum Rumpf", drawing no. H20B-7220-100-010-01,
  valid for H460, prepared (Bearb.) 07.12.2020, released (Freig.)
  15.06.2021, change entry "01 empty tube 17.02.2023", 2 sheets, CATIA V5.
- `source:manufacturer:owner-held:h20b-7220-200-010-07:2026-07-16` —
  `Technical Documents Electrical/General/H20B-7220-200-010-07.pdf`;
  title block: "WI Kabelbaum Deck", drawing no. H20B-7220-200-010-07,
  valid for H460, released 25.08.2023, change entries 01–07 (latest:
  "07 sheet 2; 3, 25.08.2023"), 3 sheets, CATIA V5.
- `source:manufacturer:owner-held:h20b-7220-200-020-02:2026-07-16` —
  `Technical Documents Electrical/General/H20B-7220-200-020-02.pdf`;
  title block: "WI Kabelbaum T-Top", drawing no. H20B-7220-200-020-02,
  valid for H460, released 22.09.2022, change entries "01 cable routing
  16.06.2022", "02 tube routing 22.09.2022", 1 sheet, CATIA V5.
- `source:manufacturer:owner-held:owners-manual-460-en-v11:2026-07-16` —
  `Manual General/General/Owners Manual 460 Buch eng V11.pdf` (119 PDF
  pages); cover: Sailing Yacht "Hanse 460", HanseYachts AG; details page:
  "Owner's Safety Manual - Translation", internal file "Owners Manual 460
  Buch eng V11 - allg.docx", May 2024. A German-language copy of the same
  V11 edition exists in the same archive folder ("Owners Manual 460 Buch
  deu V11.pdf") and is treated as the same document, not a separate entry.
  Electrical content (extraction locations, printed page numbers):
  Chapter 1 §1.2.5 "Electrical system" (p. 6, PDF p. 16); Chapter 2 §1.5
  "Electrical systems" (pp. 57–66, PDF pp. 67–76), with §1.5.1 Direct
  current system (p. 61), §1.5.2 Alternating current system (p. 64),
  §1.5.3 Navigation systems (p. 66).
- `source:manufacturer:owner-held:h460.25-spec-eu-2025-04-03:2026-07-16` —
  `Specifications/General/H460.25_SPEC_EU_20250403.pdf` (4 PDF pages, PDF
  internal title "PricelistAndSpecification", file created 2025-04-03);
  page 1 footer: "All measurements/figures are approximate. Errors and
  omissions excepted. All weights are specified in MLC. Specification and
  material can be changed without notice. Valid from 2025.04.04." Note the
  one-day discrepancy between the file-name/creation date (2025-04-03) and
  the stated validity date (2025.04.04); both are recorded, the `document:`
  identity uses the file identity 2025-04-03. A German-language copy
  ("H460.25_SPEC_DE_20250403.pdf") exists in the same folder and is
  treated as the same document, not a separate entry.
- `source:manufacturer:owner-held:mastervolt-chargemaster-plus-manual-10000016594-03:2026-07-16`
  — `Manual Navigation and Electronic/Electronic/manualChargeMasterPlus_12-35_12-50.pdf`
  (32 pages); cover: "CHARGEMASTER PLUS — ChargeMaster Plus 12/35-3,
  12/50-3, 24/20-3, 24/30-3 — Automatic Battery Charger — User and
  Installation Manual", document number 10000016594/03. The archive also
  holds the companion safety leaflet "Mastervolt_Safety_Chargemaster-5ed44.pdf"
  (Mastervolt doc. 10000009318/00, February 2015), treated as publication
  context of the same product documentation, not a separate entry.
- `source:manufacturer:owner-held:victron-multiplus-compact-manual-v12:2026-07-16`
  — `Manual Navigation and Electronic/Electronic/Victron MultiPlus Compact.pdf`
  (40 pages); cover: "Manual — MultiPlus Compact 12 | 2000 | 80-50 120V,
  24 | 2000 | 50-50 120V"; back page: Version 12, 11 April 2016, Victron
  Energy B.V.
- `source:manufacturer:owner-held:lifos-105-battery-instructions-8546:2026-07-16`
  — `Manual Navigation and Electronic/Electronic/8546 LiFOS105Ah battery instructions.pdf`
  (4 pages); "Lifos 105 — User manual, Lithium Iron Phosphate Battery
  (LiFePO4)", document file number 8546; no revision or issue date stated
  in the document. The archive file "Lifos 105 Battery.pdf" (2 pages) is a
  shorter leaflet variant of the same Lifos 105 instructions (quick guide,
  warranty and safety text) and is treated as publication context, not a
  separate entry. "Lifos Go 105 Instructions with button.PDF" documents a
  **different product** (Lifos Go 105Ah, with on/off button) and is left
  in the pending-capture inventory (§4.4) until the installed battery
  model is confirmed.
- `source:manufacturer:owner-held:simarine-pico-manual-1.5:2026-07-16` —
  `Manual Navigation and Electronic/Electronic/Simarine DC Panel Manual_Pico_EN_DE_1.5.pdf`
  (99 pages); cover: "PICO and PICOone — Battery and Tank Monitoring
  System — User Manual — Revision 1.5" (EN/DE), SIMARINE.
- `source:manufacturer:owner-held:victron-isolation-transformer-7000w-manual-03:2026-07-16`
  — `Manual Navigation and Electronic/Electronic/Victron Isolation-transformer-7000W-EN-NL-FR-DE-ES.pdf`
  (46 pages); cover: "Manual — Isolation transformer 7000W | 230V | 32A"
  (EN/NL/FR/DE/ES); back page: Version 03, 05 October 2010, Victron
  Energy B.V.
- `source:manufacturer:owner-held:whisperpower-wp-gi-3600-manual:2026-07-16`
  — `Manual Navigation and Electronic/Electronic/Whisperpower_WP-GI_3600_Galvanic_Isolation-transformer-f2b8c.pdf`
  (2 pages); "User Manual WP-GI — WhisperPower Galvanic
  Isolation-transformer", WhisperPower BV; the document body names only
  the WP-GI series — the 3600 model designation appears in the archive
  file name; no document revision stated.
- `source:manufacturer:owner-held:aquasignal-series-34-manual-9420110500:2026-07-16`
  — `Manual Navigation and Electronic/Electronic/aqua signal Serie 34.pdf`
  (2 pages); "Operating Manual for Navigation Lights Series AQUA SIGNAL 34"
  (EN/DE/FR), LED technology, supply 12V/24V DC ±20%; internal document
  file 9420110500; no revision stated. Extraction location for the
  per-light power-consumption figures: page 1, "Consumption" block.
- `source:manufacturer:owner-held:aquasignal-series-40-50-mounting:2026-07-16`
  — `Manual Navigation and Electronic/Electronic/aqua signalSeries 40-50 EN.pdf`
  (9 pages); "aqua signal 40 / 41 / 42 / 50 — Mounting Instructions for
  Navigation Lights"; internal document file 40_02_GB; no revision stated;
  a DE-language copy ("aqua signal Serie 40-50 DE.pdf") exists in the
  same folder and is treated as the same document.

## 3. Claims Extracted

Claims are transcribed only from content actually retrieved on the recorded
retrieval date, with the extraction location stated. No value in this
section originates from memory or general knowledge
(`OMSP-PLANNING-GOLDEN-PATH-0001` §4.3 rule 2).

### 3.1 Wikipedia — Hanse (yacht brand)

The following claims were transcribed into `OMSP-REFERENCE-CONFIG-0001` as
`sourced-secondary` (capture 2026-07-10; extraction location: "Current
models" metric specification table):

- model designation: Hanse 460;
- model introduction year: 2021;
- length overall: 14.60 m;
- beam: 4.79 m;
- standard displacement: 12.6 t;
- draft values: 2.25 m and 1.75 m, with option applicability not
  independently verified at capture time;
- air draft: 21.90 m;
- standard sail area: 106.0 m².

Re-verification 2026-07-15
(`source:secondary:wikipedia:hanse-brand:2026-07-15`): all values above are
unchanged in the live article (last edited 2024-05-27). The table
additionally states an SA/D ratio of 4.4 (metric), which has not been
transcribed into the reference configuration.

These values have medium confidence for reference-model use only. They are
not verified manufacturer or as-built data.

### 3.2 HanseYachts AG product pages (manufacturer-controlled web channel)

From `source:manufacturer:hanseyachts-com:hanse-460-product-page:2026-07-15`
(extraction locations: exterior-design and accommodation sections of the
product page):

- exterior and interior design attributed to Berret-Racoupeau;
- accommodation: six to ten berths;
- 48 layout variants offered;
- the page's document/download section returns "No documents found" — no
  technical specification is published on this channel.

From
`source:manufacturer:hanseyachts-com:hanse-460-historical-page:2026-07-15`
(extraction location: historical-models section header and page body):

- model production span stated as "Hanse 460 2021-2026";
- same designer and accommodation claims as the product page;
- no downloadable documents ("No documents found").

These are the only claims currently held at class `sourced-manufacturer`.
They are marketing-level facts; **no electrical or dimensional technical
value is available from the manufacturer-controlled web channel** (§4.2).

### 3.3 Hanse 460 Specification and Pricelist (dealer-hosted, US market)

All claims below are class `sourced-secondary`, medium confidence,
applicability "Hanse 460 US-market standard specification valid from
2021.11.12; design family only, no hull applicability". The document itself
marks all figures as approximate. Extraction locations are PDF page numbers
of `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15`.

Principal dimensions and general data (page 1):

- LOA 14.60 m; hull length 13.87 m; LWL 13.05 m; beam 4.79 m;
- draft: shallow keel 1.75 m; L-keel medium 2.25 m;
- displacement (L-keel, medium): approx. 12.60 t;
- engine (diesel): standard approx. 57 PS / 57 hp; option approx. 80 PS /
  80 hp;
- fuel tank approx. 210 l; fresh water approx. 450 l;
- CE certificate: A - 12;
- design and interior: Berret-Racoupeau;
- mast length above waterline approx. 21.90 m;
- sail areas: upwind approx. 114.00 m²; main approx. 64.00 m²; jib approx.
  42.00 m²; genoa approx. 50.00 m²; reacher approx. 78.00 m²; gennaker
  approx. 170.00 m²; downwind approx. 234.00 m².

Electrical energy system, standard specification (page 3, "EQUIPMENT"
section) — golden-path relevant:

- "12 V and 230 V electric system with main panels and 230 V shore power
  and sockets in cabins and heads";
- battery set (standard): AGM, capacity 1x 90 Ah + 1x 160 Ah;
- battery charger: 35 A (no manufacturer/model named);
- 12 V fridge approx. 135 l (galley, standard; no manufacturer named);
- navigation lights: LED;
- 2 LEWMAR 45 ST EVO manual halyard winches (named vendor; manual, not an
  electrical consumer in standard trim).

Other systems, standard specification (page 4):

- electric and manual bilge pump (no manufacturer named);
- fresh water system with electric pump and 40 l hot water, heated also by
  main engine;
- black water system approx. 85 l each bathroom;
- CE certificate categories: A - 12, B - 14, C - 16;
- "Owners manual" and "EC - Type Examination Certificate" listed as
  delivered items (supports §4.4: an owner's manual exists for the design
  family).

Factory options relevant to the golden-path electrical slice (pages 5, 6
and 12; option codes as printed):

- XH1001 — battery set upgrade, 1x 90 Ah + 2x 160 Ah AGM;
- XH1005 — battery set upgrade, 1x 90 Ah + 6x 105 Ah Li-Ion;
- XH1110 — deep charge protection for service batteries;
- XH2201 — inverter/charger, 12 V / 2600 W - 100 A, incl. AC panel (only
  with XH1001 or XH1005; no manufacturer/model named);
- XH2080 — solar panel integrated in hard top (only with GRP hard top);
- XH2101 / XH2102 — generator 8000i (6.4 kW) / 10000i (8.0 kW);
- XG3101 / XG3201 — bow/stern thruster, 24 V, retractable, incl. battery;
- XW2000 — B&G Navigation Package (Triton² displays, Zeus³S plotter, V60
  VHF, Precision 9 compass; named vendor identities, optional equipment).

Applicability note for all named option equipment: **optional equipment per
the US-market specification/pricelist; installed as-built configuration
unknown.** Standard-equipment electrical items (battery set, charger, bilge
pump, fridge) carry **no vendor identity** in this document; vendor manuals
for them therefore cannot be registered yet (§4.4).

Conflict assessment (§6 discipline — recorded side by side, not resolved):

- Displacement: Wikipedia "12.6 t" and specification "approx. 12.60 t
  (L-keel, medium)" are consistent.
- Sail area: Wikipedia states "106.0 m²" (consistent with main 64.00 m² +
  self-tacking jib 42.00 m²); the specification states upwind sail area
  approx. 114.00 m² (main + genoa 50.00 m²). This is a differing sail-plan
  basis, not a numeric contradiction; both figures remain recorded with
  their basis.

### 3.4 H460.25 EU Specification 2025 (owner-held) — conflict assessment

Full value transcription from the owner-held document set is downstream
work (v0.3.0 is register capture only). This subsection records only the
identity-page claims actually read during capture, because they conflict
with, or corroborate, existing §3.3 claims and §6 requires side-by-side
recording in the same change. All claims below are class
`sourced-manufacturer`, applicability "Hanse 460 EU-market standard
specification, model year 2025; design family only, no hull
applicability"; the document marks all figures as approximate. Source:
`source:manufacturer:owner-held:h460.25-spec-eu-2025-04-03:2026-07-16`
(extraction locations: PDF page numbers).

Conflicting with the 2021 US specification (§3.3) — recorded side by
side, **not resolved** (§6); the two documents differ in market (US vs
EU) and validity date (2021.11.12 vs 2025.04.04), so divergence may be
market- or model-year-driven:

- fuel tank: US 2021 approx. 210 l — EU 2025 approx. 200 l (page 1);
- upwind sail area: US 2021 approx. 114.00 m² — EU 2025 approx.
  113.00 m² (page 1);
- genoa: US 2021 approx. 50.00 m² — EU 2025 approx. 49.00 m² (page 1).

Consistent with existing claims (corroboration, no promotion — §5 keeps
promotion of §3.3 claims a human decision, and this is a different
document from the 2021 US specification, so it does not trigger the §4.2
promotion path):

- LOA 14.60 m; hull length 13.87 m; LWL 13.05 m; beam 4.79 m; drafts
  1.75 m / 2.25 m; displacement L-keel approx. 12.60 t; mast length above
  WL approx. 21.90 m; main approx. 64.00 m²; jib approx. 42.00 m²;
  reacher approx. 78.00 m²; gennaker approx. 170.00 m²; downwind approx.
  234.00 m²; engine standard approx. 57 PS / option approx. 80 PS; fresh
  water approx. 450 l; CE certificate A - 12 (page 1); CE categories
  A - 12, B - 14, C - 16 (page 4);
- golden-path-relevant standard equipment (page 3): "12 V and 230 V
  electric system with main panels and 230 V shore power and sockets in
  cabins and heads"; "AGM battery set, capacity: 1x 90 Ah + 1x 160 Ah
  AGM"; "Battery charger" (listed **without** an ampere rating — the
  35 A figure exists only in the 2021 US specification, §3.3); 12 V
  fridge approx. 135 l; navigation lights LED; "Country Version:
  EU / AUS";
- other systems (page 4): electric and manual bilge pump; fresh water
  system with electric pump and 40 l hot water; black water approx. 85 l
  each bathroom.

New value not present in §3.3: displacement with shallow keel approx.
13.00 t (page 1; the 2021 US document stated only the L-keel figure).

## 4. Authority-Class Coverage and Evidence Gaps

### 4.1 Coverage of golden-path input classes

Per `OMSP-PLANNING-GOLDEN-PATH-0001` §4.1, every authority class is either
covered by a register entry or explicitly declared absent:

| Authority class | Register status | Where |
| --- | --- | --- |
| `reference` | Covered by declaration — OMSP modeling structure originates from governed OMSP artifacts (`OMSP-REFERENCE-VESSEL-0001`, `OMSP-REFERENCE-EQUIPMENT-0001`), not from external sources; no external source entry is required | This row |
| `sourced-secondary` | Covered — entries exist | §2.2 (Wikipedia 2026-07-10 / 2026-07-15; dealer-hosted specification/pricelist) |
| `sourced-manufacturer` | Covered — since v0.3.0 the owner-held document set provides manufacturer/vendor technical documents (factory drawings, owner's manual, EU specification, vendor manuals); before v0.3.0 this class held marketing-level claims only (§3.2, §4.2). Technical **values** from these documents are not yet transcribed into the model (§4.4) | §2.2, §3.2, §3.4, §4.2, §4.4 |
| `verified-design` | **Explicitly absent** — no claim carries this class; the v0.3.0 captures enter at `sourced-manufacturer`, and promotion is a human decision per §5 | This row; §5 governs promotion |
| `verified-as-built` | **Explicitly absent** — no vessel-instance evidence captured (no hull identity, no panel/nameplate observation); the owner-held documents alone do not establish as-built state | This row; §5 governs promotion |
| `unknown` | Explicitly represented — every inaccessible source produces an `unknown` declaration, never a silent gap | §4.3 |

### 4.2 Manufacturer technical evidence gap

The manufacturer-controlled web channel (`hanseyachts.com`) was captured on
2026-07-15 and publishes **no technical specification and no downloadable
documents** for the Hanse 460 ("No documents found" on both captured
pages). The manufacturer's controlled document portal (`hanseyachtsag.com`
MIS) is login-gated (§4.3). Therefore:

- until v0.3.0, no electrical or dimensional technical value was
  classified `sourced-manufacturer`; since v0.3.0 the owner-held document
  set (§4.4) provides that class for its captured documents;
- no claim is classified `verified-design` or `verified-as-built`;
- the dealer-hosted specification/pricelist (§3.3) is manufacturer-authored
  content on a dealer channel; it is conservatively classified
  `sourced-secondary` because the hosting channel is not
  manufacturer-controlled and the copy's integrity is not independently
  confirmed. It is a **promotion candidate**: if the identical document is
  captured from a manufacturer-controlled channel or from the owner-held
  document set (§4.4), its claims may be promoted to
  `sourced-manufacturer` per §5 (human decision);
- **promotion-candidacy status after v0.3.0:** the owner-held archive
  does **not** contain the 2021 US specification/pricelist; it contains
  the H460.25 EU specification (valid from 2025.04.04), which is a
  **different document** (different market, different validity, partially
  differing values — §3.4). The v0.3.0 capture therefore does **not**
  trigger the promotion path above, and the §3.3 claims remain
  `sourced-secondary`;
- secondary values must be rechecked before future promotion;
- inaccessible or assumed source content was not reconstructed from memory.

### 4.3 Capture attempts without access (2026-07-15)

The following sources were attempted and are declared inaccessible; they
produce `unknown` for any value they might have supported. None of them is
recorded as a register entry.

| Attempted source | Location (text) | Result |
| --- | --- | --- |
| HanseYachts AG official Hanse 460 brochure 2021 (MIS portal) | `https://www.hanseyachtsag.com/mis/website/document/download/hanse-460-brochure-2021-hanse-460-brochure_-8766270238080370119.pdf` | Returns the MIS login page (HTML), not the document; login-gated |
| HanseYachts AG official Hanse 460 brochure 2023 (MIS portal) | `https://www.hanseyachtsag.com/mis/website/document/download/hanse-460-brochure-2023-hanse-460-brochure_-2644375116673249588.pdf` | Returns the MIS login page (HTML), not the document; login-gated |
| Hanse 460 brochure (UK dealer copy) | `https://www.hanseyachts.co.uk/files/Hanse_460_brochure.pdf` | Returns an HTML page, not a PDF; document not retrievable |
| Hanse 460 brochure (dealer copy) | `https://boatingfreedom.com/wp-content/uploads/2021/07/Hanse_460_Bro_Web96_DoSei_0721.pdf` | Returns an HTML page, not a PDF; document not retrievable |
| sailboatdata.com Hanse 460 record | `https://sailboatdata.com/sailboat/hanse-460/` | HTTP 403; content not retrieved — values circulating from this source (e.g. ballast, engine make) remain `unknown` here |
| B&G Triton² official product page | `https://www.bandg.com/bg/type/instruments/triton2-digital-display/` | HTTP 403; vendor documentation for the optional B&G equipment (§3.3) not captured |
| Hanse 460 owner's manual / wiring diagrams (public channels) | Owner-forum threads (`myhanse.com`) are registration-gated; third-party manual aggregator sites are not legitimate distribution channels and are not used | Not captured; see §4.4 |

### 4.4 Owner-held document set — captured (v0.3.0)

The owner-held document set for the reference vessel (per
`OMSP-PLANNING-GOLDEN-PATH-0001` §4.2) became available on **2026-07-16**
as a local archive provided by the accountable maintainer. The
golden-path electrical slice of the set is **captured in this register**
(v0.3.0, WP-0092/#253): fifteen §2.2 entries under the
`source:manufacturer:owner-held:*` identity family, each with its §7
`document:` mapping row registered in the same change (§7 rule 4).

Capture contract (applied in v0.3.0, and binding for every future
capture from this archive): each document is registered as a new §2.2
entry with all six contract fields, plus document title, revision and
publication context, extraction locations for every transcribed value,
and a `document:` mapping row in §7 in the same change. Classes:
`sourced-manufacturer` for manufacturer/vendor documents — this is a new
record at that class, **not** a promotion of existing claims (promotion
to `verified-design`/`verified-as-built` only per §5, human decision) —
with applicability naming the specific hull where a document is
hull-specific. Where a document states no revision, the entry says
"revision not stated in document"; revisions are never invented.

Honesty boundaries of the v0.3.0 capture:

- **Hull identity:** the archive is the reference vessel's delivery set,
  but no captured document names a hull/serial number (the drawing
  title-block field "gültig ab Serien-Nr." carries no value). All
  applicability statements therefore read "reference vessel delivery
  set; hull identity not yet recorded in the register". The H20B prefix
  is the Hanse 460 drawing-series code, not a hull identity.
- **No value transcription:** except for the §3.4 conflict assessment,
  no technical value from the captured documents has been transcribed
  into this register or the instance models; the 99 explicit unknowns of
  `reference/hanse460/` are unchanged in this version (closure path:
  §4.5).
- **Vessel observation evidence** (photographs of panels, breaker
  labels, battery nameplates) remains uncaptured; `verified-as-built`
  stays explicitly absent (§4.1).

**Archive inventory — present in the archive, capture deferred to a
later iteration.** The following documents neighbour the electrical
slice but are deliberately **not** captured in v0.3.0; they are listed
at file-name level so future capture work is traceable and the v0.3.0
scope stays honest. File names are archive-relative; no identity beyond
the file name has been extracted or is claimed:

- `Manual Navigation and Electronic/Electronic/` (electrical, next
  capture candidates): `Mastervol MasterShunt 500.pdf`,
  `Mastervolt Combimaster EN.pdf` (+ DE), `Mastervolt Magic DC-DC
  Converter.pdf`, `Mastervolt Smart Remote EN.pdf` (+ DE),
  `Würth_DC-Panel_V2_EN.pdf` (+ DE), `Whisperpower_WBL160-5a658.pdf`,
  `Whisperpower DC-DC_Converters_MC_Series (1).pdf`,
  `SIMARINE_SCP220H_Operating_Manuals_EN_DE.pdf`,
  `SLS2 Lightcontrol ML1901_v3.pdf`, `ProMariner ProSafe FS30 Galvanic
  Isolator.pdf`, `Victron Digital-Multi-Control-Panel.pdf`,
  `Sentinel Boat Monitor.pdf`, `Sentinel IG.pdf`,
  `Lifos Go 105 Instructions with button.PDF` (distinct product from the
  captured Lifos 105 — see §2.2 source locations);
- `Manual Propulsion/General/` (identified in the issue #253 inventory
  as the propulsion/engine set; manufacturer identity to be confirmed at
  capture): `0AJHC-EN0014-20171115_OPM_CD.pdf` (+ DE),
  `0ASDM-EN0022-20171225.pdf` (+ DE),
  `0JMPE-EN0035-20171115_WarrantyHandbook_CD.pdf` (+ DE);
- `Manual Options/General/` (generator, HVAC, refrigeration, thrusters —
  electrical consumers/producers outside the current slice):
  `Fischer Panda 4K EN.pdf`, `Fischer Panda 5000i Neo PMS EN.pdf`,
  `Fischer Panda 8000i 10000iPMS EN.pdf` (+ DE copies),
  `Quick BTR185_IT_EN Rev08B.pdf` (+ F/D/E), `Quick TCD1022-1042
  REV005A.pdf`, `Quick TCD1044 REV003A.pdf`, `Isotherm Fridge.pdf`,
  `Dometic AC MCS T6-T16 EN DE FR NL.pdf`, `Dometic Cooling Unit.pdf`,
  `Dometic Elite OM.pdf` (+ DE), `Dometic Refrigeration CD20.pdf`,
  Eberspächer heating set (Airtronic D4R, Hydronic MII, EasyStart,
  EN/DE), `Piccolo_8101215_Marine_User_15092020 EN.pdf` (+ DE),
  `Fisher & Paykel Dishdrawer Dishwasher DD60-DD24-userguide.pdf`,
  `Outils Oceans Emergency Ladder.pdf`, `TSX0043 Manual.pdf`,
  `eno-76a93.pdf`;
- `Manual Navigation and Electronic/Navigation/` (Raymarine/navigation
  set): `LightHouse 3.4 Basic Operation instructions 81369-6 EN.pdf`,
  `Ray53, Ray63, Ray73 Installation and Operation instructions
  81381-5-EN.pdf` (+ DE), `Raymarine AIS700 EN.pdf` (+ DE),
  `Raymarine I70s eng.pdf` (+ DE), `Raymarine Quantum 2 EN.pdf` (+ DE),
  `Raymarine RS150 GNSS EN.pdf` (+ DE), `Raymarine p70rs EN.pdf` (+ DE),
  `AirMar_Installation_Geber_Lot_Logge-43e6d.pdf`,
  `Silva_100BH125BH-ec10a.pdf`;
- `Manual Hardware/General/` (windlass/chain counter — electrical
  consumers outside the current slice): `Quick Windlass
  DP3_7-10-15_Rev_003A.pdf`, `Quick Chain Counter CHC1102M en fr.pdf`
  (+ de/es), `Lewmar Ocean and Eva B2303 V10.pdf`,
  `lewmar_deck_switch_advisory.pdf`, `Selden Assembly of endless
  line.pdf`;
- `Manual Grey-/Fresh Water System/General/` (pumps/boiler): `Quick
  Boiler BO20UT.pdf`, Jabsco toilet manuals; `Manual Entertainment/
  General/` (Fusion audio, VONETS WiFi); `Manual Rig & Sails/General/`
  (Selden furling, Quantum sails);
- `Technical Documents/General/` (naval-architecture plans: deck/hull/
  sail plans, stability curve, speed guide — outside the electrical
  slice), `Technical Documents Drawings/General/`
  (`H20B-3040-010-35-DW1.pdf`, `H20B-7560-950-02.pdf`),
  `Specifications/General/H460.25_SPEC_DE_20250403.pdf` (DE copy of the
  captured EU specification), `Layout/General/` (interior layout
  drawings), `Brochure/General/Hanse_2024_460_Bro_Web_Doublepages.pdf`,
  `Manual General/General/` remaining care/maintenance leaflets and
  `Storage Plan 460.pdf`, plus `Upgrade/` (Raymarine firmware images)
  and `APP/` (signed .apk files) — software artifacts, not documents;
  `Awards/`, `Color cards/`, `Photo Interieur/`, `Photo Exterieur/`
  (non-technical or photographic material; photographs may later serve
  §5 `verified-as-built` evidence, human decision).

### 4.5 Unknown-closure paths (model README §5 → captured documents)

`reference/hanse460/README.md` §5 publishes 99 explicit unknowns. The
v0.3.0 captures provide a **traceable closure path** for most of them;
no value is transcribed here (downstream work), this table only records
which captured document is expected to close which unknown group. Where
no captured document covers a group, the gap is stated:

| Unknown group (README §5 files) | Closure-path document(s) (§7 IDs) | Note |
| --- | --- | --- |
| `equipment-service-battery-bank` (8) | `document:hanseyachts:h20b-7215-100-010:03`; `document:lifos:lifos-105-battery-instructions-8546:undated`; `document:hanseyachts:owners-manual-460-en:v11` (§1.5.1) | Bank topology from the circuit diagram; cell/battery data from the Lifos manual **only after** the installed battery model (Lifos 105 vs. Lifos Go 105Ah) is confirmed as-built |
| `equipment-battery-charger` (7) | `document:mastervolt:chargemaster-plus-manual-10000016594:03`; `document:hanseyachts:h20b-7215-100-010:03` | Installed charger model within the manual's family requires as-built confirmation |
| `equipment-inverter` (6) | `document:victron:multiplus-compact-manual-120v:12`; `document:hanseyachts:h20b-7215-100-010:03` | **Caveat:** the archived manual edition covers 120 V models; EU 230 V unit identity must be confirmed before transcription |
| `equipment-shore-power-inlet` (7) | `document:hanseyachts:h20b-7215-100-010:03`; `document:hanseyachts:owners-manual-460-en:v11` (§1.5.2); `document:victron:isolation-transformer-7000w-manual:03`; `document:whisperpower:wp-gi-3600-manual:undated` | Which isolation transformer (if either) is installed requires as-built confirmation |
| `equipment-alternator-charging` (7) | `document:hanseyachts:h20b-7215-100-010:03`; `document:hanseyachts:owners-manual-460-en:v11` (§1.5.1) | Engine-side alternator data expected in the propulsion set (pending capture, §4.4 inventory) |
| `equipment-dc-main-distribution` (6) | `document:hanseyachts:h20b-7215-100-010:03` | DC-panel vendor document (`Würth_DC-Panel_V2_EN.pdf`) pending capture |
| `equipment-protection-dc-main` (7) | `document:hanseyachts:h20b-7215-100-010:03` | Protection/breaker sheets of the circuit diagram |
| `equipment-measurement-service-battery` (8) | `document:simarine:pico-manual-en-de:1.5`; `document:hanseyachts:h20b-7215-100-010:03` | Shunt documents (`SIMARINE_SCP220H`, `Mastervol MasterShunt 500`) pending capture |
| `equipment-dc-consumer-navigation-lights` (7) | `document:aquasignal:series-34-operating-manual-9420110500:undated`; `document:aquasignal:series-40-50-mounting:undated`; `document:hanseyachts:h20b-7215-100-010:03` | Installed light series/positions require as-built confirmation |
| `equipment-dc-consumer-refrigeration` (4) | `document:hanseyachts:h20b-7215-100-010:03` | Fridge vendor document (`Isotherm Fridge.pdf`) pending capture |
| `equipment-dc-consumer-bilge-pump` (6) | `document:hanseyachts:h20b-7215-100-010:03`; `document:hanseyachts:owners-manual-460-en:v11` (Ch. 2 §1.2.5 bilge system, printed p. 52) | Pump vendor identity not yet established by any captured document |
| `equipment-dc-consumer-freshwater-pump` (6) | `document:hanseyachts:h20b-7215-100-010:03`; `document:hanseyachts:owners-manual-460-en:v11` (Ch. 2 §1.2.1 fresh water, printed pp. 41–43) | Pump vendor identity not yet established by any captured document |
| `interface-*` / `connection-*` (13) | `document:hanseyachts:h20b-7215-100-010:03` (cover-sheet cable-color code and default cross-section; per-circuit sheets); `document:hanseyachts:h20b-7220-100-010:01`; `document:hanseyachts:h20b-7220-200-010:07`; `document:hanseyachts:h20b-7220-200-020:02` | Conductor/routing data from circuit diagram + harness drawings |
| `system-electrical` (1) | `document:hanseyachts:owners-manual-460-en:v11` (Ch. 2 §1.5); `document:hanseyachts:h460.25-spec-eu:2025-04-03` | System-level 12 V / 230 V description |

Closure of any unknown remains downstream work: it requires value
transcription with full five-field provenance into the instance models,
schema/integrity validation, and — for any authority-class change —
human decision per §5.

## 5. Promotion Requirements

A claim may be promoted from `sourced-secondary` only when a reviewer
captures evidence with:

- manufacturer or controlled-document identity;
- document title, revision and publication context;
- stable URL or repository-preserved copy where legally permitted;
- applicable model year, variant and market;
- extraction location such as page, table or section;
- retrieval date and reviewer identity;
- conflict assessment against existing claims.

Promotion to `verified-design` additionally requires accountable human
confirmation that the evidence applies to the intended design
configuration. Promotion to `verified-as-built` requires vessel-specific
evidence.

## 6. Conflict Handling

Conflicting claims must remain side by side with their source and
applicability metadata. The reference model must not resolve a conflict
merely by selecting the newest, most precise or most frequently repeated
value.

## 7. Document-Reference Mapping

Downstream instance models bind equipment roles to documentation through
`DocumentReference` identities of the form
`document:<authority>:<identifier>:<version>`
(`OMSP-REFERENCE-EQUIPMENT-0001` §3; `schemas/equipment-instance.schema.json`
`documents[]`, pattern `^document:[a-z0-9][a-z0-9:._-]*$`).

Mapping rules (consumed by the WP-0083 validator extension):

1. Every `document:` identity cited by any instance model MUST resolve to
   exactly one row of the mapping table below.
2. A register source entry MAY back multiple `document:` identities; a
   `document:` identity MUST map to exactly one register source ID.
3. A `document:` identity MUST NOT map to a source declared inaccessible in
   §4.3; inaccessible documentation is representable only as `unknown` in
   the model.
4. New owner-held documents (§4.4) receive their `document:` identity and
   mapping row in the same change that registers them.

Current mapping:

| Document ID | Register source ID |
| --- | --- |
| `document:hanseyachts:hanse-460-specification-pricelist-us:2021-11-12` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` |
| `document:hanseyachts:h20b-7215-100-010:03` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` |
| `document:hanseyachts:h20b-7215-100-020:02` | `source:manufacturer:owner-held:h20b-7215-100-020-02:2026-07-16` |
| `document:hanseyachts:h20b-7220-100-010:01` | `source:manufacturer:owner-held:h20b-7220-100-010-01:2026-07-16` |
| `document:hanseyachts:h20b-7220-200-010:07` | `source:manufacturer:owner-held:h20b-7220-200-010-07:2026-07-16` |
| `document:hanseyachts:h20b-7220-200-020:02` | `source:manufacturer:owner-held:h20b-7220-200-020-02:2026-07-16` |
| `document:hanseyachts:owners-manual-460-en:v11` | `source:manufacturer:owner-held:owners-manual-460-en-v11:2026-07-16` |
| `document:hanseyachts:h460.25-spec-eu:2025-04-03` | `source:manufacturer:owner-held:h460.25-spec-eu-2025-04-03:2026-07-16` |
| `document:mastervolt:chargemaster-plus-manual-10000016594:03` | `source:manufacturer:owner-held:mastervolt-chargemaster-plus-manual-10000016594-03:2026-07-16` |
| `document:victron:multiplus-compact-manual-120v:12` | `source:manufacturer:owner-held:victron-multiplus-compact-manual-v12:2026-07-16` |
| `document:lifos:lifos-105-battery-instructions-8546:undated` | `source:manufacturer:owner-held:lifos-105-battery-instructions-8546:2026-07-16` |
| `document:simarine:pico-manual-en-de:1.5` | `source:manufacturer:owner-held:simarine-pico-manual-1.5:2026-07-16` |
| `document:victron:isolation-transformer-7000w-manual:03` | `source:manufacturer:owner-held:victron-isolation-transformer-7000w-manual-03:2026-07-16` |
| `document:whisperpower:wp-gi-3600-manual:undated` | `source:manufacturer:owner-held:whisperpower-wp-gi-3600-manual:2026-07-16` |
| `document:aquasignal:series-34-operating-manual-9420110500:undated` | `source:manufacturer:owner-held:aquasignal-series-34-manual-9420110500:2026-07-16` |
| `document:aquasignal:series-40-50-mounting:undated` | `source:manufacturer:owner-held:aquasignal-series-40-50-mounting:2026-07-16` |

Where a document states no revision, the `document:` identity uses the
version segment `undated` and the §2.2 entry says "revision not stated
in document" — a fabricated revision is never used. No other `document:`
identity is currently registered; web-page sources (§2.2) are citable
directly as source IDs in provenance records but do not constitute
document references.

## 8. Known Limitations

This register is intentionally incomplete. It does not establish
regulatory approval, certification status, production change history or
individual-vessel applicability. The CE category claims in §3.3/§3.4 are
transcribed specification statements, not certification evidence.

State after v0.3.0:

- The owner-held document set — the primary intended evidence base for
  the golden-path electrical slice — **is captured at register level**
  (§4.4): document identities, locations and conflict assessments exist
  at class `sourced-manufacturer`. Its technical **values are not yet
  transcribed** into the instance models; the 99 explicit unknowns of
  `reference/hanse460/` are unchanged, with closure paths recorded in
  §4.5. That transcription is separate downstream work.
- Pre-v0.3.0 claims (§3.1–§3.3) keep their original classes; no
  promotion has occurred (§4.2), and any promotion remains a human
  decision per §5.
- No hull identity is recorded; nothing in this register is
  `verified-design` or `verified-as-built`, and the captured documents
  alone cannot establish as-built state without vessel observation
  evidence (§4.4).
- Parts of the archive neighbouring the electrical slice are inventoried
  but uncaptured (§4.4); their content is represented nowhere in this
  register.
