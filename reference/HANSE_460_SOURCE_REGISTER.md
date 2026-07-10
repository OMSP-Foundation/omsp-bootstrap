---
Artifact-ID: OMSP-REFERENCE-SOURCE-0001
Title: Hanse 460 Reference Source Register
Version: 0.1.0
Status: Review
Owner: OMSP Engineering Council
Approvers:
  - Accountable Maintainer
Created: 2026-07-10
Last-Updated: 2026-07-10
Sprint: Sprint-4
Work-Package: WP-0040
Traceability:
  - ISSUE-74
  - OMSP-REFERENCE-CONFIG-0001
---

# Hanse 460 Reference Source Register

## 1. Purpose

This register records the evidence context used by the initial Hanse 460 reference configuration. It prevents secondary data, inaccessible manufacturer pages and unverified assumptions from being represented as controlled design facts.

## 2. Source Record

| Source ID | Title | Owner | Class | Retrieved | Applicability |
| --- | --- | --- | --- | --- | --- |
| `source:secondary:wikipedia:hanse-brand:2026-07-10` | Hanse (yacht brand) | Wikipedia contributors | Secondary | 2026-07-10 | Hanse 460 design-family summary |

Source location: `https://en.wikipedia.org/wiki/Hanse_(yacht_brand)`

## 3. Claims Extracted

The following claims were transcribed into `OMSP-REFERENCE-CONFIG-0001` as `sourced-secondary`:

- model designation: Hanse 460;
- model introduction year: 2021;
- length overall: 14.60 m;
- beam: 4.79 m;
- standard displacement: 12.6 t;
- draft values: 2.25 m and 1.75 m, with option applicability not independently verified;
- air draft: 21.90 m;
- standard sail area: 106.0 m².

These values have medium confidence for reference-model use only. They are not verified manufacturer or as-built data.

## 4. Manufacturer Evidence Gap

During WP-0040 preparation, the current manufacturer product page or a controlled manufacturer brochure was not captured as repository evidence. Therefore:

- no value is classified as `sourced-manufacturer`;
- no claim is classified as `verified-design`;
- product options, capacities and equipment packages remain unknown;
- secondary values must be rechecked before future promotion;
- inaccessible or assumed source content was not reconstructed from memory.

## 5. Promotion Requirements

A claim may be promoted from `sourced-secondary` only when a reviewer captures evidence with:

- manufacturer or controlled-document identity;
- document title, revision and publication context;
- stable URL or repository-preserved copy where legally permitted;
- applicable model year, variant and market;
- extraction location such as page, table or section;
- retrieval date and reviewer identity;
- conflict assessment against existing claims.

Promotion to `verified-design` additionally requires accountable human confirmation that the evidence applies to the intended design configuration. Promotion to `verified-as-built` requires vessel-specific evidence.

## 6. Conflict Handling

Conflicting claims must remain side by side with their source and applicability metadata. The reference model must not resolve a conflict merely by selecting the newest, most precise or most frequently repeated value.

## 7. Known Limitations

This register contains one secondary source and is intentionally incomplete. It does not establish manufacturer authority, regulatory approval, certification status, production change history or individual-vessel applicability.