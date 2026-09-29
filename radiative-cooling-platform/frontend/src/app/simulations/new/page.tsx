"use client";

import { type FormEvent, useState } from "react";

import { HeatFluxChart } from "@/components/charts/heat-flux-chart";
import { PhysiologyChart } from "@/components/charts/physiology-chart";
import { TemperatureChart } from "@/components/charts/temperature-chart";
import { NumberField } from "@/components/forms/number-field";
import { EnvironmentInputFields } from "@/components/simulation/environment-input-fields";
import { MaterialInputFields } from "@/components/simulation/material-input-fields";
import { ModelProvenancePanel } from "@/components/simulation/model-provenance-panel";
import { ModelQualityPanel } from "@/components/simulation/model-quality-panel";
import { PersonInputFields } from "@/components/simulation/person-input-fields";
import { runSimulation } from "@/lib/api-client";
import type { SimulationRequest, SimulationResponse } from "@/types/simulation";

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
    body_mass_kg: 70,
    body_surface_area_m2: 1.8,
    initial_core_temperature_c: 36.8,
    initial_skin_temperature_c: 33.7,
  },

  control_material: {
    name: "Ordinary clothing",
    clothing_insulation_clo: 0.5,
    clothing_area_factor: null,
    solar_reflectance: 0.4,
    solar_transmittance: 0,
    infrared_emissivity: 0.8,
    projected_solar_area_factor: 0.25,
    absorbed_solar_to_body_fraction: 0.35,
  },

  rc_material: {
    name: "Radiative Cooling Clothing",
    clothing_insulation_clo: 0.4,
    clothing_area_factor: null,
    solar_reflectance: 0.92,
    solar_transmittance: 0,
    infrared_emissivity: 0.95,
    projected_solar_area_factor: 0.25,
    absorbed_solar_to_body_fraction: 0.35,
  },
};

export default function NewSimulationPage() {
  const [request, setRequest] = useState<SimulationRequest>(initialRequest);
  const [result, setResult] = useState<SimulationResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    setLoading(true);
    setError("");

    try {
      const response = await runSimulation(request);
      setResult(response);
    } catch (caughtError) {
      setError(
        caughtError instanceof Error ? caughtError.message : "Simulation failed",
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
            Create New Radiative Cooling Clothing Simulation
          </h1>

          <p className="mt-3 max-w-3xl text-slate-400">
            Compare the thermal performance of ordinary clothing and radiative
            cooling clothing under specified environmental conditions. The
            simulation tracks transient core, skin and clothing-surface
            temperature, heat flux components and thermoregulatory response.
          </p>
        </header>

        <form onSubmit={handleSubmit} className="mt-10 space-y-8">
          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">Basic Scenario</h2>

            <div className="mt-5 grid gap-5 md:grid-cols-3">
              <label className="block">
                <span className="mb-2 block text-sm text-slate-300">City</span>

                <input
                  value={request.city}
                  onChange={(event) =>
                    setRequest({ ...request, city: event.target.value })
                  }
                  className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 outline-none focus:border-cyan-500"
                />
              </label>

              <NumberField
                label="Simulation Duration"
                suffix="min"
                value={request.duration_minutes}
                min={1}
                max={1440}
                step={1}
                onChange={(value) =>
                  setRequest({ ...request, duration_minutes: value })
                }
              />

              <NumberField
                label="Output Interval"
                suffix="min"
                value={request.output_interval_minutes}
                min={1}
                max={60}
                step={1}
                onChange={(value) =>
                  setRequest({ ...request, output_interval_minutes: value })
                }
              />
            </div>
          </section>

          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">Environmental Parameters</h2>

            <div className="mt-5">
              <EnvironmentInputFields
                environment={request.environment}
                onChange={(environment) =>
                  setRequest({ ...request, environment })
                }
              />
            </div>
          </section>

          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">Person</h2>

            <div className="mt-5">
              <PersonInputFields
                person={request.person}
                onChange={(person) => setRequest({ ...request, person })}
              />
            </div>
          </section>

          <div className="grid gap-8 lg:grid-cols-2">
            <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
              <h2 className="text-xl font-semibold">Control Clothing</h2>

              <div className="mt-5">
                <MaterialInputFields
                  material={request.control_material}
                  onChange={(material) =>
                    setRequest({ ...request, control_material: material })
                  }
                />
              </div>
            </section>

            <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
              <h2 className="text-xl font-semibold">
                Radiative Cooling Clothing
              </h2>

              <div className="mt-5">
                <MaterialInputFields
                  material={request.rc_material}
                  onChange={(material) =>
                    setRequest({ ...request, rc_material: material })
                  }
                />
              </div>
            </section>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="rounded-xl bg-cyan-400 px-8 py-3 font-semibold text-slate-950 transition hover:bg-cyan-300 disabled:cursor-not-allowed disabled:opacity-50"
          >
            {loading ? "Numerical solution in progress..." : "Start simulation"}
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
            <PhysiologyChart result={result} />
            <HeatFluxChart result={result} />
            <ModelQualityPanel result={result} />
            <ModelProvenancePanel result={result} />
          </section>
        )}
      </div>
    </main>
  );
}

function SummaryCards({ result }: { result: SimulationResponse }) {
  const cards = [
    {
      label: "Final Skin Temperature Improvement",
      value: result.summary.final_skin_temperature_improvement_c,
    },
    {
      label: "Average Skin Temperature Improvement",
      value: result.summary.average_skin_temperature_improvement_c,
    },
    {
      label: "Final Core Temperature Improvement",
      value: result.summary.final_core_temperature_improvement_c,
    },
    {
      label: "RC Final Skin Temperature",
      value: result.radiative_cooling.final_skin_temperature_c,
    },
  ];

  return (
    <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
      {cards.map((card) => (
        <div
          key={card.label}
          className="rounded-2xl border border-slate-800 bg-slate-900 p-5"
        >
          <p className="text-sm text-slate-400">{card.label}</p>

          <p className="mt-2 text-3xl font-bold text-cyan-300">
            {card.value.toFixed(3)}
            <span className="ml-1 text-base font-normal">°C</span>
          </p>
        </div>
      ))}
    </div>
  );
}