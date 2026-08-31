import gzip
import json
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from app.services import result_storage


class FakeSimulationResult:
    """提供 save_simulation_result 所需的最小介面。"""

    def __init__(self, payload):
        self.payload = payload
        self.requested_mode = None

    def model_dump(self, *, mode):
        self.requested_mode = mode
        return self.payload


@pytest.mark.unit
def test_save_simulation_result_creates_gzip_json_file(
    tmp_path,
    monkeypatch,
):
    result_directory = tmp_path / "results"

    monkeypatch.setattr(
        result_storage.settings,
        "result_directory",
        result_directory,
    )

    payload = {
        "city": "Dubai",
        "duration_minutes": 120,
        "warning": "測試警告",
    }
    result = FakeSimulationResult(payload)

    saved_path = result_storage.save_simulation_result(
        job_id="job-123",
        result=result,
    )

    assert saved_path == result_directory / "job-123.json.gz"
    assert saved_path.exists()
    assert saved_path.is_file()

    with gzip.open(
        saved_path,
        mode="rt",
        encoding="utf-8",
    ) as file:
        saved_payload = json.load(file)

    assert saved_payload == payload
    assert result.requested_mode == "json"


@pytest.mark.unit
def test_save_simulation_result_creates_missing_directory(
    tmp_path,
    monkeypatch,
):
    result_directory = (
        tmp_path
        / "nested"
        / "simulation"
        / "results"
    )

    assert not result_directory.exists()

    monkeypatch.setattr(
        result_storage.settings,
        "result_directory",
        result_directory,
    )

    result = FakeSimulationResult(
        {
            "city": "Dubai",
            "duration_minutes": 60,
        }
    )

    saved_path = result_storage.save_simulation_result(
        job_id="directory-test",
        result=result,
    )

    assert result_directory.exists()
    assert saved_path.exists()


@pytest.mark.unit
def test_save_simulation_result_removes_temporary_file(
    tmp_path,
    monkeypatch,
):
    monkeypatch.setattr(
        result_storage.settings,
        "result_directory",
        tmp_path,
    )

    result = FakeSimulationResult(
        {
            "city": "Tokyo",
            "warning": "",
        }
    )

    saved_path = result_storage.save_simulation_result(
        job_id="atomic-test",
        result=result,
    )

    temporary_path = tmp_path / "atomic-test.tmp.json.gz"

    assert saved_path.exists()
    assert not temporary_path.exists()


@pytest.mark.unit
def test_save_simulation_result_preserves_unicode(
    tmp_path,
    monkeypatch,
):
    monkeypatch.setattr(
        result_storage.settings,
        "result_directory",
        tmp_path,
    )

    payload = {
        "city": "臺北",
        "environment_model_note": "模擬結果測試",
        "warning": "高溫警告",
    }
    result = FakeSimulationResult(payload)

    saved_path = result_storage.save_simulation_result(
        job_id="unicode-test",
        result=result,
    )

    with gzip.open(
        saved_path,
        mode="rt",
        encoding="utf-8",
    ) as file:
        raw_json = file.read()

    assert "臺北" in raw_json
    assert "模擬結果測試" in raw_json
    assert "高溫警告" in raw_json
    assert "\\u81fa" not in raw_json

    assert json.loads(raw_json) == payload


@pytest.mark.unit
def test_save_simulation_result_replaces_existing_file(
    tmp_path,
    monkeypatch,
):
    monkeypatch.setattr(
        result_storage.settings,
        "result_directory",
        tmp_path,
    )

    old_result = FakeSimulationResult(
        {
            "city": "Old city",
            "duration_minutes": 30,
        }
    )
    new_result = FakeSimulationResult(
        {
            "city": "New city",
            "duration_minutes": 120,
        }
    )

    first_path = result_storage.save_simulation_result(
        job_id="same-job",
        result=old_result,
    )
    second_path = result_storage.save_simulation_result(
        job_id="same-job",
        result=new_result,
    )

    assert first_path == second_path

    with gzip.open(
        second_path,
        mode="rt",
        encoding="utf-8",
    ) as file:
        saved_payload = json.load(file)

    assert saved_payload == {
        "city": "New city",
        "duration_minutes": 120,
    }


@pytest.mark.unit
def test_load_simulation_result_reads_and_validates_payload(
    tmp_path,
    monkeypatch,
):
    result_path = tmp_path / "load-test.json.gz"

    payload = {
        "city": "Dubai",
        "duration_minutes": 120,
        "warning": "",
    }

    with gzip.open(
        result_path,
        mode="wt",
        encoding="utf-8",
    ) as file:
        json.dump(
            payload,
            file,
            ensure_ascii=False,
        )

    expected_result = object()
    model_validate = Mock(
        return_value=expected_result
    )

    fake_response_model = SimpleNamespace(
        model_validate=model_validate
    )

    monkeypatch.setattr(
        result_storage,
        "WeatherSimulationResponse",
        fake_response_model,
    )

    loaded_result = (
        result_storage.load_simulation_result(
            str(result_path)
        )
    )

    assert loaded_result is expected_result
    model_validate.assert_called_once_with(payload)


@pytest.mark.unit
def test_load_simulation_result_raises_for_missing_file(
    tmp_path,
):
    missing_path = (
        tmp_path / "does-not-exist.json.gz"
    )

    with pytest.raises(
        FileNotFoundError,
        match="The result file does not exist",
    ):
        result_storage.load_simulation_result(
            str(missing_path)
        )