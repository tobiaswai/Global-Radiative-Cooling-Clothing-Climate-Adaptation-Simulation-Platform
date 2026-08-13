from __future__ import annotations

import csv
import hashlib
import io
import math
from dataclasses import dataclass


MAX_SPECTRUM_FILE_SIZE = 2 * 1024 * 1024
MAX_SPECTRUM_POINTS = 20_000


@dataclass
class ParsedSpectrum:
    points: list[dict[str, float]]
    checksum_sha256: str
    minimum_wavelength_um: float
    maximum_wavelength_um: float


def _normalize_header(value: str) -> str:
    return (
        value.strip()
        .lower()
        .replace(" ", "_")
        .replace("µ", "u")
        .replace("μ", "u")
    )


def parse_spectrum_csv(
    file_bytes: bytes,
) -> ParsedSpectrum:
    if not file_bytes:
        raise ValueError("上傳文件為空")

    if len(file_bytes) > MAX_SPECTRUM_FILE_SIZE:
        raise ValueError(
            "光譜 CSV 不能超過 2 MB"
        )

    try:
        text = file_bytes.decode("utf-8-sig")
    except UnicodeDecodeError as error:
        raise ValueError(
            "CSV 必須使用 UTF-8 編碼"
        ) from error

    reader = csv.DictReader(
        io.StringIO(text)
    )

    if not reader.fieldnames:
        raise ValueError("CSV 缺少表頭")

    header_map = {
        _normalize_header(name): name
        for name in reader.fieldnames
    }

    wavelength_candidates = [
        "wavelength_um",
        "wavelength",
        "lambda_um",
    ]

    value_candidates = [
        "value",
        "reflectance",
        "emissivity",
        "transmittance",
    ]

    wavelength_column = next(
        (
            header_map[name]
            for name in wavelength_candidates
            if name in header_map
        ),
        None,
    )

    value_column = next(
        (
            header_map[name]
            for name in value_candidates
            if name in header_map
        ),
        None,
    )

    if wavelength_column is None:
        raise ValueError(
            "CSV 必須包含 wavelength_um 欄位"
        )

    if value_column is None:
        raise ValueError(
            "CSV 必須包含 value 欄位"
        )

    points: list[dict[str, float]] = []

    for row_number, row in enumerate(
        reader,
        start=2,
    ):
        try:
            wavelength = float(
                row[wavelength_column]
            )
            value = float(
                row[value_column]
            )
        except (
            TypeError,
            ValueError,
            KeyError,
        ) as error:
            raise ValueError(
                f"第 {row_number} 行包含無效數值"
            ) from error

        if not math.isfinite(wavelength):
            raise ValueError(
                f"第 {row_number} 行波長不是有限數值"
            )

        if not math.isfinite(value):
            raise ValueError(
                f"第 {row_number} 行光譜值不是有限數值"
            )

        if wavelength <= 0:
            raise ValueError(
                f"第 {row_number} 行波長必須大於 0"
            )

        if not 0 <= value <= 1:
            raise ValueError(
                f"第 {row_number} 行光譜值必須位於 0 至 1"
            )

        points.append(
            {
                "wavelength_um": wavelength,
                "value": value,
            }
        )

        if len(points) > MAX_SPECTRUM_POINTS:
            raise ValueError(
                "光譜點數不能超過 20000"
            )

    if len(points) < 2:
        raise ValueError(
            "光譜文件至少需要兩個數據點"
        )

    wavelengths = [
        point["wavelength_um"]
        for point in points
    ]

    for previous, current in zip(
        wavelengths,
        wavelengths[1:],
        strict=False,
    ):
        if current <= previous:
            raise ValueError(
                "波長必須嚴格遞增且不能重複"
            )

    return ParsedSpectrum(
        points=points,
        checksum_sha256=hashlib.sha256(
            file_bytes
        ).hexdigest(),
        minimum_wavelength_um=wavelengths[0],
        maximum_wavelength_um=wavelengths[-1],
    )