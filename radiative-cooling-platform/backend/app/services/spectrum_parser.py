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
        raise ValueError("Uploaded file is empty")

    if len(file_bytes) > MAX_SPECTRUM_FILE_SIZE:
        raise ValueError(
            "Spectrum CSV cannot exceed 2 MB"
        )

    try:
        text = file_bytes.decode("utf-8-sig")
    except UnicodeDecodeError as error:
        raise ValueError(
            "CSV must use UTF-8 encoding"
        ) from error

    reader = csv.DictReader(
        io.StringIO(text)
    )

    if not reader.fieldnames:
        raise ValueError("CSV is missing headers")

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
            "CSV must include a 'wavelength_um' column"
        )

    if value_column is None:
        raise ValueError(
            "CSV must include a 'value' column"
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
                f"Row {row_number} contains invalid values"
            ) from error

        if not math.isfinite(wavelength):
            raise ValueError(
                f"Row {row_number} wavelength is not a finite value"
            )

        if not math.isfinite(value):
            raise ValueError(
                f"Row {row_number} spectrum value is not a finite value"
            )

        if wavelength <= 0:
            raise ValueError(
                f"Row {row_number} wavelength must be positive"
            )

        if not 0 <= value <= 1:
            raise ValueError(
                f"Row {row_number} spectrum value must be between 0 and 1"
            )

        points.append(
            {
                "wavelength_um": wavelength,
                "value": value,
            }
        )

        if len(points) > MAX_SPECTRUM_POINTS:
            raise ValueError(
                "Row {row_number} spectrum points cannot exceed 20000"
            )

    if len(points) < 2:
        raise ValueError(
            "Row {row_number} spectrum file must contain at least two data points"
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
                "Row {row_number} wavelengths must be strictly increasing and unique"
            )

    return ParsedSpectrum(
        points=points,
        checksum_sha256=hashlib.sha256(
            file_bytes
        ).hexdigest(),
        minimum_wavelength_um=wavelengths[0],
        maximum_wavelength_um=wavelengths[-1],
    )