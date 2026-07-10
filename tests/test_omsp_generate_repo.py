#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("omsp_generate_repo", ROOT / "tooling" / "omsp_generate_repo.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class GeneratorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.profile = MODULE.load_profile(ROOT / "tests" / "generator" / "repository-profile.json")
        self.files = MODULE.render(self.profile)

    def test_render_is_deterministic(self) -> None:
        self.assertEqual(self.files, MODULE.render(self.profile))

    def test_generation_creates_expected_structure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            entries = MODULE.plan(output, self.files, False)
            MODULE.apply(output, entries)
            self.assertTrue((output / "README.md").is_file())
            self.assertTrue((output / "governance" / "GOVERNANCE.md").is_file())
            self.assertTrue((output / ".omsp" / "repository-profile.json").is_file())

    def test_existing_file_is_blocked_without_force(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            (output / "README.md").write_text("existing\n", encoding="utf-8")
            entries = MODULE.plan(output, self.files, False)
            self.assertIn("blocked", {entry.action for entry in entries})
            with self.assertRaises(ValueError):
                MODULE.apply(output, entries)

    def test_force_allows_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            (output / "README.md").write_text("existing\n", encoding="utf-8")
            entries = MODULE.plan(output, self.files, True)
            MODULE.apply(output, entries)
            self.assertEqual(self.files["README.md"], (output / "README.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
