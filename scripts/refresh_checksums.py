#!/usr/bin/env python3
"""Refresh repository inventory hashes and checksums after an approved update."""
from __future__ import annotations

import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifests" / "repository_file_manifest.csv"
CHECKSUMS = ROOT / "manifests" / "checksums.sha256"
IGNORED_DIRS = {".git", "__pycache__", ".ipynb_checkpoints"}
MANIFEST_EXCLUSIONS = {
    "manifests/repository_file_manifest.csv",
    "manifests/checksums.sha256",
}
CHECKSUM_EXCLUSIONS = {"manifests/checksums.sha256"}
FIELDS = [
    "repository_path", "sha256", "size_bytes", "extension",
    "source_group", "original_path", "role", "notes",
]


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def iter_repo_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*")
        if p.is_file() and not any(part in IGNORED_DIRS for part in p.relative_to(ROOT).parts)
    )


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


existing: dict[str, dict[str, str]] = {}
if MANIFEST.exists():
    with MANIFEST.open(newline="", encoding="utf-8") as f:
        existing = {row["repository_path"]: row for row in csv.DictReader(f)}

files = iter_repo_files()
manifest_rows: list[dict[str, str]] = []
for path in files:
    rel = relative(path)
    if rel in MANIFEST_EXCLUSIONS:
        continue
    prior = existing.get(rel, {})
    manifest_rows.append({
        "repository_path": rel,
        "sha256": digest(path),
        "size_bytes": str(path.stat().st_size),
        "extension": path.suffix.lower(),
        "source_group": prior.get("source_group", "generated"),
        "original_path": prior.get("original_path", ""),
        "role": prior.get("role", "new file pending role review"),
        "notes": prior.get("notes", "Added after the initial consolidated snapshot."),
    })

MANIFEST.parent.mkdir(parents=True, exist_ok=True)
with MANIFEST.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=FIELDS)
    writer.writeheader()
    writer.writerows(manifest_rows)

# Re-read the file list because the manifest itself has now changed.
files = iter_repo_files()
lines = [
    f"{digest(path)}  {relative(path)}"
    for path in files
    if relative(path) not in CHECKSUM_EXCLUSIONS
]
CHECKSUMS.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Wrote {len(manifest_rows)} manifest rows and {len(lines)} checksums.")
