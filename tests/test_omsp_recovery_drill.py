#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("omsp_recovery_drill", ROOT / "tooling" / "omsp_recovery_drill.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class Result:
    def __init__(self, code: int) -> None:
        self.returncode = code
        self.stdout = "ok"
        self.stderr = "failed" if code else ""


class RecoveryDrillTests(unittest.TestCase):
    def test_missing_evidence_blocks_recovery(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            output = Path(directory) / "drill"
            with patch.object(MODULE.subprocess, "run", return_value=Result(0)):
                record = MODULE.execute(ROOT, output, "abc123")
        self.assertEqual("blocked", record["decision"])
        self.assertTrue(record["missing_evidence"])
        self.assertTrue(record["human_approval_required"])

    def test_complete_evidence_marks_drill_recovered(self) -> None:
        def fake_run(command, cwd, text, capture_output, check):
            demonstrator = Path(command[command.index("--output") + 1])
            base = ROOT / demonstrator
            for relative in MODULE.REQUIRED_EVIDENCE:
                path = base / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("{}\n", encoding="utf-8")
            return Result(0)

        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            output = Path(directory) / "drill"
            with patch.object(MODULE.subprocess, "run", side_effect=fake_run):
                record = MODULE.execute(ROOT, output, "abc123")
            saved = json.loads((output / "recovery-drill-record.json").read_text(encoding="utf-8"))
        self.assertEqual("recovered", record["decision"])
        self.assertEqual(len(MODULE.REQUIRED_EVIDENCE), len(saved["evidence"]))
        self.assertIn("cannot close an incident", saved["approval_boundary"])


if __name__ == "__main__":
    unittest.main()
