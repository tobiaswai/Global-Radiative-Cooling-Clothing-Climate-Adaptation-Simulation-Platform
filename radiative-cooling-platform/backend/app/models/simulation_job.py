from datetime import datetime
from uuid import uuid4

from sqlalchemy import (
    DateTime,
    Integer,
    String,
    Text,
    func,
    Index,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.db.base import Base


class SimulationJob(Base):
    __tablename__ = "simulation_jobs"
    __table_args__ = (
        Index("ix_simulation_jobs_lease_reap", "status", "lease_expires_at"),
    )
    
    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    celery_task_id: Mapped[str | None] = (
        mapped_column(
            String(255),
            nullable=True,
            index=True,
        )
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

    city_id: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    request_json: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
    )

    summary_json: Mapped[dict | None] = (
        mapped_column(
            JSONB,
            nullable=True,
        )
    )

    result_path: Mapped[str | None] = (
        mapped_column(
            Text,
            nullable=True,
        )
    )

    error_message: Mapped[str | None] = (
        mapped_column(
            Text,
            nullable=True,
        )
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

    started_at: Mapped[datetime | None] = (
        mapped_column(
            DateTime(timezone=True),
            nullable=True,
        )
    )

    completed_at: Mapped[datetime | None] = (
        mapped_column(
            DateTime(timezone=True),
            nullable=True,
        )
    )

    # Stage 4. Material library versions the request was resolved against.
    control_material_version_id: Mapped[str | None] = mapped_column(
        String(36),
        ForeignKey("material_versions.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    rc_material_version_id: Mapped[str | None] = mapped_column(
        String(36),
        ForeignKey("material_versions.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    
    # Stage 9. Same lease contract as GlobalCityResult.
    attempt: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default="0")
    lease_owner: Mapped[str | None] = mapped_column(String(100), nullable=True)
    lease_expires_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    last_heartbeat_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)