"use client";

import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";

import { NumberField, OptionalNumberField } from "@/components/forms/number-field";
import { SelectField } from "@/components/forms/select-field";
import { EnvironmentAssumptionsFields } from "@/components/simulation/environment-assumptions-fields";
import { MaterialInputFields } from "@/components/simulation/material-input-fields";
import { PersonInputFields } from "@/components/simulation/person-input-fields";
import { createOptimization, estimateOptimization, getCities } from "@/lib/api-client";
import { DEFAULT_ENVIRONMENT_ASSUMPTIONS } from "@/lib/environment-assumptions";
import {
  DEFAULT_DEMAND_DIRECTION,
  EMISSIVITY_BAND_VARIABLES,
  METRIC_OPTIONS,
  METRIC_SCALES,
  OBJECTIVE_OPTIONS,
  VARIABLE_LABELS,
} from "@/lib/optimization-labels";
import type {
  DecisionVariable,
  DecisionVariableName,
  DemandDirection,
  MetricConstraint,
  MetricName,
  ObjectiveName,
  OptimizationCreate,
  OptimizationEstimate,
  Sense,
} from "@/types/optimization";
import type { City } from "@/types/simulation";

const VARIABLE_DEFAULTS: Record<DecisionVariableName, { lower: number; upper: number; step: number }> = {
  solar_reflectance: { lower: 0.3, upper: 0.98, step: 0.01 },
  solar_transmittance: { lower: 0, upper: 0.3, step: 0.01 },
  infrared_emissivity: { lower: 0.5, upper: 0.99, step: 0.01 },
  infrared_emissivity_window: { lower: 0.5, upper: 0.99, step: 0.01 },
  infrared_emissivity_outside_window: { lower: 0.05, upper: 0.99, step: 0.01 },
  infrared_transmittance: { lower: 0, upper: 0.5, step: 0.01 },
  clothing_insulation_clo: { lower: 0.2, upper: 0.8, step: 0.05 },
  evaporative_resistance_m2pa_w: { lower: 5, upper: 30, step: 0.5 },
  infrared_emissivity_ground_facing: { lower: 0.05, upper: 0.99, step: 0.01 },
};

const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
const MAX_VARIABLES = 6;

function newVariable(name: DecisionVariableName): DecisionVariable {
  const { lower, upper } = VARIABLE_DEFAULTS[name];
  return { name, lower, upper, demand_direction: DEFAULT_DEMAND_DIRECTION[name], demand_weight: 1 };
}

const initialRequest: OptimizationCreate = {
  name: "Guangzhou August requirement search",
  city_id: "guangzhou",
  year: 2023,
  months: [8],
  sample_days_per_month: 3,
  local_start_hour: 12,
  duration_minutes: 120,
  output_interval_minutes: 5,
  skin_threshold_c: 35,
  core_threshold_c: 38,
  person: {
    met: 2.6, body_mass_kg: 70, body_surface_area_m2: 1.8,
    initial_core_temperature_c: 36.8, initial_skin_temperature_c: 33.7, position: "standing",
  },
  control_material: {
    name: "Conventional clothing", clothing_insulation_clo: 0.5, clothing_area_factor: null,
    solar_reflectance: 0.3, solar_transmittance: 0, infrared_emissivity: 0.9,
    projected_solar_area_factor: 0.25,
  },
  base_material: {
    name: "RC candidate", clothing_insulation_clo: 0.4, clothing_area_factor: null,
    solar_reflectance: 0.9, solar_transmittance: 0, infrared_emissivity: 0.95,
    projected_solar_area_factor: 0.25,
  },
  environment_assumptions: DEFAULT_ENVIRONMENT_ASSUMPTIONS,
  variables: [newVariable("solar_reflectance"), newVariable("infrared_emissivity")],
  objective: { metric: "skin_excess_degree_hours", sense: "minimize" },
  constraints: [
    { metric: "skin_excess_degree_hours", operator: "<=", threshold: 0.5, scale: null },
    { metric: "peak_core_temperature_c", operator: "<=", threshold: 38, scale: null },
  ],
  algorithm: "differential_evolution",
  population_multiplier: 10,
  max_generations: 30,
  seed: 42,
  secondary_demand_weight: 0.001,
  convergence_tolerance: 0.0001,
  requirement_map: { x_variable: "solar_reflectance", y_variable: "infrared_emissivity", resolution: 11 },
};

