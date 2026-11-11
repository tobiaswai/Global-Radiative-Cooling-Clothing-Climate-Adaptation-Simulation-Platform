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