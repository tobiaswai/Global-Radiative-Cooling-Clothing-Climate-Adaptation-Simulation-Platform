import gzip
import json
from pathlib import Path

from app.core.config import settings
from app.schemas.simulation import (
    WeatherSimulationResponse,
)


def save_simulation_result(
    job_id: str,
    result: WeatherSimulationResponse,
) -> Path:
    result_directory = (
        settings.result_directory
    )
    result_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    final_path = (
        result_directory
        / f"{job_id}.json.gz"
    )

    temporary_path = (
        result_directory
        / f"{job_id}.tmp.json.gz"
    )

    with gzip.open(
        temporary_path,
        mode="wt",
        encoding="utf-8",
    ) as file:
        json.dump(
            result.model_dump(mode="json"),
            file,
            ensure_ascii=False,
            separators=(",", ":"),
        )

    temporary_path.replace(final_path)

    return final_path


def load_simulation_result(
    result_path: str,
) -> WeatherSimulationResponse:
    path = Path(result_path)

    if not path.exists():
        raise FileNotFoundError(
            f"The result file does not exist:{path}"
        )

    with gzip.open(
        path,
        mode="rt",
        encoding="utf-8",
    ) as file:
        payload = json.load(file)

    return WeatherSimulationResponse.model_validate(
        payload
    )