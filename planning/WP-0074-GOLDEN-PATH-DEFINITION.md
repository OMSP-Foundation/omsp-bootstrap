---
Artifact-ID: OMSP-PLANNING-GOLDEN-PATH-0001
Title: WP-0074 Hanse 460 Golden Path Product Definition
Version: 0.1.0
Status: Draft
Owner: toss-cengiz
Baseline: Sprint-6
Classification: Public
Related-Issue: WP-0074 / #168
Traceability:
  - ISSUE-168
  - OMSP-CANON-METHODOLOGY-0001
  - OMSP-REFERENCE-CONFIG-0001
  - OMSP-REFERENCE-SOURCE-0001
  - OMSP-REFERENCE-EQUIPMENT-0001
  - OMSP-REFERENCE-SCENARIO-0001
  - OMSP-VAL-VALIDATION-0001
---

# WP-0074 — Hanse 460 Golden Path Product Definition

## 1. Purpose and Boundary of This Artifact

This artifact defines the first complete OMSP product slice: the **golden
path** from real Hanse 460 electrical-system data to a validated domain model
and a human-readable operational output, anchored on one primary scenario
(critical service-battery voltage).

This is a **definition artifact, not an implementation artifact**. It fixes
the user, problem, inputs, model boundary, validator evidence, output
specification, demo storyboard, exclusions, and success conditions — so that
implementation work in Sprint 7–9 can begin without unresolved core product
questions. No YAML model, schema, tooling, or publication code is delivered
by this Work Package.

Methodology anchor: the golden path is a direct application of the core triad
(Knowledge First • Models Before Code • Traceability by Design) and the
layered digital-twin method (`OMSP-CANON-METHODOLOGY-0001` §2, §3.7). This
definition precedes all code, per Models Before Code.

## 2. User and Problem Statement

### 2.1 Primary users

1. **Vessel owner (owner-operator of a Hanse 460 class sailing yacht).**
   Operates the vessel with limited crew, often single- or double-handed. Has
   the boat's paper manuals scattered across binders and PDFs. When an
   electrical anomaly occurs at anchor or under way, needs to understand —
   quickly and without deep electrical expertise — what is affected, what the
   plausible causes are, in what order to check things, and where the
   authoritative documentation is.
2. **Marine technician (independent service engineer).** Arrives at an
   unfamiliar boat. Needs a trustworthy, source-attributed picture of the
   electrical architecture — what feeds what, through which protection, with
   which measurement points — before touching anything, and needs to know
   which claims are manufacturer-verified versus assumed.

### 2.2 Problem statement

Today, the knowledge needed to answer "the service battery is critically low
— what does that mean for this boat, right now?" exists only as a mental
model of the owner plus a pile of disconnected vendor manuals. There is:

- no single structured model connecting energy sources, storage,
  distribution, protection, and consumers;
- no provenance — no way to distinguish a verified manufacturer limit from a
  forum rumor;
- no traceable link from an operational symptom to affected systems, likely
  causes, an inspection sequence, and the exact source documents.

### 2.3 What OMSP does for these users (value statement)

OMSP turns the vessel's electrical-system knowledge into a governed,
provenance-carrying model, validates it mechanically, and renders it into a
human-readable output that answers the primary scenario question with
explicit evidence classes and explicit unknowns. The user gets an **advisory
knowledge product**, not an autopilot: every safety-relevant conclusion
requires human judgment.

## 3. Golden Path Definition

```text
Real vessel data
  → domain model (YAML, single source of truth)
    → schema and ontology validation (CI, repeatable)
      → system and interface relationships (traceability queries)
        → operational scenario (service-battery critical voltage)
          → human-readable output (advisory, source-attributed)
```

The YAML model layer is the **single source of truth**; every downstream
artifact (relationship views, scenario rendering, human-readable output) is
derived, never hand-maintained in parallel (docs-as-code single-source rule,
`OMSP-CANON-METHODOLOGY-0001` §3.6).

## 4. Input and Provenance Definition

### 4.1 Input classes

