import pytest

from app.services.result_export import (
    export_result_csv,
)


@pytest.mark.unit
def test_result_csv_contains_headers(
    simulation_request,
):
    # 可使用現有模擬 fixture 建立結果，
    # 或在此使用已保存的測試結果 fixture。
    expected_headers = [
        "minute",
        "control_core_temperature_c",
        "rc_skin_temperature_c",
    ]

    # result = ...
    # csv_text = export_result_csv(result)

    # for header in expected_headers:
    #     assert header in csv_text