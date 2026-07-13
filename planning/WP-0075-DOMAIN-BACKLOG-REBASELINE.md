---
Artifact-ID: OMSP-PLANNING-REBASELINE-0001
Title: WP-0075 Domain Roadmap & Backlog Re-baseline
Version: 0.1.0
Status: Draft
Owner: toss-cengiz
Baseline: Sprint-6
Classification: Public
Related-Issue: WP-0075 / #169
Traceability:
  - ISSUE-145
  - ISSUE-169
  - ISSUE-171
  - ISSUE-172
  - ISSUE-173
  - ISSUE-174
  - ISSUE-175
  - ISSUE-176
  - ISSUE-177
  - ISSUE-178
  - OMSP-PLANNING-GOLDEN-PATH-0001
  - OMSP-CANON-METHODOLOGY-0001
---

# WP-0075 — Domain Roadmap & Backlog Re-baseline

## 1. Purpose and Authority

This artifact converts the approved post-audit roadmap (issue #145, official
roadmap since 2026-07-13; `roadmap/OMSP_ROADMAP.md` Sprint-7+ blocks) into an
ordered, product-led backlog for Sprint 7–14. It defines:

- exit criteria for the Sprint 7–14 epics (#171–#178);
- an implementation-ready Work Package breakdown for Sprint 7–9, numbered
  from **WP-0077** (WP-0076 is reserved for the v0.5.1 clean-baseline
  closure; WP-0060–0068 remain retired and are never reused);
- the binding dependency chain and the spec-first ordering for the MODS/ODS
  product stack;
- the capacity-policy application (65% domain/data, 20% tooling,
  10% documentation, 5% governance);
- the deferred-governance list and the release gates for v0.5.1 through
  v1.0.0.

This artifact **proposes** the backlog; opening the Work Package issues and
committing any sprint remain human decisions. GitHub issues stay the tracking
authority once opened; this artifact records scope, ordering, and
traceability.

Numbering basis (verified 2026-07-13): highest assigned Work Package is
WP-0076 (#170); WP-0070–0074 are merged (#192–#196); therefore new Work
Packages start at WP-0077.

## 2. Governing Rules

1. **Visible-outcome rule (binding).** No sprint goal may be satisfied by
   governance-only delivery. Every sprint in this plan names at least one
   demonstrable user-facing or domain-facing result (Section 5, "Sprint
   visible outcome" rows).
2. **Spec-first ordering (binding, per CTO product architecture and
   `OMSP-PLANNING-GOLDEN-PATH-0001` §7.2).** The minimal MODS/ODS document
   standards (ODS-100 structure, ODS-300 procedural language) must exist at
   least in Draft status before the first rendered operational-content
   instance is produced. Standards precede content; content becomes the
   first conformance test of the standard.
3. **Single source of truth.** The YAML model layer is authoritative; every
   rendered document is derived, never hand-maintained in parallel.
4. **Provenance rigor is never cut.** When scope pressure occurs, scope is
   reduced on the consumer set and interface detail, never on provenance or
   validation rigor (`OMSP-PLANNING-GOLDEN-PATH-0001` §10.2.3).
5. **Every new Work Package** carries `User Value` and `Evidence Produced`
   sections (as required by issue #169 and the Work Package template).

## 3. Sprint 7–14 Epic Exit Criteria

Milestone assignments verified against GitHub on 2026-07-13 (#174 is now in
the v0.6.1 milestone).

### 3.1 Sprint-7 — EPIC #171: Maritime Domain Model Foundation (v0.6.0)

Exit criteria (all measurable):

1. Maritime core ontology v0.1 is merged: vessel, system, equipment,
   interface, connection, protection, measurement, scenario, and provenance
   concepts mapped to `OMSP-ONTOLOGY-CORE-0001` identifiers;
   `tooling/validate_ontology.py` (extended as needed) passes in CI.
2. JSON Schemas for vessel, system, equipment, interface, connection, and
   scenario instances (including the provenance block) exist in `schemas/`
   and are enforced by a CI gate.
3. A representative sample maritime model package passes **all** domain
   validators with 0 findings — the Sprint-7 visible outcome.
4. MODS Specification v0.1 skeleton with ODS-100 and ODS-300 in Draft status
   is merged (spec-first gate for all Sprint 8–9 rendered content).
5. Core concepts contain no Hanse-460-only or electrical-only assumptions:
   demonstrated by the sample package including at least one non-electrical
   placeholder concept validated by the same pipeline.
6. Sprint-8 can ingest real Hanse 460 equipment data without redesigning
   the foundation (assessed at Sprint-8 planning; redesign found = epic not
   exited).

### 3.2 Sprint-8 — EPIC #172: Hanse 460 Electrical Golden Path (v0.6.0)

1. Hanse 460 source register extended with the owner-held documentation set
   (owner's manual, wiring diagrams, vendor manuals), each entry carrying
   source ID, authority class, retrieval date, and applicability.
2. Hanse 460 electrical-slice YAML model covers 100% of the role list in
   `OMSP-PLANNING-GOLDEN-PATH-0001` §5.1, with a published unknowns count
   per model file (`unknown` values allowed, never hidden).
3. Model passes schema, ontology, referential-integrity, and
   provenance-completeness validation in CI (golden-path evidence items
   §6.2–§6.5) — the Sprint-8 visible outcome.
4. Verified, sourced, observed, assumed, and unknown data are mechanically
   distinguishable (provenance validator rejects any non-`unknown` value
   without source ID + authority class + confidence).
5. ODS-200/400/500/600 Draft sections and Marine Diagram System (MDS) v0.1
   are merged.
6. Sprint-9 can execute operational scenarios directly from the model
   (scenario schema fields consumed by the model are complete).

### 3.3 Sprint-9 — EPIC #173: Operational Scenarios & Five-Minute Demo (v0.6.0)

1. Three scenario instances are merged and validate against the scenario
   schema: service-battery critical voltage (primary), shore-power loss,
   maintenance-due.
2. Scenario outputs are derived from validated model relationships
   (interface graph), not hand-listed narrative; checked by referential
   integrity of every scenario step to equipment roles and source entries.
3. The report generator renders the human-readable advisory output from the
   model in CI with zero manual steps, conformant to ODS-100/300 Draft, and
   byte-reproducible from repository sources.
4. The five-minute demo passes its pass criteria
   (`OMSP-PLANNING-GOLDEN-PATH-0001` §9) in a recorded run — the Sprint-9
   visible outcome.
5. Core Operations Manual skeleton (MODS-conformant) is merged.
6. A human validation outcome (Validated / Validated with Exceptions / Not
   Validated / Deferred) is recorded against the golden-path problem
   statement — this is the v0.6.0 release gate input.

### 3.4 Sprint-10 — EPIC #174: Second Maritime Domain Slice (v0.6.1)

1. A second vessel-system domain (preferred: fresh-water, bilge and pumping
   systems) is modeled and passes the **unchanged** core validator pipeline.
2. No electrical assumption leaks into common schemas or tooling: the diff
   of `schemas/` core files shows extensions only, no electrical-specific
   modifications to shared definitions.
3. At least one cross-system dependency relationship (e.g., bilge pump →
   DC distribution) is modeled and rendered in scenario output.
4. Scenario Library v0.1 exists with validated entries from both domains.
5. Maintenance and failure relationships for the second domain are modeled
   with sourced or explicitly `unknown` values.

### 3.5 Sprint-11 — EPIC #175: Multi-Vessel Platform Proof (v0.7.0)

1. VDM–Hanse 460 delta module separates platform core, vessel profile, and
   vessel-instance data.
2. A second vessel profile with materially different equipment/topology is
   generated using OMSP tooling and passes the same core validation
   pipeline; generator output contains real differentiated system data,
   not copied scaffolding.
3. Zero vessel-specific changes to core platform code are needed for the
   second vessel (verified by diff review).
4. Cross-vessel schema compatibility and variation points are documented.

### 3.6 Sprint-12 — EPIC #176: Controlled Design Partner Pilot (v0.8.0)

1. QRH v0.1 is generated fully source-traceable from the model; automated
   PDF pipeline produces the publication artifact in CI.
2. At least three structured evaluations completed (vessel owner, marine
   specialist, systems/software engineer).
3. At least one external participant attempts to model real equipment or
   system data; effort and failure points are recorded.
4. Pilot entry, pause, abort, and exit criteria are exercised and recorded.
5. Persistent risks RR-001–RR-005 are reassessed using pilot evidence
   (re-entry of the deferred item from WP-0059 / #144).

### 3.7 Sprint-13 — EPIC #177: Community & Contributor Readiness (v0.9.0)

1. Contributor guide, first-contribution path, and domain-data contribution
   templates are published.
2. A curated `good first issue` set exists.
3. At least one external issue, PR, or domain-data contribution is
   received; contribution effort and failure points are measured.
4. Monorepo ADR re-evaluation trigger T1 is executed
   (`governance/ADR-0001-REPOSITORY-TOPOLOGY.md`).
5. Public materials contain no claims exceeding actual maturity.

### 3.8 Sprint-14+ — EPIC #178: v1.0 Stabilization (v1.0.0)

Exit criteria are the v1.0 gates recorded in issue #178 (stable core
ontology; schema versioning + migration mechanism; ≥2 vessel types; ≥2
system domains; ≥3 operational scenarios; external design-partner
validation; security/provenance/release controls; documented CLI or API
entry points; ≥1 external contribution) plus MODS Specification v1.0
release candidate. Human release approval confirms all gates.

## 4. Sprint 7–9 Work Package Breakdown (implementation-ready)

Numbering starts at WP-0077. Effort scale: S=1, M=2, L=3 points. Golden-path
implementation slices (a)–(e) refer to `OMSP-PLANNING-GOLDEN-PATH-0001` §13.

### Sprint-7 (epic #171, milestone v0.6.0)

#### WP-0077 — Maritime Core Ontology v0.1

- **Objective:** Extend `OMSP-ONTOLOGY-CORE-0001` with maritime domain
  concepts and relations: vessel, system, equipment role, port, interface,
  connection, protection, measurement, scenario, source/provenance.
- **User Value:** Owners and technicians get a shared, machine-checkable
  vocabulary; every later model element means one thing.
- **Evidence Produced:** Ontology artifact merged; `validate_ontology.py`
  green in CI; mapping table core→maritime concepts.
- **Acceptance (summary):** All §5.1 golden-path roles expressible; no
  vessel- or electrical-only concept in the core layer; validator passes.
- **Dependencies:** WP-0074 definition (merged). — **Effort:** L (3).
  **Category:** domain/data.

#### WP-0078 — Vessel & Equipment YAML Schemas v0.1

- **Objective:** JSON Schemas in `schemas/` for vessel, system, equipment,
  interface, connection, and scenario instances, including the mandatory
  provenance block (source ID, authority class, confidence, retrieval date,
  applicability) and explicit `unknown` representation.
- **User Value:** Real vessel data can be captured once, validated
  mechanically, and trusted downstream.
- **Evidence Produced:** Schemas merged; schema-validation CI gate active;
  negative test fixtures rejected.
- **Acceptance (summary):** Every golden-path §5.1 role and §8 scenario
  shape is expressible; provenance block required on all value-bearing
  fields; CI gate blocks invalid instances.
- **Dependencies:** WP-0077. — **Effort:** L (3). **Category:** domain/data.

#### WP-0079 — MODS Specification v0.1 Skeleton + ODS-100/ODS-300 Draft

- **Objective:** Create the MODS Specification skeleton and draft ODS-100
  (document structure) and ODS-300 (procedural step language) — the minimal
  sections required before any rendered operational content (spec-first
  gate).
- **User Value:** Rendered outputs follow a consistent, reviewable
  operational-documentation standard from the first instance.
- **Evidence Produced:** MODS spec artifact(s) merged with Status: Draft;
  conformance checklist for renderers.
- **Acceptance (summary):** ODS-100 defines document structure for the
  golden-path output (§7.1 sections); ODS-300 defines step language
  compatible with `OMSP-REFERENCE-SCENARIO-0001` §7; explicitly marked
  Draft, subject to first-conformance-test revision in Sprint 9.
- **Dependencies:** WP-0074 §7.2. — **Effort:** M (2).
  **Category:** documentation.

#### WP-0080 — Domain Validation Rules + Compliant Sample Package

- **Objective:** Implement domain validation rules (schema + ontology
  conformance run) and deliver a representative sample maritime model
  package that passes all domain validators — including one non-electrical
  placeholder concept to prove domain neutrality.
- **User Value:** Proof, before real data entry, that the foundation
  validates end-to-end — Sprint-7's visible domain outcome.
- **Evidence Produced:** CI run with 0 findings on the sample package;
  validator invocation documented.
- **Acceptance (summary):** Sample package covers every schema type; the
  pipeline is one documented command chain; failure fixtures fail.
- **Dependencies:** WP-0077, WP-0078. — **Effort:** M (2).
  **Category:** tooling (1) + domain/data (1).

### Sprint-8 (epic #172, milestone v0.6.0)

#### WP-0081 — Hanse 460 Source Capture & Register Extension (slice a)

- **Objective:** Register the owner-held Hanse 460 documentation set in
  `reference/HANSE_460_SOURCE_REGISTER.md` (or successor) with source ID,
  owner, authority class, retrieval date, applicability.
- **User Value:** Every later claim about the boat is traceable to a named
  source; rumor and fact are separated.
- **Evidence Produced:** Extended register merged; each entry passes
  register-contract checks.
- **Acceptance (summary):** All input classes of golden-path §4.1 covered
  or explicitly absent; no value entered from memory; inaccessible sources
  produce `unknown`, not gaps.
- **Dependencies:** none hard (register exists); precedes WP-0082 values.
  — **Effort:** M (2). **Category:** domain/data.

#### WP-0082 — Hanse 460 Electrical-Slice YAML Model (slice b)

- **Objective:** Author the electrical-slice model under
  `reference/hanse460/`: all §5.1 roles, typed interfaces, protection,
  measurement points, document references — every value sourced or
  `unknown`.
- **User Value:** The first real, provenance-carrying structured model of
  the reference vessel — the core of what OMSP *is* for its users.
- **Evidence Produced:** Model files merged; schema validation green;
  published unknowns count per file.
- **Acceptance (summary):** 100% role coverage; identity pattern
  `equipment:<configuration-id>:<local-id>`; conflicting claims kept side
  by side; boundary rule respected (no silent scope accretion).
- **Dependencies:** WP-0078, WP-0081. — **Effort:** L (3).
  **Category:** domain/data.

#### WP-0083 — Validator Extensions: Referential Integrity & Provenance Completeness (slice c)

- **Objective:** Extend the validator family for golden-path evidence
  §6.4–§6.5: interface endpoints → existing ports; scenario steps →
  existing roles; document references → register entries; zero
  non-`unknown` values without full provenance.
- **User Value:** Users can trust that the rendered answer is mechanically
  consistent with the model and its sources.
- **Evidence Produced:** New/extended validator scripts in `tooling/` with
  CI wiring; failing fixtures demonstrably fail.
- **Acceptance (summary):** All four integrity classes checked; JSON
  findings output consistent with `omsp_validate.py` conventions; runs in
  the standard quality gate.
- **Dependencies:** WP-0078 (schema shapes). — **Effort:** M (2).
  **Category:** tooling.

#### WP-0084 — ODS-200/400/500/600 Draft + Marine Diagram System v0.1

- **Objective:** Draft the remaining ODS series sections and MDS v0.1
  (diagram conventions for energy chain and interface views).
- **User Value:** The full operational-documentation product stack has a
  defined shape before content scales in Sprint 9–10.
- **Evidence Produced:** Draft artifacts merged; MDS applied to at least
  one golden-path diagram.
- **Acceptance (summary):** Each ODS section has scope, structure, and
  conformance notes; Draft status explicit; no content instance is blocked
  on non-minimal sections (only ODS-100/300 gate rendering).
- **Dependencies:** WP-0079. — **Effort:** M (2).
  **Category:** documentation.

### Sprint-9 (epic #173, milestone v0.6.0)

#### WP-0085 — Primary Scenario Instance: Service-Battery Critical Voltage (slice d)

- **Objective:** Author
  `scenario:hanse:460:service-battery-critical-voltage:0.1.0` per
  golden-path §8: affected systems derived from the interface graph, cause
  taxonomy, inspection sequence, safety constraints, related equipment,
  source manuals.
- **User Value:** The first real operational answer: "battery is critical —
  what does that mean on this boat?"
- **Evidence Produced:** Scenario instance merged; scenario-schema and
  referential-integrity validation green; threshold values sourced or
  `<to-be-sourced>`/`unknown`.
- **Acceptance (summary):** Conforms to `OMSP-REFERENCE-SCENARIO-0001`;
  every inspection step references ≥1 equipment role and ≥1 source (or
  explicit unknown marker); stop/abort conditions and conservative
  human-review branch present.
- **Dependencies:** WP-0082, WP-0083 ((a),(b) → (d) ordering).
  — **Effort:** M (2). **Category:** domain/data.

#### WP-0086 — Additional Scenarios: Shore-Power Loss & Maintenance-Due

- **Objective:** Author the two remaining v0.6.0 scenarios using the
  WP-0085 pattern, including at least one maintenance relationship.
- **User Value:** Demonstrates the scenario mechanism generalizes beyond a
  single hand-tuned case.
- **Evidence Produced:** Two validated scenario instances; same evidence
  classes as WP-0085.
- **Acceptance (summary):** Same rigor as WP-0085; shared cause-taxonomy
  entries reused, not duplicated.
- **Dependencies:** WP-0085. — **Effort:** M (2). **Category:** domain/data.

#### WP-0087 — Report Generator & Human-Readable Output (slice e)

- **Objective:** Implement the generator rendering the golden-path §7.1
  output (system overview, scenario section, evidence appendix, advisory
  banner) from the YAML model, Markdown-first, in CI with zero manual
  steps.
- **User Value:** The user-visible product: an advisory, source-attributed
  answer document.
- **Evidence Produced:** Generator in `tooling/`; CI-generated output;
  byte-reproducibility check; ODS-100/300 conformance check.
- **Acceptance (summary):** No claim absent from the model; unknowns
  rendered, not hidden; advisory banner fixed text; conformant to
  ODS-100/300 Draft (spec-first gate satisfied by WP-0079).
- **Dependencies:** WP-0079 (binding spec-first gate), WP-0085.
  — **Effort:** L (3). **Category:** tooling.

#### WP-0088 — Core Operations Manual Skeleton

- **Objective:** Assemble the MODS-conformant Core Operations Manual
  skeleton with the three scenarios as its first abnormal-procedure
  content, all derived from the model.
- **User Value:** Shows users the shape of the full operational
  documentation product.
- **Evidence Produced:** Manual skeleton merged; ODS conformance checklist
  applied.
- **Acceptance (summary):** Structure follows ODS-100; content only via
  the generator (single source of truth); gaps explicit.
- **Dependencies:** WP-0079, WP-0087. — **Effort:** S (1).
  **Category:** domain/data.

#### WP-0089 — Five-Minute Demo Assembly & v0.6.0 Release Readiness

- **Objective:** Assemble and record the five-minute demo (golden-path §9)
  and prepare the v0.6.0 release-readiness evidence package.
- **User Value:** A reproducible demonstration any stakeholder can watch or
  re-run — the proof the golden path exists.
- **Evidence Produced:** Recorded demo run meeting pass criteria; release
  checklist with validator evidence; human validation outcome recorded.
- **Acceptance (summary):** Demo ≤5 minutes, reproducible from the
  repository alone; v0.6.0 gate items (Section 7) evidenced; release
  publication remains a human decision.
- **Dependencies:** all Sprint 7–9 WPs. — **Effort:** M (2).
  **Category:** domain/data (1, demo) + governance (1, release evidence).

## 5. Dependency Record

Binding chain (ontology → schema → real data → validation → report
generation):

| Order | Stage | Work Packages | Feeds |
| --- | --- | --- | --- |
| 1 | Ontology | WP-0077 | WP-0078, WP-0080 |
| 2 | Schemas | WP-0078 | WP-0080, WP-0082, WP-0083 |
| 3 | Real data (sources → model) | WP-0081 → WP-0082 | WP-0085 |
| 4 | Validation | WP-0080 (sample), WP-0083 (extensions) | WP-0085, WP-0086 |
| 5 | Scenarios | WP-0085 → WP-0086 | WP-0087 |
| 6 | Report generation | WP-0087 → WP-0088 | WP-0089 |
| — | MODS spec track (parallel, spec-first) | WP-0079 → WP-0084 | gates WP-0087, WP-0088 |

Ordering constraints restated from `OMSP-PLANNING-GOLDEN-PATH-0001` §13:
slices (a) WP-0081 and (b) WP-0082 precede (d) WP-0085; the minimal MODS/ODS
Draft sections (WP-0079) precede (e) WP-0087.

Critical path: WP-0077 → WP-0078 → WP-0082 → WP-0085 → WP-0087 → WP-0089.

Sprint visible outcomes (rule 2.1): Sprint-7 = validated sample maritime
model package (WP-0080); Sprint-8 = sourced Hanse 460 electrical model
passing full validation (WP-0082/0083); Sprint-9 = rendered advisory report
and recorded five-minute demo (WP-0087/0089).

## 6. Capacity Policy Application (Sprint 7–9)

Target: 65% domain/data, 20% tooling, 10% documentation, 5% governance.
Effort points: S=1, M=2, L=3; fractional attribution where a Work Package
spans categories. Tolerance rule: each planning window must land within ±5
percentage points of target per category; deviations beyond tolerance
require a recorded planning decision.

| WP | Effort | Domain/Data | Tooling | Documentation | Governance |
| --- | --- | --- | --- | --- | --- |
| WP-0077 | 3 | 3 | — | — | — |
| WP-0078 | 3 | 3 | — | — | — |
| WP-0079 | 2 | — | — | 2 | — |
| WP-0080 | 2 | 1 | 1 | — | — |
| WP-0081 | 2 | 2 | — | — | — |
| WP-0082 | 3 | 3 | — | — | — |
| WP-0083 | 2 | — | 2 | — | — |
| WP-0084 | 2 | — | — | 2 | — |
| WP-0085 | 2 | 2 | — | — | — |
| WP-0086 | 2 | 2 | — | — | — |
| WP-0087 | 3 | — | 3 | — | — |
| WP-0088 | 1 | 1 | — | — | — |
| WP-0089 | 2 | 1 | — | — | 1 |
| **Total** | **29** | **18 (62.1%)** | **6 (20.7%)** | **4 (13.8%)** | **1 (3.4%)** |

Assessment: within the ±5-point tolerance on every category. Domain/data
runs 2.9 points under target and documentation 3.8 over because Sprint 7–9
carry the one-time MODS/ODS specification investment that the spec-first
rule requires before content scales; Sprint 10–11 planning shall rebalance
toward domain/data (Scenario Library, second domain slice, second vessel
are almost entirely domain work).

## 7. Release Gates (measurable)

| Release | Gate (all items required; release publication is a human decision) |
| --- | --- |
| **v0.5.1** | All Sprint-6 WPs (WP-0070–0076) merged or formally deferred; `omsp_validate.py` on governed paths = 0 findings; quality gate green; no duplicate active authority domain; root docs aligned; golden-path definition and this backlog approved. |
| **v0.6.0** | Epics #171–#173 exit criteria met (Sections 3.1–3.3); golden-path success conditions §11.1–§11.6 evidenced; recorded five-minute demo passes; human validation outcome recorded; CI fully green on `develop`. |
| **v0.6.1** | Epic #174 exit criteria met (Section 3.4); second domain passes unchanged core pipeline; ≥1 cross-system relationship rendered; Scenario Library v0.1 with validated entries from two domains. |
| **v0.7.0** | Epic #175 exit criteria met (Section 3.5); second vessel profile generated and validated with zero vessel-specific core changes; variation points documented. |
| **v0.8.0** | Epic #176 exit criteria met (Section 3.6); ≥3 structured evaluations; ≥1 external modelling attempt; QRH v0.1 + PDF pipeline in CI; RR-001–RR-005 reassessed with pilot evidence. |
| **v0.9.0** | Epic #177 exit criteria met (Section 3.7); ≥1 external contribution received and measured; contributor path published; ADR-0001 trigger T1 executed. |
| **v1.0.0** | All #178 gates evidenced (Section 3.8); schema/ontology SemVer commitment and migration mechanism demonstrated on an existing vessel model; MODS Specification v1.0 release candidate; explicit human release approval. |

## 8. Deferred Governance Work (does not feed the golden path)

Each item stays deferred until its re-entry trigger fires; deferral was
established by the Sprint-6 reorientation (#145) and WP-0059 (#144).

| Deferred item | Origin | Re-entry trigger |
| --- | --- | --- |
| Persistent-risk reassessment RR-001–RR-005 | #144 / WP-0059 | Design-partner pilot evidence (Sprint-12, WP under epic #176) |
| Signed provenance & immutable audit evidence | retired WP-0062 (#150) | Pilot or external-contribution security need (Sprint-12/13) |
| Remote telemetry, alerting & evidence retention | retired WP-0063 (#151) | Any live-data ingestion decision (explicitly out of golden-path scope) |
| Vulnerability intelligence & history secret scanning | retired WP-0064 (#152) | Community opening (Sprint-13) |
| Performance, availability & capacity qualification | retired WP-0065 (#153) | First hosted/service component (none planned before v1.0) |
| External backup & disaster-recovery infrastructure | retired WP-0066 (#154) | Same as above |
| Controlled pilot environment & access-control baseline | retired WP-0061 (#149) | Sprint-12 pilot preparation (folded into epic #176 planning) |
| Monorepo ADR re-evaluation | ADR-0001 | Trigger T1 at Sprint-13 (epic #177) |
| Further foundation/governance consolidation beyond WP-0072 | audit disposition | Only if a validator or authority conflict blocks domain work |
| Contributor governance (CLA, review tiers) | epic #177 | Sprint-13 |

## 9. Proposed GitHub Issues (human-approved step; not yet opened)

| Proposed issue title | Epic | Milestone | Sprint |
| --- | --- | --- | --- |
| WP-0077: Maritime Core Ontology v0.1 | #171 | v0.6.0 | 7 |
| WP-0078: Vessel & Equipment YAML Schemas v0.1 | #171 | v0.6.0 | 7 |
| WP-0079: MODS Specification v0.1 Skeleton + ODS-100/300 Draft | #171 | v0.6.0 | 7 |
| WP-0080: Domain Validation Rules & Compliant Sample Package | #171 | v0.6.0 | 7 |
| WP-0081: Hanse 460 Source Capture & Register Extension | #172 | v0.6.0 | 8 |
| WP-0082: Hanse 460 Electrical-Slice YAML Model | #172 | v0.6.0 | 8 |
| WP-0083: Validator Extensions — Referential Integrity & Provenance | #172 | v0.6.0 | 8 |
| WP-0084: ODS-200/400/500/600 Draft + Marine Diagram System v0.1 | #172 | v0.6.0 | 8 |
| WP-0085: Primary Scenario — Service-Battery Critical Voltage | #173 | v0.6.0 | 9 |
| WP-0086: Scenarios — Shore-Power Loss & Maintenance-Due | #173 | v0.6.0 | 9 |
| WP-0087: Report Generator & Human-Readable Output | #173 | v0.6.0 | 9 |
| WP-0088: Core Operations Manual Skeleton | #173 | v0.6.0 | 9 |
| WP-0089: Five-Minute Demo Assembly & v0.6.0 Release Readiness | #173 | v0.6.0 | 9 |

Sprint 10–14 Work Packages are intentionally not numbered here; they are
broken down at each sprint's planning against the epic exit criteria of
Section 3, so that numbering follows actual sequence of commitment.

## 10. Approval Boundary

This artifact is advisory planning input. Committing Sprint 7, opening the
WP-0077–0089 issues, accepting the capacity assessment, and every release
decision in Section 7 require explicit human approval by the accountable
maintainer. AI assistance drafted this backlog; it approves nothing.
