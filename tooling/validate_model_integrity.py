#!/usr/bin/env python3
"""Validate cross-file model integrity of OMSP instance packages (WP-0083).

Four mechanical, advisory integrity classes, each with its own rule ID,
implementing `planning/WP-0074-GOLDEN-PATH-DEFINITION.md` §6 items 4-5
independently of (and in addition to) the per-file schema contract of
``tooling/validate_instance_schemas.py``:

- ``OMSP-INTEGRITY-001`` — referential integrity of endpoints: every
  ``source_port``/``target_port`` of an interface or connection instance
  resolves to a ``ports[]`` entry of an equipment instance in the package.
- ``OMSP-INTEGRITY-002`` — referential integrity of scenarios: every
  ``equipment:``/``connection:`` reference in ``related_equipment[]`` and
  ``causes[].implicates[]`` of a scenario instance resolves to an
  equipment/connection instance in the package. The class is evaluated on
  every run; a package without scenario instances is checked over zero
  instances and reports the rule ID with a zero count.
- ``OMSP-INTEGRITY-003`` — document-reference resolution: every
  ``document:`` identity cited anywhere in an instance resolves to exactly
  one row of the source register's document-reference mapping table, the
  mapped source is a register source entry, and the mapped source is not
  declared inaccessible (``reference/HANSE_460_SOURCE_REGISTER.md`` §7
  rules 1-3). The register is parsed mechanically from its markdown
  tables; no document or source ID is hard-coded.
- ``OMSP-INTEGRITY-004`` — provenance completeness: every non-``unknown``
  value carries a provenance block with all five contract fields
  (``source_id``, ``authority_class``, ``confidence``, ``retrieval_date``,
  ``applicability``) non-empty; every entry of an ``attributes``/
  ``nominal_limits`` map is an explicit provenanced value (known-value,
  unknown marker or ``claims[]``); every claim inside ``claims[]`` is a
  complete known-value held to the same standard (``claims[]`` needs at
  least two claims); and every ``source_id`` resolves to a register
  source entry. This check is independent of the JSON Schema contract of
  ``schemas/provenance.schema.json`` and runs on schema-valid files too.

``OMSP-INTEGRITY-000`` reports load errors (missing target, invalid YAML).

Output is a JSON findings report consistent with ``tooling/omsp_validate.py``
(findings with ``rule_id``/``severity``/``path``/``message``, a summary and
an ``advisory-validation-only`` authority statement). Exit code 0 means no
findings; 1 means findings; 2 means the tool could not run (missing
dependency, bad arguments or an unusable register).

Traceability: WP-0083 / ISSUE-204; permanent fixtures in ``tests/integrity/``
and unit tests in ``tests/test_model_integrity.py``.

Dependencies (pinned per governance/ADR-0004-PYTHON-VALIDATION-DEPENDENCIES.md):
``PyYAML==6.0.3`` (standard library otherwise; jsonschema is not required).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    print(
        "ERROR: missing dependency: "
        f"{exc.name}. Install pinned dependencies first: "
        "pip install PyYAML==6.0.3",
        file=sys.stderr,
    )
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]

RULE_LOAD = "OMSP-INTEGRITY-000"
RULE_ENDPOINT = "OMSP-INTEGRITY-001"
RULE_SCENARIO = "OMSP-INTEGRITY-002"
RULE_DOCUMENT = "OMSP-INTEGRITY-003"
RULE_PROVENANCE = "OMSP-INTEGRITY-004"
INTEGRITY_RULES = (RULE_ENDPOINT, RULE_SCENARIO, RULE_DOCUMENT, RULE_PROVENANCE)

PROVENANCE_FIELDS = (
    "source_id",
    "authority_class",
    "confidence",
    "retrieval_date",
    "applicability",
)

CONCEPT_EQUIPMENT = "OMSP-CONCEPT-EQUIPMENT-ROLE"
CONCEPT_INTERFACE = "OMSP-CONCEPT-INTERFACE"
CONCEPT_CONNECTION = "OMSP-CONCEPT-CONNECTION"
CONCEPT_SCENARIO = "OMSP-CONCEPT-OPERATIONAL-SCENARIO"

SOURCE_ID_PATTERN = re.compile(r"source:[a-z0-9][a-z0-9:._-]*")
DOCUMENT_ID_PATTERN = re.compile(r"^document:[a-z0-9][a-z0-9:._-]*$")


class RegisterError(Exception):
    """The source register cannot be used (tool-cannot-run condition)."""


@dataclass(frozen=True)
class Finding:
    rule_id: str
    severity: str
    path: str
    message: str


@dataclass
class Register:
    path: str
    source_ids: set[str] = field(default_factory=set)
    inaccessible_ids: set[str] = field(default_factory=set)
    document_map: dict[str, str] = field(default_factory=dict)
    duplicate_documents: set[str] = field(default_factory=set)


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def strip_cell(cell: str) -> str:
    return cell.strip().strip("`").strip()


def parse_markdown_tables(text: str) -> list[list[list[str]]]:
    """Return every markdown table as a list of rows of stripped cells."""
    tables: list[list[list[str]]] = []
    current: list[list[str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("|"):
            cells = [strip_cell(cell) for cell in stripped.strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells if cell):
                continue  # separator row
            current.append(cells)
        else:
            if current:
                tables.append(current)
                current = []
    if current:
        tables.append(current)
    return tables


def load_register(register_path: Path) -> Register:
    """Mechanically parse the source register's markdown tables.

    Table classification is by header text, matching the structure of
    ``reference/HANSE_460_SOURCE_REGISTER.md``:

    - source entries (§2.2): header contains ``Source ID`` — the first
      column of each row is a register source ID;
    - inaccessible sources (§4.3): header contains ``Attempted source`` —
      every ``source:`` token in a row is recorded as inaccessible;
    - document mapping (§7): header contains ``Document ID`` and
      ``Register source ID``.
    """
    try:
        text = register_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise RegisterError(f"cannot read source register {rel(register_path)}: {exc}") from exc

    register = Register(path=rel(register_path))
    for table in parse_markdown_tables(text):
        header = [cell.lower() for cell in table[0]]
        rows = table[1:]
        if any("source id" == cell for cell in header) and not any(
            "document id" in cell for cell in header
        ):
            for row in rows:
                if row and row[0].startswith("source:"):
                    register.source_ids.add(row[0])
        elif any("attempted source" in cell for cell in header):
            for row in rows:
                for cell in row:
                    register.inaccessible_ids.update(SOURCE_ID_PATTERN.findall(cell))
        elif any("document id" in cell for cell in header) and any(
            "register source id" in cell for cell in header
        ):
            for row in rows:
                if len(row) < 2 or not row[0].startswith("document:"):
                    continue
                document_id, source_id = row[0], row[1]
                if document_id in register.document_map:
                    register.duplicate_documents.add(document_id)
                register.document_map[document_id] = source_id

    if not register.source_ids:
        raise RegisterError(
            f"source register {rel(register_path)} contains no parseable source-entry "
            "table (header with a 'Source ID' column); cannot run integrity checks"
        )
    return register


def collect_yaml_files(targets: list[str], findings: list[Finding]) -> list[Path]:
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
            findings.append(Finding(RULE_LOAD, "error", target, "target not found"))
    return sorted(set(files))


def load_instances(files: list[Path], findings: list[Finding]) -> list[tuple[Path, dict]]:
    instances: list[tuple[Path, dict]] = []
    for path in files:
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as exc:
            findings.append(Finding(RULE_LOAD, "error", rel(path), f"cannot load instance: {exc}"))
            continue
        if not isinstance(data, dict):
            findings.append(Finding(RULE_LOAD, "error", rel(path), "instance is not a mapping"))
            continue
        instances.append((path, data))
    return instances


def index_ids(instances: list[tuple[Path, dict]]) -> tuple[set[str], set[str], set[str]]:
    """Return (equipment IDs, port IDs, connection IDs) declared by the package."""
    equipment_ids: set[str] = set()
    port_ids: set[str] = set()
    connection_ids: set[str] = set()
    for _, data in instances:
        concept = data.get("concept")
        instance_id = data.get("id")
        if concept == CONCEPT_EQUIPMENT and isinstance(instance_id, str):
            equipment_ids.add(instance_id)
            ports = data.get("ports")
            if isinstance(ports, list):
                for port in ports:
                    if isinstance(port, dict) and isinstance(port.get("id"), str):
                        port_ids.add(port["id"])
        elif concept == CONCEPT_CONNECTION and isinstance(instance_id, str):
            connection_ids.add(instance_id)
    return equipment_ids, port_ids, connection_ids


def check_endpoints(
    instances: list[tuple[Path, dict]], port_ids: set[str], findings: list[Finding]
) -> int:
    """OMSP-INTEGRITY-001: interface/connection endpoints resolve to ports."""
    checked = 0
    for path, data in instances:
        if data.get("concept") not in {CONCEPT_INTERFACE, CONCEPT_CONNECTION}:
            continue
        for endpoint_field in ("source_port", "target_port"):
            endpoint = data.get(endpoint_field)
            if not isinstance(endpoint, str):
                continue  # missing/typed endpoints are the schema contract's job
            checked += 1
            if endpoint not in port_ids:
                findings.append(
                    Finding(
                        RULE_ENDPOINT,
                        "error",
                        rel(path),
                        f"{endpoint_field} does not resolve to any ports[] entry of an "
                        f"equipment instance in the package: {endpoint}",
                    )
                )
    return checked


def check_scenarios(
    instances: list[tuple[Path, dict]],
    equipment_ids: set[str],
    connection_ids: set[str],
    findings: list[Finding],
) -> tuple[int, int]:
    """OMSP-INTEGRITY-002: scenario role references resolve to package instances."""
    scenarios = 0
    checked = 0

    def check_ref(path: Path, location: str, ref: object) -> None:
        nonlocal checked
        if not isinstance(ref, str):
            return
        if ref.startswith("equipment:"):
            checked += 1
            if ref not in equipment_ids:
                findings.append(
                    Finding(
                        RULE_SCENARIO,
                        "error",
                        rel(path),
                        f"{location} does not resolve to any equipment instance "
                        f"in the package: {ref}",
                    )
                )
        elif ref.startswith("connection:"):
            checked += 1
            if ref not in connection_ids:
                findings.append(
                    Finding(
                        RULE_SCENARIO,
                        "error",
                        rel(path),
                        f"{location} does not resolve to any connection instance "
                        f"in the package: {ref}",
                    )
                )

    for path, data in instances:
        if data.get("concept") != CONCEPT_SCENARIO:
            continue
        scenarios += 1
        related = data.get("related_equipment")
        if isinstance(related, list):
            for index, ref in enumerate(related):
                check_ref(path, f"related_equipment/{index}", ref)
        causes = data.get("causes")
        if isinstance(causes, list):
            for cause_index, cause in enumerate(causes):
                if not isinstance(cause, dict):
                    continue
                implicates = cause.get("implicates")
                if isinstance(implicates, list):
                    for index, ref in enumerate(implicates):
                        check_ref(path, f"causes/{cause_index}/implicates/{index}", ref)
    return scenarios, checked


def collect_document_refs(node: object, location: str = "") -> list[tuple[str, str]]:
    """Collect every ``document:`` identity string with its location."""
    refs: list[tuple[str, str]] = []
    if isinstance(node, str):
        if DOCUMENT_ID_PATTERN.match(node):
            refs.append((location or "<root>", node))
    elif isinstance(node, dict):
        for key, value in node.items():
            refs.extend(collect_document_refs(value, f"{location}/{key}" if location else str(key)))
    elif isinstance(node, (list, tuple)):
        for index, item in enumerate(node):
            refs.extend(collect_document_refs(item, f"{location}/{index}" if location else str(index)))
    return refs


def check_documents(
    instances: list[tuple[Path, dict]], register: Register, findings: list[Finding]
) -> int:
    """OMSP-INTEGRITY-003: document references resolve through the register."""
    checked = 0
    for path, data in instances:
        for location, document_id in collect_document_refs(data):
            checked += 1
            if document_id in register.duplicate_documents:
                findings.append(
                    Finding(
                        RULE_DOCUMENT,
                        "error",
                        rel(path),
                        f"{location}: document reference maps to more than one register "
                        f"source entry in {register.path} (mapping rule 2): {document_id}",
                    )
                )
            elif document_id not in register.document_map:
                findings.append(
                    Finding(
                        RULE_DOCUMENT,
                        "error",
                        rel(path),
                        f"{location}: document reference does not resolve to the "
                        f"document-reference mapping table of the source register "
                        f"({register.path}): {document_id}",
                    )
                )
            elif register.document_map[document_id] in register.inaccessible_ids:
                findings.append(
                    Finding(
                        RULE_DOCUMENT,
                        "error",
                        rel(path),
                        f"{location}: document reference {document_id} maps to a source "
                        f"declared inaccessible in the source register ({register.path}); "
                        f"inaccessible documentation is representable only as unknown "
                        f"(mapping rule 3): {register.document_map[document_id]}",
                    )
                )
            elif register.document_map[document_id] not in register.source_ids:
                findings.append(
                    Finding(
                        RULE_DOCUMENT,
                        "error",
                        rel(path),
                        f"{location}: document reference {document_id} maps to an ID that "
                        f"is not a source entry of the source register ({register.path}): "
                        f"{register.document_map[document_id]}",
                    )
                )
    return checked


class ProvenanceChecker:
    """OMSP-INTEGRITY-004: provenance completeness, independent of schemas."""

    def __init__(self, register: Register, findings: list[Finding]) -> None:
        self.register = register
        self.findings = findings
        self.values_checked = 0
        self.claims_checked = 0
        self.provenance_blocks_checked = 0

    def report(self, path: Path, location: str, message: str) -> None:
        self.findings.append(
            Finding(RULE_PROVENANCE, "error", rel(path), f"{location or '<root>'}: {message}")
        )

    def check_provenance(self, path: Path, location: str, provenance: object) -> None:
        self.provenance_blocks_checked += 1
        if not isinstance(provenance, dict):
            self.report(path, location, "provenance is not a mapping")
            return
        for field_name in PROVENANCE_FIELDS:
            value = provenance.get(field_name)
            if not isinstance(value, str) or not value.strip():
                self.report(
                    path,
                    location,
                    f"provenance field missing or empty: {field_name} "
                    "(five-field contract of schemas/provenance.schema.json)",
                )
        source_id = provenance.get("source_id")
        if (
            isinstance(source_id, str)
            and source_id.strip()
            and source_id not in self.register.source_ids
        ):
            self.report(
                path,
                location,
                f"source_id does not resolve to a source entry of the source register "
                f"({self.register.path}): {source_id}",
            )

    def check_known_value(self, path: Path, location: str, node: dict) -> None:
        self.values_checked += 1
        if "value" not in node:
            self.report(path, location, "known-value has no value field")
        if "provenance" not in node:
            self.report(
                path,
                location,
                "non-unknown value carries no provenance block "
                "(every non-unknown value needs five-field provenance)",
            )
        else:
            self.check_provenance(path, f"{location}/provenance", node["provenance"])

    def check_claims(self, path: Path, location: str, claims: object) -> None:
        if not isinstance(claims, list) or len(claims) < 2:
            self.report(
                path,
                location,
                "claims[] must record at least two conflicting claims side by side "
                "(single or empty claims[] is not a conflict)",
            )
        if isinstance(claims, list):
            for index, claim in enumerate(claims):
                self.claims_checked += 1
                claim_location = f"{location}/{index}"
                if not isinstance(claim, dict):
                    self.report(path, claim_location, "claim is not a mapping")
                    continue
                self.check_known_value(path, claim_location, claim)

    def check_attribute_map(self, path: Path, location: str, entries: dict) -> None:
        for name, entry in entries.items():
            entry_location = f"{location}/{name}"
            if not isinstance(entry, dict) or not (
                "value" in entry or "claims" in entry or entry.get("status") == "unknown"
            ):
                self.report(
                    path,
                    entry_location,
                    "attribute is not an explicit provenanced value "
                    "(known-value, unknown marker or claims[])",
                )
                continue
            self.walk(path, entry_location, entry)

    def walk(self, path: Path, location: str, node: object) -> None:
        if isinstance(node, dict):
            if node.get("status") == "unknown":
                return  # explicit unknown marker — nothing to prove
            if "claims" in node:
                self.check_claims(path, f"{location}/claims" if location else "claims", node["claims"])
                for key, value in node.items():
                    if key != "claims":
                        self.walk(path, f"{location}/{key}" if location else str(key), value)
                return
            if "value" in node:
                self.check_known_value(path, location, node)
                return
            if "provenance" in node:
                self.check_provenance(
                    path, f"{location}/provenance" if location else "provenance", node["provenance"]
                )
            for key, value in node.items():
                if key == "provenance":
                    continue
                child_location = f"{location}/{key}" if location else str(key)
                if key in {"attributes", "nominal_limits"} and isinstance(value, dict):
                    self.check_attribute_map(path, child_location, value)
                else:
                    self.walk(path, child_location, value)
        elif isinstance(node, (list, tuple)):
            for index, item in enumerate(node):
                self.walk(path, f"{location}/{index}" if location else str(index), item)


def run(targets: list[str], register_path: Path) -> dict:
    """Run all integrity classes and return the JSON-serializable report."""
    findings: list[Finding] = []
    register = load_register(register_path)

    files = collect_yaml_files(targets, findings)
    instances = load_instances(files, findings)
    equipment_ids, port_ids, connection_ids = index_ids(instances)

    endpoints_checked = check_endpoints(instances, port_ids, findings)
    scenarios, scenario_refs_checked = check_scenarios(
        instances, equipment_ids, connection_ids, findings
    )
    document_refs_checked = check_documents(instances, register, findings)

    provenance = ProvenanceChecker(register, findings)
    for path, data in instances:
        provenance.walk(path, "", data)

    findings.sort(key=lambda item: (item.path, item.rule_id, item.message))
    errors = sum(item.severity == "error" for item in findings)
    return {
        "tool": {"name": "omsp-model-integrity-validator", "version": "0.1.0"},
        "repository": str(ROOT),
        "summary": {
            "targets": targets,
            "register": {
                "path": register.path,
                "source_entries": len(register.source_ids),
                "inaccessible_sources": len(register.inaccessible_ids),
                "document_mappings": len(register.document_map),
            },
            "instances_loaded": len(instances),
            "equipment_instances": len(equipment_ids),
            "ports_indexed": len(port_ids),
            "checks": {
                RULE_ENDPOINT: {"endpoints_checked": endpoints_checked},
                RULE_SCENARIO: {
                    "scenario_instances": scenarios,
                    "references_checked": scenario_refs_checked,
                },
                RULE_DOCUMENT: {"document_references_checked": document_refs_checked},
                RULE_PROVENANCE: {
                    "provenanced_values_checked": provenance.values_checked,
                    "claims_checked": provenance.claims_checked,
                    "provenance_blocks_checked": provenance.provenance_blocks_checked,
                },
            },
            "findings": len(findings),
            "errors": errors,
        },
        "findings": [asdict(item) for item in findings],
        "authority": "advisory-validation-only",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("targets", nargs="+", help="instance YAML files or directories to validate")
    parser.add_argument(
        "--register",
        required=True,
        help="source register markdown file (e.g. reference/HANSE_460_SOURCE_REGISTER.md)",
    )
    parser.add_argument("--output", help="write the JSON report to this path")
    args = parser.parse_args()

    register_path = Path(args.register)
    if not register_path.is_absolute():
        register_path = (ROOT / args.register).resolve()

    try:
        report = run(args.targets, register_path)
    except RegisterError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 1 if report["summary"]["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
