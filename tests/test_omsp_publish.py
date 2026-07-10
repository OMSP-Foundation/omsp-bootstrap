#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("omsp_publish", ROOT / "tooling" / "omsp_publish.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PublicationTests(unittest.TestCase):
    def test_preview_build_preserves_status_and_is_deterministic(self) -> None:
        request = MODULE.load_request(ROOT / "tests" / "publication" / "preview-request.json")
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first"
            second = Path(directory) / "second"
            manifest = MODULE.build(ROOT, request, first)
            MODULE.build(ROOT, request, second)
            self.assertEqual("preview", manifest["publication_channel"])
            self.assertTrue(all(entry["status"] == "Review" for entry in manifest["artifacts"]))
            first_files = sorted(path.relative_to(first) for path in first.rglob("*") if path.is_file())
            second_files = sorted(path.relative_to(second) for path in second.rglob("*") if path.is_file())
            self.assertEqual(first_files, second_files)
            for relative in first_files:
                self.assertEqual((first / relative).read_bytes(), (second / relative).read_bytes())

    def test_release_requires_approval(self) -> None:
        request = json.loads((ROOT / "tests" / "publication" / "preview-request.json").read_text(encoding="utf-8"))
        request["channel"] = "release"
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
            json.dump(request, handle)
            path = Path(handle.name)
        try:
            with self.assertRaises(ValueError):
                MODULE.load_request(path)
        finally:
            path.unlink(missing_ok=True)

    def test_release_rejects_review_artifact_even_with_approval(self) -> None:
        request = MODULE.load_request(ROOT / "tests" / "publication" / "preview-request.json")
        request["channel"] = "release"
        request["approval_evidence"] = "TEST-APPROVAL"
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                MODULE.build(ROOT, request, Path(directory) / "release")


if __name__ == "__main__":
    unittest.main()
