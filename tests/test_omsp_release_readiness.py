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
SPEC = importlib.util.spec_from_file_location("omsp_release_readiness", ROOT / "tooling" / "omsp_release_readiness.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class Result:
    def __init__(self, code: int = 0) -> None:
        self.returncode = code
        self.stdout = "ok"
        self.stderr = "failed" if code else ""


class ReleaseReadinessTests(unittest.TestCase):
    def test_missing_evidence_blocks_candidate(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            output = Path(directory) / "release"
            with patch.object(MODULE.subprocess, "run", return_value=Result(0)):
                assessment = MODULE.execute(ROOT, output, "abc123")
        self.assertEqual("not-ready", assessment["automated_recommendation"])
        self.assertTrue(assessment["missing_evidence"])
        self.assertFalse(assessment["production_release_authorized"])

    def test_complete_evidence_only_recommends_human_approval(self) -> None:
        def fake_run(command, cwd, text, capture_output, check):
            output_flag = command.index("--output") + 1
            target = ROOT / command[output_flag]
            executable = next((part for part in command if part.endswith(".py")), "")
            if executable.endswith("omsp_quality_gate.py"):
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text("{}\n", encoding="utf-8")
            elif executable.endswith("omsp_demonstrate.py"):
                (target / "demonstrator-manifest.json").parent.mkdir(parents=True, exist_ok=True)
                (target / "demonstrator-manifest.json").write_text("{}\n", encoding="utf-8")
            else:
                (target / "recovery-drill-record.json").parent.mkdir(parents=True, exist_ok=True)
                (target / "recovery-drill-record.json").write_text("{}\n", encoding="utf-8")
            return Result(0)

        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            output = Path(directory) / "release"
            with patch.object(MODULE.subprocess, "run", side_effect=fake_run):
                assessment = MODULE.execute(ROOT, output, "abc123")
            approval = json.loads((output / "baseline-approval-record.json").read_text(encoding="utf-8"))
        self.assertEqual("candidate-for-human-approval", assessment["automated_recommendation"])
        self.assertFalse(assessment["production_release_authorized"])
        self.assertEqual("pending-accountable-human-approval", approval["status"])
        self.assertEqual(5, len(assessment["residual_risks"]))


if __name__ == "__main__":
    unittest.main()
