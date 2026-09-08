"""Allowlisted local filesystem discovery and scanning tools."""
from __future__ import annotations

import hashlib
from collections import Counter
from pathlib import Path
from collections.abc import Callable
from typing import Any, Iterable

from app.core.config import settings
from app.tools.detection_tools import detect_masked
from app.utils.file_parser import FileParser


SUPPORTED_EXTENSIONS = {
    ".txt",
    ".csv",
    ".json",
    ".xml",
    ".log",
    ".pdf",
    ".docx",
    ".xlsx",
}
ScanProgressCallback = Callable[[dict[str, Any]], None]


def _allowed_roots(configured: str | None = None) -> list[Path]:
    raw = configured or settings.SYSTEM_SCAN_ALLOWED_ROOTS
    return [Path(item.strip()).expanduser().resolve() for item in raw.split(",") if item.strip()]


def validate_allowed_path(root_path: str, allowed_roots: Iterable[Path] | None = None) -> Path:
    requested = Path(root_path).expanduser().resolve(strict=True)

    # SYSTEM_SCAN_ALLOW_ANY_PATH=true (dev default) -- scan whatever path
    # is entered, no allowlist check. Set it to false in .env to go back
    # to only-SYSTEM_SCAN_ALLOWED_ROOTS-is-scannable, which is what a
    # shared/production deployment should always use -- a typo or a
    # malicious goal string should never be able to point a scan at the
    # whole filesystem there.
    if allowed_roots is None and settings.SYSTEM_SCAN_ALLOW_ANY_PATH:
        return requested

    roots = list(allowed_roots or _allowed_roots())
    if not any(requested == root or root in requested.parents for root in roots):
        raise PermissionError(f"Scan path is outside configured allowlist: {requested}")
    return requested


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _safe_file_size(path: Path) -> int:
    try:
        return path.stat().st_size
    except OSError:
        return 0


def scan_system_path(
    root_path: str,
    *,
    entities: set[str],
    previous_hashes: dict[str, str] | None = None,
    max_file_size_mb: int | None = None,
    allowed_roots: Iterable[Path] | None = None,
    progress_callback: ScanProgressCallback | None = None,
    file_extensions: Iterable[str] | None = None,
) -> dict[str, Any]:
    """Scan one or more root paths (comma-separated) and merge results.

    Multiple paths (e.g. "D:\\a, D:\\b") each get validated against the
    allowlist independently -- one disallowed path fails the whole call,
    same as before, so this doesn't weaken the allowlist check per path.

    file_extensions restricts discovery to those extensions (e.g.
    {".csv", ".pdf"}) -- must still be a subset of SUPPORTED_EXTENSIONS,
    since those are the only formats FileParser/detection actually handle.
    """
    roots = [item.strip() for item in root_path.split(",") if item.strip()]
    if not roots:
        raise ValueError("No scan path provided")

    if len(roots) == 1:
        return _scan_single_root_path(
            roots[0],
            entities=entities,
            previous_hashes=previous_hashes,
            max_file_size_mb=max_file_size_mb,
            allowed_roots=allowed_roots,
            progress_callback=progress_callback,
            file_extensions=file_extensions,
        )

    merged_stats = {
        "files_discovered": 0,
        "files_processed": 0,
        "files_scanned": 0,
        "files_skipped": 0,
        "files_failed": 0,
        "bytes_discovered": 0,
        "bytes_processed": 0,
        "bytes_scanned": 0,
        "findings_detected": 0,
        "progress_percent": 0,
        "total_files": 0,
        "total_bytes": 0,
    }
    merged_findings: list[dict[str, Any]] = []
    merged_hashes: dict[str, str] = {}
    merged_errors: list[dict[str, str]] = []
    remaining_hashes = dict(previous_hashes or {})

    for single_root in roots:
        result = _scan_single_root_path(
            single_root,
            entities=entities,
            previous_hashes=remaining_hashes,
            max_file_size_mb=max_file_size_mb,
            allowed_roots=allowed_roots,
            progress_callback=progress_callback,
            file_extensions=file_extensions,
        )
        for key in merged_stats:
            merged_stats[key] += result["stats"].get(key, 0)
        merged_findings.extend(result["findings"])
        merged_hashes.update(result["file_hashes"])
        merged_errors.extend(result["errors"])

    total = merged_stats["files_discovered"] or 1
    merged_stats["progress_percent"] = round(
        (merged_stats["files_scanned"] + merged_stats["files_skipped"] + merged_stats["files_failed"])
        * 100
        / total
    )
    counts = Counter(item["entity_type"] for item in merged_findings)

    return {
        "stats": merged_stats,
        "findings": merged_findings,
        "entity_counts": dict(counts),
        "file_hashes": merged_hashes,
        "errors": merged_errors,
    }


