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

  return (
    <div className="overflow-hidden rounded-2xl border border-slate-800 bg-slate-900 p-4">
      <h2 className="mb-4 text-xl font-semibold">
        輻射製冷服裝熱流分解
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
            name: "對流",
          },
          {
            x: points.map((point) => point.minute),
            y: points.map(
              (point) =>
                point.longwave_radiation_w_m2,
            ),
            type: "scatter",
            mode: "lines",
            name: "長波輻射",
          },
          {
            x: points.map((point) => point.minute),
            y: points.map(
              (point) => point.evaporation_w_m2,
            ),
            type: "scatter",
            mode: "lines",
            name: "蒸發",
          },
          {
            x: points.map((point) => point.minute),
            y: points.map(
              (point) => point.absorbed_solar_w_m2,
            ),
            type: "scatter",
            mode: "lines",
            name: "太陽吸收",
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
            r: 30,
            t: 20,
            b: 60,
          },
          xaxis: {
            title: {
              text: "時間（分鐘）",
            },
            gridcolor: "#334155",
          },
          yaxis: {
            title: {
              text: "熱流密度（W/m²）",
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
        正長波輻射和正對流代表人體向外散熱；
        太陽吸收代表環境向服裝／人體增加的熱負荷。
      </p>
    </div>
  );
}