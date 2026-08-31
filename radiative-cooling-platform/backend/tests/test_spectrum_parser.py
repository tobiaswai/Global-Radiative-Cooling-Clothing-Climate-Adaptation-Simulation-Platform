import pytest

from app.services.spectrum_parser import (
    parse_spectrum_csv,
)


@pytest.mark.unit
def test_parse_valid_spectrum_csv():
    content = (
        "wavelength_um,value\n"
        "0.3,0.91\n"
        "0.5,0.92\n"
        "1.0,0.93\n"
    ).encode("utf-8")

    result = parse_spectrum_csv(content)

    assert len(result.points) == 3
    assert (
        result.minimum_wavelength_um
        == pytest.approx(0.3)
    )
    assert (
        result.maximum_wavelength_um
        == pytest.approx(1.0)
    )


@pytest.mark.unit
def test_reject_value_above_one():
    content = (
        "wavelength_um,value\n"
        "0.3,0.9\n"
        "0.5,1.2\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="0 and 1",
    ):
        parse_spectrum_csv(content)


@pytest.mark.unit
def test_reject_unsorted_wavelengths():
    content = (
        "wavelength_um,value\n"
        "1.0,0.9\n"
        "0.5,0.8\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="strictly increasing",
    ):
        parse_spectrum_csv(content)

import hashlib

from app.services import spectrum_parser


@pytest.mark.unit
def test_parse_spectrum_returns_checksum():
    content = (
        "wavelength_um,value\n"
        "0.3,0.9\n"
        "0.5,0.8\n"
    ).encode("utf-8")

    result = parse_spectrum_csv(content)

    assert result.checksum_sha256 == (
        hashlib.sha256(content).hexdigest()
    )


@pytest.mark.unit
def test_parse_normalizes_header_names():
    content = (
        " Wavelength µm , Reflectance \n"
        "0.3,0.9\n"
        "0.5,0.8\n"
    ).encode("utf-8")

    result = parse_spectrum_csv(content)

    assert len(result.points) == 2


@pytest.mark.unit
def test_reject_empty_spectrum():
    with pytest.raises(
        ValueError,
        match="empty",
    ):
        parse_spectrum_csv(b"")


@pytest.mark.unit
def test_reject_non_utf8_spectrum():
    with pytest.raises(
        ValueError,
        match="UTF-8",
    ):
        parse_spectrum_csv(b"\xff\xfe\xfa")


@pytest.mark.unit
def test_reject_missing_wavelength_column():
    content = (
        "frequency,value\n"
        "1.0,0.9\n"
        "2.0,0.8\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="wavelength_um",
    ):
        parse_spectrum_csv(content)


@pytest.mark.unit
def test_reject_missing_value_column():
    content = (
        "wavelength_um,measurement\n"
        "0.3,0.9\n"
        "0.5,0.8\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="'value'",
    ):
        parse_spectrum_csv(content)


@pytest.mark.unit
@pytest.mark.parametrize(
    "row",
    [
        "not-a-number,0.8",
        "0.3,not-a-number",
    ],
)
def test_reject_invalid_numeric_values(row):
    content = (
        "wavelength_um,value\n"
        f"{row}\n"
        "0.5,0.7\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="invalid values",
    ):
        parse_spectrum_csv(content)


@pytest.mark.unit
@pytest.mark.parametrize(
    ("row", "message"),
    [
        ("nan,0.8", "wavelength"),
        ("0.3,nan", "spectrum value"),
        ("-0.3,0.8", "positive"),
        ("0.3,-0.1", "between 0 and 1"),
    ],
)
def test_reject_invalid_spectrum_ranges(
    row,
    message,
):
    content = (
        "wavelength_um,value\n"
        f"{row}\n"
        "0.5,0.7\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match=message,
    ):
        parse_spectrum_csv(content)


@pytest.mark.unit
def test_reject_single_data_point():
    content = (
        "wavelength_um,value\n"
        "0.3,0.9\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="at least two",
    ):
        parse_spectrum_csv(content)


@pytest.mark.unit
def test_reject_file_above_size_limit(
    monkeypatch,
):
    monkeypatch.setattr(
        spectrum_parser,
        "MAX_SPECTRUM_FILE_SIZE",
        10,
    )

    with pytest.raises(
        ValueError,
        match="2 MB",
    ):
        spectrum_parser.parse_spectrum_csv(
            b"x" * 11
        )


@pytest.mark.unit
def test_reject_too_many_points(
    monkeypatch,
):
    monkeypatch.setattr(
        spectrum_parser,
        "MAX_SPECTRUM_POINTS",
        2,
    )

    content = (
        "wavelength_um,value\n"
        "0.1,0.9\n"
        "0.2,0.8\n"
        "0.3,0.7\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="cannot exceed",
    ):
        spectrum_parser.parse_spectrum_csv(
            content
        )