"use client";

import { type FormEvent, useState } from "react";

import { BenchmarkChart } from "@/components/charts/benchmark-chart";
import { NumberField } from "@/components/forms/number-field";
import { EnvironmentInputFields } from "@/components/simulation/environment-input-fields";
import { MaterialInputFields } from "@/components/simulation/material-input-fields";
import { PersonInputFields } from "@/components/simulation/person-input-fields";
import { compareWithGagge } from "@/lib/api-client";
import { formatNumber, formatSignedNumber } from "@/lib/format";
import type {
  BenchmarkMetric,
  GaggeBenchmarkRequest,
  GaggeBenchmarkResponse,
} from "@/types/benchmark";

/**
 * Defaults describe a warm, still, indoor-like scene where the Gagge two-node
 * model is defined. Raise solar radiation to probe the outdoor extension; the
 * backend reports how it aligned the inputs under "Alignment applied".
 */
const initialRequest: GaggeBenchmarkRequest = {
  duration_minutes: 60,

  environment: {
    air_temperature_c: 34,
    mean_radiant_temperature_c: 34,
    sky_temperature_c: null,
    relative_humidity_percent: 40,
    wind_speed_m_s: 0.5,
    solar_radiation_w_m2: 0,
    sky_view_factor: 0.5,
  },

  person: {
    met: 1.2,
    body_mass_kg: 70,
    body_surface_area_m2: 1.8,
    initial_core_temperature_c: 36.8,
    initial_skin_temperature_c: 33.7,
  },

  material: {
    name: "Ordinary clothing",
    clothing_insulation_clo: 0.5,
    clothing_area_factor: null,
    solar_reflectance: 0.4,
    solar_transmittance: 0,
    infrared_emissivity: 0.9,
    projected_solar_area_factor: 0.25,
    absorbed_solar_to_body_fraction: 0.35,
  },

  tolerances: {
    core_temperature_c: 0.31,
    skin_temperature_c: 1.01,
  },
};

