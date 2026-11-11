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