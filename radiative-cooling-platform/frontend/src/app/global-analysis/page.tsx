"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import {
  createGlobalBatch,
  getGlobalCities,
} from "@/lib/api-client";

import type {
  AnalysisResolution,
  GlobalBatchCreate,
  GlobalCity,
} from "@/types/global-batch";

const initialRequest: GlobalBatchCreate = {
  name: "Global climate adaptation analysis",
  city_ids: [],

  year: 2025,
  start_month: 1,
  end_month: 12,

  analysis_resolution: "representative",
  sample_days_per_month: 3,
  daily_stride_days: 1,

  representative_day: null,

  local_start_hour: 12,
  duration_minutes: 120,
  output_interval_minutes: 10,

  minimum_skin_improvement_c: 0.2,

  minimum_air_temperature_c: 30,
  minimum_solar_radiation_w_m2: 300,
  exposure_match_mode: "all",

  person: {
    met: 2.0,
    body_surface_area_m2: 1.8,
    initial_core_temperature_c: 36.8,
    initial_skin_temperature_c: 33.7,
  },

  control_material: {
    name: "Conventional clothing",
    clothing_insulation_clo: 0.5,
    solar_reflectance: 0.3,
    solar_transmittance: 0,
    infrared_emissivity: 0.9,
    projected_solar_area_factor: 0.25,
    absorbed_solar_to_body_fraction: 0.35,
  },

  rc_material: {
    name: "Radiative cooling clothing",
    clothing_insulation_clo: 0.4,
    solar_reflectance: 0.92,
    solar_transmittance: 0,
    infrared_emissivity: 0.95,
    projected_solar_area_factor: 0.25,
    absorbed_solar_to_body_fraction: 0.35,
  },
};

