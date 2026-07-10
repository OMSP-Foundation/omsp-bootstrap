#!/usr/bin/env python3
"""Exercise OMSP incident evidence preservation and recovery against the demonstrator."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

REQUIRED_EVIDENCE = (
    "demonstrator-manifest.json",
    "demonstrator-gate.json",
    "audit-events.jsonl",
    "health.json",
    "security-report.json",
    "generated-validation.json",
    "publication-preview/manifest.json",
    "publication-preview/integrity/checksums.sha256",
)


def sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def execute(root: Path, output: Path, source_commit: str) -> dict:
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)
    demonstrator = output / "demonstrator"
    command = [sys.executable, "tooling/omsp_demonstrate.py", "--output", str(demonstrator.relative_to(root)), "--source-commit", source_commit]
    result = subprocess.run(command, cwd=root, text=True, capture_output=True, check=False)

    evidence = []
    missing = []
    for relative in REQUIRED_EVIDENCE:
        path = demonstrator / relative
        if path.is_file():
            evidence.append({"path": path.relative_to(root).as_posix(), "digest": sha256(path)})
        else:
            missing.append(relative)

    incident = {
        "incident_id": "DRILL-WP-0055-0001",
        "severity": "S2",
        "classification": "simulated-deterministic-workflow-failure",
        "containment": "publication-and-release-held",
        "evidence_preserved": not missing,
        "human_escalation_required": True,
        "authority": "recovery-drill-evidence-only",
    }
    incident_path = output / "simulated-incident.json"
    incident_path.write_text(json.dumps(incident, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    recovered = result.returncode == 0 and not missing
    record = {
        "drill": {"name": "omsp-incident-recovery", "version": "0.1.0"},
        "source_commit": source_commit,
        "demonstrator_exit_code": result.returncode,
        "decision": "recovered" if recovered else "blocked",
        "evidence": evidence,
        "missing_evidence": missing,
        "incident_record": {"path": incident_path.relative_to(root).as_posix(), "digest": sha256(incident_path)},
        "human_approval_required": True,
        "approval_boundary": "A successful drill cannot close an incident or authorize production resumption.",
        "stdout": result.stdout[-3000:],
        "stderr": result.stderr[-3000:],
    }
    record_path = output / "recovery-drill-record.json"
    record_path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=Path("build/recovery-drill"))
    parser.add_argument("--source-commit", default="UNSPECIFIED")
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output if args.output.is_absolute() else root / args.output
    record = execute(root, output, args.source_commit)
    print(json.dumps({"decision": record["decision"], "evidence": len(record["evidence"])}, sort_keys=True))
    return 0 if record["decision"] == "recovered" else 1


if __name__ == "__main__":
    raise SystemExit(main())
