"""Tests for process-level runtime configuration."""

from __future__ import annotations

import os
from pathlib import Path

import pytest

from app.core.runtime import (
    NUMBA_CACHE_ENVIRONMENT_VARIABLE,
    configure_numba_cache,
)


def test_uses_configured_cache_directory(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.delenv(
        NUMBA_CACHE_ENVIRONMENT_VARIABLE,
        raising=False,
    )

    configured_directory = (
        tmp_path
        / "configured cache"
    )

    result = configure_numba_cache(
        configured_directory
    )

    assert result == configured_directory.resolve()
    assert result.exists()
    assert result.is_dir()
    assert (
        os.environ[NUMBA_CACHE_ENVIRONMENT_VARIABLE]
        == str(result)
    )


def test_environment_variable_takes_precedence(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    environment_directory = (
        tmp_path
        / "environment-cache"
    )
    configured_directory = (
        tmp_path
        / "configured-cache"
    )

    monkeypatch.setenv(
        NUMBA_CACHE_ENVIRONMENT_VARIABLE,
        str(environment_directory),
    )

    result = configure_numba_cache(
        configured_directory
    )

    assert result == environment_directory.resolve()
    assert result.exists()
    assert result.is_dir()


def test_blank_environment_variable_is_ignored(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    configured_directory = (
        tmp_path
        / "configured-cache"
    )

    monkeypatch.setenv(
        NUMBA_CACHE_ENVIRONMENT_VARIABLE,
        "   ",
    )

    result = configure_numba_cache(
        configured_directory
    )

    assert result == configured_directory.resolve()
    assert result.is_dir()


def test_uses_cross_platform_temporary_default(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.delenv(
        NUMBA_CACHE_ENVIRONMENT_VARIABLE,
        raising=False,
    )

    result = configure_numba_cache(
        temporary_root=tmp_path,
    )

    expected_directory = (
        tmp_path
        / "radiative-cooling-platform"
        / "numba"
    ).resolve()

    assert result == expected_directory
    assert result.exists()
    assert result.is_dir()
    assert (
        os.environ[NUMBA_CACHE_ENVIRONMENT_VARIABLE]
        == str(expected_directory)
    )


def test_resolves_relative_path_from_working_directory(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.delenv(
        NUMBA_CACHE_ENVIRONMENT_VARIABLE,
        raising=False,
    )
    monkeypatch.chdir(tmp_path)

    result = configure_numba_cache(
        "var/numba"
    )

    expected_directory = (
        tmp_path
        / "var"
        / "numba"
    ).resolve()

    assert result == expected_directory
    assert result.is_dir()


def test_creates_missing_parent_directories(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.delenv(
        NUMBA_CACHE_ENVIRONMENT_VARIABLE,
        raising=False,
    )

    configured_directory = (
        tmp_path
        / "first"
        / "second"
        / "numba"
    )

    assert not configured_directory.exists()

    result = configure_numba_cache(
        configured_directory
    )

    assert result == configured_directory.resolve()
    assert result.exists()
    assert result.is_dir()


def test_removes_write_probe_after_validation(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.delenv(
        NUMBA_CACHE_ENVIRONMENT_VARIABLE,
        raising=False,
    )

    result = configure_numba_cache(
        tmp_path / "numba-cache"
    )

    probe_files = list(
        result.glob(".numba-cache-write-test-*")
    )

    assert probe_files == []


def test_rejects_path_that_is_an_existing_file(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.delenv(
        NUMBA_CACHE_ENVIRONMENT_VARIABLE,
        raising=False,
    )

    invalid_directory = tmp_path / "not-a-directory"
    invalid_directory.write_text(
        "This path is a file.",
        encoding="utf-8",
    )

    with pytest.raises(
        RuntimeError,
        match=(
            "Unable to create or write to the "
            "Numba cache directory"
        ),
    ):
        configure_numba_cache(
            invalid_directory
        )