Inputs to the golden path are facts about the Hanse 460 electrical energy
system, each carried with the authority classification already established in
`OMSP-REFERENCE-CONFIG-0001` §3 and `OMSP-REFERENCE-SOURCE-0001`:

| Authority class | Meaning | Golden-path usage |
| --- | --- | --- |
| `reference` | OMSP modeling structure or placeholder | Allowed for structure (roles, ports, interface types) |
| `sourced-secondary` | Transcribed from a named secondary source | Allowed, flagged; never rendered as manufacturer fact |
| `sourced-manufacturer` | Transcribed from accessible manufacturer documentation | Preferred class for equipment values |
| `verified-design` | Verified against controlled design evidence | Requires accountable human promotion |
| `verified-as-built` | Verified on the physical vessel | Requires vessel-instance evidence; out of scope for v0.1.0 |
| `unknown` | Not established by current evidence | Mandatory explicit representation; never silently omitted |

### 4.2 Expected input sources

- **Owner-held vessel documentation** for the reference Hanse 460:
  manufacturer owner's manual, electrical wiring diagrams, and equipment
  vendor manuals (battery, charger, inverter, shore-power installation).
  Each captured source must be registered in
  `reference/HANSE_460_SOURCE_REGISTER.md` (or a successor register entry)
  with source ID, owner, class, retrieval date, and applicability, following
  the existing register contract.
- **Direct vessel observation** (photographs of panels, breaker labels,
  battery nameplates) — classified per the register's promotion rules; such
  evidence supports `verified-as-built` claims only through the promotion
  procedure of `OMSP-REFERENCE-SOURCE-0001` §5 and is not required for the
  first golden-path iteration.
- **Existing OMSP reference artifacts**: system identifier
  `system:vessel-design:hanse:460:electrical` and the equipment/interface
  contracts of `OMSP-REFERENCE-EQUIPMENT-0001`.

### 4.3 Provenance rules (binding)

1. Every non-`unknown` value in the golden-path model carries: source ID,
   authority class, confidence, retrieval date, and applicability context.
2. No electrical specification (voltage thresholds, capacities, fuse ratings,
   charge parameters) may be entered from memory or general knowledge; a
   value without a captured source is recorded as `unknown` or explicitly
   marked `<to-be-sourced>` during drafting.
3. Conflicting claims remain side by side per `OMSP-REFERENCE-CONFIG-0001`
   §8; safety-relevant conflicts block promotion.

## 5. Domain-Model Boundary

### 5.1 In scope (the modeled slice)

All items are **configuration items** (equipment roles) under
`configuration:vessel-design:hanse:460:reference-0.1.0`, system
`system:vessel-design:hanse:460:electrical`, using the identity pattern
`equipment:<configuration-id>:<local-id>` from
`OMSP-REFERENCE-EQUIPMENT-0001` §3:

| Local role ID (proposed) | Role | Notes |
| --- | --- | --- |
| `shore-power-inlet` | Shore power inlet and AC supply path | Nominal supply, inlet protection: `<to-be-sourced>` |
| `service-battery-bank` | Service (house) battery bank | Chemistry, nominal voltage, capacity: `<to-be-sourced>` |
| `battery-charger` | Shore-powered battery charger | Rating and charge profile: `<to-be-sourced>` |
| `alternator-charging` | Engine-driven charging source | Modeled as charging source role only |
| `inverter` | DC→AC inverter | Rating and transfer behavior: `<to-be-sourced>` |
| `dc-main-distribution` | Main DC distribution panel/bus | Bus topology: `<to-be-sourced>` |
| `dc-consumer-*` | Selected consumers (small named set) | Candidate set: navigation instruments, refrigeration, cabin lighting, bilge pump — final set fixed at implementation with sources |
| `protection-*` | Fuses, breakers, main battery switches | Ratings and locations: `<to-be-sourced>` |
| `measurement-*` | Voltage/current measurement points | Battery monitor / panel meters: `<to-be-sourced>` |

Also in scope:

- typed interfaces among the above (families `electrical-power`,
  `safety-protection`, `data-signal`, `human`, `procedural` per
  `OMSP-REFERENCE-EQUIPMENT-0001` §6);
- document references binding each role to its source manual entry;
- the single primary operational scenario (Section 8).

