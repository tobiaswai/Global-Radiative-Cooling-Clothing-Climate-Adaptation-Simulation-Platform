from app.schemas.global_batch import (
    GlobalBatchCreate,
)
from app.schemas.simulation import (
    MaterialInput,
    PersonInput,
)


def make_batch_request():
    return GlobalBatchCreate(
        city_ids=[
            "dubai",
            "guangzhou",
        ],
        year=2023,
        start_month=1,
        end_month=3,
        representative_day=15,
        local_start_hour=12,
        duration_minutes=120,
        output_interval_minutes=10,
        minimum_skin_improvement_c=0.2,
        person=PersonInput(
            met=2.0,
            body_surface_area_m2=1.8,
            initial_core_temperature_c=36.8,
            initial_skin_temperature_c=33.7,
        ),
        control_material=MaterialInput(
            name="Control",
            clothing_insulation_clo=0.5,
            solar_reflectance=0.3,
            solar_transmittance=0,
            infrared_emissivity=0.9,
            projected_solar_area_factor=0.25,
            absorbed_solar_to_body_fraction=0.35,
        ),
        rc_material=MaterialInput(
            name="RC",
            clothing_insulation_clo=0.4,
            solar_reflectance=0.92,
            solar_transmittance=0,
            infrared_emissivity=0.95,
            projected_solar_area_factor=0.25,
            absorbed_solar_to_body_fraction=0.35,
        ),
    )


def test_global_batch_month_range():
    request = make_batch_request()

    assert request.start_month == 1
    assert request.end_month == 3
    assert len(request.city_ids) == 2


def test_global_batch_rejects_duplicate_cities():
    request = make_batch_request().model_dump()
    request["city_ids"] = [
        "dubai",
        "dubai",
    ]

    try:
        GlobalBatchCreate.model_validate(
            request
        )
        assert False
    except ValueError as error:
        assert "duplicate" in str(error)