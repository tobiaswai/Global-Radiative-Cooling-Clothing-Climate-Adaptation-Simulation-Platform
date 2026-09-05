"""Integration test for the Numba compilation cache."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


BACKEND_ROOT = Path(__file__).resolve().parents[2]


def test_numba_writes_cache_files_to_configured_directory(
    tmp_path: Path,
) -> None:
    module_directory = tmp_path / "module"
    module_directory.mkdir()

    target_module = (
        module_directory
        / "cached_kernel.py"
    )

    target_module.write_text(
        "\n".join(
            [
                '"""Temporary Numba integration target."""',
                "",
                "from numba import njit",
                "",
                "",
                "@njit(cache=True)",
                "def add(left: int, right: int) -> int:",
                "    return left + right",
                "",
            ]
        ),
        encoding="utf-8",
    )

    cache_directory = tmp_path / "numba-cache"

    environment = os.environ.copy()
    environment["NUMBA_CACHE_DIR"] = str(
        cache_directory
    )
    environment["NUMBA_DISABLE_JIT"] = "0"

    python_path_entries = [
        str(module_directory),
        str(BACKEND_ROOT),
    ]

    existing_python_path = environment.get(
        "PYTHONPATH"
    )

    if existing_python_path:
        python_path_entries.append(
            existing_python_path
        )

    environment["PYTHONPATH"] = os.pathsep.join(
        python_path_entries
    )

    command = "\n".join(
        [
            "from app.core.runtime import configure_numba_cache",
            "configure_numba_cache()",
            "from cached_kernel import add",
            "assert add(2, 3) == 5",
        ]
    )

    completed = subprocess.run(
        [
            sys.executable,
            "-c",
            command,
        ],
        cwd=BACKEND_ROOT,
        env=environment,
        capture_output=True,
        text=True,
        timeout=180,
        check=False,
    )

    assert completed.returncode == 0, (
        "The Numba subprocess failed.\n"
        f"stdout:\n{completed.stdout}\n"
        f"stderr:\n{completed.stderr}"
    )

    index_files = list(
        cache_directory.rglob("*.nbi")
    )
    object_files = list(
        cache_directory.rglob("*.nbc")
    )

    assert index_files, (
        "Numba did not create an .nbi cache index."
    )
    assert object_files, (
        "Numba did not create an .nbc cache object."
    )