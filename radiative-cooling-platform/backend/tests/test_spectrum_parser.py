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