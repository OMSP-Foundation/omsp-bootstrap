#!/usr/bin/env python3
"""Validate OMSP maritime instance schemas and YAML instances (WP-0078).

Three stages, all mechanical and advisory:

1. Parse every ``schemas/*.schema.json`` file and check it against the
   JSON Schema Draft 2020-12 meta-schema.
2. Self-test the schema contracts against the permanent fixtures:
   every file under ``tests/schemas/positive`` must validate, and every
   file under ``tests/schemas/negative`` must be rejected.
3. Validate any instance YAML files or directories passed as arguments.

Output is a JSON findings report consistent with ``omsp_validate.py``.
Exit code 0 means no findings; 1 means findings; 2 means the tool could
not run (missing dependencies or bad arguments).

Dependencies (pinned per governance/ADR-0003-PYTHON-VALIDATION-DEPENDENCIES.md):
``jsonschema==4.26.0`` and ``PyYAML==6.0.3``.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

try:
    import yaml
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import SchemaError
    from referencing import Registry, Resource
except ImportError as exc:  # pragma: no cover - environment guard
    print(
        "ERROR: missing dependency: "
        f"{exc.name}. Install pinned dependencies first: "
        "pip install jsonschema==4.26.0 PyYAML==6.0.3",
        file=sys.stderr,
    )
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS_DIR = ROOT / "schemas"
POSITIVE_DIR = ROOT / "tests" / "schemas" / "positive"
NEGATIVE_DIR = ROOT / "tests" / "schemas" / "negative"


@dataclass(frozen=True)
class Finding:
    rule_id: str
    severity: str
    path: str
    message: str


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def load_schemas(findings: list[Finding]) -> tuple[dict[str, dict], dict[str, str]]:
    """Return (schema-by-concept, schema-file-by-concept) after meta-schema checks."""
    schemas: dict[str, dict] = {}
    schema_files: dict[str, str] = {}
    resources: list[tuple[str, Resource]] = []
    loaded: list[tuple[Path, dict]] = []

    for schema_path in sorted(SCHEMAS_DIR.glob("*.schema.json")):
        try:
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            findings.append(Finding("OMSP-ISCHEMA-001", "error", rel(schema_path), f"invalid JSON: {exc.msg}"))
            continue
        try:
            Draft202012Validator.check_schema(schema)
        except SchemaError as exc:
            findings.append(Finding("OMSP-ISCHEMA-001", "error", rel(schema_path), f"meta-schema violation: {exc.message}"))
            continue
        schema_id = schema.get("$id")
        if not schema_id:
            findings.append(Finding("OMSP-ISCHEMA-001", "error", rel(schema_path), "schema has no $id"))
            continue
        resources.append((schema_id, Resource.from_contents(schema)))
        loaded.append((schema_path, schema))

    registry = Registry().with_resources(resources)
    for schema_path, schema in loaded:
        concept = schema.get("properties", {}).get("concept", {}).get("const")
        if concept:
            validator = Draft202012Validator(schema, registry=registry)
            schemas[concept] = validator
            schema_files[concept] = rel(schema_path)
    return schemas, schema_files


def load_instance(path: Path, findings: list[Finding], rule_id: str) -> dict | None:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        findings.append(Finding(rule_id, "error", rel(path), f"invalid YAML: {exc}"))
        return None
    if not isinstance(data, dict):
        findings.append(Finding(rule_id, "error", rel(path), "instance is not a mapping"))
        return None
    return data


def dispatch(data: dict, validators: dict[str, Draft202012Validator]):
    concept = data.get("concept")
    return concept, validators.get(concept) if isinstance(concept, str) else None


def validate_positive(validators: dict[str, Draft202012Validator], findings: list[Finding]) -> int:
    count = 0
    for path in sorted(POSITIVE_DIR.glob("*.yaml")):
        count += 1
        data = load_instance(path, findings, "OMSP-ISCHEMA-002")
        if data is None:
            continue
        concept, validator = dispatch(data, validators)
        if validator is None:
            findings.append(Finding("OMSP-ISCHEMA-002", "error", rel(path), f"no schema for concept: {concept!r}"))
            continue
        errors = sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path))
        for error in errors[:5]:
            location = "/".join(str(part) for part in error.absolute_path) or "<root>"
            findings.append(Finding("OMSP-ISCHEMA-002", "error", rel(path), f"positive fixture rejected at {location}: {error.message}"))
    if count == 0:
        findings.append(Finding("OMSP-ISCHEMA-002", "error", rel(POSITIVE_DIR), "no positive fixtures found"))
    return count


def validate_negative(validators: dict[str, Draft202012Validator], findings: list[Finding]) -> int:
    count = 0
    for path in sorted(NEGATIVE_DIR.glob("*.yaml")):
        count += 1
        data = load_instance(path, findings, "OMSP-ISCHEMA-003")
        if data is None:
            continue
        concept, validator = dispatch(data, validators)
        if validator is None:
            findings.append(Finding("OMSP-ISCHEMA-003", "error", rel(path), f"no schema for concept: {concept!r}"))
            continue
        if validator.is_valid(data):
            findings.append(Finding("OMSP-ISCHEMA-003", "error", rel(path), "negative fixture was ACCEPTED; it must be rejected"))
    if count == 0:
        findings.append(Finding("OMSP-ISCHEMA-003", "error", rel(NEGATIVE_DIR), "no negative fixtures found"))
    return count


def validate_targets(targets: list[str], validators: dict[str, Draft202012Validator], findings: list[Finding]) -> int:
    files: list[Path] = []
    for target in targets:
        candidate = Path(target)
        if not candidate.is_absolute():
            candidate = (ROOT / target).resolve()
        if candidate.is_file():
            files.append(candidate)
        elif candidate.is_dir():
            files.extend(sorted(p for p in candidate.rglob("*") if p.suffix in {".yaml", ".yml"}))
        else:
            findings.append(Finding("OMSP-ISCHEMA-004", "error", target, "target not found"))
    for path in sorted(set(files)):
        data = load_instance(path, findings, "OMSP-ISCHEMA-004")
        if data is None:
            continue
        concept, validator = dispatch(data, validators)
        if validator is None:
            findings.append(Finding("OMSP-ISCHEMA-004", "error", rel(path), f"no schema for concept: {concept!r}"))
            continue
        for error in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
            location = "/".join(str(part) for part in error.absolute_path) or "<root>"
            findings.append(Finding("OMSP-ISCHEMA-004", "error", rel(path), f"invalid at {location}: {error.message}"))
    return len(files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("targets", nargs="*", help="instance YAML files or directories to validate")
    parser.add_argument("--output", help="write the JSON report to this path")
    args = parser.parse_args()

    findings: list[Finding] = []
    validators, schema_files = load_schemas(findings)
    schemas_checked = len(list(SCHEMAS_DIR.glob("*.schema.json")))

    positive = validate_positive(validators, findings)
    negative = validate_negative(validators, findings)
    instances = validate_targets(args.targets, validators, findings) if args.targets else 0

    findings.sort(key=lambda item: (item.path, item.rule_id, item.message))
    errors = sum(item.severity == "error" for item in findings)
    report = {
        "tool": {"name": "omsp-instance-schema-validator", "version": "0.1.0"},
        "repository": str(ROOT),
        "summary": {
            "schemas_checked": schemas_checked,
            "instance_schemas": {concept: path for concept, path in sorted(schema_files.items())},
            "positive_fixtures": positive,
            "negative_fixtures": negative,
            "instances_validated": instances,
            "findings": len(findings),
            "errors": errors,
        },
        "findings": [asdict(item) for item in findings],
        "authority": "advisory-validation-only",
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
