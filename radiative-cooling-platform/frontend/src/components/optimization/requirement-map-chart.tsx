"use client";

import dynamic from "next/dynamic";
import type { Data } from "plotly.js";

import { METRIC_LABELS, TREND_LABELS, VARIABLE_LABELS } from "@/lib/optimization-labels";
import type { MetricName, RequirementMapResult } from "@/types/optimization";

const Plot = dynamic(() => import("react-plotly.js"), { ssr: false });

export function RequirementMapChart({ map, metric }: { map: RequirementMapResult; metric: MetricName }) {
  const z = map.cells.map((row) => row.map((cell) => (cell ? cell.metric_value : null)));
  const feasible = map.cells.flat().filter((cell): cell is NonNullable<typeof cell> => Boolean(cell?.feasible));
  const frontier = map.frontier
    .map((p) => ({ y: p.y, x: p.required_x ?? p.minimum_x }))
    .filter((p): p is { y: number; x: number } => p.x !== null);

  const data: Data[] = [
    {
      type: "heatmap", x: map.x_values, y: map.y_values, z,
      colorscale: "RdYlBu",
      colorbar: { title: { text: METRIC_LABELS[metric] } },
      hovertemplate: "x=%{x}<br>y=%{y}<br>value=%{z:.4f}<extra></extra>",
    },
    {
      type: "scatter", mode: "markers", name: "Feasible",
      x: feasible.map((c) => c.x), y: feasible.map((c) => c.y),
      marker: { symbol: "circle-open", size: 12, color: "#0f172a", line: { width: 2 } },
    },
    {
      type: "scatter", mode: "lines+markers", name: "Least demanding feasible x per row",
      x: frontier.map((p) => p.x), y: frontier.map((p) => p.y),
      line: { color: "#f8fafc", width: 3, shape: "hv" },
    },
  ];

  return (
    <div className="overflow-hidden rounded-2xl border border-slate-800 bg-slate-900 p-4">
      <h2 className="mb-1 text-xl font-semibold">Requirement Map</h2>
      <p className="mb-4 text-sm text-slate-400">
        Metric {METRIC_LABELS[metric]}
        {map.objective_trend_x && ` · along ${VARIABLE_LABELS[map.x_variable]}: ${TREND_LABELS[map.objective_trend_x]}`}
        {map.objective_trend_y && ` · along ${VARIABLE_LABELS[map.y_variable]}: ${TREND_LABELS[map.objective_trend_y]}`}
        {typeof map.plateau_fraction === "number" && ` · plateau ${(map.plateau_fraction * 100).toFixed(0)} %`}
      </p>
      <Plot
        data={data}
        layout={{
          autosize: true, height: 520, paper_bgcolor: "#0f172a", plot_bgcolor: "#0f172a",
          font: { color: "#cbd5e1" }, margin: { l: 70, r: 30, t: 20, b: 60 },
          xaxis: { title: { text: `${VARIABLE_LABELS[map.x_variable]} (more demanding → ${map.x_demand_direction === "decreasing" ? "left" : "right"})` } },
          yaxis: { title: { text: VARIABLE_LABELS[map.y_variable] } },
          legend: { orientation: "h", y: -0.2 },
        }}
        config={{ responsive: true, displaylogo: false, toImageButtonOptions: { format: "png", filename: "requirement-map", scale: 2 } }}
        useResizeHandler
        style={{ width: "100%", height: "100%" }}
      />
      <p className="mt-2 text-sm text-slate-400">
        Other variables fixed at the reported optimum:{" "}
        {Object.entries(map.fixed_parameters).map(([k, v]) => `${k} = ${v.toFixed(3)}`).join(", ") || "none"}.
        Blank cells are physically impossible garments.
      </p>
    </div>
  );
}