### 5.2 Explicitly out of scope

- Engine start battery and engine starting circuit (beyond naming the
  alternator as a charging source role).
- Bow thruster, windlass, and other high-current dedicated circuits.
- Solar, wind, hydro, fuel-cell, or generator charging sources.
- AC distribution beyond the shore-inlet → charger (and inverter output
  role) path; no AC consumer inventory.
- NMEA 2000 / SignalK network topology and live telemetry ingestion (the
  measurement roles are modeled as points, not as a live data pipeline).
- Lightning protection, galvanic isolation/bonding, corrosion systems.
- All non-electrical systems of the Hanse 460 decomposition.
- Any vessel-instance (`verified-as-built`) assertion; the slice remains a
  design-family reference configuration.
- Any automation acting on the vessel; the golden path is read-only
  knowledge, never control.

Boundary rule: an item outside this list may enter the slice only through a
scope-change decision recorded against this artifact (new version), not by
silent accretion.

## 6. Expected Validator Evidence

The golden path is complete only when the following mechanical evidence
exists, reproducible in CI from repository sources alone:

1. **Governed metadata validation** — `python3 tooling/omsp_validate.py
   governance planning roadmap architecture knowledge reference schemas
   validation` returns **0 findings** including all new golden-path
   artifacts.
2. **Schema validation** — every golden-path YAML model instance validates
   against a JSON Schema in `schemas/` (equipment/interface/scenario
   instance schemas; to be created or extended in the implementation Work
   Packages). Validation is a CI gate, not a manual step.
3. **Ontology conformance** — model concepts and relations map to
   `OMSP-ONTOLOGY-CORE-0001` identifiers; `tooling/validate_ontology.py`
   (extended as needed) passes.
4. **Referential integrity** — every interface endpoint references an
   existing port; every scenario step references existing equipment roles;
   every document reference resolves to a source-register entry. Checked
   mechanically (new or extended validator), per
   `OMSP-REFERENCE-EQUIPMENT-0001` §12.
5. **Provenance completeness** — zero non-`unknown` values without source
   ID + authority class + confidence; checked mechanically.
6. **Quality gate** — `python3 tooling/omsp_quality_gate.py` passes.

Verification vs. validation split (`OMSP-VAL-VALIDATION-0001`): items 1–6
are **verification**. **Validation** (did we build the right thing) is the
human judgment that the rendered output actually answers the Section 2
problem statement — recorded as a validation outcome (Validated / Validated
with Exceptions / Not Validated / Deferred) by the accountable human.

## 7. Human-Readable Output Specification

### 7.1 What is rendered

One generated, human-readable document (Markdown first; PDF via the
publication pipeline later) containing, for the modeled slice:

1. **System overview** — the energy chain (shore power → charger → battery
   bank → DC distribution → consumers; inverter branch), with each element's
   role, key values (or explicit `unknown`), and protection.
2. **Scenario section** — the critical service-battery-voltage scenario
   rendered as: affected systems, likely causes, inspection sequence, safety
   constraints, related equipment, and supporting source documents — each
   line item traceable to a model element and a source-register entry.
3. **Evidence appendix** — authority class and source for every rendered
   claim; unknowns listed, not hidden.
4. **Advisory banner** — fixed text stating the output is advisory, is not a
   certified procedure, carries no seaworthiness or navigation-safety claim,
   and requires human judgment (Section 12).

### 7.2 Relationship to MODS/ODS (spec-first ordering note)

This output is the **precursor of the MODS Core Operations Manual /
Abnormal-procedure format**. The MODS/ODS document standards (ODS-100
structure, ODS-300 procedural language) are not yet drafted; therefore:

- This artifact is a **requirements/product definition**, not a content
  instance — producing it does not violate the "standard before content"
  ordering of the spec-first product architecture. It is, in fact, an input
  that MODS drafting will consume.
- Before the first *rendered output instance* is produced in Sprint 7–9, the
  minimal relevant MODS/ODS sections (document structure and
  abnormal-procedure step language) must exist at least in Draft status; the
  golden-path output then becomes the first conformance test of those
  sections.
