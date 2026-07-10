#!/usr/bin/env python3
"""Build deterministic OMSP preview, baseline, or release packages."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path

ALLOWED_CHANNELS = {"preview", "baseline", "release"}
APPROVED_CHANNELS = {"baseline", "release"}
APPROVED_STATUSES = {"Active", "Superseded", "Deprecated", "Retired"}
REQUIRED_META = ("Artifact-ID", "Title", "Version", "Status", "Owner")


def read_metadata(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"missing front matter: {path}")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"unterminated front matter: {path}")
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith((" ", "-", "\t")):
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    missing = [key for key in REQUIRED_META if not result.get(key)]
    if missing:
        raise ValueError(f"missing metadata in {path}: {', '.join(missing)}")
    return result


def sha256(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def load_request(path: Path) -> dict:
    request = json.loads(path.read_text(encoding="utf-8"))
    required = ("package_id", "title", "package_version", "channel", "source_repository", "source_commit", "artifacts")
    missing = [key for key in required if not request.get(key)]
    if missing:
        raise ValueError("missing request fields: " + ", ".join(missing))
    if request["channel"] not in ALLOWED_CHANNELS:
        raise ValueError("channel must be preview, baseline or release")
    if request["channel"] in APPROVED_CHANNELS and not request.get("approval_evidence"):
        raise ValueError(f"{request['channel']} requires approval_evidence")
    return request


def build(root: Path, request: dict, output: Path) -> dict:
    channel = request["channel"]
    entries: list[dict] = []
    staged: list[tuple[Path, bytes]] = []
    seen: set[str] = set()

    for item in sorted(request["artifacts"], key=lambda value: value["path"]):
        source = (root / item["path"]).resolve()
        if root not in source.parents or not source.is_file():
            raise ValueError(f"invalid artifact path: {item['path']}")
        meta = read_metadata(source)
        artifact_id = meta["Artifact-ID"]
        if artifact_id in seen:
            raise ValueError(f"duplicate Artifact-ID: {artifact_id}")
        seen.add(artifact_id)
        if channel in APPROVED_CHANNELS and meta["Status"] not in APPROVED_STATUSES:
            raise ValueError(f"{channel} cannot include {meta['Status']} artifact: {item['path']}")
        data = source.read_bytes()
        target = Path("artifacts") / item["path"]
        staged.append((target, data))
        entries.append({
            "artifact_id": artifact_id,
            "title": meta["Title"],
            "version": meta["Version"],
            "status": meta["Status"],
            "path": target.as_posix(),
            "source_path": item["path"],
            "content_digest": sha256(data),
            "included_as": item.get("included_as", "informative"),
        })

    manifest = {
        "package_id": request["package_id"],
        "title": request["title"],
        "package_version": request["package_version"],
        "publication_channel": channel,
        "authority": "non-authoritative-preview" if channel == "preview" else "human-approved-publication",
        "source_repository": request["source_repository"],
        "source_commit": request["source_commit"],
        "approval_evidence": request.get("approval_evidence"),
        "artifacts": entries,
        "dependencies": request.get("dependencies", []),
        "tool": {"name": "omsp-publication-pipeline", "version": "0.1.0"},
    }

    temporary = output.with_name(output.name + ".tmp")
    if temporary.exists():
        shutil.rmtree(temporary)
    temporary.mkdir(parents=True)
    for target, data in staged:
        destination = temporary / target
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
    manifest_bytes = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
    (temporary / "manifest.json").write_bytes(manifest_bytes)
    checksums = [f"{sha256(data).split(':', 1)[1]}  {target.as_posix()}" for target, data in staged]
    checksums.append(f"{hashlib.sha256(manifest_bytes).hexdigest()}  manifest.json")
    (temporary / "integrity").mkdir()
    (temporary / "integrity" / "checksums.sha256").write_text("\n".join(sorted(checksums)) + "\n", encoding="utf-8")
    label = "PREVIEW — NON-AUTHORITATIVE" if channel == "preview" else channel.upper()
    (temporary / "README.md").write_text(
        f"# {request['title']}\n\nPublication channel: **{label}**\n\nPackaging does not change source lifecycle status.\n",
        encoding="utf-8",
    )
    if output.exists():
        shutil.rmtree(output)
    temporary.replace(output)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    try:
        request = load_request(args.request)
        manifest = build(args.root.resolve(), request, args.output)
    except (OSError, ValueError, json.JSONDecodeError, KeyError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({"package": manifest["package_id"], "channel": manifest["publication_channel"], "artifacts": len(manifest["artifacts"])}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
