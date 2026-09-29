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