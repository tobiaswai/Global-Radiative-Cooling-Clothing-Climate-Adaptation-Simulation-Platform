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