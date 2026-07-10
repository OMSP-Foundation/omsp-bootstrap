#!/usr/bin/env python3
"""Generate structured, privacy-aware OMSP operational audit evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "0.1.0"
SENSITIVE_KEYS = re.compile(r"(?:secret|token|password|credential|private[_-]?key|authorization)", re.IGNORECASE)
SENSITIVE_VALUES = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"Bearer\s+[A-Za-z0-9._~+/=-]{10,}", re.IGNORECASE),
)


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def redact(value: Any, key: str = "") -> Any:
    if key and SENSITIVE_KEYS.search(key):
        return "[REDACTED]"
    if isinstance(value, dict):
        return {str(k): redact(v, str(k)) for k, v in sorted(value.items(), key=lambda item: str(item[0]))}
    if isinstance(value, list):
        return [redact(item) for item in value]
    if isinstance(value, str):
        redacted = value
        for pattern in SENSITIVE_VALUES:
            redacted = pattern.sub("[REDACTED]", redacted)
        return redacted
    return value


def event_id(payload: dict[str, Any]) -> str:
    return "evt-" + hashlib.sha256(canonical(payload)).hexdigest()[:24]


def make_event(
    event_type: str,
    severity: str,
    outcome: str,
    context: dict[str, str],
    details: dict[str, Any],
) -> dict[str, Any]:
    payload = {
        "schema_version": SCHEMA_VERSION,
        "event_type": event_type,
        "severity": severity,
        "outcome": outcome,
        "observed_at": context["observed_at"],
        "correlation_id": context["correlation_id"],
        "source": context["source"],
        "repository": context["repository"],
        "source_commit": context["source_commit"],
        "workflow_run": context["workflow_run"],
        "actor": context["actor"],
        "details": redact(details),
        "authority": "operational-evidence-only",
    }
    payload["event_id"] = event_id(payload)
    return payload


def build_events(gate: dict[str, Any], context: dict[str, str]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    events: list[dict[str, Any]] = []
    checks = sorted(gate.get("checks", []), key=lambda item: str(item.get("name", "")))
    for check in checks:
        passed = check.get("status") == "pass"
        details = {
            "check": check.get("name"),
            "classification": check.get("classification"),
            "exit_code": check.get("exit_code"),
            "evidence": check.get("evidence", []),
            "stderr": check.get("stderr", "")[-1000:],
        }
        events.append(make_event(
            "quality_gate.check.completed",
            "info" if passed else "error",
            "success" if passed else "failure",
            context,
            details,
        ))

    decision = str(gate.get("decision", "unknown"))
    healthy = decision == "passed"
    events.append(make_event(
        "quality_gate.decision.recorded",
        "info" if healthy else "critical",
        "success" if healthy else "failure",
        context,
        {
            "decision": decision,
            "summary": gate.get("summary", {}),
            "blocking_failures": gate.get("blocking_failures", []),
            "human_approval_required": gate.get("human_approval_required", True),
        },
    ))
    events.sort(key=lambda item: (item["event_type"], item["event_id"]))
    health = {
        "schema_version": SCHEMA_VERSION,
        "service": "omsp-sprint-5-toolchain",
        "status": "healthy" if healthy else "degraded",
        "observed_at": context["observed_at"],
        "correlation_id": context["correlation_id"],
        "source_commit": context["source_commit"],
        "checks_total": len(checks),
        "checks_failed": sum(check.get("status") != "pass" for check in checks),
        "blocking_failures": sorted(gate.get("blocking_failures", [])),
        "owner": "OMSP Engineering Council",
        "response_expectation": "critical failures require accountable triage before release or publication",
        "authority": "diagnostic-signal-only",
    }
    return events, health


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("gate_report", type=Path)
    parser.add_argument("--events", type=Path, required=True)
    parser.add_argument("--health", type=Path, required=True)
    parser.add_argument("--observed-at", required=True)
    parser.add_argument("--correlation-id", required=True)
    parser.add_argument("--source", default="github-actions")
    parser.add_argument("--repository", required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--workflow-run", required=True)
    parser.add_argument("--actor", required=True)
    args = parser.parse_args()
    gate = json.loads(args.gate_report.read_text(encoding="utf-8"))
    context = {
        "observed_at": args.observed_at,
        "correlation_id": args.correlation_id,
        "source": args.source,
        "repository": args.repository,
        "source_commit": args.source_commit,
        "workflow_run": args.workflow_run,
        "actor": args.actor,
    }
    events, health = build_events(gate, context)
    args.events.parent.mkdir(parents=True, exist_ok=True)
    args.events.write_text("".join(json.dumps(event, sort_keys=True) + "\n" for event in events), encoding="utf-8")
    args.health.parent.mkdir(parents=True, exist_ok=True)
    args.health.write_text(json.dumps(health, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"events": len(events), "health": health["status"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
