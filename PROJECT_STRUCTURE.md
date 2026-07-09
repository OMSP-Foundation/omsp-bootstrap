# Project Structure

This document explains the top-level structure of the OMSP Foundation repository.

```text
omsp-bootstrap/
├── .github/
├── assets/
├── canon/
├── docs/
├── examples/
├── foundation/
├── governance/
├── platform/
├── reference/
├── release/
├── roadmap/
├── schemas/
├── templates/
├── tests/
├── tooling/
└── validation/
```

## `.github/`

GitHub-native project configuration, issue templates, pull request templates and workflow definitions.

## `assets/`

Static documentation assets such as diagrams, images and future visual material.

## `canon/`

Canonical OMSP language and identity, including vision, mission, philosophy, principles, terminology and ontology overview.

## `docs/`

Repository-level documentation, navigation, overview and onboarding material.

## `examples/`

Examples of OMSP artifacts, structures and future domain-specific usage.

## `foundation/`

Engineering standards that define artifacts, metadata, traceability, naming, repository structure, documentation quality and AI governance.

## `governance/`

Governance documents defining how OMSP work is planned, reviewed, approved, released and baselined.

## `platform/`

Platform component concepts such as Engineering Kernel, Knowledge Engine, Traceability Engine and Publication Engine.

## `reference/`

Reference material and domain examples. This area will expand as OMSP develops maritime operational reference models.

## `release/`

Release, versioning and change policy documentation.

## `roadmap/`

Sprint plans, program roadmap and future development direction.

## `schemas/`

Machine-readable schema definitions for artifacts, metadata and traceability.

## `templates/`

Reusable templates for engineering work such as ADRs, requirements, risks, validation and Work Packages.

## `tests/`

Repository validation strategy and future automated checks.

## `tooling/`

Scripts, validators and generators used to support repeatable engineering work.

## `validation/`

Quality gates, verification framework, validation framework and review checklists.

## Structure Rule

Each top-level directory must have a clear engineering purpose. New directories should be added only when their responsibility cannot be represented by an existing area.
