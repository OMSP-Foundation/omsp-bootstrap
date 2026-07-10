#!/usr/bin/env python3
"""Run the deterministic OMSP Sprint-5 CI/CD quality gate."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

GATE_VERSION = "0.1.0"
GOVERNED_PATHS = (
    "governance", "planning", "roadmap", "architecture", "knowledge",
    "reference", "release", "schemas", "validation", "generator",
    "publication", "security", "ci",
)


def sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def run_check(name: str, command: list[str], root: Path, evidence: list[Path]) -> dict:
    completed = subprocess.run(command, cwd=root, text=True, capture_output=True, check=False)
    return {
        "name": name,
        "classification": "blocking",
        "status": "pass" if completed.returncode == 0 else "fail",
        "exit_code": completed.returncode,
        "command": command,
        "stdout": completed.stdout[-4000:],
        "stderr": completed.stderr[-4000:],
        "evidence": [
            {"path": path.relative_to(root).as_posix(), "digest": sha256(path)}
            for path in evidence
            if path.is_file()
        ],
    }


def execute(root: Path, output: Path, work: Path) -> dict:
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)
    python = sys.executable
    checks: list[dict] = []

    checks.append(run_check(
        "unit-tests",
        [python, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"],
        root,
        [],
    ))

    validator_report = work / "validator-report.json"
    checks.append(run_check(
        "governed-artifact-validation",
        [python, "tooling/omsp_validate.py", *GOVERNED_PATHS, "--output", str(validator_report.relative_to(root))],
        root,
        [validator_report],
    ))

    security_report = work / "security-report.json"
    checks.append(run_check(
        "security-supply-chain",
        [python, "tooling/omsp_security_baseline.py", "--output", str(security_report.relative_to(root))],
        root,
        [security_report],
    ))

    generated = work / "generated-repository"
    generator_report = work / "generator-report.json"
    checks.append(run_check(
        "repository-generator",
        [python, "tooling/omsp_generate_repo.py", "tests/generator/repository-profile.json", str(generated.relative_to(root)), "--report", str(generator_report.relative_to(root))],
        root,
        [generator_report],
    ))

    generated_validation = work / "generated-validation.json"
    checks.append(run_check(
        "generated-repository-validation",
        [python, "tooling/omsp_validate.py", str(generated.relative_to(root)), "--output", str(generated_validation.relative_to(root))],
        root,
        [generated_validation],
    ))

    publication = work / "publication-preview"
    checks.append(run_check(
        "publication-preview",
        [python, "tooling/omsp_publish.py", "tests/publication/preview-request.json", str(publication.relative_to(root))],
        root,
        [publication / "manifest.json", publication / "integrity" / "checksums.sha256"],
    ))

    failures = [check["name"] for check in checks if check["status"] == "fail"]
    report = {
        "gate": {"name": "omsp-sprint-5-quality-gate", "version": GATE_VERSION},
        "authority": "validation-evidence-only",
        "decision": "blocked" if failures else "passed",
        "summary": {
            "checks": len(checks),
            "passed": sum(check["status"] == "pass" for check in checks),
            "failed": len(failures),
        },
        "blocking_failures": failures,
        "checks": checks,
        "human_approval_required": True,
        "approval_boundary": "A passing gate cannot approve merge, baseline, release, risk acceptance, or deployment.",
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", type=Path)
    parser.add_argument("--output", default="build/quality-gate-report.json", type=Path)
    parser.add_argument("--work", default="build/quality-gate", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output if args.output.is_absolute() else root / args.output
    work = args.work if args.work.is_absolute() else root / args.work
    report = execute(root, output, work)
    print(json.dumps(report["summary"], sort_keys=True))
    return 1 if report["blocking_failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