function blockedReason(name: DecisionVariableName, request: OptimizationCreate): string | null {
  const names = new Set(request.variables.map((v) => v.name));
  if (names.has(name)) return null;
  if (name === "infrared_emissivity") {
    if ([...EMISSIVITY_BAND_VARIABLES].some((n) => names.has(n))) return "Not combinable with ε_W / ε_N.";
    if (request.base_material.infrared_emissivity_window != null) return "Candidate is selective; use ε_W / ε_N.";
  }
  if (EMISSIVITY_BAND_VARIABLES.has(name) && names.has("infrared_emissivity")) return "Not combinable with gray ε.";
  if (request.variables.length >= MAX_VARIABLES) return `At most ${MAX_VARIABLES} variables.`;
  return null;
}

export default function NewOptimizationPage() {
  const router = useRouter();
  const [request, setRequest] = useState<OptimizationCreate>(initialRequest);
  const [cities, setCities] = useState<City[]>([]);
  const [estimate, setEstimate] = useState<{ key: string; data: OptimizationEstimate | null; error: string } | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    let disposed = false;
    getCities()
      .then((list) => { if (!disposed) setCities(list); })
      .catch((caught: unknown) => { if (!disposed) setError(caught instanceof Error ? caught.message : "Unable to load cities"); });
    return () => { disposed = true; };
  }, []);

  const requestKey = JSON.stringify(request);

  useEffect(() => {
    let disposed = false;
    const timer = window.setTimeout(() => {
      estimateOptimization(request)
        .then((data) => { if (!disposed) setEstimate({ key: requestKey, data, error: "" }); })
        .catch((caught: unknown) => {
          if (!disposed) setEstimate({ key: requestKey, data: null, error: caught instanceof Error ? caught.message : "Estimate failed" });
        });
    }, 400);
    return () => { disposed = true; window.clearTimeout(timer); };
  }, [request, requestKey]);

  const currentEstimate = estimate?.key === requestKey ? estimate : null;

  function update<K extends keyof OptimizationCreate>(key: K, value: OptimizationCreate[K]) {
    setRequest((current) => ({ ...current, [key]: value }));
  }

  function toggleVariable(name: DecisionVariableName) {
    setRequest((current) => {
      const exists = current.variables.some((v) => v.name === name);
      const variables = exists
        ? current.variables.filter((v) => v.name !== name)
        : [...current.variables, newVariable(name)];
      const map = current.requirement_map;
      const valid = map && variables.some((v) => v.name === map.x_variable) && variables.some((v) => v.name === map.y_variable);
      return { ...current, variables, requirement_map: valid ? map : null };
    });
  }

  function updateVariable(name: DecisionVariableName, patch: Partial<DecisionVariable>) {
    update("variables", request.variables.map((v) => (v.name === name ? { ...v, ...patch } : v)));
  }

  function updateConstraint(index: number, patch: Partial<MetricConstraint>) {
    update("constraints", request.constraints.map((c, i) => (i === index ? { ...c, ...patch } : c)));
  }

  function toggleMonth(month: number) {
    const months = request.months.includes(month)
      ? request.months.filter((m) => m !== month)
      : [...request.months, month].sort((a, b) => a - b);
    if (months.length > 0) update("months", months);
  }

  function setObjectiveMetric(metric: ObjectiveName) {
    update("objective", { metric, sense: metric === "material_demand" ? "minimize" : request.objective.sense });
  }

  async function submit() {
    setSubmitting(true);
    setError("");
    try {
      const job = await createOptimization(request);
      router.push(`/optimizations/${job.id}`);
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : "Unable to create optimization");
      setSubmitting(false);
    }
  }

  const variableOptions = request.variables.map((v) => ({ value: v.name, label: VARIABLE_LABELS[v.name] }));
  const variableNames = request.variables.map((v) => v.name);

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl space-y-6 px-6 py-10">
        <header>
          <p className="text-sm text-cyan-400">Inverse Design</p>
          <h1 className="mt-2 text-3xl font-bold">Derive Material Requirements from a Comfort Target</h1>
          <p className="mt-3 max-w-4xl text-slate-400">
            Constraints are satisfied first; among feasible garments the objective is optimised and
            ties go to the least demanding design. Choose <em>Material demand</em> as the objective to
            ask directly for the minimum properties that meet the constraints.
          </p>
        </header>

        {error && <div role="alert" className="rounded-xl border border-red-900 bg-red-950 p-4 text-red-300">{error}</div>}

        <Section title="Scenario">
          <div className="grid gap-5 md:grid-cols-2 lg:grid-cols-4">
            <label className="block md:col-span-2">
              <span className="mb-2 block text-sm text-slate-300">Name</span>
              <input value={request.name} onChange={(e) => update("name", e.target.value)}
                className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2" />
            </label>
            <SelectField label="City" value={request.city_id}
              options={cities.length ? cities.map((c) => ({ value: c.id, label: `${c.name} – ${c.climate_type}` })) : [{ value: request.city_id, label: request.city_id }]}
              onChange={(v) => update("city_id", v)} />
            <NumberField label="Weather year" value={request.year} min={1940} max={2100} onChange={(v) => update("year", v)} />
            <NumberField label="Sample days / month" value={request.sample_days_per_month} min={1} max={31} onChange={(v) => update("sample_days_per_month", v)} />
            <NumberField label="Local start hour" value={request.local_start_hour} min={0} max={23} onChange={(v) => update("local_start_hour", v)} />
            <NumberField label="Exposure duration" suffix="min" value={request.duration_minutes} min={30} max={480} step={10} onChange={(v) => update("duration_minutes", v)} />
            <NumberField label="Output interval" suffix="min" value={request.output_interval_minutes} min={1} max={30} onChange={(v) => update("output_interval_minutes", v)} />
            <NumberField label="Skin threshold" suffix="°C" value={request.skin_threshold_c} min={30} max={42} step={0.1} onChange={(v) => update("skin_threshold_c", v)} />
            <NumberField label="Core threshold" suffix="°C" value={request.core_threshold_c} min={36.5} max={41} step={0.1} onChange={(v) => update("core_threshold_c", v)} />
          </div>
          <div className="mt-5 flex flex-wrap gap-2">
            {MONTHS.map((label, index) => {
              const month = index + 1;
              const active = request.months.includes(month);
              return (
                <button key={label} type="button" aria-pressed={active} onClick={() => toggleMonth(month)}
                  className={`rounded-lg border px-3 py-1.5 text-sm ${active ? "border-cyan-400 bg-cyan-950 text-cyan-200" : "border-slate-700 text-slate-400"}`}>
                  {label}
                </button>
              );
            })}
          </div>
        </Section>

        <Section title="Decision variables">
          <p className="mb-4 text-sm text-slate-400">
            Demand direction says which end of a range is harder to manufacture; it drives requirement
            readings and tie-breaking only, never the physics.
          </p>
          <div className="space-y-3">
            {(Object.keys(VARIABLE_DEFAULTS) as DecisionVariableName[]).map((name) => {
              const variable = request.variables.find((v) => v.name === name);
              const blocked = blockedReason(name, request);
              const { step } = VARIABLE_DEFAULTS[name];
              return (
                <div key={name} className="grid items-end gap-4 rounded-xl border border-slate-800 bg-slate-950/50 p-4 md:grid-cols-[16rem_1fr_1fr_10rem_7rem]">
                  <label className={`flex items-center gap-3 ${blocked ? "opacity-50" : ""}`}>
                    <input type="checkbox" checked={Boolean(variable)} disabled={Boolean(blocked)}
                      onChange={() => toggleVariable(name)} className="h-4 w-4 accent-cyan-400" />
                    <span>{VARIABLE_LABELS[name]}</span>
                  </label>
                  {variable ? (
                    <>
                      <NumberField label="Lower" value={variable.lower} step={step} onChange={(v) => updateVariable(name, { lower: v })} />
                      <NumberField label="Upper" value={variable.upper} step={step} onChange={(v) => updateVariable(name, { upper: v })} />
                      <SelectField<DemandDirection> label="Harder when"
                        value={variable.demand_direction ?? DEFAULT_DEMAND_DIRECTION[name]}
                        options={[{ value: "increasing", label: "Higher" }, { value: "decreasing", label: "Lower" }]}
                        onChange={(v) => updateVariable(name, { demand_direction: v })} />
                      <NumberField label="Weight" value={variable.demand_weight ?? 1} min={0.1} max={10} step={0.1}
                        onChange={(v) => updateVariable(name, { demand_weight: v })} />
                    </>
                  ) : (
                    <p className="text-sm text-slate-500 md:col-span-4">{blocked ?? "Fixed at the candidate garment value."}</p>
                  )}
                </div>
              );
            })}
          </div>
        </Section>

        <Section title="Objective and constraints">
          <div className="grid gap-5 md:grid-cols-2">
            <SelectField<ObjectiveName> label="Objective" value={request.objective.metric} options={OBJECTIVE_OPTIONS}
              onChange={setObjectiveMetric} />
            <SelectField<Sense> label="Sense" value={request.objective.sense}
              disabled={request.objective.metric === "material_demand"}
              options={[{ value: "minimize", label: "Minimize" }, { value: "maximize", label: "Maximize" }]}
              onChange={(sense) => update("objective", { ...request.objective, sense })} />
          </div>
          {request.objective.metric.endsWith("exceedance_fraction") && (
            <p className="mt-3 text-sm text-amber-300">
              Exceedance fractions saturate when the threshold is crossed almost everywhere. The
              degree-hour metrics measure the same thing and keep a gradient.
            </p>
          )}
          <div className="mt-5 space-y-3">
            {request.constraints.map((constraint, index) => (
              <div key={index} className="grid items-end gap-4 md:grid-cols-[1fr_7rem_9rem_9rem_auto]">
                <SelectField<MetricName> label="Metric" value={constraint.metric} options={METRIC_OPTIONS}
                  onChange={(metric) => updateConstraint(index, { metric })} />
                <SelectField<"<=" | ">="> label="Operator" value={constraint.operator}
                  options={[{ value: "<=", label: "≤" }, { value: ">=", label: "≥" }]}
                  onChange={(operator) => updateConstraint(index, { operator })} />
                <NumberField label="Threshold" value={constraint.threshold} step={0.01}
                  onChange={(threshold) => updateConstraint(index, { threshold })} />
                <OptionalNumberField label="Scale" value={constraint.scale ?? null}
                  placeholder={`default ${METRIC_SCALES[constraint.metric]}`} step={0.01} min={0}
                  hint="Violation is divided by this before summing."
                  onChange={(scale) => updateConstraint(index, { scale })} />
                <button type="button" onClick={() => update("constraints", request.constraints.filter((_, i) => i !== index))}
                  className="rounded-lg border border-slate-700 px-3 py-2 text-sm text-slate-300">Remove</button>
              </div>
            ))}
            {request.constraints.length < 6 && (
              <button type="button"
                onClick={() => update("constraints", [...request.constraints, { metric: "mean_skin_cooling_c", operator: ">=", threshold: 1, scale: null }])}
                className="rounded-lg border border-cyan-800 px-4 py-2 text-sm text-cyan-300">Add constraint</button>
            )}
          </div>
        </Section>

        <Section title="Search settings">
          <div className="grid gap-5 md:grid-cols-2 lg:grid-cols-3">
            <NumberField label="Population multiplier" value={request.population_multiplier} min={4} max={30}
              hint="Population = multiplier × variable count" onChange={(v) => update("population_multiplier", v)} />
            <NumberField label="Max generations" value={request.max_generations} min={1} max={200} onChange={(v) => update("max_generations", v)} />
            <NumberField label="Seed" value={request.seed ?? 0} min={0} onChange={(v) => update("seed", v)} />
            <NumberField label="Convergence tolerance" value={request.convergence_tolerance} min={0.000001} max={1} step={0.00001}
              hint="Absolute, on the normalised objective." onChange={(v) => update("convergence_tolerance", v)} />
            <NumberField label="Secondary demand weight" value={request.secondary_demand_weight} min={0} max={1} step={0.001}
              hint="Tie-breaker towards less demanding garments." onChange={(v) => update("secondary_demand_weight", v)} />
            {request.requirement_map && variableOptions.length >= 2 && (
              <NumberField label="Map resolution" value={request.requirement_map.resolution} min={3} max={21}
                onChange={(resolution) => update("requirement_map", { ...request.requirement_map!, resolution })} />
            )}
          </div>
          {variableOptions.length >= 2 && (
            <div className="mt-5 grid gap-5 md:grid-cols-3">
              <label className="flex items-center gap-3 text-sm">
                <input type="checkbox" checked={Boolean(request.requirement_map)} className="h-4 w-4 accent-cyan-400"
                  onChange={(e) => update("requirement_map", e.target.checked
                    ? { x_variable: request.variables[0].name, y_variable: request.variables[1].name, resolution: 11 }
                    : null)} />
                Build requirement map
              </label>
              {request.requirement_map && (
                <>
                  <SelectField<DecisionVariableName> label="Map x axis" value={request.requirement_map.x_variable} options={variableOptions}
                    onChange={(x) => update("requirement_map", { ...request.requirement_map!, x_variable: x })} />
                  <SelectField<DecisionVariableName> label="Map y axis" value={request.requirement_map.y_variable} options={variableOptions}
                    onChange={(y) => update("requirement_map", { ...request.requirement_map!, y_variable: y })} />
                </>
              )}
            </div>
          )}
        </Section>

        <Section title="Person">
          <PersonInputFields person={request.person} onChange={(person) => update("person", person)} />
        </Section>

        <EnvironmentAssumptionsFields
          value={request.environment_assumptions ?? DEFAULT_ENVIRONMENT_ASSUMPTIONS}
          onChange={(value) => update("environment_assumptions", value)}
        />

        <div className="grid gap-6 lg:grid-cols-2">
          <Section title="Control clothing">
            <MaterialInputFields material={request.control_material} showName enableLibrary
              onChange={(m) => update("control_material", m)} />
          </Section>
          <Section title="Candidate garment (fixed fields)">
            <p className="mb-4 text-sm text-slate-400">
              Overwritten by the search: {variableNames.map((n) => VARIABLE_LABELS[n]).join(", ")}.
            </p>
            <MaterialInputFields material={request.base_material} showName enableLibrary
              onChange={(m) => update("base_material", m)} />
          </Section>
        </div>

        <Section title="Workload estimate">
          {currentEstimate?.data ? (
            <dl className="grid gap-4 text-sm sm:grid-cols-3 lg:grid-cols-4">
              <Stat label="Population" value={currentEstimate.data.population_size} />
              <Stat label="Optimizer evaluations" value={currentEstimate.data.optimizer_evaluation_budget} />
              <Stat label="Map evaluations" value={currentEstimate.data.requirement_map_evaluations} />
              <Stat label="Corners" value={currentEstimate.data.corner_evaluations} />
              <Stat label="Sensitivity probes" value={currentEstimate.data.sensitivity_evaluations} />
              <Stat label="Sample days" value={currentEstimate.data.sample_count} />
              <Stat label="Thermal simulations (max)" value={currentEstimate.data.thermal_simulation_budget} />
              <Stat label="Weather requests" value={currentEstimate.data.weather_requests} />
            </dl>
          ) : currentEstimate?.error ? (
            <p className="text-sm text-amber-300">{currentEstimate.error}</p>
          ) : (
            <p className="text-sm text-slate-400">Calculating…</p>
          )}
        </Section>

        <button type="button" onClick={submit} disabled={submitting || Boolean(currentEstimate?.error)}
          className="rounded-xl bg-cyan-400 px-8 py-3 font-semibold text-slate-950 disabled:cursor-not-allowed disabled:opacity-50">
          {submitting ? "Submitting…" : "Start Search"}
        </button>
      </div>
    </main>
  );
}

function Section({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="mb-5 text-xl font-semibold">{title}</h2>
      {children}
    </section>
  );
}

function Stat({ label, value }: { label: string; value: number }) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-950 p-4">
      <dt className="text-xs uppercase tracking-wide text-slate-500">{label}</dt>
      <dd className="mt-2 text-lg font-semibold text-cyan-300">{value.toLocaleString()}</dd>
    </div>
  );
}