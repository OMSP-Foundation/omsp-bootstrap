---
Artifact-ID: OMSP-REFERENCE-SOURCE-0001
Title: Hanse 460 Reference Source Register
Version: 0.2.0
Status: Review
Owner: OMSP Engineering Council
Approvers:
  - Accountable Maintainer
Created: 2026-07-10
Last-Updated: 2026-07-15
Sprint: Sprint-8
Work-Package: WP-0081
Traceability:
  - ISSUE-74
  - ISSUE-202
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

## 4. Authority-Class Coverage and Evidence Gaps

### 4.1 Coverage of golden-path input classes

Per `OMSP-PLANNING-GOLDEN-PATH-0001` §4.1, every authority class is either
covered by a register entry or explicitly declared absent:

| Authority class | Register status | Where |
| --- | --- | --- |
| `reference` | Covered by declaration — OMSP modeling structure originates from governed OMSP artifacts (`OMSP-REFERENCE-VESSEL-0001`, `OMSP-REFERENCE-EQUIPMENT-0001`), not from external sources; no external source entry is required | This row |
| `sourced-secondary` | Covered — entries exist | §2.2 (Wikipedia 2026-07-10 / 2026-07-15; dealer-hosted specification/pricelist) |
| `sourced-manufacturer` | Covered for marketing-level claims only; **explicitly absent for technical values** — see §4.2 | §2.2, §3.2, §4.2 |
| `verified-design` | **Explicitly absent** — no controlled design evidence captured; no claim carries this class | This row; §5 governs promotion |
| `verified-as-built` | **Explicitly absent** — no vessel-instance evidence captured; requires owner-held documents and vessel observation (§4.4) | This row; §5 governs promotion |
| `unknown` | Explicitly represented — every inaccessible source produces an `unknown` declaration, never a silent gap | §4.3 |

### 4.2 Manufacturer technical evidence gap

The manufacturer-controlled web channel (`hanseyachts.com`) was captured on
2026-07-15 and publishes **no technical specification and no downloadable
documents** for the Hanse 460 ("No documents found" on both captured
pages). The manufacturer's controlled document portal (`hanseyachtsag.com`
MIS) is login-gated (§4.3). Therefore:

- no electrical or dimensional technical value is classified
  `sourced-manufacturer`;
- no claim is classified `verified-design` or `verified-as-built`;
- the dealer-hosted specification/pricelist (§3.3) is manufacturer-authored
  content on a dealer channel; it is conservatively classified
  `sourced-secondary` because the hosting channel is not
  manufacturer-controlled and the copy's integrity is not independently
  confirmed. It is a **promotion candidate**: if the identical document is
  captured from a manufacturer-controlled channel or from the owner-held
  document set (§4.4), its claims may be promoted to
  `sourced-manufacturer` per §5 (human decision);
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

### 4.4 Owner-held document set — declared absent, pending capture

The owner-held physical document set for the reference vessel (per
`OMSP-PLANNING-GOLDEN-PATH-0001` §4.2) was **not available in this capture
session and has no register entries yet**. No entry in this register
represents, summarizes or anticipates its content. Expected document types:

- manufacturer owner's manual (existence supported by §3.3, page 4:
  "Owners manual" is a listed delivery item);
- electrical wiring diagrams;
- equipment vendor manuals: battery, battery charger, inverter (if
  installed), shore-power installation;
- vessel observation evidence (photographs of panels, breaker labels,
  battery nameplates) — supports `verified-as-built` only through §5.

Capture contract when these documents become available: each document is
registered as a new §2.2 entry with all six contract fields, plus document
title, revision and publication context, extraction locations for every
transcribed value, and a `document:` mapping row in §7. Expected classes:
`sourced-manufacturer` for manufacturer/vendor documents (promotion to
`verified-design`/`verified-as-built` only per §5), with applicability
naming the specific hull where the document is hull-specific.

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

No other `document:` identity is currently registered; web-page sources
(§2.2) are citable directly as source IDs in provenance records but do not
constitute document references.

## 8. Known Limitations

This register is intentionally incomplete. It does not establish
manufacturer authority for technical values, regulatory approval,
certification status, production change history or individual-vessel
applicability. The CE category claims in §3.3 are transcribed
specification statements, not certification evidence. The owner-held
document set (§4.4) — the primary intended evidence base for the
golden-path electrical slice — is pending capture; until then, all
electrical values remain `sourced-secondary` at best, and every
uncaptured value is `unknown`.
