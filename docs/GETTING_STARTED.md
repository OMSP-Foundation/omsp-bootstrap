# Getting Started with OMSP Foundation

This guide provides the recommended first steps for understanding and contributing to the OMSP Foundation repository.

## 1. Understand the Purpose

OMSP Foundation is the bootstrap and foundation repository for the Open Maritime Systems Platform. It defines the engineering governance, standards, terminology, templates and baseline structure used by future OMSP repositories.

Start with:

1. `README.md`
2. `docs/REPOSITORY_OVERVIEW.md`
3. `governance/ENGINEERING_PLAYBOOK.md`
4. `docs/NAVIGATION.md`

## 2. Understand the Repository Model

OMSP treats documentation, standards, schemas and decisions as governed engineering artifacts.

The repository is organized around these concerns:

- governance and decision making;
- engineering standards;
- metadata and traceability;
- reusable templates;
- canonical language;
- platform architecture;
- verification and validation;
- release and baseline management.

## 3. Understand the Work Package Flow

All normal work follows this lifecycle:

```text
Issue → Branch → Commit → Draft PR → Review → Merge → Baseline Update
```

Each Work Package has a unique identifier such as `WP-0011`.

## 4. Create or Select an Issue

Before changing the repository, create or select a GitHub issue. The issue should define:

- objective;
- deliverables;
- acceptance criteria;
- branch name;
- target branch.

## 5. Create a Feature Branch

Branch names should include the Work Package identifier:

```text
feature/wp-0011-repository-modernization
```

## 6. Make Focused Commits

Use Conventional Commits:

```text
docs(readme): modernize repository landing page
docs(repository): add documentation center
ci(validation): add markdown validation workflow
```

## 7. Open a Draft Pull Request

Pull Requests should start as Draft PRs and target `develop`.

The PR description should include:

- summary;
- deliverables;
- related issue;
- validation notes;
- review checklist.

## 8. Complete Review and Merge

A Work Package is complete only when the PR is reviewed, merged into `develop`, and the related issue is closed.

## 9. Next Reading

Continue with:

- `docs/REPOSITORY_OVERVIEW.md`
- `docs/ARCHITECTURE_OVERVIEW.md`
- `PROJECT_STRUCTURE.md`
- `roadmap/OMSP_ROADMAP.md`
