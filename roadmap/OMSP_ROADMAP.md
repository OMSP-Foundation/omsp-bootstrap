# OMSP Roadmap

This roadmap describes the staged evolution of OMSP Foundation and the broader Open Maritime Systems Platform.

## Roadmap Philosophy

OMSP evolves from governed knowledge to models, tooling and runtime platform capabilities. Each sprint should increase engineering maturity while preserving traceability.

## Sprint Overview

| Sprint | Status | Goal |
| --- | --- | --- |
| Sprint-0 | Completed | Bootstrap repository and governance skeleton |
| Sprint-1 | Completed | Production-quality Foundation Repository |
| Sprint-2 | Completed | Formal engineering foundation and automation-ready designs |
| Sprint-3 | Completed | Knowledge platform foundations |
| Sprint-4 | Completed | Digital twin foundation |
| Sprint-5 | Completed | Production platform readiness |
| Sprint-6 | Active | Post-audit product reorientation and clean v0.5.1 baseline |

## Sprint-0: Bootstrap Foundation

Sprint-0 established the first repository baseline:

```text
v0.1.0-bootstrap
```

Main outcomes:

- repository skeleton;
- governance placeholders;
- foundation standards placeholders;
- schemas and templates;
- GitHub engineering bootstrap;
- canon bootstrap;
- platform bootstrap;
- validation bootstrap;
- reference and release bootstrap.

## Sprint-1: Foundation Repository

Sprint-1 converted the bootstrap baseline into production-quality foundation documentation.

Baseline/release candidate:

```text
v0.1.0-foundation-sprint-1
```

Main outcomes:

- modern repository landing page;
- onboarding and navigation documentation;
- Engineering Playbook v1.0;
- Governance Foundation v1.0;
- Engineering Artifact Standard v1.0;
- Metadata and Traceability Standard v1.0;
- Canon Foundation v1.0;
- Platform Architecture v1.0;
- Validation Framework v1.0;
- GitHub Quality Gates;
- Sprint-1 baseline and release package;
- Sprint-1 closure reconciliation.

Closure status:

- Sprint-1 Work Packages were merged into `develop`.
- Sprint-1 baseline approval was recorded through accountable human instruction.
- Future-scope issues are non-blocking for Sprint-1 closure unless later reclassified by governance.

## Sprint-2: Formal Engineering Foundation

Sprint-2 converted selected Sprint-1 follow-ups into formal, traceable and automation-ready artifacts.

Execution plan:

- `planning/SPRINT_2_EXECUTION_PLAN.md`
- WP-0022 / issue #62

Ordered Work Packages:

1. WP-0022 — Sprint scope and execution plan;
2. WP-0057 — canonical standard authority and duplicate retirement;
3. WP-0023 — formal ontology artifact;
4. WP-0024 — platform engine architecture artifacts;
5. WP-0025 — platform context diagram;
6. WP-0026 — Traceability Engine automation design;
7. WP-0027 — Publication Engine workflow;
8. WP-0028 — validation checklist linting design;
9. WP-0029 — baseline and release readiness.

Release candidate:

```text
v0.2.0-foundation-sprint-2
```

Release and baseline authority remain subject to accountable human approval records.

## Sprint-3: Knowledge Platform Foundations

Sprint-3 established the governed conceptual and processing foundations for an OMSP knowledge platform.

Execution plan:

- `planning/SPRINT_3_EXECUTION_PLAN.md`
- WP-0030 / issue #64

Ordered Work Packages:

1. WP-0030 — Sprint scope and execution plan;
2. WP-0031 — knowledge graph conceptual model;
3. WP-0032 — semantic relationship catalog;
4. WP-0033 — artifact registry and knowledge index;
5. WP-0034 — AI-readable artifact processing contract;
6. WP-0035 — knowledge publication package;
7. WP-0036 — knowledge platform validation scenarios;
8. WP-0037 — baseline and release readiness.

Release candidate:

```text
v0.3.0-foundation-sprint-3
```

Sprint-3 Work Packages were completed and the governed baseline was prepared under accountable human approval authority.

## Sprint-4: Digital Twin Foundation

Sprint-4 established domain-specific maritime reference modeling on top of the governed ontology, traceability and knowledge-platform foundations.

Execution plan:

- `planning/SPRINT_4_EXECUTION_PLAN.md`
- WP-0038 / issue #72

Ordered Work Packages:

1. WP-0038 — Sprint scope and execution plan;
2. WP-0039 — vessel reference model;
3. WP-0040 — Hanse 460 reference configuration;
4. WP-0041 — equipment and interface model;
5. WP-0042 — operational scenario model;
6. WP-0043 — digital twin state and observation model;
7. WP-0044 — digital twin validation demonstrator;
8. WP-0045 — digital twin governance and safety boundaries;
9. WP-0046 — baseline and release readiness.

