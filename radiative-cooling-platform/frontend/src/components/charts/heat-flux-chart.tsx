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