def _scan_single_root_path(
    root_path: str,
    *,
    entities: set[str],
    previous_hashes: dict[str, str] | None = None,
    max_file_size_mb: int | None = None,
    allowed_roots: Iterable[Path] | None = None,
    progress_callback: ScanProgressCallback | None = None,
    file_extensions: Iterable[str] | None = None,
) -> dict[str, Any]:
    root = validate_allowed_path(root_path, allowed_roots)
    previous_hashes = previous_hashes or {}
    max_bytes = (max_file_size_mb or settings.MAX_FILE_SIZE_MB) * 1024 * 1024
    findings: list[dict[str, Any]] = []
    hashes: dict[str, str] = {}
    stats = {
        "files_discovered": 0,
        "files_processed": 0,
        "files_scanned": 0,
        "files_skipped": 0,
        "files_failed": 0,
        "bytes_discovered": 0,
        "bytes_processed": 0,
        "bytes_scanned": 0,
        "findings_detected": 0,
        "progress_percent": 0,
    }
    errors: list[dict[str, str]] = []

    paths = [root] if root.is_file() else list(root.rglob("*"))
    active_extensions = (
        {ext.lower() for ext in file_extensions} & SUPPORTED_EXTENSIONS
        if file_extensions
        else SUPPORTED_EXTENSIONS
    )
    paths = [
        path
        for path in paths
        if path.is_file() and path.suffix.lower() in active_extensions
    ]
    stats["files_discovered"] = len(paths)
    stats["total_files"] = len(paths)
    stats["bytes_discovered"] = sum(_safe_file_size(path) for path in paths)
    stats["total_bytes"] = stats["bytes_discovered"]

    def publish_progress() -> None:
        stats["files_processed"] = (
            stats["files_scanned"]
            + stats["files_skipped"]
            + stats["files_failed"]
        )
        stats["findings_detected"] = len(findings)
        stats["progress_percent"] = (
            round(stats["files_processed"] * 100 / len(paths))
            if paths
            else 100
        )

        if progress_callback is not None:
            progress_callback(
                {
                    "stats": dict(stats),
                    "findings": list(findings),
                    "file_hashes": dict(hashes),
                    "errors": list(errors),
                }
            )

    publish_progress()

    for path in paths:
        try:
            file_size = path.stat().st_size

            if file_size > max_bytes:
                stats["files_skipped"] += 1
                stats["bytes_processed"] += file_size
                errors.append({"path": str(path), "error": "file_too_large"})
                publish_progress()
                continue
            digest = file_sha256(path)
            hashes[str(path)] = digest
            if previous_hashes.get(str(path)) == digest:
                stats["files_skipped"] += 1
                stats["bytes_processed"] += file_size
                publish_progress()
                continue
            text = FileParser.parse(str(path))
            if text is None:
                raise ValueError("unsupported_or_unreadable")
            location = {
                "source": "system",
                "path": str(path),
                "sha256": digest,
                "size_bytes": file_size,
            }
            matches = detect_masked(text, location)
            findings.extend(match for match in matches if match["entity_type"] in entities)
            stats["files_scanned"] += 1
            stats["bytes_scanned"] += file_size
            stats["bytes_processed"] += file_size
        except Exception as exc:
            stats["files_failed"] += 1
            stats["bytes_processed"] += _safe_file_size(path)
            errors.append({"path": str(path), "error": type(exc).__name__})
        publish_progress()

    counts = Counter(item["entity_type"] for item in findings)
    return {
        "stats": stats,
        "findings": findings,
        "entity_counts": dict(counts),
        "file_hashes": hashes,
        "errors": errors,
    } 