"""Local Windows/Linux endpoint scanner CLI that emits masked JSON only."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from app.tools.filesystem_tools import scan_system_path


def main() -> int:
    parser = argparse.ArgumentParser(description="SentinelDLP endpoint scanner")
    parser.add_argument("scan", choices=["scan"])
    parser.add_argument("--path", required=True)
    parser.add_argument("--allowed-root", required=True)
    parser.add_argument("--entities", default="CREDIT_CARD,AADHAAR,PAN,EMAIL,PHONE")
    parser.add_argument("--output", default="scan-result.json")
    args = parser.parse_args()
    result = scan_system_path(
        args.path,
        entities={item.strip().upper() for item in args.entities.split(",") if item.strip()},
        allowed_roots=[Path(args.allowed_root).expanduser().resolve()],
    )
    output = Path(args.output).expanduser().resolve()
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({"status": "completed", "output": str(output), "stats": result["stats"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
