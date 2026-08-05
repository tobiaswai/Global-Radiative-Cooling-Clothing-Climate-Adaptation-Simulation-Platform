"use client";

import {
  type FormEvent,
  useEffect,
  useState,
} from "react";
import { useRouter } from "next/navigation";

import {
  createSimulationJob,
  getCities,
} from "@/lib/api-client";
import type {
  City,
  WeatherSimulationRequest,
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
  const router = useRouter();

  const [cities, setCities] =
    useState<City[]>([]);

  const [request, setRequest] =
    useState<WeatherSimulationRequest>(
      initialRequest,
    );

  const [loadingCities, setLoadingCities] =
    useState(true);

  const [submitting, setSubmitting] =
    useState(false);

  const [error, setError] =
    useState("");


  useEffect(() => {
    let cancelled = false;

    async function loadCities() {
      setLoadingCities(true);
      setError("");

      try {
        const cityList = await getCities();

        if (!cancelled) {
          setCities(cityList);
        }
      } catch (caughtError) {
        if (!cancelled) {
          setError(
            caughtError instanceof Error
              ? caughtError.message
              : "無法載入城市列表",
          );
        }
      } finally {
        if (!cancelled) {
          setLoadingCities(false);
        }
      }
    }

    void loadCities();

    return () => {
      cancelled = true;
    };
  }, []);


  async function handleSubmit(
    event: FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault();

    if (submitting) {
      return;
    }

    setSubmitting(true);
    setError("");

    try {
      const job =
        await createSimulationJob(request);

      router.push(
        `/simulations/${job.id}`,
      );
    } catch (caughtError) {
      setError(
        caughtError instanceof Error
          ? caughtError.message
          : "建立模擬任務失敗",
      );

      setSubmitting(false);
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

          <p className="mt-3 max-w-3xl text-slate-400">
            使用 ERA5 歷史逐小時氣象資料，
            建立普通服裝與輻射製冷服裝的異步動態模擬任務。
          </p>
        </header>

        <form
          onSubmit={handleSubmit}
          className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-6"
        >
          <div className="grid gap-5 md:grid-cols-2 lg:grid-cols-4">
            <label className="block">
              <span className="mb-2 block text-sm text-slate-300">
                城市
              </span>

              <select
                value={request.city_id}
                disabled={
                  loadingCities
                  || submitting
                }
                onChange={(event) => {
                  setRequest((current) => ({
                    ...current,
                    city_id: event.target.value,
                  }));
                }}
                className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 outline-none focus:border-cyan-500 disabled:cursor-not-allowed disabled:opacity-50"
              >
                {loadingCities && (
                  <option value="">
                    正在載入城市……
                  </option>
                )}

                {!loadingCities
                  && cities.length === 0 && (
                    <option value="">
                      沒有可用城市
                    </option>
                  )}

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

            <label className="block">
              <span className="mb-2 block text-sm text-slate-300">
                當地開始時間
              </span>

              <input
                type="datetime-local"
                required
                value={
                  request.start_time_local
                }
                disabled={submitting}
                onChange={(event) => {
                  setRequest((current) => ({
                    ...current,
                    start_time_local:
                      event.target.value,
                  }));
                }}
                className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 outline-none focus:border-cyan-500 disabled:cursor-not-allowed disabled:opacity-50"
              />
            </label>

            <label className="block">
              <span className="mb-2 block text-sm text-slate-300">
                模擬時長（分鐘）
              </span>

              <input
                type="number"
                required
                min={1}
                max={1440}
                step={1}
                value={
                  request.duration_minutes
                }
                disabled={submitting}
                onChange={(event) => {
                  setRequest((current) => ({
                    ...current,
                    duration_minutes: Number(
                      event.target.value,
                    ),
                  }));
                }}
                className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 outline-none focus:border-cyan-500 disabled:cursor-not-allowed disabled:opacity-50"
              />
            </label>

            <label className="block">
              <span className="mb-2 block text-sm text-slate-300">
                活動強度（MET）
              </span>

              <input
                type="number"
                required
                min={0.7}
                max={10}
                step={0.1}
                value={request.person.met}
                disabled={submitting}
                onChange={(event) => {
                  const met = Number(
                    event.target.value,
                  );

                  setRequest((current) => ({
                    ...current,
                    person: {
                      ...current.person,
                      met,
                    },
                  }));
                }}
                className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 outline-none focus:border-cyan-500 disabled:cursor-not-allowed disabled:opacity-50"
              />
            </label>
          </div>

          <section className="mt-8 rounded-xl border border-slate-800 bg-slate-950/50 p-5">
            <h2 className="text-lg font-semibold">
              模擬配置摘要
            </h2>

            <dl className="mt-4 grid gap-4 text-sm sm:grid-cols-2 lg:grid-cols-4">
              <div>
                <dt className="text-slate-500">
                  輸出間隔
                </dt>
                <dd className="mt-1 text-slate-200">
                  {
                    request
                      .output_interval_minutes
                  }{" "}
                  分鐘
                </dd>
              </div>

              <div>
                <dt className="text-slate-500">
                  普通服裝
                </dt>
                <dd className="mt-1 text-slate-200">
                  {
                    request.control_material
                      .clothing_insulation_clo
                  }{" "}
                  clo
                </dd>
              </div>

              <div>
                <dt className="text-slate-500">
                  普通服裝太陽反射率
                </dt>
                <dd className="mt-1 text-slate-200">
                  {
                    request.control_material
                      .solar_reflectance
                  }
                </dd>
              </div>

              <div>
                <dt className="text-slate-500">
                  RC 服裝太陽反射率
                </dt>
                <dd className="mt-1 text-slate-200">
                  {
                    request.rc_material
                      .solar_reflectance
                  }
                </dd>
              </div>
            </dl>
          </section>

          <button
            type="submit"
            disabled={
              submitting
              || loadingCities
              || cities.length === 0
            }
            className="mt-6 rounded-xl bg-cyan-400 px-7 py-3 font-semibold text-slate-950 transition hover:bg-cyan-300 disabled:cursor-not-allowed disabled:opacity-50"
          >
            {submitting
              ? "正在建立模擬任務……"
              : "建立歷史氣象模擬任務"}
          </button>

          {error && (
            <div
              role="alert"
              className="mt-5 rounded-lg border border-red-900 bg-red-950 p-4 text-red-300"
            >
              {error}
            </div>
          )}
        </form>

        <section className="mt-8 rounded-xl border border-slate-800 bg-slate-900/50 p-5 text-sm text-slate-400">
          <h2 className="font-semibold text-slate-200">
            異步任務流程
          </h2>

          <ol className="mt-3 list-inside list-decimal space-y-2">
            <li>
              前端將模擬配置提交至 FastAPI。
            </li>
            <li>
              後端在 PostgreSQL 中建立任務記錄。
            </li>
            <li>
              Celery Worker 下載氣象資料並執行數值模擬。
            </li>
            <li>
              建立成功後，頁面會自動跳轉至任務進度頁。
            </li>
          </ol>
        </section>
      </div>
    </main>
  );
}