Release baseline:

```text
v0.4.0-foundation-sprint-4
```

Sprint-4 completed its governed documentation baseline and recorded accountable human approval with explicit limitations. It did not establish production control, autonomous operation, certification or operational authority.

## Sprint-5: Production Platform Readiness

Sprint-5 implemented the first executable, testable and supportable OMSP platform toolchain while keeping production-readiness, release and deployment authority separate from automation. It closed with the `v0.5.0` Production Baseline Candidate approved with conditions.

Execution plan:

- `planning/SPRINT_5_EXECUTION_PLAN.md`
- WP-0047 / issue #81

Ordered Work Packages:

1. WP-0047 — Sprint scope and production-readiness plan;
2. WP-0048 — validator toolchain MVP;
3. WP-0049 — repository generator MVP;
4. WP-0050 — documentation publication pipeline;
5. WP-0051 — security and supply-chain baseline;
6. WP-0052 — CI/CD quality-gate integration;
7. WP-0053 — operational observability and audit model;
8. WP-0054 — end-to-end platform integration demonstrator;
9. WP-0055 — operations, incident and recovery runbook;
10. WP-0056 — production baseline and release readiness.

Proposed release candidate:

```text
v0.5.0-foundation-sprint-5
```

Sprint-5 production-readiness claims require measurable evidence, explicit residual risks and accountable human approval. Demonstrator or CI success alone does not authorize production deployment.

## Sprint-6: Post-Audit Product Reorientation

Sprint-6 is active. Following a full technical audit, the program pivoted from governance growth to domain-content growth: the guiding rule is that no governance work is added unless it directly enables a visible product outcome.

Roadmap authority:

- issue #145 — Post-Audit Product Reorientation (approved as the official roadmap, 2026-07-13);
- the original controlled-pilot-readiness plan (`planning/SPRINT_6_EXECUTION_PLAN.md`, WP-0060) is Superseded; WP-0060–WP-0068 remain reserved for the retired pilot definitions in closed issues #149–#156.

Ordered Work Packages:

1. WP-0070 — audit reconciliation and current-state verification (#165);
2. WP-0071 — governed artifact templates P0 fill (#191);
3. WP-0072 — artifact rationalization and stub disposition (#166);
4. WP-0073 — AI governance consolidation (#167);
5. WP-0074 — Hanse 460 golden path product definition (#168);
6. WP-0075 — domain roadmap and backlog re-baseline (#169);
7. WP-0076 — clean baseline and v0.5.1 release readiness (#170).

Proposed release:

```text
v0.5.1 — clean baseline
```

## Sprint-7 and Beyond: Domain Value and the MODS Stack

From Sprint-7 onward the program builds maritime domain value on two fused
tracks: the machine-verifiable vessel model (YAML as the single source of
truth) and the MODS operational-documentation product stack (MODS
Specification with the ODS-100…600 series → Marine Diagram System → Core
Operations Manual → Vessel Definition Modules → Scenario Library → QRH), where
MODS is the human-readable publication standard over the model. Repository
topology is monorepo per `governance/ADR-0001-REPOSITORY-TOPOLOGY.md`.

Planned blocks (targets, refined per sprint through issue-backed planning):

| Block | Goal | Milestone | Epic |
| --- | --- | --- | --- |
| Sprint-7 | Maritime core ontology v0.1, vessel/equipment schemas, MODS Spec v0.1 (ODS-100/300 Draft) | v0.6.0 | #171 |
| Sprint-8 | Hanse 460 electrical golden path with sourced data; ODS-200/400/500/600 Draft; MDS v0.1 | v0.6.0 | #172 |
| Sprint-9 | Three operational scenarios, report generator, five-minute reproducible demo; Core Operations Manual skeleton | v0.6.0 | #173 |
| Sprint-10 | Second maritime domain slice; Scenario Library v0.1 with validated entries | v0.6.1 | #174 |
| Sprint-11 | VDM–Hanse 460 delta module; second vessel profile via generator (multi-vessel proof) | v0.7.0 | #175 |
| Sprint-12 | QRH v0.1 (fully source-traceable), design-partner pilot, automated PDF pipeline | v0.8.0 | #176 |
| Sprint-13 | Community and contributor readiness; monorepo ADR re-evaluation trigger T1 | v0.9.0 | #177 |
| Sprint-14+ | v1.0 stabilization: schema/ontology SemVer commitment, MODS Specification v1.0 release candidate | v1.0.0 | #178 |

No block produces navigation-safety approval, certification or seaworthiness
claims; operational content remains Draft until validated against real-vessel
experience under accountable human authority.

## Roadmap Rule

The roadmap is directional, not static. Changes must be traceable through issues, pull requests and governance decisions.