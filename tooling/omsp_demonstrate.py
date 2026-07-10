#!/usr/bin/env python3
"""Run the reproducible OMSP Sprint-5 end-to-end integration demonstrator."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path


def digest(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def run(name: str, command: list[str], root: Path, outputs: list[Path]) -> dict:
    result = subprocess.run(command, cwd=root, text=True, capture_output=True, check=False)
    return {
        "name": name,
        "command": command,
        "exit_code": result.returncode,
        "status": "pass" if result.returncode == 0 else "fail",
        "stdout": result.stdout[-3000:],
        "stderr": result.stderr[-3000:],
        "evidence": [
            {"path": p.relative_to(root).as_posix(), "digest": digest(p)}
            for p in outputs if p.is_file()
        ],
    }


def execute(root: Path, output: Path, source_commit: str) -> dict:
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)
    py = sys.executable
    steps: list[dict] = []

    generated = output / "generated-repository"
    generator_report = output / "generator-report.json"
    steps.append(run("generate-repository", [py, "tooling/omsp_generate_repo.py", "tests/generator/repository-profile.json", str(generated.relative_to(root)), "--report", str(generator_report.relative_to(root))], root, [generator_report]))

    generated_validation = output / "generated-validation.json"
    steps.append(run("validate-generated-repository", [py, "tooling/omsp_validate.py", str(generated.relative_to(root)), "--output", str(generated_validation.relative_to(root))], root, [generated_validation]))

    publication = output / "publication-preview"
    steps.append(run("assemble-publication-preview", [py, "tooling/omsp_publish.py", "tests/publication/preview-request.json", str(publication.relative_to(root))], root, [publication / "manifest.json", publication / "integrity" / "checksums.sha256"]))

    security_report = output / "security-report.json"
    steps.append(run("security-supply-chain", [py, "tooling/omsp_security_baseline.py", "--output", str(security_report.relative_to(root))], root, [security_report]))

    failures = [step["name"] for step in steps if step["status"] == "fail"]
    gate = {
        "decision": "blocked" if failures else "passed",
        "summary": {"checks": len(steps), "passed": len(steps) - len(failures), "failed": len(failures)},
        "blocking_failures": failures,
        "human_approval_required": True,
        "checks": [{"name": s["name"], "status": s["status"], "classification": "blocking", "exit_code": s["exit_code"], "evidence": s["evidence"]} for s in steps],
    }
    gate_path = output / "demonstrator-gate.json"
    gate_path.write_text(json.dumps(gate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    events = output / "audit-events.jsonl"
    health = output / "health.json"
    steps.append(run("generate-audit-evidence", [py, "tooling/omsp_observability.py", str(gate_path.relative_to(root)), "--events", str(events.relative_to(root)), "--health", str(health.relative_to(root)), "--observed-at", "2026-07-10T00:00:00Z", "--correlation-id", "wp-0054-demonstrator", "--repository", "OMSP-Foundation/omsp-bootstrap", "--source-commit", source_commit, "--workflow-run", "local-demonstrator", "--actor", "accountable-operator"], root, [events, health]))

    failures = [step["name"] for step in steps if step["status"] == "fail"]
    manifest = {
        "demonstrator": {"name": "omsp-platform-integration", "version": "0.1.0"},
        "authority": "demonstration-evidence-only",
        "source_commit": source_commit,
        "decision": "blocked" if failures else "passed",
        "human_approval_required": True,
        "steps": steps,
        "known_gap": "A passing demonstration does not authorize production release or deployment.",
    }
    manifest_path = output / "demonstrator-manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=Path("build/demonstrator"))
    parser.add_argument("--source-commit", default="UNSPECIFIED")
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output if args.output.is_absolute() else root / args.output
    manifest = execute(root, output, args.source_commit)
    print(json.dumps({"decision": manifest["decision"], "steps": len(manifest["steps"])}, sort_keys=True))
    return 1 if manifest["decision"] == "blocked" else 0


if __name__ == "__main__":
    raise SystemExit(main())
