"use client";

import {
  FormEvent,
  useState,
} from "react";

import { HeatFluxChart } from "@/components/charts/heat-flux-chart";
import { TemperatureChart } from "@/components/charts/temperature-chart";
import { runSimulation } from "@/lib/api-client";
import type {
  SimulationRequest,
  SimulationResponse,
} from "@/types/simulation";

const initialRequest: SimulationRequest = {
  city: "Dubai",
  duration_minutes: 120,
  output_interval_minutes: 1,

  environment: {
    air_temperature_c: 38,
    mean_radiant_temperature_c: 45,
    sky_temperature_c: 23,
    relative_humidity_percent: 40,
    wind_speed_m_s: 1.5,
    solar_radiation_w_m2: 800,
    sky_view_factor: 0.5,
  },

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

type NumberFieldProps = {
  label: string;
  value: number;
  min?: number;
  max?: number;
  step?: number;
  onChange: (value: number) => void;
};

function NumberField({
  label,
  value,
  min,
  max,
  step = 0.1,
  onChange,
}: NumberFieldProps) {
  return (
    <label className="block">
      <span className="mb-2 block text-sm text-slate-300">
        {label}
      </span>

      <input
        type="number"
        value={value}
        min={min}
        max={max}
        step={step}
        onChange={(event) =>
          onChange(Number(event.target.value))
        }
        className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-white outline-none focus:border-cyan-500"
      />
    </label>
  );
}

export default function NewSimulationPage() {
  const [request, setRequest] =
    useState<SimulationRequest>(initialRequest);

  const [result, setResult] =
    useState<SimulationResponse | null>(null);

  const [loading, setLoading] =
    useState(false);

  const [error, setError] =
    useState("");

  async function handleSubmit(
    event: FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault();

    setLoading(true);
    setError("");

    try {
      const response =
        await runSimulation(request);

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
            Simulation Engine Prototype
          </p>

          <h1 className="mt-2 text-3xl font-bold">
            新建輻射製冷服裝模擬
          </h1>

          <p className="mt-3 max-w-3xl text-slate-400">
            比較普通服裝與輻射製冷服裝在指定環境下的
            瞬態核心溫度、皮膚溫度與熱流變化。
          </p>
        </header>

        <form
          onSubmit={handleSubmit}
          className="mt-10 space-y-8"
        >
          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">
              基本情景
            </h2>

            <div className="mt-5 grid gap-5 md:grid-cols-3">
              <label className="block">
                <span className="mb-2 block text-sm text-slate-300">
                  城市
                </span>

                <input
                  value={request.city}
                  onChange={(event) =>
                    setRequest({
                      ...request,
                      city: event.target.value,
                    })
                  }
                  className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 outline-none focus:border-cyan-500"
                />
              </label>

              <NumberField
                label="模擬時長（分鐘）"
                value={request.duration_minutes}
                min={1}
                max={1440}
                step={1}
                onChange={(value) =>
                  setRequest({
                    ...request,
                    duration_minutes: value,
                  })
                }
              />

              <NumberField
                label="輸出間隔（分鐘）"
                value={
                  request.output_interval_minutes
                }
                min={1}
                max={60}
                step={1}
                onChange={(value) =>
                  setRequest({
                    ...request,
                    output_interval_minutes: value,
                  })
                }
              />
            </div>
          </section>

          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">
              環境參數
            </h2>

            <div className="mt-5 grid gap-5 md:grid-cols-2 lg:grid-cols-4">
              <NumberField
                label="空氣溫度（°C）"
                value={
                  request.environment
                    .air_temperature_c
                }
                onChange={(value) =>
                  setRequest({
                    ...request,
                    environment: {
                      ...request.environment,
                      air_temperature_c: value,
                    },
                  })
                }
              />

              <NumberField
                label="平均輻射溫度（°C）"
                value={
                  request.environment
                    .mean_radiant_temperature_c
                }
                onChange={(value) =>
                  setRequest({
                    ...request,
                    environment: {
                      ...request.environment,
                      mean_radiant_temperature_c:
                        value,
                    },
                  })
                }
              />

              <NumberField
                label="天空溫度（°C）"
                value={
                  request.environment
                    .sky_temperature_c ?? 23
                }
                onChange={(value) =>
                  setRequest({
                    ...request,
                    environment: {
                      ...request.environment,
                      sky_temperature_c: value,
                    },
                  })
                }
              />

              <NumberField
                label="相對濕度（%）"
                value={
                  request.environment
                    .relative_humidity_percent
                }
                min={0}
                max={100}
                onChange={(value) =>
                  setRequest({
                    ...request,
                    environment: {
                      ...request.environment,
                      relative_humidity_percent:
                        value,
                    },
                  })
                }
              />

              <NumberField
                label="風速（m/s）"
                value={
                  request.environment
                    .wind_speed_m_s
                }
                min={0}
                max={30}
                onChange={(value) =>
                  setRequest({
                    ...request,
                    environment: {
                      ...request.environment,
                      wind_speed_m_s: value,
                    },
                  })
                }
              />

              <NumberField
                label="太陽輻射（W/m²）"
                value={
                  request.environment
                    .solar_radiation_w_m2
                }
                min={0}
                max={1500}
                step={10}
                onChange={(value) =>
                  setRequest({
                    ...request,
                    environment: {
                      ...request.environment,
                      solar_radiation_w_m2: value,
                    },
                  })
                }
              />

              <NumberField
                label="天空視角係數"
                value={
                  request.environment
                    .sky_view_factor
                }
                min={0}
                max={1}
                step={0.05}
                onChange={(value) =>
                  setRequest({
                    ...request,
                    environment: {
                      ...request.environment,
                      sky_view_factor: value,
                    },
                  })
                }
              />

              <NumberField
                label="活動強度（MET）"
                value={request.person.met}
                min={0.7}
                max={10}
                onChange={(value) =>
                  setRequest({
                    ...request,
                    person: {
                      ...request.person,
                      met: value,
                    },
                  })
                }
              />
            </div>
          </section>

          <div className="grid gap-8 lg:grid-cols-2">
            <MaterialSection
              title="普通對照服裝"
              material={request.control_material}
              onChange={(material) =>
                setRequest({
                  ...request,
                  control_material: material,
                })
              }
            />

            <MaterialSection
              title="輻射製冷服裝"
              material={request.rc_material}
              onChange={(material) =>
                setRequest({
                  ...request,
                  rc_material: material,
                })
              }
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            className="rounded-xl bg-cyan-400 px-8 py-3 font-semibold text-slate-950 transition hover:bg-cyan-300 disabled:cursor-not-allowed disabled:opacity-50"
          >
            {loading
              ? "正在進行數值求解……"
              : "開始模擬"}
          </button>

          {error && (
            <div className="rounded-xl border border-red-900 bg-red-950 p-4 text-red-300">
              {error}
            </div>
          )}
        </form>

        {result && (
          <section className="mt-12 space-y-8">
            <SummaryCards result={result} />

            <div className="rounded-xl border border-amber-800 bg-amber-950/50 p-4 text-sm text-amber-200">
              {result.warning}
            </div>

            <TemperatureChart result={result} />
            <HeatFluxChart result={result} />
          </section>
        )}
      </div>
    </main>
  );
}

type MaterialSectionProps = {
  title: string;
  material: SimulationRequest["control_material"];
  onChange: (
    material: SimulationRequest["control_material"],
  ) => void;
};

function MaterialSection({
  title,
  material,
  onChange,
}: MaterialSectionProps) {
  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="text-xl font-semibold">
        {title}
      </h2>

      <div className="mt-5 grid gap-5 sm:grid-cols-2">
        <NumberField
          label="服裝熱阻（clo）"
          value={material.clothing_insulation_clo}
          min={0}
          max={5}
          step={0.05}
          onChange={(value) =>
            onChange({
              ...material,
              clothing_insulation_clo: value,
            })
          }
        />

        <NumberField
          label="太陽反射率"
          value={material.solar_reflectance}
          min={0}
          max={1}
          step={0.01}
          onChange={(value) =>
            onChange({
              ...material,
              solar_reflectance: value,
            })
          }
        />

        <NumberField
          label="太陽透射率"
          value={material.solar_transmittance}
          min={0}
          max={1}
          step={0.01}
          onChange={(value) =>
            onChange({
              ...material,
              solar_transmittance: value,
            })
          }
        />

        <NumberField
          label="中紅外發射率"
          value={material.infrared_emissivity}
          min={0}
          max={1}
          step={0.01}
          onChange={(value) =>
            onChange({
              ...material,
              infrared_emissivity: value,
            })
          }
        />
      </div>
    </section>
  );
}

function SummaryCards({
  result,
}: {
  result: SimulationResponse;
}) {
  const cards = [
    {
      label: "最終皮膚溫度改善",
      value:
        result.summary
          .final_skin_temperature_improvement_c,
      unit: "°C",
    },
    {
      label: "平均皮膚溫度改善",
      value:
        result.summary
          .average_skin_temperature_improvement_c,
      unit: "°C",
    },
    {
      label: "最終核心溫度改善",
      value:
        result.summary
          .final_core_temperature_improvement_c,
      unit: "°C",
    },
    {
      label: "RC 最終皮膚溫度",
      value:
        result.radiative_cooling
          .final_skin_temperature_c,
      unit: "°C",
    },
  ];

  return (
    <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
      {cards.map((card) => (
        <div
          key={card.label}
          className="rounded-2xl border border-slate-800 bg-slate-900 p-5"
        >
          <p className="text-sm text-slate-400">
            {card.label}
          </p>

          <p className="mt-2 text-3xl font-bold text-cyan-300">
            {card.value.toFixed(3)}
            <span className="ml-1 text-base font-normal">
              {card.unit}
            </span>
          </p>
        </div>
      ))}
    </div>
  );
}