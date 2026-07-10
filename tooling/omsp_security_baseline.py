#!/usr/bin/env python3
"""Generate deterministic OMSP security and software supply-chain evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ACTION_RE = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)", re.MULTILINE)
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{30,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
)
WRITE_PERMISSIONS = re.compile(r"^\s*(contents|actions|checks|deployments|packages|pull-requests|issues):\s*write\s*$", re.MULTILINE)


def digest(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def scan(root: Path) -> dict:
    findings: list[dict] = []
    workflows: list[dict] = []
    for path in sorted((root / ".github" / "workflows").glob("*.y*ml")):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(root).as_posix()
        actions = sorted(set(ACTION_RE.findall(text)))
        if "permissions:" not in text:
            findings.append({"rule_id": "SEC-PERM-001", "severity": "error", "path": rel, "message": "workflow lacks explicit permissions"})
        for match in WRITE_PERMISSIONS.finditer(text):
            findings.append({"rule_id": "SEC-PERM-002", "severity": "warning", "path": rel, "message": f"write permission requires review: {match.group(0).strip()}"})
        for action in actions:
            if "@" not in action:
                findings.append({"rule_id": "SEC-ACTION-001", "severity": "error", "path": rel, "message": f"action reference lacks version: {action}"})
            elif not re.fullmatch(r"[^@]+@[0-9a-f]{40}", action):
                findings.append({"rule_id": "SEC-ACTION-002", "severity": "warning", "path": rel, "message": f"action is tag-pinned, not commit-pinned: {action}"})
        workflows.append({"path": rel, "digest": digest(path), "actions": actions})

    scanned_files = 0
    for path in sorted(root.rglob("*")):
        if not path.is_file() or ".git" in path.parts or path.stat().st_size > 1_000_000:
            continue
        scanned_files += 1
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                findings.append({"rule_id": "SEC-SECRET-001", "severity": "error", "path": path.relative_to(root).as_posix(), "message": "potential committed secret material"})
                break

    findings.sort(key=lambda item: (item["path"], item["rule_id"], item["message"]))
    return {
        "tool": {"name": "omsp-security-baseline", "version": "0.1.0"},
        "authority": "advisory-evidence-only",
        "summary": {
            "files_scanned": scanned_files,
            "workflows": len(workflows),
            "errors": sum(item["severity"] == "error" for item in findings),
            "warnings": sum(item["severity"] == "warning" for item in findings),
        },
        "workflows": workflows,
        "findings": findings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    root = Path(args.root).resolve()
    report = scan(root)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], sort_keys=True))
    return 1 if report["summary"]["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
