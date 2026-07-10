#!/usr/bin/env python3
"""Deterministic OMSP artifact validator MVP."""
from __future__ import annotations
import argparse, json, re, sys
from dataclasses import asdict, dataclass
from pathlib import Path

ARTIFACT_ID_RE = re.compile(r"^OMSP-[A-Z0-9]+(?:-[A-Z0-9]+)*-[0-9]{4}$")
REQUIRED_METADATA = ("Artifact-ID", "Title", "Version", "Status", "Owner")

@dataclass(frozen=True)
class Finding:
    rule_id: str
    severity: str
    path: str
    message: str
    line: int | None = None


def front_matter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    result: dict[str, str] = {}
    for raw in text[4:end].splitlines():
        if ":" in raw and not raw.startswith((" ", "-", "\t")):
            key, value = raw.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def validate_markdown(path: Path, root: Path) -> list[Finding]:
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(root).as_posix()
    meta = front_matter(text)
    if not meta:
        return []
    findings: list[Finding] = []
    for key in REQUIRED_METADATA:
        if not meta.get(key):
            findings.append(Finding("OMSP-META-001", "error", rel, f"missing required metadata: {key}"))
    artifact_id = meta.get("Artifact-ID", "")
    if artifact_id and not ARTIFACT_ID_RE.fullmatch(artifact_id):
        findings.append(Finding("OMSP-ID-001", "error", rel, f"invalid Artifact-ID: {artifact_id}"))
    lower = text.lower()
    for phrase in ("automatically approved", "ai approved", "validator approved", "ci approved"):
        if phrase in lower:
            findings.append(Finding("OMSP-AUTH-001", "gate", rel, f"automation authority claim detected: {phrase}"))
    return findings


def validate_json(path: Path, root: Path) -> list[Finding]:
    rel = path.relative_to(root).as_posix()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [Finding("OMSP-JSON-001", "error", rel, f"invalid JSON: {exc.msg}", exc.lineno)]
    findings: list[Finding] = []
    if isinstance(data, dict):
        artifact_id = data.get("artifact_id") or data.get("artifactId")
        if artifact_id and not ARTIFACT_ID_RE.fullmatch(str(artifact_id)):
            findings.append(Finding("OMSP-ID-001", "error", rel, f"invalid artifact ID: {artifact_id}"))
    return findings


def discover(root: Path, targets: list[str]) -> list[Path]:
    files: list[Path] = []
    for target in targets:
        candidate = (root / target).resolve()
        if root not in candidate.parents and candidate != root:
            raise ValueError(f"target escapes repository root: {target}")
        if candidate.is_file():
            files.append(candidate)
        elif candidate.is_dir():
            files.extend(p for p in candidate.rglob("*") if p.suffix.lower() in {".md", ".json"} and ".git" not in p.parts)
    return sorted(set(files))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("targets", nargs="*", default=["."])
    parser.add_argument("--root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    try:
        files = discover(root, args.targets)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 2
    findings: list[Finding] = []
    for path in files:
        findings.extend(validate_markdown(path, root) if path.suffix.lower() == ".md" else validate_json(path, root))
    findings.sort(key=lambda item: (item.path, item.rule_id, item.line or 0, item.message))
    errors = sum(item.severity in {"error", "gate"} for item in findings)
    report = {
        "tool": {"name": "omsp-validator", "version": "0.1.0"},
        "repository": str(root),
        "summary": {"files_scanned": len(files), "findings": len(findings), "errors": errors},
        "findings": [asdict(item) for item in findings],
        "authority": "advisory-validation-only"
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
