# Project Structure

This document explains the top-level structure of the OMSP Foundation repository.

```text
omsp-bootstrap/
├── .github/
├── architecture/
├── assets/
├── canon/
├── ci/
├── demonstrator/
├── docs/
├── examples/
├── generator/
├── governance/
├── knowledge/
├── observability/
├── ontology/
├── operations/
├── performance/
├── pilot/
├── planning/
├── provenance/
├── publication/
├── recovery/
├── reference/
├── risk/
├── roadmap/
├── schemas/
├── security/
├── templates/
├── tests/
├── tooling/
└── validation/
```

## `.github/`

GitHub-native project configuration, issue templates, pull request templates and workflow definitions.

## `architecture/`

Platform architecture designs, including the platform context and the design documents for the Engineering Kernel, Knowledge Engine, Traceability Engine and Publication Engine.

## `assets/`

Static documentation assets such as diagrams, images and future visual material.

## `canon/`

Canonical OMSP language and identity, including vision, mission, philosophy, principles, terminology and ontology overview.

## `ci/`

Continuous integration design documentation, such as quality gate integration.

## `demonstrator/`

Platform integration demonstrators that show governed artifacts, tooling and engines working together.

## `docs/`

Repository-level documentation, navigation, overview and onboarding material.

## `examples/`

Examples of OMSP artifacts, structures and future domain-specific usage.

## `generator/`

Repository generator MVP that derives new governed repositories from the foundation baseline.

## `governance/`

Governance documents defining how OMSP work is planned, reviewed, approved, released and baselined.

## `knowledge/`

Knowledge platform concepts, including the artifact registry, knowledge graph conceptual model, semantic relationship catalog and the AI-readable artifact processing contract.

## `observability/`

Remote telemetry and alerting baseline with its machine-readable profile.

## `ontology/`

OMSP ontology meta-model, canon-ontology mapping and ontology change policy.

## `operations/`

Operational runbooks and audit models, such as incident recovery and observability auditing.

## `performance/`

Performance, availability and capacity baseline with its machine-readable profile.

## `pilot/`

Controlled pilot environment baseline, validation, integration demonstrator and pilot readiness assessment.

## `planning/`

Sprint execution plans and work package maps.

## `provenance/`

Signed provenance and audit baseline with its machine-readable profile.

## `publication/`

Publication pipeline MVP for preview, baseline and release channels.

## `recovery/`

External backup and disaster recovery validation baseline with its machine-readable profile.

## `reference/`

Reference material and domain examples. This area will expand as OMSP develops maritime operational reference models.

## `risk/`

Persistent risk reassessment plan and residual risk records.

## `roadmap/`

Sprint plans, program roadmap and future development direction.

## `schemas/`

Machine-readable schema definitions for artifacts, metadata and traceability.

## `security/`

Security and supply chain baseline, vulnerability and history scanning baseline, and their machine-readable profiles.

## `templates/`

Reusable templates for engineering work such as ADRs, requirements, risks, validation and Work Packages.

## `tests/`

Repository validation strategy and automated checks for tooling such as the generator and publication pipeline.

## `tooling/`

Scripts, validators and generators used to support repeatable engineering work.

## `validation/`

Quality gates, verification framework, validation framework and review checklists.

## Structure Rule

Each top-level directory must have a clear engineering purpose. New directories should be added only when their responsibility cannot be represented by an existing area.
