#!/usr/bin/env python3
"""Build an evidence-backed OMSP Sprint-5 production-readiness decision package."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

VERSION = "0.1.0"
REQUIRED = (
    "quality-gate-report.json",
    "demonstrator/demonstrator-manifest.json",
    "recovery-drill/recovery-drill-record.json",
)
RESIDUAL_RISKS = (
    {"id": "RR-001", "severity": "high", "title": "No production deployment target or environment approval", "disposition": "deferred-next-horizon"},
    {"id": "RR-002", "severity": "high", "title": "No signed provenance or cryptographically signed audit log", "disposition": "deferred-next-horizon"},
    {"id": "RR-003", "severity": "medium", "title": "No remote observability, paging or long-term evidence store", "disposition": "deferred-next-horizon"},
    {"id": "RR-004", "severity": "medium", "title": "No vulnerability-database or repository-history secret scan", "disposition": "deferred-next-horizon"},
    {"id": "RR-005", "severity": "high", "title": "No load, availability or external disaster-recovery validation", "disposition": "deferred-next-horizon"},
)


def sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def run(command: list[str], root: Path) -> dict:
    result = subprocess.run(command, cwd=root, text=True, capture_output=True, check=False)
    return {
        "command": command,
        "exit_code": result.returncode,
        "status": "pass" if result.returncode == 0 else "fail",
        "stdout": result.stdout[-3000:],
        "stderr": result.stderr[-3000:],
    }


def execute(root: Path, output: Path, source_commit: str) -> dict:
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)
    py = sys.executable

    executions = {
        "quality_gate": run([py, "tooling/omsp_quality_gate.py", "--output", str((output / "quality-gate-report.json").relative_to(root)), "--work", str((output / "quality-gate-work").relative_to(root))], root),
        "demonstrator": run([py, "tooling/omsp_demonstrate.py", "--output", str((output / "demonstrator").relative_to(root)), "--source-commit", source_commit], root),
        "recovery_drill": run([py, "tooling/omsp_recovery_drill.py", "--output", str((output / "recovery-drill").relative_to(root)), "--source-commit", source_commit], root),
    }

    evidence = []
    missing = []
    for relative in REQUIRED:
        path = output / relative
        if path.is_file():
            evidence.append({"path": path.relative_to(root).as_posix(), "digest": sha256(path)})
        else:
            missing.append(relative)

    automated_failures = [name for name, result in executions.items() if result["status"] == "fail"]
    candidate = not automated_failures and not missing
    assessment = {
        "assessment": {"name": "omsp-sprint-5-production-readiness", "version": VERSION},
        "source_commit": source_commit,
        "release_version_proposal": "0.5.0",
        "automated_recommendation": "candidate-for-human-approval" if candidate else "not-ready",
        "production_release_authorized": False,
        "human_approval_required": True,
        "approval_status": "pending",
        "automated_failures": automated_failures,
        "missing_evidence": missing,
        "executions": executions,
        "evidence": evidence,
        "residual_risks": list(RESIDUAL_RISKS),
        "roadmap_horizon": "Sprint-5 implementation horizon complete; production operation capabilities remain deferred.",
        "approval_boundary": "Automation cannot approve the production baseline, accept residual risk, create a release, publish externally or authorize deployment.",
    }
    assessment_path = output / "production-readiness-assessment.json"
    assessment_path.write_text(json.dumps(assessment, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    approval = {
        "record_type": "production-baseline-approval",
        "proposed_version": "0.5.0",
        "source_commit": source_commit,
        "status": "pending-accountable-human-approval",
        "required_approver": "Accountable Maintainer",
        "risk_acceptance_required": True,
        "assessment_digest": sha256(assessment_path),
        "decision": None,
        "approver": None,
        "approved_at": None,
    }
    (output / "baseline-approval-record.json").write_text(json.dumps(approval, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return assessment


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=Path("build/release-readiness"))
    parser.add_argument("--source-commit", default="UNSPECIFIED")
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output if args.output.is_absolute() else root / args.output
    assessment = execute(root, output, args.source_commit)
    print(json.dumps({"recommendation": assessment["automated_recommendation"], "risks": len(assessment["residual_risks"])}, sort_keys=True))
    return 0 if assessment["automated_recommendation"] == "candidate-for-human-approval" else 1


if __name__ == "__main__":
    raise SystemExit(main())
