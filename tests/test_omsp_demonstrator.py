#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("omsp_demonstrate", ROOT / "tooling" / "omsp_demonstrate.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class Result:
    def __init__(self, code: int = 0) -> None:
        self.returncode = code
        self.stdout = "ok"
        self.stderr = "failed" if code else ""


class DemonstratorTests(unittest.TestCase):
    def test_run_maps_success_and_failure(self) -> None:
        with patch.object(MODULE.subprocess, "run", return_value=Result(0)):
            passed = MODULE.run("step", ["true"], ROOT, [])
        with patch.object(MODULE.subprocess, "run", return_value=Result(2)):
            failed = MODULE.run("step", ["false"], ROOT, [])
        self.assertEqual("pass", passed["status"])
        self.assertEqual("fail", failed["status"])
        self.assertEqual(2, failed["exit_code"])

    def test_evidence_digest_is_traceable(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            evidence = Path(directory) / "evidence.json"
            evidence.write_text("{}\n", encoding="utf-8")
            with patch.object(MODULE.subprocess, "run", return_value=Result()):
                result = MODULE.run("step", ["true"], ROOT, [evidence])
        self.assertEqual(1, len(result["evidence"]))
        self.assertTrue(result["evidence"][0]["digest"].startswith("sha256:"))

    def test_manifest_keeps_human_approval_boundary(self) -> None:
        self.assertIn("human_approval_required", (ROOT / "tooling" / "omsp_demonstrate.py").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
