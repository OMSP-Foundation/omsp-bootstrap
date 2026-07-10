#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("omsp_quality_gate", ROOT / "tooling" / "omsp_quality_gate.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class Result:
    def __init__(self, code: int) -> None:
        self.returncode = code
        self.stdout = "output"
        self.stderr = "error" if code else ""


class QualityGateTests(unittest.TestCase):
    def test_run_check_maps_zero_to_pass(self) -> None:
        with patch.object(MODULE.subprocess, "run", return_value=Result(0)):
            result = MODULE.run_check("example", ["true"], ROOT, [])
        self.assertEqual("pass", result["status"])
        self.assertEqual("blocking", result["classification"])

    def test_run_check_maps_nonzero_to_fail(self) -> None:
        with patch.object(MODULE.subprocess, "run", return_value=Result(7)):
            result = MODULE.run_check("example", ["false"], ROOT, [])
        self.assertEqual("fail", result["status"])
        self.assertEqual(7, result["exit_code"])

    def test_evidence_digest_is_recorded(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            evidence = Path(directory) / "evidence.json"
            evidence.write_text("{}\n", encoding="utf-8")
            with patch.object(MODULE.subprocess, "run", return_value=Result(0)):
                result = MODULE.run_check("example", ["true"], ROOT, [evidence])
        self.assertEqual(1, len(result["evidence"]))
        self.assertTrue(result["evidence"][0]["digest"].startswith("sha256:"))


if __name__ == "__main__":
    unittest.main()
