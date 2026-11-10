"use client";

import dynamic from "next/dynamic";
import type { Data } from "plotly.js";

import { METRIC_LABELS, VARIABLE_LABELS } from "@/lib/optimization-labels";
import type { MetricName, RequirementMapResult } from "@/types/optimization";

const Plot = dynamic(() => import("react-plotly.js"), { ssr: false });

export function RequirementMapChart({ map, metric }: { map: RequirementMapResult; metric: MetricName }) {
  const z = map.cells.map((row) => row.map((cell) => (cell ? cell.metric_value : null)));
  const feasible = map.cells.flat().filter((cell) => cell?.feasible);
  const frontier = map.frontier.filter((p) => p.minimum_x !== null);

  const data: Data[] = [
    {
      type: "heatmap", x: map.x_values, y: map.y_values, z,
      colorscale: "RdYlBu", reversescale: false,
      colorbar: { title: { text: METRIC_LABELS[metric] } },
      hovertemplate: "x=%{x}<br>y=%{y}<br>value=%{z:.4f}<extra></extra>",
    },
    {
      type: "scatter", mode: "markers", name: "Feasible",
      x: feasible.map((c) => c!.x), y: feasible.map((c) => c!.y),
      marker: { symbol: "circle-open", size: 12, color: "#0f172a", line: { width: 2 } },
    },
    {
      type: "scatter", mode: "lines+markers", name: "Requirement frontier",
      x: frontier.map((p) => p.minimum_x), y: frontier.map((p) => p.y),
      line: { color: "#f8fafc", width: 3, shape: "hv" },
    },
  ];

  return (
    <div className="overflow-hidden rounded-2xl border border-slate-800 bg-slate-900 p-4">
      <h2 className="mb-4 text-xl font-semibold">Requirement Map</h2>
      <Plot
        data={data}
        layout={{
          autosize: true, height: 520, paper_bgcolor: "#0f172a", plot_bgcolor: "#0f172a",
          font: { color: "#cbd5e1" }, margin: { l: 70, r: 30, t: 20, b: 60 },
          xaxis: { title: { text: VARIABLE_LABELS[map.x_variable] } },
          yaxis: { title: { text: VARIABLE_LABELS[map.y_variable] } },
          legend: { orientation: "h", y: -0.2 },
        }}
        config={{ responsive: true, displaylogo: false, toImageButtonOptions: { format: "png", filename: "requirement-map", scale: 2 } }}
        useResizeHandler
        style={{ width: "100%", height: "100%" }}
      />
      <p className="mt-2 text-sm text-slate-400">
        Other variables fixed at the optimum:{" "}
        {Object.entries(map.fixed_parameters).map(([k, v]) => `${k} = ${v.toFixed(3)}`).join(", ") || "none"}.
        Blank cells violate the optical energy constraint.
      </p>
    </div>
  );
}