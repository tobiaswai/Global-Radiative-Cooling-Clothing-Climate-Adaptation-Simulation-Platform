"use client";

import {
  FormEvent,
  useEffect,
  useState,
} from "react";

import { HeatFluxChart } from "@/components/charts/heat-flux-chart";
import { TemperatureChart } from "@/components/charts/temperature-chart";
import { WeatherChart } from "@/components/charts/weather-chart";
import {
  getCities,
  runWeatherSimulation,
} from "@/lib/api-client";
import type {
  City,
  WeatherSimulationRequest,
  WeatherSimulationResponse,
} from "@/types/simulation";


const initialRequest: WeatherSimulationRequest = {
  city_id: "dubai",
  start_time_local: "2025-07-15T10:00",
  duration_minutes: 120,
  output_interval_minutes: 1,

  person: {
    met: 2.6,
    body_surface_area_m2: 1.8,
    initial_core_temperature_c: 36.8,
    initial_skin_temperature_c: 33.7,
  },

  control_material: {
    name: "普通服裝",
    clothing_insulation_clo: 0.5,
    solar_reflectance: 0.4,
    solar_transmittance: 0,
    infrared_emissivity: 0.8,
    projected_solar_area_factor: 0.25,
    absorbed_solar_to_body_fraction: 0.35,
  },

  rc_material: {
    name: "輻射製冷服裝",
    clothing_insulation_clo: 0.4,
    solar_reflectance: 0.92,
    solar_transmittance: 0,
    infrared_emissivity: 0.95,
    projected_solar_area_factor: 0.25,
    absorbed_solar_to_body_fraction: 0.35,
  },
};


export default function WeatherSimulationPage() {
  const [cities, setCities] =
    useState<City[]>([]);

  const [request, setRequest] =
    useState(initialRequest);

  const [result, setResult] =
    useState<WeatherSimulationResponse | null>(
      null,
    );

  const [loading, setLoading] =
    useState(false);

  const [error, setError] =
    useState("");

  useEffect(() => {
    getCities()
      .then(setCities)
      .catch((caughtError) => {
        setError(
          caughtError instanceof Error
            ? caughtError.message
            : "無法載入城市",
        );
      });
  }, []);

  async function handleSubmit(
    event: FormEvent,
  ) {
    event.preventDefault();
    setLoading(true);
    setError("");

    try {
      const response =
        await runWeatherSimulation(request);

      setResult(response);
    } catch (caughtError) {
      setError(
        caughtError instanceof Error
          ? caughtError.message
          : "模擬失敗",
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl px-6 py-10">
        <header>
          <p className="text-sm font-medium text-cyan-400">
            Historical Weather Simulation
          </p>

          <h1 className="mt-2 text-3xl font-bold">
            歷史氣象驅動模擬
          </h1>

          <p className="mt-3 text-slate-400">
            使用 ERA5 歷史逐小時氣象資料，
            模擬普通服裝與輻射製冷服裝的動態熱反應。
          </p>
        </header>

        <form
          onSubmit={handleSubmit}
          className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-6"
        >
          <div className="grid gap-5 md:grid-cols-4">
            <label>
              <span className="mb-2 block text-sm text-slate-300">
                城市
              </span>

              <select
                value={request.city_id}
                onChange={(event) =>
                  setRequest({
                    ...request,
                    city_id: event.target.value,
                  })
                }
                className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2"
              >
                {cities.map((city) => (
                  <option
                    key={city.id}
                    value={city.id}
                  >
                    {city.name}－
                    {city.climate_type}
                  </option>
                ))}
              </select>
            </label>

            <label>
              <span className="mb-2 block text-sm text-slate-300">
                當地開始時間
              </span>

              <input
                type="datetime-local"
                value={request.start_time_local}
                onChange={(event) =>
                  setRequest({
                    ...request,
                    start_time_local:
                      event.target.value,
                  })
                }
                className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2"
              />
            </label>

            <label>
              <span className="mb-2 block text-sm text-slate-300">
                模擬時長（分鐘）
              </span>

              <input
                type="number"
                min={1}
                max={1440}
                value={request.duration_minutes}
                onChange={(event) =>
                  setRequest({
                    ...request,
                    duration_minutes: Number(
                      event.target.value,
                    ),
                  })
                }
                className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2"
              />
            </label>

            <label>
              <span className="mb-2 block text-sm text-slate-300">
                活動強度（MET）
              </span>

              <input
                type="number"
                min={0.7}
                max={10}
                step={0.1}
                value={request.person.met}
                onChange={(event) =>
                  setRequest({
                    ...request,
                    person: {
                      ...request.person,
                      met: Number(
                        event.target.value,
                      ),
                    },
                  })
                }
                className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2"
              />
            </label>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="mt-6 rounded-xl bg-cyan-400 px-7 py-3 font-semibold text-slate-950 disabled:opacity-50"
          >
            {loading
              ? "正在下載氣象資料並計算……"
              : "開始歷史氣象模擬"}
          </button>

          {error && (
            <div className="mt-5 rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">
              {error}
            </div>
          )}
        </form>

        {result && (
          <section className="mt-10 space-y-8">
            <div className="grid gap-4 md:grid-cols-3">
              <SummaryCard
                label="最終皮膚溫度改善"
                value={
                  result.summary
                    .final_skin_temperature_improvement_c
                }
              />

              <SummaryCard
                label="平均皮膚溫度改善"
                value={
                  result.summary
                    .average_skin_temperature_improvement_c
                }
              />

              <SummaryCard
                label="核心溫度改善"
                value={
                  result.summary
                    .final_core_temperature_improvement_c
                }
              />
            </div>

            <div className="rounded-xl border border-amber-800 bg-amber-950/50 p-4 text-amber-200">
              <p>{result.warning}</p>
              <p className="mt-2 text-sm">
                {result.environment_model_note}
              </p>
            </div>

            <WeatherChart
              weather={result.weather}
            />

            <TemperatureChart result={result} />

            <HeatFluxChart result={result} />
          </section>
        )}
      </div>
    </main>
  );
}


function SummaryCard({
  label,
  value,
}: {
  label: string;
  value: number;
}) {
  return (
    <article className="rounded-2xl border border-slate-800 bg-slate-900 p-5">
      <p className="text-sm text-slate-400">
        {label}
      </p>

      <p className="mt-2 text-3xl font-bold text-cyan-300">
        {value.toFixed(3)}
        <span className="ml-1 text-base font-normal">
          °C
        </span>
      </p>
    </article>
  );
}