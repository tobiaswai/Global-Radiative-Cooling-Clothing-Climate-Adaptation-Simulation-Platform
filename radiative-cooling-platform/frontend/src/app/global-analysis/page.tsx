"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import {
  createGlobalBatch,
  getGlobalCities,
} from "@/lib/api-client";

import type {
  GlobalBatchCreate,
  GlobalCity,
} from "@/types/global-batch";

const initialRequest: GlobalBatchCreate = {
  name: "Global annual adaptation analysis",
  city_ids: [],
  year: 2023,
  start_month: 1,
  end_month: 12,
  representative_day: 15,
  local_start_hour: 12,
  duration_minutes: 120,
  output_interval_minutes: 10,
  minimum_skin_improvement_c: 0.2,

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
  const [request, setRequest] = useState(initialRequest);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadCities() {
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
      }
    }

    void loadCities();
  }, []);

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

  async function submitBatch() {
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

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl px-6 py-10">
        <header>
          <p className="text-sm font-medium text-cyan-400">
            Stage 4 Global Analysis
          </p>

          <h1 className="mt-2 text-3xl font-bold">
            Global Climate Adaptation Analysis
          </h1>

          <p className="mt-3 max-w-3xl text-slate-400">
            Compare conventional clothing with radiative cooling clothing
            using a representative day for each month and weighting the
            results by the number of days in that month.
          </p>
        </header>

        <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">
            Analysis Settings
          </h2>

          <div className="mt-5 grid gap-5 md:grid-cols-4">
            <NumberField
              label="Year"
              value={request.year}
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
              onChange={(start_month) =>
                setRequest((current) => ({
                  ...current,
                  start_month,
                }))
              }
            />

            <NumberField
              label="End Month"
              value={request.end_month}
              onChange={(end_month) =>
                setRequest((current) => ({
                  ...current,
                  end_month,
                }))
              }
            />

            <NumberField
              label="Minimum Average Cooling (°C)"
              value={request.minimum_skin_improvement_c}
              step={0.1}
              onChange={(minimum_skin_improvement_c) =>
                setRequest((current) => ({
                  ...current,
                  minimum_skin_improvement_c,
                }))
              }
            />
          </div>
        </section>

        <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-6">
          <div className="flex flex-wrap items-center justify-between gap-4">
            <h2 className="text-xl font-semibold">
              Cities
            </h2>

            <div className="flex gap-3">
              <button
                type="button"
                onClick={() =>
                  setRequest((current) => ({
                    ...current,
                    city_ids: cities.map((city) => city.id),
                  }))
                }
                className="rounded-lg border border-slate-700 px-4 py-2 text-sm"
              >
                Select All
              </button>

              <button
                type="button"
                onClick={() =>
                  setRequest((current) => ({
                    ...current,
                    city_ids: [],
                  }))
                }
                className="rounded-lg border border-slate-700 px-4 py-2 text-sm"
              >
                Clear Selection
              </button>
            </div>
          </div>

          <div className="mt-5 grid gap-3 md:grid-cols-3 lg:grid-cols-4">
            {cities.map((city) => {
              const selected = request.city_ids.includes(city.id);

              return (
                <button
                  key={city.id}
                  type="button"
                  onClick={() => toggleCity(city.id)}
                  className={[
                    "rounded-xl border p-4 text-left",
                    selected
                      ? "border-cyan-400 bg-cyan-950"
                      : "border-slate-700 bg-slate-950",
                  ].join(" ")}
                >
                  <p className="font-medium">
                    {city.name}
                  </p>

                  <p className="mt-1 text-sm text-slate-400">
                    {city.country}
                  </p>

                  <p className="mt-2 text-xs text-slate-500">
                    {city.climate_type}
                  </p>
                </button>
              );
            })}
          </div>
        </section>

        {error && (
          <div className="mt-6 rounded-xl border border-red-900 bg-red-950 p-4 text-red-300">
            {error}
          </div>
        )}

        <button
          type="button"
          disabled={loading || request.city_ids.length === 0}
          onClick={submitBatch}
          className="mt-8 rounded-lg bg-cyan-400 px-7 py-3 font-semibold text-slate-950 disabled:opacity-50"
        >
          {loading
            ? "Creating Analysis Batch..."
            : `Analyze ${request.city_ids.length} ${
                request.city_ids.length === 1 ? "City" : "Cities"
              }`}
        </button>
      </div>
    </main>
  );
}

function NumberField({
  label,
  value,
  step = 1,
  onChange,
}: {
  label: string;
  value: number;
  step?: number;
  onChange: (value: number) => void;
}) {
  return (
    <label>
      <span className="mb-2 block text-sm text-slate-300">
        {label}
      </span>

      <input
        type="number"
        value={value}
        step={step}
        onChange={(event) =>
          onChange(Number(event.target.value))
        }
        className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2"
      />
    </label>
  );
}