- The output format is a derived view of the YAML model (single source of
  truth); no content may exist only in the rendered document.

## 8. Primary Scenario — Critical Service-Battery Voltage

Defined per the contract of `OMSP-REFERENCE-SCENARIO-0001`; the full scenario
instance is an implementation deliverable. This section fixes its shape.

| Field | Definition |
| --- | --- |
| Scenario ID | `scenario:hanse:460:service-battery-critical-voltage:0.1.0` |
| Class | `degraded` |
| Applicability | `vessel-design:hanse:460`, `configuration:vessel-design:hanse:460:reference-0.1.0` — design-family reference, not vessel-specific instruction |
| Accountable authority | Skipper (human); software role is monitoring/advisory only |
| Trigger | Observed or reported service-battery voltage at or below a critical threshold. The threshold value is battery-chemistry- and manufacturer-specific: `<to-be-sourced>` from the battery manufacturer's documentation; never asserted from general knowledge. Trigger source, timestamp, and confidence recorded per `OMSP-REFERENCE-SCENARIO-0001` §6 |
| Preconditions | Configuration applicability confirmed; measurement source identified (which meter/monitor, its authority and calibration state — `unknown` allowed but explicit) |

The scenario definition must enumerate, each traceable to model elements:

1. **Affected systems** — consumers fed from the service bank via
   `dc-main-distribution` (navigation instruments, refrigeration, lighting,
   bilge pump per the final consumer set), the inverter and its AC loads;
   derived from the interface graph, not hand-listed.
2. **Likely causes** — as a cause taxonomy with evidence requirements
   (e.g., charging-source failure, excessive consumer load, protection
   device open, battery degradation, measurement error). Each cause links
   to the equipment roles and interfaces it implicates. No probability
   claims without evidence.
3. **Inspection sequence** — ordered check steps with responsible actor,
   entry/completion criteria, expected observation, and escalation handling
   per `OMSP-REFERENCE-SCENARIO-0001` §7. The sequence is a *reference*
   inspection order, not an approved vessel procedure.
4. **Safety constraints** — explicit hazards and safeguards, minimally:
   electrical hazard during inspection, load-shedding decisions affecting
   navigation and bilge capability (human decision only), no instruction to
   bypass protection devices, and a conservative stop condition routing
   ambiguity to the human skipper.
5. **Related equipment** — the in-scope roles of Section 5.1 touched by the
   scenario.
6. **Source manuals** — document references (source-register entries) for
   every equipment role cited in causes and inspection steps.

Unacceptable outcome classes, stop/abort conditions, and the rule that
unknown or conflicting evidence routes to a conservative human-reviewed
branch are mandatory scenario fields.

## 9. Five-Minute Demo Storyboard

Target audience: Cengiz (as owner) or a marine technician. Constraint: the
entire demo is reproducible from the repository by CI or a single documented
command chain — no manual editing, no out-of-repo assets.

| Minute | Step | What is shown | Evidence |
| --- | --- | --- | --- |
| 0:00–1:00 | **The question** | "Service battery voltage is critical — what does that mean on this boat?" Show the golden-path diagram and the problem statement | This artifact §2–§3 |
| 1:00–2:00 | **The model** | Open the YAML model of the electrical slice: roles, interfaces, protection, measurements — each value with authority class or `unknown` | Model files under `reference/hanse460/` (implementation WP) |
| 2:00–3:00 | **The proof** | Run the validator chain live (or show the CI run): schema + ontology + referential integrity + provenance completeness → 0 findings | §6 commands and CI logs |
| 3:00–4:00 | **The relationships** | Show a traceability view: battery bank → distribution → affected consumers; scenario steps → equipment → source manuals | Derived relationship output |
| 4:00–5:00 | **The answer** | Render/show the human-readable output for the critical-voltage scenario: affected systems, likely causes, inspection sequence, safety constraints, sources — with the advisory banner | §7 output, generated in CI |

Demo pass criteria (measurable): completes in ≤ 5 minutes; every displayed
claim carries a visible authority class; validator run shows 0 findings; the
rendered output is byte-reproducible from repository sources on CI.

