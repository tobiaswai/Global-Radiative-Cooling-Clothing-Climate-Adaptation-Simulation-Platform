# Frontend Source Bundle (`frontend/` - excluding node_modules, .next, public assets)

## Directory Structure
```text
frontend/package.json
frontend/tsconfig.json
frontend/next.config.ts
frontend/eslint.config.mjs
frontend/AGENTS.md
frontend/CLAUDE.md
frontend/README.md
frontend/.env.example
frontend/src/app/benchmarks/gagge/page.tsx
frontend/src/app/global-analysis/[batchId]/page.tsx
frontend/src/app/global-analysis/page.tsx
frontend/src/app/globals.css
frontend/src/app/layout.tsx
frontend/src/app/materials/[materialId]/page.tsx
frontend/src/app/materials/new/page.tsx
frontend/src/app/materials/page.tsx
frontend/src/app/page.tsx
frontend/src/app/simulations/[jobId]/page.tsx
frontend/src/app/simulations/new/page.tsx
frontend/src/app/simulations/page.tsx
frontend/src/app/simulations/weather/page.tsx
frontend/src/components/charts/benchmark-chart.tsx
frontend/src/components/charts/heat-flux-chart.tsx
frontend/src/components/charts/physiology-chart.tsx
frontend/src/components/charts/temperature-chart.tsx
frontend/src/components/charts/weather-chart.tsx
frontend/src/components/forms/number-field.tsx
frontend/src/components/forms/select-field.tsx
frontend/src/components/global-adaptation-map.tsx
frontend/src/components/layout/NavBar.tsx
frontend/src/components/materials/provenance-editor.tsx
frontend/src/components/simulation/environment-assumptions-fields.tsx
frontend/src/components/simulation/environment-input-fields.tsx
frontend/src/components/simulation/material-input-fields.tsx
frontend/src/components/simulation/material-version-picker.tsx
frontend/src/components/simulation/model-provenance-panel.tsx
frontend/src/components/simulation/model-quality-panel.tsx
frontend/src/components/simulation/person-input-fields.tsx
frontend/src/config/navigation.ts
frontend/src/lib/api-client.ts
frontend/src/lib/date-defaults.test.ts
frontend/src/lib/date-defaults.ts
frontend/src/lib/environment-assumptions.ts
frontend/src/lib/format.test.ts
frontend/src/lib/format.ts
frontend/src/lib/time-series.test.ts
frontend/src/lib/time-series.ts
frontend/src/locales/en.ts
frontend/src/types/benchmark.ts
frontend/src/types/global-batch.ts
frontend/src/types/material.ts
frontend/src/types/simulation.ts

# public/ (names only)
frontend/public/file.svg
frontend/public/globe.svg
frontend/public/next.svg
frontend/public/vercel.svg
frontend/public/window.svg
```

---

## Source Code Files

### File: `frontend/package.json`
```json
{
  "name": "frontend",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint .",
    "test": "vitest run"
  },
  "dependencies": {
    "maplibre-gl": "^6.7.0",
    "next": "^16.3.7",
    "plotly.js": "^4.1.1",
    "react": "19.2.4",
    "react-dom": "19.2.4",
    "react-plotly.js": "^4.1.0"
  },
  "devDependencies": {
    "@tailwindcss/postcss": "^4",
    "@types/geojson": "^7946.0.16",
    "@types/node": "^24.19.0",
    "@types/plotly.js": "^3.0.10",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "@types/react-plotly.js": "^2.6.4",
    "eslint": "^9",
    "eslint-config-next": "16.2.12",
    "tailwindcss": "^4",
    "typescript": "^5",
    "vitest": "^5.0.2"
  },
  "allowScripts": {
    "maplibre-gl@6.7.0": true,
    "maplibre-gl@4.7.1": true,
    "sharp@0.34.5": true,
    "unrs-resolver@1.12.2": true,
    "es5-ext@0.10.64": true,
    "esbuild@0.28.2": true
  }
}

```

### File: `frontend/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2017",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "react-jsx",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": [
    "next-env.d.ts",
    "**/*.ts",
    "**/*.tsx",
    ".next/types/**/*.ts",
    ".next/dev/types/**/*.ts",
    "**/*.mts"
  ],
  "exclude": ["node_modules"]
}

```

### File: `frontend/next.config.ts`
```typescript
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  outputFileTracingRoot: process.cwd(),
}

export default nextConfig
```

### File: `frontend/eslint.config.mjs`
```javascript
import { defineConfig, globalIgnores } from "eslint/config";
import nextVitals from "eslint-config-next/core-web-vitals";
import nextTs from "eslint-config-next/typescript";

const eslintConfig = defineConfig([
  ...nextVitals,
  ...nextTs,
  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    ".next/**",
    "out/**",
    "build/**",
    "next-env.d.ts",
  ]),
]);

export default eslintConfig;

```

### File: `frontend/AGENTS.md`
```markdown
<!-- BEGIN:nextjs-agent-rules -->
# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` before writing any code. Heed deprecation notices.
<!-- END:nextjs-agent-rules -->

```

### File: `frontend/CLAUDE.md`
```markdown
@AGENTS.md

```

### File: `frontend/README.md`
```markdown
# Radiative Cooling Platform Frontend

This directory contains the Next.js frontend for the Global Radiative
Cooling Clothing Climate Adaptation Simulation Platform.

## Requirements

- Node.js
- npm

## Development

npm install
npm run dev

## Build

npm run build

## Lint

npm run lint
```

### File: `frontend/.env.example`
```text
# Base URL of the FastAPI backend (no trailing slash)
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

### File: `frontend/src/app/benchmarks/gagge/page.tsx`
```tsx
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
    direct_normal_irradiance_w_m2: null, 
    diffuse_horizontal_irradiance_w_m2: null, 
    ground_albedo: 0.2
  },

  person: {
    met: 1.2,
    body_mass_kg: 70,
    body_surface_area_m2: 1.8,
    initial_core_temperature_c: 36.8,
    initial_skin_temperature_c: 33.7,
    position: "standing",
  },

  material: {
    name: "Ordinary clothing",
    clothing_insulation_clo: 0.5,
    clothing_area_factor: null,
    solar_reflectance: 0.4,
    solar_transmittance: 0,
    infrared_emissivity: 0.9,
    projected_solar_area_factor: 0.25,
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
```

### File: `frontend/src/app/global-analysis/[batchId]/page.tsx`
```tsx
"use client";
import Link from "next/link";

import dynamic from "next/dynamic";

import { useParams } from "next/navigation";

import {
  useEffect,
  useMemo,
  useState,
} from "react";

import {
  cancelGlobalBatch,
  getGlobalBatch,
  getGlobalBatchExportUrl,
  getGlobalBatchGeoJson,
  retryFailedGlobalBatchCities,
} from "@/lib/api-client";

import type {
  GeoJsonFeatureCollection,
  GlobalBatchDetail,
  GlobalCityResult,
  HeatwaveEvent,
} from "@/types/global-batch";


const GlobalAdaptationMap = dynamic(
  () =>
    import(
      "@/components/global-adaptation-map"
    ),
  {
    ssr: false,

    loading: () => (
      <div className="flex h-[35rem] items-center justify-center rounded-2xl bg-slate-950 text-slate-400">
        Loading global map...
      </div>
    ),
  },
);


const terminalStatuses =
  new Set<string>([
    "completed",
    "partial_completed",
    "failed",
    "cancelled",
  ]);


export default function GlobalBatchPage() {
  const parameters = useParams<{
    batchId: string;
  }>();

  const [
    batch,
    setBatch,
  ] = useState<GlobalBatchDetail | null>(
    null,
  );

  const [
    geoJson,
    setGeoJson,
  ] =
    useState<GeoJsonFeatureCollection | null>(
      null,
    );

  const [
    selectedCityId,
    setSelectedCityId,
  ] = useState<string | null>(null);

  const [
    error,
    setError,
  ] = useState("");

  const [
    pollingRevision,
    setPollingRevision,
  ] = useState(0);

  const [
    isCancelling,
    setIsCancelling,
  ] = useState(false);

  const [
    isRetrying,
    setIsRetrying,
  ] = useState(false);

  useEffect(() => {
    let disposed = false;
    let timer: number | null = null;

    async function load() {
      try {
        const response =
          await getGlobalBatch(
            parameters.batchId,
          );

        if (disposed) {
          return;
        }

        setBatch(response);
        setError("");

        if (
          response.completed_city_count > 0
        ) {
          try {
            const mapData =
              await getGlobalBatchGeoJson(
                parameters.batchId,
              );

            if (!disposed) {
              setGeoJson(mapData);
            }
          } catch (mapError) {
            if (!disposed) {
              setError(
                getErrorMessage(
                  mapError,
                  "Unable to load global map data.",
                ),
              );
            }
          }
        } else {
          setGeoJson(null);
        }

        if (
          !terminalStatuses.has(
            response.status,
          )
        ) {
          timer = window.setTimeout(
            load,
            3000,
          );
        }
      } catch (caughtError) {
        if (disposed) {
          return;
        }

        setError(
          getErrorMessage(
            caughtError,
            "Unable to load the global analysis.",
          ),
        );

        timer = window.setTimeout(
          load,
          5000,
        );
      }
    }

    void load();

    return () => {
      disposed = true;

      if (timer !== null) {
        window.clearTimeout(timer);
      }
    };
  }, [
    parameters.batchId,
    pollingRevision,
  ]);

  const selectedCity = useMemo(() => {
    if (!batch || !selectedCityId) {
      return null;
    }

    return (
      batch.city_results.find(
        (result) =>
          result.id === selectedCityId,
      ) ?? null
    );
  }, [
    batch,
    selectedCityId,
  ]);

  const completedResults = useMemo(
    () =>
      batch?.city_results.filter(
        (result) =>
          result.status === "completed",
      ) ?? [],
    [batch],
  );

  const aggregateMetrics = useMemo(
    () => ({
      meanExposureCoverage:
        calculateMean(
          completedResults.map(
            (result) =>
              result
                .exposure_coverage_percent,
          ),
        ),

      meanAdaptationRate:
        calculateMean(
          completedResults.map(
            (result) =>
              result
                .climate_adaptation_rate_percent,
          ),
        ),

      meanSkinCooling:
        calculateMean(
          completedResults.map(
            (result) =>
              result
                .annual_average_skin_improvement_c,
          ),
        ),

      meanSkinP90:
        calculateMean(
          completedResults.map(
            (result) =>
              result
                .skin_improvement_p90_c,
          ),
        ),

      totalHeatwaveEvents:
        completedResults.reduce(
          (total, result) =>
            total +
            (result.heatwave_event_count ??
              0),
          0,
        ),
    }),
    [completedResults],
  );

  async function refreshBatch() {
    const updated =
      await getGlobalBatch(
        parameters.batchId,
      );

    setBatch(updated);

    if (
      updated.completed_city_count > 0
    ) {
      const mapData =
        await getGlobalBatchGeoJson(
          parameters.batchId,
        );

      setGeoJson(mapData);
    } else {
      setGeoJson(null);
    }

    return updated;
  }

  async function cancelBatch() {
    if (isCancelling) {
      return;
    }

    try {
      setIsCancelling(true);
      setError("");

      await cancelGlobalBatch(
        parameters.batchId,
      );

      await refreshBatch();
    } catch (caughtError) {
      setError(
        getErrorMessage(
          caughtError,
          "Unable to cancel the analysis batch.",
        ),
      );
    } finally {
      setIsCancelling(false);
    }
  }

  async function retryFailedCities() {
    if (isRetrying) {
      return;
    }

    try {
      setIsRetrying(true);
      setError("");

      await retryFailedGlobalBatchCities(
        parameters.batchId,
      );

      await refreshBatch();

      setPollingRevision(
        (current) => current + 1,
      );
    } catch (caughtError) {
      setError(
        getErrorMessage(
          caughtError,
          "Unable to retry failed cities.",
        ),
      );
    } finally {
      setIsRetrying(false);
    }
  }

  if (!batch) {
    return (
      <main className="min-h-screen bg-slate-950 p-10 text-white">
        <div className="mx-auto max-w-7xl">
          {error ? (
            <div className="rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">
              {error}
            </div>
          ) : (
            <p className="text-slate-400">
              Loading global analysis...
            </p>
          )}
        </div>
      </main>
    );
  }

  const isTerminal =
    terminalStatuses.has(batch.status);

  const canRetry =
    isTerminal &&
    batch.failed_city_count > 0 &&
    (
      batch.status ===
        "partial_completed" ||
      batch.status === "failed"
    );

  const analysisResolution =
    batch.request.analysis_resolution ??
    "representative";

  const analysisResolutionLabel =
    analysisResolution === "daily"
      ? "Daily"
      : "Representative Days";

  const samplingLabel =
    analysisResolution === "daily"
      ? `Every ${
          batch.request.daily_stride_days ??
          1
        } day(s)`
      : `${
          batch.request
            .sample_days_per_month ?? 1
        } day(s) per month`;

  const heatwaveAvailable =
    batch.request
      .enable_heatwave_analysis &&
    analysisResolution === "daily" &&
    (
      batch.request.daily_stride_days ??
      1
    ) === 1;

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-[95rem] px-6 py-10">
        <nav className="mb-4 flex items-center gap-2 text-sm text-slate-400">
          <Link href="/global-analysis" className="hover:text-slate-100">
            Global Analysis
          </Link>
          <span>/</span>
          <span className="text-slate-200">Batch Result</span>
        </nav>
        <header className="flex flex-wrap items-start justify-between gap-5">
          <div>
            <p className="text-sm font-medium text-cyan-400">
              Global Analysis
            </p>

            <h1 className="mt-2 text-3xl font-bold">
              {batch.request.name}
            </h1>

            <p className="mt-3 text-sm text-slate-400">
              Batch ID:{" "}
              <span className="font-mono text-slate-300">
                {batch.id}
              </span>
            </p>

            <p className="mt-1 text-sm text-slate-500">
              Created{" "}
              {formatDateTime(
                batch.created_at,
              )}
            </p>
          </div>

          <div className="flex flex-wrap gap-3">
            {canRetry && (
              <button
                type="button"
                onClick={
                  retryFailedCities
                }
                disabled={isRetrying}
                className="rounded-lg border border-amber-700 px-5 py-2 text-amber-300 transition-colors hover:bg-amber-950 disabled:cursor-not-allowed disabled:opacity-50"
              >
                {isRetrying
                  ? "Submitting Retry..."
                  : "Retry Failed Cities"}
              </button>
            )}

            <a
              href={getGlobalBatchExportUrl(
                batch.id,
              )}
              className="rounded-lg border border-cyan-700 px-5 py-2 text-cyan-300 transition-colors hover:bg-cyan-950"
            >
              Download Export
            </a>

            {!isTerminal && (
              <button
                type="button"
                onClick={cancelBatch}
                disabled={isCancelling}
                className="rounded-lg border border-red-800 px-5 py-2 text-red-300 transition-colors hover:bg-red-950 disabled:cursor-not-allowed disabled:opacity-50"
              >
                {isCancelling
                  ? "Cancelling..."
                  : "Cancel Batch"}
              </button>
            )}
          </div>
        </header>

        <section className="mt-8 grid gap-4 md:grid-cols-2 lg:grid-cols-4 xl:grid-cols-8">
          <Metric
            label="Status"
            value={formatLabel(
              batch.status,
            )}
          />

          <Metric
            label="Overall Progress"
            value={`${batch.progress}%`}
          />

          <Metric
            label="Completed Cities"
            value={
              `${batch.completed_city_count}` +
              ` / ${batch.total_city_count}`
            }
          />

          <Metric
            label="Failed Cities"
            value={String(
              batch.failed_city_count,
            )}
          />

          <Metric
            label="Cancelled Cities"
            value={String(
              batch.cancelled_city_count,
            )}
          />

          <Metric
            label="Resolution"
            value={
              analysisResolutionLabel
            }
          />

          <Metric
            label="Sampling"
            value={samplingLabel}
          />

          <Metric
            label="Execution Profile"
            value={formatLabel(
              batch.request
                .execution_profile ??
                "auto",
            )}
          />
        </section>

        <div className="mt-5 h-3 overflow-hidden rounded-full bg-slate-800">
          <div
            className="h-full bg-cyan-400 transition-all duration-500"
            style={{
              width: `${
                clampProgress(
                  batch.progress,
                )
              }%`,
            }}
          />
        </div>

        <section className="mt-6 grid gap-4 md:grid-cols-2 lg:grid-cols-5">
          <Metric
            label="Mean Exposure Coverage"
            value={formatNumber(
              aggregateMetrics
                .meanExposureCoverage,
              "%",
            )}
          />

          <Metric
            label="Mean Adaptation Rate"
            value={formatNumber(
              aggregateMetrics
                .meanAdaptationRate,
              "%",
            )}
          />

          <Metric
            label="Mean Skin Cooling"
            value={formatNumber(
              aggregateMetrics
                .meanSkinCooling,
              " °C",
            )}
          />

          <Metric
            label="Mean P90 Skin Cooling"
            value={formatNumber(
              aggregateMetrics
                .meanSkinP90,
              " °C",
            )}
          />

          <Metric
            label="Detected Heatwaves"
            value={
              heatwaveAvailable
                ? String(
                    aggregateMetrics
                      .totalHeatwaveEvents,
                  )
                : "Unavailable"
            }
          />
        </section>

        {batch.error_message && (
          <div className="mt-6 rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">
            <p className="font-semibold">
              Batch Error
            </p>

            <p className="mt-2 text-sm">
              {batch.error_message}
            </p>
          </div>
        )}

        {error && (
          <div className="mt-6 rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">
            {error}
          </div>
        )}

        <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-5">
          <div className="mb-5">
            <h2 className="text-xl font-semibold">
              Global Adaptation Map
            </h2>

            <p className="mt-2 text-sm text-slate-400">
              Completed cities are colored by
              climate adaptation rate.
            </p>
          </div>

          {geoJson &&
          geoJson.features.length > 0 ? (
            <GlobalAdaptationMap
              data={geoJson}
            />
          ) : (
            <div className="flex h-80 items-center justify-center rounded-xl bg-slate-950 text-slate-500">
              Map data will appear after at
              least one city completes.
            </div>
          )}
        </section>

        <section className="mt-8 overflow-hidden rounded-2xl border border-slate-800 bg-slate-900">
          <div className="border-b border-slate-800 p-5">
            <h2 className="text-xl font-semibold">
              City Results
            </h2>

            <p className="mt-2 text-sm text-slate-400">
              Select a city to inspect monthly,
              percentile, checkpoint, and
              heatwave results.
            </p>
          </div>

          <div className="overflow-x-auto">
            <table className="min-w-[90rem] w-full text-left text-sm">
              <thead className="bg-slate-950 text-xs uppercase tracking-wide text-slate-500">
                <tr>
                  <th className="px-4 py-4">
                    City
                  </th>

                  <th className="px-4 py-4">
                    Status
                  </th>

                  <th className="px-4 py-4">
                    Checkpoint
                  </th>

                  <th className="px-4 py-4">
                    Exposure
                  </th>

                  <th className="px-4 py-4">
                    Adaptation
                  </th>

                  <th className="px-4 py-4">
                    Mean Skin
                  </th>

                  <th className="px-4 py-4">
                    P90 Skin
                  </th>

                  <th className="px-4 py-4">
                    P95 Skin
                  </th>

                  <th className="px-4 py-4">
                    Heatwaves
                  </th>

                  <th className="px-4 py-4">
                    Samples
                  </th>

                  <th className="px-4 py-4">
                    Heartbeat
                  </th>
                </tr>
              </thead>

              <tbody>
                {batch.city_results.map(
                  (result) => (
                    <CityResultRow
                      key={result.id}
                      result={result}
                      selected={
                        selectedCityId ===
                        result.id
                      }
                      onSelect={() =>
                        setSelectedCityId(
                          result.id,
                        )
                      }
                    />
                  ),
                )}
              </tbody>
            </table>
          </div>
        </section>

        {selectedCity && (
          <CityDetailPanel
            result={selectedCity}
            heatwaveAvailable={
              heatwaveAvailable
            }
            onClose={() =>
              setSelectedCityId(null)
            }
          />
        )}
      </div>
    </main>
  );
}


function CityResultRow({
  result,
  selected,
  onSelect,
}: {
  result: GlobalCityResult;
  selected: boolean;
  onSelect: () => void;
}) {
  return (
    <tr
      className={[
        "cursor-pointer border-t border-slate-800 align-top transition",
        selected
          ? "bg-cyan-950/50"
          : "hover:bg-slate-800/50",
      ].join(" ")}
      onClick={onSelect}
    >
      <td className="px-4 py-4">
        <p className="font-medium">
          {result.city_name}
        </p>

        <p className="text-xs text-slate-500">
          {result.country}
        </p>

        {result.error_message && (
          <p className="mt-2 max-w-xs text-xs leading-5 text-red-400">
            {result.error_message}
          </p>
        )}
      </td>

      <td className="px-4 py-4">
        <StatusBadge
          status={result.status}
        />

        <p className="mt-2 text-xs text-slate-500">
          {result.progress}%
        </p>

        <p className="mt-1 max-w-44 break-words text-xs text-slate-600">
          {formatLabel(result.stage)}
        </p>
      </td>

      <td className="px-4 py-4">
        <p>
          {result.completed_month_count}{" "}
          month(s)
        </p>

        <p className="mt-1 text-xs text-slate-500">
          Last month:{" "}
          {result.last_checkpoint_month ??
            "—"}
        </p>

        {result.resumed_from_checkpoint && (
          <span className="mt-2 inline-flex rounded-full border border-violet-800 bg-violet-950 px-2 py-1 text-xs text-violet-300">
            Resumed
          </span>
        )}
      </td>

      <td className="px-4 py-4">
        {formatNumber(
          result.exposure_coverage_percent,
          "%",
        )}

        {result.evaluated_weighted_days !==
          null && (
          <p className="mt-1 text-xs text-slate-500">
            {
              result.evaluated_weighted_days
            }{" "}
            weighted days
          </p>
        )}
      </td>

      <td className="px-4 py-4 text-cyan-300">
        {result
          .climate_adaptation_rate_percent ===
        null ? (
          <span className="text-slate-500">
            No qualifying exposure
          </span>
        ) : (
          formatNumber(
            result
              .climate_adaptation_rate_percent,
            "%",
          )
        )}
      </td>

      <td className="px-4 py-4">
        {formatNumber(
          result
            .annual_average_skin_improvement_c,
          " °C",
        )}
      </td>

      <td className="px-4 py-4">
        {formatNumber(
          result.skin_improvement_p90_c,
          " °C",
        )}
      </td>

      <td className="px-4 py-4">
        {formatNumber(
          result.skin_improvement_p95_c,
          " °C",
        )}
      </td>

      <td className="px-4 py-4">
        {result.heatwave_event_count ??
          "—"}

        {result.longest_heatwave_days !==
          null && (
          <p className="mt-1 text-xs text-slate-500">
            Longest:{" "}
            {result.longest_heatwave_days}{" "}
            days
          </p>
        )}
      </td>

      <td className="px-4 py-4">
        {result.sampled_day_count ?? "—"}

        {result.eligible_sample_count !==
          null && (
          <p className="mt-1 text-xs text-slate-500">
            {
              result.eligible_sample_count
            }{" "}
            eligible
          </p>
        )}
      </td>

      <td className="px-4 py-4 text-xs text-slate-400">
        {formatDateTime(
          result.last_heartbeat_at,
        )}
      </td>
    </tr>
  );
}


function CityDetailPanel({
  result,
  heatwaveAvailable,
  onClose,
}: {
  result: GlobalCityResult;
  heatwaveAvailable: boolean;
  onClose: () => void;
}) {
  return (
    <section className="mt-8 rounded-2xl border border-cyan-900 bg-slate-900 p-6">
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div>
          <p className="text-sm font-medium text-cyan-400">
            City Analytics
          </p>

          <h2 className="mt-1 text-2xl font-semibold">
            {result.city_name},{" "}
            {result.country}
          </h2>

          <p className="mt-2 text-sm text-slate-500">
            {result.latitude.toFixed(4)},{" "}
            {result.longitude.toFixed(4)}
          </p>
        </div>

        <button
          type="button"
          onClick={onClose}
          className="rounded-lg border border-slate-700 px-4 py-2 text-sm text-slate-300 hover:bg-slate-800"
        >
          Close
        </button>
      </div>

      <div className="mt-6 grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <Metric
          label="Skin Cooling P50"
          value={formatNumber(
            result.skin_improvement_p50_c,
            " °C",
          )}
        />

        <Metric
          label="Skin Cooling P90"
          value={formatNumber(
            result.skin_improvement_p90_c,
            " °C",
          )}
        />

        <Metric
          label="Skin Cooling P95"
          value={formatNumber(
            result.skin_improvement_p95_c,
            " °C",
          )}
        />

        <Metric
          label="Maximum Skin Cooling"
          value={formatNumber(
            result
              .maximum_skin_improvement_c,
            " °C",
          )}
        />

        <Metric
          label="Core Cooling P50"
          value={formatNumber(
            result.core_improvement_p50_c,
            " °C",
          )}
        />

        <Metric
          label="Core Cooling P90"
          value={formatNumber(
            result.core_improvement_p90_c,
            " °C",
          )}
        />

        <Metric
          label="Core Cooling P95"
          value={formatNumber(
            result.core_improvement_p95_c,
            " °C",
          )}
        />

        <Metric
          label="Effective Cooling"
          value={formatNumber(
            result.effective_cooling_hours,
            " hours",
          )}
        />
      </div>

      <MonthlyResultsTable
        result={result}
      />

      <HeatwaveResults
        events={
          result.heatwave_events ?? []
        }
        available={heatwaveAvailable}
      />
    </section>
  );
}


function MonthlyResultsTable({
  result,
}: {
  result: GlobalCityResult;
}) {
  const monthlyResults =
    result.monthly_results ?? [];

  return (
    <div className="mt-8">
      <h3 className="text-lg font-semibold">
        Monthly Results
      </h3>

      {monthlyResults.length === 0 ? (
        <p className="mt-3 text-sm text-slate-500">
          No monthly results are available.
        </p>
      ) : (
        <div className="mt-4 overflow-x-auto rounded-xl border border-slate-800">
          <table className="min-w-[70rem] w-full text-left text-sm">
            <thead className="bg-slate-950 text-xs uppercase tracking-wide text-slate-500">
              <tr>
                <th className="px-4 py-3">
                  Month
                </th>

                <th className="px-4 py-3">
                  Samples
                </th>

                <th className="px-4 py-3">
                  Eligible
                </th>

                <th className="px-4 py-3">
                  Exposure
                </th>

                <th className="px-4 py-3">
                  Adaptation
                </th>

                <th className="px-4 py-3">
                  Average Skin
                </th>

                <th className="px-4 py-3">
                  Average Core
                </th>

                <th className="px-4 py-3">
                  Maximum Skin
                </th>

                <th className="px-4 py-3">
                  Weighted Days
                </th>
              </tr>
            </thead>

            <tbody>
              {monthlyResults.map(
                (month) => (
                  <tr
                    key={month.month}
                    className="border-t border-slate-800"
                  >
                    <td className="px-4 py-3 font-medium">
                      {formatMonth(
                        month.month,
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {
                        month.sampled_day_count
                      }
                    </td>

                    <td className="px-4 py-3">
                      {
                        month.eligible_sample_count
                      }
                    </td>

                    <td className="px-4 py-3">
                      {formatNumber(
                        month
                          .exposure_coverage_percent,
                        "%",
                      )}
                    </td>

                    <td className="px-4 py-3 text-cyan-300">
                      {formatNumber(
                        month
                          .climate_adaptation_rate_percent,
                        "%",
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {formatNumber(
                        month
                          .average_skin_improvement_c,
                        " °C",
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {formatNumber(
                        month
                          .average_core_improvement_c,
                        " °C",
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {formatNumber(
                        month
                          .maximum_skin_improvement_c,
                        " °C",
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {
                        month.evaluated_weighted_days
                      }{" "}
                      /{" "}
                      {
                        month.total_weighted_days
                      }
                    </td>
                  </tr>
                ),
              )}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}


function HeatwaveResults({
  events,
  available,
}: {
  events: HeatwaveEvent[];
  available: boolean;
}) {
  return (
    <div className="mt-8">
      <h3 className="text-lg font-semibold">
        Heatwave Events
      </h3>

      {!available ? (
        <p className="mt-3 text-sm text-amber-300">
          Heatwave analysis is unavailable for
          this sampling configuration.
        </p>
      ) : events.length === 0 ? (
        <p className="mt-3 text-sm text-slate-500">
          No qualifying heatwave event was
          detected.
        </p>
      ) : (
        <div className="mt-4 overflow-x-auto rounded-xl border border-slate-800">
          <table className="min-w-[65rem] w-full text-left text-sm">
            <thead className="bg-slate-950 text-xs uppercase tracking-wide text-slate-500">
              <tr>
                <th className="px-4 py-3">
                  Start
                </th>

                <th className="px-4 py-3">
                  End
                </th>

                <th className="px-4 py-3">
                  Duration
                </th>

                <th className="px-4 py-3">
                  Mean Maximum Air
                </th>

                <th className="px-4 py-3">
                  Peak Air
                </th>

                <th className="px-4 py-3">
                  Mean Skin Cooling
                </th>

                <th className="px-4 py-3">
                  P90 Skin Cooling
                </th>

                <th className="px-4 py-3">
                  Beneficial Days
                </th>
              </tr>
            </thead>

            <tbody>
              {events.map(
                (event, index) => (
                  <tr
                    key={
                      `${event.start_date_local}-` +
                      `${event.end_date_local}-` +
                      index
                    }
                    className="border-t border-slate-800"
                  >
                    <td className="px-4 py-3">
                      {formatDate(
                        event.start_date_local,
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {formatDate(
                        event.end_date_local,
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {event.duration_days} days
                    </td>

                    <td className="px-4 py-3">
                      {formatNumber(
                        event
                          .mean_maximum_air_temperature_c,
                        " °C",
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {formatNumber(
                        event
                          .peak_air_temperature_c,
                        " °C",
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {formatNumber(
                        event
                          .mean_skin_improvement_c,
                        " °C",
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {formatNumber(
                        event
                          .p90_skin_improvement_c,
                        " °C",
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {
                        event.beneficial_day_count
                      }
                    </td>
                  </tr>
                ),
              )}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}


function Metric({
  label,
  value,
}: {
  label: string;
  value: string;
}) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-5">
      <p className="text-sm text-slate-400">
        {label}
      </p>

      <p className="mt-2 break-words text-xl font-semibold text-cyan-300">
        {value}
      </p>
    </div>
  );
}


function StatusBadge({
  status,
}: {
  status: string;
}) {
  return (
    <span
      className={
        "inline-flex rounded-full border " +
        "px-2.5 py-1 text-xs font-medium " +
        getStatusColorClass(status)
      }
    >
      {formatLabel(status)}
    </span>
  );
}


function getStatusColorClass(
  status: string,
): string {
  switch (status) {
    case "completed":
      return (
        "border-emerald-800 " +
        "bg-emerald-950 " +
        "text-emerald-300"
      );

    case "running":
      return (
        "border-cyan-800 " +
        "bg-cyan-950 " +
        "text-cyan-300"
      );

    case "queued":
      return (
        "border-slate-700 " +
        "bg-slate-900 " +
        "text-slate-300"
      );

    case "failed":
      return (
        "border-red-800 " +
        "bg-red-950 " +
        "text-red-300"
      );

    case "cancelled":
      return (
        "border-slate-700 " +
        "bg-slate-950 " +
        "text-slate-400"
      );

    default:
      return (
        "border-amber-800 " +
        "bg-amber-950 " +
        "text-amber-300"
      );
  }
}


function formatNumber(
  value: number | null | undefined,
  suffix: string,
): string {
  if (
    value === null ||
    value === undefined ||
    !Number.isFinite(value)
  ) {
    return "—";
  }

  return `${value.toFixed(2)}${suffix}`;
}


function formatLabel(
  value: string,
): string {
  if (!value) {
    return "—";
  }

  return value
    .split("_")
    .map(
      (word) =>
        word.charAt(0).toUpperCase() +
        word.slice(1),
    )
    .join(" ");
}


function formatMonth(
  month: number,
): string {
  if (
    !Number.isInteger(month) ||
    month < 1 ||
    month > 12
  ) {
    return String(month);
  }

  return new Intl.DateTimeFormat(
    "en-US",
    {
      month: "long",
      timeZone: "UTC",
    },
  ).format(
    new Date(
      Date.UTC(2023, month - 1, 1),
    ),
  );
}


function formatDate(
  value: string | null,
): string {
  if (!value) {
    return "—";
  }

  const date = new Date(value);

  if (
    Number.isNaN(date.getTime())
  ) {
    return value;
  }

  return new Intl.DateTimeFormat(
    "en-US",
    {
      year: "numeric",
      month: "short",
      day: "numeric",
    },
  ).format(date);
}


function formatDateTime(
  value: string | null,
): string {
  if (!value) {
    return "—";
  }

  const date = new Date(value);

  if (
    Number.isNaN(date.getTime())
  ) {
    return value;
  }

  return new Intl.DateTimeFormat(
    "en-US",
    {
      year: "numeric",
      month: "short",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    },
  ).format(date);
}


function calculateMean(
  values: Array<
    number | null | undefined
  >,
): number | null {
  const validValues = values.filter(
    (value): value is number =>
      value !== null &&
      value !== undefined &&
      Number.isFinite(value),
  );

  if (validValues.length === 0) {
    return null;
  }

  return (
    validValues.reduce(
      (total, value) =>
        total + value,
      0,
    ) / validValues.length
  );
}


function clampProgress(
  value: number,
): number {
  if (!Number.isFinite(value)) {
    return 0;
  }

  return Math.max(
    0,
    Math.min(100, value),
  );
}


function getErrorMessage(
  error: unknown,
  fallback: string,
): string {
  return error instanceof Error
    ? error.message
    : fallback;
}
```

### File: `frontend/src/app/global-analysis/page.tsx`
```tsx
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

import { MaterialInputFields } from "@/components/simulation/material-input-fields";

import type {
  AnalysisResolution,
  ExecutionProfile,
  ExposureMatchMode,
  GlobalBatchCreate,
  GlobalBatchEstimate,
  GlobalCity,
} from "@/types/global-batch";
import { DEFAULT_ENVIRONMENT_ASSUMPTIONS } from "@/lib/environment-assumptions";

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
  environment_assumptions: DEFAULT_ENVIRONMENT_ASSUMPTIONS,

  person: {
    met: 2,
    body_mass_kg: 70,            // ← 加這行
    body_surface_area_m2: 1.8,
    initial_core_temperature_c: 36.8,
    initial_skin_temperature_c: 33.7,
    position: "standing",
  },

  control_material: {
    name: "Conventional clothing",
    clothing_insulation_clo: 0.5,
    clothing_area_factor: null,  // ← 加這行
    solar_reflectance: 0.3,
    solar_transmittance: 0,
    infrared_emissivity: 0.9,
    projected_solar_area_factor: 0.25,
  },

  rc_material: {
    name: "Radiative cooling clothing",
    clothing_insulation_clo: 0.4,
    clothing_area_factor: null,  // ← 加這行
    solar_reflectance: 0.92,
    solar_transmittance: 0,
    infrared_emissivity: 0.95,
    projected_solar_area_factor: 0.25,
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
            Global Analysis
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

          <div className="mt-8 grid gap-6 lg:grid-cols-2">
            <section className="rounded-xl border border-slate-800 bg-slate-950/50 p-5">
              <h2 className="text-lg font-semibold">Control Clothing</h2>
              <div className="mt-4">
                <MaterialInputFields
                  material={request.control_material}
                  showName
                  enableLibrary
                  disabled={submitting}
                  onChange={(control_material) =>
                    setRequest((current) => ({ ...current, control_material }))
                  }
                />
              </div>
            </section>

            <section className="rounded-xl border border-slate-800 bg-slate-950/50 p-5">
              <h2 className="text-lg font-semibold">Radiative Cooling Clothing</h2>
              <div className="mt-4">
                <MaterialInputFields
                  material={request.rc_material}
                  showName
                  enableLibrary
                  disabled={submitting}
                  onChange={(rc_material) =>
                    setRequest((current) => ({ ...current, rc_material }))
                  }
                />
              </div>
            </section>
          </div>

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

      <p className="mt-2 wrap-break-word font-semibold text-cyan-300">
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
```

### File: `frontend/src/app/globals.css`
```css
@import "tailwindcss";

:root {
  --background: #ffffff;
  --foreground: #171717;
}

@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --font-sans: var(--font-geist-sans);
  --font-mono: var(--font-geist-mono);
}

@media (prefers-color-scheme: dark) {
  :root {
    --background: #0a0a0a;
    --foreground: #ededed;
  }
}

body {
  background: var(--background);
  color: var(--foreground);
  font-family: Arial, Helvetica, sans-serif;
}

```

### File: `frontend/src/app/layout.tsx`
```tsx
import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";

import { NavBar } from "@/components/layout/NavBar";

import "./globals.css";
import "maplibre-gl/dist/maplibre-gl.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title:
    "Global Radiative Cooling Clothing Climate Adaptation Simulation Platform",
  description:
    "A platform for evaluating radiative cooling clothing under global climate conditions.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
    >
      <body
        suppressHydrationWarning
        className="flex min-h-full flex-col"
      >
        <NavBar />

        <main className="flex-1">
          {children}
        </main>
      </body>
    </html>
  );
}
```

### File: `frontend/src/app/materials/[materialId]/page.tsx`
```tsx
"use client";

import {
  useEffect,
  useState,
} from "react";
import { useParams } from "next/navigation";

import Link from "next/link";
import { getMaterial, getSimulationJobs, uploadMaterialSpectrum } from "@/lib/api-client";
import type { SimulationJob } from "@/types/simulation";
import type {
  Material,
} from "@/types/material";

type SpectrumType =
  | "solar_reflectance"
  | "solar_transmittance"
  | "mir_emissivity"
  | "mir_transmittance";

export default function MaterialDetailPage() {
  const parameters =
    useParams<{ materialId: string }>();

  const materialId = parameters.materialId;

  return (
    <MaterialDetailContent
      key={materialId}
      materialId={materialId}
    />
  );
}

function MaterialDetailContent({
  materialId,
}: {
  materialId: string;
}) {
  const [material, setMaterial] =
    useState<Material | null>(null);

  const [file, setFile] =
    useState<File | null>(null);

  const [spectrumType, setSpectrumType] =
    useState<SpectrumType>(
      "mir_emissivity",
    );

  const [message, setMessage] =
    useState("");

  const [error, setError] =
    useState("");

  const [loading, setLoading] =
    useState(true);

  const [uploading, setUploading] =
    useState(false);

  useEffect(() => {
    let ignore = false;

    getMaterial(materialId)
      .then((response) => {
        if (!ignore) {
          setMaterial(response);
        }
      })
      .catch((caughtError: unknown) => {
        if (!ignore) {
          setError(
            caughtError instanceof Error
              ? caughtError.message
              : "Loading material failed",
          );
        }
      })
      .finally(() => {
        if (!ignore) {
          setLoading(false);
        }
      });

    return () => {

      ignore = true;
    };
  }, [materialId]);

  async function handleUpload() {
    const latestVersion =
      material?.versions.at(-1);

    if (!file || !latestVersion) {
      return;
    }

    setUploading(true);
    setMessage("");
    setError("");

    try {
      await uploadMaterialSpectrum(
        latestVersion.id,
        spectrumType,
        file,
      );

      const refreshedMaterial =
        await getMaterial(materialId);

      setMaterial(refreshedMaterial);
      setFile(null);
      setMessage("Spectrum uploaded successfully");
    } catch (caughtError) {
      setError(
        caughtError instanceof Error
          ? caughtError.message
          : "Upload failed",
      );
    } finally {
      setUploading(false);
    }
  }

  if (loading) {
    return (
      <main className="min-h-screen bg-slate-950 p-10 text-white">
        Loading material…
      </main>
    );
  }

  if (error && !material) {
    return (
      <main className="min-h-screen bg-slate-950 p-10 text-white">
        <div className="rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">
          {error}
        </div>
      </main>
    );
  }

  if (!material) {
    return (
      <main className="min-h-screen bg-slate-950 p-10 text-white">
        Material not found
      </main>
    );
  }

  const latestVersion =
    material.versions.at(-1);

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-6xl px-6 py-10">
        <header>
          <p className="text-sm text-cyan-400">
            Material Detail
          </p>

          <h1 className="mt-2 text-3xl font-bold">
            {material.name}
          </h1>

          <p className="mt-2 text-slate-400">
            {material.description ||
              "Material description not available"}
          </p>

          <div className="mt-4 flex flex-wrap gap-4 text-sm text-slate-500">
            <span>
              Slug：{material.slug}
            </span>

            <span>
              Institution:
              {material.institution ?? "—"}
            </span>
          </div>
        </header>

        {error && (
          <div className="mt-6 rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">
            {error}
          </div>
        )}

        {message && (
          <div className="mt-6 rounded-lg border border-emerald-900 bg-emerald-950 p-4 text-emerald-300">
            {message}
          </div>
        )}

        <section className="mt-8 space-y-5">
          {material.versions.map(
            (version) => (
              <article
                key={version.id}
                className="rounded-2xl border border-slate-800 bg-slate-900 p-6"
              >
                <div className="flex flex-wrap items-center justify-between gap-4">
                  <h2 className="text-xl font-semibold">
                    Version{" "}
                    {version.version_number}
                  </h2>

                  <span className="rounded-full bg-slate-800 px-3 py-1 text-xs text-slate-300">
                    {version.mode}
                  </span>
                </div>

                <div className="mt-4 grid gap-4 sm:grid-cols-2 md:grid-cols-5">
                  <Metric
                    label="solar reflectance"
                    value={
                      version.solar_reflectance
                    }
                  />

                  <Metric
                    label="infrared emissivity"
                    value={
                      version.infrared_emissivity
                    }
                  />

                  <Metric
                    label="infrared transmittance"
                    value={
                      version.infrared_transmittance
                    }
                  />

                  <Metric
                    label="clothing insulation"
                    value={
                      version.clothing_insulation_clo
                    }
                    unit="clo"
                  />

                  <Metric
                    label="clothing area factor"
                    value={version.clothing_area_factor}
                    fallback="Derived from clo"
                  />

                  <Metric
                    label="evaporative resistance"
                    value={version.evaporative_resistance_m2pa_w}
                    unit="m²·Pa/W"
                    fallback="Derived from clo"
                    digits={1}
                  />
                </div>

                <div className="mt-5">
                  <p className="text-sm text-slate-400">
                    Spectra uploaded:
                    {version.spectra.length}
                  </p>

                  {version.spectra.length >
                    0 && (
                    <ul className="mt-3 space-y-2">
                      {version.spectra.map(
                        (spectrum) => (
                          <li
                            key={spectrum.id}
                            className="rounded-lg bg-slate-950 px-4 py-3 text-sm text-slate-300"
                          >
                            <span className="font-medium text-cyan-300">
                              {
                                spectrum.spectrum_type
                              }
                            </span>

                            <span className="ml-3 text-slate-500">
                              {
                                spectrum.point_count
                              }{" "}
                              data points
                            </span>

                            <span className="ml-3 text-slate-500">
                              {
                                spectrum.minimum_wavelength_um
                              }
                              –
                              {
                                spectrum.maximum_wavelength_um
                              }{" "}
                              μm
                            </span>
                          </li>
                        ),
                      )}
                    </ul>
                  )}
                </div>
                <ProvenanceTable sources={version.parameter_sources ?? null} />
                <LinkedSimulations versionId={version.id} />
              </article>
            ),
          )}
        </section>

        {latestVersion && (
          <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">
              Upload Version{" "}
              {latestVersion.version_number}{" "}
              Spectra
            </h2>

            <p className="mt-2 text-sm text-slate-400">
              CSV must contain
              wavelength_um and value
              two columns.
            </p>

            <div className="mt-5 flex flex-wrap gap-4">
              <select
                value={spectrumType}
                disabled={uploading}
                onChange={(event) =>
                  setSpectrumType(
                    event.target
                      .value as SpectrumType,
                  )
                }
                className="rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 disabled:opacity-50"
              >
                <option value="solar_reflectance">
                  Solar Reflectance Spectra
                </option>

                <option value="solar_transmittance">
                  Solar Transmittance Spectra
                </option>

                <option value="mir_emissivity">
                  Infrared Emissivity Spectra
                </option>

                <option value="mir_transmittance">
                  Infrared Transmittance Spectra
                </option>
              </select>

              <input
                key={
                  file?.name ??
                  "empty-file-input"
                }
                type="file"
                accept=".csv,text/csv"
                disabled={uploading}
                onChange={(event) => {
                  setFile(
                    event.target.files?.[0] ??
                      null,
                  );
                  setMessage("");
                  setError("");
                }}
                className="rounded-lg border border-slate-700 p-2 disabled:opacity-50"
              />

              <button
                type="button"
                onClick={handleUpload}
                disabled={!file || uploading}
                className="rounded-lg bg-cyan-400 px-5 py-2 font-semibold text-slate-950 disabled:cursor-not-allowed disabled:opacity-50"
              >
                {uploading
                  ? "Uploading…"
                  : "Upload"}
              </button>
            </div>

            {file && (
              <p className="mt-4 text-sm text-slate-400">
                File selected: {file.name}
              </p>
            )}
          </section>
        )}
      </div>
    </main>
  );
}

function Metric({
  label,
  value,
  unit,
  fallback = "—",
  digits = 3,
}: {
  label: string;
  value: number | null | undefined;
  unit?: string;
  fallback?: string;
  digits?: number;
}) {
  const hasValue = typeof value === "number" && Number.isFinite(value);

  return (
    <div className="rounded-lg bg-slate-950 p-4">
      <p className="text-sm text-slate-400">{label}</p>

      <p className="mt-1 text-xl font-semibold text-cyan-300">
        {hasValue ? value.toFixed(digits) : fallback}

        {hasValue && unit && (
          <span className="ml-1 text-sm font-normal text-slate-400">{unit}</span>
        )}
      </p>
    </div>
  );
}

function ProvenanceTable({
  sources,
}: {
  sources: Record<string, { source_type: string; reference?: string | null; note?: string | null }> | null;
}) {
  const entries = Object.entries(sources ?? {});

  if (entries.length === 0) {
    return (
      <p className="mt-5 text-sm text-slate-500">
        No per-parameter provenance recorded for this version.
      </p>
    );
  }

  return (
    <div className="mt-5">
      <p className="text-sm text-slate-400">Parameter provenance</p>
      <table className="mt-2 w-full text-left text-sm">
        <tbody>
          {entries.map(([field, source]) => (
            <tr key={field} className="border-t border-slate-800">
              <td className="py-2 pr-4 font-mono text-slate-300">{field}</td>
              <td className="py-2 pr-4 text-cyan-300">{source.source_type}</td>
              <td className="py-2 text-slate-400">{source.reference ?? "—"}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function LinkedSimulations({ versionId }: { versionId: string }) {
  const [jobs, setJobs] = useState<SimulationJob[] | null>(null);

  useEffect(() => {
    let ignore = false;

    getSimulationJobs(10, 0, versionId)
      .then((response) => {
        if (!ignore) setJobs(response.items);
      })
      .catch(() => {
        if (!ignore) setJobs([]);
      });

    return () => {
      ignore = true;
    };
  }, [versionId]);

  if (jobs === null || jobs.length === 0) {
    return null;
  }

  return (
    <div className="mt-5">
      <p className="text-sm text-slate-400">Recent simulations using this version</p>
      <ul className="mt-2 flex flex-wrap gap-2">
        {jobs.map((job) => (
          <li key={job.id}>
            <Link
              href={`/simulations/${job.id}`}
              className="rounded-full border border-slate-700 px-3 py-1 font-mono text-xs text-cyan-300 hover:bg-slate-800"
            >
              {job.id.slice(0, 8)} · {job.city_id} · {job.status}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
```

### File: `frontend/src/app/materials/new/page.tsx`
```tsx
"use client";

import { type FormEvent, useState } from "react";
import { useRouter } from "next/navigation";
import {ProvenanceEditor} from "@/components/materials/provenance-editor";
import { OptionalNumberField } from "@/components/forms/number-field";
import { createMaterial } from "@/lib/api-client";
import type { MaterialCreate, MaterialVersionInput } from "@/types/material";


const initialMaterial: MaterialCreate = {
  name: "",
  slug: "",
  description: "",
  institution: "",
  initial_version: {
    mode: "opaque_emitter",
    clothing_insulation_clo: 0.4,
    clothing_area_factor: null,
    evaporative_resistance_m2pa_w: 18,
    solar_reflectance: 0.92,
    solar_transmittance: 0,
    infrared_emissivity: 0.95,
    infrared_transmittance: 0,
    projected_solar_area_factor: 0.25,
    areal_density_g_m2: 150,
    specific_heat_j_kgk: 1300,
    source_type: "manual",
    source_reference: "",
    notes: "",
  },
};


export default function NewMaterialPage() {
  const router = useRouter();

  const [material, setMaterial] =
    useState(initialMaterial);

  const [loading, setLoading] =
    useState(false);

  const [error, setError] =
    useState("");

  async function handleSubmit(
    event: FormEvent,
  ) {
    event.preventDefault();
    setLoading(true);
    setError("");

    try {
      const created =
        await createMaterial(material);

      router.push(
        `/materials/${created.id}`,
      );
    } catch (caughtError) {
      setError(
        caughtError instanceof Error
          ? caughtError.message
          : "Failed to load materials.",
      );
    } finally {
      setLoading(false);
    }
  }

  function updateVersion<K extends keyof MaterialVersionInput>(
    field: K,
    value: MaterialVersionInput[K],
  ) {
    setMaterial({
      ...material,
      initial_version: { ...material.initial_version, [field]: value },
    });
  }

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-4xl px-6 py-10">
        <h1 className="text-3xl font-bold">
          New Material
        </h1>

        <form
          onSubmit={handleSubmit}
          className="mt-8 space-y-8"
        >
          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">
              Basic Information
            </h2>

            <div className="mt-5 grid gap-5 md:grid-cols-2">
              <TextInput
                label="Material Name"
                value={material.name}
                onChange={(value) =>
                  setMaterial({
                    ...material,
                    name: value,
                  })
                }
              />

              <TextInput
                label="Slug"
                value={material.slug}
                onChange={(value) =>
                  setMaterial({
                    ...material,
                    slug: value
                      .toLowerCase()
                      .replace(
                        /[^a-z0-9]+/g,
                        "-",
                      )
                      .replace(/^-|-$/g, ""),
                  })
                }
              />

              <TextInput
                label="Institution"
                value={
                  material.institution ?? ""
                }
                onChange={(value) =>
                  setMaterial({
                    ...material,
                    institution: value,
                  })
                }
              />

              <TextInput
                label="Source Reference"
                value={
                  material.initial_version
                    .source_reference ?? ""
                }
                onChange={(value) =>
                  updateVersion(
                    "source_reference",
                    value,
                  )
                }
              />
            </div>
          </section>

          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">
              Initial Physical Parameters
            </h2>

            <div className="mt-5 grid gap-5 md:grid-cols-2">
              <NumberInput
                label="Clothing Insulation (clo)"
                value={
                  material.initial_version
                    .clothing_insulation_clo
                }
                onChange={(value) =>
                  updateVersion(
                    "clothing_insulation_clo",
                    value,
                  )
                }
              />

              <OptionalNumberField
                label="Clothing Area Factor (f_cl)"
                value={material.initial_version.clothing_area_factor}
                placeholder="Derived from clo"
                min={1}
                max={2}
                step={0.01}
                hint="Leave empty to let the backend derive f_cl from clo."
                onChange={(value) => updateVersion("clothing_area_factor", value)}
              />

              <OptionalNumberField
                label="Evaporative Resistance (Re,cl)"
                suffix="m²·Pa/W"
                value={material.initial_version.evaporative_resistance_m2pa_w}
                placeholder="Derived from clo"
                min={0} max={1000} step={0.5}
                onChange={(value) => updateVersion("evaporative_resistance_m2pa_w", value)}
              />
              <NumberInput
                label="Projected Solar Area Factor"
                value={material.initial_version.projected_solar_area_factor}
                onChange={(value) => updateVersion("projected_solar_area_factor", value)}
              />


              <NumberInput
                label="Solar Reflectance"
                value={
                  material.initial_version
                    .solar_reflectance
                }
                onChange={(value) =>
                  updateVersion(
                    "solar_reflectance",
                    value,
                  )
                }
              />

              <NumberInput
                label="Solar Transmittance"
                value={
                  material.initial_version
                    .solar_transmittance
                }
                onChange={(value) =>
                  updateVersion(
                    "solar_transmittance",
                    value,
                  )
                }
              />

              <NumberInput
                label="Infrared Emissivity"
                value={
                  material.initial_version
                    .infrared_emissivity
                }
                onChange={(value) =>
                  updateVersion(
                    "infrared_emissivity",
                    value,
                  )
                }
              />

              <NumberInput
                label="Infrared Transmittance"
                value={
                  material.initial_version
                    .infrared_transmittance
                }
                onChange={(value) =>
                  updateVersion(
                    "infrared_transmittance",
                    value,
                  )
                }
              />

              <NumberInput
                label="Areal Density (g/m²)"
                value={
                  material.initial_version
                    .areal_density_g_m2 ?? 0
                }
                onChange={(value) =>
                  updateVersion(
                    "areal_density_g_m2",
                    value,
                  )
                }
              />
            </div>
          </section>

          <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">Parameter Provenance</h2>
            <p className="mt-2 text-sm text-slate-400">
              Record where each value came from. Provenance travels with the
              version into every simulation that references it.
            </p>
            <div className="mt-5">
              <ProvenanceEditor
                sources={material.initial_version.parameter_sources ?? null}
                values={material.initial_version}
                disabled={loading}
                onChange={(sources) => updateVersion("parameter_sources", sources)}
              />
            </div>
          </section>

          {error && (
            <div className="rounded-lg bg-red-950 p-4 text-red-300">
              {error}
            </div>
          )}

          <button
            type="submit"
            disabled={loading}
            className="rounded-lg bg-cyan-400 px-7 py-3 font-semibold text-slate-950 disabled:opacity-50"
          >
            {loading
              ? "Creating Material…"
              : "Create Material"}
          </button>
        </form>
      </div>
    </main>
  );
}


function TextInput({
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
        required
        value={value}
        onChange={(event) =>
          onChange(event.target.value)
        }
        className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2"
      />
    </label>
  );
}


function NumberInput({
  label,
  value,
  onChange,
}: {
  label: string;
  value: number;
  onChange: (value: number) => void;
}) {
  return (
    <label>
      <span className="mb-2 block text-sm text-slate-300">
        {label}
      </span>

      <input
        type="number"
        min={0}
        step={0.01}
        value={value}
        onChange={(event) =>
          onChange(
            Number(event.target.value),
          )
        }
        className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2"
      />
    </label>
  );
}
```

### File: `frontend/src/app/materials/page.tsx`
```tsx
"use client";

import Link from "next/link";
import {
  FormEvent,
  useEffect,
  useState,
} from "react";

import { getMaterials } from "@/lib/api-client";
import type {
  MaterialListItem,
} from "@/types/material";

export default function MaterialsPage() {
  const [materials, setMaterials] =
    useState<MaterialListItem[]>([]);

  const [search, setSearch] =
    useState("");

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState("");

  useEffect(() => {
    let ignore = false;

    getMaterials()
      .then((response) => {
        if (!ignore) {
          setMaterials(response.items);
        }
      })
      .catch((caughtError: unknown) => {
        if (!ignore) {
          setError(
            caughtError instanceof Error
              ? caughtError.message
              : "Failed to load materials.",
          );
        }
      })
      .finally(() => {
        if (!ignore) {
          setLoading(false);
        }
      });

    return () => {
      ignore = true;
    };
  }, []);

  async function handleSearchSubmit(
    event: FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault();

    setLoading(true);
    setError("");

    try {
      const response = await getMaterials(
        search,
      );

      setMaterials(response.items);
    } catch (caughtError) {
      setError(
        caughtError instanceof Error
          ? caughtError.message
          : "Failed to load materials.",
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl px-6 py-10">
        <header className="flex flex-wrap items-center justify-between gap-4">
          <div>
            <p className="text-sm text-cyan-400">
              Material Database
            </p>

            <h1 className="mt-2 text-3xl font-bold">
              Radiative Cooling Materials
            </h1>
          </div>

          <Link
            href="/materials/new"
            className="rounded-lg bg-cyan-400 px-5 py-2.5 font-semibold text-slate-950"
          >
            New materials
          </Link>
        </header>

        <form
          className="mt-8 flex gap-3"
          onSubmit={handleSearchSubmit}
        >
          <input
            value={search}
            onChange={(event) =>
              setSearch(event.target.value)
            }
            placeholder="Search materials"
            className="max-w-md flex-1 rounded-lg border border-slate-700 bg-slate-900 px-4 py-2"
          />

          <button
            type="submit"
            disabled={loading}
            className="rounded-lg border border-slate-700 px-5 py-2 disabled:cursor-not-allowed disabled:opacity-50"
          >
            {loading ? "Loading…" : "Search"}
          </button>
        </form>

        {error && (
          <div className="mt-6 rounded-lg bg-red-950 p-4 text-red-300">
            {error}
          </div>
        )}

        <section className="mt-8 overflow-hidden rounded-2xl border border-slate-800">
          <table className="w-full text-left">
            <thead className="bg-slate-900 text-sm text-slate-400">
              <tr>
                <th className="px-5 py-4">
                  Material
                </th>
                <th className="px-5 py-4">
                  Institution
                </th>
                <th className="px-5 py-4">
                  Latest Version
                </th>
                <th className="px-5 py-4">
                  Created At
                </th>
              </tr>
            </thead>

            <tbody>
              {materials.map((material) => (
                <tr
                  key={material.id}
                  className="border-t border-slate-800 bg-slate-950"
                >
                  <td className="px-5 py-4">
                    <Link
                      href={`/materials/${material.id}`}
                      className="font-medium text-cyan-300 hover:underline"
                    >
                      {material.name}
                    </Link>

                    <p className="mt-1 text-xs text-slate-500">
                      {material.slug}
                    </p>
                  </td>

                  <td className="px-5 py-4 text-slate-300">
                    {material.institution ?? "—"}
                  </td>

                  <td className="px-5 py-4">
                    {material.latest_version_number
                      ? `v${material.latest_version_number}`
                      : "—"}
                  </td>

                  <td className="px-5 py-4 text-sm text-slate-400">
                    {new Date(
                      material.created_at,
                    ).toLocaleString()}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>

          {loading && (
            <div className="p-10 text-center text-slate-400">
              Loading…
            </div>
          )}

          {!loading &&
            materials.length === 0 && (
              <div className="p-10 text-center text-slate-400">
                No materials available.
              </div>
            )}
        </section>
      </div>
    </main>
  );
}
```

### File: `frontend/src/app/page.tsx`
```tsx
import { redirect } from "next/navigation";

export default function HomePage() {
  redirect("/simulations");
}
```

### File: `frontend/src/app/simulations/[jobId]/page.tsx`
```tsx
"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";

import { HeatFluxChart } from "@/components/charts/heat-flux-chart";
import { PhysiologyChart } from "@/components/charts/physiology-chart";
import { TemperatureChart } from "@/components/charts/temperature-chart";
import { WeatherChart } from "@/components/charts/weather-chart";
import { ModelProvenancePanel } from "@/components/simulation/model-provenance-panel";
import { ModelQualityPanel } from "@/components/simulation/model-quality-panel";
import {
  cancelSimulationJob,
  getSimulationEventsUrl,
  getSimulationExportUrl,
  getSimulationJob,
  getSimulationResult,
} from "@/lib/api-client";
import type {
  SimulationJob,
  WeatherSimulationResponse,
} from "@/types/simulation";

const terminalStatuses =
  new Set<SimulationJob["status"]>([
    "completed",
    "failed",
    "cancelled",
  ]);


const stageLabels: Record<string, string> = {
  queued: "Waiting for computing resources",
  initializing: "Initializing model",
  downloading_weather:
    "Downloading historical weather data",
  running_control_simulation:
    "Running control simulation",
  running_radiative_cooling_simulation:
    "Running radiative cooling simulation",
  generating_summary:
    "Generating summary",
  saving_result:
    "Saving result",
  completed: "Simulation completed",
  failed: "Simulation failed",
  cancelling: "Cancelling simulation",
  waiting_for_cooperative_cancel:
    "Waiting for cooperative cancel",
  cancelled: "Cancelled",
};


export default function SimulationJobPage() {
  const parameters =
    useParams<{ jobId: string }>();

  const jobId = parameters.jobId;

  const [job, setJob] =
    useState<SimulationJob | null>(null);

  const [result, setResult] =
    useState<WeatherSimulationResponse | null>(
      null,
    );

  const [error, setError] =
    useState("");

  const [cancelling, setCancelling] =
    useState(false);


  useEffect(() => {
    let ignore = false;

    function handleJobUpdate(
      nextJob: SimulationJob,
    ) {
      if (ignore) {
        return;
      }

      setJob((currentJob) => {
        if (!currentJob) {
          return nextJob;
        }

        return {
          ...currentJob,
          ...nextJob,
        };
      });
    }

    function handleRequestError(
      caughtError: unknown,
    ) {
      if (ignore) {
        return;
      }

      setError(
        caughtError instanceof Error
          ? caughtError.message
          : "Failed to load simulation job",
      );
    }

    getSimulationJob(jobId)
      .then(handleJobUpdate)
      .catch(handleRequestError);

    const eventSource = new EventSource(
      getSimulationEventsUrl(jobId),
    );

    eventSource.addEventListener(
      "progress",
      (event) => {
        try {
          const nextJob = JSON.parse(
            (event as MessageEvent<string>).data,
          ) as SimulationJob;

          handleJobUpdate(nextJob);
        } catch {
          if (!ignore) {
            setError("Failed to parse job progress data");
          }
        }
      },
    );

    eventSource.addEventListener(
      "terminal",
      (event) => {
        try {
          const nextJob = JSON.parse(
            (event as MessageEvent<string>).data,
          ) as SimulationJob;

          handleJobUpdate(nextJob);
        } catch {
          if (!ignore) {
            setError("Failed to parse job terminal state");
          }
        } finally {
          eventSource.close();
        }
      },
    );

    eventSource.onerror = () => {
      eventSource.close();
    };

    const pollingTimer = window.setInterval(
      () => {
        getSimulationJob(jobId)
          .then(handleJobUpdate)
          .catch(handleRequestError);
      },
      5000,
    );

    return () => {
      ignore = true;
      window.clearInterval(pollingTimer);
      eventSource.close();
    };
  }, [jobId]);


  useEffect(() => {
    if (
      job?.status !== "completed"
      || result !== null
    ) {
      return;
    }

    let ignore = false;

    getSimulationResult(jobId)
      .then((nextResult) => {
        if (!ignore) {
          setResult(nextResult);
        }
      })
      .catch((caughtError: unknown) => {
        if (!ignore) {
          setError(
            caughtError instanceof Error
              ? caughtError.message
              : "Failed to load simulation result",
          );
        }
      });

    return () => {
      ignore = true;
    };
  }, [job?.status, jobId, result]);


  async function handleCancel() {
    if (cancelling) {
      return;
    }

    setCancelling(true);
    setError("");

    try {
      const updatedJob =
        await cancelSimulationJob(jobId);

      setJob((currentJob) => {
        if (!currentJob) {
          return updatedJob;
        }

        return {
          ...currentJob,
          ...updatedJob,
        };
      });
    } catch (caughtError) {
      setError(
        caughtError instanceof Error
          ? caughtError.message
          : "Failed to cancel simulation job",
      );
    } finally {
      setCancelling(false);
    }
  }
  
  if (!job) {
    return (
      <main className="min-h-screen bg-slate-950 p-10 text-white">
        <div className="mx-auto max-w-4xl">
          {error ? (
            <div
              role="alert"
              className="rounded-xl border border-red-900 bg-red-950 p-5 text-red-300"
            >
              {error}
            </div>
          ) : (
            <p className="text-slate-400">
              Loading simulation job…
            </p>
          )}
        </div>
      </main>
    );
  }

  const isTerminal =
    terminalStatuses.has(job.status);

  const progress = Math.min(
    100,
    Math.max(0, job.progress),
  );


  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl px-6 py-10">
        <header>
          <p className="text-sm font-medium text-cyan-400">
            Simulation Job
          </p>

          <h1 className="mt-2 text-3xl font-bold">
            Simulation Job
          </h1>

          <p className="mt-2 break-all text-sm text-slate-400">
            {job.id}
          </p>
        </header>

        <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-6">
          <div className="flex flex-wrap items-center justify-between gap-4">
            <div>
              <p className="text-sm text-slate-400">
                Current Stage
              </p>

              <p className="mt-1 text-xl font-semibold">
                {stageLabels[job.stage]
                  ?? job.stage}
              </p>
            </div>

            {!isTerminal && (
              <button
                type="button"
                onClick={handleCancel}
                disabled={cancelling}
                className="rounded-lg border border-red-800 px-4 py-2 text-red-300 transition hover:bg-red-950 disabled:cursor-not-allowed disabled:opacity-50"
              >
                {cancelling
                  ? "Cancelling…"
                  : "Cancel Job"}
              </button>
            )}
          </div>

          <div className="mt-6 h-3 overflow-hidden rounded-full bg-slate-800">
            <div
              className="h-full bg-cyan-400 transition-all duration-500"
              style={{
                width: `${progress}%`,
              }}
            />
          </div>

          <div className="mt-2 flex justify-between text-sm text-slate-400">
            <span>{job.status}</span>
            <span>{progress}%</span>
          </div>

          <dl className="mt-6 grid gap-4 text-sm sm:grid-cols-2 lg:grid-cols-4">
            <div>
              <dt className="text-slate-500">
                City
              </dt>
              <dd className="mt-1">
                {job.city_id}
              </dd>
            </div>

            <div>
              <dt className="text-slate-500">
                Created At
              </dt>
              <dd className="mt-1">
                {new Date(
                  job.created_at,
                ).toLocaleString()}
              </dd>
            </div>

            <div>
              <dt className="text-slate-500">
                Started At
              </dt>
              <dd className="mt-1">
                {job.started_at
                  ? new Date(
                      job.started_at,
                    ).toLocaleString()
                  : "Not started"}
              </dd>
            </div>

            <div>
              <dt className="text-slate-500">
                Completed At
              </dt>
              <dd className="mt-1">
                {job.completed_at
                  ? new Date(
                      job.completed_at,
                    ).toLocaleString()
                  : "Not completed"}
              </dd>
            </div>
          </dl>
          {(job.control_material_version_id || job.rc_material_version_id) && (
            <dl className="mt-5 grid gap-4 text-sm sm:grid-cols-2">
              <div>
                <dt className="text-slate-500">Control material version</dt>
                <dd className="mt-1 font-mono text-xs text-slate-300">
                  {job.control_material_version_id ?? "manual values"}
                </dd>
              </div>
              <div>
                <dt className="text-slate-500">RC material version</dt>
                <dd className="mt-1 font-mono text-xs text-slate-300">
                  {job.rc_material_version_id ?? "manual values"}
                </dd>
              </div>
            </dl>
          )}
          {job.error_message && (
            <div className="mt-5 rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">
              {job.error_message}
            </div>
          )}

          {error && (
            <div
              role="alert"
              className="mt-5 rounded-lg border border-red-900 bg-red-950 p-4 text-red-300"
            >
              {error}
            </div>
          )}
        </section>

        {job.status === "completed"
          && !result && (
            <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-6 text-slate-400">
              Loading complete simulation results…
            </section>
          )}

        {result && (
          <section className="mt-10 space-y-8">
            <div className="grid gap-4 md:grid-cols-3">
              <SummaryCard
                label="final skin temperature improvement"
                value={
                  result.summary
                    .final_skin_temperature_improvement_c
                }
              />

              <SummaryCard
                label="average skin temperature improvement"
                value={
                  result.summary
                    .average_skin_temperature_improvement_c
                }
              />

              <SummaryCard
                label="final core temperature improvement"
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

            <TemperatureChart
              result={result}
            />

            <HeatFluxChart
              result={result}
            />
            <PhysiologyChart result={result} />
            <ModelQualityPanel result={result} />
            <ModelProvenancePanel result={result} />
            <div className="flex flex-wrap gap-3">
              <a
                href={getSimulationExportUrl(
                  jobId,
                  "csv",
                )}
                className="rounded-lg bg-cyan-400 px-5 py-2 font-semibold text-slate-950"
              >
                Export CSV
              </a>

              <a
                href={getSimulationExportUrl(
                  jobId,
                  "json",
                )}
                className="rounded-lg border border-slate-700 px-5 py-2"
              >
                Export JSON
              </a>
            </div>
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


```

### File: `frontend/src/app/simulations/new/page.tsx`
```tsx
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
    direct_normal_irradiance_w_m2: null, 
    diffuse_horizontal_irradiance_w_m2: null, 
    ground_albedo: 0.2
  },

  person: {
    met: 2.6,
    body_mass_kg: 70,
    body_surface_area_m2: 1.8,
    initial_core_temperature_c: 36.8,
    initial_skin_temperature_c: 33.7,
    position: "standing",
  },

  control_material: {
    name: "Ordinary clothing",
    clothing_insulation_clo: 0.5,
    clothing_area_factor: null,
    solar_reflectance: 0.4,
    solar_transmittance: 0,
    infrared_emissivity: 0.8,
    projected_solar_area_factor: 0.25,
  },

  rc_material: {
    name: "Radiative Cooling Clothing",
    clothing_insulation_clo: 0.4,
    clothing_area_factor: null,
    solar_reflectance: 0.92,
    solar_transmittance: 0,
    infrared_emissivity: 0.95,
    projected_solar_area_factor: 0.25,
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
                  enableLibrary
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
                  enableLibrary
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
```

### File: `frontend/src/app/simulations/page.tsx`
```tsx
"use client";

import Link from "next/link";
import {
  useEffect,
  useState,
} from "react";

import {
  getSimulationJobs,
} from "@/lib/api-client";
import type {
  SimulationJob,
} from "@/types/simulation";


export default function SimulationJobsPage() {
  const [jobs, setJobs] =
    useState<SimulationJob[]>([]);

  const [loading, setLoading] =
    useState(true);

  useEffect(() => {
    async function loadJobs() {
      try {
        const response =
          await getSimulationJobs();

        setJobs(response.items);
      } finally {
        setLoading(false);
      }
    }

    void loadJobs();

    const timer = window.setInterval(
      loadJobs,
      5000,
    );

    return () => {
      window.clearInterval(timer);
    };
  }, []);

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl px-6 py-10">
        <header className="flex items-center justify-between">
          <div>
            <p className="text-sm text-cyan-400">
              Simulation Jobs
            </p>

            <h1 className="mt-2 text-3xl font-bold">
              Simulation Jobs
            </h1>
          </div>

          <Link
            href="/simulations/weather"
            className="rounded-lg bg-cyan-400 px-5 py-2.5 font-semibold text-slate-950"
          >
            New Simulation
          </Link>
        </header>

        <section className="mt-8 overflow-hidden rounded-2xl border border-slate-800">
          <table className="w-full text-left">
            <thead className="bg-slate-900 text-sm text-slate-400">
              <tr>
                <th className="px-5 py-4">
                  Job
                </th>
                <th className="px-5 py-4">
                  City
                </th>
                <th className="px-5 py-4">
                  Status
                </th>
                <th className="px-5 py-4">
                  Progress
                </th>
                <th className="px-5 py-4">
                  Created At
                </th>
              </tr>
            </thead>

            <tbody>
              {jobs.map((job) => (
                <tr
                  key={job.id}
                  className="border-t border-slate-800"
                >
                  <td className="px-5 py-4">
                    <Link
                      href={`/simulations/${job.id}`}
                      className="font-medium text-cyan-300 hover:underline"
                    >
                      {job.id.slice(0, 8)}
                    </Link>
                  </td>

                  <td className="px-5 py-4">
                    {job.city_id}
                  </td>

                  <td className="px-5 py-4">
                    <StatusBadge
                      status={job.status}
                    />
                  </td>

                  <td className="px-5 py-4">
                    {job.progress}%
                  </td>

                  <td className="px-5 py-4 text-sm text-slate-400">
                    {new Date(
                      job.created_at,
                    ).toLocaleString()}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>

          {loading && (
            <div className="p-10 text-center text-slate-400">
              Loading…
            </div>
          )}
        </section>
      </div>
    </main>
  );
}


function StatusBadge({
  status,
}: {
  status: string;
}) {
  const colors: Record<string, string> = {
    completed:
      "bg-emerald-950 text-emerald-300",
    running:
      "bg-cyan-950 text-cyan-300",
    queued:
      "bg-amber-950 text-amber-300",
    failed:
      "bg-red-950 text-red-300",
    cancelled:
      "bg-slate-800 text-slate-300",
  };

  return (
    <span
      className={`rounded-full px-3 py-1 text-xs font-medium ${
        colors[status]
        ?? "bg-slate-800 text-slate-300"
      }`}
    >
      {status}
    </span>
  );
}
```

### File: `frontend/src/app/simulations/weather/page.tsx`
```tsx
"use client";

import { PersonInputFields } from "@/components/simulation/person-input-fields";
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
import { NumberField } from "@/components/forms/number-field";
import { MaterialInputFields } from "@/components/simulation/material-input-fields";
import { getDefaultSimulationDateTime } from "@/lib/date-defaults";
import { DEFAULT_ENVIRONMENT_ASSUMPTIONS } from "@/lib/environment-assumptions";
import { EnvironmentAssumptionsFields } from "@/components/simulation/environment-assumptions-fields";


const initialRequest: WeatherSimulationRequest = {
  city_id: "dubai",
  start_time_local: getDefaultSimulationDateTime(), 
  duration_minutes: 120,
  output_interval_minutes: 1,
  environment_assumptions: DEFAULT_ENVIRONMENT_ASSUMPTIONS,

  person: {
    met: 2.6,
    body_surface_area_m2: 1.8,
    initial_core_temperature_c: 36.8,
    initial_skin_temperature_c: 33.7,
    body_mass_kg: 70,
    position: "standing",
  },

  control_material: {
    name: "Ordinary clothing",
    clothing_insulation_clo: 0.5,
    solar_reflectance: 0.4,
    solar_transmittance: 0,
    infrared_emissivity: 0.8,
    projected_solar_area_factor: 0.25,
    clothing_area_factor: null,
  },

  rc_material: {
    name: "Radiative Cooling Clothing",
    clothing_insulation_clo: 0.4,
    solar_reflectance: 0.92,
    solar_transmittance: 0,
    infrared_emissivity: 0.95,
    projected_solar_area_factor: 0.25,
    clothing_area_factor: null,
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
              : "Unable to load city list",
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
          : "Unable to create simulation job",
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
            Historical Weather-Driven Simulation
          </h1>

          <p className="mt-3 max-w-3xl text-slate-400">
            Using ERA5 historical hourly weather data,
            create asynchronous dynamic simulation tasks for ordinary clothing and radiative cooling clothing.
          </p>
        </header>

        <form
          onSubmit={handleSubmit}
          className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-6"
        >
          <div className="grid gap-5 md:grid-cols-2 lg:grid-cols-4">
            <label className="block">
              <span className="mb-2 block text-sm text-slate-300">
                City
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
                    Loading cities…
                  </option>
                )}

                {!loadingCities
                  && cities.length === 0 && (
                    <option value="">
                      No available cities
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
                Local Start Time
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
                Simulation Duration (Minutes)
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
            <NumberField
              label="Output Interval"
              suffix="min"
              value={request.output_interval_minutes}
              min={1} max={60} step={1}
              disabled={submitting}
              onChange={(value) =>
                setRequest((current) => ({ ...current, output_interval_minutes: value }))
              }
            />
          </div>

          <section className="mt-8 rounded-xl border border-slate-800 bg-slate-950/50 p-5">
            <h2 className="text-lg font-semibold">Person</h2>

            <p className="mt-1 text-sm text-slate-400">
              Body mass sets the core and skin heat capacities used by the
              transient solver (Stage 3).
            </p>

            <div className="mt-4">
              <PersonInputFields
                person={request.person}
                disabled={submitting}
                onChange={(person) =>
                  setRequest((current) => ({ ...current, person }))
                }
              />
            </div>
          </section>

          <div className="mt-8">
            <EnvironmentAssumptionsFields
              value={request.environment_assumptions ?? DEFAULT_ENVIRONMENT_ASSUMPTIONS}
              disabled={submitting}
              onChange={(environment_assumptions) =>
                setRequest((current) => ({ ...current, environment_assumptions }))
              }
            />
          </div>

          <div className="mt-8 grid gap-6 lg:grid-cols-2">
            <section className="rounded-xl border border-slate-800 bg-slate-950/50 p-5">
              <h2 className="text-lg font-semibold">Control Clothing</h2>
              <div className="mt-4">
                <MaterialInputFields
                  material={request.control_material}
                  showName
                  enableLibrary
                  disabled={submitting}
                  onChange={(control_material) =>
                    setRequest((current) => ({ ...current, control_material }))
                  }
                />
              </div>
            </section>

            <section className="rounded-xl border border-slate-800 bg-slate-950/50 p-5">
              <h2 className="text-lg font-semibold">Radiative Cooling Clothing</h2>
              <div className="mt-4">
                <MaterialInputFields
                  material={request.rc_material}
                  showName
                  enableLibrary
                  disabled={submitting}
                  onChange={(rc_material) =>
                    setRequest((current) => ({ ...current, rc_material }))
                  }
                />
              </div>
            </section>
          </div>

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
              ? "Simulation task being set up..."
              : "Create Historical Weather Simulation Task"}
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
            Asynchronous Task Flow
          </h2>

          <ol className="mt-3 list-inside list-decimal space-y-2">
            <li>
              The frontend submits the simulation configuration to FastAPI.
            </li>
            <li>
              The backend creates a task record in PostgreSQL.
            </li>
            <li>
              The Celery Worker downloads weather data and executes the numerical simulation.
            </li>
            <li>
              Upon successful creation, the page will automatically redirect to the task progress page.
            </li>
          </ol>
        </section>
      </div>
    </main>
  );
}
```

### File: `frontend/src/components/charts/benchmark-chart.tsx`
```tsx
"use client";

import dynamic from "next/dynamic";
import type { Data } from "plotly.js";

import type { BenchmarkSeriesPoint } from "@/types/benchmark";

const Plot = dynamic(() => import("react-plotly.js"), {
  ssr: false,
  loading: () => (
    <div className="flex h-96 items-center justify-center text-slate-400">
      Loading chart...
    </div>
  ),
});

type BenchmarkChartProps = {
  points: BenchmarkSeriesPoint[];
  referenceLabel: string;
};

export function BenchmarkChart({ points, referenceLabel }: BenchmarkChartProps) {
  const minutes = points.map((point) => point.minute);

  const data: Data[] = [
    {
      x: minutes,
      y: points.map((point) => point.prototype_core_temperature_c),
      type: "scatter",
      mode: "lines",
      name: "Prototype: Core",
      line: { color: "#ef4444", width: 3 },
    },
    {
      x: minutes,
      y: points.map((point) => point.reference_core_temperature_c),
      type: "scatter",
      mode: "lines",
      name: `${referenceLabel}: Core`,
      line: { color: "#fca5a5", width: 2, dash: "dash" },
    },
    {
      x: minutes,
      y: points.map((point) => point.prototype_skin_temperature_c),
      type: "scatter",
      mode: "lines",
      name: "Prototype: Skin",
      line: { color: "#22d3ee", width: 3 },
    },
    {
      x: minutes,
      y: points.map((point) => point.reference_skin_temperature_c),
      type: "scatter",
      mode: "lines",
      name: `${referenceLabel}: Skin`,
      line: { color: "#a5f3fc", width: 2, dash: "dash" },
    },
    {
      x: minutes,
      y: points.map((point) => point.prototype_evaporation_w_m2),
      type: "scatter",
      mode: "lines",
      name: "Prototype: Evaporation",
      line: { color: "#a3e635", width: 2 },
      yaxis: "y2",
      visible: "legendonly",
    },
    {
      x: minutes,
      y: points.map((point) => point.reference_evaporation_w_m2),
      type: "scatter",
      mode: "lines",
      name: `${referenceLabel}: Evaporation`,
      line: { color: "#d9f99d", width: 2, dash: "dash" },
      yaxis: "y2",
      visible: "legendonly",
    },
  ];

  return (
    <div className="overflow-hidden rounded-2xl border border-slate-800 bg-slate-900 p-4">
      <h2 className="mb-4 text-xl font-semibold">Trajectory Comparison</h2>

      <Plot
        data={data}
        layout={{
          autosize: true,
          height: 480,
          paper_bgcolor: "#0f172a",
          plot_bgcolor: "#0f172a",
          font: { color: "#cbd5e1" },
          margin: { l: 65, r: 70, t: 20, b: 60 },
          xaxis: { title: { text: "Time (min)" }, gridcolor: "#334155" },
          yaxis: { title: { text: "Temperature (°C)" }, gridcolor: "#334155" },
          yaxis2: {
            title: { text: "Evaporation (W/m²)" },
            overlaying: "y",
            side: "right",
            showgrid: false,
          },
          legend: { orientation: "h", y: -0.25 },
          hovermode: "x unified",
        }}
        config={{
          responsive: true,
          displaylogo: false,
          toImageButtonOptions: {
            format: "png",
            filename: "gagge-benchmark",
            scale: 2,
          },
        }}
        useResizeHandler
        style={{ width: "100%", height: "100%" }}
      />

      <p className="mt-3 text-sm text-slate-400">
        Solid lines are the platform prototype; dashed lines are the reference
        model. Evaporation is on the right axis and hidden until toggled.
      </p>
    </div>
  );
}
```

### File: `frontend/src/components/charts/heat-flux-chart.tsx`
```tsx
"use client";

import dynamic from "next/dynamic";

import type { SimulationResponse } from "@/types/simulation";

const Plot = dynamic(
  () => import("react-plotly.js"),
  { ssr: false },
);

type HeatFluxChartProps = {
  result: SimulationResponse;
};

export function HeatFluxChart({
  result,
}: HeatFluxChartProps) {
  const points =
    result.radiative_cooling.time_series;

  // 檢查時間序列的第一個點是否包含 solar_incident_w_m2 屬性
  const hasOptionalSeries =
    points.length > 0 &&
    "solar_incident_w_m2" in points[0];

  return (
    <div className="overflow-hidden rounded-2xl border border-slate-800 bg-slate-900 p-4">
      <h2 className="mb-4 text-xl font-semibold">
        Radiative Cooling Clothing Heat Flux Components
      </h2>

      <Plot
        data={[
          {
            x: points.map((point) => point.minute),
            y: points.map(
              (point) => point.convection_w_m2,
            ),
            type: "scatter",
            mode: "lines",
            name: "Convection",
          },
          {
            x: points.map((point) => point.minute),
            y: points.map(
              (point) =>
                point.longwave_radiation_w_m2,
            ),
            type: "scatter",
            mode: "lines",
            name: "Longwave Radiation",
          },
          {
            x: points.map((point) => point.minute),
            y: points.map(
              (point) => point.evaporation_w_m2,
            ),
            type: "scatter",
            mode: "lines",
            name: "Evaporation",
          },
          {
            x: points.map((point) => point.minute),
            y: points.map(
              (point) => point.absorbed_solar_w_m2,
            ),
            type: "scatter",
            mode: "lines",
            name: "Absorbed Solar Radiation",
          },
          ...(hasOptionalSeries
            ? [
                {
                  x: points.map((point) => point.minute),
                  y: points.map(
                    (point) =>
                      (point as { solar_incident_w_m2?: number })
                        .solar_incident_w_m2 ?? 0,
                  ),
                  type: "scatter" as const,
                  mode: "lines" as const,
                  name: "Incident Solar (per A_D)",
                  visible: "legendonly" as const,
                },
              ]
            : []),
        ]}
        layout={{
          autosize: true,
          height: 450,
          paper_bgcolor: "#0f172a",
          plot_bgcolor: "#0f172a",
          font: {
            color: "#cbd5e1",
          },
          margin: {
            l: 65,
            r: 30,
            t: 20,
            b: 60,
          },
          xaxis: {
            title: {
              text: "Time (min)",
            },
            gridcolor: "#334155",
          },
          yaxis: {
            title: {
              text: "Heat Flux (W/m²)",
            },
            gridcolor: "#334155",
          },
          hovermode: "x unified",
        }}
        config={{
          responsive: true,
          displaylogo: false,
        }}
        useResizeHandler
        style={{
          width: "100%",
          height: "100%",
        }}
      />

      <p className="mt-3 text-sm text-slate-400">
        Positive longwave radiation and convection represent heat loss from the human body.
        Absorbed solar radiation represents heat gained by the clothing–body system from the environment.
      </p>
    </div>
  );
}


```

### File: `frontend/src/components/charts/physiology-chart.tsx`
```tsx
"use client";

import dynamic from "next/dynamic";
import type { Data } from "plotly.js";

import { hasOptionalSeries, pluckOptionalSeries } from "@/lib/time-series";
import type { SimulationResponse } from "@/types/simulation";

const Plot = dynamic(() => import("react-plotly.js"), { ssr: false });

type PhysiologyChartProps = {
  result: SimulationResponse;
};

/**
 * Stage 3 physiological state: skin blood flow (left axis) and skin
 * wettedness (right axis). Renders nothing for results that predate Stage 3.
 */
export function PhysiologyChart({ result }: PhysiologyChartProps) {
  const control = result.control.time_series;
  const rc = result.radiative_cooling.time_series;

  const hasBloodFlow =
    hasOptionalSeries(control, "skin_blood_flow_kg_h_m2") ||
    hasOptionalSeries(rc, "skin_blood_flow_kg_h_m2");

  const hasWettedness =
    hasOptionalSeries(control, "skin_wettedness") ||
    hasOptionalSeries(rc, "skin_wettedness");

  if (!hasBloodFlow && !hasWettedness) {
    return null;
  }

  const controlMinutes = control.map((point) => point.minute);
  const rcMinutes = rc.map((point) => point.minute);

  const data: Data[] = [];

  if (hasBloodFlow) {
    data.push(
      {
        x: controlMinutes,
        y: pluckOptionalSeries(control, "skin_blood_flow_kg_h_m2"),
        type: "scatter",
        mode: "lines",
        name: "Standard Clothing: Skin Blood Flow",
        line: { color: "#f97316", width: 3 },
        yaxis: "y",
      },
      {
        x: rcMinutes,
        y: pluckOptionalSeries(rc, "skin_blood_flow_kg_h_m2"),
        type: "scatter",
        mode: "lines",
        name: "Radiative Cooling: Skin Blood Flow",
        line: { color: "#22d3ee", width: 3 },
        yaxis: "y",
      },
    );
  }

  if (hasWettedness) {
    data.push(
      {
        x: controlMinutes,
        y: pluckOptionalSeries(control, "skin_wettedness"),
        type: "scatter",
        mode: "lines",
        name: "Standard Clothing: Skin Wettedness",
        line: { color: "#fdba74", width: 2, dash: "dot" },
        yaxis: "y2",
        visible: hasBloodFlow ? "legendonly" : true,
      },
      {
        x: rcMinutes,
        y: pluckOptionalSeries(rc, "skin_wettedness"),
        type: "scatter",
        mode: "lines",
        name: "Radiative Cooling: Skin Wettedness",
        line: { color: "#67e8f9", width: 2, dash: "dot" },
        yaxis: "y2",
        visible: hasBloodFlow ? "legendonly" : true,
      },
    );
  }

  return (
    <div className="overflow-hidden rounded-2xl border border-slate-800 bg-slate-900 p-4">
      <h2 className="mb-4 text-xl font-semibold">
        Thermoregulatory Response
      </h2>

      <Plot
        data={data}
        layout={{
          autosize: true,
          height: 420,
          paper_bgcolor: "#0f172a",
          plot_bgcolor: "#0f172a",
          font: { color: "#cbd5e1" },
          margin: { l: 65, r: 70, t: 20, b: 60 },
          xaxis: { title: { text: "Time (min)" }, gridcolor: "#334155" },
          yaxis: {
            title: { text: "Skin Blood Flow (kg/(h·m²))" },
            gridcolor: "#334155",
          },
          yaxis2: {
            title: { text: "Skin Wettedness" },
            overlaying: "y",
            side: "right",
            range: [0, 1],
            showgrid: false,
          },
          legend: { orientation: "h", y: -0.25 },
          hovermode: "x unified",
        }}
        config={{ responsive: true, displaylogo: false }}
        useResizeHandler
        style={{ width: "100%", height: "100%" }}
      />

      <p className="mt-3 text-sm text-slate-400">
        Skin blood flow follows the Gagge two-node control law ported in
        Stage 3. Skin wettedness is shown on the right axis; toggle it from the
        legend.
      </p>
    </div>
  );
}
```

### File: `frontend/src/components/charts/temperature-chart.tsx`
```tsx
"use client";

import dynamic from "next/dynamic";
import type { Data } from "plotly.js";

import { hasOptionalSeries, pluckOptionalSeries } from "@/lib/time-series";
import type { SimulationResponse } from "@/types/simulation";

const Plot = dynamic(() => import("react-plotly.js"), {
  ssr: false,
  loading: () => (
    <div className="flex h-96 items-center justify-center text-slate-400">
      Loading charts...
    </div>
  ),
});

type TemperatureChartProps = {
  result: SimulationResponse;
};

export function TemperatureChart({ result }: TemperatureChartProps) {
  const control = result.control.time_series;
  const rc = result.radiative_cooling.time_series;

  const controlMinutes = control.map((point) => point.minute);
  const rcMinutes = rc.map((point) => point.minute);

  const hasClothingSurface =
    hasOptionalSeries(control, "clothing_surface_temperature_c") ||
    hasOptionalSeries(rc, "clothing_surface_temperature_c");

  const data: Data[] = [
    {
      x: controlMinutes,
      y: control.map((point) => point.skin_temperature_c),
      type: "scatter",
      mode: "lines",
      name: "Standard Clothing: Skin Temperature",
      line: { color: "#f97316", width: 3 },
    },
    {
      x: rcMinutes,
      y: rc.map((point) => point.skin_temperature_c),
      type: "scatter",
      mode: "lines",
      name: "Radiative Cooling: Skin Temperature",
      line: { color: "#22d3ee", width: 3 },
    },
    {
      x: controlMinutes,
      y: control.map((point) => point.core_temperature_c),
      type: "scatter",
      mode: "lines",
      name: "Standard Clothing: Core Temperature",
      line: { color: "#ef4444", width: 2, dash: "dot" },
    },
    {
      x: rcMinutes,
      y: rc.map((point) => point.core_temperature_c),
      type: "scatter",
      mode: "lines",
      name: "Radiative Cooling: Core Temperature",
      line: { color: "#3b82f6", width: 2, dash: "dot" },
    },
  ];

  if (hasClothingSurface) {
    data.push(
      {
        x: controlMinutes,
        y: pluckOptionalSeries(control, "clothing_surface_temperature_c"),
        type: "scatter",
        mode: "lines",
        name: "Standard Clothing: Clothing Surface",
        line: { color: "#fdba74", width: 2, dash: "dashdot" },
        visible: "legendonly",
      },
      {
        x: rcMinutes,
        y: pluckOptionalSeries(rc, "clothing_surface_temperature_c"),
        type: "scatter",
        mode: "lines",
        name: "Radiative Cooling: Clothing Surface",
        line: { color: "#67e8f9", width: 2, dash: "dashdot" },
        visible: "legendonly",
      },
    );
  }

  return (
    <div className="overflow-hidden rounded-2xl border border-slate-800 bg-slate-900 p-4">
      <h2 className="mb-4 text-xl font-semibold">
        Human Body Temperature Dynamics
      </h2>

      <Plot
        data={data}
        layout={{
          autosize: true,
          height: 480,
          paper_bgcolor: "#0f172a",
          plot_bgcolor: "#0f172a",
          font: { color: "#cbd5e1" },
          margin: { l: 65, r: 30, t: 20, b: 60 },
          xaxis: { title: { text: "Time (min)" }, gridcolor: "#334155" },
          yaxis: { title: { text: "Temperature (°C)" }, gridcolor: "#334155" },
          legend: { orientation: "h", y: -0.25 },
          hovermode: "x unified",
        }}
        config={{
          responsive: true,
          displaylogo: false,
          toImageButtonOptions: {
            format: "png",
            filename: "temperature-comparison",
            scale: 2,
          },
        }}
        useResizeHandler
        style={{ width: "100%", height: "100%" }}
      />

      {hasClothingSurface && (
        <p className="mt-3 text-sm text-slate-400">
          Clothing surface temperature is hidden by default. Click its legend
          entry to overlay it on the skin and core curves.
        </p>
      )}
    </div>
  );
}
```

### File: `frontend/src/components/charts/weather-chart.tsx`
```tsx
"use client";

import dynamic from "next/dynamic";

import type {
  WeatherTimeSeries,
} from "@/types/simulation";

const Plot = dynamic(
  () => import("react-plotly.js"),
  { ssr: false },
);

export function WeatherChart({
  weather,
}: {
  weather: WeatherTimeSeries;
}) {
  const points = weather.points;

  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-900 p-5">
      <h2 className="text-xl font-semibold">
        Historical Weather Time Series
      </h2>

      <Plot
        data={[
          {
            x: points.map(
              (point) => point.timestamp,
            ),
            y: points.map(
              (point) =>
                point.air_temperature_c,
            ),
            name: "Air Temperature (°C)",
            type: "scatter",
            mode: "lines+markers",
            yaxis: "y",
          },
          {
            x: points.map(
              (point) => point.timestamp,
            ),
            y: points.map(
              (point) => point.ghi_w_m2,
            ),
            name: "GHI (W/m²)",
            type: "scatter",
            mode: "lines+markers",
            yaxis: "y2",
          },
          {
            x: points.map(
              (point) => point.timestamp,
            ),
            y: points.map(
              (point) =>
                point.relative_humidity_percent,
            ),
            name: "Relative Humidity (%)",
            type: "scatter",
            mode: "lines",
            yaxis: "y3",
            visible: "legendonly",
          },
        ]}
        layout={{
          autosize: true,
          height: 450,
          paper_bgcolor: "#0f172a",
          plot_bgcolor: "#0f172a",
          font: {
            color: "#cbd5e1",
          },
          margin: {
            l: 65,
            r: 70,
            t: 30,
            b: 70,
          },
          xaxis: {
            title: {
              text: "Local Time",
            },
            gridcolor: "#334155",
          },
          yaxis: {
            title: {
              text: "Air Temperature (°C)",
            },
            gridcolor: "#334155",
          },
          yaxis2: {
            title: {
              text: "GHI (W/m²)",
            },
            overlaying: "y",
            side: "right",
            gridcolor: "#334155",
          },
          yaxis3: {
            overlaying: "y",
            side: "right",
            visible: false,
          },
          hovermode: "x unified",
          legend: {
            orientation: "h",
            y: -0.25,
          },
        }}
        config={{
          responsive: true,
          displaylogo: false,
        }}
        useResizeHandler
        style={{
          width: "100%",
          height: "100%",
        }}
      />

      <div className="mt-4 border-t border-slate-800 pt-4 text-sm text-slate-400">
        <p>
          Data source:{weather.source.provider} /{" "}
          {weather.source.model}
        </p>
        <p>
          Grid Location:
          {weather.source.latitude.toFixed(4)},{" "}
          {weather.source.longitude.toFixed(4)}
        </p>
        <p>
          Cache:
          {weather.source.from_cache
            ? "Local Cache"
            : "Current API Download"}
        </p>

        <p className="mt-2">
          Weather data by Open-Meteo.com
        </p>
      </div>
    </section>
  );
}
```

### File: `frontend/src/components/forms/number-field.tsx`
```tsx
"use client";

const inputClassName =
  "w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-white outline-none focus:border-cyan-500 disabled:cursor-not-allowed disabled:opacity-50";

type BaseProps = {
  label: string;
  min?: number;
  max?: number;
  step?: number;
  suffix?: string;
  hint?: string;
  disabled?: boolean;
};

type NumberFieldProps = BaseProps & {
  value: number;
  onChange: (value: number) => void;
};

export function NumberField({
  label,
  value,
  min,
  max,
  step = 1,
  suffix,
  hint,
  disabled = false,
  onChange,
}: NumberFieldProps) {
  return (
    <label className="block">
      <span className="mb-2 block text-sm text-slate-300">{label}</span>

      <div className="relative">
        <input
          type="number"
          value={value}
          min={min}
          max={max}
          step={step}
          disabled={disabled}
          onChange={(event) => {
            const parsed = Number(event.target.value);

            if (Number.isFinite(parsed)) {
              onChange(parsed);
            }
          }}
          className={`${inputClassName} ${suffix ? "pr-16" : ""}`}
        />

        {suffix && (
          <span className="pointer-events-none absolute inset-y-0 right-3 flex items-center text-xs text-slate-500">
            {suffix}
          </span>
        )}
      </div>

      {hint && <span className="mt-1 block text-xs text-slate-500">{hint}</span>}
    </label>
  );
}

type OptionalNumberFieldProps = BaseProps & {
  value: number | null;
  placeholder?: string;
  onChange: (value: number | null) => void;
};

/** Empty input means `null`, i.e. "let the backend derive this value". */
export function OptionalNumberField({
  label,
  value,
  min,
  max,
  step = 1,
  suffix,
  hint,
  placeholder,
  disabled = false,
  onChange,
}: OptionalNumberFieldProps) {
  return (
    <label className="block">
      <span className="mb-2 block text-sm text-slate-300">{label}</span>

      <div className="relative">
        <input
          type="number"
          value={value ?? ""}
          placeholder={placeholder}
          min={min}
          max={max}
          step={step}
          disabled={disabled}
          onChange={(event) => {
            const raw = event.target.value;

            if (raw === "") {
              onChange(null);
              return;
            }

            const parsed = Number(raw);

            if (Number.isFinite(parsed)) {
              onChange(parsed);
            }
          }}
          className={`${inputClassName} ${suffix ? "pr-16" : ""}`}
        />

        {suffix && (
          <span className="pointer-events-none absolute inset-y-0 right-3 flex items-center text-xs text-slate-500">
            {suffix}
          </span>
        )}
      </div>

      {hint && <span className="mt-1 block text-xs text-slate-500">{hint}</span>}
    </label>
  );
}
```

### File: `frontend/src/components/forms/select-field.tsx`
```tsx
"use client";

type Option<T extends string> = { value: T; label: string };

type SelectFieldProps<T extends string> = {
  label: string;
  value: T;
  options: Option<T>[];
  hint?: string;
  disabled?: boolean;
  onChange: (value: T) => void;
};

export function SelectField<T extends string>({
  label,
  value,
  options,
  hint,
  disabled = false,
  onChange,
}: SelectFieldProps<T>) {
  return (
    <label className="block">
      <span className="mb-2 block text-sm text-slate-300">{label}</span>

      <select
        value={value}
        disabled={disabled}
        onChange={(event) => onChange(event.target.value as T)}
        className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-white outline-none focus:border-cyan-500 disabled:cursor-not-allowed disabled:opacity-50"
      >
        {options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>

      {hint && <span className="mt-1 block text-xs text-slate-500">{hint}</span>}
    </label>
  );
}
```

### File: `frontend/src/components/global-adaptation-map.tsx`
```tsx
"use client";

import {
  useEffect,
  useRef,
} from "react";

import type * as GeoJSON from "geojson";
import * as maplibregl from "maplibre-gl";

import type {
  GeoJsonFeatureCollection,
} from "@/types/global-batch";


type Props = {
  data: GeoJsonFeatureCollection;
};


const ADAPTATION_SOURCE_ID =
  "adaptation";

const ADAPTATION_LAYER_ID =
  "adaptation-circles";


export default function GlobalAdaptationMap({
  data,
}: Props) {
  const containerRef =
    useRef<HTMLDivElement | null>(null);

  const mapRef =
    useRef<maplibregl.Map | null>(null);

  /*
   * useRef 的 initialValue 只會在第一次 render 時使用。
   * 後續資料更新會在下方的 useEffect 中同步。
   */
  const dataRef =
    useRef<GeoJsonFeatureCollection>(data);

  useEffect(() => {
    if (!containerRef.current) {
      return;
    }

    const map = new maplibregl.Map({
      container: containerRef.current,

      style: {
        version: 8,

        sources: {
          openstreetmap: {
            type: "raster",

            tiles: [
              "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
            ],

            tileSize: 256,

            attribution:
              "© OpenStreetMap contributors",
          },
        },

        layers: [
          {
            id: "openstreetmap",
            type: "raster",
            source: "openstreetmap",
          },
        ],
      },

      center: [20, 15],
      zoom: 1.2,
      minZoom: 1,
      maxZoom: 12,
    });

    mapRef.current = map;

    map.addControl(
      new maplibregl.NavigationControl({
        showCompass: true,
        showZoom: true,
        visualizePitch: true,
      }),
      "top-right",
    );

    map.addControl(
      new maplibregl.FullscreenControl(),
      "top-right",
    );

    map.on("load", () => {
      /*
       * load callback 可能延後執行，因此從 dataRef
       * 取得當時最新的 GeoJSON，而不是使用初次 render
       * 捕獲的 data。
       */
      map.addSource(
        ADAPTATION_SOURCE_ID,
        {
          type: "geojson",

          data:
            dataRef.current as GeoJSON.FeatureCollection,
        },
      );

      map.addLayer({
        id: ADAPTATION_LAYER_ID,
        type: "circle",
        source: ADAPTATION_SOURCE_ID,

        paint: {
          /*
           * 沒有 qualifying exposure 時 adaptation rate 為 null。
           * coalesce 將 null 視為 0，只用於決定圓形尺寸。
           */
          "circle-radius": [
            "interpolate",
            ["linear"],

            [
              "coalesce",

              [
                "get",
                "climate_adaptation_rate_percent",
              ],

              0,
            ],

            0,
            7,

            100,
            18,
          ],

          /*
           * null 代表城市沒有符合門檻的熱暴露資料，
           * 使用灰色顯示。
           */
          "circle-color": [
            "case",

            [
              "==",

              [
                "get",
                "climate_adaptation_rate_percent",
              ],

              null,
            ],

            "#64748b",

            [
              "interpolate",
              ["linear"],

              [
                "get",
                "climate_adaptation_rate_percent",
              ],

              0,
              "#ef4444",

              40,
              "#f59e0b",

              70,
              "#22d3ee",

              100,
              "#10b981",
            ],
          ],

          "circle-opacity": 0.85,
          "circle-stroke-color": "#ffffff",
          "circle-stroke-width": 1,
        },
      });

      map.on(
        "click",
        ADAPTATION_LAYER_ID,
        (event) => {
          const feature =
            event.features?.[0];

          if (
            !feature ||
            feature.geometry.type !== "Point"
          ) {
            return;
          }

          const properties =
            (
              feature.properties ?? {}
            ) as Record<string, unknown>;

          const coordinates = (
            feature.geometry as GeoJSON.Point
          ).coordinates.slice() as [
            number,
            number,
          ];

          /*
           * 當地圖跨越日期變更線時，確保 popup 出現在
           * 使用者點擊的世界副本，而不是另一側。
           */
          while (
            Math.abs(
              event.lngLat.lng -
                coordinates[0],
            ) > 180
          ) {
            coordinates[0] +=
              event.lngLat.lng >
              coordinates[0]
                ? 360
                : -360;
          }

          const adaptationRate =
            readNullableNumber(
              properties
                .climate_adaptation_rate_percent,
            );

          const exposureCoverage =
            readNullableNumber(
              properties
                .exposure_coverage_percent,
            );

          const averageSkinCooling =
            readNullableNumber(
              properties
                .annual_average_skin_improvement_c,
            );

          const maximumSkinCooling =
            readNullableNumber(
              properties
                .maximum_skin_improvement_c,
            );

          const effectiveCoolingHours =
            readNullableNumber(
              properties
                .effective_cooling_hours,
            );

          const sampledDayCount =
            readNullableNumber(
              properties.sampled_day_count,
            );

          const eligibleSampleCount =
            readNullableNumber(
              properties.eligible_sample_count,
            );

          const adaptationText =
            adaptationRate === null
              ? "No qualifying exposure"
              : `${adaptationRate.toFixed(1)}%`;

          const coverageText =
            exposureCoverage === null
              ? "—"
              : `${exposureCoverage.toFixed(1)}%`;

          const averageSkinText =
            averageSkinCooling === null
              ? "—"
              : `${averageSkinCooling.toFixed(
                  2,
                )} °C`;

          const maximumSkinText =
            maximumSkinCooling === null
              ? "—"
              : `${maximumSkinCooling.toFixed(
                  2,
                )} °C`;

          const effectiveCoolingHoursText =
            effectiveCoolingHours === null
              ? "—"
              : `${effectiveCoolingHours.toFixed(
                  1,
                )} hours`;

          const sampleCountText =
            sampledDayCount === null
              ? "—"
              : (
                  `${eligibleSampleCount ?? 0}` +
                  ` / ${sampledDayCount}`
                );

          const cityName = escapeHtml(
            readText(
              properties.city_name,
              "Unknown city",
            ),
          );

          const country = escapeHtml(
            readText(
              properties.country,
              "Unknown country",
            ),
          );

          new maplibregl.Popup({
            closeButton: true,
            closeOnClick: true,
            maxWidth: "320px",
          })
            .setLngLat(coordinates)
            .setHTML(`
              <div
                style="
                  color:#0f172a;
                  min-width:250px;
                  line-height:1.5;
                "
              >
                <strong
                  style="
                    display:block;
                    font-size:16px;
                    margin-bottom:2px;
                  "
                >
                  ${cityName}
                </strong>

                <div
                  style="
                    color:#475569;
                    font-size:13px;
                  "
                >
                  ${country}
                </div>

                <hr
                  style="
                    border:0;
                    border-top:1px solid #cbd5e1;
                    margin:10px 0;
                  "
                />

                <div>
                  <strong>
                    Exposure coverage:
                  </strong>
                  ${coverageText}
                </div>

                <div>
                  <strong>
                    Adaptation rate:
                  </strong>
                  ${adaptationText}
                </div>

                <div>
                  <strong>
                    Average skin cooling:
                  </strong>
                  ${averageSkinText}
                </div>

                <div>
                  <strong>
                    Maximum skin cooling:
                  </strong>
                  ${maximumSkinText}
                </div>

                <div>
                  <strong>
                    Effective cooling:
                  </strong>
                  ${effectiveCoolingHoursText}
                </div>

                <div>
                  <strong>
                    Eligible samples:
                  </strong>
                  ${sampleCountText}
                </div>
              </div>
            `)
            .addTo(map);
        },
      );

      map.on(
        "mouseenter",
        ADAPTATION_LAYER_ID,
        () => {
          map.getCanvas().style.cursor =
            "pointer";
        },
      );

      map.on(
        "mouseleave",
        ADAPTATION_LAYER_ID,
        () => {
          map.getCanvas().style.cursor = "";
        },
      );
    });

    return () => {
      map.remove();
      mapRef.current = null;
    };
  }, []);

  /*
   * React refs 不應在 render 階段讀寫。
   *
   * 在 effect 中同步最新的 data，並更新已存在的
   * MapLibre GeoJSON source。
   */
  useEffect(() => {
    dataRef.current = data;

    const map = mapRef.current;

    if (
      !map ||
      !map.isStyleLoaded()
    ) {
      return;
    }

    /*
     * getSource() 的回傳型別是通用 Source，
     * 因此必須明確縮窄為 GeoJSONSource，才能使用 setData()。
     */
    const source =
      map.getSource(
        ADAPTATION_SOURCE_ID,
      ) as
        | maplibregl.GeoJSONSource
        | undefined;

    if (!source) {
      return;
    }

    source.setData(
      data as GeoJSON.FeatureCollection,
    );
  }, [data]);

  return (
    <div className="relative">
      <div
        ref={containerRef}
        className="h-140 w-full overflow-hidden rounded-2xl"
        aria-label="Global climate adaptation map"
      />

      <MapLegend />
    </div>
  );
}


function MapLegend() {
  return (
    <div className="pointer-events-none absolute bottom-4 left-4 z-10 rounded-lg bg-white/95 px-4 py-3 text-xs text-slate-900 shadow-lg">
      <p className="mb-2 font-semibold">
        Climate Adaptation Rate
      </p>

      <div className="space-y-1.5">
        <LegendItem
          color="#64748b"
          label="No qualifying exposure"
        />

        <LegendItem
          color="#ef4444"
          label="0–39%"
        />

        <LegendItem
          color="#f59e0b"
          label="40–69%"
        />

        <LegendItem
          color="#22d3ee"
          label="70–99%"
        />

        <LegendItem
          color="#10b981"
          label="100%"
        />
      </div>
    </div>
  );
}


function LegendItem({
  color,
  label,
}: {
  color: string;
  label: string;
}) {
  return (
    <div className="flex items-center gap-2">
      <span
        className="h-3 w-3 rounded-full border border-white shadow-sm"
        style={{
          backgroundColor: color,
        }}
      />

      <span>{label}</span>
    </div>
  );
}


function readNullableNumber(
  value: unknown,
): number | null {
  if (
    value === null ||
    value === undefined ||
    value === ""
  ) {
    return null;
  }

  const numericValue = Number(value);

  if (!Number.isFinite(numericValue)) {
    return null;
  }

  return numericValue;
}


function readText(
  value: unknown,
  fallback: string,
): string {
  if (
    typeof value !== "string" ||
    value.trim() === ""
  ) {
    return fallback;
  }

  return value;
}


/*
 * MapLibre Popup 使用 setHTML，因此必須先 escape
 * 後端提供的城市名稱及國家名稱。
 */
function escapeHtml(
  value: string,
): string {
  return value.replace(
    /[&<>"']/g,
    (character) => {
      const replacements: Record<
        string,
        string
      > = {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#039;",
      };

      return replacements[character];
    },
  );
}
```

### File: `frontend/src/components/layout/NavBar.tsx`
```tsx
"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";

import { NAV_LINKS } from "@/config/navigation";

function isActivePath(pathname: string, href: string): boolean {
  return pathname === href || pathname.startsWith(`${href}/`);
}

export function NavBar() {
  const pathname = usePathname();
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  return (
    <header className="border-b border-slate-800 bg-slate-950">
      <nav className="mx-auto flex min-h-16 w-full items-center justify-between px-4 sm:px-6 lg:px-8">
        <Link
          href="/simulations"
          className="font-semibold text-white"
          onClick={() => setIsMobileMenuOpen(false)}
        >
          Global Radiative Cooling Clothing Climate Adaptation Simulation Platform
        </Link>

        {/* Desktop navigation */}
        <div className="hidden items-center gap-6 md:flex">
          {NAV_LINKS.map((link) => {
            const active = isActivePath(pathname, link.href);

            return (
              <Link
                key={link.href}
                href={link.href}
                aria-current={active ? "page" : undefined}
                className={
                  active
                    ? "text-sm font-semibold text-blue-400"
                    : "text-sm font-medium text-slate-300 transition-colors hover:text-white"
                }
              >
                {link.label}
              </Link>
            );
          })}
        </div>

        {/* Mobile menu button */}
        <button
          type="button"
          className="rounded-md border border-slate-700 px-3 py-2 text-sm text-slate-200 hover:bg-slate-900 md:hidden"
          aria-label="Toggle navigation menu"
          aria-expanded={isMobileMenuOpen}
          onClick={() => {
            setIsMobileMenuOpen((current) => !current);
          }}
        >
          {isMobileMenuOpen ? "Close" : "Menu"}
        </button>
      </nav>

      {/* Mobile navigation */}
      {isMobileMenuOpen && (
        <div className="border-t border-slate-800 bg-slate-950 px-4 py-3 md:hidden">
          <div className="flex flex-col gap-1">
            {NAV_LINKS.map((link) => {
              const active = isActivePath(pathname, link.href);

              return (
                <Link
                  key={link.href}
                  href={link.href}
                  aria-current={active ? "page" : undefined}
                  onClick={() => setIsMobileMenuOpen(false)}
                  className={
                    active
                      ? "rounded-md bg-blue-950/50 px-3 py-2 text-sm font-semibold text-blue-400"
                      : "rounded-md px-3 py-2 text-sm font-medium text-slate-300 hover:bg-slate-900 hover:text-white"
                  }
                >
                  {link.label}
                </Link>
              );
            })}
          </div>
        </div>
      )}
    </header>
  );
}
```

### File: `frontend/src/components/materials/provenance-editor.tsx`
```tsx
"use client";

import { useEffect, useState } from "react";

import { getMaterialFieldManifest } from "@/lib/api-client";
import type {
  MaterialFieldManifest,
  ParameterSource,
  ParameterSourceType,
} from "@/types/simulation";

type ProvenanceEditorProps = {
  sources: Record<string, ParameterSource> | null;
  /** The version being edited; only physical fields are read. */
  values: Record<string, unknown>;
  disabled?: boolean;
  onChange: (sources: Record<string, ParameterSource> | null) => void;
};

export function ProvenanceEditor({
  sources,
  values,
  disabled = false,
  onChange,
}: ProvenanceEditorProps) {
  const [manifest, setManifest] = useState<MaterialFieldManifest | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    let ignore = false;

    getMaterialFieldManifest()
      .then((response) => {
        if (!ignore) setManifest(response);
      })
      .catch((caughtError: unknown) => {
        if (!ignore) {
          setError(
            caughtError instanceof Error
              ? caughtError.message
              : "Failed to load field manifest",
          );
        }
      });

    return () => {
      ignore = true;
    };
  }, []);

  function update(field: string, patch: Partial<ParameterSource>) {
    const current = sources?.[field] ?? { source_type: "assumed" as ParameterSourceType };
    onChange({ ...(sources ?? {}), [field]: { ...current, ...patch } });
  }

  function clear(field: string) {
    const next = { ...(sources ?? {}) };
    delete next[field];
    onChange(Object.keys(next).length > 0 ? next : null);
  }

  if (error) {
    return <p className="text-sm text-red-300">{error}</p>;
  }

  if (!manifest) {
    return <p className="text-sm text-slate-500">Loading field manifest…</p>;
  }

  return (
    <div className="overflow-x-auto">
      <table className="w-full min-w-160 text-left text-sm">
        <thead className="border-b border-slate-700 text-slate-400">
          <tr>
            <th className="px-3 py-3">Parameter</th>
            <th className="px-3 py-3">Value</th>
            <th className="px-3 py-3">Source type</th>
            <th className="px-3 py-3">Reference</th>
            <th className="px-3 py-3" />
          </tr>
        </thead>

        <tbody>
          {manifest.fields.map((field) => {
            const source = sources?.[field.name];
            const value = values[field.name];

            return (
              <tr key={field.name} className="border-b border-slate-800 align-top">
                <td className="px-3 py-3">
                  <p className="font-mono text-slate-200">{field.name}</p>
                  <p className="mt-1 text-xs text-slate-500">
                    {field.description}
                    {field.unit !== "-" ? ` (${field.unit})` : ""}
                  </p>
                </td>

                <td className="px-3 py-3 text-slate-300">
                  {typeof value === "number"
                    ? value
                    : field.derived_when_null
                      ? <span className="text-slate-500">derived: {field.derived_when_null}</span>
                      : "—"}
                </td>

                <td className="px-3 py-3">
                  <select
                    value={source?.source_type ?? ""}
                    disabled={disabled}
                    onChange={(event) =>
                      event.target.value
                        ? update(field.name, {
                            source_type: event.target.value as ParameterSourceType,
                          })
                        : clear(field.name)
                    }
                    className="rounded-lg border border-slate-700 bg-slate-950 px-2 py-1.5 text-white disabled:opacity-50"
                  >
                    <option value="">— not recorded —</option>
                    {manifest.source_types.map((type) => (
                      <option key={type} value={type}>
                        {type}
                      </option>
                    ))}
                  </select>
                </td>

                <td className="px-3 py-3">
                  <input
                    type="text"
                    value={source?.reference ?? ""}
                    disabled={disabled || !source}
                    maxLength={500}
                    placeholder={source ? "Report, DOI, datasheet…" : ""}
                    onChange={(event) =>
                      update(field.name, { reference: event.target.value || null })
                    }
                    className="w-full rounded-lg border border-slate-700 bg-slate-950 px-2 py-1.5 text-white disabled:opacity-50"
                  />
                </td>

                <td className="px-3 py-3">
                  {source && (
                    <button
                      type="button"
                      disabled={disabled}
                      onClick={() => clear(field.name)}
                      className="text-xs text-slate-400 hover:text-white"
                    >
                      Clear
                    </button>
                  )}
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
```

### File: `frontend/src/components/simulation/environment-assumptions-fields.tsx`
```tsx
"use client";

import { NumberField } from "@/components/forms/number-field";
import { SelectField } from "@/components/forms/select-field";
import type { EnvironmentAssumptions } from "@/types/simulation";

type Props = {
  value: EnvironmentAssumptions;
  disabled?: boolean;
  onChange: (value: EnvironmentAssumptions) => void;
};

/**
 * Rules that turn ERA5 variables into model boundary conditions (Stage 2,
 * Stage 5 adds ground albedo). Every value is echoed back in the result.
 */
export function EnvironmentAssumptionsFields({ value, disabled = false, onChange }: Props) {
  function update<K extends keyof EnvironmentAssumptions>(
    key: K,
    next: EnvironmentAssumptions[K],
  ) {
    onChange({ ...value, [key]: next });
  }

  const solarMrt = value.mean_radiant_temperature_method === "air_plus_solar_linear";
  const humidityOffset = value.sky_temperature_method === "humidity_offset";
  const fixedOffset = value.sky_temperature_method === "fixed_offset";

  return (
    <details className="rounded-xl border border-slate-800 bg-slate-950/50 p-5">
      <summary className="cursor-pointer text-lg font-semibold">
        Environment assumptions
      </summary>

      <p className="mt-2 text-sm text-slate-400">
        How ERA5 air temperature, humidity, wind and irradiance become mean
        radiant temperature, sky temperature and body-height wind. Defaults
        reproduce the Stage 1 estimates.
      </p>

      <div className="mt-4 grid gap-5 md:grid-cols-2 lg:grid-cols-4">
        <SelectField
          label="Mean radiant temperature"
          value={value.mean_radiant_temperature_method}
          disabled={disabled}
          options={[
            { value: "air_plus_solar_linear", label: "Air + linear solar gain" },
            { value: "equal_to_air", label: "Equal to air (shaded)" },
          ]}
          onChange={(v) => update("mean_radiant_temperature_method", v)}
        />

        {solarMrt && (
          <>
            <NumberField
              label="Solar MRT gain"
              suffix="K/(W/m²)"
              value={value.solar_mrt_gain_k_per_w_m2}
              min={0} max={0.05} step={0.001}
              disabled={disabled}
              onChange={(v) => update("solar_mrt_gain_k_per_w_m2", v)}
            />
            <NumberField
              label="Solar MRT cap"
              suffix="K"
              value={value.solar_mrt_gain_cap_k}
              min={0} max={40} step={0.5}
              disabled={disabled}
              onChange={(v) => update("solar_mrt_gain_cap_k", v)}
            />
          </>
        )}

        <SelectField
          label="Sky temperature"
          value={value.sky_temperature_method}
          disabled={disabled}
          options={[
            { value: "humidity_offset", label: "Humidity-dependent offset" },
            { value: "fixed_offset", label: "Fixed offset" },
            { value: "swinbank", label: "Swinbank clear sky" },
          ]}
          onChange={(v) => update("sky_temperature_method", v)}
        />

        {humidityOffset && (
          <>
            <NumberField
              label="Sky offset at 100 % RH"
              suffix="K"
              value={value.sky_offset_base_k}
              min={0} max={40} step={0.5}
              disabled={disabled}
              onChange={(v) => update("sky_offset_base_k", v)}
            />
            <NumberField
              label="Extra offset at 0 % RH"
              suffix="K"
              value={value.sky_offset_humidity_range_k}
              min={0} max={40} step={0.5}
              disabled={disabled}
              onChange={(v) => update("sky_offset_humidity_range_k", v)}
            />
          </>
        )}

        {fixedOffset && (
          <NumberField
            label="Fixed sky offset"
            suffix="K"
            value={value.fixed_sky_offset_k}
            min={0} max={50} step={0.5}
            disabled={disabled}
            onChange={(v) => update("fixed_sky_offset_k", v)}
          />
        )}

        <NumberField
          label="Sky view factor"
          value={value.sky_view_factor}
          min={0} max={1} step={0.05}
          disabled={disabled}
          onChange={(v) => update("sky_view_factor", v)}
        />

        <NumberField
          label="Ground albedo"
          value={value.ground_albedo}
          min={0} max={1} step={0.05}
          disabled={disabled}
          hint="Shortwave reflectance of the ground (Stage 5, ADR 0006)."
          onChange={(v) => update("ground_albedo", v)}
        />

        <NumberField
          label="Wind scaling (10 m → body)"
          value={value.wind_speed_scaling_factor}
          min={0.05} max={1.5} step={0.01}
          disabled={disabled}
          hint="0.67 ≈ logarithmic profile to 1.1 m over open terrain."
          onChange={(v) => update("wind_speed_scaling_factor", v)}
        />
      </div>
    </details>
  );
}
```

### File: `frontend/src/components/simulation/environment-input-fields.tsx`
```tsx
"use client";

import {
  NumberField,
  OptionalNumberField,
} from "@/components/forms/number-field";
import type { EnvironmentInput } from "@/types/simulation";

type EnvironmentInputFieldsProps = {
  environment: EnvironmentInput;
  disabled?: boolean;
  onChange: (environment: EnvironmentInput) => void;
};

export function EnvironmentInputFields({
  environment,
  disabled = false,
  onChange,
}: EnvironmentInputFieldsProps) {
  function update<K extends keyof EnvironmentInput>(
    key: K,
    value: EnvironmentInput[K],
  ) {
    onChange({ ...environment, [key]: value });
  }

  return (
    <div className="grid gap-5 md:grid-cols-2 lg:grid-cols-4">
      <NumberField
        label="Air Temperature"
        suffix="°C"
        value={environment.air_temperature_c}
        min={-50}
        max={70}
        step={0.1}
        disabled={disabled}
        onChange={(value) => update("air_temperature_c", value)}
      />

      <NumberField
        label="Mean Radiant Temperature"
        suffix="°C"
        value={environment.mean_radiant_temperature_c}
        min={-50}
        max={100}
        step={0.1}
        disabled={disabled}
        onChange={(value) => update("mean_radiant_temperature_c", value)}
      />

      <OptionalNumberField
        label="Sky Temperature"
        suffix="°C"
        value={environment.sky_temperature_c}
        placeholder="Derived by backend"
        min={-100}
        max={70}
        step={0.1}
        disabled={disabled}
        onChange={(value) => update("sky_temperature_c", value)}
      />

      <NumberField
        label="Relative Humidity"
        suffix="%"
        value={environment.relative_humidity_percent}
        min={0}
        max={100}
        step={1}
        disabled={disabled}
        onChange={(value) => update("relative_humidity_percent", value)}
      />

      <NumberField
        label="Wind Speed"
        suffix="m/s"
        value={environment.wind_speed_m_s}
        min={0}
        max={30}
        step={0.1}
        disabled={disabled}
        onChange={(value) => update("wind_speed_m_s", value)}
      />

      <NumberField
        label="Global Horizontal Irradiance"
        suffix="W/m²"
        value={environment.solar_radiation_w_m2}
        min={0}
        max={1500}
        step={10}
        disabled={disabled}
        onChange={(value) => update("solar_radiation_w_m2", value)}
      />

      <OptionalNumberField
        label="Direct Normal Irradiance"
        suffix="W/m²"
        value={environment.direct_normal_irradiance_w_m2}
        placeholder="Not split"
        min={0} max={1500} step={10}
        disabled={disabled}
        hint="Supply DNI and DHI together; leave both empty to treat GHI as beam."
        onChange={(value) => update("direct_normal_irradiance_w_m2", value)}
      />

      <OptionalNumberField
        label="Diffuse Horizontal Irradiance"
        suffix="W/m²"
        value={environment.diffuse_horizontal_irradiance_w_m2}
        placeholder="Not split"
        min={0} max={1500} step={10}
        disabled={disabled}
        onChange={(value) => update("diffuse_horizontal_irradiance_w_m2", value)}
      />

      <NumberField
        label="Ground Albedo"
        value={environment.ground_albedo}
        min={0} max={1} step={0.05}
        disabled={disabled}
        onChange={(value) => update("ground_albedo", value)}
      />

      <NumberField
        label="Sky View Factor"
        value={environment.sky_view_factor}
        min={0}
        max={1}
        step={0.05}
        disabled={disabled}
        onChange={(value) => update("sky_view_factor", value)}
      />
    </div>
  );
}
```

### File: `frontend/src/components/simulation/material-input-fields.tsx`
```tsx
"use client";

import {
  NumberField,
  OptionalNumberField,
} from "@/components/forms/number-field";
import { MaterialVersionPicker } from "@/components/simulation/material-version-picker";
import type { MaterialInput, ParameterSource } from "@/types/simulation";

/** Every MaterialInput key that enters the physics (i.e. not provenance/name). */
type PhysicalKey = Exclude<
  keyof MaterialInput,
  | "name"
  | "material_version_id"
  | "parameter_sources"
  | "source_type"
  | "source_reference"
  | "absorbed_solar_to_body_fraction"
>;

type MaterialInputFieldsProps = {
  material: MaterialInput;
  showName?: boolean;
  /** Show the material library picker (Stage 4). */
  enableLibrary?: boolean;
  disabled?: boolean;
  onChange: (material: MaterialInput) => void;
};

export function MaterialInputFields({
  material,
  showName = false,
  enableLibrary = false,
  disabled = false,
  onChange,
}: MaterialInputFieldsProps) {
  const linked = Boolean(material.material_version_id);

  function updatePhysical<K extends PhysicalKey>(key: K, value: MaterialInput[K]) {
    const next: MaterialInput = { ...material, [key]: value };

    if (linked) {
      // The backend rejects a version id whose values were edited; drop the
      // link (and the provenance that came with it) instead.
      next.material_version_id = null;
      next.parameter_sources = null;
      next.source_type = null;
      next.source_reference = null;
    }

    onChange(next);
  }

  return (
    <div className="space-y-5">
      {enableLibrary && (
        <MaterialVersionPicker
          material={material}
          disabled={disabled}
          onChange={onChange}
        />
      )}

      {linked && (
        <p className="text-xs text-slate-500">
          Values come from the linked library version. Editing any physical
          value removes the link so the result is not attributed to that version.
        </p>
      )}

      <div className="grid gap-5 sm:grid-cols-2">
        {showName && (
          <label className="block sm:col-span-2">
            <span className="mb-2 block text-sm text-slate-300">Material Name</span>
            <input
              type="text"
              value={material.name}
              maxLength={100}
              disabled={disabled}
              onChange={(event) => onChange({ ...material, name: event.target.value })}
              className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-white outline-none focus:border-cyan-500 disabled:cursor-not-allowed disabled:opacity-50"
            />
          </label>
        )}

        <NumberField
          label="Clothing Insulation"
          suffix="clo"
          value={material.clothing_insulation_clo}
          min={0} max={5} step={0.05}
          disabled={disabled}
          onChange={(value) => updatePhysical("clothing_insulation_clo", value)}
        />

        <OptionalNumberField
          label="Evaporative Resistance (Re,cl)"
          suffix="m²·Pa/W"
          value={material.evaporative_resistance_m2pa_w ?? null}
          placeholder="Derived from clo"
          min={0} max={1000} step={0.5}
          disabled={disabled}
          hint="Leave empty to derive R_cl / (LR · i_cl) (Stage 2)."
          onChange={(value) => updatePhysical("evaporative_resistance_m2pa_w", value)}
        />

        <OptionalNumberField
          label="Clothing Area Factor (f_cl)"
          value={material.clothing_area_factor}
          placeholder="Derived from clo"
          min={1} max={2} step={0.01}
          disabled={disabled}
          hint="Leave empty to derive 1 + 0.15 · clo (Stage 3)."
          onChange={(value) => updatePhysical("clothing_area_factor", value)}
        />

        <NumberField
          label="Solar Reflectance"
          value={material.solar_reflectance}
          min={0} max={1} step={0.01}
          disabled={disabled}
          onChange={(value) => updatePhysical("solar_reflectance", value)}
        />

        <NumberField
          label="Solar Transmittance"
          value={material.solar_transmittance}
          min={0} max={1} step={0.01}
          disabled={disabled}
          onChange={(value) => updatePhysical("solar_transmittance", value)}
        />

        <NumberField
          label="Infrared Emissivity"
          value={material.infrared_emissivity}
          min={0} max={1} step={0.01}
          disabled={disabled}
          onChange={(value) => updatePhysical("infrared_emissivity", value)}
        />

        <NumberField
          label="Infrared Transmittance"
          value={material.infrared_transmittance ?? 0}
          min={0} max={1} step={0.01}
          disabled={disabled}
          hint="Emissivity + transmittance must not exceed 1."
          onChange={(value) => updatePhysical("infrared_transmittance", value)}
        />

        <NumberField
          label="Projected Solar Area Factor"
          value={material.projected_solar_area_factor}
          min={0} max={1} step={0.01}
          disabled={disabled}
          onChange={(value) => updatePhysical("projected_solar_area_factor", value)}
        />
      </div>

      <ProvenanceBadges sources={material.parameter_sources} />
    </div>
  );
}

function ProvenanceBadges({
  sources,
}: {
  sources: Record<string, ParameterSource> | null | undefined;
}) {
  const entries = Object.entries(sources ?? {});

  if (entries.length === 0) {
    return null;
  }

  return (
    <div>
      <p className="text-xs font-semibold uppercase tracking-wide text-slate-500">
        Parameter provenance
      </p>

      <ul className="mt-2 flex flex-wrap gap-2">
        {entries.map(([field, source]) => (
          <li
            key={field}
            title={source.reference ?? undefined}
            className="rounded-full border border-slate-700 bg-slate-950 px-2.5 py-1 text-xs text-slate-300"
          >
            <span className="font-mono">{field}</span>
            <span className="ml-1 text-cyan-300">{source.source_type}</span>
            {source.reference && (
              <span className="ml-1 text-slate-500">— {source.reference}</span>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
```

### File: `frontend/src/components/simulation/material-version-picker.tsx`
```tsx
"use client";

import { useEffect, useState } from "react";

import {
  getMaterialSimulationInput,
  getMaterialVersions,
} from "@/lib/api-client";
import type { MaterialVersionListItem } from "@/types/material";
import type { MaterialInput } from "@/types/simulation";

type MaterialVersionPickerProps = {
  material: MaterialInput;
  disabled?: boolean;
  onChange: (material: MaterialInput) => void;
};

/**
 * Links a MaterialInput to an immutable material library version. Selecting a
 * version loads the backend's `simulation-input` projection, so the values
 * shown are exactly what the backend will verify against on submit.
 */
export function MaterialVersionPicker({
  material,
  disabled = false,
  onChange,
}: MaterialVersionPickerProps) {
  const [versions, setVersions] = useState<MaterialVersionListItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [applying, setApplying] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    let ignore = false;

    getMaterialVersions()
      .then((response) => {
        if (!ignore) setVersions(response.items);
      })
      .catch((caughtError: unknown) => {
        if (!ignore) {
          setError(
            caughtError instanceof Error
              ? caughtError.message
              : "Failed to load material library",
          );
        }
      })
      .finally(() => {
        if (!ignore) setLoading(false);
      });

    return () => {
      ignore = true;
    };
  }, []);

  const linked = material.material_version_id
    ? versions.find((v) => v.id === material.material_version_id) ?? null
    : null;

  async function applyVersion(versionId: string) {
    if (!versionId) {
      unlink();
      return;
    }

    setApplying(true);
    setError("");

    try {
      const input = await getMaterialSimulationInput(versionId);
      onChange(input);
    } catch (caughtError) {
      setError(
        caughtError instanceof Error
          ? caughtError.message
          : "Failed to apply material version",
      );
    } finally {
      setApplying(false);
    }
  }

  function unlink() {
    onChange({
      ...material,
      material_version_id: null,
      parameter_sources: null,
      source_type: null,
      source_reference: null,
    });
  }

  const grouped = new Map<string, MaterialVersionListItem[]>();
  for (const version of versions) {
    const list = grouped.get(version.material_name) ?? [];
    list.push(version);
    grouped.set(version.material_name, list);
  }

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-950/60 p-4">
      <label className="block">
        <span className="mb-2 block text-sm text-slate-300">
          Material library
        </span>

        <select
          value={material.material_version_id ?? ""}
          disabled={disabled || loading || applying}
          onChange={(event) => void applyVersion(event.target.value)}
          className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-white outline-none focus:border-cyan-500 disabled:cursor-not-allowed disabled:opacity-50"
        >
          <option value="">
            {loading ? "Loading library…" : "— Manual values (not linked) —"}
          </option>

          {Array.from(grouped.entries()).map(([name, items]) => (
            <optgroup key={name} label={name}>
              {items.map((version) => (
                <option key={version.id} value={version.id}>
                  v{version.version_number} · {version.clothing_insulation_clo} clo · ρ
                  {version.solar_reflectance.toFixed(2)} · ε
                  {version.infrared_emissivity.toFixed(2)}
                  {version.infrared_transmittance > 0
                    ? ` · τ_IR ${version.infrared_transmittance.toFixed(2)}`
                    : ""}
                </option>
              ))}
            </optgroup>
          ))}
        </select>
      </label>

      {material.material_version_id && (
        <div className="mt-3 flex flex-wrap items-center justify-between gap-3 text-xs">
          <span className="rounded-full border border-emerald-800 bg-emerald-950 px-2.5 py-1 text-emerald-300">
            Linked to{" "}
            {linked
              ? `${linked.material_name} v${linked.version_number}`
              : material.material_version_id}
            {material.source_type ? ` · ${material.source_type}` : ""}
          </span>

          <button
            type="button"
            onClick={unlink}
            disabled={disabled}
            className="text-slate-400 underline-offset-2 hover:text-white hover:underline"
          >
            Unlink
          </button>
        </div>
      )}

      {applying && (
        <p className="mt-2 text-xs text-slate-500">Loading version parameters…</p>
      )}

      {error && (
        <p role="alert" className="mt-2 text-xs text-red-300">
          {error}
        </p>
      )}
    </div>
  );
}
```

### File: `frontend/src/components/simulation/model-provenance-panel.tsx`
```tsx
import { formatNumber } from "@/lib/format";
import type {
  ResolvedParameterSource,
  ScenarioResult,
  SimulationResponse,
} from "@/types/simulation";

type ModelProvenancePanelProps = {
  result: SimulationResponse;
};

type ResolvedRow = {
  label: string;
  render: (scenario: ScenarioResult) => string;
};

function sourceLabel(
  source: ResolvedParameterSource | null | undefined,
): string {
  switch (source) {
    case "material_input":
      return "material input";
    case "derived_from_clo":
      return "derived from clo";
    default:
      return "";
  }
}

function withSource(
  value: string,
  source: ResolvedParameterSource | null | undefined,
): string {
  const label = sourceLabel(source);

  return label && value !== "—" ? `${value} (${label})` : value;
}

const resolvedRows: ResolvedRow[] = [
  {
    label: "Dry resistance",
    render: (scenario) =>
      formatNumber(scenario.clothing?.dry_resistance_m2k_w, 4, " m²·K/W"),
  },
  {
    label: "Evaporative resistance",
    render: (scenario) =>
      withSource(
        formatNumber(
          scenario.clothing?.evaporative_resistance_m2pa_w,
          2,
          " m²·Pa/W",
        ),
        scenario.clothing?.evaporative_resistance_source,
      ),
  },
  {
    label: "Clothing area factor (f_cl)",
    render: (scenario) =>
      withSource(
        formatNumber(scenario.clothing?.clothing_area_factor, 3),
        scenario.clothing?.clothing_area_factor_source,
      ),
  },
  {
    label: "Infrared transmittance",
    render: (scenario) =>
      formatNumber(scenario.clothing?.infrared_transmittance, 3),
  },
  {
    label: "Body mass",
    render: (scenario) => formatNumber(scenario.body?.body_mass_kg, 1, " kg"),
  },
  {
    label: "Body surface area",
    render: (scenario) =>
      formatNumber(scenario.body?.body_surface_area_m2, 2, " m²"),
  },
  {
    label: "Core heat capacity",
    render: (scenario) =>
      formatNumber(scenario.body?.core_heat_capacity_j_m2k, 0, " J/(m²·K)"),
  },
  {
    label: "Skin heat capacity",
    render: (scenario) =>
      formatNumber(scenario.body?.skin_heat_capacity_j_m2k, 0, " J/(m²·K)"),
  },
  {
    label: "Posture / A_r/A_D",
    render: (scenario) =>
      scenario.body?.position
        ? `${scenario.body.position} (${formatNumber(scenario.body.effective_radiation_area_ratio, 2)})`
        : "—",
  },
];

export function ModelProvenancePanel({ result }: ModelProvenancePanelProps) {
  const metadata = result.model_metadata ?? null;
  const scenarios = [result.control, result.radiative_cooling];

  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="text-xl font-semibold">Model Provenance</h2>

      <p className="mt-2 text-sm text-slate-400">
        Model and parameter-set identifiers written into this result, plus the
        clothing and body quantities the solver actually used.
      </p>

      <dl className="mt-5 grid gap-4 text-sm sm:grid-cols-2 lg:grid-cols-4">
        <div>
          <dt className="text-slate-500">Model</dt>
          <dd className="mt-1 text-slate-200">{result.model_name}</dd>
        </div>

        <div>
          <dt className="text-slate-500">Model version</dt>
          <dd className="mt-1 font-mono text-cyan-300">{result.model_version}</dd>
        </div>

        <div>
          <dt className="text-slate-500">Parameter set version</dt>
          <dd className="mt-1 font-mono text-cyan-300">
            {metadata?.parameter_set_version ?? "—"}
          </dd>
        </div>

        <div>
          <dt className="text-slate-500">Parameter set SHA-256</dt>
          <dd
            className="mt-1 font-mono text-slate-300"
            title={metadata?.parameter_set_sha256}
          >
            {metadata ? `${metadata.parameter_set_sha256.slice(0, 12)}…` : "—"}
          </dd>
        </div>
      </dl>

      <div className="mt-6 overflow-x-auto">
        <table className="w-full min-w-160 text-left text-sm">
          <thead className="border-b border-slate-700 text-slate-400">
            <tr>
              <th className="px-3 py-3">Resolved quantity</th>
              {scenarios.map((scenario) => (
                <th key={scenario.material_name} className="px-3 py-3">
                  {scenario.material_name}
                </th>
              ))}
            </tr>
          </thead>

          <tbody>
            {resolvedRows.map((row) => (
              <tr key={row.label} className="border-b border-slate-800">
                <td className="px-3 py-3 text-slate-300">{row.label}</td>
                {scenarios.map((scenario) => (
                  <td
                    key={`${row.label}-${scenario.material_name}`}
                    className="px-3 py-3 text-slate-200"
                  >
                    {row.render(scenario)}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="mt-6 grid gap-6 lg:grid-cols-2">
        {scenarios.map((scenario) => {
          const assumptions = scenario.assumptions_applied ?? [];

          return (
            <div key={scenario.material_name}>
              <h3 className="text-sm font-semibold text-slate-300">
                Assumptions applied — {scenario.material_name}
              </h3>

              {assumptions.length === 0 ? (
                <p className="mt-2 text-sm text-slate-500">
                  No assumptions were recorded for this scenario.
                </p>
              ) : (
                <ul className="mt-2 list-inside list-disc space-y-1 text-sm text-slate-400">
                  {assumptions.map((assumption) => (
                    <li key={assumption}>{assumption}</li>
                  ))}
                </ul>
              )}
            </div>
          );
        })}
      </div>
    </section>
  );
}
```

### File: `frontend/src/components/simulation/model-quality-panel.tsx`
```tsx
import type {
  SimulationResponse,
} from "@/types/simulation";

type ModelQualityPanelProps = {
  result: SimulationResponse;
};

function residualColor(value: number): string {
  if (value < 0.5) {
    return "text-emerald-300";
  }

  if (value < 2.0) {
    return "text-amber-300";
  }

  return "text-red-300";
}

export function ModelQualityPanel({
  result,
}: ModelQualityPanelProps) {
  const control =
    result.control.diagnostics;

  const rc =
    result.radiative_cooling.diagnostics;

  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="text-xl font-semibold">
        Numerical computation quality
      </h2>

      <p className="mt-2 text-sm text-slate-400">
        The closer the energy residual is to 0%, the more consistent the integral heat flux is with the changes in human body energy storage.
      </p>

      <div className="mt-5 overflow-x-auto">
        <table className="w-full min-w-175 text-left text-sm">
          <thead className="border-b border-slate-700 text-slate-400">
            <tr>
              <th className="px-3 py-3">
                Scenario
              </th>
              <th className="px-3 py-3">
                Energy Residual
              </th>
              <th className="px-3 py-3">
                Stored Energy Change
              </th>
              <th className="px-3 py-3">
                Integrated Net Heat
              </th>
              <th className="px-3 py-3">
                Solver Function Evaluations
              </th>
            </tr>
          </thead>

          <tbody>
            {[
              {
                name: result.control.material_name,
                diagnostics: control,
              },
              {
                name:
                  result.radiative_cooling
                    .material_name,
                diagnostics: rc,
              },
            ].map((item) => (
              <tr
                key={item.name}
                className="border-b border-slate-800"
              >
                <td className="px-3 py-4">
                  {item.name}
                </td>

                <td
                  className={`px-3 py-4 font-semibold ${residualColor(
                    item.diagnostics
                      .normalized_residual_percent,
                  )}`}
                >
                  {item.diagnostics
                    .normalized_residual_percent
                    .toFixed(4)}
                  %
                </td>

                <td className="px-3 py-4">
                  {item.diagnostics
                    .stored_energy_change_j_m2
                    .toFixed(1)}
                  {" J/m²"}
                </td>

                <td className="px-3 py-4">
                  {item.diagnostics
                    .integrated_net_heat_j_m2
                    .toFixed(1)}
                  {" J/m²"}
                </td>

                <td className="px-3 py-4">
                  {
                    item.diagnostics
                      .solver_function_evaluations
                  }
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
```

### File: `frontend/src/components/simulation/person-input-fields.tsx`
```tsx
"use client";

import { NumberField } from "@/components/forms/number-field";
import { SelectField } from "@/components/forms/select-field";
import type { PersonInput } from "@/types/simulation";

type PersonInputFieldsProps = {
  person: PersonInput;
  disabled?: boolean;
  onChange: (person: PersonInput) => void;
};

export function PersonInputFields({
  person,
  disabled = false,
  onChange,
}: PersonInputFieldsProps) {
  function update<K extends keyof PersonInput>(key: K, value: PersonInput[K]) {
    onChange({ ...person, [key]: value });
  }

  return (
    <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-6">
      <NumberField
        label="Activity Level"
        suffix="MET"
        value={person.met}
        min={0.7}
        max={10}
        step={0.1}
        disabled={disabled}
        onChange={(value) => update("met", value)}
      />

      <NumberField
        label="Body Mass"
        suffix="kg"
        value={person.body_mass_kg}
        min={30}
        max={200}
        step={0.5}
        disabled={disabled}
        hint="Sets the core and skin heat capacities (Stage 3)."
        onChange={(value) => update("body_mass_kg", value)}
      />

      <NumberField
        label="Body Surface Area"
        suffix="m²"
        value={person.body_surface_area_m2}
        min={1}
        max={3}
        step={0.01}
        disabled={disabled}
        onChange={(value) => update("body_surface_area_m2", value)}
      />

      <NumberField
        label="Initial Core Temperature"
        suffix="°C"
        value={person.initial_core_temperature_c}
        min={34}
        max={40}
        step={0.1}
        disabled={disabled}
        onChange={(value) => update("initial_core_temperature_c", value)}
      />

      <NumberField
        label="Initial Skin Temperature"
        suffix="°C"
        value={person.initial_skin_temperature_c}
        min={20}
        max={40}
        step={0.1}
        disabled={disabled}
        onChange={(value) => update("initial_skin_temperature_c", value)}
      />

      <SelectField
        label="Posture"
        value={person.position}
        disabled={disabled}
        options={[
          { value: "standing", label: "Standing (A_r/A_D = 0.73)" },
          { value: "sitting", label: "Sitting (A_r/A_D = 0.70)" },
        ]}
        hint="Effective radiation area for longwave and diffuse solar (Stage 5)."
        onChange={(value) => update("position", value)}
      />
    </div>
  );
}
```

### File: `frontend/src/config/navigation.ts`
```typescript
export type NavLink = {
  href: string;
  label: string;
};

export const NAV_LINKS: NavLink[] = [
  { href: "/simulations", label: "Simulations" },
  { href: "/materials", label: "Materials" },
  { href: "/global-analysis", label: "Global Analysis" },
  { href: "/benchmarks/gagge", label: "Gagge Benchmark" },
];

```

### File: `frontend/src/lib/api-client.ts`
```typescript
import type {
  GaggeBenchmarkRequest,
  GaggeBenchmarkResponse,
} from "@/types/benchmark";
import type {
  GeoJsonFeatureCollection,
  GlobalBatch,
  GlobalBatchCreate,
  GlobalBatchDetail,
  GlobalBatchEstimate,
  GlobalCity,
} from "@/types/global-batch";
import type {
  Material, MaterialCreate, MaterialListResponse,
  MaterialVersionListResponse,
} from "@/types/material";
import type {
  City,
  MaterialInput,
  SimulationJob,
  SimulationJobDetail,
  SimulationJobList,
  SimulationRequest,
  SimulationResponse,
  WeatherSimulationRequest,
  WeatherSimulationResponse,
  WeatherTimeSeries,
  MaterialFieldManifest, 
  ModelMetadata, 
  ModelParameterManifest,
} from "@/types/simulation";


const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_BASE_URL ??
  "http://localhost:8000";


/**
 * 嘗試從後端回應中取得可讀的錯誤訊息。
 *
 * FastAPI 的 detail 可能是：
 * 1. 字串
 * 2. Pydantic 驗證錯誤陣列
 * 3. 其他 JSON 物件
 */
async function getErrorMessage(
  response: Response,
  fallbackMessage: string,
): Promise<string> {
  const errorBody: unknown = await response
    .json()
    .catch(() => null);

  if (
    typeof errorBody === "object" &&
    errorBody !== null &&
    "detail" in errorBody
  ) {
    const detail = (
      errorBody as {
        detail?: unknown;
      }
    ).detail;

    if (typeof detail === "object" && detail !== null && "message" in detail) {
      const { code, message } = detail as { code?: string; message?: string };
      return code ? `${message} [${code}]` : String(message);
    }

    if (typeof detail === "string") {
      return detail;
    }

    if (detail !== undefined) {
      return JSON.stringify(detail);
    }
  }
  
  return `${fallbackMessage}：HTTP ${response.status}`;
}

export async function runSimulation(
  request: SimulationRequest,
): Promise<SimulationResponse> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/simulations/run`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(request),
    },
  );

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(
        response,
        "Simulation request failed",
      ),
    );
  }

  return response.json() as Promise<SimulationResponse>;
}


export async function getCities(): Promise<City[]> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/weather/cities`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(
        response,
        "Failed to fetch city list",
      ),
    );
  }

  return response.json() as Promise<City[]>;
}


export async function getWeatherHistory(
  cityId: string,
  startTimeLocal: string,
  durationMinutes: number,
): Promise<WeatherTimeSeries> {
  const parameters = new URLSearchParams({
    city_id: cityId,
    start_time_local: startTimeLocal,
    duration_minutes: String(durationMinutes),
  });

  const response = await fetch(
    `${API_BASE_URL}/api/v1/weather/history?${parameters.toString()}`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(
        response,
        "Failed to fetch weather history",
      ),
    );
  }

  return response.json() as Promise<WeatherTimeSeries>;
}

export async function runWeatherSimulation(
  request: WeatherSimulationRequest,
): Promise<WeatherSimulationResponse> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/simulations/run-weather`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(request),
    },
  );

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(
        response,
        "Weather simulation failed",
      ),
    );
  }

  return response.json() as Promise<WeatherSimulationResponse>;
}


export async function createSimulationJob(
  request: WeatherSimulationRequest,
): Promise<SimulationJob> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/simulations/jobs`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(request),
    },
  );

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(
        response,
        "Failed to create simulation job",
      ),
    );
  }

  return response.json() as Promise<SimulationJob>;
}

export async function getSimulationJob(
  jobId: string,
): Promise<SimulationJobDetail> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/simulations/jobs/${encodeURIComponent(jobId)}`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(
        response,
        "Failed to fetch simulation job",
      ),
    );
  }

  return response.json() as Promise<SimulationJobDetail>;
}



export async function getSimulationJobs(
  limit = 20,
  offset = 0,
  materialVersionId?: string,
): Promise<SimulationJobList> {
  const parameters = new URLSearchParams({
    limit: String(limit),
    offset: String(offset),
  });

  if (materialVersionId) {
    parameters.set("material_version_id", materialVersionId);
  }
  
  const response = await fetch(
    `${API_BASE_URL}/api/v1/simulations/jobs?${parameters.toString()}`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(
        response,
        "Failed to fetch simulation job list",
      ),
    );
  }

  return response.json() as Promise<SimulationJobList>;
}


export async function getSimulationResult(
  jobId: string,
): Promise<WeatherSimulationResponse> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/simulations/jobs/${encodeURIComponent(jobId)}/result`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(
        response,
        "Failed to fetch simulation result",
      ),
    );
  }

  return response.json() as Promise<WeatherSimulationResponse>;
}


export async function cancelSimulationJob(
  jobId: string,
): Promise<SimulationJob> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/simulations/jobs/${encodeURIComponent(jobId)}/cancel`,
    {
      method: "POST",
    },
  );

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(
        response,
        "Failed to cancel simulation job",
      ),
    );
  }

  return response.json() as Promise<SimulationJob>;
}


export function getSimulationEventsUrl(
  jobId: string,
): string {
  return (
    `${API_BASE_URL}/api/v1/simulations/jobs/` +
    `${encodeURIComponent(jobId)}/events`
  );
}



export async function getMaterials(
  search = "",
): Promise<MaterialListResponse> {
  const parameters = new URLSearchParams();

  if (search) {
    parameters.set("search", search);
  }

  const response = await fetch(
    `${API_BASE_URL}/api/v1/materials?${parameters}`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error("Failed to fetch material list");
  }

  return response.json();
}


export async function getMaterial(
  materialId: string,
): Promise<Material> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/materials/${materialId}`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error("Failed to fetch material");
  }

  return response.json();
}


export async function createMaterial(
  request: MaterialCreate,
): Promise<Material> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/materials`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(request),
    },
  );

  if (!response.ok) {
    const body = await response
      .json()
      .catch(() => null);

    throw new Error(
      body?.detail ?? "Failed to create material",
    );
  }

  return response.json();
}


export async function uploadMaterialSpectrum(
  versionId: string,
  spectrumType: string,
  file: File,
) {
  const formData = new FormData();

  formData.append(
    "spectrum_type",
    spectrumType,
  );

  formData.append(
    "file",
    file,
  );

  const response = await fetch(
    `${API_BASE_URL}/api/v1/materials/versions/${versionId}/spectra`,
    {
      method: "POST",
      body: formData,
    },
  );

  if (!response.ok) {
    const body = await response
      .json()
      .catch(() => null);

    throw new Error(
      body?.detail ?? "Failed to upload spectrum",
    );
  }

  return response.json();
}


export async function getMaterialSimulationInput(
  versionId: string,
): Promise<MaterialInput> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/materials/versions/${encodeURIComponent(versionId)}/simulation-input`,
    { cache: "no-store" },
  );

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(response, "Failed to fetch material simulation input"),
    );
  }

  return response.json() as Promise<MaterialInput>;
}

export async function getMaterialFieldManifest(): Promise<MaterialFieldManifest> {
  const response = await fetch(`${API_BASE_URL}/api/v1/model/material-fields`);

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(response, "Failed to fetch material field manifest"),
    );
  }

  return response.json() as Promise<MaterialFieldManifest>;
}

export async function getModelMetadata(): Promise<ModelMetadata> {
  const response = await fetch(`${API_BASE_URL}/api/v1/model/metadata`);

  if (!response.ok) {
    throw new Error(await getErrorMessage(response, "Failed to fetch model metadata"));
  }

  return response.json() as Promise<ModelMetadata>;
}

export async function getModelParameters(): Promise<ModelParameterManifest> {
  const response = await fetch(`${API_BASE_URL}/api/v1/model/parameters`);

  if (!response.ok) {
    throw new Error(await getErrorMessage(response, "Failed to fetch model parameters"));
  }

  return response.json() as Promise<ModelParameterManifest>;
}

export function getSimulationExportUrl(
  jobId: string,
  format: "csv" | "json",
): string {
  return (
    `${API_BASE_URL}/api/v1/simulations/jobs/` +
    `${jobId}/export?format=${format}`
  );
}


export async function getGlobalCities(): Promise<
  GlobalCity[]
> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/global-batches/cities`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error(
      "Unable to load supported cities",
    );
  }

  const body = await response.json();

  return body.items;
}


export async function createGlobalBatch(
  request: GlobalBatchCreate,
): Promise<GlobalBatch> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/global-batches`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(request),
    },
  );

  if (!response.ok) {
    const body = await response
      .json()
      .catch(() => null);

    throw new Error(
      body?.detail
      ?? "Unable to create global batch",
    );
  }

  return response.json();
}

export async function estimateGlobalBatch(
  request: GlobalBatchCreate,
): Promise<GlobalBatchEstimate> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/global-batches/estimate`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(request),
    },
  );

  if (!response.ok) {
    const body = await response
      .json()
      .catch(() => null);

    throw new Error(
      body?.detail
      ?? "Unable to estimate global batch",
    );
  }

  return response.json();
}

export async function getGlobalBatch(
  batchId: string,
): Promise<GlobalBatchDetail> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/global-batches/${batchId}`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error(
      "Unable to load global batch",
    );
  }

  return response.json();
}


export async function getGlobalBatchGeoJson(
  batchId: string,
): Promise<GeoJsonFeatureCollection> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/global-batches/${batchId}/geojson`,
    {
      cache: "no-store",
    },
  );

  if (!response.ok) {
    throw new Error(
      "Unable to load global map data",
    );
  }

  return response.json();
}


export async function cancelGlobalBatch(
  batchId: string,
): Promise<GlobalBatch> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/global-batches/${batchId}/cancel`,
    {
      method: "POST",
    },
  );

  if (!response.ok) {
    const body = await response
      .json()
      .catch(() => null);

    throw new Error(
      body?.detail
      ?? "Unable to cancel global batch",
    );
  }

  return response.json();
}

export async function retryFailedGlobalBatchCities(
  batchId: string,
): Promise<GlobalBatch> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/global-batches/${batchId}/retry-failed`,
    {
      method: "POST",
    },
  );

  if (!response.ok) {
    const body = await response
      .json()
      .catch(() => null);

    throw new Error(
      body?.detail
      ?? "Unable to retry failed cities",
    );
  }

  return response.json();
}


export function getGlobalBatchExportUrl(
  batchId: string,
): string {
  return (
    `${API_BASE_URL}/api/v1/` +
    `global-batches/${batchId}/export`
  );
}

export async function compareWithGagge(
  request: GaggeBenchmarkRequest,
): Promise<GaggeBenchmarkResponse> {
  const response = await fetch(`${API_BASE_URL}/api/v1/benchmarks/gagge`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(request),
  });

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(response, "Gagge benchmark request failed"),
    );
  }

  return response.json() as Promise<GaggeBenchmarkResponse>;
}

export async function getMaterialVersions(
  includeArchived = false,
  limit = 200,
): Promise<MaterialVersionListResponse> {
  const parameters = new URLSearchParams({
    include_archived: String(includeArchived),
    limit: String(limit),
  });

  const response = await fetch(
    `${API_BASE_URL}/api/v1/materials/versions?${parameters}`,
    { cache: "no-store" },
  );

  if (!response.ok) {
    throw new Error(
      await getErrorMessage(response, "Failed to fetch material versions"),
    );
  }

  return response.json() as Promise<MaterialVersionListResponse>;
}

```

### File: `frontend/src/lib/date-defaults.test.ts`
```typescript
import { describe, expect, it } from "vitest";

import {
  getDefaultSimulationDateTime,
  getPreviousCompleteYear,
} from "@/lib/date-defaults";

describe("date defaults", () => {
  it("uses the previous calendar year", () => {
    expect(getPreviousCompleteYear(new Date("2026-03-01T00:00:00"))).toBe(2025);
  });

  it("builds a datetime-local string for 15 July 10:00", () => {
    expect(getDefaultSimulationDateTime(new Date("2026-03-01T00:00:00"))).toBe(
      "2025-07-15T10:00",
    );
  });

  it("rejects invalid dates", () => {
    expect(() => getPreviousCompleteYear(new Date("nope"))).toThrow();
  });
  it("matches the datetime-local value format exactly", () => {
    expect(getDefaultSimulationDateTime(new Date("2026-03-01T00:00:00"))).toMatch(
      /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$/,
    );
  });
});
```

### File: `frontend/src/lib/date-defaults.ts`
```typescript
const DEFAULT_SIMULATION_MONTH = 7;
const DEFAULT_SIMULATION_DAY = 15;
const DEFAULT_SIMULATION_HOUR = 10;
const DEFAULT_SIMULATION_MINUTE = 0;

function padTwoDigits(value: number): string {
  return value.toString().padStart(2, "0");
}

export function getPreviousCompleteYear(now: Date = new Date()): number {
  if (Number.isNaN(now.getTime())) {
    throw new Error("A valid date is required.");
  }

  return now.getFullYear() - 1;
}

/** `YYYY-MM-DDTHH:mm`, the value format of an `<input type="datetime-local">`. */
export function getDefaultSimulationDateTime(now: Date = new Date()): string {
  const year = getPreviousCompleteYear(now);

  const date = [
    String(year),
    padTwoDigits(DEFAULT_SIMULATION_MONTH),
    padTwoDigits(DEFAULT_SIMULATION_DAY),
  ].join("-");

  const time = [
    padTwoDigits(DEFAULT_SIMULATION_HOUR),
    padTwoDigits(DEFAULT_SIMULATION_MINUTE),
  ].join(":");

  return `${date}T${time}`;
}
```

### File: `frontend/src/lib/environment-assumptions.ts`
```typescript
import type { EnvironmentAssumptions } from "@/types/simulation";

/** Mirrors the backend defaults (GET /api/v1/model/environment-assumptions/defaults). */
export const DEFAULT_ENVIRONMENT_ASSUMPTIONS: EnvironmentAssumptions = {
  mean_radiant_temperature_method: "air_plus_solar_linear",
  solar_mrt_gain_k_per_w_m2: 0.012,
  solar_mrt_gain_cap_k: 15,
  sky_temperature_method: "humidity_offset",
  sky_offset_base_k: 5,
  sky_offset_humidity_range_k: 10,
  fixed_sky_offset_k: 15,
  sky_view_factor: 0.5,
  wind_speed_scaling_factor: 1,
  ground_albedo: 0.2,
};
```

### File: `frontend/src/lib/format.test.ts`
```typescript
import { describe, expect, it } from "vitest";

import { formatNumber, formatSignedNumber } from "@/lib/format";

describe("formatNumber", () => {
  it("renders an em dash for missing or non-finite values", () => {
    expect(formatNumber(null)).toBe("—");
    expect(formatNumber(undefined)).toBe("—");
    expect(formatNumber(Number.NaN)).toBe("—");
    expect(formatNumber(Number.POSITIVE_INFINITY)).toBe("—");
  });

  it("applies digits and unit", () => {
    expect(formatNumber(1.23456, 3, " °C")).toBe("1.235 °C");
    expect(formatNumber(2)).toBe("2.00");
  });
});

describe("formatSignedNumber", () => {
  it("prefixes positive values only", () => {
    expect(formatSignedNumber(0.5, 1)).toBe("+0.5");
    expect(formatSignedNumber(-0.5, 1)).toBe("-0.5");
    expect(formatSignedNumber(0, 1)).toBe("0.0");
  });
});
```

### File: `frontend/src/lib/format.ts`
```typescript
export function formatNumber(
  value: number | null | undefined,
  digits = 2,
  unit = "",
): string {
  if (typeof value !== "number" || !Number.isFinite(value)) {
    return "—";
  }

  return `${value.toFixed(digits)}${unit}`;
}

export function formatSignedNumber(
  value: number | null | undefined,
  digits = 2,
  unit = "",
): string {
  if (typeof value !== "number" || !Number.isFinite(value)) {
    return "—";
  }

  const sign = value > 0 ? "+" : "";

  return `${sign}${value.toFixed(digits)}${unit}`;
}
```

### File: `frontend/src/lib/time-series.test.ts`
```typescript
import { describe, expect, it } from "vitest";

import { hasOptionalSeries, pluckOptionalSeries } from "@/lib/time-series";
import type { TimeSeriesPoint } from "@/types/simulation";

function point(overrides: Partial<TimeSeriesPoint> = {}): TimeSeriesPoint {
  return {
    minute: 0,
    core_temperature_c: 36.8,
    skin_temperature_c: 33.7,
    convection_w_m2: 0,
    longwave_radiation_w_m2: 0,
    evaporation_w_m2: 0,
    absorbed_solar_w_m2: 0,
    core_to_skin_w_m2: 0,
    ...overrides,
  };
}

describe("hasOptionalSeries", () => {
  it("is false when every value is absent or null", () => {
    const points = [point(), point({ skin_wettedness: null })];
    expect(hasOptionalSeries(points, "skin_wettedness")).toBe(false);
  });

  it("is true when at least one numeric value exists", () => {
    const points = [point(), point({ skin_wettedness: 0.2 })];
    expect(hasOptionalSeries(points, "skin_wettedness")).toBe(true);
  });
});

describe("pluckOptionalSeries", () => {
  it("maps missing and non-finite values to null", () => {
    const points = [
      point({ clothing_surface_temperature_c: 35.1 }),
      point({ clothing_surface_temperature_c: null }),
      point(),
      point({ clothing_surface_temperature_c: Number.NaN }),
    ];

    expect(
      pluckOptionalSeries(points, "clothing_surface_temperature_c"),
    ).toEqual([35.1, null, null, null]);
  });
});
```

### File: `frontend/src/lib/time-series.ts`
```typescript
import type { TimeSeriesPoint } from "@/types/simulation";

/** Series that may be null on the wire or absent on pre-Stage-3 results. */
export type OptionalSeriesKey =
  | "maximum_evaporation_w_m2"
  | "skin_wettedness"
  | "clothing_surface_temperature_c"
  | "skin_blood_flow_kg_h_m2"
  | "solar_incident_w_m2"
  | "solar_absorbed_by_textile_w_m2"
  | "solar_transmitted_w_m2";

export function hasOptionalSeries(
  points: TimeSeriesPoint[],
  key: OptionalSeriesKey,
): boolean {
  return points.some((point) => typeof point[key] === "number");
}

export function pluckOptionalSeries(
  points: TimeSeriesPoint[],
  key: OptionalSeriesKey,
): Array<number | null> {
  return points.map((point) => {
    const value = point[key];

    return typeof value === "number" && Number.isFinite(value) ? value : null;
  });
}
```

### File: `frontend/src/locales/en.ts`
```typescript
export const en = {
  common: {
    loading: "Loading...",
    noData: "No data available.",
    save: "Save",
    cancel: "Cancel",
    delete: "Delete",
    back: "Back",
  },

  materials: {
    title: "Material Management",
    create: "Create Material",
    edit: "Edit Material",
    loadError: "Failed to load materials.",
  },

  simulations: {
    title: "Simulation Jobs",
    create: "New Simulation",
    loading: "Loading simulation jobs...",
  },

  status: {
    pending: "Pending",
    queued: "Queued",
    running: "Running",
    completed: "Completed",
    failed: "Failed",
    cancelled: "Cancelled",
  },
} as const;
```

### File: `frontend/src/types/benchmark.ts`
```typescript
import type {
  EnvironmentInput,
  MaterialInput,
  PersonInput,
} from "@/types/simulation";

/** Acceptance thresholds on the maximum absolute trajectory difference. */
export type BenchmarkTolerances = {
  core_temperature_c: number;
  skin_temperature_c: number;
};

export type GaggeBenchmarkRequest = {
  duration_minutes: number;
  environment: EnvironmentInput;
  person: PersonInput;
  material: MaterialInput;
  tolerances: BenchmarkTolerances;
};

export type BenchmarkMetric = {
  final_difference_c: number;
  maximum_absolute_difference_c: number;
  root_mean_square_difference_c: number;
  tolerance_c: number;
  passed: boolean;
};

export type BenchmarkSeriesPoint = {
  minute: number;
  prototype_core_temperature_c: number;
  prototype_skin_temperature_c: number;
  prototype_evaporation_w_m2: number;
  reference_core_temperature_c: number;
  reference_skin_temperature_c: number;
  reference_evaporation_w_m2: number;
};

export type PrototypeBenchmarkOutput = {
  core_temperature_c: number;
  skin_temperature_c: number;
  evaporation_w_m2: number;
  skin_wettedness: number;
  skin_blood_flow_kg_h_m2: number;
  energy_residual_percent: number;
};

export type GaggeModelOutput = {
  core_temperature_c: number;
  skin_temperature_c: number;
  skin_evaporation_w_m2: number;
  skin_heat_loss_w_m2: number;
  respiratory_heat_loss_w_m2: number;
  skin_blood_flow_kg_h_m2: number;
  skin_wettedness: number;
  standard_effective_temperature_c: number;
};

/** Port vs. library after 60 minutes (the only duration the library runs). */
export type ReferencePortParity = {
  library_core_temperature_c: number;
  port_core_temperature_c: number;
  library_skin_temperature_c: number;
  port_skin_temperature_c: number;
  maximum_absolute_difference_c: number;
};

export type GaggeBenchmarkResponse = {
  reference_model: string;
  reference_library: string;
  reference_library_version: string;
  environment_note: string;
  alignment_applied: string[];
  prototype: PrototypeBenchmarkOutput;
  gagge: GaggeModelOutput;
  difference_core_temperature_c: number;
  difference_skin_temperature_c: number;
  core_temperature: BenchmarkMetric;
  skin_temperature: BenchmarkMetric;
  passed: boolean;
  time_series: BenchmarkSeriesPoint[];
  reference_port_parity: ReferencePortParity;
  warning: string;
};
```

### File: `frontend/src/types/global-batch.ts`
```typescript
import type {
  MaterialInput,
  PersonInput,
  EnvironmentAssumptions,
} from "@/types/simulation";


export type GlobalBatchStatus =
  | "queued"
  | "running"
  | "cancelling"
  | "cancelled"
  | "completed"
  | "partial_completed"
  | "failed";


export type GlobalCityStatus =
  | "queued"
  | "running"
  | "cancelled"
  | "completed"
  | "failed";


export type ExposureMatchMode =
  | "all"
  | "any";


export type AnalysisResolution =
  | "representative"
  | "daily";


export type ExecutionProfile =
  | "auto"
  | "standard"
  | "large";


export type GlobalCity = {
  id: string;
  name: string;
  country: string;
  latitude: number;
  longitude: number;
  elevation_m: number;
  timezone: string;
  climate_type: string;
};


export type GlobalBatchCreate = {
  name: string;
  city_ids: string[];

  year: number;
  start_month: number;
  end_month: number;

  analysis_resolution: AnalysisResolution;

  sample_days_per_month: number;
  daily_stride_days: number;

  execution_profile: ExecutionProfile;
  resume_from_checkpoint: boolean;

  enable_heatwave_analysis: boolean;
  heatwave_temperature_threshold_c: number;
  heatwave_minimum_consecutive_days: number;

  representative_day?: number | null;

  local_start_hour: number;
  duration_minutes: number;
  output_interval_minutes: number;

  minimum_skin_improvement_c: number;

  minimum_air_temperature_c:
    | number
    | null;

  minimum_solar_radiation_w_m2:
    | number
    | null;

  exposure_match_mode: ExposureMatchMode;

  person: PersonInput;
  control_material: MaterialInput;
  rc_material: MaterialInput;
  environment_assumptions?: EnvironmentAssumptions;
};


export type DailyAdaptationResult = {
  sample_date_local: string;
  weight_days: number;

  mean_air_temperature_c: number;
  maximum_air_temperature_c: number;

  mean_solar_radiation_w_m2: number;
  maximum_solar_radiation_w_m2: number;

  exposure_eligible: boolean;
  beneficial: boolean;

  average_skin_improvement_c: number;
  final_skin_improvement_c: number;
  average_core_improvement_c: number;
  maximum_skin_improvement_c: number;

  weather_from_cache: boolean;
};


export type MonthlyAdaptationResult = {
  month: number;

  sampled_day_count: number;
  eligible_sample_count: number;

  total_weighted_days: number;
  evaluated_weighted_days: number;
  beneficial_weighted_days: number;

  exposure_coverage_percent: number;

  climate_adaptation_rate_percent:
    | number
    | null;

  average_skin_improvement_c:
    | number
    | null;

  average_core_improvement_c:
    | number
    | null;

  maximum_skin_improvement_c:
    | number
    | null;

  samples: DailyAdaptationResult[];

  representative_date_local?:
    | string
    | null;

  weight_days?:
    | number
    | null;

  final_skin_improvement_c?:
    | number
    | null;

  beneficial?:
    | boolean
    | null;
};


export type HeatwaveEvent = {
  start_date_local: string;
  end_date_local: string;

  duration_days: number;

  mean_maximum_air_temperature_c: number;
  peak_air_temperature_c: number;

  mean_skin_improvement_c: number;
  p90_skin_improvement_c: number;

  beneficial_day_count: number;
};


export type GlobalCityResult = {
  id: string;
  batch_id: string;
  celery_task_id: string | null;

  city_id: string;
  city_name: string;
  country: string;
  latitude: number;
  longitude: number;

  status: GlobalCityStatus;
  stage: string;
  progress: number;

  climate_adaptation_rate_percent:
    | number
    | null;

  exposure_coverage_percent:
    | number
    | null;

  annual_average_skin_improvement_c:
    | number
    | null;

  annual_average_core_improvement_c:
    | number
    | null;

  maximum_skin_improvement_c:
    | number
    | null;

  effective_cooling_hours:
    | number
    | null;

  sampled_day_count:
    | number
    | null;

  eligible_sample_count:
    | number
    | null;

  evaluated_weighted_days:
    | number
    | null;

  beneficial_weighted_days:
    | number
    | null;

  completed_month_count: number;

  last_checkpoint_month:
    | number
    | null;

  resumed_from_checkpoint: boolean;

  last_heartbeat_at:
    | string
    | null;

  skin_improvement_p50_c:
    | number
    | null;

  skin_improvement_p90_c:
    | number
    | null;

  skin_improvement_p95_c:
    | number
    | null;

  core_improvement_p50_c:
    | number
    | null;

  core_improvement_p90_c:
    | number
    | null;

  core_improvement_p95_c:
    | number
    | null;

  heatwave_event_count:
    | number
    | null;

  longest_heatwave_days:
    | number
    | null;

  heatwave_events:
    | HeatwaveEvent[]
    | null;

  retry_count: number;

  monthly_results:
    | MonthlyAdaptationResult[]
    | null;

  error_message: string | null;
  started_at: string | null;
  completed_at: string | null;
};


export type GlobalBatch = {
  id: string;
  celery_group_id: string | null;

  status: GlobalBatchStatus;
  stage: string;
  progress: number;

  total_city_count: number;
  completed_city_count: number;
  failed_city_count: number;
  cancelled_city_count: number;

  summary: Record<string, unknown> | null;
  error_message: string | null;

  created_at: string;
  updated_at: string;
  started_at: string | null;
  completed_at: string | null;
  control_material_version_id?: string | null;
  rc_material_version_id?: string | null;
};


export type GlobalBatchDetail =
  GlobalBatch & {
    request: GlobalBatchCreate;
    city_results: GlobalCityResult[];
  };


export type GlobalBatchListResponse = {
  items: GlobalBatch[];
  total: number;
  limit: number;
  offset: number;
};


export type GlobalBatchEstimate = {
  city_count: number;
  month_count: number;

  samples_per_city: number;
  total_samples: number;

  thermal_simulation_count: number;
  estimated_weather_requests: number;

  analysis_resolution: AnalysisResolution;

  resolved_execution_profile:
    ExecutionProfile;

  resolved_queue: string;

  checkpoint_count_per_city: number;

  heatwave_analysis_available: boolean;
};


export type GeoJsonFeatureProperties = {
  city_id: string;
  city_name: string;
  country: string;

  status: string;

  climate_adaptation_rate_percent:
    | number
    | null;

  exposure_coverage_percent:
    | number
    | null;

  annual_average_skin_improvement_c:
    | number
    | null;

  annual_average_core_improvement_c:
    | number
    | null;

  maximum_skin_improvement_c:
    | number
    | null;

  effective_cooling_hours:
    | number
    | null;

  sampled_day_count:
    | number
    | null;

  eligible_sample_count:
    | number
    | null;

  evaluated_weighted_days:
    | number
    | null;

  beneficial_weighted_days:
    | number
    | null;

  skin_improvement_p50_c:
    | number
    | null;

  skin_improvement_p90_c:
    | number
    | null;

  skin_improvement_p95_c:
    | number
    | null;

  core_improvement_p50_c:
    | number
    | null;

  core_improvement_p90_c:
    | number
    | null;

  core_improvement_p95_c:
    | number
    | null;

  heatwave_event_count:
    | number
    | null;

  longest_heatwave_days:
    | number
    | null;
};


export type GeoJsonFeatureCollection = {
  type: "FeatureCollection";

  metadata: {
    batch_id?: string;
    status?: string;
    year?: number;
    method?: string;

    analysis_resolution?:
      AnalysisResolution;

    sample_days_per_month?: number;
    daily_stride_days?: number;

    execution_profile?:
      ExecutionProfile;

    heatwave_analysis_available?:
      boolean;

    [key: string]: unknown;
  };

  features: Array<{
    type: "Feature";

    geometry: {
      type: "Point";
      coordinates: [number, number];
    };

    properties: GeoJsonFeatureProperties;
  }>;
};
```

### File: `frontend/src/types/material.ts`
```typescript
import type { ParameterSource } from "@/types/simulation";

export type MaterialMode =
  | "ordinary"
  | "opaque_emitter"
  | "infrared_transparent"
  | "hybrid";

export type MaterialVersionInput = {
  mode: MaterialMode;
  clothing_insulation_clo: number;
  /** Stage 3: f_cl in [1, 2]; `null` = derived from clo by the backend. */
  clothing_area_factor: number | null;
  evaporative_resistance_m2pa_w: number | null;
  solar_reflectance: number;
  solar_transmittance: number;
  infrared_emissivity: number;
  infrared_transmittance: number;
  projected_solar_area_factor: number;
  absorbed_solar_to_body_fraction?: number;
  areal_density_g_m2: number | null;
  specific_heat_j_kgk: number | null;
  source_type: string;
  source_reference: string | null;
  notes: string | null;
  parameter_sources?: Record<string, ParameterSource> | null;
};

export type MaterialCreate = {
  name: string;
  slug: string;
  description: string | null;
  institution: string | null;
  initial_version: MaterialVersionInput;
};

export type SpectrumSummary = {
  id: string;
  spectrum_type: string;
  wavelength_unit: string;
  point_count: number;
  minimum_wavelength_um: number;
  maximum_wavelength_um: number;
  original_filename: string;
  file_checksum_sha256: string;
  created_at: string;
};

export type MaterialVersion = MaterialVersionInput & {
  id: string;
  material_id: string;
  version_number: number;
  created_at: string;
  spectra: SpectrumSummary[];
};

export type Material = {
  id: string;
  name: string;
  slug: string;
  description: string | null;
  institution: string | null;
  is_archived: boolean;
  created_at: string;
  updated_at: string;
  versions: MaterialVersion[];
};

export type MaterialListItem = {
  id: string;
  name: string;
  slug: string;
  institution: string | null;
  is_archived: boolean;
  latest_version_number: number | null;
  created_at: string;
};

export type MaterialListResponse = {
  items: MaterialListItem[];
  total: number;
  limit: number;
  offset: number;
};

export type MaterialVersionListItem = {
  id: string;
  material_id: string;
  material_name: string;
  material_slug: string;
  version_number: number;
  mode: string;
  clothing_insulation_clo: number;
  evaporative_resistance_m2pa_w: number | null;
  clothing_area_factor: number | null;
  solar_reflectance: number;
  solar_transmittance: number;
  infrared_emissivity: number;
  infrared_transmittance: number;
  source_type: string;
  is_archived: boolean;
  created_at: string;
};

export type MaterialVersionListResponse = {
  items: MaterialVersionListItem[];
  total: number;
  limit: number;
  offset: number;
};
```

### File: `frontend/src/types/simulation.ts`
```typescript
export type ParameterSourceType =
  | "measured"
  | "manufacturer"
  | "literature"
  | "standard"
  | "derived"
  | "assumed"
  | "manual";

export type ParameterSource = {
  source_type: ParameterSourceType;
  reference?: string | null;
  note?: string | null;
};

/** How the solver obtained a resolved clothing quantity. */
export type ResolvedParameterSource = "material_input" | "derived_from_clo";
export type MeanRadiantTemperatureMethod = "air_plus_solar_linear" | "equal_to_air";
export type SkyTemperatureMethod = "humidity_offset" | "fixed_offset" | "swinbank";

export type EnvironmentAssumptions = {
  mean_radiant_temperature_method: MeanRadiantTemperatureMethod;
  solar_mrt_gain_k_per_w_m2: number;
  solar_mrt_gain_cap_k: number;
  sky_temperature_method: SkyTemperatureMethod;
  sky_offset_base_k: number;
  sky_offset_humidity_range_k: number;
  fixed_sky_offset_k: number;
  sky_view_factor: number;
  wind_speed_scaling_factor: number;
  ground_albedo: number;
};

export type BodyPosition = "standing" | "sitting";

export type EnvironmentInput = {
  air_temperature_c: number;
  mean_radiant_temperature_c: number;
  sky_temperature_c: number | null;
  relative_humidity_percent: number;
  wind_speed_m_s: number;
  /** Global horizontal irradiance. */
  solar_radiation_w_m2: number;
  sky_view_factor: number;
  /** Stage 5: supply both DNI and DHI or neither. */
  direct_normal_irradiance_w_m2: number | null;
  diffuse_horizontal_irradiance_w_m2: number | null;
  ground_albedo: number;
};

export type PersonInput = {
  met: number;
  body_mass_kg: number;
  body_surface_area_m2: number;
  initial_core_temperature_c: number;
  initial_skin_temperature_c: number;
  /** Stage 5 (ADR 0006). */
  position: BodyPosition;
};

export type MaterialInput = {
  name: string;
  clothing_insulation_clo: number;
  /** Stage 3: f_cl in [1, 2]. `null` lets the backend derive it from clo. */
  clothing_area_factor: number | null;
  evaporative_resistance_m2pa_w?: number | null;
  solar_reflectance: number;
  solar_transmittance: number;
  infrared_emissivity: number;
  infrared_transmittance?: number;
  projected_solar_area_factor: number;
  /** @deprecated Stage 5, ignored by the backend. */ 
  absorbed_solar_to_body_fraction?: number | null;
  material_version_id?: string | null;
  parameter_sources?: Record<string, ParameterSource> | null;
  source_type?: string | null;
  source_reference?: string | null;
};

export type SimulationRequest = {
  city: string;
  duration_minutes: number;
  output_interval_minutes: number;
  environment: EnvironmentInput;
  person: PersonInput;
  control_material: MaterialInput;
  rc_material: MaterialInput;
};

/**
 * Optional members are nullable on the wire and may be absent entirely on
 * results persisted before Stage 3. Always read them defensively.
 */
export type TimeSeriesPoint = {
  minute: number;
  core_temperature_c: number;
  skin_temperature_c: number;
  convection_w_m2: number;
  longwave_radiation_w_m2: number;
  evaporation_w_m2: number;
  absorbed_solar_w_m2: number;
  core_to_skin_w_m2: number;
  maximum_evaporation_w_m2?: number | null;
  skin_wettedness?: number | null;
  /** Stage 3 */
  clothing_surface_temperature_c?: number | null;
  /** Stage 3 */
  skin_blood_flow_kg_h_m2?: number | null;
  solar_incident_w_m2?: number | null; 
  solar_absorbed_by_textile_w_m2?: number | null; 
  solar_transmitted_w_m2?: number | null;
};

export type EnergyDiagnostics = {
  stored_energy_change_j_m2: number;
  integrated_net_heat_j_m2: number;
  energy_residual_j_m2: number;
  normalized_residual_percent: number;
  maximum_core_step_c: number;
  maximum_skin_step_c: number;
  solver_function_evaluations: number;
};

export type ClothingSummary = {
  dry_resistance_m2k_w: number;
  evaporative_resistance_m2pa_w: number;
  evaporative_resistance_source: ResolvedParameterSource;
  infrared_transmittance: number;
  /** Stage 3 */
  clothing_area_factor?: number | null;
  /** Stage 3 */
  clothing_area_factor_source?: ResolvedParameterSource | null;
};

/** Stage 3 (ADR 0001): heat capacities derived from PersonInput. */
export type BodyThermalSummary = {
  body_mass_kg: number;
  body_surface_area_m2: number;
  core_heat_capacity_j_m2k: number;
  skin_heat_capacity_j_m2k: number;
  position?: BodyPosition | null;
  effective_radiation_area_ratio?: number | null;
};

export type ScenarioResult = {
  material_name: string;
  time_series: TimeSeriesPoint[];
  final_core_temperature_c: number;
  final_skin_temperature_c: number;
  peak_core_temperature_c: number;
  peak_skin_temperature_c: number;
  diagnostics: EnergyDiagnostics;
  assumptions_applied?: string[];
  clothing?: ClothingSummary | null;
  /** Stage 3 */
  body?: BodyThermalSummary | null;
};

export type ModelMetadata = {
  parameter_set_version: string;
  parameter_set_sha256: string;
};

export type SimulationSummary = {
  final_skin_temperature_improvement_c: number;
  final_core_temperature_improvement_c: number;
  average_skin_temperature_improvement_c: number;
};

export type SimulationResponse = {
  model_name: string;
  model_version: string;
  model_metadata?: ModelMetadata | null;
  city: string;
  duration_minutes: number;
  control: ScenarioResult;
  radiative_cooling: ScenarioResult;
  summary: SimulationSummary;
  warning: string;
};

export type City = {
  id: string;
  name: string;
  country: string;
  latitude: number;
  longitude: number;
  elevation_m: number;
  timezone: string;
  climate_type: string;
};

export type WeatherPoint = {
  timestamp: string;
  air_temperature_c: number;
  relative_humidity_percent: number;
  wind_speed_m_s: number;
  ghi_w_m2: number;
  direct_radiation_w_m2: number;
  diffuse_radiation_w_m2: number;
  dni_w_m2: number;
};

export type WeatherTimeSeries = {
  city: City;
  requested_start_time: string;
  requested_end_time: string;
  points: WeatherPoint[];
  source: {
    provider: string;
    dataset: string;
    model: string;
    latitude: number;
    longitude: number;
    elevation_m: number;
    timezone: string;
    downloaded_at: string;
    from_cache: boolean;
    attribution: string;
  };
};

export type WeatherSimulationRequest = {
  city_id: string;
  start_time_local: string;
  duration_minutes: number;
  output_interval_minutes: number;
  person: PersonInput;
  control_material: MaterialInput;
  rc_material: MaterialInput;
  environment_assumptions?: EnvironmentAssumptions;
};

export type WeatherSimulationResponse = SimulationResponse & {
  weather: WeatherTimeSeries;
  environment_model_note: string;
  environment_assumptions?: EnvironmentAssumptions | null;
};

export type SimulationJobStatus =
  | "queued"
  | "running"
  | "cancelling"
  | "cancelled"
  | "completed"
  | "failed";

export type SimulationJob = {
  id: string;
  celery_task_id: string | null;
  status: SimulationJobStatus;
  stage: string;
  progress: number;
  city_id: string;
  summary: Record<string, number> | null;
  error_message: string | null;
  created_at: string;
  updated_at: string;
  started_at: string | null;
  completed_at: string | null;
  control_material_version_id?: string | null;
  rc_material_version_id?: string | null;
};

export type SimulationJobDetail = SimulationJob & {
  request: WeatherSimulationRequest;
};

export type SimulationJobList = {
  items: SimulationJob[];
  total: number;
  limit: number;
  offset: number;
};

export type MaterialFieldDescriptor = {
  name: string;
  unit: string;
  description: string;
  minimum: number | null;
  maximum: number | null;
  default: number | null;
  nullable: boolean;
  derived_when_null: string | null;
};

export type MaterialFieldManifest = ModelMetadata & {
  source_types: ParameterSourceType[];
  fields: MaterialFieldDescriptor[];
};

export type ModelParameter = {
  name: string;
  value: number;
  unit: string;
  description: string;
  source_type: ParameterSourceType;
  reference: string;
  note: string | null;
};

export type ModelParameterManifest = ModelMetadata & {
  parameters: ModelParameter[];
};
```

### File: `.stage-3-api-contract-before.json`
```json
{
  "components": {
    "schemas": {
      "Body_upload_material_spectrum_api_v1_materials_versions__version_id__spectra_post": {
        "properties": {
          "file": {
            "contentMediaType": "application/octet-stream",
            "title": "File",
            "type": "string"
          },
          "spectrum_type": {
            "title": "Spectrum Type",
            "type": "string"
          }
        },
        "required": [
          "spectrum_type",
          "file"
        ],
        "title": "Body_upload_material_spectrum_api_v1_materials_versions__version_id__spectra_post",
        "type": "object"
      },
      "CityResponse": {
        "properties": {
          "climate_type": {
            "title": "Climate Type",
            "type": "string"
          },
          "country": {
            "title": "Country",
            "type": "string"
          },
          "elevation_m": {
            "title": "Elevation M",
            "type": "number"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "latitude": {
            "title": "Latitude",
            "type": "number"
          },
          "longitude": {
            "title": "Longitude",
            "type": "number"
          },
          "name": {
            "title": "Name",
            "type": "string"
          },
          "timezone": {
            "title": "Timezone",
            "type": "string"
          }
        },
        "required": [
          "id",
          "name",
          "country",
          "latitude",
          "longitude",
          "elevation_m",
          "timezone",
          "climate_type"
        ],
        "title": "CityResponse",
        "type": "object"
      },
      "ClothingSummary": {
        "description": "Resolved clothing resistances actually used by the solver.",
        "properties": {
          "dry_resistance_m2k_w": {
            "title": "Dry Resistance M2K W",
            "type": "number"
          },
          "evaporative_resistance_m2pa_w": {
            "title": "Evaporative Resistance M2Pa W",
            "type": "number"
          },
          "evaporative_resistance_source": {
            "enum": [
              "material_input",
              "derived_from_clo"
            ],
            "title": "Evaporative Resistance Source",
            "type": "string"
          },
          "infrared_transmittance": {
            "title": "Infrared Transmittance",
            "type": "number"
          }
        },
        "required": [
          "dry_resistance_m2k_w",
          "evaporative_resistance_m2pa_w",
          "evaporative_resistance_source",
          "infrared_transmittance"
        ],
        "title": "ClothingSummary",
        "type": "object"
      },
      "DailyAdaptationResult": {
        "properties": {
          "average_core_improvement_c": {
            "title": "Average Core Improvement C",
            "type": "number"
          },
          "average_skin_improvement_c": {
            "title": "Average Skin Improvement C",
            "type": "number"
          },
          "beneficial": {
            "title": "Beneficial",
            "type": "boolean"
          },
          "exposure_eligible": {
            "title": "Exposure Eligible",
            "type": "boolean"
          },
          "final_skin_improvement_c": {
            "title": "Final Skin Improvement C",
            "type": "number"
          },
          "maximum_air_temperature_c": {
            "title": "Maximum Air Temperature C",
            "type": "number"
          },
          "maximum_skin_improvement_c": {
            "title": "Maximum Skin Improvement C",
            "type": "number"
          },
          "maximum_solar_radiation_w_m2": {
            "title": "Maximum Solar Radiation W M2",
            "type": "number"
          },
          "mean_air_temperature_c": {
            "title": "Mean Air Temperature C",
            "type": "number"
          },
          "mean_solar_radiation_w_m2": {
            "title": "Mean Solar Radiation W M2",
            "type": "number"
          },
          "sample_date_local": {
            "format": "date-time",
            "title": "Sample Date Local",
            "type": "string"
          },
          "weather_from_cache": {
            "title": "Weather From Cache",
            "type": "boolean"
          },
          "weight_days": {
            "minimum": 1.0,
            "title": "Weight Days",
            "type": "integer"
          }
        },
        "required": [
          "sample_date_local",
          "weight_days",
          "mean_air_temperature_c",
          "maximum_air_temperature_c",
          "mean_solar_radiation_w_m2",
          "maximum_solar_radiation_w_m2",
          "exposure_eligible",
          "beneficial",
          "average_skin_improvement_c",
          "final_skin_improvement_c",
          "average_core_improvement_c",
          "maximum_skin_improvement_c",
          "weather_from_cache"
        ],
        "title": "DailyAdaptationResult",
        "type": "object"
      },
      "EnergyDiagnostics": {
        "properties": {
          "energy_residual_j_m2": {
            "title": "Energy Residual J M2",
            "type": "number"
          },
          "integrated_net_heat_j_m2": {
            "title": "Integrated Net Heat J M2",
            "type": "number"
          },
          "maximum_core_step_c": {
            "title": "Maximum Core Step C",
            "type": "number"
          },
          "maximum_skin_step_c": {
            "title": "Maximum Skin Step C",
            "type": "number"
          },
          "normalized_residual_percent": {
            "title": "Normalized Residual Percent",
            "type": "number"
          },
          "solver_function_evaluations": {
            "title": "Solver Function Evaluations",
            "type": "integer"
          },
          "stored_energy_change_j_m2": {
            "title": "Stored Energy Change J M2",
            "type": "number"
          }
        },
        "required": [
          "stored_energy_change_j_m2",
          "integrated_net_heat_j_m2",
          "energy_residual_j_m2",
          "normalized_residual_percent",
          "maximum_core_step_c",
          "maximum_skin_step_c",
          "solver_function_evaluations"
        ],
        "title": "EnergyDiagnostics",
        "type": "object"
      },
      "EnvironmentAssumptions": {
        "additionalProperties": false,
        "properties": {
          "fixed_sky_offset_k": {
            "default": 15.0,
            "description": "fixed_offset: T_air - T_sky",
            "maximum": 50.0,
            "minimum": 0.0,
            "reference": "Stage 1 prototype",
            "source_type": "assumed",
            "title": "Fixed Sky Offset K",
            "type": "number"
          },
          "mean_radiant_temperature_method": {
            "default": "air_plus_solar_linear",
            "enum": [
              "air_plus_solar_linear",
              "equal_to_air"
            ],
            "reference": "Stage 1 prototype",
            "source_type": "assumed",
            "title": "Mean Radiant Temperature Method",
            "type": "string"
          },
          "sky_offset_base_k": {
            "default": 5.0,
            "description": "humidity_offset: depression at 100 % RH",
            "maximum": 40.0,
            "minimum": 0.0,
            "reference": "Stage 1 prototype",
            "source_type": "assumed",
            "title": "Sky Offset Base K",
            "type": "number"
          },
          "sky_offset_humidity_range_k": {
            "default": 10.0,
            "description": "humidity_offset: additional depression at 0 % RH",
            "maximum": 40.0,
            "minimum": 0.0,
            "reference": "Stage 1 prototype",
            "source_type": "assumed",
            "title": "Sky Offset Humidity Range K",
            "type": "number"
          },
          "sky_temperature_method": {
            "default": "humidity_offset",
            "enum": [
              "humidity_offset",
              "fixed_offset",
              "swinbank"
            ],
            "reference": "Stage 1 prototype",
            "source_type": "assumed",
            "title": "Sky Temperature Method",
            "type": "string"
          },
          "sky_view_factor": {
            "default": 0.5,
            "description": "Fraction of the body's radiative view occupied by sky",
            "maximum": 1.0,
            "minimum": 0.0,
            "reference": "Standing person on an open, unobstructed site",
            "source_type": "assumed",
            "title": "Sky View Factor",
            "type": "number"
          },
          "solar_mrt_gain_cap_k": {
            "default": 15.0,
            "description": "Upper bound of the solar MRT rise",
            "maximum": 40.0,
            "minimum": 0.0,
            "reference": "Stage 1 prototype",
            "source_type": "assumed",
            "title": "Solar Mrt Gain Cap K",
            "type": "number"
          },
          "solar_mrt_gain_k_per_w_m2": {
            "default": 0.012,
            "description": "MRT rise per W/m^2 of GHI (air_plus_solar_linear only)",
            "maximum": 0.05,
            "minimum": 0.0,
            "reference": "Stage 1 prototype",
            "source_type": "assumed",
            "title": "Solar Mrt Gain K Per W M2",
            "type": "number"
          },
          "wind_speed_scaling_factor": {
            "default": 1.0,
            "description": "Multiplier from ERA5 10 m wind to body-height wind. 1.0 keeps Stage 1 behaviour; ~0.67 approximates 1.1 m height via a logarithmic profile over open terrain.",
            "exclusiveMinimum": 0.0,
            "maximum": 1.5,
            "reference": "Stage 1 prototype",
            "source_type": "assumed",
            "title": "Wind Speed Scaling Factor",
            "type": "number"
          }
        },
        "title": "EnvironmentAssumptions",
        "type": "object"
      },
      "EnvironmentInput": {
        "properties": {
          "air_temperature_c": {
            "default": 38.0,
            "maximum": 70.0,
            "minimum": -50.0,
            "title": "Air Temperature C",
            "type": "number"
          },
          "mean_radiant_temperature_c": {
            "default": 45.0,
            "maximum": 100.0,
            "minimum": -50.0,
            "title": "Mean Radiant Temperature C",
            "type": "number"
          },
          "relative_humidity_percent": {
            "default": 40.0,
            "maximum": 100.0,
            "minimum": 0.0,
            "title": "Relative Humidity Percent",
            "type": "number"
          },
          "sky_temperature_c": {
            "anyOf": [
              {
                "maximum": 70.0,
                "minimum": -100.0,
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Sky Temperature C"
          },
          "sky_view_factor": {
            "default": 0.5,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Sky View Factor",
            "type": "number"
          },
          "solar_radiation_w_m2": {
            "default": 800.0,
            "maximum": 1500.0,
            "minimum": 0.0,
            "title": "Solar Radiation W M2",
            "type": "number"
          },
          "wind_speed_m_s": {
            "default": 1.5,
            "maximum": 30.0,
            "minimum": 0.0,
            "title": "Wind Speed M S",
            "type": "number"
          }
        },
        "title": "EnvironmentInput",
        "type": "object"
      },
      "GaggeBenchmarkRequest": {
        "properties": {
          "duration_minutes": {
            "default": 60,
            "maximum": 240.0,
            "minimum": 1.0,
            "title": "Duration Minutes",
            "type": "integer"
          },
          "environment": {
            "$ref": "#/components/schemas/EnvironmentInput"
          },
          "material": {
            "$ref": "#/components/schemas/MaterialInput"
          },
          "person": {
            "$ref": "#/components/schemas/PersonInput"
          }
        },
        "required": [
          "environment",
          "person",
          "material"
        ],
        "title": "GaggeBenchmarkRequest",
        "type": "object"
      },
      "GaggeBenchmarkResponse": {
        "properties": {
          "difference_core_temperature_c": {
            "title": "Difference Core Temperature C",
            "type": "number"
          },
          "difference_skin_temperature_c": {
            "title": "Difference Skin Temperature C",
            "type": "number"
          },
          "environment_note": {
            "title": "Environment Note",
            "type": "string"
          },
          "gagge": {
            "$ref": "#/components/schemas/GaggeModelOutput"
          },
          "prototype": {
            "$ref": "#/components/schemas/PrototypeBenchmarkOutput"
          },
          "reference_library": {
            "title": "Reference Library",
            "type": "string"
          },
          "reference_model": {
            "title": "Reference Model",
            "type": "string"
          },
          "warning": {
            "title": "Warning",
            "type": "string"
          }
        },
        "required": [
          "reference_model",
          "reference_library",
          "environment_note",
          "prototype",
          "gagge",
          "difference_core_temperature_c",
          "difference_skin_temperature_c",
          "warning"
        ],
        "title": "GaggeBenchmarkResponse",
        "type": "object"
      },
      "GaggeModelOutput": {
        "properties": {
          "core_temperature_c": {
            "title": "Core Temperature C",
            "type": "number"
          },
          "respiratory_heat_loss_w_m2": {
            "title": "Respiratory Heat Loss W M2",
            "type": "number"
          },
          "skin_blood_flow_kg_h_m2": {
            "title": "Skin Blood Flow Kg H M2",
            "type": "number"
          },
          "skin_evaporation_w_m2": {
            "title": "Skin Evaporation W M2",
            "type": "number"
          },
          "skin_heat_loss_w_m2": {
            "title": "Skin Heat Loss W M2",
            "type": "number"
          },
          "skin_temperature_c": {
            "title": "Skin Temperature C",
            "type": "number"
          },
          "skin_wettedness": {
            "title": "Skin Wettedness",
            "type": "number"
          },
          "standard_effective_temperature_c": {
            "title": "Standard Effective Temperature C",
            "type": "number"
          }
        },
        "required": [
          "core_temperature_c",
          "skin_temperature_c",
          "skin_evaporation_w_m2",
          "skin_heat_loss_w_m2",
          "respiratory_heat_loss_w_m2",
          "skin_blood_flow_kg_h_m2",
          "skin_wettedness",
          "standard_effective_temperature_c"
        ],
        "title": "GaggeModelOutput",
        "type": "object"
      },
      "GlobalBatchCreate": {
        "properties": {
          "analysis_resolution": {
            "default": "representative",
            "enum": [
              "representative",
              "daily"
            ],
            "title": "Analysis Resolution",
            "type": "string"
          },
          "city_ids": {
            "items": {
              "type": "string"
            },
            "maxItems": 100,
            "minItems": 1,
            "title": "City Ids",
            "type": "array"
          },
          "control_material": {
            "$ref": "#/components/schemas/MaterialInput"
          },
          "daily_stride_days": {
            "default": 1,
            "maximum": 7.0,
            "minimum": 1.0,
            "title": "Daily Stride Days",
            "type": "integer"
          },
          "duration_minutes": {
            "default": 120,
            "maximum": 1440.0,
            "minimum": 30.0,
            "title": "Duration Minutes",
            "type": "integer"
          },
          "enable_heatwave_analysis": {
            "default": true,
            "title": "Enable Heatwave Analysis",
            "type": "boolean"
          },
          "end_month": {
            "default": 12,
            "maximum": 12.0,
            "minimum": 1.0,
            "title": "End Month",
            "type": "integer"
          },
          "environment_assumptions": {
            "$ref": "#/components/schemas/EnvironmentAssumptions"
          },
          "execution_profile": {
            "default": "auto",
            "enum": [
              "auto",
              "standard",
              "large"
            ],
            "title": "Execution Profile",
            "type": "string"
          },
          "exposure_match_mode": {
            "default": "all",
            "enum": [
              "all",
              "any"
            ],
            "title": "Exposure Match Mode",
            "type": "string"
          },
          "heatwave_minimum_consecutive_days": {
            "default": 3,
            "maximum": 30.0,
            "minimum": 2.0,
            "title": "Heatwave Minimum Consecutive Days",
            "type": "integer"
          },
          "heatwave_temperature_threshold_c": {
            "default": 35.0,
            "maximum": 70.0,
            "minimum": -20.0,
            "title": "Heatwave Temperature Threshold C",
            "type": "number"
          },
          "local_start_hour": {
            "default": 12,
            "maximum": 23.0,
            "minimum": 0.0,
            "title": "Local Start Hour",
            "type": "integer"
          },
          "minimum_air_temperature_c": {
            "anyOf": [
              {
                "maximum": 70.0,
                "minimum": -50.0,
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "default": 30.0,
            "title": "Minimum Air Temperature C"
          },
          "minimum_skin_improvement_c": {
            "default": 0.2,
            "maximum": 10.0,
            "minimum": -5.0,
            "title": "Minimum Skin Improvement C",
            "type": "number"
          },
          "minimum_solar_radiation_w_m2": {
            "anyOf": [
              {
                "maximum": 1500.0,
                "minimum": 0.0,
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "default": 300.0,
            "title": "Minimum Solar Radiation W M2"
          },
          "name": {
            "default": "Global multi-day climate adaptation analysis",
            "maxLength": 200,
            "minLength": 1,
            "title": "Name",
            "type": "string"
          },
          "output_interval_minutes": {
            "default": 10,
            "maximum": 60.0,
            "minimum": 1.0,
            "title": "Output Interval Minutes",
            "type": "integer"
          },
          "person": {
            "$ref": "#/components/schemas/PersonInput"
          },
          "rc_material": {
            "$ref": "#/components/schemas/MaterialInput"
          },
          "representative_day": {
            "anyOf": [
              {
                "maximum": 28.0,
                "minimum": 1.0,
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Representative Day"
          },
          "resume_from_checkpoint": {
            "default": true,
            "title": "Resume From Checkpoint",
            "type": "boolean"
          },
          "sample_days_per_month": {
            "default": 3,
            "maximum": 7.0,
            "minimum": 1.0,
            "title": "Sample Days Per Month",
            "type": "integer"
          },
          "start_month": {
            "default": 1,
            "maximum": 12.0,
            "minimum": 1.0,
            "title": "Start Month",
            "type": "integer"
          },
          "year": {
            "default": 2023,
            "maximum": 2100.0,
            "minimum": 1940.0,
            "title": "Year",
            "type": "integer"
          }
        },
        "required": [
          "city_ids",
          "person",
          "control_material",
          "rc_material"
        ],
        "title": "GlobalBatchCreate",
        "type": "object"
      },
      "GlobalBatchDetail": {
        "properties": {
          "cancelled_city_count": {
            "title": "Cancelled City Count",
            "type": "integer"
          },
          "celery_group_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Celery Group Id"
          },
          "city_results": {
            "items": {
              "$ref": "#/components/schemas/GlobalCityResultResponse"
            },
            "title": "City Results",
            "type": "array"
          },
          "completed_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Completed At"
          },
          "completed_city_count": {
            "title": "Completed City Count",
            "type": "integer"
          },
          "created_at": {
            "format": "date-time",
            "title": "Created At",
            "type": "string"
          },
          "error_message": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Error Message"
          },
          "failed_city_count": {
            "title": "Failed City Count",
            "type": "integer"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "progress": {
            "title": "Progress",
            "type": "integer"
          },
          "request": {
            "$ref": "#/components/schemas/GlobalBatchCreate"
          },
          "stage": {
            "title": "Stage",
            "type": "string"
          },
          "started_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Started At"
          },
          "status": {
            "enum": [
              "queued",
              "running",
              "cancelling",
              "cancelled",
              "completed",
              "partial_completed",
              "failed"
            ],
            "title": "Status",
            "type": "string"
          },
          "summary": {
            "anyOf": [
              {
                "additionalProperties": true,
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Summary"
          },
          "total_city_count": {
            "title": "Total City Count",
            "type": "integer"
          },
          "updated_at": {
            "format": "date-time",
            "title": "Updated At",
            "type": "string"
          }
        },
        "required": [
          "id",
          "celery_group_id",
          "status",
          "stage",
          "progress",
          "total_city_count",
          "completed_city_count",
          "failed_city_count",
          "cancelled_city_count",
          "summary",
          "error_message",
          "created_at",
          "updated_at",
          "started_at",
          "completed_at",
          "request",
          "city_results"
        ],
        "title": "GlobalBatchDetail",
        "type": "object"
      },
      "GlobalBatchEstimateResponse": {
        "properties": {
          "analysis_resolution": {
            "enum": [
              "representative",
              "daily"
            ],
            "title": "Analysis Resolution",
            "type": "string"
          },
          "checkpoint_count_per_city": {
            "title": "Checkpoint Count Per City",
            "type": "integer"
          },
          "city_count": {
            "title": "City Count",
            "type": "integer"
          },
          "estimated_weather_requests": {
            "title": "Estimated Weather Requests",
            "type": "integer"
          },
          "heatwave_analysis_available": {
            "title": "Heatwave Analysis Available",
            "type": "boolean"
          },
          "month_count": {
            "title": "Month Count",
            "type": "integer"
          },
          "resolved_execution_profile": {
            "enum": [
              "auto",
              "standard",
              "large"
            ],
            "title": "Resolved Execution Profile",
            "type": "string"
          },
          "resolved_queue": {
            "title": "Resolved Queue",
            "type": "string"
          },
          "samples_per_city": {
            "title": "Samples Per City",
            "type": "integer"
          },
          "thermal_simulation_count": {
            "title": "Thermal Simulation Count",
            "type": "integer"
          },
          "total_samples": {
            "title": "Total Samples",
            "type": "integer"
          }
        },
        "required": [
          "city_count",
          "month_count",
          "samples_per_city",
          "total_samples",
          "thermal_simulation_count",
          "estimated_weather_requests",
          "analysis_resolution",
          "resolved_execution_profile",
          "resolved_queue",
          "checkpoint_count_per_city",
          "heatwave_analysis_available"
        ],
        "title": "GlobalBatchEstimateResponse",
        "type": "object"
      },
      "GlobalBatchListResponse": {
        "properties": {
          "items": {
            "items": {
              "$ref": "#/components/schemas/GlobalBatchResponse"
            },
            "title": "Items",
            "type": "array"
          },
          "limit": {
            "title": "Limit",
            "type": "integer"
          },
          "offset": {
            "title": "Offset",
            "type": "integer"
          },
          "total": {
            "title": "Total",
            "type": "integer"
          }
        },
        "required": [
          "items",
          "total",
          "limit",
          "offset"
        ],
        "title": "GlobalBatchListResponse",
        "type": "object"
      },
      "GlobalBatchResponse": {
        "properties": {
          "cancelled_city_count": {
            "title": "Cancelled City Count",
            "type": "integer"
          },
          "celery_group_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Celery Group Id"
          },
          "completed_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Completed At"
          },
          "completed_city_count": {
            "title": "Completed City Count",
            "type": "integer"
          },
          "created_at": {
            "format": "date-time",
            "title": "Created At",
            "type": "string"
          },
          "error_message": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Error Message"
          },
          "failed_city_count": {
            "title": "Failed City Count",
            "type": "integer"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "progress": {
            "title": "Progress",
            "type": "integer"
          },
          "stage": {
            "title": "Stage",
            "type": "string"
          },
          "started_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Started At"
          },
          "status": {
            "enum": [
              "queued",
              "running",
              "cancelling",
              "cancelled",
              "completed",
              "partial_completed",
              "failed"
            ],
            "title": "Status",
            "type": "string"
          },
          "summary": {
            "anyOf": [
              {
                "additionalProperties": true,
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Summary"
          },
          "total_city_count": {
            "title": "Total City Count",
            "type": "integer"
          },
          "updated_at": {
            "format": "date-time",
            "title": "Updated At",
            "type": "string"
          }
        },
        "required": [
          "id",
          "celery_group_id",
          "status",
          "stage",
          "progress",
          "total_city_count",
          "completed_city_count",
          "failed_city_count",
          "cancelled_city_count",
          "summary",
          "error_message",
          "created_at",
          "updated_at",
          "started_at",
          "completed_at"
        ],
        "title": "GlobalBatchResponse",
        "type": "object"
      },
      "GlobalCityResultResponse": {
        "properties": {
          "annual_average_core_improvement_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Annual Average Core Improvement C"
          },
          "annual_average_skin_improvement_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Annual Average Skin Improvement C"
          },
          "batch_id": {
            "title": "Batch Id",
            "type": "string"
          },
          "beneficial_weighted_days": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Beneficial Weighted Days"
          },
          "celery_task_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Celery Task Id"
          },
          "city_id": {
            "title": "City Id",
            "type": "string"
          },
          "city_name": {
            "title": "City Name",
            "type": "string"
          },
          "climate_adaptation_rate_percent": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Climate Adaptation Rate Percent"
          },
          "completed_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Completed At"
          },
          "completed_month_count": {
            "default": 0,
            "title": "Completed Month Count",
            "type": "integer"
          },
          "core_improvement_p50_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Core Improvement P50 C"
          },
          "core_improvement_p90_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Core Improvement P90 C"
          },
          "core_improvement_p95_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Core Improvement P95 C"
          },
          "country": {
            "title": "Country",
            "type": "string"
          },
          "data_quality": {
            "anyOf": [
              {
                "additionalProperties": true,
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Data Quality"
          },
          "effective_cooling_hours": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Effective Cooling Hours"
          },
          "eligible_sample_count": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Eligible Sample Count"
          },
          "error_message": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Error Message"
          },
          "evaluated_weighted_days": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Evaluated Weighted Days"
          },
          "exposure_coverage_percent": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Exposure Coverage Percent"
          },
          "heatwave_event_count": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Heatwave Event Count"
          },
          "heatwave_events": {
            "anyOf": [
              {
                "items": {
                  "$ref": "#/components/schemas/HeatwaveEvent"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Heatwave Events"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "last_checkpoint_month": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Last Checkpoint Month"
          },
          "last_heartbeat_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Last Heartbeat At"
          },
          "latitude": {
            "title": "Latitude",
            "type": "number"
          },
          "longest_heatwave_days": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Longest Heatwave Days"
          },
          "longitude": {
            "title": "Longitude",
            "type": "number"
          },
          "maximum_skin_improvement_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Maximum Skin Improvement C"
          },
          "metric_definitions": {
            "anyOf": [
              {
                "additionalProperties": true,
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Metric Definitions"
          },
          "monthly_results": {
            "anyOf": [
              {
                "items": {
                  "$ref": "#/components/schemas/MonthlyAdaptationResult"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Monthly Results"
          },
          "progress": {
            "title": "Progress",
            "type": "integer"
          },
          "resumed_from_checkpoint": {
            "default": false,
            "title": "Resumed From Checkpoint",
            "type": "boolean"
          },
          "retry_count": {
            "title": "Retry Count",
            "type": "integer"
          },
          "sampled_day_count": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Sampled Day Count"
          },
          "skin_improvement_p50_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Skin Improvement P50 C"
          },
          "skin_improvement_p90_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Skin Improvement P90 C"
          },
          "skin_improvement_p95_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Skin Improvement P95 C"
          },
          "stage": {
            "title": "Stage",
            "type": "string"
          },
          "started_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Started At"
          },
          "status": {
            "enum": [
              "queued",
              "running",
              "cancelled",
              "completed",
              "failed"
            ],
            "title": "Status",
            "type": "string"
          }
        },
        "required": [
          "id",
          "batch_id",
          "celery_task_id",
          "city_id",
          "city_name",
          "country",
          "latitude",
          "longitude",
          "status",
          "stage",
          "progress",
          "climate_adaptation_rate_percent",
          "exposure_coverage_percent",
          "annual_average_skin_improvement_c",
          "annual_average_core_improvement_c",
          "maximum_skin_improvement_c",
          "effective_cooling_hours",
          "sampled_day_count",
          "eligible_sample_count",
          "evaluated_weighted_days",
          "beneficial_weighted_days",
          "retry_count",
          "monthly_results",
          "error_message",
          "started_at",
          "completed_at"
        ],
        "title": "GlobalCityResultResponse",
        "type": "object"
      },
      "HTTPValidationError": {
        "properties": {
          "detail": {
            "items": {
              "$ref": "#/components/schemas/ValidationError"
            },
            "title": "Detail",
            "type": "array"
          }
        },
        "title": "HTTPValidationError",
        "type": "object"
      },
      "HeatwaveEvent": {
        "properties": {
          "beneficial_day_count": {
            "minimum": 0.0,
            "title": "Beneficial Day Count",
            "type": "integer"
          },
          "duration_days": {
            "minimum": 1.0,
            "title": "Duration Days",
            "type": "integer"
          },
          "end_date_local": {
            "format": "date-time",
            "title": "End Date Local",
            "type": "string"
          },
          "mean_maximum_air_temperature_c": {
            "title": "Mean Maximum Air Temperature C",
            "type": "number"
          },
          "mean_skin_improvement_c": {
            "title": "Mean Skin Improvement C",
            "type": "number"
          },
          "p90_skin_improvement_c": {
            "title": "P90 Skin Improvement C",
            "type": "number"
          },
          "peak_air_temperature_c": {
            "title": "Peak Air Temperature C",
            "type": "number"
          },
          "start_date_local": {
            "format": "date-time",
            "title": "Start Date Local",
            "type": "string"
          }
        },
        "required": [
          "start_date_local",
          "end_date_local",
          "duration_days",
          "mean_maximum_air_temperature_c",
          "peak_air_temperature_c",
          "mean_skin_improvement_c",
          "p90_skin_improvement_c",
          "beneficial_day_count"
        ],
        "title": "HeatwaveEvent",
        "type": "object"
      },
      "MaterialCreate": {
        "properties": {
          "description": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Description"
          },
          "initial_version": {
            "$ref": "#/components/schemas/MaterialVersionCreate"
          },
          "institution": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Institution"
          },
          "name": {
            "maxLength": 200,
            "minLength": 1,
            "title": "Name",
            "type": "string"
          },
          "slug": {
            "maxLength": 200,
            "minLength": 1,
            "pattern": "^[a-z0-9]+(?:-[a-z0-9]+)*$",
            "title": "Slug",
            "type": "string"
          }
        },
        "required": [
          "name",
          "slug",
          "initial_version"
        ],
        "title": "MaterialCreate",
        "type": "object"
      },
      "MaterialInput": {
        "properties": {
          "absorbed_solar_to_body_fraction": {
            "default": 0.35,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Absorbed Solar To Body Fraction",
            "type": "number"
          },
          "clothing_insulation_clo": {
            "default": 0.5,
            "maximum": 5.0,
            "minimum": 0.0,
            "title": "Clothing Insulation Clo",
            "type": "number"
          },
          "evaporative_resistance_m2pa_w": {
            "anyOf": [
              {
                "maximum": 1000.0,
                "minimum": 0.0,
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Evaporative Resistance M2Pa W"
          },
          "infrared_emissivity": {
            "default": 0.9,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Infrared Emissivity",
            "type": "number"
          },
          "infrared_transmittance": {
            "default": 0.0,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Infrared Transmittance",
            "type": "number"
          },
          "material_version_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Material Version Id"
          },
          "name": {
            "maxLength": 100,
            "minLength": 1,
            "title": "Name",
            "type": "string"
          },
          "parameter_sources": {
            "anyOf": [
              {
                "additionalProperties": {
                  "$ref": "#/components/schemas/ParameterSource"
                },
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Parameter Sources"
          },
          "projected_solar_area_factor": {
            "default": 0.25,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Projected Solar Area Factor",
            "type": "number"
          },
          "solar_reflectance": {
            "default": 0.5,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Solar Reflectance",
            "type": "number"
          },
          "solar_transmittance": {
            "default": 0,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Solar Transmittance",
            "type": "number"
          },
          "source_reference": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Source Reference"
          },
          "source_type": {
            "anyOf": [
              {
                "maxLength": 50,
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Source Type"
          }
        },
        "required": [
          "name"
        ],
        "title": "MaterialInput",
        "type": "object"
      },
      "MaterialListItem": {
        "properties": {
          "created_at": {
            "format": "date-time",
            "title": "Created At",
            "type": "string"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "institution": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Institution"
          },
          "is_archived": {
            "title": "Is Archived",
            "type": "boolean"
          },
          "latest_version_number": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Latest Version Number"
          },
          "name": {
            "title": "Name",
            "type": "string"
          },
          "slug": {
            "title": "Slug",
            "type": "string"
          }
        },
        "required": [
          "id",
          "name",
          "slug",
          "institution",
          "is_archived",
          "latest_version_number",
          "created_at"
        ],
        "title": "MaterialListItem",
        "type": "object"
      },
      "MaterialListResponse": {
        "properties": {
          "items": {
            "items": {
              "$ref": "#/components/schemas/MaterialListItem"
            },
            "title": "Items",
            "type": "array"
          },
          "limit": {
            "title": "Limit",
            "type": "integer"
          },
          "offset": {
            "title": "Offset",
            "type": "integer"
          },
          "total": {
            "title": "Total",
            "type": "integer"
          }
        },
        "required": [
          "items",
          "total",
          "limit",
          "offset"
        ],
        "title": "MaterialListResponse",
        "type": "object"
      },
      "MaterialResponse": {
        "properties": {
          "created_at": {
            "format": "date-time",
            "title": "Created At",
            "type": "string"
          },
          "description": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Description"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "institution": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Institution"
          },
          "is_archived": {
            "title": "Is Archived",
            "type": "boolean"
          },
          "name": {
            "title": "Name",
            "type": "string"
          },
          "slug": {
            "title": "Slug",
            "type": "string"
          },
          "updated_at": {
            "format": "date-time",
            "title": "Updated At",
            "type": "string"
          },
          "versions": {
            "items": {
              "$ref": "#/components/schemas/MaterialVersionResponse"
            },
            "title": "Versions",
            "type": "array"
          }
        },
        "required": [
          "id",
          "name",
          "slug",
          "description",
          "institution",
          "is_archived",
          "created_at",
          "updated_at",
          "versions"
        ],
        "title": "MaterialResponse",
        "type": "object"
      },
      "MaterialUpdate": {
        "properties": {
          "description": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Description"
          },
          "institution": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Institution"
          },
          "is_archived": {
            "anyOf": [
              {
                "type": "boolean"
              },
              {
                "type": "null"
              }
            ],
            "title": "Is Archived"
          },
          "name": {
            "anyOf": [
              {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Name"
          }
        },
        "title": "MaterialUpdate",
        "type": "object"
      },
      "MaterialVersionCreate": {
        "properties": {
          "absorbed_solar_to_body_fraction": {
            "default": 0.35,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Absorbed Solar To Body Fraction",
            "type": "number"
          },
          "areal_density_g_m2": {
            "anyOf": [
              {
                "minimum": 0.0,
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Areal Density G M2"
          },
          "clothing_insulation_clo": {
            "default": 0.5,
            "maximum": 5.0,
            "minimum": 0.0,
            "title": "Clothing Insulation Clo",
            "type": "number"
          },
          "evaporative_resistance_m2pa_w": {
            "anyOf": [
              {
                "minimum": 0.0,
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Evaporative Resistance M2Pa W"
          },
          "infrared_emissivity": {
            "default": 0.9,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Infrared Emissivity",
            "type": "number"
          },
          "infrared_transmittance": {
            "default": 0,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Infrared Transmittance",
            "type": "number"
          },
          "mode": {
            "default": "opaque_emitter",
            "enum": [
              "ordinary",
              "opaque_emitter",
              "infrared_transparent",
              "hybrid"
            ],
            "title": "Mode",
            "type": "string"
          },
          "notes": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Notes"
          },
          "parameter_sources": {
            "anyOf": [
              {
                "additionalProperties": {
                  "$ref": "#/components/schemas/ParameterSource"
                },
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Parameter Sources"
          },
          "projected_solar_area_factor": {
            "default": 0.25,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Projected Solar Area Factor",
            "type": "number"
          },
          "solar_reflectance": {
            "default": 0.5,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Solar Reflectance",
            "type": "number"
          },
          "solar_transmittance": {
            "default": 0,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Solar Transmittance",
            "type": "number"
          },
          "source_reference": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Source Reference"
          },
          "source_type": {
            "default": "manual",
            "maxLength": 50,
            "title": "Source Type",
            "type": "string"
          },
          "specific_heat_j_kgk": {
            "anyOf": [
              {
                "minimum": 0.0,
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Specific Heat J Kgk"
          }
        },
        "title": "MaterialVersionCreate",
        "type": "object"
      },
      "MaterialVersionResponse": {
        "properties": {
          "absorbed_solar_to_body_fraction": {
            "title": "Absorbed Solar To Body Fraction",
            "type": "number"
          },
          "areal_density_g_m2": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Areal Density G M2"
          },
          "clothing_insulation_clo": {
            "title": "Clothing Insulation Clo",
            "type": "number"
          },
          "created_at": {
            "format": "date-time",
            "title": "Created At",
            "type": "string"
          },
          "evaporative_resistance_m2pa_w": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Evaporative Resistance M2Pa W"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "infrared_emissivity": {
            "title": "Infrared Emissivity",
            "type": "number"
          },
          "infrared_transmittance": {
            "title": "Infrared Transmittance",
            "type": "number"
          },
          "material_id": {
            "title": "Material Id",
            "type": "string"
          },
          "mode": {
            "title": "Mode",
            "type": "string"
          },
          "notes": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Notes"
          },
          "parameter_sources": {
            "anyOf": [
              {
                "additionalProperties": {
                  "$ref": "#/components/schemas/ParameterSource"
                },
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Parameter Sources"
          },
          "projected_solar_area_factor": {
            "title": "Projected Solar Area Factor",
            "type": "number"
          },
          "solar_reflectance": {
            "title": "Solar Reflectance",
            "type": "number"
          },
          "solar_transmittance": {
            "title": "Solar Transmittance",
            "type": "number"
          },
          "source_reference": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Source Reference"
          },
          "source_type": {
            "title": "Source Type",
            "type": "string"
          },
          "specific_heat_j_kgk": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Specific Heat J Kgk"
          },
          "spectra": {
            "default": [],
            "items": {
              "$ref": "#/components/schemas/SpectrumSummary"
            },
            "title": "Spectra",
            "type": "array"
          },
          "version_number": {
            "title": "Version Number",
            "type": "integer"
          }
        },
        "required": [
          "id",
          "material_id",
          "version_number",
          "mode",
          "clothing_insulation_clo",
          "evaporative_resistance_m2pa_w",
          "solar_reflectance",
          "solar_transmittance",
          "infrared_emissivity",
          "infrared_transmittance",
          "projected_solar_area_factor",
          "absorbed_solar_to_body_fraction",
          "areal_density_g_m2",
          "specific_heat_j_kgk",
          "source_type",
          "source_reference",
          "notes",
          "created_at"
        ],
        "title": "MaterialVersionResponse",
        "type": "object"
      },
      "ModelMetadata": {
        "description": "Written into every simulation response for traceability.",
        "properties": {
          "parameter_set_sha256": {
            "title": "Parameter Set Sha256",
            "type": "string"
          },
          "parameter_set_version": {
            "title": "Parameter Set Version",
            "type": "string"
          }
        },
        "required": [
          "parameter_set_version",
          "parameter_set_sha256"
        ],
        "title": "ModelMetadata",
        "type": "object"
      },
      "ModelParameter": {
        "description": "A physical constant used by the thermal model.",
        "properties": {
          "description": {
            "title": "Description",
            "type": "string"
          },
          "name": {
            "title": "Name",
            "type": "string"
          },
          "note": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Note"
          },
          "reference": {
            "title": "Reference",
            "type": "string"
          },
          "source_type": {
            "enum": [
              "measured",
              "manufacturer",
              "literature",
              "standard",
              "derived",
              "assumed",
              "manual"
            ],
            "title": "Source Type",
            "type": "string"
          },
          "unit": {
            "title": "Unit",
            "type": "string"
          },
          "value": {
            "title": "Value",
            "type": "number"
          }
        },
        "required": [
          "name",
          "value",
          "unit",
          "description",
          "source_type",
          "reference"
        ],
        "title": "ModelParameter",
        "type": "object"
      },
      "ModelParameterManifest": {
        "properties": {
          "parameter_set_sha256": {
            "title": "Parameter Set Sha256",
            "type": "string"
          },
          "parameter_set_version": {
            "title": "Parameter Set Version",
            "type": "string"
          },
          "parameters": {
            "items": {
              "$ref": "#/components/schemas/ModelParameter"
            },
            "title": "Parameters",
            "type": "array"
          }
        },
        "required": [
          "parameter_set_version",
          "parameter_set_sha256",
          "parameters"
        ],
        "title": "ModelParameterManifest",
        "type": "object"
      },
      "MonthlyAdaptationResult": {
        "properties": {
          "average_core_improvement_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Average Core Improvement C"
          },
          "average_skin_improvement_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Average Skin Improvement C"
          },
          "beneficial": {
            "anyOf": [
              {
                "type": "boolean"
              },
              {
                "type": "null"
              }
            ],
            "title": "Beneficial"
          },
          "beneficial_weighted_days": {
            "default": 0,
            "title": "Beneficial Weighted Days",
            "type": "integer"
          },
          "climate_adaptation_rate_percent": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Climate Adaptation Rate Percent"
          },
          "eligible_sample_count": {
            "default": 0,
            "title": "Eligible Sample Count",
            "type": "integer"
          },
          "evaluated_weighted_days": {
            "default": 0,
            "title": "Evaluated Weighted Days",
            "type": "integer"
          },
          "exposure_coverage_percent": {
            "default": 0.0,
            "title": "Exposure Coverage Percent",
            "type": "number"
          },
          "final_skin_improvement_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Final Skin Improvement C"
          },
          "maximum_skin_improvement_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Maximum Skin Improvement C"
          },
          "month": {
            "maximum": 12.0,
            "minimum": 1.0,
            "title": "Month",
            "type": "integer"
          },
          "representative_date_local": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Representative Date Local"
          },
          "sampled_day_count": {
            "default": 1,
            "title": "Sampled Day Count",
            "type": "integer"
          },
          "samples": {
            "items": {
              "$ref": "#/components/schemas/DailyAdaptationResult"
            },
            "title": "Samples",
            "type": "array"
          },
          "skipped_samples": {
            "items": {
              "$ref": "#/components/schemas/SkippedSample"
            },
            "title": "Skipped Samples",
            "type": "array"
          },
          "skipped_weighted_days": {
            "default": 0,
            "title": "Skipped Weighted Days",
            "type": "integer"
          },
          "total_weighted_days": {
            "default": 0,
            "title": "Total Weighted Days",
            "type": "integer"
          },
          "weight_days": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Weight Days"
          }
        },
        "required": [
          "month"
        ],
        "title": "MonthlyAdaptationResult",
        "type": "object"
      },
      "ParameterSource": {
        "additionalProperties": false,
        "description": "Provenance of one numeric input.",
        "properties": {
          "note": {
            "anyOf": [
              {
                "maxLength": 1000,
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Note"
          },
          "reference": {
            "anyOf": [
              {
                "maxLength": 500,
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Reference"
          },
          "source_type": {
            "default": "assumed",
            "enum": [
              "measured",
              "manufacturer",
              "literature",
              "standard",
              "derived",
              "assumed",
              "manual"
            ],
            "title": "Source Type",
            "type": "string"
          }
        },
        "title": "ParameterSource",
        "type": "object"
      },
      "PersonInput": {
        "properties": {
          "body_surface_area_m2": {
            "default": 1.8,
            "maximum": 3.0,
            "minimum": 1.0,
            "title": "Body Surface Area M2",
            "type": "number"
          },
          "initial_core_temperature_c": {
            "default": 36.8,
            "maximum": 40.0,
            "minimum": 34.0,
            "title": "Initial Core Temperature C",
            "type": "number"
          },
          "initial_skin_temperature_c": {
            "default": 33.7,
            "maximum": 40.0,
            "minimum": 20.0,
            "title": "Initial Skin Temperature C",
            "type": "number"
          },
          "met": {
            "default": 2.6,
            "maximum": 10.0,
            "minimum": 0.7,
            "title": "Met",
            "type": "number"
          }
        },
        "title": "PersonInput",
        "type": "object"
      },
      "PrototypeBenchmarkOutput": {
        "properties": {
          "core_temperature_c": {
            "title": "Core Temperature C",
            "type": "number"
          },
          "energy_residual_percent": {
            "title": "Energy Residual Percent",
            "type": "number"
          },
          "evaporation_w_m2": {
            "title": "Evaporation W M2",
            "type": "number"
          },
          "skin_temperature_c": {
            "title": "Skin Temperature C",
            "type": "number"
          }
        },
        "required": [
          "core_temperature_c",
          "skin_temperature_c",
          "evaporation_w_m2",
          "energy_residual_percent"
        ],
        "title": "PrototypeBenchmarkOutput",
        "type": "object"
      },
      "ScenarioResult": {
        "properties": {
          "assumptions_applied": {
            "items": {
              "type": "string"
            },
            "title": "Assumptions Applied",
            "type": "array"
          },
          "clothing": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ClothingSummary"
              },
              {
                "type": "null"
              }
            ]
          },
          "diagnostics": {
            "$ref": "#/components/schemas/EnergyDiagnostics"
          },
          "final_core_temperature_c": {
            "title": "Final Core Temperature C",
            "type": "number"
          },
          "final_skin_temperature_c": {
            "title": "Final Skin Temperature C",
            "type": "number"
          },
          "material_name": {
            "title": "Material Name",
            "type": "string"
          },
          "peak_core_temperature_c": {
            "title": "Peak Core Temperature C",
            "type": "number"
          },
          "peak_skin_temperature_c": {
            "title": "Peak Skin Temperature C",
            "type": "number"
          },
          "time_series": {
            "items": {
              "$ref": "#/components/schemas/TimeSeriesPoint"
            },
            "title": "Time Series",
            "type": "array"
          }
        },
        "required": [
          "material_name",
          "time_series",
          "final_core_temperature_c",
          "final_skin_temperature_c",
          "peak_core_temperature_c",
          "peak_skin_temperature_c",
          "diagnostics"
        ],
        "title": "ScenarioResult",
        "type": "object"
      },
      "SimulationJobDetail": {
        "properties": {
          "celery_task_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Celery Task Id"
          },
          "city_id": {
            "title": "City Id",
            "type": "string"
          },
          "completed_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Completed At"
          },
          "created_at": {
            "format": "date-time",
            "title": "Created At",
            "type": "string"
          },
          "error_message": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Error Message"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "progress": {
            "title": "Progress",
            "type": "integer"
          },
          "request": {
            "$ref": "#/components/schemas/WeatherSimulationRequest"
          },
          "stage": {
            "title": "Stage",
            "type": "string"
          },
          "started_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Started At"
          },
          "status": {
            "enum": [
              "queued",
              "running",
              "cancelling",
              "cancelled",
              "completed",
              "failed"
            ],
            "title": "Status",
            "type": "string"
          },
          "summary": {
            "anyOf": [
              {
                "additionalProperties": true,
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Summary"
          },
          "updated_at": {
            "format": "date-time",
            "title": "Updated At",
            "type": "string"
          }
        },
        "required": [
          "id",
          "celery_task_id",
          "status",
          "stage",
          "progress",
          "city_id",
          "summary",
          "error_message",
          "created_at",
          "updated_at",
          "started_at",
          "completed_at",
          "request"
        ],
        "title": "SimulationJobDetail",
        "type": "object"
      },
      "SimulationJobListResponse": {
        "properties": {
          "items": {
            "items": {
              "$ref": "#/components/schemas/SimulationJobResponse"
            },
            "title": "Items",
            "type": "array"
          },
          "limit": {
            "title": "Limit",
            "type": "integer"
          },
          "offset": {
            "title": "Offset",
            "type": "integer"
          },
          "total": {
            "title": "Total",
            "type": "integer"
          }
        },
        "required": [
          "items",
          "total",
          "limit",
          "offset"
        ],
        "title": "SimulationJobListResponse",
        "type": "object"
      },
      "SimulationJobResponse": {
        "properties": {
          "celery_task_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Celery Task Id"
          },
          "city_id": {
            "title": "City Id",
            "type": "string"
          },
          "completed_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Completed At"
          },
          "created_at": {
            "format": "date-time",
            "title": "Created At",
            "type": "string"
          },
          "error_message": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Error Message"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "progress": {
            "title": "Progress",
            "type": "integer"
          },
          "stage": {
            "title": "Stage",
            "type": "string"
          },
          "started_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Started At"
          },
          "status": {
            "enum": [
              "queued",
              "running",
              "cancelling",
              "cancelled",
              "completed",
              "failed"
            ],
            "title": "Status",
            "type": "string"
          },
          "summary": {
            "anyOf": [
              {
                "additionalProperties": true,
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Summary"
          },
          "updated_at": {
            "format": "date-time",
            "title": "Updated At",
            "type": "string"
          }
        },
        "required": [
          "id",
          "celery_task_id",
          "status",
          "stage",
          "progress",
          "city_id",
          "summary",
          "error_message",
          "created_at",
          "updated_at",
          "started_at",
          "completed_at"
        ],
        "title": "SimulationJobResponse",
        "type": "object"
      },
      "SimulationRequest": {
        "properties": {
          "city": {
            "default": "Dubai",
            "minLength": 1,
            "title": "City",
            "type": "string"
          },
          "control_material": {
            "$ref": "#/components/schemas/MaterialInput"
          },
          "duration_minutes": {
            "default": 120,
            "maximum": 1440.0,
            "minimum": 1.0,
            "title": "Duration Minutes",
            "type": "integer"
          },
          "environment": {
            "$ref": "#/components/schemas/EnvironmentInput"
          },
          "output_interval_minutes": {
            "default": 1,
            "maximum": 60.0,
            "minimum": 1.0,
            "title": "Output Interval Minutes",
            "type": "integer"
          },
          "person": {
            "$ref": "#/components/schemas/PersonInput"
          },
          "rc_material": {
            "$ref": "#/components/schemas/MaterialInput"
          }
        },
        "required": [
          "environment",
          "person",
          "control_material",
          "rc_material"
        ],
        "title": "SimulationRequest",
        "type": "object"
      },
      "SimulationResponse": {
        "properties": {
          "city": {
            "title": "City",
            "type": "string"
          },
          "control": {
            "$ref": "#/components/schemas/ScenarioResult"
          },
          "duration_minutes": {
            "title": "Duration Minutes",
            "type": "integer"
          },
          "model_metadata": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ModelMetadata"
              },
              {
                "type": "null"
              }
            ]
          },
          "model_name": {
            "title": "Model Name",
            "type": "string"
          },
          "model_version": {
            "title": "Model Version",
            "type": "string"
          },
          "radiative_cooling": {
            "$ref": "#/components/schemas/ScenarioResult"
          },
          "summary": {
            "$ref": "#/components/schemas/SimulationSummary"
          },
          "warning": {
            "title": "Warning",
            "type": "string"
          }
        },
        "required": [
          "model_name",
          "model_version",
          "city",
          "duration_minutes",
          "control",
          "radiative_cooling",
          "summary",
          "warning"
        ],
        "title": "SimulationResponse",
        "type": "object"
      },
      "SimulationSummary": {
        "properties": {
          "average_skin_temperature_improvement_c": {
            "title": "Average Skin Temperature Improvement C",
            "type": "number"
          },
          "final_core_temperature_improvement_c": {
            "title": "Final Core Temperature Improvement C",
            "type": "number"
          },
          "final_skin_temperature_improvement_c": {
            "title": "Final Skin Temperature Improvement C",
            "type": "number"
          }
        },
        "required": [
          "final_skin_temperature_improvement_c",
          "final_core_temperature_improvement_c",
          "average_skin_temperature_improvement_c"
        ],
        "title": "SimulationSummary",
        "type": "object"
      },
      "SkippedSample": {
        "description": "A planned sample day that could not be simulated for data reasons.",
        "properties": {
          "message": {
            "title": "Message",
            "type": "string"
          },
          "reason_code": {
            "title": "Reason Code",
            "type": "string"
          },
          "sample_date_local": {
            "format": "date-time",
            "title": "Sample Date Local",
            "type": "string"
          },
          "weight_days": {
            "minimum": 1.0,
            "title": "Weight Days",
            "type": "integer"
          }
        },
        "required": [
          "sample_date_local",
          "weight_days",
          "reason_code",
          "message"
        ],
        "title": "SkippedSample",
        "type": "object"
      },
      "SpectrumPoint": {
        "properties": {
          "value": {
            "title": "Value",
            "type": "number"
          },
          "wavelength_um": {
            "title": "Wavelength Um",
            "type": "number"
          }
        },
        "required": [
          "wavelength_um",
          "value"
        ],
        "title": "SpectrumPoint",
        "type": "object"
      },
      "SpectrumResponse": {
        "properties": {
          "points": {
            "items": {
              "$ref": "#/components/schemas/SpectrumPoint"
            },
            "title": "Points",
            "type": "array"
          },
          "summary": {
            "$ref": "#/components/schemas/SpectrumSummary"
          }
        },
        "required": [
          "summary",
          "points"
        ],
        "title": "SpectrumResponse",
        "type": "object"
      },
      "SpectrumSummary": {
        "properties": {
          "created_at": {
            "format": "date-time",
            "title": "Created At",
            "type": "string"
          },
          "file_checksum_sha256": {
            "title": "File Checksum Sha256",
            "type": "string"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "maximum_wavelength_um": {
            "title": "Maximum Wavelength Um",
            "type": "number"
          },
          "minimum_wavelength_um": {
            "title": "Minimum Wavelength Um",
            "type": "number"
          },
          "original_filename": {
            "title": "Original Filename",
            "type": "string"
          },
          "point_count": {
            "title": "Point Count",
            "type": "integer"
          },
          "spectrum_type": {
            "title": "Spectrum Type",
            "type": "string"
          },
          "wavelength_unit": {
            "title": "Wavelength Unit",
            "type": "string"
          }
        },
        "required": [
          "id",
          "spectrum_type",
          "wavelength_unit",
          "point_count",
          "minimum_wavelength_um",
          "maximum_wavelength_um",
          "original_filename",
          "file_checksum_sha256",
          "created_at"
        ],
        "title": "SpectrumSummary",
        "type": "object"
      },
      "TimeSeriesPoint": {
        "properties": {
          "absorbed_solar_w_m2": {
            "title": "Absorbed Solar W M2",
            "type": "number"
          },
          "convection_w_m2": {
            "title": "Convection W M2",
            "type": "number"
          },
          "core_temperature_c": {
            "title": "Core Temperature C",
            "type": "number"
          },
          "core_to_skin_w_m2": {
            "title": "Core To Skin W M2",
            "type": "number"
          },
          "evaporation_w_m2": {
            "title": "Evaporation W M2",
            "type": "number"
          },
          "longwave_radiation_w_m2": {
            "title": "Longwave Radiation W M2",
            "type": "number"
          },
          "maximum_evaporation_w_m2": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Maximum Evaporation W M2"
          },
          "minute": {
            "title": "Minute",
            "type": "number"
          },
          "skin_temperature_c": {
            "title": "Skin Temperature C",
            "type": "number"
          },
          "skin_wettedness": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Skin Wettedness"
          }
        },
        "required": [
          "minute",
          "core_temperature_c",
          "skin_temperature_c",
          "convection_w_m2",
          "longwave_radiation_w_m2",
          "evaporation_w_m2",
          "absorbed_solar_w_m2",
          "core_to_skin_w_m2"
        ],
        "title": "TimeSeriesPoint",
        "type": "object"
      },
      "ValidationError": {
        "properties": {
          "ctx": {
            "title": "Context",
            "type": "object"
          },
          "input": {
            "title": "Input"
          },
          "loc": {
            "items": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "integer"
                }
              ]
            },
            "title": "Location",
            "type": "array"
          },
          "msg": {
            "title": "Message",
            "type": "string"
          },
          "type": {
            "title": "Error Type",
            "type": "string"
          }
        },
        "required": [
          "loc",
          "msg",
          "type"
        ],
        "title": "ValidationError",
        "type": "object"
      },
      "WeatherGap": {
        "description": "A break in the hourly timeline between two consecutive points.",
        "properties": {
          "end": {
            "format": "date-time",
            "title": "End",
            "type": "string"
          },
          "missing_steps": {
            "minimum": 1.0,
            "title": "Missing Steps",
            "type": "integer"
          },
          "start": {
            "format": "date-time",
            "title": "Start",
            "type": "string"
          }
        },
        "required": [
          "start",
          "end",
          "missing_steps"
        ],
        "title": "WeatherGap",
        "type": "object"
      },
      "WeatherPoint": {
        "properties": {
          "air_temperature_c": {
            "title": "Air Temperature C",
            "type": "number"
          },
          "diffuse_radiation_w_m2": {
            "title": "Diffuse Radiation W M2",
            "type": "number"
          },
          "direct_radiation_w_m2": {
            "title": "Direct Radiation W M2",
            "type": "number"
          },
          "dni_w_m2": {
            "title": "Dni W M2",
            "type": "number"
          },
          "ghi_w_m2": {
            "title": "Ghi W M2",
            "type": "number"
          },
          "relative_humidity_percent": {
            "title": "Relative Humidity Percent",
            "type": "number"
          },
          "timestamp": {
            "format": "date-time",
            "title": "Timestamp",
            "type": "string"
          },
          "wind_speed_m_s": {
            "title": "Wind Speed M S",
            "type": "number"
          }
        },
        "required": [
          "timestamp",
          "air_temperature_c",
          "relative_humidity_percent",
          "wind_speed_m_s",
          "ghi_w_m2",
          "direct_radiation_w_m2",
          "diffuse_radiation_w_m2",
          "dni_w_m2"
        ],
        "title": "WeatherPoint",
        "type": "object"
      },
      "WeatherQualityReport": {
        "description": "Result of normalising a raw weather timeline (Stage 1, PR-1).",
        "properties": {
          "duplicates_removed": {
            "default": 0,
            "title": "Duplicates Removed",
            "type": "integer"
          },
          "expected_step_seconds": {
            "exclusiveMinimum": 0.0,
            "title": "Expected Step Seconds",
            "type": "integer"
          },
          "first_timestamp": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "First Timestamp"
          },
          "gaps": {
            "items": {
              "$ref": "#/components/schemas/WeatherGap"
            },
            "title": "Gaps",
            "type": "array"
          },
          "last_timestamp": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Last Timestamp"
          },
          "notes": {
            "items": {
              "type": "string"
            },
            "title": "Notes",
            "type": "array"
          },
          "point_count": {
            "minimum": 0.0,
            "title": "Point Count",
            "type": "integer"
          },
          "was_sorted": {
            "default": true,
            "title": "Was Sorted",
            "type": "boolean"
          }
        },
        "required": [
          "expected_step_seconds",
          "point_count"
        ],
        "title": "WeatherQualityReport",
        "type": "object"
      },
      "WeatherSimulationRequest": {
        "properties": {
          "city_id": {
            "default": "dubai",
            "minLength": 1,
            "title": "City Id",
            "type": "string"
          },
          "control_material": {
            "$ref": "#/components/schemas/MaterialInput"
          },
          "duration_minutes": {
            "default": 120,
            "maximum": 1440.0,
            "minimum": 1.0,
            "title": "Duration Minutes",
            "type": "integer"
          },
          "environment_assumptions": {
            "$ref": "#/components/schemas/EnvironmentAssumptions"
          },
          "output_interval_minutes": {
            "default": 1,
            "maximum": 60.0,
            "minimum": 1.0,
            "title": "Output Interval Minutes",
            "type": "integer"
          },
          "person": {
            "$ref": "#/components/schemas/PersonInput"
          },
          "rc_material": {
            "$ref": "#/components/schemas/MaterialInput"
          },
          "start_time_local": {
            "format": "date-time",
            "title": "Start Time Local",
            "type": "string"
          }
        },
        "required": [
          "start_time_local",
          "person",
          "control_material",
          "rc_material"
        ],
        "title": "WeatherSimulationRequest",
        "type": "object"
      },
      "WeatherSimulationResponse": {
        "properties": {
          "city": {
            "title": "City",
            "type": "string"
          },
          "control": {
            "$ref": "#/components/schemas/ScenarioResult"
          },
          "duration_minutes": {
            "title": "Duration Minutes",
            "type": "integer"
          },
          "environment_assumptions": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/EnvironmentAssumptions"
              },
              {
                "type": "null"
              }
            ]
          },
          "environment_model_note": {
            "title": "Environment Model Note",
            "type": "string"
          },
          "model_metadata": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ModelMetadata"
              },
              {
                "type": "null"
              }
            ]
          },
          "model_name": {
            "title": "Model Name",
            "type": "string"
          },
          "model_version": {
            "title": "Model Version",
            "type": "string"
          },
          "radiative_cooling": {
            "$ref": "#/components/schemas/ScenarioResult"
          },
          "summary": {
            "$ref": "#/components/schemas/SimulationSummary"
          },
          "warning": {
            "title": "Warning",
            "type": "string"
          },
          "weather": {
            "$ref": "#/components/schemas/WeatherTimeSeries"
          }
        },
        "required": [
          "model_name",
          "model_version",
          "city",
          "duration_minutes",
          "control",
          "radiative_cooling",
          "summary",
          "warning",
          "weather",
          "environment_model_note"
        ],
        "title": "WeatherSimulationResponse",
        "type": "object"
      },
      "WeatherSourceMetadata": {
        "properties": {
          "attribution": {
            "title": "Attribution",
            "type": "string"
          },
          "dataset": {
            "title": "Dataset",
            "type": "string"
          },
          "downloaded_at": {
            "format": "date-time",
            "title": "Downloaded At",
            "type": "string"
          },
          "elevation_m": {
            "title": "Elevation M",
            "type": "number"
          },
          "from_cache": {
            "title": "From Cache",
            "type": "boolean"
          },
          "latitude": {
            "title": "Latitude",
            "type": "number"
          },
          "longitude": {
            "title": "Longitude",
            "type": "number"
          },
          "model": {
            "title": "Model",
            "type": "string"
          },
          "payload_sha256": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Payload Sha256"
          },
          "provider": {
            "title": "Provider",
            "type": "string"
          },
          "quality": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/WeatherQualityReport"
              },
              {
                "type": "null"
              }
            ]
          },
          "timezone": {
            "title": "Timezone",
            "type": "string"
          }
        },
        "required": [
          "provider",
          "dataset",
          "model",
          "latitude",
          "longitude",
          "elevation_m",
          "timezone",
          "downloaded_at",
          "from_cache",
          "attribution"
        ],
        "title": "WeatherSourceMetadata",
        "type": "object"
      },
      "WeatherTimeSeries": {
        "properties": {
          "city": {
            "$ref": "#/components/schemas/CityResponse"
          },
          "points": {
            "items": {
              "$ref": "#/components/schemas/WeatherPoint"
            },
            "title": "Points",
            "type": "array"
          },
          "requested_end_time": {
            "format": "date-time",
            "title": "Requested End Time",
            "type": "string"
          },
          "requested_start_time": {
            "format": "date-time",
            "title": "Requested Start Time",
            "type": "string"
          },
          "source": {
            "$ref": "#/components/schemas/WeatherSourceMetadata"
          }
        },
        "required": [
          "city",
          "requested_start_time",
          "requested_end_time",
          "points",
          "source"
        ],
        "title": "WeatherTimeSeries",
        "type": "object"
      }
    }
  },
  "info": {
    "description": "Backend API for simulating and evaluating radiative cooling clothing under global climate conditions.",
    "title": "Global Radiative Cooling Clothing Climate Adaptation API",
    "version": "0.2.0"
  },
  "openapi": "3.1.0",
  "paths": {
    "/api/v1/benchmarks/gagge": {
      "post": {
        "operationId": "compare_with_gagge_api_v1_benchmarks_gagge_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/GaggeBenchmarkRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GaggeBenchmarkResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Compare With Gagge",
        "tags": [
          "benchmarks"
        ]
      }
    },
    "/api/v1/global-batches": {
      "get": {
        "operationId": "list_global_batches_api_v1_global_batches_get",
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "required": false,
            "schema": {
              "default": 20,
              "maximum": 100,
              "minimum": 1,
              "title": "Limit",
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "offset",
            "required": false,
            "schema": {
              "default": 0,
              "minimum": 0,
              "title": "Offset",
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GlobalBatchListResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "List Global Batches",
        "tags": [
          "global-batches"
        ]
      },
      "post": {
        "operationId": "create_global_batch_api_v1_global_batches_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/GlobalBatchCreate"
              }
            }
          },
          "required": true
        },
        "responses": {
          "202": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GlobalBatchResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Create Global Batch",
        "tags": [
          "global-batches"
        ]
      }
    },
    "/api/v1/global-batches/cities": {
      "get": {
        "operationId": "get_supported_cities_api_v1_global_batches_cities_get",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "additionalProperties": true,
                  "title": "Response Get Supported Cities Api V1 Global Batches Cities Get",
                  "type": "object"
                }
              }
            },
            "description": "Successful Response"
          }
        },
        "summary": "Get Supported Cities",
        "tags": [
          "global-batches"
        ]
      }
    },
    "/api/v1/global-batches/estimate": {
      "post": {
        "operationId": "estimate_global_batch_api_v1_global_batches_estimate_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/GlobalBatchCreate"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GlobalBatchEstimateResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Estimate Global Batch",
        "tags": [
          "global-batches"
        ]
      }
    },
    "/api/v1/global-batches/{batch_id}": {
      "get": {
        "operationId": "get_global_batch_api_v1_global_batches__batch_id__get",
        "parameters": [
          {
            "in": "path",
            "name": "batch_id",
            "required": true,
            "schema": {
              "title": "Batch Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GlobalBatchDetail"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Get Global Batch",
        "tags": [
          "global-batches"
        ]
      }
    },
    "/api/v1/global-batches/{batch_id}/cancel": {
      "post": {
        "operationId": "cancel_global_batch_api_v1_global_batches__batch_id__cancel_post",
        "parameters": [
          {
            "in": "path",
            "name": "batch_id",
            "required": true,
            "schema": {
              "title": "Batch Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GlobalBatchResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Cancel Global Batch",
        "tags": [
          "global-batches"
        ]
      }
    },
    "/api/v1/global-batches/{batch_id}/export": {
      "get": {
        "operationId": "export_global_batch_api_v1_global_batches__batch_id__export_get",
        "parameters": [
          {
            "in": "path",
            "name": "batch_id",
            "required": true,
            "schema": {
              "title": "Batch Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {}
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Export Global Batch",
        "tags": [
          "global-batches"
        ]
      }
    },
    "/api/v1/global-batches/{batch_id}/geojson": {
      "get": {
        "operationId": "get_global_batch_geojson_api_v1_global_batches__batch_id__geojson_get",
        "parameters": [
          {
            "in": "path",
            "name": "batch_id",
            "required": true,
            "schema": {
              "title": "Batch Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "additionalProperties": true,
                  "title": "Response Get Global Batch Geojson Api V1 Global Batches  Batch Id  Geojson Get",
                  "type": "object"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Get Global Batch Geojson",
        "tags": [
          "global-batches"
        ]
      }
    },
    "/api/v1/global-batches/{batch_id}/retry-failed": {
      "post": {
        "operationId": "retry_failed_cities_api_v1_global_batches__batch_id__retry_failed_post",
        "parameters": [
          {
            "in": "path",
            "name": "batch_id",
            "required": true,
            "schema": {
              "title": "Batch Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "202": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GlobalBatchResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Retry Failed Cities",
        "tags": [
          "global-batches"
        ]
      }
    },
    "/api/v1/health": {
      "get": {
        "operationId": "health_check_api_v1_health_get",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {}
              }
            },
            "description": "Successful Response"
          }
        },
        "summary": "Health Check"
      }
    },
    "/api/v1/materials": {
      "get": {
        "operationId": "list_materials_api_v1_materials_get",
        "parameters": [
          {
            "in": "query",
            "name": "include_archived",
            "required": false,
            "schema": {
              "default": false,
              "title": "Include Archived",
              "type": "boolean"
            }
          },
          {
            "in": "query",
            "name": "search",
            "required": false,
            "schema": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ],
              "title": "Search"
            }
          },
          {
            "in": "query",
            "name": "limit",
            "required": false,
            "schema": {
              "default": 20,
              "maximum": 100,
              "minimum": 1,
              "title": "Limit",
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "offset",
            "required": false,
            "schema": {
              "default": 0,
              "minimum": 0,
              "title": "Offset",
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MaterialListResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "List Materials",
        "tags": [
          "materials"
        ]
      },
      "post": {
        "operationId": "create_material_api_v1_materials_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MaterialCreate"
              }
            }
          },
          "required": true
        },
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MaterialResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Create Material",
        "tags": [
          "materials"
        ]
      }
    },
    "/api/v1/materials/versions/{version_id}/simulation-input": {
      "get": {
        "operationId": "material_version_to_simulation_input_api_v1_materials_versions__version_id__simulation_input_get",
        "parameters": [
          {
            "in": "path",
            "name": "version_id",
            "required": true,
            "schema": {
              "title": "Version Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MaterialInput"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Material Version To Simulation Input",
        "tags": [
          "materials"
        ]
      }
    },
    "/api/v1/materials/versions/{version_id}/spectra": {
      "post": {
        "operationId": "upload_material_spectrum_api_v1_materials_versions__version_id__spectra_post",
        "parameters": [
          {
            "in": "path",
            "name": "version_id",
            "required": true,
            "schema": {
              "title": "Version Id",
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Body_upload_material_spectrum_api_v1_materials_versions__version_id__spectra_post"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SpectrumResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Upload Material Spectrum",
        "tags": [
          "materials"
        ]
      }
    },
    "/api/v1/materials/versions/{version_id}/spectra/{spectrum_type}": {
      "get": {
        "operationId": "get_material_spectrum_api_v1_materials_versions__version_id__spectra__spectrum_type__get",
        "parameters": [
          {
            "in": "path",
            "name": "version_id",
            "required": true,
            "schema": {
              "title": "Version Id",
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "spectrum_type",
            "required": true,
            "schema": {
              "title": "Spectrum Type",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SpectrumResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Get Material Spectrum",
        "tags": [
          "materials"
        ]
      }
    },
    "/api/v1/materials/{material_id}": {
      "get": {
        "operationId": "get_material_api_v1_materials__material_id__get",
        "parameters": [
          {
            "in": "path",
            "name": "material_id",
            "required": true,
            "schema": {
              "title": "Material Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MaterialResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Get Material",
        "tags": [
          "materials"
        ]
      },
      "patch": {
        "operationId": "update_material_api_v1_materials__material_id__patch",
        "parameters": [
          {
            "in": "path",
            "name": "material_id",
            "required": true,
            "schema": {
              "title": "Material Id",
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MaterialUpdate"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MaterialResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Update Material",
        "tags": [
          "materials"
        ]
      }
    },
    "/api/v1/materials/{material_id}/versions": {
      "post": {
        "operationId": "create_material_version_api_v1_materials__material_id__versions_post",
        "parameters": [
          {
            "in": "path",
            "name": "material_id",
            "required": true,
            "schema": {
              "title": "Material Id",
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MaterialVersionCreate"
              }
            }
          },
          "required": true
        },
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MaterialVersionResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Create Material Version",
        "tags": [
          "materials"
        ]
      }
    },
    "/api/v1/model/environment-assumptions/defaults": {
      "get": {
        "operationId": "get_default_environment_assumptions_api_v1_model_environment_assumptions_defaults_get",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/EnvironmentAssumptions"
                }
              }
            },
            "description": "Successful Response"
          }
        },
        "summary": "Get Default Environment Assumptions",
        "tags": [
          "model"
        ]
      }
    },
    "/api/v1/model/parameters": {
      "get": {
        "operationId": "get_model_parameters_api_v1_model_parameters_get",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ModelParameterManifest"
                }
              }
            },
            "description": "Successful Response"
          }
        },
        "summary": "Get Model Parameters",
        "tags": [
          "model"
        ]
      }
    },
    "/api/v1/simulations/jobs": {
      "get": {
        "operationId": "list_simulation_jobs_api_v1_simulations_jobs_get",
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "required": false,
            "schema": {
              "default": 20,
              "maximum": 100,
              "minimum": 1,
              "title": "Limit",
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "offset",
            "required": false,
            "schema": {
              "default": 0,
              "minimum": 0,
              "title": "Offset",
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SimulationJobListResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "List Simulation Jobs",
        "tags": [
          "simulations"
        ]
      },
      "post": {
        "operationId": "create_simulation_job_api_v1_simulations_jobs_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/WeatherSimulationRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "202": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SimulationJobResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Create Simulation Job",
        "tags": [
          "simulations"
        ]
      }
    },
    "/api/v1/simulations/jobs/{job_id}": {
      "get": {
        "operationId": "get_simulation_job_api_v1_simulations_jobs__job_id__get",
        "parameters": [
          {
            "in": "path",
            "name": "job_id",
            "required": true,
            "schema": {
              "title": "Job Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SimulationJobDetail"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Get Simulation Job",
        "tags": [
          "simulations"
        ]
      }
    },
    "/api/v1/simulations/jobs/{job_id}/cancel": {
      "post": {
        "operationId": "cancel_simulation_job_api_v1_simulations_jobs__job_id__cancel_post",
        "parameters": [
          {
            "in": "path",
            "name": "job_id",
            "required": true,
            "schema": {
              "title": "Job Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SimulationJobResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Cancel Simulation Job",
        "tags": [
          "simulations"
        ]
      }
    },
    "/api/v1/simulations/jobs/{job_id}/events": {
      "get": {
        "operationId": "simulation_job_events_api_v1_simulations_jobs__job_id__events_get",
        "parameters": [
          {
            "in": "path",
            "name": "job_id",
            "required": true,
            "schema": {
              "title": "Job Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {}
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Simulation Job Events",
        "tags": [
          "simulations"
        ]
      }
    },
    "/api/v1/simulations/jobs/{job_id}/export": {
      "get": {
        "operationId": "export_simulation_result_api_v1_simulations_jobs__job_id__export_get",
        "parameters": [
          {
            "in": "path",
            "name": "job_id",
            "required": true,
            "schema": {
              "title": "Job Id",
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "format",
            "required": false,
            "schema": {
              "default": "csv",
              "pattern": "^(csv|json)$",
              "title": "Format",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {}
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Export Simulation Result",
        "tags": [
          "simulations"
        ]
      }
    },
    "/api/v1/simulations/jobs/{job_id}/result": {
      "get": {
        "operationId": "get_simulation_result_api_v1_simulations_jobs__job_id__result_get",
        "parameters": [
          {
            "in": "path",
            "name": "job_id",
            "required": true,
            "schema": {
              "title": "Job Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/WeatherSimulationResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Get Simulation Result",
        "tags": [
          "simulations"
        ]
      }
    },
    "/api/v1/simulations/run": {
      "post": {
        "operationId": "run_simulation_api_v1_simulations_run_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/SimulationRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SimulationResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Run Simulation",
        "tags": [
          "simulations"
        ]
      }
    },
    "/api/v1/simulations/run-weather": {
      "post": {
        "operationId": "run_weather_simulation_api_v1_simulations_run_weather_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/WeatherSimulationRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/WeatherSimulationResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Run Weather Simulation",
        "tags": [
          "simulations"
        ]
      }
    },
    "/api/v1/weather/cities": {
      "get": {
        "operationId": "list_cities_api_v1_weather_cities_get",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "items": {
                    "$ref": "#/components/schemas/CityResponse"
                  },
                  "title": "Response List Cities Api V1 Weather Cities Get",
                  "type": "array"
                }
              }
            },
            "description": "Successful Response"
          }
        },
        "summary": "List Cities",
        "tags": [
          "weather"
        ]
      }
    },
    "/api/v1/weather/history": {
      "get": {
        "operationId": "weather_history_api_v1_weather_history_get",
        "parameters": [
          {
            "in": "query",
            "name": "city_id",
            "required": true,
            "schema": {
              "title": "City Id",
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "start_time_local",
            "required": true,
            "schema": {
              "format": "date-time",
              "title": "Start Time Local",
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "duration_minutes",
            "required": false,
            "schema": {
              "default": 120,
              "maximum": 1440,
              "minimum": 1,
              "title": "Duration Minutes",
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/WeatherTimeSeries"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Weather History",
        "tags": [
          "weather"
        ]
      }
    }
  }
}
```

### File: `.stage-3-api-contract-after.json`
```json
{
  "components": {
    "schemas": {
      "BenchmarkMetric": {
        "properties": {
          "final_difference_c": {
            "title": "Final Difference C",
            "type": "number"
          },
          "maximum_absolute_difference_c": {
            "title": "Maximum Absolute Difference C",
            "type": "number"
          },
          "passed": {
            "title": "Passed",
            "type": "boolean"
          },
          "root_mean_square_difference_c": {
            "title": "Root Mean Square Difference C",
            "type": "number"
          },
          "tolerance_c": {
            "title": "Tolerance C",
            "type": "number"
          }
        },
        "required": [
          "final_difference_c",
          "maximum_absolute_difference_c",
          "root_mean_square_difference_c",
          "tolerance_c",
          "passed"
        ],
        "title": "BenchmarkMetric",
        "type": "object"
      },
      "BenchmarkSeriesPoint": {
        "properties": {
          "minute": {
            "title": "Minute",
            "type": "integer"
          },
          "prototype_core_temperature_c": {
            "title": "Prototype Core Temperature C",
            "type": "number"
          },
          "prototype_evaporation_w_m2": {
            "title": "Prototype Evaporation W M2",
            "type": "number"
          },
          "prototype_skin_temperature_c": {
            "title": "Prototype Skin Temperature C",
            "type": "number"
          },
          "reference_core_temperature_c": {
            "title": "Reference Core Temperature C",
            "type": "number"
          },
          "reference_evaporation_w_m2": {
            "title": "Reference Evaporation W M2",
            "type": "number"
          },
          "reference_skin_temperature_c": {
            "title": "Reference Skin Temperature C",
            "type": "number"
          }
        },
        "required": [
          "minute",
          "prototype_core_temperature_c",
          "prototype_skin_temperature_c",
          "prototype_evaporation_w_m2",
          "reference_core_temperature_c",
          "reference_skin_temperature_c",
          "reference_evaporation_w_m2"
        ],
        "title": "BenchmarkSeriesPoint",
        "type": "object"
      },
      "BenchmarkTolerances": {
        "description": "Acceptance thresholds on the maximum absolute trajectory difference.",
        "properties": {
          "core_temperature_c": {
            "default": 0.3,
            "exclusiveMinimum": 0.0,
            "maximum": 5.0,
            "title": "Core Temperature C",
            "type": "number"
          },
          "skin_temperature_c": {
            "default": 1.0,
            "exclusiveMinimum": 0.0,
            "maximum": 10.0,
            "title": "Skin Temperature C",
            "type": "number"
          }
        },
        "title": "BenchmarkTolerances",
        "type": "object"
      },
      "BodyThermalSummary": {
        "description": "Heat capacities derived from PersonInput (Stage 3, ADR 0001).",
        "properties": {
          "body_mass_kg": {
            "title": "Body Mass Kg",
            "type": "number"
          },
          "body_surface_area_m2": {
            "title": "Body Surface Area M2",
            "type": "number"
          },
          "core_heat_capacity_j_m2k": {
            "title": "Core Heat Capacity J M2K",
            "type": "number"
          },
          "skin_heat_capacity_j_m2k": {
            "title": "Skin Heat Capacity J M2K",
            "type": "number"
          }
        },
        "required": [
          "body_mass_kg",
          "body_surface_area_m2",
          "core_heat_capacity_j_m2k",
          "skin_heat_capacity_j_m2k"
        ],
        "title": "BodyThermalSummary",
        "type": "object"
      },
      "Body_upload_material_spectrum_api_v1_materials_versions__version_id__spectra_post": {
        "properties": {
          "file": {
            "contentMediaType": "application/octet-stream",
            "title": "File",
            "type": "string"
          },
          "spectrum_type": {
            "title": "Spectrum Type",
            "type": "string"
          }
        },
        "required": [
          "spectrum_type",
          "file"
        ],
        "title": "Body_upload_material_spectrum_api_v1_materials_versions__version_id__spectra_post",
        "type": "object"
      },
      "CityResponse": {
        "properties": {
          "climate_type": {
            "title": "Climate Type",
            "type": "string"
          },
          "country": {
            "title": "Country",
            "type": "string"
          },
          "elevation_m": {
            "title": "Elevation M",
            "type": "number"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "latitude": {
            "title": "Latitude",
            "type": "number"
          },
          "longitude": {
            "title": "Longitude",
            "type": "number"
          },
          "name": {
            "title": "Name",
            "type": "string"
          },
          "timezone": {
            "title": "Timezone",
            "type": "string"
          }
        },
        "required": [
          "id",
          "name",
          "country",
          "latitude",
          "longitude",
          "elevation_m",
          "timezone",
          "climate_type"
        ],
        "title": "CityResponse",
        "type": "object"
      },
      "ClothingSummary": {
        "description": "Resolved clothing quantities actually used by the solver.",
        "properties": {
          "clothing_area_factor": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Clothing Area Factor"
          },
          "clothing_area_factor_source": {
            "anyOf": [
              {
                "enum": [
                  "material_input",
                  "derived_from_clo"
                ],
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Clothing Area Factor Source"
          },
          "dry_resistance_m2k_w": {
            "title": "Dry Resistance M2K W",
            "type": "number"
          },
          "evaporative_resistance_m2pa_w": {
            "title": "Evaporative Resistance M2Pa W",
            "type": "number"
          },
          "evaporative_resistance_source": {
            "enum": [
              "material_input",
              "derived_from_clo"
            ],
            "title": "Evaporative Resistance Source",
            "type": "string"
          },
          "infrared_transmittance": {
            "title": "Infrared Transmittance",
            "type": "number"
          }
        },
        "required": [
          "dry_resistance_m2k_w",
          "evaporative_resistance_m2pa_w",
          "evaporative_resistance_source",
          "infrared_transmittance"
        ],
        "title": "ClothingSummary",
        "type": "object"
      },
      "DailyAdaptationResult": {
        "properties": {
          "average_core_improvement_c": {
            "title": "Average Core Improvement C",
            "type": "number"
          },
          "average_skin_improvement_c": {
            "title": "Average Skin Improvement C",
            "type": "number"
          },
          "beneficial": {
            "title": "Beneficial",
            "type": "boolean"
          },
          "exposure_eligible": {
            "title": "Exposure Eligible",
            "type": "boolean"
          },
          "final_skin_improvement_c": {
            "title": "Final Skin Improvement C",
            "type": "number"
          },
          "maximum_air_temperature_c": {
            "title": "Maximum Air Temperature C",
            "type": "number"
          },
          "maximum_skin_improvement_c": {
            "title": "Maximum Skin Improvement C",
            "type": "number"
          },
          "maximum_solar_radiation_w_m2": {
            "title": "Maximum Solar Radiation W M2",
            "type": "number"
          },
          "mean_air_temperature_c": {
            "title": "Mean Air Temperature C",
            "type": "number"
          },
          "mean_solar_radiation_w_m2": {
            "title": "Mean Solar Radiation W M2",
            "type": "number"
          },
          "sample_date_local": {
            "format": "date-time",
            "title": "Sample Date Local",
            "type": "string"
          },
          "weather_from_cache": {
            "title": "Weather From Cache",
            "type": "boolean"
          },
          "weight_days": {
            "minimum": 1.0,
            "title": "Weight Days",
            "type": "integer"
          }
        },
        "required": [
          "sample_date_local",
          "weight_days",
          "mean_air_temperature_c",
          "maximum_air_temperature_c",
          "mean_solar_radiation_w_m2",
          "maximum_solar_radiation_w_m2",
          "exposure_eligible",
          "beneficial",
          "average_skin_improvement_c",
          "final_skin_improvement_c",
          "average_core_improvement_c",
          "maximum_skin_improvement_c",
          "weather_from_cache"
        ],
        "title": "DailyAdaptationResult",
        "type": "object"
      },
      "EnergyDiagnostics": {
        "properties": {
          "energy_residual_j_m2": {
            "title": "Energy Residual J M2",
            "type": "number"
          },
          "integrated_net_heat_j_m2": {
            "title": "Integrated Net Heat J M2",
            "type": "number"
          },
          "maximum_core_step_c": {
            "title": "Maximum Core Step C",
            "type": "number"
          },
          "maximum_skin_step_c": {
            "title": "Maximum Skin Step C",
            "type": "number"
          },
          "normalized_residual_percent": {
            "title": "Normalized Residual Percent",
            "type": "number"
          },
          "solver_function_evaluations": {
            "title": "Solver Function Evaluations",
            "type": "integer"
          },
          "stored_energy_change_j_m2": {
            "title": "Stored Energy Change J M2",
            "type": "number"
          }
        },
        "required": [
          "stored_energy_change_j_m2",
          "integrated_net_heat_j_m2",
          "energy_residual_j_m2",
          "normalized_residual_percent",
          "maximum_core_step_c",
          "maximum_skin_step_c",
          "solver_function_evaluations"
        ],
        "title": "EnergyDiagnostics",
        "type": "object"
      },
      "EnvironmentAssumptions": {
        "additionalProperties": false,
        "properties": {
          "fixed_sky_offset_k": {
            "default": 15.0,
            "description": "fixed_offset: T_air - T_sky",
            "maximum": 50.0,
            "minimum": 0.0,
            "reference": "Stage 1 prototype",
            "source_type": "assumed",
            "title": "Fixed Sky Offset K",
            "type": "number"
          },
          "mean_radiant_temperature_method": {
            "default": "air_plus_solar_linear",
            "enum": [
              "air_plus_solar_linear",
              "equal_to_air"
            ],
            "reference": "Stage 1 prototype",
            "source_type": "assumed",
            "title": "Mean Radiant Temperature Method",
            "type": "string"
          },
          "sky_offset_base_k": {
            "default": 5.0,
            "description": "humidity_offset: depression at 100 % RH",
            "maximum": 40.0,
            "minimum": 0.0,
            "reference": "Stage 1 prototype",
            "source_type": "assumed",
            "title": "Sky Offset Base K",
            "type": "number"
          },
          "sky_offset_humidity_range_k": {
            "default": 10.0,
            "description": "humidity_offset: additional depression at 0 % RH",
            "maximum": 40.0,
            "minimum": 0.0,
            "reference": "Stage 1 prototype",
            "source_type": "assumed",
            "title": "Sky Offset Humidity Range K",
            "type": "number"
          },
          "sky_temperature_method": {
            "default": "humidity_offset",
            "enum": [
              "humidity_offset",
              "fixed_offset",
              "swinbank"
            ],
            "reference": "Stage 1 prototype",
            "source_type": "assumed",
            "title": "Sky Temperature Method",
            "type": "string"
          },
          "sky_view_factor": {
            "default": 0.5,
            "description": "Fraction of the body's radiative view occupied by sky",
            "maximum": 1.0,
            "minimum": 0.0,
            "reference": "Standing person on an open, unobstructed site",
            "source_type": "assumed",
            "title": "Sky View Factor",
            "type": "number"
          },
          "solar_mrt_gain_cap_k": {
            "default": 15.0,
            "description": "Upper bound of the solar MRT rise",
            "maximum": 40.0,
            "minimum": 0.0,
            "reference": "Stage 1 prototype",
            "source_type": "assumed",
            "title": "Solar Mrt Gain Cap K",
            "type": "number"
          },
          "solar_mrt_gain_k_per_w_m2": {
            "default": 0.012,
            "description": "MRT rise per W/m^2 of GHI (air_plus_solar_linear only)",
            "maximum": 0.05,
            "minimum": 0.0,
            "reference": "Stage 1 prototype",
            "source_type": "assumed",
            "title": "Solar Mrt Gain K Per W M2",
            "type": "number"
          },
          "wind_speed_scaling_factor": {
            "default": 1.0,
            "description": "Multiplier from ERA5 10 m wind to body-height wind. 1.0 keeps Stage 1 behaviour; ~0.67 approximates 1.1 m height via a logarithmic profile over open terrain.",
            "exclusiveMinimum": 0.0,
            "maximum": 1.5,
            "reference": "Stage 1 prototype",
            "source_type": "assumed",
            "title": "Wind Speed Scaling Factor",
            "type": "number"
          }
        },
        "title": "EnvironmentAssumptions",
        "type": "object"
      },
      "EnvironmentInput": {
        "properties": {
          "air_temperature_c": {
            "default": 38.0,
            "maximum": 70.0,
            "minimum": -50.0,
            "title": "Air Temperature C",
            "type": "number"
          },
          "mean_radiant_temperature_c": {
            "default": 45.0,
            "maximum": 100.0,
            "minimum": -50.0,
            "title": "Mean Radiant Temperature C",
            "type": "number"
          },
          "relative_humidity_percent": {
            "default": 40.0,
            "maximum": 100.0,
            "minimum": 0.0,
            "title": "Relative Humidity Percent",
            "type": "number"
          },
          "sky_temperature_c": {
            "anyOf": [
              {
                "maximum": 70.0,
                "minimum": -100.0,
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Sky Temperature C"
          },
          "sky_view_factor": {
            "default": 0.5,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Sky View Factor",
            "type": "number"
          },
          "solar_radiation_w_m2": {
            "default": 800.0,
            "maximum": 1500.0,
            "minimum": 0.0,
            "title": "Solar Radiation W M2",
            "type": "number"
          },
          "wind_speed_m_s": {
            "default": 1.5,
            "maximum": 30.0,
            "minimum": 0.0,
            "title": "Wind Speed M S",
            "type": "number"
          }
        },
        "title": "EnvironmentInput",
        "type": "object"
      },
      "GaggeBenchmarkRequest": {
        "properties": {
          "duration_minutes": {
            "default": 60,
            "maximum": 240.0,
            "minimum": 1.0,
            "title": "Duration Minutes",
            "type": "integer"
          },
          "environment": {
            "$ref": "#/components/schemas/EnvironmentInput"
          },
          "material": {
            "$ref": "#/components/schemas/MaterialInput"
          },
          "person": {
            "$ref": "#/components/schemas/PersonInput"
          },
          "tolerances": {
            "$ref": "#/components/schemas/BenchmarkTolerances"
          }
        },
        "required": [
          "environment",
          "person",
          "material"
        ],
        "title": "GaggeBenchmarkRequest",
        "type": "object"
      },
      "GaggeBenchmarkResponse": {
        "properties": {
          "alignment_applied": {
            "items": {
              "type": "string"
            },
            "title": "Alignment Applied",
            "type": "array"
          },
          "core_temperature": {
            "$ref": "#/components/schemas/BenchmarkMetric"
          },
          "difference_core_temperature_c": {
            "title": "Difference Core Temperature C",
            "type": "number"
          },
          "difference_skin_temperature_c": {
            "title": "Difference Skin Temperature C",
            "type": "number"
          },
          "environment_note": {
            "title": "Environment Note",
            "type": "string"
          },
          "gagge": {
            "$ref": "#/components/schemas/GaggeModelOutput"
          },
          "passed": {
            "title": "Passed",
            "type": "boolean"
          },
          "prototype": {
            "$ref": "#/components/schemas/PrototypeBenchmarkOutput"
          },
          "reference_library": {
            "title": "Reference Library",
            "type": "string"
          },
          "reference_library_version": {
            "title": "Reference Library Version",
            "type": "string"
          },
          "reference_model": {
            "title": "Reference Model",
            "type": "string"
          },
          "reference_port_parity": {
            "$ref": "#/components/schemas/ReferencePortParity"
          },
          "skin_temperature": {
            "$ref": "#/components/schemas/BenchmarkMetric"
          },
          "time_series": {
            "items": {
              "$ref": "#/components/schemas/BenchmarkSeriesPoint"
            },
            "title": "Time Series",
            "type": "array"
          },
          "warning": {
            "title": "Warning",
            "type": "string"
          }
        },
        "required": [
          "reference_model",
          "reference_library",
          "reference_library_version",
          "environment_note",
          "alignment_applied",
          "prototype",
          "gagge",
          "difference_core_temperature_c",
          "difference_skin_temperature_c",
          "core_temperature",
          "skin_temperature",
          "passed",
          "time_series",
          "reference_port_parity",
          "warning"
        ],
        "title": "GaggeBenchmarkResponse",
        "type": "object"
      },
      "GaggeModelOutput": {
        "properties": {
          "core_temperature_c": {
            "title": "Core Temperature C",
            "type": "number"
          },
          "respiratory_heat_loss_w_m2": {
            "title": "Respiratory Heat Loss W M2",
            "type": "number"
          },
          "skin_blood_flow_kg_h_m2": {
            "title": "Skin Blood Flow Kg H M2",
            "type": "number"
          },
          "skin_evaporation_w_m2": {
            "title": "Skin Evaporation W M2",
            "type": "number"
          },
          "skin_heat_loss_w_m2": {
            "title": "Skin Heat Loss W M2",
            "type": "number"
          },
          "skin_temperature_c": {
            "title": "Skin Temperature C",
            "type": "number"
          },
          "skin_wettedness": {
            "title": "Skin Wettedness",
            "type": "number"
          },
          "standard_effective_temperature_c": {
            "title": "Standard Effective Temperature C",
            "type": "number"
          }
        },
        "required": [
          "core_temperature_c",
          "skin_temperature_c",
          "skin_evaporation_w_m2",
          "skin_heat_loss_w_m2",
          "respiratory_heat_loss_w_m2",
          "skin_blood_flow_kg_h_m2",
          "skin_wettedness",
          "standard_effective_temperature_c"
        ],
        "title": "GaggeModelOutput",
        "type": "object"
      },
      "GlobalBatchCreate": {
        "properties": {
          "analysis_resolution": {
            "default": "representative",
            "enum": [
              "representative",
              "daily"
            ],
            "title": "Analysis Resolution",
            "type": "string"
          },
          "city_ids": {
            "items": {
              "type": "string"
            },
            "maxItems": 100,
            "minItems": 1,
            "title": "City Ids",
            "type": "array"
          },
          "control_material": {
            "$ref": "#/components/schemas/MaterialInput"
          },
          "daily_stride_days": {
            "default": 1,
            "maximum": 7.0,
            "minimum": 1.0,
            "title": "Daily Stride Days",
            "type": "integer"
          },
          "duration_minutes": {
            "default": 120,
            "maximum": 1440.0,
            "minimum": 30.0,
            "title": "Duration Minutes",
            "type": "integer"
          },
          "enable_heatwave_analysis": {
            "default": true,
            "title": "Enable Heatwave Analysis",
            "type": "boolean"
          },
          "end_month": {
            "default": 12,
            "maximum": 12.0,
            "minimum": 1.0,
            "title": "End Month",
            "type": "integer"
          },
          "environment_assumptions": {
            "$ref": "#/components/schemas/EnvironmentAssumptions"
          },
          "execution_profile": {
            "default": "auto",
            "enum": [
              "auto",
              "standard",
              "large"
            ],
            "title": "Execution Profile",
            "type": "string"
          },
          "exposure_match_mode": {
            "default": "all",
            "enum": [
              "all",
              "any"
            ],
            "title": "Exposure Match Mode",
            "type": "string"
          },
          "heatwave_minimum_consecutive_days": {
            "default": 3,
            "maximum": 30.0,
            "minimum": 2.0,
            "title": "Heatwave Minimum Consecutive Days",
            "type": "integer"
          },
          "heatwave_temperature_threshold_c": {
            "default": 35.0,
            "maximum": 70.0,
            "minimum": -20.0,
            "title": "Heatwave Temperature Threshold C",
            "type": "number"
          },
          "local_start_hour": {
            "default": 12,
            "maximum": 23.0,
            "minimum": 0.0,
            "title": "Local Start Hour",
            "type": "integer"
          },
          "minimum_air_temperature_c": {
            "anyOf": [
              {
                "maximum": 70.0,
                "minimum": -50.0,
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "default": 30.0,
            "title": "Minimum Air Temperature C"
          },
          "minimum_skin_improvement_c": {
            "default": 0.2,
            "maximum": 10.0,
            "minimum": -5.0,
            "title": "Minimum Skin Improvement C",
            "type": "number"
          },
          "minimum_solar_radiation_w_m2": {
            "anyOf": [
              {
                "maximum": 1500.0,
                "minimum": 0.0,
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "default": 300.0,
            "title": "Minimum Solar Radiation W M2"
          },
          "name": {
            "default": "Global multi-day climate adaptation analysis",
            "maxLength": 200,
            "minLength": 1,
            "title": "Name",
            "type": "string"
          },
          "output_interval_minutes": {
            "default": 10,
            "maximum": 60.0,
            "minimum": 1.0,
            "title": "Output Interval Minutes",
            "type": "integer"
          },
          "person": {
            "$ref": "#/components/schemas/PersonInput"
          },
          "rc_material": {
            "$ref": "#/components/schemas/MaterialInput"
          },
          "representative_day": {
            "anyOf": [
              {
                "maximum": 28.0,
                "minimum": 1.0,
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Representative Day"
          },
          "resume_from_checkpoint": {
            "default": true,
            "title": "Resume From Checkpoint",
            "type": "boolean"
          },
          "sample_days_per_month": {
            "default": 3,
            "maximum": 7.0,
            "minimum": 1.0,
            "title": "Sample Days Per Month",
            "type": "integer"
          },
          "start_month": {
            "default": 1,
            "maximum": 12.0,
            "minimum": 1.0,
            "title": "Start Month",
            "type": "integer"
          },
          "year": {
            "default": 2023,
            "maximum": 2100.0,
            "minimum": 1940.0,
            "title": "Year",
            "type": "integer"
          }
        },
        "required": [
          "city_ids",
          "person",
          "control_material",
          "rc_material"
        ],
        "title": "GlobalBatchCreate",
        "type": "object"
      },
      "GlobalBatchDetail": {
        "properties": {
          "cancelled_city_count": {
            "title": "Cancelled City Count",
            "type": "integer"
          },
          "celery_group_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Celery Group Id"
          },
          "city_results": {
            "items": {
              "$ref": "#/components/schemas/GlobalCityResultResponse"
            },
            "title": "City Results",
            "type": "array"
          },
          "completed_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Completed At"
          },
          "completed_city_count": {
            "title": "Completed City Count",
            "type": "integer"
          },
          "created_at": {
            "format": "date-time",
            "title": "Created At",
            "type": "string"
          },
          "error_message": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Error Message"
          },
          "failed_city_count": {
            "title": "Failed City Count",
            "type": "integer"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "progress": {
            "title": "Progress",
            "type": "integer"
          },
          "request": {
            "$ref": "#/components/schemas/GlobalBatchCreate"
          },
          "stage": {
            "title": "Stage",
            "type": "string"
          },
          "started_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Started At"
          },
          "status": {
            "enum": [
              "queued",
              "running",
              "cancelling",
              "cancelled",
              "completed",
              "partial_completed",
              "failed"
            ],
            "title": "Status",
            "type": "string"
          },
          "summary": {
            "anyOf": [
              {
                "additionalProperties": true,
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Summary"
          },
          "total_city_count": {
            "title": "Total City Count",
            "type": "integer"
          },
          "updated_at": {
            "format": "date-time",
            "title": "Updated At",
            "type": "string"
          }
        },
        "required": [
          "id",
          "celery_group_id",
          "status",
          "stage",
          "progress",
          "total_city_count",
          "completed_city_count",
          "failed_city_count",
          "cancelled_city_count",
          "summary",
          "error_message",
          "created_at",
          "updated_at",
          "started_at",
          "completed_at",
          "request",
          "city_results"
        ],
        "title": "GlobalBatchDetail",
        "type": "object"
      },
      "GlobalBatchEstimateResponse": {
        "properties": {
          "analysis_resolution": {
            "enum": [
              "representative",
              "daily"
            ],
            "title": "Analysis Resolution",
            "type": "string"
          },
          "checkpoint_count_per_city": {
            "title": "Checkpoint Count Per City",
            "type": "integer"
          },
          "city_count": {
            "title": "City Count",
            "type": "integer"
          },
          "estimated_weather_requests": {
            "title": "Estimated Weather Requests",
            "type": "integer"
          },
          "heatwave_analysis_available": {
            "title": "Heatwave Analysis Available",
            "type": "boolean"
          },
          "month_count": {
            "title": "Month Count",
            "type": "integer"
          },
          "resolved_execution_profile": {
            "enum": [
              "auto",
              "standard",
              "large"
            ],
            "title": "Resolved Execution Profile",
            "type": "string"
          },
          "resolved_queue": {
            "title": "Resolved Queue",
            "type": "string"
          },
          "samples_per_city": {
            "title": "Samples Per City",
            "type": "integer"
          },
          "thermal_simulation_count": {
            "title": "Thermal Simulation Count",
            "type": "integer"
          },
          "total_samples": {
            "title": "Total Samples",
            "type": "integer"
          }
        },
        "required": [
          "city_count",
          "month_count",
          "samples_per_city",
          "total_samples",
          "thermal_simulation_count",
          "estimated_weather_requests",
          "analysis_resolution",
          "resolved_execution_profile",
          "resolved_queue",
          "checkpoint_count_per_city",
          "heatwave_analysis_available"
        ],
        "title": "GlobalBatchEstimateResponse",
        "type": "object"
      },
      "GlobalBatchListResponse": {
        "properties": {
          "items": {
            "items": {
              "$ref": "#/components/schemas/GlobalBatchResponse"
            },
            "title": "Items",
            "type": "array"
          },
          "limit": {
            "title": "Limit",
            "type": "integer"
          },
          "offset": {
            "title": "Offset",
            "type": "integer"
          },
          "total": {
            "title": "Total",
            "type": "integer"
          }
        },
        "required": [
          "items",
          "total",
          "limit",
          "offset"
        ],
        "title": "GlobalBatchListResponse",
        "type": "object"
      },
      "GlobalBatchResponse": {
        "properties": {
          "cancelled_city_count": {
            "title": "Cancelled City Count",
            "type": "integer"
          },
          "celery_group_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Celery Group Id"
          },
          "completed_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Completed At"
          },
          "completed_city_count": {
            "title": "Completed City Count",
            "type": "integer"
          },
          "created_at": {
            "format": "date-time",
            "title": "Created At",
            "type": "string"
          },
          "error_message": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Error Message"
          },
          "failed_city_count": {
            "title": "Failed City Count",
            "type": "integer"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "progress": {
            "title": "Progress",
            "type": "integer"
          },
          "stage": {
            "title": "Stage",
            "type": "string"
          },
          "started_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Started At"
          },
          "status": {
            "enum": [
              "queued",
              "running",
              "cancelling",
              "cancelled",
              "completed",
              "partial_completed",
              "failed"
            ],
            "title": "Status",
            "type": "string"
          },
          "summary": {
            "anyOf": [
              {
                "additionalProperties": true,
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Summary"
          },
          "total_city_count": {
            "title": "Total City Count",
            "type": "integer"
          },
          "updated_at": {
            "format": "date-time",
            "title": "Updated At",
            "type": "string"
          }
        },
        "required": [
          "id",
          "celery_group_id",
          "status",
          "stage",
          "progress",
          "total_city_count",
          "completed_city_count",
          "failed_city_count",
          "cancelled_city_count",
          "summary",
          "error_message",
          "created_at",
          "updated_at",
          "started_at",
          "completed_at"
        ],
        "title": "GlobalBatchResponse",
        "type": "object"
      },
      "GlobalCityResultResponse": {
        "properties": {
          "annual_average_core_improvement_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Annual Average Core Improvement C"
          },
          "annual_average_skin_improvement_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Annual Average Skin Improvement C"
          },
          "batch_id": {
            "title": "Batch Id",
            "type": "string"
          },
          "beneficial_weighted_days": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Beneficial Weighted Days"
          },
          "celery_task_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Celery Task Id"
          },
          "city_id": {
            "title": "City Id",
            "type": "string"
          },
          "city_name": {
            "title": "City Name",
            "type": "string"
          },
          "climate_adaptation_rate_percent": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Climate Adaptation Rate Percent"
          },
          "completed_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Completed At"
          },
          "completed_month_count": {
            "default": 0,
            "title": "Completed Month Count",
            "type": "integer"
          },
          "core_improvement_p50_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Core Improvement P50 C"
          },
          "core_improvement_p90_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Core Improvement P90 C"
          },
          "core_improvement_p95_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Core Improvement P95 C"
          },
          "country": {
            "title": "Country",
            "type": "string"
          },
          "data_quality": {
            "anyOf": [
              {
                "additionalProperties": true,
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Data Quality"
          },
          "effective_cooling_hours": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Effective Cooling Hours"
          },
          "eligible_sample_count": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Eligible Sample Count"
          },
          "error_message": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Error Message"
          },
          "evaluated_weighted_days": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Evaluated Weighted Days"
          },
          "exposure_coverage_percent": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Exposure Coverage Percent"
          },
          "heatwave_event_count": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Heatwave Event Count"
          },
          "heatwave_events": {
            "anyOf": [
              {
                "items": {
                  "$ref": "#/components/schemas/HeatwaveEvent"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Heatwave Events"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "last_checkpoint_month": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Last Checkpoint Month"
          },
          "last_heartbeat_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Last Heartbeat At"
          },
          "latitude": {
            "title": "Latitude",
            "type": "number"
          },
          "longest_heatwave_days": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Longest Heatwave Days"
          },
          "longitude": {
            "title": "Longitude",
            "type": "number"
          },
          "maximum_skin_improvement_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Maximum Skin Improvement C"
          },
          "metric_definitions": {
            "anyOf": [
              {
                "additionalProperties": true,
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Metric Definitions"
          },
          "monthly_results": {
            "anyOf": [
              {
                "items": {
                  "$ref": "#/components/schemas/MonthlyAdaptationResult"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Monthly Results"
          },
          "progress": {
            "title": "Progress",
            "type": "integer"
          },
          "resumed_from_checkpoint": {
            "default": false,
            "title": "Resumed From Checkpoint",
            "type": "boolean"
          },
          "retry_count": {
            "title": "Retry Count",
            "type": "integer"
          },
          "sampled_day_count": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Sampled Day Count"
          },
          "skin_improvement_p50_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Skin Improvement P50 C"
          },
          "skin_improvement_p90_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Skin Improvement P90 C"
          },
          "skin_improvement_p95_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Skin Improvement P95 C"
          },
          "stage": {
            "title": "Stage",
            "type": "string"
          },
          "started_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Started At"
          },
          "status": {
            "enum": [
              "queued",
              "running",
              "cancelled",
              "completed",
              "failed"
            ],
            "title": "Status",
            "type": "string"
          }
        },
        "required": [
          "id",
          "batch_id",
          "celery_task_id",
          "city_id",
          "city_name",
          "country",
          "latitude",
          "longitude",
          "status",
          "stage",
          "progress",
          "climate_adaptation_rate_percent",
          "exposure_coverage_percent",
          "annual_average_skin_improvement_c",
          "annual_average_core_improvement_c",
          "maximum_skin_improvement_c",
          "effective_cooling_hours",
          "sampled_day_count",
          "eligible_sample_count",
          "evaluated_weighted_days",
          "beneficial_weighted_days",
          "retry_count",
          "monthly_results",
          "error_message",
          "started_at",
          "completed_at"
        ],
        "title": "GlobalCityResultResponse",
        "type": "object"
      },
      "HTTPValidationError": {
        "properties": {
          "detail": {
            "items": {
              "$ref": "#/components/schemas/ValidationError"
            },
            "title": "Detail",
            "type": "array"
          }
        },
        "title": "HTTPValidationError",
        "type": "object"
      },
      "HeatwaveEvent": {
        "properties": {
          "beneficial_day_count": {
            "minimum": 0.0,
            "title": "Beneficial Day Count",
            "type": "integer"
          },
          "duration_days": {
            "minimum": 1.0,
            "title": "Duration Days",
            "type": "integer"
          },
          "end_date_local": {
            "format": "date-time",
            "title": "End Date Local",
            "type": "string"
          },
          "mean_maximum_air_temperature_c": {
            "title": "Mean Maximum Air Temperature C",
            "type": "number"
          },
          "mean_skin_improvement_c": {
            "title": "Mean Skin Improvement C",
            "type": "number"
          },
          "p90_skin_improvement_c": {
            "title": "P90 Skin Improvement C",
            "type": "number"
          },
          "peak_air_temperature_c": {
            "title": "Peak Air Temperature C",
            "type": "number"
          },
          "start_date_local": {
            "format": "date-time",
            "title": "Start Date Local",
            "type": "string"
          }
        },
        "required": [
          "start_date_local",
          "end_date_local",
          "duration_days",
          "mean_maximum_air_temperature_c",
          "peak_air_temperature_c",
          "mean_skin_improvement_c",
          "p90_skin_improvement_c",
          "beneficial_day_count"
        ],
        "title": "HeatwaveEvent",
        "type": "object"
      },
      "MaterialCreate": {
        "properties": {
          "description": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Description"
          },
          "initial_version": {
            "$ref": "#/components/schemas/MaterialVersionCreate"
          },
          "institution": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Institution"
          },
          "name": {
            "maxLength": 200,
            "minLength": 1,
            "title": "Name",
            "type": "string"
          },
          "slug": {
            "maxLength": 200,
            "minLength": 1,
            "pattern": "^[a-z0-9]+(?:-[a-z0-9]+)*$",
            "title": "Slug",
            "type": "string"
          }
        },
        "required": [
          "name",
          "slug",
          "initial_version"
        ],
        "title": "MaterialCreate",
        "type": "object"
      },
      "MaterialInput": {
        "properties": {
          "absorbed_solar_to_body_fraction": {
            "default": 0.35,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Absorbed Solar To Body Fraction",
            "type": "number"
          },
          "clothing_area_factor": {
            "anyOf": [
              {
                "maximum": 2.0,
                "minimum": 1.0,
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Clothing Area Factor"
          },
          "clothing_insulation_clo": {
            "default": 0.5,
            "maximum": 5.0,
            "minimum": 0.0,
            "title": "Clothing Insulation Clo",
            "type": "number"
          },
          "evaporative_resistance_m2pa_w": {
            "anyOf": [
              {
                "maximum": 1000.0,
                "minimum": 0.0,
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Evaporative Resistance M2Pa W"
          },
          "infrared_emissivity": {
            "default": 0.9,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Infrared Emissivity",
            "type": "number"
          },
          "infrared_transmittance": {
            "default": 0.0,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Infrared Transmittance",
            "type": "number"
          },
          "material_version_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Material Version Id"
          },
          "name": {
            "maxLength": 100,
            "minLength": 1,
            "title": "Name",
            "type": "string"
          },
          "parameter_sources": {
            "anyOf": [
              {
                "additionalProperties": {
                  "$ref": "#/components/schemas/ParameterSource"
                },
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Parameter Sources"
          },
          "projected_solar_area_factor": {
            "default": 0.25,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Projected Solar Area Factor",
            "type": "number"
          },
          "solar_reflectance": {
            "default": 0.5,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Solar Reflectance",
            "type": "number"
          },
          "solar_transmittance": {
            "default": 0,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Solar Transmittance",
            "type": "number"
          },
          "source_reference": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Source Reference"
          },
          "source_type": {
            "anyOf": [
              {
                "maxLength": 50,
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Source Type"
          }
        },
        "required": [
          "name"
        ],
        "title": "MaterialInput",
        "type": "object"
      },
      "MaterialListItem": {
        "properties": {
          "created_at": {
            "format": "date-time",
            "title": "Created At",
            "type": "string"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "institution": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Institution"
          },
          "is_archived": {
            "title": "Is Archived",
            "type": "boolean"
          },
          "latest_version_number": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Latest Version Number"
          },
          "name": {
            "title": "Name",
            "type": "string"
          },
          "slug": {
            "title": "Slug",
            "type": "string"
          }
        },
        "required": [
          "id",
          "name",
          "slug",
          "institution",
          "is_archived",
          "latest_version_number",
          "created_at"
        ],
        "title": "MaterialListItem",
        "type": "object"
      },
      "MaterialListResponse": {
        "properties": {
          "items": {
            "items": {
              "$ref": "#/components/schemas/MaterialListItem"
            },
            "title": "Items",
            "type": "array"
          },
          "limit": {
            "title": "Limit",
            "type": "integer"
          },
          "offset": {
            "title": "Offset",
            "type": "integer"
          },
          "total": {
            "title": "Total",
            "type": "integer"
          }
        },
        "required": [
          "items",
          "total",
          "limit",
          "offset"
        ],
        "title": "MaterialListResponse",
        "type": "object"
      },
      "MaterialResponse": {
        "properties": {
          "created_at": {
            "format": "date-time",
            "title": "Created At",
            "type": "string"
          },
          "description": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Description"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "institution": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Institution"
          },
          "is_archived": {
            "title": "Is Archived",
            "type": "boolean"
          },
          "name": {
            "title": "Name",
            "type": "string"
          },
          "slug": {
            "title": "Slug",
            "type": "string"
          },
          "updated_at": {
            "format": "date-time",
            "title": "Updated At",
            "type": "string"
          },
          "versions": {
            "items": {
              "$ref": "#/components/schemas/MaterialVersionResponse"
            },
            "title": "Versions",
            "type": "array"
          }
        },
        "required": [
          "id",
          "name",
          "slug",
          "description",
          "institution",
          "is_archived",
          "created_at",
          "updated_at",
          "versions"
        ],
        "title": "MaterialResponse",
        "type": "object"
      },
      "MaterialUpdate": {
        "properties": {
          "description": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Description"
          },
          "institution": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Institution"
          },
          "is_archived": {
            "anyOf": [
              {
                "type": "boolean"
              },
              {
                "type": "null"
              }
            ],
            "title": "Is Archived"
          },
          "name": {
            "anyOf": [
              {
                "maxLength": 200,
                "minLength": 1,
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Name"
          }
        },
        "title": "MaterialUpdate",
        "type": "object"
      },
      "MaterialVersionCreate": {
        "properties": {
          "absorbed_solar_to_body_fraction": {
            "default": 0.35,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Absorbed Solar To Body Fraction",
            "type": "number"
          },
          "areal_density_g_m2": {
            "anyOf": [
              {
                "minimum": 0.0,
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Areal Density G M2"
          },
          "clothing_area_factor": {
            "anyOf": [
              {
                "maximum": 2.0,
                "minimum": 1.0,
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Clothing Area Factor"
          },
          "clothing_insulation_clo": {
            "default": 0.5,
            "maximum": 5.0,
            "minimum": 0.0,
            "title": "Clothing Insulation Clo",
            "type": "number"
          },
          "evaporative_resistance_m2pa_w": {
            "anyOf": [
              {
                "minimum": 0.0,
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Evaporative Resistance M2Pa W"
          },
          "infrared_emissivity": {
            "default": 0.9,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Infrared Emissivity",
            "type": "number"
          },
          "infrared_transmittance": {
            "default": 0,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Infrared Transmittance",
            "type": "number"
          },
          "mode": {
            "default": "opaque_emitter",
            "enum": [
              "ordinary",
              "opaque_emitter",
              "infrared_transparent",
              "hybrid"
            ],
            "title": "Mode",
            "type": "string"
          },
          "notes": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Notes"
          },
          "parameter_sources": {
            "anyOf": [
              {
                "additionalProperties": {
                  "$ref": "#/components/schemas/ParameterSource"
                },
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Parameter Sources"
          },
          "projected_solar_area_factor": {
            "default": 0.25,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Projected Solar Area Factor",
            "type": "number"
          },
          "solar_reflectance": {
            "default": 0.5,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Solar Reflectance",
            "type": "number"
          },
          "solar_transmittance": {
            "default": 0,
            "maximum": 1.0,
            "minimum": 0.0,
            "title": "Solar Transmittance",
            "type": "number"
          },
          "source_reference": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Source Reference"
          },
          "source_type": {
            "default": "manual",
            "maxLength": 50,
            "title": "Source Type",
            "type": "string"
          },
          "specific_heat_j_kgk": {
            "anyOf": [
              {
                "minimum": 0.0,
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Specific Heat J Kgk"
          }
        },
        "title": "MaterialVersionCreate",
        "type": "object"
      },
      "MaterialVersionResponse": {
        "properties": {
          "absorbed_solar_to_body_fraction": {
            "title": "Absorbed Solar To Body Fraction",
            "type": "number"
          },
          "areal_density_g_m2": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Areal Density G M2"
          },
          "clothing_area_factor": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Clothing Area Factor"
          },
          "clothing_insulation_clo": {
            "title": "Clothing Insulation Clo",
            "type": "number"
          },
          "created_at": {
            "format": "date-time",
            "title": "Created At",
            "type": "string"
          },
          "evaporative_resistance_m2pa_w": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Evaporative Resistance M2Pa W"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "infrared_emissivity": {
            "title": "Infrared Emissivity",
            "type": "number"
          },
          "infrared_transmittance": {
            "title": "Infrared Transmittance",
            "type": "number"
          },
          "material_id": {
            "title": "Material Id",
            "type": "string"
          },
          "mode": {
            "title": "Mode",
            "type": "string"
          },
          "notes": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Notes"
          },
          "parameter_sources": {
            "anyOf": [
              {
                "additionalProperties": {
                  "$ref": "#/components/schemas/ParameterSource"
                },
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Parameter Sources"
          },
          "projected_solar_area_factor": {
            "title": "Projected Solar Area Factor",
            "type": "number"
          },
          "solar_reflectance": {
            "title": "Solar Reflectance",
            "type": "number"
          },
          "solar_transmittance": {
            "title": "Solar Transmittance",
            "type": "number"
          },
          "source_reference": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Source Reference"
          },
          "source_type": {
            "title": "Source Type",
            "type": "string"
          },
          "specific_heat_j_kgk": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Specific Heat J Kgk"
          },
          "spectra": {
            "default": [],
            "items": {
              "$ref": "#/components/schemas/SpectrumSummary"
            },
            "title": "Spectra",
            "type": "array"
          },
          "version_number": {
            "title": "Version Number",
            "type": "integer"
          }
        },
        "required": [
          "id",
          "material_id",
          "version_number",
          "mode",
          "clothing_insulation_clo",
          "evaporative_resistance_m2pa_w",
          "solar_reflectance",
          "solar_transmittance",
          "infrared_emissivity",
          "infrared_transmittance",
          "projected_solar_area_factor",
          "absorbed_solar_to_body_fraction",
          "areal_density_g_m2",
          "specific_heat_j_kgk",
          "source_type",
          "source_reference",
          "notes",
          "created_at"
        ],
        "title": "MaterialVersionResponse",
        "type": "object"
      },
      "ModelMetadata": {
        "description": "Written into every simulation response for traceability.",
        "properties": {
          "parameter_set_sha256": {
            "title": "Parameter Set Sha256",
            "type": "string"
          },
          "parameter_set_version": {
            "title": "Parameter Set Version",
            "type": "string"
          }
        },
        "required": [
          "parameter_set_version",
          "parameter_set_sha256"
        ],
        "title": "ModelMetadata",
        "type": "object"
      },
      "ModelParameter": {
        "description": "A physical constant used by the thermal model.",
        "properties": {
          "description": {
            "title": "Description",
            "type": "string"
          },
          "name": {
            "title": "Name",
            "type": "string"
          },
          "note": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Note"
          },
          "reference": {
            "title": "Reference",
            "type": "string"
          },
          "source_type": {
            "enum": [
              "measured",
              "manufacturer",
              "literature",
              "standard",
              "derived",
              "assumed",
              "manual"
            ],
            "title": "Source Type",
            "type": "string"
          },
          "unit": {
            "title": "Unit",
            "type": "string"
          },
          "value": {
            "title": "Value",
            "type": "number"
          }
        },
        "required": [
          "name",
          "value",
          "unit",
          "description",
          "source_type",
          "reference"
        ],
        "title": "ModelParameter",
        "type": "object"
      },
      "ModelParameterManifest": {
        "properties": {
          "parameter_set_sha256": {
            "title": "Parameter Set Sha256",
            "type": "string"
          },
          "parameter_set_version": {
            "title": "Parameter Set Version",
            "type": "string"
          },
          "parameters": {
            "items": {
              "$ref": "#/components/schemas/ModelParameter"
            },
            "title": "Parameters",
            "type": "array"
          }
        },
        "required": [
          "parameter_set_version",
          "parameter_set_sha256",
          "parameters"
        ],
        "title": "ModelParameterManifest",
        "type": "object"
      },
      "MonthlyAdaptationResult": {
        "properties": {
          "average_core_improvement_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Average Core Improvement C"
          },
          "average_skin_improvement_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Average Skin Improvement C"
          },
          "beneficial": {
            "anyOf": [
              {
                "type": "boolean"
              },
              {
                "type": "null"
              }
            ],
            "title": "Beneficial"
          },
          "beneficial_weighted_days": {
            "default": 0,
            "title": "Beneficial Weighted Days",
            "type": "integer"
          },
          "climate_adaptation_rate_percent": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Climate Adaptation Rate Percent"
          },
          "eligible_sample_count": {
            "default": 0,
            "title": "Eligible Sample Count",
            "type": "integer"
          },
          "evaluated_weighted_days": {
            "default": 0,
            "title": "Evaluated Weighted Days",
            "type": "integer"
          },
          "exposure_coverage_percent": {
            "default": 0.0,
            "title": "Exposure Coverage Percent",
            "type": "number"
          },
          "final_skin_improvement_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Final Skin Improvement C"
          },
          "maximum_skin_improvement_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Maximum Skin Improvement C"
          },
          "month": {
            "maximum": 12.0,
            "minimum": 1.0,
            "title": "Month",
            "type": "integer"
          },
          "representative_date_local": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Representative Date Local"
          },
          "sampled_day_count": {
            "default": 1,
            "title": "Sampled Day Count",
            "type": "integer"
          },
          "samples": {
            "items": {
              "$ref": "#/components/schemas/DailyAdaptationResult"
            },
            "title": "Samples",
            "type": "array"
          },
          "skipped_samples": {
            "items": {
              "$ref": "#/components/schemas/SkippedSample"
            },
            "title": "Skipped Samples",
            "type": "array"
          },
          "skipped_weighted_days": {
            "default": 0,
            "title": "Skipped Weighted Days",
            "type": "integer"
          },
          "total_weighted_days": {
            "default": 0,
            "title": "Total Weighted Days",
            "type": "integer"
          },
          "weight_days": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Weight Days"
          }
        },
        "required": [
          "month"
        ],
        "title": "MonthlyAdaptationResult",
        "type": "object"
      },
      "ParameterSource": {
        "additionalProperties": false,
        "description": "Provenance of one numeric input.",
        "properties": {
          "note": {
            "anyOf": [
              {
                "maxLength": 1000,
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Note"
          },
          "reference": {
            "anyOf": [
              {
                "maxLength": 500,
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Reference"
          },
          "source_type": {
            "default": "assumed",
            "enum": [
              "measured",
              "manufacturer",
              "literature",
              "standard",
              "derived",
              "assumed",
              "manual"
            ],
            "title": "Source Type",
            "type": "string"
          }
        },
        "title": "ParameterSource",
        "type": "object"
      },
      "PersonInput": {
        "properties": {
          "body_mass_kg": {
            "default": 70.0,
            "maximum": 200.0,
            "minimum": 30.0,
            "title": "Body Mass Kg",
            "type": "number"
          },
          "body_surface_area_m2": {
            "default": 1.8,
            "maximum": 3.0,
            "minimum": 1.0,
            "title": "Body Surface Area M2",
            "type": "number"
          },
          "initial_core_temperature_c": {
            "default": 36.8,
            "maximum": 40.0,
            "minimum": 34.0,
            "title": "Initial Core Temperature C",
            "type": "number"
          },
          "initial_skin_temperature_c": {
            "default": 33.7,
            "maximum": 40.0,
            "minimum": 20.0,
            "title": "Initial Skin Temperature C",
            "type": "number"
          },
          "met": {
            "default": 2.6,
            "maximum": 10.0,
            "minimum": 0.7,
            "title": "Met",
            "type": "number"
          }
        },
        "title": "PersonInput",
        "type": "object"
      },
      "PrototypeBenchmarkOutput": {
        "properties": {
          "core_temperature_c": {
            "title": "Core Temperature C",
            "type": "number"
          },
          "energy_residual_percent": {
            "title": "Energy Residual Percent",
            "type": "number"
          },
          "evaporation_w_m2": {
            "title": "Evaporation W M2",
            "type": "number"
          },
          "skin_blood_flow_kg_h_m2": {
            "title": "Skin Blood Flow Kg H M2",
            "type": "number"
          },
          "skin_temperature_c": {
            "title": "Skin Temperature C",
            "type": "number"
          },
          "skin_wettedness": {
            "title": "Skin Wettedness",
            "type": "number"
          }
        },
        "required": [
          "core_temperature_c",
          "skin_temperature_c",
          "evaporation_w_m2",
          "skin_wettedness",
          "skin_blood_flow_kg_h_m2",
          "energy_residual_percent"
        ],
        "title": "PrototypeBenchmarkOutput",
        "type": "object"
      },
      "ReferencePortParity": {
        "description": "Port vs. library after 60 minutes (the only duration the library runs).",
        "properties": {
          "library_core_temperature_c": {
            "title": "Library Core Temperature C",
            "type": "number"
          },
          "library_skin_temperature_c": {
            "title": "Library Skin Temperature C",
            "type": "number"
          },
          "maximum_absolute_difference_c": {
            "title": "Maximum Absolute Difference C",
            "type": "number"
          },
          "port_core_temperature_c": {
            "title": "Port Core Temperature C",
            "type": "number"
          },
          "port_skin_temperature_c": {
            "title": "Port Skin Temperature C",
            "type": "number"
          }
        },
        "required": [
          "library_core_temperature_c",
          "port_core_temperature_c",
          "library_skin_temperature_c",
          "port_skin_temperature_c",
          "maximum_absolute_difference_c"
        ],
        "title": "ReferencePortParity",
        "type": "object"
      },
      "ScenarioResult": {
        "properties": {
          "assumptions_applied": {
            "items": {
              "type": "string"
            },
            "title": "Assumptions Applied",
            "type": "array"
          },
          "body": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/BodyThermalSummary"
              },
              {
                "type": "null"
              }
            ]
          },
          "clothing": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ClothingSummary"
              },
              {
                "type": "null"
              }
            ]
          },
          "diagnostics": {
            "$ref": "#/components/schemas/EnergyDiagnostics"
          },
          "final_core_temperature_c": {
            "title": "Final Core Temperature C",
            "type": "number"
          },
          "final_skin_temperature_c": {
            "title": "Final Skin Temperature C",
            "type": "number"
          },
          "material_name": {
            "title": "Material Name",
            "type": "string"
          },
          "peak_core_temperature_c": {
            "title": "Peak Core Temperature C",
            "type": "number"
          },
          "peak_skin_temperature_c": {
            "title": "Peak Skin Temperature C",
            "type": "number"
          },
          "time_series": {
            "items": {
              "$ref": "#/components/schemas/TimeSeriesPoint"
            },
            "title": "Time Series",
            "type": "array"
          }
        },
        "required": [
          "material_name",
          "time_series",
          "final_core_temperature_c",
          "final_skin_temperature_c",
          "peak_core_temperature_c",
          "peak_skin_temperature_c",
          "diagnostics"
        ],
        "title": "ScenarioResult",
        "type": "object"
      },
      "SimulationJobDetail": {
        "properties": {
          "celery_task_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Celery Task Id"
          },
          "city_id": {
            "title": "City Id",
            "type": "string"
          },
          "completed_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Completed At"
          },
          "created_at": {
            "format": "date-time",
            "title": "Created At",
            "type": "string"
          },
          "error_message": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Error Message"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "progress": {
            "title": "Progress",
            "type": "integer"
          },
          "request": {
            "$ref": "#/components/schemas/WeatherSimulationRequest"
          },
          "stage": {
            "title": "Stage",
            "type": "string"
          },
          "started_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Started At"
          },
          "status": {
            "enum": [
              "queued",
              "running",
              "cancelling",
              "cancelled",
              "completed",
              "failed"
            ],
            "title": "Status",
            "type": "string"
          },
          "summary": {
            "anyOf": [
              {
                "additionalProperties": true,
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Summary"
          },
          "updated_at": {
            "format": "date-time",
            "title": "Updated At",
            "type": "string"
          }
        },
        "required": [
          "id",
          "celery_task_id",
          "status",
          "stage",
          "progress",
          "city_id",
          "summary",
          "error_message",
          "created_at",
          "updated_at",
          "started_at",
          "completed_at",
          "request"
        ],
        "title": "SimulationJobDetail",
        "type": "object"
      },
      "SimulationJobListResponse": {
        "properties": {
          "items": {
            "items": {
              "$ref": "#/components/schemas/SimulationJobResponse"
            },
            "title": "Items",
            "type": "array"
          },
          "limit": {
            "title": "Limit",
            "type": "integer"
          },
          "offset": {
            "title": "Offset",
            "type": "integer"
          },
          "total": {
            "title": "Total",
            "type": "integer"
          }
        },
        "required": [
          "items",
          "total",
          "limit",
          "offset"
        ],
        "title": "SimulationJobListResponse",
        "type": "object"
      },
      "SimulationJobResponse": {
        "properties": {
          "celery_task_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Celery Task Id"
          },
          "city_id": {
            "title": "City Id",
            "type": "string"
          },
          "completed_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Completed At"
          },
          "created_at": {
            "format": "date-time",
            "title": "Created At",
            "type": "string"
          },
          "error_message": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Error Message"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "progress": {
            "title": "Progress",
            "type": "integer"
          },
          "stage": {
            "title": "Stage",
            "type": "string"
          },
          "started_at": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Started At"
          },
          "status": {
            "enum": [
              "queued",
              "running",
              "cancelling",
              "cancelled",
              "completed",
              "failed"
            ],
            "title": "Status",
            "type": "string"
          },
          "summary": {
            "anyOf": [
              {
                "additionalProperties": true,
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Summary"
          },
          "updated_at": {
            "format": "date-time",
            "title": "Updated At",
            "type": "string"
          }
        },
        "required": [
          "id",
          "celery_task_id",
          "status",
          "stage",
          "progress",
          "city_id",
          "summary",
          "error_message",
          "created_at",
          "updated_at",
          "started_at",
          "completed_at"
        ],
        "title": "SimulationJobResponse",
        "type": "object"
      },
      "SimulationRequest": {
        "properties": {
          "city": {
            "default": "Dubai",
            "minLength": 1,
            "title": "City",
            "type": "string"
          },
          "control_material": {
            "$ref": "#/components/schemas/MaterialInput"
          },
          "duration_minutes": {
            "default": 120,
            "maximum": 1440.0,
            "minimum": 1.0,
            "title": "Duration Minutes",
            "type": "integer"
          },
          "environment": {
            "$ref": "#/components/schemas/EnvironmentInput"
          },
          "output_interval_minutes": {
            "default": 1,
            "maximum": 60.0,
            "minimum": 1.0,
            "title": "Output Interval Minutes",
            "type": "integer"
          },
          "person": {
            "$ref": "#/components/schemas/PersonInput"
          },
          "rc_material": {
            "$ref": "#/components/schemas/MaterialInput"
          }
        },
        "required": [
          "environment",
          "person",
          "control_material",
          "rc_material"
        ],
        "title": "SimulationRequest",
        "type": "object"
      },
      "SimulationResponse": {
        "properties": {
          "city": {
            "title": "City",
            "type": "string"
          },
          "control": {
            "$ref": "#/components/schemas/ScenarioResult"
          },
          "duration_minutes": {
            "title": "Duration Minutes",
            "type": "integer"
          },
          "model_metadata": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ModelMetadata"
              },
              {
                "type": "null"
              }
            ]
          },
          "model_name": {
            "title": "Model Name",
            "type": "string"
          },
          "model_version": {
            "title": "Model Version",
            "type": "string"
          },
          "radiative_cooling": {
            "$ref": "#/components/schemas/ScenarioResult"
          },
          "summary": {
            "$ref": "#/components/schemas/SimulationSummary"
          },
          "warning": {
            "title": "Warning",
            "type": "string"
          }
        },
        "required": [
          "model_name",
          "model_version",
          "city",
          "duration_minutes",
          "control",
          "radiative_cooling",
          "summary",
          "warning"
        ],
        "title": "SimulationResponse",
        "type": "object"
      },
      "SimulationSummary": {
        "properties": {
          "average_skin_temperature_improvement_c": {
            "title": "Average Skin Temperature Improvement C",
            "type": "number"
          },
          "final_core_temperature_improvement_c": {
            "title": "Final Core Temperature Improvement C",
            "type": "number"
          },
          "final_skin_temperature_improvement_c": {
            "title": "Final Skin Temperature Improvement C",
            "type": "number"
          }
        },
        "required": [
          "final_skin_temperature_improvement_c",
          "final_core_temperature_improvement_c",
          "average_skin_temperature_improvement_c"
        ],
        "title": "SimulationSummary",
        "type": "object"
      },
      "SkippedSample": {
        "description": "A planned sample day that could not be simulated for data reasons.",
        "properties": {
          "message": {
            "title": "Message",
            "type": "string"
          },
          "reason_code": {
            "title": "Reason Code",
            "type": "string"
          },
          "sample_date_local": {
            "format": "date-time",
            "title": "Sample Date Local",
            "type": "string"
          },
          "weight_days": {
            "minimum": 1.0,
            "title": "Weight Days",
            "type": "integer"
          }
        },
        "required": [
          "sample_date_local",
          "weight_days",
          "reason_code",
          "message"
        ],
        "title": "SkippedSample",
        "type": "object"
      },
      "SpectrumPoint": {
        "properties": {
          "value": {
            "title": "Value",
            "type": "number"
          },
          "wavelength_um": {
            "title": "Wavelength Um",
            "type": "number"
          }
        },
        "required": [
          "wavelength_um",
          "value"
        ],
        "title": "SpectrumPoint",
        "type": "object"
      },
      "SpectrumResponse": {
        "properties": {
          "points": {
            "items": {
              "$ref": "#/components/schemas/SpectrumPoint"
            },
            "title": "Points",
            "type": "array"
          },
          "summary": {
            "$ref": "#/components/schemas/SpectrumSummary"
          }
        },
        "required": [
          "summary",
          "points"
        ],
        "title": "SpectrumResponse",
        "type": "object"
      },
      "SpectrumSummary": {
        "properties": {
          "created_at": {
            "format": "date-time",
            "title": "Created At",
            "type": "string"
          },
          "file_checksum_sha256": {
            "title": "File Checksum Sha256",
            "type": "string"
          },
          "id": {
            "title": "Id",
            "type": "string"
          },
          "maximum_wavelength_um": {
            "title": "Maximum Wavelength Um",
            "type": "number"
          },
          "minimum_wavelength_um": {
            "title": "Minimum Wavelength Um",
            "type": "number"
          },
          "original_filename": {
            "title": "Original Filename",
            "type": "string"
          },
          "point_count": {
            "title": "Point Count",
            "type": "integer"
          },
          "spectrum_type": {
            "title": "Spectrum Type",
            "type": "string"
          },
          "wavelength_unit": {
            "title": "Wavelength Unit",
            "type": "string"
          }
        },
        "required": [
          "id",
          "spectrum_type",
          "wavelength_unit",
          "point_count",
          "minimum_wavelength_um",
          "maximum_wavelength_um",
          "original_filename",
          "file_checksum_sha256",
          "created_at"
        ],
        "title": "SpectrumSummary",
        "type": "object"
      },
      "TimeSeriesPoint": {
        "properties": {
          "absorbed_solar_w_m2": {
            "title": "Absorbed Solar W M2",
            "type": "number"
          },
          "clothing_surface_temperature_c": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Clothing Surface Temperature C"
          },
          "convection_w_m2": {
            "title": "Convection W M2",
            "type": "number"
          },
          "core_temperature_c": {
            "title": "Core Temperature C",
            "type": "number"
          },
          "core_to_skin_w_m2": {
            "title": "Core To Skin W M2",
            "type": "number"
          },
          "evaporation_w_m2": {
            "title": "Evaporation W M2",
            "type": "number"
          },
          "longwave_radiation_w_m2": {
            "title": "Longwave Radiation W M2",
            "type": "number"
          },
          "maximum_evaporation_w_m2": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Maximum Evaporation W M2"
          },
          "minute": {
            "title": "Minute",
            "type": "number"
          },
          "skin_blood_flow_kg_h_m2": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Skin Blood Flow Kg H M2"
          },
          "skin_temperature_c": {
            "title": "Skin Temperature C",
            "type": "number"
          },
          "skin_wettedness": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Skin Wettedness"
          }
        },
        "required": [
          "minute",
          "core_temperature_c",
          "skin_temperature_c",
          "convection_w_m2",
          "longwave_radiation_w_m2",
          "evaporation_w_m2",
          "absorbed_solar_w_m2",
          "core_to_skin_w_m2"
        ],
        "title": "TimeSeriesPoint",
        "type": "object"
      },
      "ValidationError": {
        "properties": {
          "ctx": {
            "title": "Context",
            "type": "object"
          },
          "input": {
            "title": "Input"
          },
          "loc": {
            "items": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "integer"
                }
              ]
            },
            "title": "Location",
            "type": "array"
          },
          "msg": {
            "title": "Message",
            "type": "string"
          },
          "type": {
            "title": "Error Type",
            "type": "string"
          }
        },
        "required": [
          "loc",
          "msg",
          "type"
        ],
        "title": "ValidationError",
        "type": "object"
      },
      "WeatherGap": {
        "description": "A break in the hourly timeline between two consecutive points.",
        "properties": {
          "end": {
            "format": "date-time",
            "title": "End",
            "type": "string"
          },
          "missing_steps": {
            "minimum": 1.0,
            "title": "Missing Steps",
            "type": "integer"
          },
          "start": {
            "format": "date-time",
            "title": "Start",
            "type": "string"
          }
        },
        "required": [
          "start",
          "end",
          "missing_steps"
        ],
        "title": "WeatherGap",
        "type": "object"
      },
      "WeatherPoint": {
        "properties": {
          "air_temperature_c": {
            "title": "Air Temperature C",
            "type": "number"
          },
          "diffuse_radiation_w_m2": {
            "title": "Diffuse Radiation W M2",
            "type": "number"
          },
          "direct_radiation_w_m2": {
            "title": "Direct Radiation W M2",
            "type": "number"
          },
          "dni_w_m2": {
            "title": "Dni W M2",
            "type": "number"
          },
          "ghi_w_m2": {
            "title": "Ghi W M2",
            "type": "number"
          },
          "relative_humidity_percent": {
            "title": "Relative Humidity Percent",
            "type": "number"
          },
          "timestamp": {
            "format": "date-time",
            "title": "Timestamp",
            "type": "string"
          },
          "wind_speed_m_s": {
            "title": "Wind Speed M S",
            "type": "number"
          }
        },
        "required": [
          "timestamp",
          "air_temperature_c",
          "relative_humidity_percent",
          "wind_speed_m_s",
          "ghi_w_m2",
          "direct_radiation_w_m2",
          "diffuse_radiation_w_m2",
          "dni_w_m2"
        ],
        "title": "WeatherPoint",
        "type": "object"
      },
      "WeatherQualityReport": {
        "description": "Result of normalising a raw weather timeline (Stage 1, PR-1).",
        "properties": {
          "duplicates_removed": {
            "default": 0,
            "title": "Duplicates Removed",
            "type": "integer"
          },
          "expected_step_seconds": {
            "exclusiveMinimum": 0.0,
            "title": "Expected Step Seconds",
            "type": "integer"
          },
          "first_timestamp": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "First Timestamp"
          },
          "gaps": {
            "items": {
              "$ref": "#/components/schemas/WeatherGap"
            },
            "title": "Gaps",
            "type": "array"
          },
          "last_timestamp": {
            "anyOf": [
              {
                "format": "date-time",
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Last Timestamp"
          },
          "notes": {
            "items": {
              "type": "string"
            },
            "title": "Notes",
            "type": "array"
          },
          "point_count": {
            "minimum": 0.0,
            "title": "Point Count",
            "type": "integer"
          },
          "was_sorted": {
            "default": true,
            "title": "Was Sorted",
            "type": "boolean"
          }
        },
        "required": [
          "expected_step_seconds",
          "point_count"
        ],
        "title": "WeatherQualityReport",
        "type": "object"
      },
      "WeatherSimulationRequest": {
        "properties": {
          "city_id": {
            "default": "dubai",
            "minLength": 1,
            "title": "City Id",
            "type": "string"
          },
          "control_material": {
            "$ref": "#/components/schemas/MaterialInput"
          },
          "duration_minutes": {
            "default": 120,
            "maximum": 1440.0,
            "minimum": 1.0,
            "title": "Duration Minutes",
            "type": "integer"
          },
          "environment_assumptions": {
            "$ref": "#/components/schemas/EnvironmentAssumptions"
          },
          "output_interval_minutes": {
            "default": 1,
            "maximum": 60.0,
            "minimum": 1.0,
            "title": "Output Interval Minutes",
            "type": "integer"
          },
          "person": {
            "$ref": "#/components/schemas/PersonInput"
          },
          "rc_material": {
            "$ref": "#/components/schemas/MaterialInput"
          },
          "start_time_local": {
            "format": "date-time",
            "title": "Start Time Local",
            "type": "string"
          }
        },
        "required": [
          "start_time_local",
          "person",
          "control_material",
          "rc_material"
        ],
        "title": "WeatherSimulationRequest",
        "type": "object"
      },
      "WeatherSimulationResponse": {
        "properties": {
          "city": {
            "title": "City",
            "type": "string"
          },
          "control": {
            "$ref": "#/components/schemas/ScenarioResult"
          },
          "duration_minutes": {
            "title": "Duration Minutes",
            "type": "integer"
          },
          "environment_assumptions": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/EnvironmentAssumptions"
              },
              {
                "type": "null"
              }
            ]
          },
          "environment_model_note": {
            "title": "Environment Model Note",
            "type": "string"
          },
          "model_metadata": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ModelMetadata"
              },
              {
                "type": "null"
              }
            ]
          },
          "model_name": {
            "title": "Model Name",
            "type": "string"
          },
          "model_version": {
            "title": "Model Version",
            "type": "string"
          },
          "radiative_cooling": {
            "$ref": "#/components/schemas/ScenarioResult"
          },
          "summary": {
            "$ref": "#/components/schemas/SimulationSummary"
          },
          "warning": {
            "title": "Warning",
            "type": "string"
          },
          "weather": {
            "$ref": "#/components/schemas/WeatherTimeSeries"
          }
        },
        "required": [
          "model_name",
          "model_version",
          "city",
          "duration_minutes",
          "control",
          "radiative_cooling",
          "summary",
          "warning",
          "weather",
          "environment_model_note"
        ],
        "title": "WeatherSimulationResponse",
        "type": "object"
      },
      "WeatherSourceMetadata": {
        "properties": {
          "attribution": {
            "title": "Attribution",
            "type": "string"
          },
          "dataset": {
            "title": "Dataset",
            "type": "string"
          },
          "downloaded_at": {
            "format": "date-time",
            "title": "Downloaded At",
            "type": "string"
          },
          "elevation_m": {
            "title": "Elevation M",
            "type": "number"
          },
          "from_cache": {
            "title": "From Cache",
            "type": "boolean"
          },
          "latitude": {
            "title": "Latitude",
            "type": "number"
          },
          "longitude": {
            "title": "Longitude",
            "type": "number"
          },
          "model": {
            "title": "Model",
            "type": "string"
          },
          "payload_sha256": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Payload Sha256"
          },
          "provider": {
            "title": "Provider",
            "type": "string"
          },
          "quality": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/WeatherQualityReport"
              },
              {
                "type": "null"
              }
            ]
          },
          "timezone": {
            "title": "Timezone",
            "type": "string"
          }
        },
        "required": [
          "provider",
          "dataset",
          "model",
          "latitude",
          "longitude",
          "elevation_m",
          "timezone",
          "downloaded_at",
          "from_cache",
          "attribution"
        ],
        "title": "WeatherSourceMetadata",
        "type": "object"
      },
      "WeatherTimeSeries": {
        "properties": {
          "city": {
            "$ref": "#/components/schemas/CityResponse"
          },
          "points": {
            "items": {
              "$ref": "#/components/schemas/WeatherPoint"
            },
            "title": "Points",
            "type": "array"
          },
          "requested_end_time": {
            "format": "date-time",
            "title": "Requested End Time",
            "type": "string"
          },
          "requested_start_time": {
            "format": "date-time",
            "title": "Requested Start Time",
            "type": "string"
          },
          "source": {
            "$ref": "#/components/schemas/WeatherSourceMetadata"
          }
        },
        "required": [
          "city",
          "requested_start_time",
          "requested_end_time",
          "points",
          "source"
        ],
        "title": "WeatherTimeSeries",
        "type": "object"
      }
    }
  },
  "info": {
    "description": "Backend API for simulating and evaluating radiative cooling clothing under global climate conditions.",
    "title": "Global Radiative Cooling Clothing Climate Adaptation API",
    "version": "0.2.0"
  },
  "openapi": "3.1.0",
  "paths": {
    "/api/v1/benchmarks/gagge": {
      "post": {
        "operationId": "compare_with_gagge_api_v1_benchmarks_gagge_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/GaggeBenchmarkRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GaggeBenchmarkResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Compare With Gagge",
        "tags": [
          "benchmarks"
        ]
      }
    },
    "/api/v1/global-batches": {
      "get": {
        "operationId": "list_global_batches_api_v1_global_batches_get",
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "required": false,
            "schema": {
              "default": 20,
              "maximum": 100,
              "minimum": 1,
              "title": "Limit",
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "offset",
            "required": false,
            "schema": {
              "default": 0,
              "minimum": 0,
              "title": "Offset",
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GlobalBatchListResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "List Global Batches",
        "tags": [
          "global-batches"
        ]
      },
      "post": {
        "operationId": "create_global_batch_api_v1_global_batches_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/GlobalBatchCreate"
              }
            }
          },
          "required": true
        },
        "responses": {
          "202": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GlobalBatchResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Create Global Batch",
        "tags": [
          "global-batches"
        ]
      }
    },
    "/api/v1/global-batches/cities": {
      "get": {
        "operationId": "get_supported_cities_api_v1_global_batches_cities_get",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "additionalProperties": true,
                  "title": "Response Get Supported Cities Api V1 Global Batches Cities Get",
                  "type": "object"
                }
              }
            },
            "description": "Successful Response"
          }
        },
        "summary": "Get Supported Cities",
        "tags": [
          "global-batches"
        ]
      }
    },
    "/api/v1/global-batches/estimate": {
      "post": {
        "operationId": "estimate_global_batch_api_v1_global_batches_estimate_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/GlobalBatchCreate"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GlobalBatchEstimateResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Estimate Global Batch",
        "tags": [
          "global-batches"
        ]
      }
    },
    "/api/v1/global-batches/{batch_id}": {
      "get": {
        "operationId": "get_global_batch_api_v1_global_batches__batch_id__get",
        "parameters": [
          {
            "in": "path",
            "name": "batch_id",
            "required": true,
            "schema": {
              "title": "Batch Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GlobalBatchDetail"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Get Global Batch",
        "tags": [
          "global-batches"
        ]
      }
    },
    "/api/v1/global-batches/{batch_id}/cancel": {
      "post": {
        "operationId": "cancel_global_batch_api_v1_global_batches__batch_id__cancel_post",
        "parameters": [
          {
            "in": "path",
            "name": "batch_id",
            "required": true,
            "schema": {
              "title": "Batch Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GlobalBatchResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Cancel Global Batch",
        "tags": [
          "global-batches"
        ]
      }
    },
    "/api/v1/global-batches/{batch_id}/export": {
      "get": {
        "operationId": "export_global_batch_api_v1_global_batches__batch_id__export_get",
        "parameters": [
          {
            "in": "path",
            "name": "batch_id",
            "required": true,
            "schema": {
              "title": "Batch Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {}
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Export Global Batch",
        "tags": [
          "global-batches"
        ]
      }
    },
    "/api/v1/global-batches/{batch_id}/geojson": {
      "get": {
        "operationId": "get_global_batch_geojson_api_v1_global_batches__batch_id__geojson_get",
        "parameters": [
          {
            "in": "path",
            "name": "batch_id",
            "required": true,
            "schema": {
              "title": "Batch Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "additionalProperties": true,
                  "title": "Response Get Global Batch Geojson Api V1 Global Batches  Batch Id  Geojson Get",
                  "type": "object"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Get Global Batch Geojson",
        "tags": [
          "global-batches"
        ]
      }
    },
    "/api/v1/global-batches/{batch_id}/retry-failed": {
      "post": {
        "operationId": "retry_failed_cities_api_v1_global_batches__batch_id__retry_failed_post",
        "parameters": [
          {
            "in": "path",
            "name": "batch_id",
            "required": true,
            "schema": {
              "title": "Batch Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "202": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GlobalBatchResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Retry Failed Cities",
        "tags": [
          "global-batches"
        ]
      }
    },
    "/api/v1/health": {
      "get": {
        "operationId": "health_check_api_v1_health_get",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {}
              }
            },
            "description": "Successful Response"
          }
        },
        "summary": "Health Check"
      }
    },
    "/api/v1/materials": {
      "get": {
        "operationId": "list_materials_api_v1_materials_get",
        "parameters": [
          {
            "in": "query",
            "name": "include_archived",
            "required": false,
            "schema": {
              "default": false,
              "title": "Include Archived",
              "type": "boolean"
            }
          },
          {
            "in": "query",
            "name": "search",
            "required": false,
            "schema": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ],
              "title": "Search"
            }
          },
          {
            "in": "query",
            "name": "limit",
            "required": false,
            "schema": {
              "default": 20,
              "maximum": 100,
              "minimum": 1,
              "title": "Limit",
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "offset",
            "required": false,
            "schema": {
              "default": 0,
              "minimum": 0,
              "title": "Offset",
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MaterialListResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "List Materials",
        "tags": [
          "materials"
        ]
      },
      "post": {
        "operationId": "create_material_api_v1_materials_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MaterialCreate"
              }
            }
          },
          "required": true
        },
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MaterialResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Create Material",
        "tags": [
          "materials"
        ]
      }
    },
    "/api/v1/materials/versions/{version_id}/simulation-input": {
      "get": {
        "operationId": "material_version_to_simulation_input_api_v1_materials_versions__version_id__simulation_input_get",
        "parameters": [
          {
            "in": "path",
            "name": "version_id",
            "required": true,
            "schema": {
              "title": "Version Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MaterialInput"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Material Version To Simulation Input",
        "tags": [
          "materials"
        ]
      }
    },
    "/api/v1/materials/versions/{version_id}/spectra": {
      "post": {
        "operationId": "upload_material_spectrum_api_v1_materials_versions__version_id__spectra_post",
        "parameters": [
          {
            "in": "path",
            "name": "version_id",
            "required": true,
            "schema": {
              "title": "Version Id",
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Body_upload_material_spectrum_api_v1_materials_versions__version_id__spectra_post"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SpectrumResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Upload Material Spectrum",
        "tags": [
          "materials"
        ]
      }
    },
    "/api/v1/materials/versions/{version_id}/spectra/{spectrum_type}": {
      "get": {
        "operationId": "get_material_spectrum_api_v1_materials_versions__version_id__spectra__spectrum_type__get",
        "parameters": [
          {
            "in": "path",
            "name": "version_id",
            "required": true,
            "schema": {
              "title": "Version Id",
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "spectrum_type",
            "required": true,
            "schema": {
              "title": "Spectrum Type",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SpectrumResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Get Material Spectrum",
        "tags": [
          "materials"
        ]
      }
    },
    "/api/v1/materials/{material_id}": {
      "get": {
        "operationId": "get_material_api_v1_materials__material_id__get",
        "parameters": [
          {
            "in": "path",
            "name": "material_id",
            "required": true,
            "schema": {
              "title": "Material Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MaterialResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Get Material",
        "tags": [
          "materials"
        ]
      },
      "patch": {
        "operationId": "update_material_api_v1_materials__material_id__patch",
        "parameters": [
          {
            "in": "path",
            "name": "material_id",
            "required": true,
            "schema": {
              "title": "Material Id",
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MaterialUpdate"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MaterialResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Update Material",
        "tags": [
          "materials"
        ]
      }
    },
    "/api/v1/materials/{material_id}/versions": {
      "post": {
        "operationId": "create_material_version_api_v1_materials__material_id__versions_post",
        "parameters": [
          {
            "in": "path",
            "name": "material_id",
            "required": true,
            "schema": {
              "title": "Material Id",
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MaterialVersionCreate"
              }
            }
          },
          "required": true
        },
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MaterialVersionResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Create Material Version",
        "tags": [
          "materials"
        ]
      }
    },
    "/api/v1/model/environment-assumptions/defaults": {
      "get": {
        "operationId": "get_default_environment_assumptions_api_v1_model_environment_assumptions_defaults_get",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/EnvironmentAssumptions"
                }
              }
            },
            "description": "Successful Response"
          }
        },
        "summary": "Get Default Environment Assumptions",
        "tags": [
          "model"
        ]
      }
    },
    "/api/v1/model/parameters": {
      "get": {
        "operationId": "get_model_parameters_api_v1_model_parameters_get",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ModelParameterManifest"
                }
              }
            },
            "description": "Successful Response"
          }
        },
        "summary": "Get Model Parameters",
        "tags": [
          "model"
        ]
      }
    },
    "/api/v1/simulations/jobs": {
      "get": {
        "operationId": "list_simulation_jobs_api_v1_simulations_jobs_get",
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "required": false,
            "schema": {
              "default": 20,
              "maximum": 100,
              "minimum": 1,
              "title": "Limit",
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "offset",
            "required": false,
            "schema": {
              "default": 0,
              "minimum": 0,
              "title": "Offset",
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SimulationJobListResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "List Simulation Jobs",
        "tags": [
          "simulations"
        ]
      },
      "post": {
        "operationId": "create_simulation_job_api_v1_simulations_jobs_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/WeatherSimulationRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "202": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SimulationJobResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Create Simulation Job",
        "tags": [
          "simulations"
        ]
      }
    },
    "/api/v1/simulations/jobs/{job_id}": {
      "get": {
        "operationId": "get_simulation_job_api_v1_simulations_jobs__job_id__get",
        "parameters": [
          {
            "in": "path",
            "name": "job_id",
            "required": true,
            "schema": {
              "title": "Job Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SimulationJobDetail"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Get Simulation Job",
        "tags": [
          "simulations"
        ]
      }
    },
    "/api/v1/simulations/jobs/{job_id}/cancel": {
      "post": {
        "operationId": "cancel_simulation_job_api_v1_simulations_jobs__job_id__cancel_post",
        "parameters": [
          {
            "in": "path",
            "name": "job_id",
            "required": true,
            "schema": {
              "title": "Job Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SimulationJobResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Cancel Simulation Job",
        "tags": [
          "simulations"
        ]
      }
    },
    "/api/v1/simulations/jobs/{job_id}/events": {
      "get": {
        "operationId": "simulation_job_events_api_v1_simulations_jobs__job_id__events_get",
        "parameters": [
          {
            "in": "path",
            "name": "job_id",
            "required": true,
            "schema": {
              "title": "Job Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {}
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Simulation Job Events",
        "tags": [
          "simulations"
        ]
      }
    },
    "/api/v1/simulations/jobs/{job_id}/export": {
      "get": {
        "operationId": "export_simulation_result_api_v1_simulations_jobs__job_id__export_get",
        "parameters": [
          {
            "in": "path",
            "name": "job_id",
            "required": true,
            "schema": {
              "title": "Job Id",
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "format",
            "required": false,
            "schema": {
              "default": "csv",
              "pattern": "^(csv|json)$",
              "title": "Format",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {}
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Export Simulation Result",
        "tags": [
          "simulations"
        ]
      }
    },
    "/api/v1/simulations/jobs/{job_id}/result": {
      "get": {
        "operationId": "get_simulation_result_api_v1_simulations_jobs__job_id__result_get",
        "parameters": [
          {
            "in": "path",
            "name": "job_id",
            "required": true,
            "schema": {
              "title": "Job Id",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/WeatherSimulationResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Get Simulation Result",
        "tags": [
          "simulations"
        ]
      }
    },
    "/api/v1/simulations/run": {
      "post": {
        "operationId": "run_simulation_api_v1_simulations_run_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/SimulationRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SimulationResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Run Simulation",
        "tags": [
          "simulations"
        ]
      }
    },
    "/api/v1/simulations/run-weather": {
      "post": {
        "operationId": "run_weather_simulation_api_v1_simulations_run_weather_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/WeatherSimulationRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/WeatherSimulationResponse"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Run Weather Simulation",
        "tags": [
          "simulations"
        ]
      }
    },
    "/api/v1/weather/cities": {
      "get": {
        "operationId": "list_cities_api_v1_weather_cities_get",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "items": {
                    "$ref": "#/components/schemas/CityResponse"
                  },
                  "title": "Response List Cities Api V1 Weather Cities Get",
                  "type": "array"
                }
              }
            },
            "description": "Successful Response"
          }
        },
        "summary": "List Cities",
        "tags": [
          "weather"
        ]
      }
    },
    "/api/v1/weather/history": {
      "get": {
        "operationId": "weather_history_api_v1_weather_history_get",
        "parameters": [
          {
            "in": "query",
            "name": "city_id",
            "required": true,
            "schema": {
              "title": "City Id",
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "start_time_local",
            "required": true,
            "schema": {
              "format": "date-time",
              "title": "Start Time Local",
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "duration_minutes",
            "required": false,
            "schema": {
              "default": 120,
              "maximum": 1440,
              "minimum": 1,
              "title": "Duration Minutes",
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/WeatherTimeSeries"
                }
              }
            },
            "description": "Successful Response"
          },
          "422": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            },
            "description": "Validation Error"
          }
        },
        "summary": "Weather History",
        "tags": [
          "weather"
        ]
      }
    }
  }
}
```

