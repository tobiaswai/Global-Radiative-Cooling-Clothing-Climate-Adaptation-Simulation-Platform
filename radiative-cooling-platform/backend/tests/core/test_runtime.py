"""Tests for process-level runtime configuration."""

from pathlib import Path

from app.core.runtime import configure_numba_cache


def test_uses_configured_cache_directory(
    monkeypatch,
    tmp_path: Path,
) -> None:
    monkeypatch.delenv("NUMBA_CACHE_DIR", raising=False)

    configured_directory = tmp_path / "configured-cache"

    result = configure_numba_cache(configured_directory)

    assert result == configured_directory.resolve()
    assert result.is_dir()
    assert result.exists()
    assert result.as_posix() in (
        Path(result).as_posix(),
    )


def test_environment_variable_takes_precedence(
    monkeypatch,
    tmp_path: Path,
) -> None:
    environment_directory = tmp_path / "environment-cache"
    configured_directory = tmp_path / "configured-cache"

    monkeypatch.setenv(
        "NUMBA_CACHE_DIR",
        str(environment_directory),
    )

    result = configure_numba_cache(configured_directory)

    assert result == environment_directory.resolve()
    assert result.is_dir()


def test_uses_cross_platform_temporary_default(
    monkeypatch,
    tmp_path: Path,
) -> None:
    monkeypatch.delenv("NUMBA_CACHE_DIR", raising=False)

    result = configure_numba_cache(
        temporary_root=tmp_path,
    )

    expected = (
        tmp_path
        / "radiative-cooling-platform"
        / "numba"
    ).resolve()

    assert result == expected
    assert result.is_dir()


def test_creates_missing_parent_directories(
    monkeypatch,
    tmp_path: Path,
) -> None:
    monkeypatch.delenv("NUMBA_CACHE_DIR", raising=False)

    configured_directory = (
        tmp_path
        / "first"
        / "second"
        / "numba"
    )

    assert not configured_directory.exists()

    result = configure_numba_cache(configured_directory)

    assert result.exists()
    assert result.is_dir()