export default function GaggeBenchmarkPage() {
  const [request, setRequest] = useState<GaggeBenchmarkRequest>(initialRequest);
  const [result, setResult] = useState<GaggeBenchmarkResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    setLoading(true);
    setError("");

    try {
      setResult(await compareWithGagge(request));
    } catch (caughtError) {
      setError(
        caughtError instanceof Error
          ? caughtError.message
          : "Gagge benchmark failed",
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl px-6 py-10">
        <header>
          <p className="text-sm font-medium text-cyan-400">Model Verification</p>

          <h1 className="mt-2 text-3xl font-bold">Gagge Two-Node Benchmark</h1>

          <p className="mt-3 max-w-3xl text-slate-400">
            Run the platform prototype and the reference Gagge two-node model
            on the same scenario, then compare the full core and skin
            temperature trajectories against the acceptance tolerances.
          </p>
        </header>

        <form onSubmit={handleSubmit} className="mt-10 space-y-8">
          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">Benchmark Settings</h2>

            <div className="mt-5 grid gap-5 md:grid-cols-3">
              <NumberField
                label="Duration"
                suffix="min"
                value={request.duration_minutes}
                min={1}
                max={240}
                step={1}
                hint="The reference library itself only runs 60 minutes; longer runs use the ported model."
                onChange={(value) =>
                  setRequest({ ...request, duration_minutes: value })
                }
              />

              <NumberField
                label="Core Temperature Tolerance"
                suffix="°C"
                value={request.tolerances.core_temperature_c}
                min={0.01}
                max={5}
                step={0.05}
                onChange={(value) =>
                  setRequest({
                    ...request,
                    tolerances: { ...request.tolerances, core_temperature_c: value },
                  })
                }
              />

              <NumberField
                label="Skin Temperature Tolerance"
                suffix="°C"
                value={request.tolerances.skin_temperature_c}
                min={0.01}
                max={10}
                step={0.1}
                onChange={(value) =>
                  setRequest({
                    ...request,
                    tolerances: { ...request.tolerances, skin_temperature_c: value },
                  })
                }
              />
            </div>
          </section>

          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">Environment</h2>

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

          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">Clothing</h2>

            <div className="mt-5">
              <MaterialInputFields
                material={request.material}
                showName
                enableLibrary
                onChange={(material) => setRequest({ ...request, material })}
              />
            </div>
          </section>

          <button
            type="submit"
            disabled={loading}
            className="rounded-xl bg-cyan-400 px-8 py-3 font-semibold text-slate-950 transition hover:bg-cyan-300 disabled:cursor-not-allowed disabled:opacity-50"
          >
            {loading ? "Running benchmark..." : "Run Benchmark"}
          </button>

          {error && (
            <div
              role="alert"
              className="rounded-xl border border-red-900 bg-red-950 p-4 text-red-300"
            >
              {error}
            </div>
          )}
        </form>

        {result && (
          <section className="mt-12 space-y-8">
            <VerdictBanner result={result} />

            <div className="grid gap-4 lg:grid-cols-2">
              <MetricCard title="Core Temperature" metric={result.core_temperature} />
              <MetricCard title="Skin Temperature" metric={result.skin_temperature} />
            </div>

            <BenchmarkChart
              points={result.time_series}
              referenceLabel={result.reference_model}
            />

            <FinalStateTable result={result} />

            <div className="grid gap-8 lg:grid-cols-2">
              <AlignmentList items={result.alignment_applied} />
              <PortParityPanel result={result} />
            </div>

            <div className="rounded-xl border border-amber-800 bg-amber-950/50 p-4 text-sm text-amber-200">
              <p>{result.warning}</p>
              <p className="mt-2">{result.environment_note}</p>
            </div>
          </section>
        )}
      </div>
    </main>
  );
}

function PassBadge({ passed }: { passed: boolean }) {
  return (
    <span
      className={[
        "inline-flex rounded-full border px-2.5 py-1 text-xs font-medium",
        passed
          ? "border-emerald-800 bg-emerald-950 text-emerald-300"
          : "border-red-800 bg-red-950 text-red-300",
      ].join(" ")}
    >
      {passed ? "Within tolerance" : "Outside tolerance"}
    </span>
  );
}

function VerdictBanner({ result }: { result: GaggeBenchmarkResponse }) {
  const { passed } = result;

  return (
    <div
      className={[
        "rounded-2xl border p-5",
        passed
          ? "border-emerald-800 bg-emerald-950/40"
          : "border-red-800 bg-red-950/40",
      ].join(" ")}
    >
      <div className="flex flex-wrap items-center justify-between gap-6">
        <div>
          <p className="text-sm text-slate-400">Benchmark verdict</p>

          <p
            className={`mt-1 text-3xl font-bold ${
              passed ? "text-emerald-300" : "text-red-300"
            }`}
          >
            {passed ? "PASSED" : "FAILED"}
          </p>
        </div>

        <dl className="grid gap-x-10 gap-y-2 text-sm sm:grid-cols-3">
          <div>
            <dt className="text-slate-500">Reference model</dt>
            <dd className="mt-1 text-slate-200">{result.reference_model}</dd>
          </div>

          <div>
            <dt className="text-slate-500">Reference library</dt>
            <dd className="mt-1 text-slate-200">
              {result.reference_library}{" "}
              <span className="font-mono text-slate-400">
                {result.reference_library_version}
              </span>
            </dd>
          </div>

          <div>
            <dt className="text-slate-500">Port parity (60 min)</dt>
            <dd className="mt-1 font-mono text-slate-200">
              {formatNumber(
                result.reference_port_parity.maximum_absolute_difference_c,
                4,
                " °C",
              )}
            </dd>
          </div>
        </dl>
      </div>
    </div>
  );
}

function MetricCard({
  title,
  metric,
}: {
  title: string;
  metric: BenchmarkMetric;
}) {
  return (
    <article
      className={[
        "rounded-2xl border p-5",
        metric.passed
          ? "border-slate-800 bg-slate-900"
          : "border-red-900 bg-red-950/30",
      ].join(" ")}
    >
      <div className="flex items-center justify-between gap-4">
        <h3 className="text-lg font-semibold">{title}</h3>
        <PassBadge passed={metric.passed} />
      </div>

      <p className="mt-4 text-3xl font-bold text-cyan-300">
        {formatNumber(metric.maximum_absolute_difference_c, 3)}
        <span className="ml-1 text-base font-normal">°C</span>
      </p>

      <p className="mt-1 text-sm text-slate-400">
        maximum absolute difference · tolerance{" "}
        {formatNumber(metric.tolerance_c, 2, " °C")}
      </p>

      <dl className="mt-4 grid grid-cols-2 gap-4 text-sm">
        <div>
          <dt className="text-slate-500">Final difference</dt>
          <dd className="mt-1 text-slate-200">
            {formatSignedNumber(metric.final_difference_c, 3, " °C")}
          </dd>
        </div>

        <div>
          <dt className="text-slate-500">RMS difference</dt>
          <dd className="mt-1 text-slate-200">
            {formatNumber(metric.root_mean_square_difference_c, 3, " °C")}
          </dd>
        </div>
      </dl>
    </article>
  );
}

function FinalStateTable({ result }: { result: GaggeBenchmarkResponse }) {
  const rows = [
    {
      label: "Core temperature",
      unit: " °C",
      digits: 3,
      prototype: result.prototype.core_temperature_c,
      reference: result.gagge.core_temperature_c,
    },
    {
      label: "Skin temperature",
      unit: " °C",
      digits: 3,
      prototype: result.prototype.skin_temperature_c,
      reference: result.gagge.skin_temperature_c,
    },
    {
      label: "Skin evaporative heat loss",
      unit: " W/m²",
      digits: 1,
      prototype: result.prototype.evaporation_w_m2,
      reference: result.gagge.skin_evaporation_w_m2,
    },
    {
      label: "Skin wettedness",
      unit: "",
      digits: 3,
      prototype: result.prototype.skin_wettedness,
      reference: result.gagge.skin_wettedness,
    },
    {
      label: "Skin blood flow",
      unit: " kg/(h·m²)",
      digits: 2,
      prototype: result.prototype.skin_blood_flow_kg_h_m2,
      reference: result.gagge.skin_blood_flow_kg_h_m2,
    },
  ];

  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="text-xl font-semibold">Final State Comparison</h2>

      <p className="mt-2 text-sm text-slate-400">
        Values at the end of the {result.time_series.at(-1)?.minute ?? "—"}
        -minute run. Difference is prototype minus reference.
      </p>

      <div className="mt-5 overflow-x-auto">
        <table className="w-full min-w-160 text-left text-sm">
          <thead className="border-b border-slate-700 text-slate-400">
            <tr>
              <th className="px-3 py-3">Quantity</th>
              <th className="px-3 py-3">Prototype</th>
              <th className="px-3 py-3">{result.reference_model}</th>
              <th className="px-3 py-3">Difference</th>
            </tr>
          </thead>

          <tbody>
            {rows.map((row) => (
              <tr key={row.label} className="border-b border-slate-800">
                <td className="px-3 py-3 text-slate-300">{row.label}</td>
                <td className="px-3 py-3">
                  {formatNumber(row.prototype, row.digits, row.unit)}
                </td>
                <td className="px-3 py-3">
                  {formatNumber(row.reference, row.digits, row.unit)}
                </td>
                <td className="px-3 py-3 font-mono text-cyan-300">
                  {formatSignedNumber(
                    row.prototype - row.reference,
                    row.digits,
                    row.unit,
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <dl className="mt-5 grid gap-4 text-sm sm:grid-cols-2 lg:grid-cols-4">
        <div>
          <dt className="text-slate-500">Prototype energy residual</dt>
          <dd className="mt-1 text-slate-200">
            {formatNumber(result.prototype.energy_residual_percent, 4, " %")}
          </dd>
        </div>

        <div>
          <dt className="text-slate-500">Reference skin heat loss</dt>
          <dd className="mt-1 text-slate-200">
            {formatNumber(result.gagge.skin_heat_loss_w_m2, 1, " W/m²")}
          </dd>
        </div>

        <div>
          <dt className="text-slate-500">Reference respiratory loss</dt>
          <dd className="mt-1 text-slate-200">
            {formatNumber(result.gagge.respiratory_heat_loss_w_m2, 1, " W/m²")}
          </dd>
        </div>

        <div>
          <dt className="text-slate-500">Reference SET</dt>
          <dd className="mt-1 text-slate-200">
            {formatNumber(
              result.gagge.standard_effective_temperature_c,
              2,
              " °C",
            )}
          </dd>
        </div>
      </dl>
    </section>
  );
}

function AlignmentList({ items }: { items: string[] }) {
  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="text-xl font-semibold">Alignment Applied</h2>

      <p className="mt-2 text-sm text-slate-400">
        Adjustments the backend made so both models see an equivalent scenario.
      </p>

      {items.length === 0 ? (
        <p className="mt-4 text-sm text-slate-500">
          No alignment adjustments were needed.
        </p>
      ) : (
        <ul className="mt-4 list-inside list-disc space-y-2 text-sm text-slate-300">
          {items.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      )}
    </section>
  );
}

function PortParityPanel({ result }: { result: GaggeBenchmarkResponse }) {
  const parity = result.reference_port_parity;

  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="text-xl font-semibold">Reference Port Parity</h2>

      <p className="mt-2 text-sm text-slate-400">
        The in-house port of the reference model versus the published library
        after 60 minutes. This guards the port itself, independent of the
        prototype.
      </p>

      <table className="mt-4 w-full text-left text-sm">
        <thead className="border-b border-slate-700 text-slate-400">
          <tr>
            <th className="px-3 py-2">Quantity</th>
            <th className="px-3 py-2">Library</th>
            <th className="px-3 py-2">Port</th>
          </tr>
        </thead>

        <tbody>
          <tr className="border-b border-slate-800">
            <td className="px-3 py-2 text-slate-300">Core temperature</td>
            <td className="px-3 py-2">
              {formatNumber(parity.library_core_temperature_c, 4, " °C")}
            </td>
            <td className="px-3 py-2">
              {formatNumber(parity.port_core_temperature_c, 4, " °C")}
            </td>
          </tr>

          <tr className="border-b border-slate-800">
            <td className="px-3 py-2 text-slate-300">Skin temperature</td>
            <td className="px-3 py-2">
              {formatNumber(parity.library_skin_temperature_c, 4, " °C")}
            </td>
            <td className="px-3 py-2">
              {formatNumber(parity.port_skin_temperature_c, 4, " °C")}
            </td>
          </tr>
        </tbody>
      </table>

      <p className="mt-4 text-sm text-slate-400">
        Maximum absolute difference:{" "}
        <span className="font-mono text-cyan-300">
          {formatNumber(parity.maximum_absolute_difference_c, 4, " °C")}
        </span>
      </p>
    </section>
  );
}