export default function GlobalAnalysisPage() {
  const router = useRouter();

  const [cities, setCities] = useState<GlobalCity[]>([]);
  const [request, setRequest] =
    useState<GlobalBatchCreate>(initialRequest);

  const [loadingCities, setLoadingCities] = useState(true);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadCities() {
      setLoadingCities(true);
      setError("");

      try {
        const response = await getGlobalCities();

        setCities(response);

        setRequest((current) => ({
          ...current,
          city_ids: response.map((city) => city.id),
        }));
      } catch (caughtError) {
        setError(
          caughtError instanceof Error
            ? caughtError.message
            : "Unable to load cities",
        );
      } finally {
        setLoadingCities(false);
      }
    }

    void loadCities();
  }, []);

  function updateAnalysisResolution(
    analysisResolution: AnalysisResolution,
  ) {
    setRequest((current) => ({
      ...current,
      analysis_resolution: analysisResolution,
    }));
  }

  function toggleCity(cityId: string) {
    setRequest((current) => {
      const selected = current.city_ids.includes(cityId);

      return {
        ...current,
        city_ids: selected
          ? current.city_ids.filter((id) => id !== cityId)
          : [...current.city_ids, cityId],
      };
    });
  }

  function selectAllCities() {
    setRequest((current) => ({
      ...current,
      city_ids: cities.map((city) => city.id),
    }));
  }

  function clearSelectedCities() {
    setRequest((current) => ({
      ...current,
      city_ids: [],
    }));
  }

  async function submitBatch() {
    if (request.city_ids.length === 0) {
      setError("Select at least one city.");
      return;
    }

    if (request.start_month > request.end_month) {
      setError(
        "Start month must be less than or equal to end month.",
      );
      return;
    }

    setLoading(true);
    setError("");

    try {
      const batch = await createGlobalBatch(request);

      router.push(`/global-analysis/${batch.id}`);
    } catch (caughtError) {
      setError(
        caughtError instanceof Error
          ? caughtError.message
          : "Unable to create the analysis batch",
      );
    } finally {
      setLoading(false);
    }
  }

  const monthCount =
    request.end_month >= request.start_month
      ? request.end_month - request.start_month + 1
      : 0;

  const approximateSamplesPerCity =
    request.analysis_resolution === "representative"
      ? monthCount * request.sample_days_per_month
      : null;

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl px-6 py-10">
        <header>
          <p className="text-sm font-medium text-cyan-400">
            Stage 4.3 Global Analysis
          </p>

          <h1 className="mt-2 text-3xl font-bold">
            Global Climate Adaptation Analysis
          </h1>

          <p className="mt-3 max-w-3xl text-slate-400">
            Analyze representative days or perform fixed-stride
            daily climate adaptation analysis. Only samples matching
            the configured heat-exposure criteria are included in the
            climate adaptation rate.
          </p>
        </header>

        <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">
            Analysis Settings
          </h2>

          <div className="mt-5 grid gap-5 md:grid-cols-2 lg:grid-cols-4">
            <NumberField
              label="Year"
              value={request.year}
              min={1940}
              max={2100}
              onChange={(year) =>
                setRequest((current) => ({
                  ...current,
                  year,
                }))
              }
            />

            <NumberField
              label="Start Month"
              value={request.start_month}
              min={1}
              max={12}
              onChange={(startMonth) =>
                setRequest((current) => ({
                  ...current,
                  start_month: startMonth,
                }))
              }
            />

            <NumberField
              label="End Month"
              value={request.end_month}
              min={1}
              max={12}
              onChange={(endMonth) =>
                setRequest((current) => ({
                  ...current,
                  end_month: endMonth,
                }))
              }
            />

            <label>
              <span className="mb-2 block text-sm text-slate-300">
                Analysis Resolution
              </span>

              <select
                value={request.analysis_resolution}
                onChange={(event) =>
                  updateAnalysisResolution(
                    event.target.value as AnalysisResolution,
                  )
                }
                className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2"
              >
                <option value="representative">
                  Representative Days
                </option>

                <option value="daily">
                  Daily / Fixed Day Stride
                </option>
              </select>
            </label>

            {request.analysis_resolution === "representative" ? (
              <NumberField
                label="Sample Days per Month"
                value={request.sample_days_per_month}
                min={1}
                max={7}
                onChange={(sampleDaysPerMonth) =>
                  setRequest((current) => ({
                    ...current,
                    sample_days_per_month: sampleDaysPerMonth,
                  }))
                }
              />
            ) : (
              <NumberField
                label="Daily Stride (Days)"
                value={request.daily_stride_days}
                min={1}
                max={7}
                onChange={(dailyStrideDays) =>
                  setRequest((current) => ({
                    ...current,
                    daily_stride_days: dailyStrideDays,
                  }))
                }
              />
            )}

            <NumberField
              label="Local Start Hour"
              value={request.local_start_hour}
              min={0}
              max={23}
              onChange={(localStartHour) =>
                setRequest((current) => ({
                  ...current,
                  local_start_hour: localStartHour,
                }))
              }
            />

            <NumberField
              label="Duration (Minutes)"
              value={request.duration_minutes}
              min={30}
              max={1440}
              step={10}
              onChange={(durationMinutes) =>
                setRequest((current) => ({
                  ...current,
                  duration_minutes: durationMinutes,
                }))
              }
            />

            <NumberField
              label="Output Interval (Minutes)"
              value={request.output_interval_minutes}
              min={1}
              max={60}
              onChange={(outputIntervalMinutes) =>
                setRequest((current) => ({
                  ...current,
                  output_interval_minutes:
                    outputIntervalMinutes,
                }))
              }
            />

            <NumberField
              label="Minimum Average Cooling (°C)"
              value={request.minimum_skin_improvement_c}
              min={-5}
              max={10}
              step={0.1}
              onChange={(minimumSkinImprovementC) =>
                setRequest((current) => ({
                  ...current,
                  minimum_skin_improvement_c:
                    minimumSkinImprovementC,
                }))
              }
            />

            <NumberField
              label="Minimum Air Temperature (°C)"
              value={request.minimum_air_temperature_c ?? 30}
              min={-50}
              max={70}
              step={0.5}
              onChange={(minimumAirTemperatureC) =>
                setRequest((current) => ({
                  ...current,
                  minimum_air_temperature_c:
                    minimumAirTemperatureC,
                }))
              }
            />

            <NumberField
              label="Minimum Solar Radiation (W/m²)"
              value={
                request.minimum_solar_radiation_w_m2 ?? 300
              }
              min={0}
              max={1500}
              step={10}
              onChange={(minimumSolarRadiationWM2) =>
                setRequest((current) => ({
                  ...current,
                  minimum_solar_radiation_w_m2:
                    minimumSolarRadiationWM2,
                }))
              }
            />

            <label>
              <span className="mb-2 block text-sm text-slate-300">
                Exposure Match Mode
              </span>

              <select
                value={request.exposure_match_mode}
                onChange={(event) =>
                  setRequest((current) => ({
                    ...current,
                    exposure_match_mode: event.target.value as
                      | "all"
                      | "any",
                  }))
                }
                className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2"
              >
                <option value="all">
                  Match All Thresholds
                </option>

                <option value="any">
                  Match Any Threshold
                </option>
              </select>
            </label>
          </div>

          <div className="mt-6 rounded-xl border border-cyan-900 bg-cyan-950/30 p-4 text-sm text-cyan-100">
            {request.analysis_resolution === "daily" ? (
              <>
                <p className="font-medium">
                  Daily / fixed-stride analysis
                </p>

                <p className="mt-1 text-cyan-100/80">
                  The system analyzes one day every{" "}
                  <strong>{request.daily_stride_days}</strong>{" "}
                  day(s). A stride of{" "}
                  <strong>1</strong> performs a complete daily
                  analysis for the selected months.
                </p>
              </>
            ) : (
              <>
                <p className="font-medium">
                  Representative-day analysis
                </p>

                <p className="mt-1 text-cyan-100/80">
                  The system analyzes{" "}
                  <strong>
                    {request.sample_days_per_month}
                  </strong>{" "}
                  weighted representative day(s) per month.
                  The current selection produces approximately{" "}
                  <strong>
                    {approximateSamplesPerCity ?? 0}
                  </strong>{" "}
                  samples per city.
                </p>
              </>
            )}
          </div>
        </section>

        <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-6">
          <div className="flex flex-wrap items-center justify-between gap-4">
            <div>
              <h2 className="text-xl font-semibold">
                Cities
              </h2>

              <p className="mt-1 text-sm text-slate-400">
                {request.city_ids.length} of {cities.length} cities
                selected
              </p>
            </div>

            <div className="flex flex-wrap gap-3">
              <button
                type="button"
                disabled={
                  loadingCities
                  || cities.length === 0
                  || request.city_ids.length === cities.length
                }
                onClick={selectAllCities}
                className="rounded-lg border border-slate-700 px-4 py-2 text-sm transition hover:border-slate-500 hover:bg-slate-800 disabled:cursor-not-allowed disabled:opacity-50"
              >
                Select All
              </button>

              <button
                type="button"
                disabled={request.city_ids.length === 0}
                onClick={clearSelectedCities}
                className="rounded-lg border border-slate-700 px-4 py-2 text-sm transition hover:border-slate-500 hover:bg-slate-800 disabled:cursor-not-allowed disabled:opacity-50"
              >
                Clear Selection
              </button>
            </div>
          </div>

          {loadingCities ? (
            <div className="mt-5 rounded-xl border border-slate-800 bg-slate-950 p-6 text-center text-slate-400">
              Loading cities...
            </div>
          ) : cities.length === 0 ? (
            <div className="mt-5 rounded-xl border border-amber-900 bg-amber-950/40 p-6 text-center text-amber-200">
              No cities are currently available.
            </div>
          ) : (
            <div className="mt-5 grid gap-3 md:grid-cols-3 lg:grid-cols-4">
              {cities.map((city) => {
                const selected = request.city_ids.includes(city.id);

                return (
                  <button
                    key={city.id}
                    type="button"
                    aria-pressed={selected}
                    onClick={() => toggleCity(city.id)}
                    className={[
                      "rounded-xl border p-4 text-left transition",
                      selected
                        ? "border-cyan-400 bg-cyan-950 shadow-sm shadow-cyan-950"
                        : "border-slate-700 bg-slate-950 hover:border-slate-500",
                    ].join(" ")}
                  >
                    <div className="flex items-start justify-between gap-3">
                      <div>
                        <p className="font-medium">
                          {city.name}
                        </p>

                        <p className="mt-1 text-sm text-slate-400">
                          {city.country}
                        </p>
                      </div>

                      <span
                        className={[
                          "mt-1 inline-flex h-5 w-5 items-center justify-center rounded-full border text-xs",
                          selected
                            ? "border-cyan-300 bg-cyan-400 text-slate-950"
                            : "border-slate-600 text-transparent",
                        ].join(" ")}
                        aria-hidden="true"
                      >
                        ✓
                      </span>
                    </div>

                    <p className="mt-2 text-xs text-slate-500">
                      {city.climate_type}
                    </p>
                  </button>
                );
              })}
            </div>
          )}
        </section>

        {error && (
          <div
            role="alert"
            className="mt-6 rounded-xl border border-red-900 bg-red-950 p-4 text-red-300"
          >
            {error}
          </div>
        )}

        <div className="mt-8 flex flex-wrap items-center gap-4">
          <button
            type="button"
            disabled={
              loading
              || loadingCities
              || request.city_ids.length === 0
              || request.start_month > request.end_month
            }
            onClick={submitBatch}
            className="rounded-lg bg-cyan-400 px-7 py-3 font-semibold text-slate-950 transition hover:bg-cyan-300 disabled:cursor-not-allowed disabled:opacity-50"
          >
            {loading
              ? "Creating Analysis Batch..."
              : `Analyze ${request.city_ids.length} ${
                  request.city_ids.length === 1
                    ? "City"
                    : "Cities"
                }`}
          </button>

          <p className="text-sm text-slate-400">
            {request.analysis_resolution === "daily"
              ? `Daily analysis with a ${request.daily_stride_days}-day stride`
              : `${request.sample_days_per_month} representative sample day(s) per month`}
          </p>
        </div>
      </div>
    </main>
  );
}

function NumberField({
  label,
  value,
  min,
  max,
  step = 1,
  disabled = false,
  onChange,
}: {
  label: string;
  value: number;
  min?: number;
  max?: number;
  step?: number;
  disabled?: boolean;
  onChange: (value: number) => void;
}) {
  function handleChange(rawValue: string) {
    if (rawValue === "") {
      return;
    }

    const parsedValue = Number(rawValue);

    if (!Number.isFinite(parsedValue)) {
      return;
    }

    onChange(parsedValue);
  }

  return (
    <label>
      <span className="mb-2 block text-sm text-slate-300">
        {label}
      </span>

      <input
        type="number"
        value={value}
        min={min}
        max={max}
        step={step}
        disabled={disabled}
        onChange={(event) =>
          handleChange(event.target.value)
        }
        className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 disabled:cursor-not-allowed disabled:opacity-50"
      />
    </label>
  );
}