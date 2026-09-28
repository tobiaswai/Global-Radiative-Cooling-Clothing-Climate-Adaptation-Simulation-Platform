"""Dump the OpenAPI schema for before/after contract diffs."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.main import app  # noqa: E402


def main() -> None:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    payload = json.dumps(app.openapi(), indent=2, sort_keys=True, ensure_ascii=False)
    if target is None:
        print(payload)
    else:
        target.write_text(payload, encoding="utf-8")
        print(f"wrote {target}")


if __name__ == "__main__":
    main()