## 10. Explicit Exclusions and Assumptions

### 10.1 Exclusions

- No implementation is delivered by WP-0074 (definition only).
- No live telemetry, sensor integration, or NMEA 2000/SignalK ingestion.
- No vessel-instance claims; no `verified-as-built` data required for v1 of
  the golden path.
- No alarm-threshold, limit, or capacity value asserted without a captured
  source; all such values are `<to-be-sourced>` until registered.
- No control, automation, or actuation of any vessel system.
- No certified procedure, no seaworthiness, compliance, or
  navigation-safety claim; output does not replace manufacturer manuals or
  skipper judgment (per
  `reference/DIGITAL_TWIN_GOVERNANCE_AND_SAFETY_BOUNDARIES.md`).
- No second vessel type, no generalization claims (Horizon 3 concern).

### 10.2 Assumptions

1. Owner-held Hanse 460 documentation (owner's manual, wiring diagrams,
   equipment vendor manuals) is accessible for source capture during
   Sprint 7–9. If not, affected values remain `unknown` and the golden path
   still completes with explicit unknowns — this is an accepted outcome, not
   a failure.
2. The existing reference layer (`OMSP-REFERENCE-CONFIG-0001`,
   `OMSP-REFERENCE-EQUIPMENT-0001`, `OMSP-REFERENCE-SCENARIO-0001`) is a
   sufficient structural foundation; gaps found during implementation are
   raised as change proposals, not silently worked around.
3. Schema/validator extensions needed for items §6.2–§6.5 are small enough
   to fit the Sprint 7–9 envelope; if not, scope is cut on the consumer set
   and interface detail, never on provenance or validation rigor.
4. Markdown remains the rendering target for v1; PDF publication is
   deferred to the publication-pipeline work.

## 11. Success Conditions (Measurable)

The golden path is **done** when all of the following hold:

1. All Section 6 validator evidence exists and is green in CI on `develop`.
2. The YAML model covers 100% of the Section 5.1 role list (with `unknown`
   values allowed and counted): a published unknowns count exists per model
   file.
3. The primary scenario instance exists, conforms to
   `OMSP-REFERENCE-SCENARIO-0001` §13 validation rules, and every
   inspection step references at least one equipment role and one source
   document (or an explicit `unknown` evidence marker).
4. The human-readable output is generated by CI from the model with zero
   manual steps, includes the advisory banner, and contains no claim absent
   from the model.
5. The five-minute demo (Section 9) passes its pass criteria in a recorded
   run.
6. A validation outcome (per `OMSP-VAL-VALIDATION-0001`) is recorded by the
   accountable human: the output answers the Section 2 problem statement for
   at least one of the two user roles.
7. Total implementation effort fits within Sprint 7–9; any scope cut is
   recorded as a version change of this artifact.

Acceptance of this definition as the **canonical first OMSP golden path** is
a human decision by the accountable maintainer; this artifact proposes, it
does not approve.

## 12. Safety and Authority Boundary

- Every output of the golden path is **advisory**. It does not certify
  seaworthiness, electrical compliance, equipment fitness, or safe
  operation, and it does not authorize navigation, maintenance, or emergency
  action.
- The critical-battery scenario output in particular supports — and never
  replaces — human judgment; load-shedding, continuing a passage, or
  touching the electrical installation are decisions of the responsible
  human.
- AI assistance may draft, extract, compare, and check this slice, but
  cannot promote authority classes, resolve safety-relevant conflicts, or
  approve the golden path (`OMSP-CANON-METHODOLOGY-0001` §3.8).
- Where this artifact conflicts with manufacturer documentation or the
  responsible human's judgment, the latter prevail.

## 13. Downstream Work (indicative, for PM planning)

Implementation is decomposed by `omsp-pm` into Sprint 7–9 Work Packages;
the indicative slices are: (a) source capture and register extension,
(b) electrical-slice YAML model + schema, (c) validator extensions
(§6.2–§6.5), (d) primary scenario instance, (e) rendering of the
human-readable output + demo assembly. Ordering constraint: (a) and (b)
precede (d); the minimal MODS/ODS draft sections (§7.2) precede (e).
