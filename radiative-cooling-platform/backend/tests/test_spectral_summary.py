import pytest

from app.services.spectral_summary import summarize_ir_spectrum


def spectrum(fn, start=2.0, stop=25.0, step=0.01):
    count = int(round((stop - start) / step)) + 1
    return [
        {"wavelength_um": round(start + i * step, 4), "value": fn(start + i * step)}
        for i in range(count)
    ]


@pytest.mark.unit
def test_constant_spectrum():
    summary = summarize_ir_spectrum(spectrum(lambda _: 0.9), spectrum_type="mir_emissivity", temperature_k=305)
    assert summary.window_average == pytest.approx(0.9, abs=1e-4)
    assert summary.outside_window_average == pytest.approx(0.9, abs=1e-4)
    assert summary.window_coverage == pytest.approx(1.0)
    assert summary.broadband_coverage < 1.0


@pytest.mark.unit
def test_selective_step_spectrum():
    summary = summarize_ir_spectrum(
        spectrum(lambda w: 0.95 if 8.0 <= w <= 13.0 else 0.1),
        spectrum_type="mir_emissivity", temperature_k=305,
    )
    assert summary.window_average == pytest.approx(0.95, abs=0.01)
    assert summary.outside_window_average == pytest.approx(0.1, abs=0.01)


@pytest.mark.integration
def test_band_summary_endpoint_rejects_solar_spectra(client):
    response = client.get("/api/v1/materials/versions/x/spectra/solar_reflectance/band-summary")
    assert response.status_code == 422