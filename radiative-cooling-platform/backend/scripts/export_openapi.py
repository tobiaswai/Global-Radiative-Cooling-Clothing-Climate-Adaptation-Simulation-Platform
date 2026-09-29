"""Snapshot the OpenAPI contract. Usage: python scripts/export_openapi.py OUT.json"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.main import app  # noqa: E402

Path(sys.argv[1]).write_text(
    json.dumps(app.openapi(), indent=2, sort_keys=True), encoding="utf-8"
)