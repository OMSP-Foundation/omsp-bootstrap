#!/usr/bin/env python3
"""OMSP golden-path report generator (WP-0087 / #208).

Renders the human-readable operational document defined by
``planning/WP-0074-GOLDEN-PATH-DEFINITION.md`` §7.1 from the YAML instance
model (single source of truth), conformant to ODS-100 (document structure)
and ODS-300 (procedure language), both Draft v0.1.0.

Design rules implemented here:

- ODS-100-R-01: four mandatory components (system overview, scenario
  sections, evidence appendix, advisory banner).
- ODS-100-R-02: the advisory banner is read verbatim from
  ``publication/mods/ODS-100-DOCUMENT-STRUCTURE.md`` — the standard stays
  the single source of the fixed text; the generator never paraphrases it.
- ODS-100-R-03: every modeled element of the slice is rendered with role,
  key values (authority class or explicit ``unknown``) and protection.
- ODS-100-R-07 / ODS-300-R-09: unknowns are rendered visibly, never
  dropped; the evidence appendix lists every unknown occurrence.
- ODS-100-R-08/R-09/R-10: the output is a derived artifact with declared
  source-model identity/version, generator identity/version, a
  deterministic generation source reference (SHA-256 content digest over
  the sorted input files — the "equivalent" of a commit reference that
  keeps the output byte-reproducible), and the claimed ODS versions.
- ODS-300-R-01…R-10: inspection steps render all nine modeled step fields
  plus the ``[HUMAN CONFIRMATION REQUIRED]`` marker; the continuation
  decision is rendered as a first-class decision-point construct with the
  mandatory conservative human-review branch; fields the model does not
  establish are rendered as explicit unknowns.

Byte-reproducibility contract: two runs over the same inputs produce
byte-identical output (no timestamps, sorted traversal). CI regenerates
the committed document and fails on any difference (ODS-100-R-09: no
manual edits).

Failure behaviour: any missing file, YAML parse error or missing required
model field aborts with a non-zero exit code before anything is written —
the generator never emits partial output.

Usage (single command, zero manual steps):

    python3 tooling/generate_report.py \
        --model reference/hanse460 \
        --register reference/HANSE_460_SOURCE_REGISTER.md \
        --ods publication/mods/ODS-100-DOCUMENT-STRUCTURE.md \
        --output publication/generated/hanse460-golden-path-report.md

Dependency: PyYAML (pinned per ADR-0004 in CI).
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML is required (pip install PyYAML)", file=sys.stderr)
    sys.exit(2)

GENERATOR_ID = "tooling/generate_report.py"
GENERATOR_VERSION = "0.1.0"
CONFORMANCE_CLAIM = "ODS-100 v0.1.0 (Draft), ODS-300 v0.1.0 (Draft)"

# Energy-chain presentation order of the golden path (WP-0074 §7.1(1));
# local-id suffixes of equipment instances. Elements not listed here are
# appended in sorted order — nothing is silently omitted (ODS-100-R-03).
CHAIN_ORDER = [
    "shore-power-inlet",
    "battery-charger",
    "alternator-charging",
    "service-battery-bank",
    "dc-main-distribution",
    "protection-dc-main",
    "measurement-service-battery",
    "inverter",
    "dc-consumer-navigation-lights",
    "dc-consumer-bilge-pump",
    "dc-consumer-freshwater-pump",
    "dc-consumer-refrigeration",
]


class ModelError(Exception):
    """Raised for any input problem; maps to a non-zero exit."""


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(2)


def load_yaml(path: Path) -> dict:
    try:
        with path.open(encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
    except FileNotFoundError as exc:
        raise ModelError(f"input file missing: {path}") from exc
    except yaml.YAMLError as exc:
        raise ModelError(f"YAML parse failure in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ModelError(f"top-level mapping expected in {path}")
    return data


def require(mapping: dict, key: str, ctx: str):
    if key not in mapping:
        raise ModelError(f"required field '{key}' missing in {ctx}")
    return mapping[key]


def local_id(full_id: str) -> str:
    return full_id.rsplit(":", 1)[-1]


def extract_banner(ods100_path: Path) -> str:
    """Extract the fixed advisory banner verbatim from ODS-100 §2."""
    try:
        text = ods100_path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise ModelError(f"ODS-100 standard not found: {ods100_path}") from exc
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.startswith("> **ADVISORY MATERIAL"):
            start = i
            break
    if start is None:
        raise ModelError(
            f"advisory banner (ODS-100-R-02) not found in {ods100_path}"
        )
    banner: list[str] = []
    for line in lines[start:]:
        if not line.startswith(">"):
            break
        banner.append(line)
    if not banner:
        raise ModelError("advisory banner extraction produced no lines")
    return "\n".join(banner)


def readme_front_matter(model_dir: Path) -> dict:
    """Parse the model README front matter for identity/version (R-10)."""
    readme = model_dir / "README.md"
    try:
        text = readme.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise ModelError(f"model README missing: {readme}") from exc
    if not text.startswith("---"):
        raise ModelError(f"front matter missing in {readme}")
    block = text.split("---", 2)
    if len(block) < 3:
        raise ModelError(f"front matter not closed in {readme}")
    meta = yaml.safe_load(block[1])
    if not isinstance(meta, dict):
        raise ModelError(f"front matter not a mapping in {readme}")
    for key in ("Artifact-ID", "Version"):
        require(meta, key, f"{readme} front matter")
    return meta


def content_digest(paths: list[Path]) -> str:
    """Deterministic SHA-256 over the sorted input files (R-10 item 3)."""
    digest = hashlib.sha256()
    for path in sorted(paths):
        digest.update(path.name.encode("utf-8"))
        digest.update(path.read_bytes())
    return digest.hexdigest()


def walk_unknowns(node, path: str, out: list[tuple[str, str]], fname: str):
    """Collect every mapping whose ``status`` field equals ``unknown``."""
    if isinstance(node, dict):
        if node.get("status") == "unknown":
            out.append((fname, path or "(top level)"))
        for key, value in node.items():
            walk_unknowns(value, f"{path}.{key}" if path else key, out, fname)
    elif isinstance(node, list):
        for idx, item in enumerate(node):
            walk_unknowns(item, f"{path}[{idx}]", out, fname)


def flat(text) -> str:
    """Collapse a scalar/folded YAML value into a single rendered line."""
    return " ".join(str(text).split())


def render_value_cell(attr: dict, ctx: str) -> tuple[str, str, str]:
    """Return (value, authority class, source) cells for one attribute."""
    if attr.get("status") == "unknown":
        note = flat(attr.get("note", ""))
        return ("`unknown`" + (f" — {note}" if note else ""), "`unknown`", "—")
    value = flat(require(attr, "value", ctx))
    prov = require(attr, "provenance", ctx)
    klass = flat(require(prov, "authority_class", f"{ctx}.provenance"))
    source = flat(require(prov, "source_id", f"{ctx}.provenance"))
    return (value, f"`{klass}`", f"`{source}`")


class Model:
    """Loaded instance model, indexed for rendering."""

    def __init__(self, model_dir: Path):
        self.dir = model_dir
        self.files: dict[str, dict] = {}
        self.equipment: dict[str, dict] = {}
        self.connections: dict[str, dict] = {}
        self.interfaces: dict[str, dict] = {}
        self.scenarios: dict[str, dict] = {}
        self.system: dict | None = None
        self.system_file = ""
        yaml_paths = sorted(model_dir.glob("*.yaml"))
        if not yaml_paths:
            raise ModelError(f"no YAML instances found in {model_dir}")
        self.yaml_paths = yaml_paths
        for path in yaml_paths:
            data = load_yaml(path)
            require(data, "id", str(path))
            self.files[path.name] = data
            if path.name.startswith("equipment-"):
                self.equipment[path.name] = data
            elif path.name.startswith("connection-"):
                self.connections[path.name] = data
            elif path.name.startswith("interface-"):
                self.interfaces[path.name] = data
            elif path.name.startswith("scenario-"):
                self.scenarios[path.name] = data
            elif path.name.startswith("system-"):
                self.system = data
                self.system_file = path.name

    def protection_of(self, equip_id: str) -> list[str]:
        guards = []
        for fname, data in sorted(self.equipment.items()):
            for protected in data.get("protects", []) or []:
                if protected == equip_id:
                    guards.append(flat(data.get("name", fname)))
        return guards

    def unknown_ledger(self) -> list[tuple[str, str]]:
        out: list[tuple[str, str]] = []
        for fname in sorted(self.files):
            walk_unknowns(self.files[fname], "", out, fname)
        return out


def render_overview(model: Model, lines: list[str]) -> None:
    lines.append("## System overview")
    lines.append("")
    lines.append(
        "Energy chain of the modeled slice (shore power → charger → battery"
        " bank → DC distribution → consumers, with the inverter branch and"
        " the alternator charge path). Every modeled element of the slice is"
        " listed; key values carry their authority class or an explicit"
        " `unknown` (ODS-100-R-03)."
    )
    ordered = []
    seen = set()
    by_local = {
        local_id(data["id"]): (fname, data)
        for fname, data in model.equipment.items()
    }
    for lid in CHAIN_ORDER:
        if lid in by_local:
            ordered.append(by_local[lid])
            seen.add(lid)
    for lid in sorted(by_local):
        if lid not in seen:
            ordered.append(by_local[lid])
    for fname, data in ordered:
        name = flat(require(data, "name", fname))
        lines.append("")
        lines.append(f"### {name}")
        lines.append("")
        lines.append(f"- Model element: `{data['id']}` (`{fname}`)")
        lines.append(f"- Role: {flat(require(data, 'role', fname))}")
        guards = model.protection_of(data["id"])
        if guards:
            lines.append(f"- Protection: {'; '.join(guards)}")
        else:
            lines.append(
                "- Protection: `unknown` — no protective device resolves to"
                " this element in the model"
            )
        quantity = data.get("quantity")
        rows = []
        if isinstance(quantity, dict):
            rows.append(("quantity", quantity))
        attrs = data.get("attributes", {}) or {}
        for attr_name in sorted(attrs):
            rows.append((attr_name, attrs[attr_name]))
        if rows:
            lines.append("")
            lines.append("| Key value | Value | Authority class | Source |")
            lines.append("| --- | --- | --- | --- |")
            for attr_name, attr in rows:
                ctx = f"{fname}:{attr_name}"
                value, klass, source = render_value_cell(attr, ctx)
                lines.append(
                    f"| `{attr_name}` | {value} | {klass} | {source} |"
                )
        else:
            lines.append("- Key values: none modeled")


def render_steps(steps: list, lines: list[str], ctx: str) -> None:
    for step in steps:
        sid = flat(require(step, "step_id", ctx))
        seq = require(step, "sequence", ctx)
        actor = flat(require(step, "responsible_actor", ctx))
        marker = (
            " **[HUMAN CONFIRMATION REQUIRED]**"
            if require(step, "human_confirmation_required", ctx)
            else ""
        )
        lines.append("")
        lines.append(f"#### Step {seq} — `{sid}`{marker}")
        lines.append("")
        lines.append(f"- Responsible actor: {actor}")
        lines.append(f"- Action: {flat(require(step, 'action', ctx))}")
        lines.append(
            f"- Entry criteria: {flat(require(step, 'entry_criteria', ctx))}"
        )
        lines.append(
            "- Completion criteria: "
            + flat(require(step, "completion_criteria", ctx))
        )
        lines.append(
            "- Expected observation: "
            + flat(require(step, "expected_observation", ctx))
        )
        lines.append(
            "- Hazards and safeguards: no step-specific hazard field is"
            " modeled (explicit statement per ODS-300-R-06); the"
            " scenario-level safety constraints above apply to every step"
        )
        lines.append(f"- Escalation: {flat(require(step, 'escalation', ctx))}")


def render_scenario(fname: str, data: dict, lines: list[str]) -> None:
    ctx = fname
    # Scenario-unique heading suffix keeps repeated subsection names
    # lint-clean (MD024) across multiple scenario sections.
    label = fname.removeprefix("scenario-").removesuffix(".yaml")
    title = flat(require(data, "title", ctx))
    lines.append("")
    lines.append(f"## Scenario — {title}")
    lines.append("")
    lines.append(f"- Scenario ID: `{require(data, 'id', ctx)}`")
    lines.append(f"- Class: `{require(data, 'class', ctx)}`")
    lines.append(
        "- Accountable authority: "
        + flat(require(data, "accountable_authority", ctx))
    )
    lines.append(f"- Objective: {flat(require(data, 'objective', ctx))}")
    trigger = require(data, "trigger", ctx)
    lines.append("")
    lines.append(f"### Trigger — {label}")
    lines.append("")
    lines.append(f"- Description: {flat(require(trigger, 'description', ctx))}")
    lines.append(f"- Source: {flat(require(trigger, 'source', ctx))}")
    lines.append(f"- Timestamp handling: {flat(require(trigger, 'timestamp', ctx))}")
    lines.append(f"- Confidence: {flat(require(trigger, 'confidence', ctx))}")
    threshold = require(trigger, "threshold", ctx)
    value, klass, source = render_value_cell(threshold, f"{ctx}:threshold")
    lines.append(f"- Threshold: {value} (authority: {klass}, source: {source})")
    lines.append("")
    lines.append(f"### Affected systems — {label}")
    lines.append("")
    for system in require(data, "affected_systems", ctx):
        lines.append(f"- `{flat(system)}`")
    lines.append("")
    lines.append(f"### Likely causes — {label}")
    for cause in require(data, "causes", ctx):
        cid = flat(require(cause, "id", ctx))
        lines.append("")
        lines.append(f"**Cause: `{local_id(cid)}`**")
        lines.append("")
        lines.append(f"- Cause ID: `{cid}`")
        lines.append(
            f"- Description: {flat(require(cause, 'description', ctx))}"
        )
        lines.append("- Implicates:")
        for ref in require(cause, "implicates", ctx):
            lines.append(f"  - `{flat(ref)}`")
        lines.append(
            "- Evidence requirement: "
            + flat(require(cause, "evidence_requirement", ctx))
        )
    lines.append("")
    lines.append(f"### Inspection sequence — {label}")
    lines.append("")
    lines.append(
        "Reference inspection order, not an approved vessel procedure."
        " Steps follow ODS-300 procedure language; every step field the"
        " model does not establish is rendered as an explicit unknown."
    )
    render_steps(require(data, "inspection_sequence", ctx), lines, ctx)
    lines.append("")
    lines.append(f"### Decision point — continuation decision — {label}")
    lines.append("")
    lines.append(
        "First-class decision construct (ODS-300-R-07/R-08) derived from"
        " the scenario's modeled stop/abort conditions and mandatory"
        " conservative human-review branch:"
    )
    lines.append("")
    lines.append("- Available branches:")
    lines.append(
        "  - Continue the inspection sequence (no stop/abort condition met)."
    )
    for cond in require(data, "stop_abort_conditions", ctx):
        lines.append(f"  - Stop/abort: {flat(cond)}")
    lines.append(
        "  - Conservative human review (mandatory default for unknown or"
        " conflicting evidence, below)."
    )
    lines.append(
        "- Decision authority: "
        + flat(require(data, "accountable_authority", ctx))
    )
    lines.append(
        "- Required evidence: the entry/completion criteria and expected"
        " observations of the executed steps (rendered above); unknown"
        " markers remain unknown."
    )
    lines.append(
        "- Time sensitivity: `unknown` — not modeled by the source scenario"
        " (explicit unknown per ODS-300-R-09)."
    )
    lines.append(
        "- Fallback behaviour (conservative human-review branch): "
        + flat(require(data, "conservative_human_review_branch", ctx))
    )
    lines.append("")
    lines.append(f"### Safety constraints — {label}")
    lines.append("")
    for constraint in require(data, "safety_constraints", ctx):
        lines.append(f"- {flat(constraint)}")
    lines.append("")
    lines.append(f"### Unacceptable outcomes and stop/abort conditions — {label}")
    lines.append("")
    for outcome in require(data, "unacceptable_outcomes", ctx):
        lines.append(f"- Unacceptable outcome: {flat(outcome)}")
    for cond in require(data, "stop_abort_conditions", ctx):
        lines.append(f"- Stop/abort condition: {flat(cond)}")
    lines.append("")
    lines.append(f"### Related equipment — {label}")
    lines.append("")
    for ref in require(data, "related_equipment", ctx):
        lines.append(f"- `{flat(ref)}`")
    lines.append("")
    lines.append(f"### Source documents — {label}")
    lines.append("")
    for ref in require(data, "source_manuals", ctx):
        lines.append(f"- `{flat(ref)}`")
    for section, label_ in (
        ("assumptions", "Assumption"),
        ("unknowns", "Declared unknown"),
        ("exclusions", "Exclusion"),
    ):
        entries = data.get(section) or []
        if entries:
            lines.append("")
            lines.append(f"### {label_}s — {label}")
            lines.append("")
            for entry in entries:
                lines.append(f"- {flat(entry)}")


def render_appendix(model: Model, register: Path, lines: list[str]) -> None:
    lines.append("")
    lines.append("## Evidence appendix")
    lines.append("")
    lines.append(
        "Authority class and source for every rendered claim"
        " (ODS-100-R-06). Source IDs and `document:` identities resolve in"
        f" the source register `{register.as_posix()}`."
    )
    lines.append("")
    lines.append("### Sourced claims")
    lines.append("")
    lines.append(
        "| Model element | Field | Authority class | Source | Confidence |"
    )
    lines.append("| --- | --- | --- | --- | --- |")
    for fname in sorted(model.files):
        data = model.files[fname]
        candidates = []
        quantity = data.get("quantity")
        if isinstance(quantity, dict):
            candidates.append(("quantity", quantity))
        for attr_name, attr in sorted((data.get("attributes") or {}).items()):
            candidates.append((attr_name, attr))
        trigger = data.get("trigger")
        if isinstance(trigger, dict) and isinstance(
            trigger.get("threshold"), dict
        ):
            candidates.append(("trigger.threshold", trigger["threshold"]))
        for attr_name, attr in candidates:
            if not isinstance(attr, dict) or attr.get("status") == "unknown":
                continue
            if "provenance" not in attr:
                continue
            prov = attr["provenance"]
            lines.append(
                f"| `{fname}` | `{attr_name}` |"
                f" `{flat(require(prov, 'authority_class', fname))}` |"
                f" `{flat(require(prov, 'source_id', fname))}` |"
                f" {flat(prov.get('confidence', 'unknown'))} |"
            )
    lines.append("")
    lines.append("### Unknowns (listed, not hidden)")
    lines.append("")
    ledger = model.unknown_ledger()
    lines.append(
        f"The model publishes **{len(ledger)}** explicit `status: unknown`"
        " occurrences. Every one is listed below (ODS-100-R-07); an unknown"
        " is an accepted document state, not a rendering failure."
    )
    lines.append("")
    lines.append("| Model file | Field path |")
    lines.append("| --- | --- |")
    for fname, path in ledger:
        lines.append(f"| `{fname}` | `{path}` |")


def generate(model_dir: Path, register: Path, ods100: Path) -> str:
    banner = extract_banner(ods100)
    model = Model(model_dir)
    if model.system is None:
        raise ModelError(f"no system-*.yaml instance found in {model_dir}")
    if not model.scenarios:
        raise ModelError(f"no scenario-*.yaml instance found in {model_dir}")
    if not register.is_file():
        raise ModelError(f"source register missing: {register}")
    meta = readme_front_matter(model_dir)
    digest = content_digest(
        list(model.yaml_paths) + [model_dir / "README.md", register]
    )
    lines: list[str] = []
    lines.append("# Hanse 460 Golden-Path Operational Report")
    lines.append("")
    lines.append(banner)
    lines.append("")
    lines.append("## Generation provenance")
    lines.append("")
    lines.append(
        f"- Source model: `{meta['Artifact-ID']}` version"
        f" `{meta['Version']}` (`{model_dir.as_posix()}`)"
    )
    lines.append(
        f"- Source register: `{register.as_posix()}`"
    )
    lines.append(
        f"- Generator: `{GENERATOR_ID}` version `{GENERATOR_VERSION}`"
    )
    lines.append(
        f"- Generation source reference: input content digest `sha256:{digest}`"
        " (deterministic digest over the model files and register —"
        " commit-equivalent per ODS-100-R-10)"
    )
    lines.append(f"- Conformance claim: {CONFORMANCE_CLAIM}")
    lines.append(
        "- Derived artifact: generated from the YAML model, never edited by"
        " hand (ODS-100-R-08/R-09); corrections belong in the source model."
    )
    lines.append("")
    render_overview(model, lines)
    for fname in sorted(model.scenarios):
        render_scenario(fname, model.scenarios[fname], lines)
    render_appendix(model, register, lines)
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default="reference/hanse460")
    parser.add_argument(
        "--register", default="reference/HANSE_460_SOURCE_REGISTER.md"
    )
    parser.add_argument(
        "--ods", default="publication/mods/ODS-100-DOCUMENT-STRUCTURE.md"
    )
    parser.add_argument(
        "--output",
        default="publication/generated/hanse460-golden-path-report.md",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="regenerate and compare against the committed output; non-zero"
        " exit on any difference (CI byte-reproducibility gate)",
    )
    args = parser.parse_args()
    try:
        rendered = generate(
            Path(args.model), Path(args.register), Path(args.ods)
        )
    except ModelError as exc:
        fail(str(exc))
    output = Path(args.output)
    if args.check:
        if not output.is_file():
            fail(f"committed output missing for --check: {output}")
        committed = output.read_text(encoding="utf-8")
        if committed != rendered:
            fail(
                f"{output} differs from regeneration — rendered documents"
                " are never edited by hand (ODS-100-R-09); regenerate with"
                " the documented command"
            )
        print(f"OK: {output} is byte-identical to regeneration")
        return 0
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered, encoding="utf-8")
    print(f"generated: {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
