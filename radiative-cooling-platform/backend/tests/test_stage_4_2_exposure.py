import pytest

from app.schemas.global_batch import (
    GlobalBatchCreate,
)
from app.schemas.simulation import (
    MaterialInput,
    PersonInput,
)
from app.services.climate_adaptation import (
    is_exposure_eligible,
)


def make_request(
    *,
    match_mode: str = "all",
) -> GlobalBatchCreate:
    person = PersonInput(
        met=2.0,
        body_surface_area_m2=1.8,
        initial_core_temperature_c=36.8,
        initial_skin_temperature_c=33.7,
    )

    control = MaterialInput(
        name="Control",
        clothing_insulation_clo=0.5,
        solar_reflectance=0.3,
        solar_transmittance=0,
        infrared_emissivity=0.9,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
    )

    radiative = MaterialInput(
        name="Radiative",
        clothing_insulation_clo=0.4,
        solar_reflectance=0.92,
        solar_transmittance=0,
        infrared_emissivity=0.95,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
    )

    return GlobalBatchCreate(
        city_ids=["dubai"],
        sample_days_per_month=3,
        minimum_air_temperature_c=30,
        minimum_solar_radiation_w_m2=300,
        exposure_match_mode=match_mode,
        person=person,
        control_material=control,
        rc_material=radiative,
    )


@pytest.mark.unit
def test_all_mode_requires_all_thresholds():
    request = make_request(
        match_mode="all",
    )

    assert is_exposure_eligible(
        mean_air_temperature_c=35,
        mean_solar_radiation_w_m2=200,
        request=request,
    ) is False


@pytest.mark.unit
def test_any_mode_requires_one_threshold():
    request = make_request(
        match_mode="any",
    )

    assert is_exposure_eligible(
        mean_air_temperature_c=35,
        mean_solar_radiation_w_m2=200,
        request=request,
    ) is True


@pytest.mark.unit
def test_no_threshold_means_all_samples_eligible():
    request = make_request()

    request.minimum_air_temperature_c = None
    request.minimum_solar_radiation_w_m2 = None

    assert is_exposure_eligible(
        mean_air_temperature_c=5,
        mean_solar_radiation_w_m2=0,
        request=request,
    ) is True