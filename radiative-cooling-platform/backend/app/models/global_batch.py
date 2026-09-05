from datetime import datetime
from uuid import uuid4

from sqlalchemy import (
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


class GlobalBatchJob(Base):
    __tablename__ = "global_batch_jobs"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    celery_group_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        index=True,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="queued",
        index=True,
    )

    stage: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        default="queued",
    )

    progress: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    total_city_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    completed_city_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    failed_city_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    cancelled_city_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    request_json: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
    )

    summary_json: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    error_message: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
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

    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    city_results: Mapped[list["GlobalCityResult"]] = relationship(
        back_populates="batch",
        cascade="all, delete-orphan",
        order_by="GlobalCityResult.city_id",
    )


class GlobalCityResult(Base):
    __tablename__ = "global_city_results"

    __table_args__ = (
        UniqueConstraint(
            "batch_id",
            "city_id",
            name="uq_global_batch_city",
        ),
    )

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    batch_id: Mapped[str] = mapped_column(
        ForeignKey(
            "global_batch_jobs.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    celery_task_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        index=True,
    )

    city_id: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    city_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    country: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    latitude: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    longitude: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="queued",
        index=True,
    )

    stage: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        default="queued",
    )

    progress: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    climate_adaptation_rate_percent: Mapped[float | None] = (
        mapped_column(
            Float,
            nullable=True,
        )
    )

    annual_average_skin_improvement_c: Mapped[float | None] = (
        mapped_column(
            Float,
            nullable=True,
        )
    )

    annual_average_core_improvement_c: Mapped[float | None] = (
        mapped_column(
            Float,
            nullable=True,
        )
    )

    maximum_skin_improvement_c: Mapped[float | None] = (
        mapped_column(
            Float,
            nullable=True,
        )
    )

    effective_cooling_hours: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )
    
    exposure_coverage_percent: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    sampled_day_count: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    eligible_sample_count: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    retry_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
        server_default="0",
    )

    evaluated_weighted_days: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    beneficial_weighted_days: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    monthly_json: Mapped[list | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    error_message: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
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

    batch: Mapped["GlobalBatchJob"] = relationship(
        back_populates="city_results",
    )