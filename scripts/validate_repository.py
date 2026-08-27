#!/usr/bin/env python3
"""Validate the private Unlearning repository snapshot using only the standard library."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
import zipfile
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

EXPECTED_HASHES = {
    "data/codebooks/current/Unlearning_Codebook_2026-08_latest.xlsx": "ae88f0e46bbc4cbc31181e5e905906098be6ec35f87926dc426a4866aafc3208",
    "data/benchmarks/current/Unlearning_GPT_Test_Paragraph_Aligned_ALL_strict_codebook.xlsx": "eea91ee31b51187774880fa395e75f4e0fc7bb90419a16fbaab4bbb99ea55d83",
    "experiments/2026-08-23_gpt-test-first/inputs/Unlearning_GPT_Test_Paragraph_Aligned_ALL.xlsx": "a148051e24ccab080b35a2404cebddeff24cd7c0aec9b5af1f45c42a39c85d31",
    "notebooks/current/2026-08-23_paragraph_level_gpt_test_first_completed.ipynb": "d7c2a922bd8bfbc68adff1985365ccab3b111845ad6a3443124b051ee462feeb",
}
REQUIRED = [
    "README.md",
    "docs/CHANGELOG.md",
    "docs/EXPERIMENT_HISTORY.md",
    "docs/DATA_VERSIONING.md",
    "docs/KNOWN_LIMITATIONS.md",
    "manifests/repository_file_manifest.csv",
    "manifests/notebook_execution_status.csv",
    "manifests/excluded_files.csv",
    "manifests/checksums.sha256",
    "experiments/2026-08-23_gpt-test-first/audits/final_validation_report.json",
]
FORBIDDEN_NAMES = {
    "CSCW_Workshop_Unlearning_3Pager.pdf",
    "Unlearning_LangChain_Retrieval_AUROC_Experiment.ipynb",
    "Unlearning_LangChain_Retrieval_AUROC_Experiment_v2.ipynb",
    "qm7 notes.txt",
}
SECRET_PATTERNS = [
    re.compile(rb"sk-proj-[A-Za-z0-9_-]{20,}"),
    re.compile(rb"sk-svcacct-[A-Za-z0-9_-]{20,}"),
    re.compile(rb"sk-ant-api03-[A-Za-z0-9_-]{20,}"),
    re.compile(rb"AIza[0-9A-Za-z_-]{30,}"),
    re.compile(rb"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(rb"gh[pousr]_[A-Za-z0-9]{30,}"),
    re.compile(rb"AKIA[0-9A-Z]{16}"),
]
TEXT_SCAN_EXTS = {
    ".py", ".md", ".txt", ".json", ".jsonl", ".csv", ".yml", ".yaml", ".ipynb"
}
OFFICE_EXTS = {".xlsx", ".pptx", ".docx"}


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


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)
    print(f"FAIL: {message}")


def validate_manifest(files: list[Path], failures: list[str]) -> None:
    if not MANIFEST.exists():
        return
    with MANIFEST.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    by_path = {row["repository_path"]: row for row in rows}
    if len(by_path) != len(rows):
        fail("Duplicate repository_path values in repository_file_manifest.csv", failures)

    expected = {relative(p) for p in files if relative(p) not in MANIFEST_EXCLUSIONS}
    actual = set(by_path)
    for rel in sorted(expected - actual):
        fail(f"File missing from repository manifest: {rel}", failures)
    for rel in sorted(actual - expected):
        fail(f"Manifest row points to missing or excluded file: {rel}", failures)

    for rel in sorted(expected & actual):
        path = ROOT / rel
        row = by_path[rel]
        actual_hash = digest(path)
        if row.get("sha256") != actual_hash:
            fail(f"Manifest hash mismatch for {rel}", failures)
        try:
            recorded_size = int(row.get("size_bytes", ""))
        except ValueError:
            recorded_size = -1
        if recorded_size != path.stat().st_size:
            fail(f"Manifest size mismatch for {rel}", failures)


def validate_checksums(files: list[Path], failures: list[str]) -> None:
    if not CHECKSUMS.exists():
        return
    entries: dict[str, str] = {}
    for line_number, line in enumerate(CHECKSUMS.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            value, rel = line.split("  ", 1)
        except ValueError:
            fail(f"Malformed checksum line {line_number}", failures)
            continue
        if rel in entries:
            fail(f"Duplicate checksum entry: {rel}", failures)
        entries[rel] = value

    expected = {relative(p) for p in files if relative(p) not in CHECKSUM_EXCLUSIONS}
    actual = set(entries)
    for rel in sorted(expected - actual):
        fail(f"File missing from checksums.sha256: {rel}", failures)
    for rel in sorted(actual - expected):
        fail(f"Checksum entry points to missing or excluded file: {rel}", failures)
    for rel in sorted(expected & actual):
        if digest(ROOT / rel) != entries[rel]:
            fail(f"Checksum mismatch for {rel}", failures)


def scan_for_secrets(path: Path, failures: list[str]) -> None:
    def scan_bytes(data: bytes, location: str) -> None:
        for pattern in SECRET_PATTERNS:
            if pattern.search(data):
                fail(f"Possible secret token in {location} matching {pattern.pattern!r}", failures)

    if path.suffix.lower() in TEXT_SCAN_EXTS:
        scan_bytes(path.read_bytes(), relative(path))
    elif path.suffix.lower() in OFFICE_EXTS:
        try:
            with zipfile.ZipFile(path) as zf:
                for member in zf.namelist():
                    if member.lower().endswith((".xml", ".rels", ".txt", ".json")):
                        scan_bytes(zf.read(member), f"{relative(path)}::{member}")
        except zipfile.BadZipFile:
            fail(f"Invalid Office ZIP container: {relative(path)}", failures)


def main() -> int:
    failures: list[str] = []
    files = iter_repo_files()

    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            fail(f"Missing required path: {rel}", failures)

    for rel, expected in EXPECTED_HASHES.items():
        path = ROOT / rel
        if not path.exists():
            fail(f"Missing hash-locked file: {rel}", failures)
        elif digest(path) != expected:
            fail(f"Hash mismatch for {rel}", failures)

    for path in files:
        if path.stat().st_size > 100 * 1024 * 1024:
            fail(f"File exceeds GitHub 100 MiB limit: {relative(path)}", failures)
        if path.name in FORBIDDEN_NAMES:
            fail(f"Deliberately excluded file present: {relative(path)}", failures)
        scan_for_secrets(path, failures)

    notebooks = [p for p in files if p.suffix.lower() == ".ipynb"]
    for path in notebooks:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(f"Invalid notebook JSON {relative(path)}: {exc}", failures)
            continue
        output_cells = sum(
            1 for cell in data.get("cells", [])
            if cell.get("cell_type") == "code" and cell.get("outputs")
        )
        if output_cells == 0:
            fail(f"Outputless notebook included: {relative(path)}", failures)

    status_path = ROOT / "manifests" / "notebook_execution_status.csv"
    if status_path.exists():
        with status_path.open(newline="", encoding="utf-8") as f:
            status_rows = list(csv.DictReader(f))
        included_paths = [r["repository_path"] for r in status_rows if r["status"] == "included"]
        if len(included_paths) != len(set(included_paths)):
            fail("Duplicate included repository paths in notebook execution manifest", failures)
        actual_notebooks = {relative(p) for p in notebooks}
        if set(included_paths) != actual_notebooks:
            fail("Notebook execution manifest does not match included notebooks", failures)
        for row in status_rows:
            if row["status"] == "included" and int(row["output_cells"] or 0) == 0:
                fail(f"Included source notebook has no outputs: {row['original_path']}", failures)

    validate_manifest(files, failures)
    validate_checksums(files, failures)

    if failures:
        print(f"\nValidation failed with {len(failures)} issue(s).")
        return 1

    print(
        "Validation passed: "
        f"{len(files)} files; {len(notebooks)} output-bearing notebooks; "
        "canonical hashes, file manifests, checksums, size limits, exclusions, and secret scans verified."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
