# Tooling

Development tooling overview.

## Golden-path report generator (WP-0087)

Renders the human-readable operational report (WP-0074 §7.1; ODS-100/300
conformant) from the YAML instance model. Single command, zero manual
steps:

```bash
python3 tooling/generate_report.py
```

Defaults: model `reference/hanse460`, register
`reference/HANSE_460_SOURCE_REGISTER.md`, banner source
`publication/mods/ODS-100-DOCUMENT-STRUCTURE.md`, output
`publication/generated/hanse460-golden-path-report.md`.

The output is a derived artifact: never edit it by hand (ODS-100-R-09) —
change the model and regenerate. CI (`report-generator.yml`) regenerates
the committed report and fails on any byte difference:

```bash
python3 tooling/generate_report.py --check
```

Dependency: PyYAML (pinned per ADR-0004 in CI).
