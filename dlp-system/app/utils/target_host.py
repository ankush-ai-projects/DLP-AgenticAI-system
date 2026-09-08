"""Target host normalization shared by asset registration and scan runtime."""

from __future__ import annotations

import re
import socket


def resolve_system_target_host(
    configured_host: str | None,
    root_path: str | None,
) -> str:
    """Resolve a system target to an entered host, UNC server, or local host."""
    normalized_host = (configured_host or "").strip()
    if normalized_host:
        return normalized_host

    normalized_path = (root_path or "").strip().replace("/", "\\")
    unc_match = re.match(r"^\\\\([^\\]+)\\", normalized_path)
    if unc_match:
        return unc_match.group(1)

    return socket.gethostname()
