---
Artifact-ID: OMSP-CANON-METHODOLOGY-0001
Title: OMSP Engineering Methodology
Version: 0.1.1
Status: Draft
Owner: OMSP Foundation Governance
Baseline: Sprint-6
Classification: Public
Related-Issue: WP-0069 / #185
---

# OMSP Engineering Methodology

## 1. Purpose

This artifact consolidates the engineering methodologies that OMSP has adopted, in one canonical inventory.

Each methodology already exists in canon, governance, ontology, validation, or platform artifacts. This artifact does not create new methodology; it names, groups, and maps what is already normative, so that downstream artifacts, contributors, and AI-assisted workflows can reference the methodology set without reconstructing it from scattered sources.

## 2. Core Methodological Triad

The OMSP Philosophy defines the core triad:

```text
Knowledge First • Models Before Code • Traceability by Design
```

### 2.1 Knowledge-First Engineering

Operational knowledge is treated as a primary engineering asset: explicit, structured, reusable, governed, and traceable. Documents, models, standards, and decisions are durable engineering artifacts, not secondary outputs.

- Defined by: [Philosophy](./PHILOSOPHY.md) §2, [Principles](./PRINCIPLES.md) §2.1.

### 2.2 Model-Based Systems Engineering (Models Before Code)

Concepts, terms, responsibilities, interfaces, and decisions are modeled or documented before code or automation is treated as authoritative. The Vision names OMSP an open, model-based, knowledge-first systems engineering foundation.

- Defined by: [Vision](./VISION.md) §1, [Philosophy](./PHILOSOPHY.md) §3, [Principles](./PRINCIPLES.md) §2.7.

### 2.3 Traceability by Design

Material work preserves an explicit path across:

```text
Vision → Mission → Principles → Issue → Artifact → Decision → PR → Review → Baseline/Release
```

Traceability is a quality-control mechanism, not after-the-fact reporting. The Traceability Engine is the automation counterpart of this methodology.

- Defined by: [Philosophy](./PHILOSOPHY.md) §4, `governance/METADATA_AND_TRACEABILITY_STANDARD.md` (`OMSP-STD-METADATA-TRACEABILITY-0001`).

## 3. Supporting Methodologies

### 3.1 Ontology-Driven Semantic Modeling

A technology-neutral formal ontology defines stable concept and relation identifiers with domain, range, and governance rules, in a two-layer format: human-readable Markdown plus a machine-readable JSON registry. OWL/RDF/SHACL serializations are intentionally deferred. A knowledge-graph conceptual model and semantic relationship catalog extend the ontology toward the knowledge platform.

- Defined by: `ontology/OMSP_ONTOLOGY.md` (`OMSP-ONTOLOGY-CORE-0001`), [Ontology Overview](./ONTOLOGY_OVERVIEW.md), `knowledge/KNOWLEDGE_GRAPH_CONCEPTUAL_MODEL.md`, `knowledge/SEMANTIC_RELATIONSHIP_CATALOG.md`.

### 3.2 Verification and Validation (V&V)

OMSP adopts the classical systems-engineering separation: verification asks "did we build it correctly" (requirements, acceptance criteria, metadata, review evidence); validation asks "did we build the right thing" (fitness for purpose, downstream usability, governance alignment). Validation outcomes are explicit: Validated, Validated with Exceptions, Not Validated, Deferred.

- Defined by: `validation/VALIDATION_FRAMEWORK.md` (`OMSP-VAL-VALIDATION-0001`) §3, §7.

### 3.3 Evidence-Based Engineering and Decision Records

Claims, approvals, baselines, and releases must be supported by traceable evidence. `Evidence`, `Claim`, and `Decision` are first-class ontology concepts connected through `validates`, `verifies`, and `supports` relations. Architecture decisions are captured as decision records using the ADR template.

- Defined by: [Principles](./PRINCIPLES.md) §2.4, `ontology/OMSP_ONTOLOGY.md` §4–§5, `templates/ADR_TEMPLATE.md`, `governance/DECISION_AND_REVIEW_POLICY.md`.

### 3.4 Configuration and Baseline Management

Artifacts are versioned with SemVer, carry lifecycle status, and enter governed baseline snapshots. Superseded artifacts are retired through explicit `supersedes` relations and compatibility stubs; canonical authority follows stable Artifact IDs, not paths.

- Defined by: `governance/ENGINEERING_PLAYBOOK.md` §10–§11 (baseline management, release governance), `governance/CANONICAL_AUTHORITY_MAP.md` (`OMSP-GOV-AUTHORITY-MAP-0001`).

### 3.5 Sprint and Work-Package-Based Iterative Delivery

Work proceeds in sprint cycles decomposed into numbered Work Packages (WP-XXXX), each bound to an issue, a branch, acceptance criteria, and artifact-level traceability. Each sprint increases engineering maturity while preserving traceability.

- Defined by: `roadmap/OMSP_ROADMAP.md`, `governance/ENGINEERING_PLAYBOOK.md` §5 and §9 (Work Package lifecycle, sprint lifecycle) (`OMSP-GOV-PLAYBOOK-0001`).

### 3.6 Docs-as-Code with Automated Quality Gates

