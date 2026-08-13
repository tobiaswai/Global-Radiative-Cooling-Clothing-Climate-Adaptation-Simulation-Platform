from datetime import datetime
from uuid import uuid4

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.db.base import Base


class Material(Base):
    __tablename__ = "materials"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
        index=True,
    )

    slug: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
        unique=True,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    institution: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    is_archived: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default="false",
        index=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    versions: Mapped[list["MaterialVersion"]] = relationship(
        back_populates="material",
        cascade="all, delete-orphan",
        order_by="MaterialVersion.version_number",
    )


class MaterialVersion(Base):
    __tablename__ = "material_versions"

    __table_args__ = (
        UniqueConstraint(
            "material_id",
            "version_number",
            name="uq_material_version_number",
        ),
        CheckConstraint(
            "solar_reflectance >= 0 "
            "AND solar_reflectance <= 1",
            name="ck_material_solar_reflectance",
        ),
        CheckConstraint(
            "solar_transmittance >= 0 "
            "AND solar_transmittance <= 1",
            name="ck_material_solar_transmittance",
        ),
        CheckConstraint(
            "infrared_emissivity >= 0 "
            "AND infrared_emissivity <= 1",
            name="ck_material_ir_emissivity",
        ),
        CheckConstraint(
            "infrared_transmittance >= 0 "
            "AND infrared_transmittance <= 1",
            name="ck_material_ir_transmittance",
        ),
        CheckConstraint(
            "solar_reflectance + solar_transmittance <= 1.000001",
            name="ck_material_solar_energy_sum",
        ),
    )

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    material_id: Mapped[str] = mapped_column(
        ForeignKey(
            "materials.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    version_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    mode: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="opaque_emitter",
    )

    clothing_insulation_clo: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    evaporative_resistance_m2pa_w: Mapped[float | None] = (
        mapped_column(
            Float,
            nullable=True,
        )
    )

    solar_reflectance: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    solar_transmittance: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=0.0,
    )

    infrared_emissivity: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    infrared_transmittance: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=0.0,
    )

    projected_solar_area_factor: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=0.25,
    )

    absorbed_solar_to_body_fraction: Mapped[float] = (
        mapped_column(
            Float,
            nullable=False,
            default=0.35,
        )
    )

    areal_density_g_m2: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    specific_heat_j_kgk: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    source_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="manual",
    )

    source_reference: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    material: Mapped["Material"] = relationship(
        back_populates="versions",
    )

    spectra: Mapped[list["MaterialSpectrum"]] = relationship(
        back_populates="material_version",
        cascade="all, delete-orphan",
    )


class MaterialSpectrum(Base):
    __tablename__ = "material_spectra"

    __table_args__ = (
        UniqueConstraint(
            "material_version_id",
            "spectrum_type",
            name="uq_material_version_spectrum_type",
        ),
    )

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    material_version_id: Mapped[str] = mapped_column(
        ForeignKey(
            "material_versions.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    spectrum_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    wavelength_unit: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="um",
    )

    points_json: Mapped[list[dict]] = mapped_column(
        JSONB,
        nullable=False,
    )

    point_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    minimum_wavelength_um: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    maximum_wavelength_um: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    original_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    file_checksum_sha256: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    material_version: Mapped["MaterialVersion"] = relationship(
        back_populates="spectra",
    )