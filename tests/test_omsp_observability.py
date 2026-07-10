#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("omsp_observability", ROOT / "tooling" / "omsp_observability.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

CONTEXT = {
    "observed_at": "2026-07-10T00:00:00Z",
    "correlation_id": "test-correlation",
    "source": "unit-test",
    "repository": "OMSP-Foundation/omsp-bootstrap",
    "source_commit": "abc123",
    "workflow_run": "run-1",
    "actor": "test-actor",
}


class ObservabilityTests(unittest.TestCase):
    def test_secret_values_and_keys_are_redacted(self) -> None:
        token = "gh" + "p_" + "abcdefghijklmnopqrstuvwxyz1234567890"
        bearer = "Bearer " + "abcdefghijklmnopqrstuvwxyz"
        value = {
            "token": token,
            "message": "Authorization: " + bearer,
        }
        redacted = MODULE.redact(value)
        self.assertEqual("[REDACTED]", redacted["token"])
        self.assertNotIn("abcdefghijklmnopqrstuvwxyz", redacted["message"])

    def test_events_are_deterministic_and_sorted(self) -> None:
        gate = {
            "decision": "passed",
            "summary": {"checks": 2, "passed": 2, "failed": 0},
            "blocking_failures": [],
            "human_approval_required": True,
            "checks": [
                {"name": "z-check", "status": "pass", "classification": "blocking", "exit_code": 0},
                {"name": "a-check", "status": "pass", "classification": "blocking", "exit_code": 0},
            ],
        }
        first, health = MODULE.build_events(gate, CONTEXT)
        second, _ = MODULE.build_events(gate, CONTEXT)
        self.assertEqual(first, second)
        self.assertEqual("healthy", health["status"])
        self.assertEqual(first, sorted(first, key=lambda item: (item["event_type"], item["event_id"])))

    def test_failed_gate_produces_critical_decision_and_degraded_health(self) -> None:
        gate = {
            "decision": "blocked",
            "summary": {"checks": 1, "passed": 0, "failed": 1},
            "blocking_failures": ["security-supply-chain"],
            "checks": [{"name": "security-supply-chain", "status": "fail", "classification": "blocking", "exit_code": 1}],
        }
        events, health = MODULE.build_events(gate, CONTEXT)
        decision = next(event for event in events if event["event_type"] == "quality_gate.decision.recorded")
        self.assertEqual("critical", decision["severity"])
        self.assertEqual("degraded", health["status"])
        self.assertEqual(1, health["checks_failed"])


if __name__ == "__main__":
    unittest.main()
