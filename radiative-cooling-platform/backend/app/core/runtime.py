"""Process-level runtime configuration."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path
from typing import Final


APPLICATION_CACHE_DIRECTORY_NAME: Final = (
    "radiative-cooling-platform"
)
NUMBA_CACHE_DIRECTORY_NAME: Final = "numba"
NUMBA_CACHE_ENVIRONMENT_VARIABLE: Final = "NUMBA_CACHE_DIR"

PathValue = str | os.PathLike[str]


def _read_path_value(
    value: PathValue | None,
) -> str | None:
    """Convert a path-like value into non-empty text."""
    if value is None:
        return None

    raw_value = os.fspath(value)

    if not isinstance(raw_value, str):
        raise TypeError("Path values must resolve to text.")

    normalized_value = raw_value.strip()

    return normalized_value or None


def normalize_path(path_value: PathValue) -> Path:
    """Expand and convert a path into an absolute path."""
    normalized_value = _read_path_value(path_value)

    if normalized_value is None:
        raise ValueError("A non-empty path is required.")

    expanded_value = os.path.expandvars(
        os.path.expanduser(normalized_value)
    )

    path = Path(expanded_value)

    if not path.is_absolute():
        path = Path.cwd() / path

    return path.resolve(strict=False)


def _prepare_cache_directory(
    cache_directory: Path,
) -> None:
    """Create the cache directory and verify write access."""
    try:
        cache_directory.mkdir(
            mode=0o700,
            parents=True,
            exist_ok=True,
        )

        if not cache_directory.is_dir():
            raise NotADirectoryError(
                f"{cache_directory} is not a directory."
            )

        with tempfile.NamedTemporaryFile(
            mode="w+b",
            prefix=".numba-cache-write-test-",
            dir=cache_directory,
        ) as probe_file:
            probe_file.write(b"ok")
            probe_file.flush()

    except OSError as error:
        raise RuntimeError(
            "Unable to create or write to the Numba cache "
            f"directory at {cache_directory}."
        ) from error


def configure_numba_cache(
    configured_directory: PathValue | None = None,
    *,
    temporary_root: PathValue | None = None,
) -> Path:
    """Configure a writable cross-platform Numba cache.

    Directory precedence:

    1. The process NUMBA_CACHE_DIR environment variable.
    2. The configured_directory argument.
    3. An application-specific system temporary directory.
    """
    environment_directory = _read_path_value(
        os.environ.get(NUMBA_CACHE_ENVIRONMENT_VARIABLE)
    )
    settings_directory = _read_path_value(
        configured_directory
    )

    if environment_directory is not None:
        cache_directory = normalize_path(
            environment_directory
        )
    elif settings_directory is not None:
        cache_directory = normalize_path(
            settings_directory
        )
    else:
        temporary_root_value = _read_path_value(
            temporary_root
        )

        if temporary_root_value is not None:
            root_directory = normalize_path(
                temporary_root_value
            )
        else:
            root_directory = normalize_path(
                tempfile.gettempdir()
            )

        cache_directory = (
            root_directory
            / APPLICATION_CACHE_DIRECTORY_NAME
            / NUMBA_CACHE_DIRECTORY_NAME
        ).resolve(strict=False)

    _prepare_cache_directory(cache_directory)

    os.environ[NUMBA_CACHE_ENVIRONMENT_VARIABLE] = str(
        cache_directory
    )

    return cache_directory


def configure_runtime(
    numba_cache_dir: PathValue | None = None,
) -> Path:
    """Configure process-level runtime directories."""
    return configure_numba_cache(
        configured_directory=numba_cache_dir,
    )