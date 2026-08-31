import pytest

from app.core.cities import (
    CITIES,
    get_city,
)


@pytest.mark.unit
def test_get_city_returns_supported_city():
    city = get_city("dubai")

    assert city.id == "dubai"
    assert city.name == "Dubai"
    assert city.country == (
        "United Arab Emirates"
    )
    assert city.timezone == "Asia/Dubai"


@pytest.mark.unit
def test_get_city_normalizes_case_and_spaces():
    city = get_city("  DuBaI  ")

    assert city is CITIES["dubai"]


@pytest.mark.unit
@pytest.mark.parametrize(
    "city_id",
    [
        "dubai",
        "guangzhou",
        "lhasa",
    ],
)
def test_all_configured_cities_can_be_loaded(
    city_id,
):
    city = get_city(city_id)

    assert city.id == city_id
    assert city.latitude != 0
    assert city.longitude != 0
    assert city.timezone


@pytest.mark.unit
def test_get_city_rejects_unknown_city():
    with pytest.raises(
        ValueError,
        match="City not supported",
    ):
        get_city("hong-kong")


@pytest.mark.unit
def test_unknown_city_error_lists_supported_cities():
    with pytest.raises(ValueError) as error:
        get_city("unknown")

    message = str(error.value)

    assert "dubai" in message
    assert "guangzhou" in message
    assert "lhasa" in message