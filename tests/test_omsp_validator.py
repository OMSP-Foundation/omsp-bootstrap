#!/usr/bin/env python3
from __future__ import annotations
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("omsp_validate", ROOT / "tooling" / "omsp_validate.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)

class ValidatorTests(unittest.TestCase):
    def test_positive_fixture_passes(self) -> None:
        path = ROOT / "tests" / "validator" / "positive" / "valid-artifact.md"
        self.assertEqual([], MODULE.validate_markdown(path, ROOT))

    def test_negative_fixture_reports_metadata_and_identity(self) -> None:
        path = ROOT / "tests" / "validator" / "negative" / "invalid-artifact.md"
        rule_ids = {finding.rule_id for finding in MODULE.validate_markdown(path, ROOT)}
        self.assertEqual({"OMSP-META-001", "OMSP-ID-001"}, rule_ids)

    def test_report_order_is_deterministic(self) -> None:
        files = MODULE.discover(ROOT, ["tests/validator"])
        self.assertEqual(files, sorted(files))

if __name__ == "__main__":
    unittest.main()
