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