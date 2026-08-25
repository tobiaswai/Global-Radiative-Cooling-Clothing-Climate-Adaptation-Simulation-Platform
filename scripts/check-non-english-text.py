from pathlib import Path
import re
import sys

ROOTS = [
    Path("radiative-cooling-platform/frontend/src"),
    Path("radiative-cooling-platform/backend/app"),
    Path("radiative-cooling-platform/backend/tests"),
    Path(".github/workflows"),
]

EXCLUDED_PARTS = {
    ".git",
    ".next",
    ".venv",
    "node_modules",
    ".numba_cache",
    "htmlcov",
    "__pycache__",
}

HAN_PATTERN = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")

violations = []

for root in ROOTS:
    if not root.exists():
        continue

    for path in root.rglob("*"):
        if not path.is_file():
            continue

        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue

        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        for line_number, line in enumerate(content.splitlines(), start=1):
            if HAN_PATTERN.search(line):
                violations.append(
                    (path, line_number, line.strip())
                )

if violations:
    print("Chinese text was found:")
    for path, line_number, line in violations:
        print(f"{path}:{line_number}: {line}")
    sys.exit(1)

print("No Chinese text was found in the checked source files.")