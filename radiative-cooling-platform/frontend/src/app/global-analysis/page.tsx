"use client";

import {
  useEffect,
  useMemo,
  useState,
} from "react";

import { useRouter } from "next/navigation";

import {
  createGlobalBatch,
  estimateGlobalBatch,
  getGlobalCities,
} from "@/lib/api-client";

import type {
  AnalysisResolution,
  ExecutionProfile,
  ExposureMatchMode,
  GlobalBatchCreate,
  GlobalBatchEstimate,
  GlobalCity,
} from "@/types/global-batch";

type EstimateState = {
  requestKey: string;
  status: "loading" | "success" | "error";
  data: GlobalBatchEstimate | null;
};

const initialRequest: GlobalBatchCreate = {
  name: "Global climate adaptation analysis",
  city_ids: [],

  year: 2023,
  start_month: 1,
  end_month: 12,

  analysis_resolution: "representative",

  sample_days_per_month: 3,
  daily_stride_days: 1,

  execution_profile: "auto",
  resume_from_checkpoint: true,

  enable_heatwave_analysis: true,
  heatwave_temperature_threshold_c: 35,
  heatwave_minimum_consecutive_days: 3,

  representative_day: null,

  local_start_hour: 12,
  duration_minutes: 120,
  output_interval_minutes: 10,

  minimum_skin_improvement_c: 0.2,

  minimum_air_temperature_c: 30,
  minimum_solar_radiation_w_m2: 300,

  exposure_match_mode: "all",

  person: {
    met: 2,
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

  const [
    cities,
    setCities,
  ] = useState<GlobalCity[]>([]);

  const [
    request,
    setRequest,
  ] = useState<GlobalBatchCreate>(
    initialRequest,
  );

  const [
    loadingCities,
    setLoadingCities,
  ] = useState(true);

  const [
    estimateState,
    setEstimateState,
  ] = useState<EstimateState | null>(
    null,
  );

  const [
    submitting,
    setSubmitting,
  ] = useState(false);

  const [
    error,
    setError,
  ] = useState("");

  useEffect(() => {
    let disposed = false;

    async function loadCities() {
      setLoadingCities(true);
      setError("");

      try {
        const response =
          await getGlobalCities();

        if (disposed) {
          return;
        }

        setCities(response);

        setRequest((current) => ({
          ...current,
          city_ids: response.map(
            (city) => city.id,
          ),
        }));
      } catch (caughtError) {
        if (!disposed) {
          setError(
            getErrorMessage(
              caughtError,
              "Unable to load supported cities.",
            ),
          );
        }
      } finally {
        if (!disposed) {
          setLoadingCities(false);
        }
      }
    }

    void loadCities();

    return () => {
      disposed = true;
    };
  }, []);

  const canEstimate =
    request.city_ids.length > 0 &&
    request.start_month <= request.end_month;

  const estimateRequestKey =
    JSON.stringify(request);

  const estimate =
    canEstimate &&
    estimateState?.requestKey ===
      estimateRequestKey &&
    estimateState.status === "success"
      ? estimateState.data
      : null;

  const estimating =
    canEstimate &&
    estimateState?.requestKey ===
      estimateRequestKey &&
    estimateState.status === "loading";

  useEffect(() => {
    if (!canEstimate) {
      return;
    }

    let disposed = false;

    const timer = window.setTimeout(
      () => {
        if (disposed) {
          return;
        }

        setEstimateState({
          requestKey: estimateRequestKey,
          status: "loading",
          data: null,
        });

        void estimateGlobalBatch(request)
          .then((response) => {
            if (disposed) {
              return;
            }

            setEstimateState({
              requestKey: estimateRequestKey,
              status: "success",
              data: response,
            });
          })
          .catch(() => {
            if (disposed) {
              return;
            }

            setEstimateState({
              requestKey: estimateRequestKey,
              status: "error",
              data: null,
            });
          });
      },
      350,
    );

    return () => {
      disposed = true;
      window.clearTimeout(timer);
    };
  }, [
    canEstimate,
    estimateRequestKey,
    request,
  ]);

  const selectedCityCount =
    request.city_ids.length;

  const heatwaveAvailable =
    request.enable_heatwave_analysis &&
    request.analysis_resolution === "daily" &&
    request.daily_stride_days === 1;

  const cityGroups = useMemo(() => {
    const groups = new Map<
      string,
      GlobalCity[]
    >();

    for (const city of cities) {
      const existing =
        groups.get(city.country) ?? [];

      existing.push(city);
      groups.set(city.country, existing);
    }

    return Array.from(groups.entries())
      .sort(([first], [second]) =>
        first.localeCompare(second),
      )
      .map(([country, groupedCities]) => ({
        country,
        cities: groupedCities.sort(
          (first, second) =>
            first.name.localeCompare(
              second.name,
            ),
        ),
      }));
  }, [cities]);

  function updateAnalysisResolution(
    value: AnalysisResolution,
  ) {
    setRequest((current) => ({
      ...current,
      analysis_resolution: value,
    }));
  }

  function toggleCity(cityId: string) {
    setRequest((current) => {
      const selected =
        current.city_ids.includes(cityId);

      return {
        ...current,
        city_ids: selected
          ? current.city_ids.filter(
              (id) => id !== cityId,
            )
          : [
              ...current.city_ids,
              cityId,
            ],
      };
    });
  }

  function selectAllCities() {
    setRequest((current) => ({
      ...current,
      city_ids: cities.map(
        (city) => city.id,
      ),
    }));
  }

  function clearSelectedCities() {
    setRequest((current) => ({
      ...current,
      city_ids: [],
    }));
  }

  async function submitBatch() {
    const validationError =
      validateRequest(request);

    if (validationError) {
      setError(validationError);
      return;
    }

    try {
      setSubmitting(true);
      setError("");

      const batch =
        await createGlobalBatch(request);

      router.push(
        `/global-analysis/${batch.id}`,
      );
    } catch (caughtError) {
      setError(
        getErrorMessage(
          caughtError,
          "Unable to create the analysis batch.",
        ),
      );
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl px-6 py-10">
        <header>
          <p className="text-sm font-medium text-cyan-400">
            Stage 4.4 Global Analysis
          </p>

          <h1 className="mt-2 text-3xl font-bold">
            Global Climate Adaptation Analysis
          </h1>

          <p className="mt-3 max-w-4xl leading-7 text-slate-400">
            Run representative-day or daily
            radiative-cooling analyses across
            multiple cities. Long-running jobs
            support monthly checkpoints,
            cooperative cancellation, queue
            selection, percentile analytics, and
            heatwave event analysis.
          </p>
        </header>

        {error && (
          <div className="mt-6 rounded-xl border border-red-900 bg-red-950 p-4 text-red-300">
            {error}
          </div>
        )}

        <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">
            General Settings
          </h2>

          <div className="mt-5 grid gap-5 md:grid-cols-2 lg:grid-cols-4">
            <TextField
              label="Batch Name"
              value={request.name}
              onChange={(name) =>
                setRequest((current) => ({
                  ...current,
                  name,
                }))
              }
            />

            <NumberField
              label="Historical Weather Year"
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

            <SelectField
              label="Analysis Resolution"
              value={
                request.analysis_resolution
              }
              options={[
                {
                  value: "representative",
                  label:
                    "Representative Days",
                },
                {
                  value: "daily",
                  label:
                    "Daily / Fixed Day Stride",
                },
              ]}
              onChange={(value) =>
                updateAnalysisResolution(
                  value as AnalysisResolution,
                )
              }
            />

            {request.analysis_resolution ===
            "representative" ? (
              <NumberField
                label="Sample Days per Month"
                value={
                  request.sample_days_per_month
                }
                min={1}
                max={7}
                onChange={(
                  sampleDaysPerMonth,
                ) =>
                  setRequest((current) => ({
                    ...current,
                    sample_days_per_month:
                      sampleDaysPerMonth,
                  }))
                }
              />
            ) : (
              <NumberField
                label="Daily Stride"
                value={
                  request.daily_stride_days
                }
                min={1}
                max={7}
                suffix="days"
                onChange={(dailyStrideDays) =>
                  setRequest((current) => ({
                    ...current,
                    daily_stride_days:
                      dailyStrideDays,
                  }))
                }
              />
            )}

            <SelectField
              label="Execution Profile"
              value={
                request.execution_profile
              }
              options={[
                {
                  value: "auto",
                  label: "Automatic",
                },
                {
                  value: "standard",
                  label: "Standard Queue",
                },
                {
                  value: "large",
                  label: "Large Job Queue",
                },
              ]}
              onChange={(value) =>
                setRequest((current) => ({
                  ...current,
                  execution_profile:
                    value as ExecutionProfile,
                }))
              }
            />

            <NumberField
              label="Local Start Hour"
              value={
                request.local_start_hour
              }
              min={0}
              max={23}
              onChange={(localStartHour) =>
                setRequest((current) => ({
                  ...current,
                  local_start_hour:
                    localStartHour,
                }))
              }
            />

            <NumberField
              label="Duration"
              value={
                request.duration_minutes
              }
              min={30}
              max={1440}
              step={10}
              suffix="minutes"
              onChange={(durationMinutes) =>
                setRequest((current) => ({
                  ...current,
                  duration_minutes:
                    durationMinutes,
                }))
              }
            />

            <NumberField
              label="Output Interval"
              value={
                request
                  .output_interval_minutes
              }
              min={1}
              max={60}
              suffix="minutes"
              onChange={(
                outputIntervalMinutes,
              ) =>
                setRequest((current) => ({
                  ...current,
                  output_interval_minutes:
                    outputIntervalMinutes,
                }))
              }
            />
          </div>

          <div className="mt-6">
            <CheckboxField
              label="Resume failed city tasks from monthly checkpoints"
              description="Previously completed months will not be recalculated when a failed city is retried."
              checked={
                request.resume_from_checkpoint
              }
              onChange={(checked) =>
                setRequest((current) => ({
                  ...current,
                  resume_from_checkpoint:
                    checked,
                }))
              }
            />
          </div>
        </section>

        <section className="mt-6 rounded-2xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">
            Exposure and Cooling Criteria
          </h2>

          <p className="mt-2 text-sm leading-6 text-slate-400">
            Samples that do not satisfy the
            exposure criteria are excluded from
            the climate adaptation rate.
          </p>

          <div className="mt-5 grid gap-5 md:grid-cols-2 lg:grid-cols-4">
            <NumberField
              label="Minimum Average Cooling"
              value={
                request
                  .minimum_skin_improvement_c
              }
              min={-5}
              max={10}
              step={0.1}
              suffix="°C"
              onChange={(
                minimumSkinImprovementC,
              ) =>
                setRequest((current) => ({
                  ...current,
                  minimum_skin_improvement_c:
                    minimumSkinImprovementC,
                }))
              }
            />

            <NumberField
              label="Minimum Air Temperature"
              value={
                request
                  .minimum_air_temperature_c ??
                30
              }
              min={-50}
              max={70}
              step={0.5}
              suffix="°C"
              onChange={(
                minimumAirTemperatureC,
              ) =>
                setRequest((current) => ({
                  ...current,
                  minimum_air_temperature_c:
                    minimumAirTemperatureC,
                }))
              }
            />

            <NumberField
              label="Minimum Solar Radiation"
              value={
                request
                  .minimum_solar_radiation_w_m2 ??
                300
              }
              min={0}
              max={1500}
              step={10}
              suffix="W/m²"
              onChange={(
                minimumSolarRadiation,
              ) =>
                setRequest((current) => ({
                  ...current,
                  minimum_solar_radiation_w_m2:
                    minimumSolarRadiation,
                }))
              }
            />

            <SelectField
              label="Exposure Match Mode"
              value={
                request.exposure_match_mode
              }
              options={[
                {
                  value: "all",
                  label:
                    "All Criteria Must Match",
                },
                {
                  value: "any",
                  label:
                    "Any Criterion May Match",
                },
              ]}
              onChange={(value) =>
                setRequest((current) => ({
                  ...current,
                  exposure_match_mode:
                    value as ExposureMatchMode,
                }))
              }
            />
          </div>
        </section>

        <section className="mt-6 rounded-2xl border border-slate-800 bg-slate-900 p-6">
          <div className="flex flex-wrap items-start justify-between gap-4">
            <div>
              <h2 className="text-xl font-semibold">
                Heatwave Analysis
              </h2>

              <p className="mt-2 max-w-3xl text-sm leading-6 text-slate-400">
                Heatwave event detection requires
                daily resolution with a one-day
                stride. The temperature threshold
                is evaluated against each sampled
                day&apos;s maximum air temperature.
              </p>
            </div>

            <CheckboxField
              label="Enable heatwave analysis"
              checked={
                request.enable_heatwave_analysis
              }
              onChange={(checked) =>
                setRequest((current) => ({
                  ...current,
                  enable_heatwave_analysis:
                    checked,
                }))
              }
            />
          </div>

          <div className="mt-5 grid gap-5 md:grid-cols-2">
            <NumberField
              label="Heatwave Temperature Threshold"
              value={
                request
                  .heatwave_temperature_threshold_c
              }
              min={-20}
              max={70}
              step={0.5}
              suffix="°C"
              disabled={
                !request.enable_heatwave_analysis
              }
              onChange={(threshold) =>
                setRequest((current) => ({
                  ...current,
                  heatwave_temperature_threshold_c:
                    threshold,
                }))
              }
            />

            <NumberField
              label="Minimum Consecutive Days"
              value={
                request
                  .heatwave_minimum_consecutive_days
              }
              min={2}
              max={30}
              suffix="days"
              disabled={
                !request.enable_heatwave_analysis
              }
              onChange={(minimumDays) =>
                setRequest((current) => ({
                  ...current,
                  heatwave_minimum_consecutive_days:
                    minimumDays,
                }))
              }
            />
          </div>

          {request.enable_heatwave_analysis &&
            !heatwaveAvailable && (
              <div className="mt-5 rounded-lg border border-amber-800 bg-amber-950 p-4 text-sm text-amber-300">
                Heatwave event analysis will be
                unavailable unless Analysis
                Resolution is Daily and Daily
                Stride is 1.
              </div>
            )}
        </section>

        <section className="mt-6 rounded-2xl border border-slate-800 bg-slate-900 p-6">
          <div className="flex flex-wrap items-center justify-between gap-4">
            <div>
              <h2 className="text-xl font-semibold">
                Cities
              </h2>

              <p className="mt-1 text-sm text-slate-400">
                {selectedCityCount} of{" "}
                {cities.length} cities selected
              </p>
            </div>

            <div className="flex gap-3">
              <button
                type="button"
                onClick={selectAllCities}
                disabled={
                  loadingCities ||
                  cities.length === 0
                }
                className="rounded-lg border border-cyan-800 px-4 py-2 text-sm text-cyan-300 hover:bg-cyan-950 disabled:cursor-not-allowed disabled:opacity-50"
              >
                Select All
              </button>

              <button
                type="button"
                onClick={
                  clearSelectedCities
                }
                disabled={
                  selectedCityCount === 0
                }
                className="rounded-lg border border-slate-700 px-4 py-2 text-sm text-slate-300 hover:bg-slate-800 disabled:cursor-not-allowed disabled:opacity-50"
              >
                Clear
              </button>
            </div>
          </div>

          {loadingCities ? (
            <p className="mt-6 text-slate-400">
              Loading supported cities...
            </p>
          ) : (
            <div className="mt-6 space-y-6">
              {cityGroups.map((group) => (
                <div key={group.country}>
                  <h3 className="mb-3 text-sm font-semibold uppercase tracking-wide text-slate-500">
                    {group.country}
                  </h3>

                  <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
                    {group.cities.map(
                      (city) => {
                        const selected =
                          request.city_ids.includes(
                            city.id,
                          );

                        return (
                          <button
                            key={city.id}
                            type="button"
                            aria-pressed={
                              selected
                            }
                            onClick={() =>
                              toggleCity(
                                city.id,
                              )
                            }
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

                                <p className="mt-1 text-xs text-slate-400">
                                  {
                                    city.climate_type
                                  }
                                </p>
                              </div>

                              <span
                                className={[
                                  "mt-1 h-4 w-4 rounded-full border",
                                  selected
                                    ? "border-cyan-300 bg-cyan-400"
                                    : "border-slate-600",
                                ].join(" ")}
                              />
                            </div>

                            <p className="mt-3 text-xs text-slate-500">
                              {city.latitude.toFixed(
                                2,
                              )}
                              ,{" "}
                              {city.longitude.toFixed(
                                2,
                              )}
                            </p>
                          </button>
                        );
                      },
                    )}
                  </div>
                </div>
              ))}
            </div>
          )}
        </section>

        <section className="mt-6 rounded-2xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">
            Workload Estimate
          </h2>
            {!canEstimate ? (
              <p className="mt-4 text-slate-400">
                {request.city_ids.length === 0
                  ? "Select at least one city to calculate the workload."
                  : "Start month must be less than or equal to end month."}
              </p>
            ) : estimating ? (
              <p className="mt-4 text-slate-400">
                Calculating workload...
              </p>
            ) : estimate ? (
              <div className="mt-5 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
                <EstimateMetric
                  label="Cities"
                  value={String(estimate.city_count)}
                />

                <EstimateMetric
                  label="Samples per City"
                  value={String(
                    estimate.samples_per_city,
                  )}
                />

                <EstimateMetric
                  label="Total Samples"
                  value={String(
                    estimate.total_samples,
                  )}
                />

                <EstimateMetric
                  label="Thermal Simulations"
                  value={String(
                    estimate.thermal_simulation_count,
                  )}
                />

                <EstimateMetric
                  label="Weather Requests"
                  value={String(
                    estimate.estimated_weather_requests,
                  )}
                />

                <EstimateMetric
                  label="Resolved Profile"
                  value={formatLabel(
                    estimate.resolved_execution_profile,
                  )}
                />

                <EstimateMetric
                  label="Celery Queue"
                  value={estimate.resolved_queue}
                />

                <EstimateMetric
                  label="Monthly Checkpoints"
                  value={
                    `${estimate.checkpoint_count_per_city}` +
                    " per city"
                  }
                />

                <EstimateMetric
                  label="Heatwave Analysis"
                  value={
                    estimate.heatwave_analysis_available
                      ? "Available"
                      : "Unavailable"
                  }
                />
              </div>
            ) : estimateState?.status === "error" ? (
              <p className="mt-4 text-amber-300">
                Unable to calculate the workload estimate.
              </p>
            ) : (
              <p className="mt-4 text-slate-400">
                Preparing workload estimate...
              </p>
            )}
        </section>

        <div className="mt-8 flex flex-wrap items-center justify-between gap-4">
          <p className="text-sm text-slate-400">
            Selected cities:{" "}
            <strong className="text-white">
              {selectedCityCount}
            </strong>
          </p>

          <button
            type="button"
            onClick={submitBatch}
            disabled={
              submitting ||
              loadingCities ||
              selectedCityCount === 0
            }
            className="rounded-lg bg-cyan-400 px-6 py-3 font-semibold text-slate-950 transition hover:bg-cyan-300 disabled:cursor-not-allowed disabled:opacity-50"
          >
            {submitting
              ? "Submitting Analysis..."
              : "Start Global Analysis"}
          </button>
        </div>
      </div>
    </main>
  );
}


function validateRequest(
  request: GlobalBatchCreate,
): string | null {
  if (!request.name.trim()) {
    return "Enter a batch name.";
  }

  if (request.city_ids.length === 0) {
    return "Select at least one city.";
  }

  if (
    request.start_month >
    request.end_month
  ) {
    return (
      "Start month must be less than " +
      "or equal to end month."
    );
  }

  if (
    request.output_interval_minutes >
    request.duration_minutes
  ) {
    return (
      "Output interval cannot exceed " +
      "the simulation duration."
    );
  }

  return null;
}


function TextField({
  label,
  value,
  onChange,
}: {
  label: string;
  value: string;
  onChange: (value: string) => void;
}) {
  return (
    <label>
      <span className="mb-2 block text-sm text-slate-300">
        {label}
      </span>

      <input
        type="text"
        value={value}
        onChange={(event) =>
          onChange(event.target.value)
        }
        className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 outline-none focus:border-cyan-500"
      />
    </label>
  );
}


function NumberField({
  label,
  value,
  min,
  max,
  step = 1,
  suffix,
  disabled = false,
  onChange,
}: {
  label: string;
  value: number;
  min?: number;
  max?: number;
  step?: number;
  suffix?: string;
  disabled?: boolean;
  onChange: (value: number) => void;
}) {
  return (
    <label>
      <span className="mb-2 block text-sm text-slate-300">
        {label}
      </span>

      <div className="relative">
        <input
          type="number"
          value={value}
          min={min}
          max={max}
          step={step}
          disabled={disabled}
          onChange={(event) => {
            const parsed = Number(
              event.target.value,
            );

            if (Number.isFinite(parsed)) {
              onChange(parsed);
            }
          }}
          className={[
            "w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 outline-none focus:border-cyan-500",
            suffix ? "pr-20" : "",
            disabled
              ? "cursor-not-allowed opacity-50"
              : "",
          ].join(" ")}
        />

        {suffix && (
          <span className="pointer-events-none absolute inset-y-0 right-3 flex items-center text-xs text-slate-500">
            {suffix}
          </span>
        )}
      </div>
    </label>
  );
}


function SelectField({
  label,
  value,
  options,
  onChange,
}: {
  label: string;
  value: string;
  options: Array<{
    value: string;
    label: string;
  }>;
  onChange: (value: string) => void;
}) {
  return (
    <label>
      <span className="mb-2 block text-sm text-slate-300">
        {label}
      </span>

      <select
        value={value}
        onChange={(event) =>
          onChange(event.target.value)
        }
        className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 outline-none focus:border-cyan-500"
      >
        {options.map((option) => (
          <option
            key={option.value}
            value={option.value}
          >
            {option.label}
          </option>
        ))}
      </select>
    </label>
  );
}


function CheckboxField({
  label,
  description,
  checked,
  onChange,
}: {
  label: string;
  description?: string;
  checked: boolean;
  onChange: (checked: boolean) => void;
}) {
  return (
    <label className="flex cursor-pointer items-start gap-3">
      <input
        type="checkbox"
        checked={checked}
        onChange={(event) =>
          onChange(event.target.checked)
        }
        className="mt-1 h-4 w-4 accent-cyan-400"
      />

      <span>
        <span className="block text-sm text-slate-200">
          {label}
        </span>

        {description && (
          <span className="mt-1 block max-w-xl text-xs leading-5 text-slate-500">
            {description}
          </span>
        )}
      </span>
    </label>
  );
}


function EstimateMetric({
  label,
  value,
}: {
  label: string;
  value: string;
}) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-950 p-4">
      <p className="text-xs uppercase tracking-wide text-slate-500">
        {label}
      </p>

      <p className="mt-2 break-words font-semibold text-cyan-300">
        {value}
      </p>
    </div>
  );
}


function formatLabel(value: string): string {
  return value
    .split("_")
    .map(
      (word) =>
        word.charAt(0).toUpperCase() +
        word.slice(1),
    )
    .join(" ");
}


function getErrorMessage(
  error: unknown,
  fallback: string,
): string {
  return error instanceof Error
    ? error.message
    : fallback;
}