All engineering content is version-controlled Markdown, JSON, and YAML. Repeatable validation is automated by default: metadata validators, quality gates, lint, link checks, and consistency workflows run on every pull request.

- Defined by: `governance/ENGINEERING_PLAYBOOK.md` §3, `tooling/omsp_validate.py` and the `validate_*.py` family, `.github/workflows/`.

### 3.7 Digital Twin Engineering

Domain modeling for the Hanse 460 reference vessel follows a layered digital-twin method: vessel reference model → equipment and interface model → operational scenario model → state and observation model → validation demonstrator, with explicit governance and safety boundaries.

- Defined by: Sprint-4 Work Packages (WP-0039 … WP-0046), `reference/VESSEL_REFERENCE_MODEL.md`, `reference/DIGITAL_TWIN_STATE_AND_OBSERVATION_MODEL.md`, `reference/DIGITAL_TWIN_GOVERNANCE_AND_SAFETY_BOUNDARIES.md`.

### 3.8 Human-Governed AI-Assisted Engineering

AI assistance is advisory only: it may draft, analyze, compare, and check consistency, but may not approve, invent evidence, or hold baseline or release authority. The ontology encodes this boundary: the `approves` relation may only originate from accountable human actors.

- Defined by: [Principles](./PRINCIPLES.md) §2.10, [Philosophy](./PHILOSOPHY.md) §5, `ontology/OMSP_ONTOLOGY.md` §6, `governance/AI_GOVERNANCE.md`.

### 3.9 Reusable Open-Foundation Platform Engineering

Canon, governance, and engineering standards are designed for reuse by downstream repositories. The repository generator operationalizes this, and deriving a second vessel type from the Hanse 460 template is the planned proof of reusability.

- Defined by: [Principles](./PRINCIPLES.md) §2.2, §2.8, `roadmap/OMSP_ROADMAP.md` (Sprint-5 WP-0049).

## 4. Methodology-to-Source Map

| Methodology | Primary normative source | Automation / platform counterpart |
| --- | --- | --- |
| Knowledge-First Engineering | `OMSP-CANON-PHILOSOPHY-0001` | Knowledge Engine |
| Model-Based Systems Engineering | `OMSP-CANON-VISION-0001` | Engineering Kernel |
| Traceability by Design | `OMSP-STD-METADATA-TRACEABILITY-0001` | Traceability Engine |
| Ontology-Driven Semantic Modeling | `OMSP-ONTOLOGY-CORE-0001` | Knowledge Engine |
| Verification and Validation | `OMSP-VAL-VALIDATION-0001` | Quality gates |
| Evidence-Based Engineering / ADR | `OMSP-CANON-PRINCIPLES-0001` §2.4 | Validator toolchain |
| Configuration and Baseline Management | `OMSP-GOV-AUTHORITY-MAP-0001` | Release workflows |
| Sprint / Work-Package Delivery | `OMSP-GOV-PLAYBOOK-0001` | GitHub Projects |
| Docs-as-Code + Quality Gates | `OMSP-GOV-PLAYBOOK-0001` §3 | CI workflows |
| Digital Twin Engineering | Sprint-4 reference artifacts | Validation demonstrator |
| Human-Governed AI Assistance | `OMSP-CANON-PRINCIPLES-0001` §2.10 | PR AI-boundary checks |
| Reusable Open Foundation | `OMSP-CANON-PRINCIPLES-0001` §2.2/§2.8 | Repository generator |

## 5. Known Gap: External Standards Alignment

OMSP methodology artifacts currently define all practices in OMSP canonical language, without explicit mapping to industry systems-engineering frameworks such as ISO/IEC/IEEE 15288, the INCOSE Systems Engineering Handbook, SysML, or ARCADIA.

This is recorded as a known gap, not a defect. A future Work Package may add a standards-alignment map when downstream credibility or interoperability requires it. Until then, this artifact is the canonical statement that the omission is intentional.

## 6. Downstream Use

Downstream artifacts may cite this inventory when they need to:

- justify a practice by naming its methodology and normative source;
- onboard contributors to the OMSP way of working;
- scope new Work Packages against the existing methodology set;
- detect methodology drift during review or audit;
- decide whether a proposed practice is new methodology (requiring governance) or an application of an existing one.

## 7. Boundaries

This artifact does not:

- introduce new normative requirements;
- override the sources it maps;
- claim conformance to external standards;
- define implementation technology choices.

Where this inventory and a normative source diverge, the normative source prevails and this inventory must be corrected.

## 8. Related Canon Artifacts

- [Vision](./VISION.md) defines the direction the methodology set serves.
- [Mission](./MISSION.md) defines the purpose the methodology set executes.
- [Philosophy](./PHILOSOPHY.md) defines the core triad interpreted by this inventory.
- [Principles](./PRINCIPLES.md) define the operating rules behind each methodology.
- [Terminology](./TERMINOLOGY.md) defines the canonical language used here.
- [Ontology Overview](./ONTOLOGY_OVERVIEW.md) introduces the concept families used by the modeling methodologies.
- [Canon Index](./CANON_INDEX.md) provides the recommended reading order.

## 9. Maintenance

This inventory is maintained through issue-backed Work Packages and reviewed pull requests. Material changes require governance review and version metadata update. When a normative source changes materially, this inventory must be reviewed in the same or a follow-up Work Package.
