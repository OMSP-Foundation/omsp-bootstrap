#!/usr/bin/env python3
"""Unit tests for tooling/validate_model_integrity.py (WP-0083 / #204).

Covers the four integrity classes on the permanent fixtures under
``tests/integrity/`` (test checklist TS-1, TS-2), the JSON/exit-code CLI
contract (TS-3) and the mechanical register resolution (TS-4: appending
a register entry changes fixture behavior without any code change).
"""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tooling" / "validate_model_integrity.py"
FIXTURES = ROOT / "tests" / "integrity"
REGISTER = FIXTURES / "register.md"
POSITIVE = FIXTURES / "positive" / "package"
NEGATIVE = FIXTURES / "negative"

SPEC = importlib.util.spec_from_file_location("validate_model_integrity", VALIDATOR)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

NEGATIVE_EXPECTATIONS = {
    "n1-interface-endpoint-unknown-port": MODULE.RULE_ENDPOINT,
    "n2-scenario-unknown-equipment": MODULE.RULE_SCENARIO,
    "n3-document-not-in-register": MODULE.RULE_DOCUMENT,
    "n4-provenance-field-missing": MODULE.RULE_PROVENANCE,
    "n5-claim-missing-provenance": MODULE.RULE_PROVENANCE,
    "n6-source-id-not-in-register": MODULE.RULE_PROVENANCE,
    "n7-document-maps-to-inaccessible": MODULE.RULE_DOCUMENT,
}


def run_fixture(target: Path, register: Path = REGISTER) -> dict:
    return MODULE.run([str(target)], register)


class PositivePackageTests(unittest.TestCase):
    def test_valid_package_produces_zero_findings(self) -> None:
        report = run_fixture(POSITIVE)
        self.assertEqual([], report["findings"])
        self.assertEqual(0, report["summary"]["errors"])

    def test_all_four_integrity_classes_are_checked_in_one_run(self) -> None:
        report = run_fixture(POSITIVE)
        checks = report["summary"]["checks"]
        self.assertEqual(set(MODULE.INTEGRITY_RULES), set(checks))
        self.assertGreater(checks[MODULE.RULE_ENDPOINT]["endpoints_checked"], 0)
        self.assertGreater(checks[MODULE.RULE_SCENARIO]["references_checked"], 0)
        self.assertGreater(checks[MODULE.RULE_DOCUMENT]["document_references_checked"], 0)
        self.assertGreater(checks[MODULE.RULE_PROVENANCE]["provenanced_values_checked"], 0)

    def test_scenario_free_package_still_reports_the_scenario_rule(self) -> None:
        report = run_fixture(POSITIVE / "equipment-storage-bank.yaml")
        checks = report["summary"]["checks"]
        self.assertIn(MODULE.RULE_SCENARIO, checks)
        self.assertEqual(0, checks[MODULE.RULE_SCENARIO]["scenario_instances"])
        self.assertEqual([], report["findings"])

    def test_multi_claim_positive_passes(self) -> None:
        report = run_fixture(POSITIVE / "equipment-distribution-panel.yaml")
        self.assertEqual([], report["findings"])
        self.assertEqual(2, report["summary"]["checks"][MODULE.RULE_PROVENANCE]["claims_checked"])


class NegativeFixtureTests(unittest.TestCase):
    def test_negative_directories_match_the_documented_set(self) -> None:
        found = sorted(path.name for path in NEGATIVE.iterdir() if path.is_dir())
        self.assertEqual(sorted(NEGATIVE_EXPECTATIONS), found)

    def test_each_negative_fixture_isolates_exactly_one_violation(self) -> None:
        for name, expected_rule in NEGATIVE_EXPECTATIONS.items():
            with self.subTest(fixture=name):
                report = run_fixture(NEGATIVE / name)
                self.assertEqual(
                    1, len(report["findings"]),
                    f"{name} must isolate exactly one violation: {report['findings']}",
                )
                finding = report["findings"][0]
                self.assertEqual(expected_rule, finding["rule_id"])
                self.assertEqual("error", finding["severity"])

    def test_unregistered_source_message_names_the_register(self) -> None:
        report = run_fixture(NEGATIVE / "n6-source-id-not-in-register")
        message = report["findings"][0]["message"]
        self.assertIn("tests/integrity/register.md", message)
        self.assertIn("source:fixture:itest:not-registered:2026-07-16", message)

    def test_claim_without_provenance_is_rejected(self) -> None:
        report = run_fixture(NEGATIVE / "n5-claim-missing-provenance")
        message = report["findings"][0]["message"]
        self.assertIn("claims/1", message)
        self.assertIn("provenance", message)


class RegisterMechanicsTests(unittest.TestCase):
    def test_adding_a_register_row_changes_fixture_behavior(self) -> None:
        """TS-4: the ID sets come from the register, not from code."""
        extended = REGISTER.read_text(encoding="utf-8") + (
            "\n| Document ID | Register source ID |\n"
            "| --- | --- |\n"
            "| `document:fixture:itest:unregistered-notes:1.0` "
            "| `source:fixture:itest:design-summary:2026-07-16` |\n"
        )
        with tempfile.NamedTemporaryFile(
            "w", suffix=".md", delete=False, encoding="utf-8"
        ) as handle:
            handle.write(extended)
            temp_register = Path(handle.name)
        try:
            baseline = run_fixture(NEGATIVE / "n3-document-not-in-register")
            self.assertEqual(1, len(baseline["findings"]))
            extended_report = run_fixture(
                NEGATIVE / "n3-document-not-in-register", temp_register
            )
            self.assertEqual([], extended_report["findings"])
        finally:
            temp_register.unlink()

    def test_unusable_register_is_a_cannot_run_condition(self) -> None:
        with self.assertRaises(MODULE.RegisterError):
            MODULE.load_register(FIXTURES / "does-not-exist.md")


class CliContractTests(unittest.TestCase):
    def run_cli(self, target: Path) -> tuple[int, dict]:
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR), str(target), "--register", str(REGISTER)],
            capture_output=True,
            text=True,
            check=False,
        )
        return completed.returncode, json.loads(completed.stdout)

    def test_clean_run_exits_zero_with_json_report(self) -> None:
        code, report = self.run_cli(POSITIVE)
        self.assertEqual(0, code)
        self.assertEqual("advisory-validation-only", report["authority"])
        self.assertEqual([], report["findings"])

    def test_finding_run_exits_one_with_contract_fields(self) -> None:
        code, report = self.run_cli(NEGATIVE / "n1-interface-endpoint-unknown-port")
        self.assertEqual(1, code)
        finding = report["findings"][0]
        self.assertEqual(
            {"rule_id", "severity", "path", "message"}, set(finding)
        )

    def test_unusable_register_exits_two(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR),
                str(POSITIVE),
                "--register",
                str(FIXTURES / "does-not-exist.md"),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(2, completed.returncode)


if __name__ == "__main__":
    unittest.main()
