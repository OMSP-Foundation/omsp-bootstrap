#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("omsp_security_baseline", ROOT / "tooling" / "omsp_security_baseline.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class SecurityBaselineTests(unittest.TestCase):
    def test_explicit_read_permissions_are_not_flagged(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflows = root / ".github" / "workflows"
            workflows.mkdir(parents=True)
            (workflows / "safe.yml").write_text(
                "permissions:\n  contents: read\nsteps:\n  - uses: actions/checkout@v4\n",
                encoding="utf-8",
            )
            report = MODULE.scan(root)
            self.assertNotIn("SEC-PERM-001", {item["rule_id"] for item in report["findings"]})

    def test_secret_material_is_blocking(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            marker = "-----BEGIN " + "PRIVATE KEY-----\n"
            (root / "secret.txt").write_text(marker, encoding="utf-8")
            report = MODULE.scan(root)
            self.assertIn("SEC-SECRET-001", {item["rule_id"] for item in report["findings"]})
            self.assertEqual(1, report["summary"]["errors"])

    def test_report_order_is_deterministic(self) -> None:
        report = MODULE.scan(ROOT)
        findings = report["findings"]
        self.assertEqual(findings, sorted(findings, key=lambda item: (item["path"], item["rule_id"], item["message"])))


if __name__ == "__main__":
    unittest.main()
