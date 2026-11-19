# Complete Backend Source Code (`backend/` - Excluding tests/docs/alembic/scripts/data)

## Directory Structure
```text
backend/alembic.ini
backend/alembic/README
backend/alembic/env.py
backend/alembic/script.py.mako
backend/alembic/versions/165a424d6ba1_stage7_job_leases_and_city_checkpoints.py
backend/alembic/versions/18a914bf4989_stage2_material_version_parameter_.py
backend/alembic/versions/5c968a541440_stage2_material_version_parameter_.py
backend/alembic/versions/933e5fc5bb27_create_simulation_jobs.py
backend/alembic/versions/9cbc48c31e6e_stage7_job_leases_and_city_checkpoints.py
backend/alembic/versions/9e0b460c56c3_add_global_batch_analysis_tables.py
backend/alembic/versions/a1f4c2d9e7b3_stage4_material_library_links.py
backend/alembic/versions/b4d8e2a6c1f3_stage_inverse_optimization_jobs.py
backend/alembic/versions/b83aed15c819_add_material_version_and_spectrum_tables.py
backend/alembic/versions/c7d2e9f4a1b8_stage3_material_version_clothing_area_factor.py
backend/alembic/versions/d7e1f3a9b2c4_stage10_material_ir_window_emissivity.py
backend/alembic/versions/df85b07c9163_add_stage_4_4_checkpoint_and_analytics_.py
backend/alembic/versions/e3b8c1d5f702_stage12_ground_facing_emissivity.py
backend/alembic/versions/e4ee64441802_add_stage_4_2_exposure_and_retry_fields.py
backend/alembic/versions/f0a1b2c3d4e5_stage9_job_leases_and_checkpoint_provenance.py
backend/app/__init__.py
backend/app/api/__init__.py
backend/app/api/benchmarks.py
backend/app/api/errors.py
backend/app/api/global_batches.py
backend/app/api/materials.py
backend/app/api/model.py
backend/app/api/ops.py
backend/app/api/optimizations.py
backend/app/api/router.py
backend/app/api/simulations.py
backend/app/api/weather.py
backend/app/core/__init__.py
backend/app/core/cities.py
backend/app/core/config.py
backend/app/core/cors.py
backend/app/core/runtime.py
backend/app/core/time.py
backend/app/db/__init__.py
backend/app/db/base.py
backend/app/db/session.py
backend/app/main.py
backend/app/models/__init__.py
backend/app/models/global_batch.py
backend/app/models/material.py
backend/app/models/optimization_job.py
backend/app/models/simulation_job.py
backend/app/schemas/__init__.py
backend/app/schemas/environment.py
backend/app/schemas/global_batch.py
backend/app/schemas/job.py
backend/app/schemas/material.py
backend/app/schemas/ops.py
backend/app/schemas/optimization.py
backend/app/schemas/provenance.py
backend/app/schemas/simulation.py
backend/app/schemas/weather.py
backend/app/services/__init__.py
backend/app/services/annual_sampling.py
backend/app/services/body.py
backend/app/services/checkpoints.py
backend/app/services/climate_adaptation.py
backend/app/services/climate_analytics.py
backend/app/services/clothing.py
backend/app/services/environment.py
backend/app/services/environment_model.py
backend/app/services/execution_profile.py
backend/app/services/exposure_statistics.py
backend/app/services/gagge_benchmark.py
backend/app/services/gagge_reference.py
backend/app/services/global_batch_export.py
backend/app/services/global_batch_service.py
backend/app/services/ground_surface.py
backend/app/services/job_service.py
backend/app/services/job_state.py
backend/app/services/leases.py
backend/app/services/longwave.py
backend/app/services/material_fields.py
backend/app/services/material_resolution.py
backend/app/services/model_parameters.py
backend/app/services/optimization/__init__.py
backend/app/services/optimization/evaluator.py
backend/app/services/optimization/jobs.py
backend/app/services/optimization/metrics.py
backend/app/services/optimization/objective.py
backend/app/services/optimization/requirement_map.py
backend/app/services/optimization/runner.py
backend/app/services/optimization/search_space.py
backend/app/services/optimization/service.py
backend/app/services/optimization/variables.py
backend/app/services/planck.py
backend/app/services/psychrometrics.py
backend/app/services/reproducibility.py
backend/app/services/result_export.py
backend/app/services/result_storage.py
backend/app/services/scenario_summary.py
backend/app/services/solar.py
backend/app/services/spectral_summary.py
backend/app/services/spectrum_parser.py
backend/app/services/stored_requests.py
backend/app/services/two_node.py
backend/app/services/weather.py
backend/app/services/weather_interpolation.py
backend/app/services/weather_quality.py
backend/app/services/weather_simulation.py
backend/app/utils/date_defaults.py
backend/app/worker/__init__.py
backend/app/worker/celery_app.py
backend/app/worker/optimization_tasks.py
backend/app/worker/tasks.py
backend/scripts/capture_weather_fixture.py
backend/scripts/compare_batches.py
backend/scripts/inspect_radiant_environment.py
backend/scripts/inspect_zoned_garment.py
backend/scripts/render_model_parameters_doc.py
backend/scripts/run_stage10_experiments.py
backend/scripts/run_stage11_experiments.py
backend/scripts/run_stage12_experiments.py
backend/scripts/summarize_optimizations.py
```

---

## Source Code Files

### File: `backend/alembic.ini`
```
# A generic, single database configuration.

[alembic]
# path to migration scripts.
# this is typically a path given in POSIX (e.g. forward slashes)
# format, relative to the token %(here)s which refers to the location of this
# ini file
script_location = %(here)s/alembic

# template used to generate migration file names; The default value is %%(rev)s_%%(slug)s
# Uncomment the line below if you want the files to be prepended with date and time
# see https://alembic.sqlalchemy.org/en/latest/tutorial.html#editing-the-ini-file
# for all available tokens
# file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s
# Or organize into date-based subdirectories (requires recursive_version_locations = true)
# file_template = %%(year)d/%%(month).2d/%%(day).2d_%%(hour).2d%%(minute).2d_%%(second).2d_%%(rev)s_%%(slug)s

# sys.path path, will be prepended to sys.path if present.
# defaults to the current working directory.  for multiple paths, the path separator
# is defined by "path_separator" below.
prepend_sys_path = .


# timezone to use when rendering the date within the migration file
# as well as the filename.
# If specified, requires the tzdata library which can be installed by adding
# `alembic[tz]` to the pip requirements.
# string value is passed to ZoneInfo()
# leave blank for localtime
# timezone =

# max length of characters to apply to the "slug" field
# truncate_slug_length = 40

# set to 'true' to run the environment during
# the 'revision' command, regardless of autogenerate
# revision_environment = false

# set to 'true' to allow .pyc and .pyo files without
# a source .py file to be detected as revisions in the
# versions/ directory
# sourceless = false

# version location specification; This defaults
# to <script_location>/versions.  When using multiple version
# directories, initial revisions must be specified with --version-path.
# The path separator used here should be the separator specified by "path_separator"
# below.
# version_locations = %(here)s/bar:%(here)s/bat:%(here)s/alembic/versions

# path_separator; This indicates what character is used to split lists of file
# paths, including version_locations and prepend_sys_path within configparser
# files such as alembic.ini.
# The default rendered in new alembic.ini files is "os", which uses os.pathsep
# to provide os-dependent path splitting.
#
# Note that in order to support legacy alembic.ini files, this default does NOT
# take place if path_separator is not present in alembic.ini.  If this
# option is omitted entirely, fallback logic is as follows:
#
# 1. Parsing of the version_locations option falls back to using the legacy
#    "version_path_separator" key, which if absent then falls back to the legacy
#    behavior of splitting on spaces and/or commas.
# 2. Parsing of the prepend_sys_path option falls back to the legacy
#    behavior of splitting on spaces, commas, or colons.
#
# Valid values for path_separator are:
#
# path_separator = :
# path_separator = ;
# path_separator = space
# path_separator = newline
#
# Use os.pathsep. Default configuration used for new projects.
path_separator = os

# set to 'true' to search source files recursively
# in each "version_locations" directory
# new in Alembic version 1.10
# recursive_version_locations = false

# the output encoding used when revision files
# are written from script.py.mako
# output_encoding = utf-8

# database URL.  This is consumed by the user-maintained env.py script only.
# other means of configuring database URLs may be customized within the env.py
# file.
sqlalchemy.url = driver://user:pass@localhost/dbname


[post_write_hooks]
# post_write_hooks defines scripts or Python functions that are run
# on newly generated revision scripts.  See the documentation for further
# detail and examples

# format using "black" - use the console_scripts runner, against the "black" entrypoint
# hooks = black
# black.type = console_scripts
# black.entrypoint = black
# black.options = -l 79 REVISION_SCRIPT_FILENAME

# lint with attempts to fix using "ruff" - use the module runner, against the "ruff" module
# hooks = ruff
# ruff.type = module
# ruff.module = ruff
# ruff.options = check --fix REVISION_SCRIPT_FILENAME

# Alternatively, use the exec runner to execute a binary found on your PATH
# hooks = ruff
# ruff.type = exec
# ruff.executable = ruff
# ruff.options = check --fix REVISION_SCRIPT_FILENAME

# Logging configuration.  This is also consumed by the user-maintained
# env.py script only.
[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARNING
handlers = console
qualname =

[logger_sqlalchemy]
level = WARNING
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S

```

### File: `backend/alembic/README`
```
Generic single-database configuration.
```

### File: `backend/alembic/env.py`
```python
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config
from sqlalchemy import pool

from app.core.config import settings
from app.db.base import Base

# 必須導入模型，才能註冊到 Base.metadata。
import app.models  # noqa: F401


config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

config.set_main_option(
    "sqlalchemy.url",
    settings.database_url.replace("%", "%%"),
)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option(
        "sqlalchemy.url"
    )

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={
            "paramstyle": "named",
        },
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(
            config.config_ini_section,
            {},
        ),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

### File: `backend/alembic/script.py.mako`
```
"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision: str = ${repr(up_revision)}
down_revision: Union[str, Sequence[str], None] = ${repr(down_revision)}
branch_labels: Union[str, Sequence[str], None] = ${repr(branch_labels)}
depends_on: Union[str, Sequence[str], None] = ${repr(depends_on)}


def upgrade() -> None:
    """Upgrade schema."""
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    """Downgrade schema."""
    ${downgrades if downgrades else "pass"}

```

### File: `backend/alembic/versions/165a424d6ba1_stage7_job_leases_and_city_checkpoints.py`
```python
"""stage7 job leases and city checkpoints

Revision ID: 165a424d6ba1
Revises: 9cbc48c31e6e
Create Date: 2026-10-01 20:22:06.574354

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '165a424d6ba1'
down_revision: Union[str, Sequence[str], None] = '9cbc48c31e6e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

```

### File: `backend/alembic/versions/18a914bf4989_stage2_material_version_parameter_.py`
```python
"""stage2 material version parameter sources

Revision ID: 18a914bf4989
Revises: 5c968a541440
Create Date: 2026-09-29 11:39:52.577708

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18a914bf4989'
down_revision: Union[str, Sequence[str], None] = '5c968a541440'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

```

### File: `backend/alembic/versions/5c968a541440_stage2_material_version_parameter_.py`
```python
"""stage2 material version parameter sources

Revision ID: 5c968a541440
Revises: df85b07c9163
Create Date: 2026-09-28 22:27:44.173024

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '5c968a541440'
down_revision: Union[str, Sequence[str], None] = 'df85b07c9163'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('material_versions', sa.Column('parameter_sources_json', postgresql.JSONB(astext_type=sa.Text()), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('material_versions', 'parameter_sources_json')
    # ### end Alembic commands ###

```

### File: `backend/alembic/versions/933e5fc5bb27_create_simulation_jobs.py`
```python
"""create simulation jobs

Revision ID: 933e5fc5bb27
Revises: 
Create Date: 2026-08-04 09:57:59.602243

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '933e5fc5bb27'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('simulation_jobs',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('celery_task_id', sa.String(length=255), nullable=True),
    sa.Column('status', sa.String(length=30), nullable=False),
    sa.Column('stage', sa.String(length=100), nullable=False),
    sa.Column('progress', sa.Integer(), nullable=False),
    sa.Column('city_id', sa.String(length=100), nullable=False),
    sa.Column('request_json', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('summary_json', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('result_path', sa.Text(), nullable=True),
    sa.Column('error_message', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('started_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('completed_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_simulation_jobs_celery_task_id'), 'simulation_jobs', ['celery_task_id'], unique=False)
    op.create_index(op.f('ix_simulation_jobs_city_id'), 'simulation_jobs', ['city_id'], unique=False)
    op.create_index(op.f('ix_simulation_jobs_status'), 'simulation_jobs', ['status'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_simulation_jobs_status'), table_name='simulation_jobs')
    op.drop_index(op.f('ix_simulation_jobs_city_id'), table_name='simulation_jobs')
    op.drop_index(op.f('ix_simulation_jobs_celery_task_id'), table_name='simulation_jobs')
    op.drop_table('simulation_jobs')
    # ### end Alembic commands ###

```

### File: `backend/alembic/versions/9cbc48c31e6e_stage7_job_leases_and_city_checkpoints.py`
```python
"""stage7 job leases and city checkpoints

Revision ID: 9cbc48c31e6e
Revises: a1f4c2d9e7b3
Create Date: 2026-10-01 19:49:43.182771

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '9cbc48c31e6e'
down_revision: Union[str, Sequence[str], None] = 'a1f4c2d9e7b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('global_city_checkpoints',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('city_result_id', sa.String(length=36), nullable=False),
    sa.Column('month', sa.Integer(), nullable=False),
    sa.Column('attempt', sa.Integer(), server_default='0', nullable=False),
    sa.Column('payload_json', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['city_result_id'], ['global_city_results.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('city_result_id', 'month', name='uq_global_city_checkpoint_month')
    )
    op.create_index(op.f('ix_global_city_checkpoints_city_result_id'), 'global_city_checkpoints', ['city_result_id'], unique=False)
    op.add_column('global_batch_jobs', sa.Column('attempt', sa.Integer(), server_default='0', nullable=False))
    op.add_column('global_batch_jobs', sa.Column('lease_owner', sa.String(length=100), nullable=True))
    op.add_column('global_batch_jobs', sa.Column('lease_expires_at', sa.DateTime(timezone=True), nullable=True))
    op.add_column('global_batch_jobs', sa.Column('last_heartbeat_at', sa.DateTime(timezone=True), nullable=True))
    op.add_column('global_batch_jobs', sa.Column('cancel_requested_at', sa.DateTime(timezone=True), nullable=True))
    op.create_index(op.f('ix_global_batch_jobs_lease_expires_at'), 'global_batch_jobs', ['lease_expires_at'], unique=False)
    op.add_column('global_city_results', sa.Column('lease_owner', sa.String(length=100), nullable=True))
    op.add_column('global_city_results', sa.Column('lease_expires_at', sa.DateTime(timezone=True), nullable=True))
    op.create_index('ix_global_city_results_lease_reap', 'global_city_results', ['status', 'lease_expires_at'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_global_city_results_lease_reap', table_name='global_city_results')
    op.drop_column('global_city_results', 'lease_expires_at')
    op.drop_column('global_city_results', 'lease_owner')
    op.drop_index(op.f('ix_global_batch_jobs_lease_expires_at'), table_name='global_batch_jobs')
    op.drop_column('global_batch_jobs', 'cancel_requested_at')
    op.drop_column('global_batch_jobs', 'last_heartbeat_at')
    op.drop_column('global_batch_jobs', 'lease_expires_at')
    op.drop_column('global_batch_jobs', 'lease_owner')
    op.drop_column('global_batch_jobs', 'attempt')
    op.drop_index(op.f('ix_global_city_checkpoints_city_result_id'), table_name='global_city_checkpoints')
    op.drop_table('global_city_checkpoints')
    # ### end Alembic commands ###

```

### File: `backend/alembic/versions/9e0b460c56c3_add_global_batch_analysis_tables.py`
```python
"""add global batch analysis tables

Revision ID: 9e0b460c56c3
Revises: b83aed15c819
Create Date: 2026-09-05 17:33:28.446645

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '9e0b460c56c3'
down_revision: Union[str, Sequence[str], None] = 'b83aed15c819'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('global_batch_jobs',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('celery_group_id', sa.String(length=255), nullable=True),
    sa.Column('status', sa.String(length=30), nullable=False),
    sa.Column('stage', sa.String(length=100), nullable=False),
    sa.Column('progress', sa.Integer(), nullable=False),
    sa.Column('total_city_count', sa.Integer(), nullable=False),
    sa.Column('completed_city_count', sa.Integer(), nullable=False),
    sa.Column('failed_city_count', sa.Integer(), nullable=False),
    sa.Column('cancelled_city_count', sa.Integer(), nullable=False),
    sa.Column('request_json', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('summary_json', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('error_message', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('started_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('completed_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_global_batch_jobs_celery_group_id'), 'global_batch_jobs', ['celery_group_id'], unique=False)
    op.create_index(op.f('ix_global_batch_jobs_status'), 'global_batch_jobs', ['status'], unique=False)
    op.create_table('global_city_results',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('batch_id', sa.String(length=36), nullable=False),
    sa.Column('celery_task_id', sa.String(length=255), nullable=True),
    sa.Column('city_id', sa.String(length=100), nullable=False),
    sa.Column('city_name', sa.String(length=200), nullable=False),
    sa.Column('country', sa.String(length=200), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('status', sa.String(length=30), nullable=False),
    sa.Column('stage', sa.String(length=100), nullable=False),
    sa.Column('progress', sa.Integer(), nullable=False),
    sa.Column('climate_adaptation_rate_percent', sa.Float(), nullable=True),
    sa.Column('annual_average_skin_improvement_c', sa.Float(), nullable=True),
    sa.Column('annual_average_core_improvement_c', sa.Float(), nullable=True),
    sa.Column('maximum_skin_improvement_c', sa.Float(), nullable=True),
    sa.Column('effective_cooling_hours', sa.Float(), nullable=True),
    sa.Column('evaluated_weighted_days', sa.Integer(), nullable=True),
    sa.Column('beneficial_weighted_days', sa.Integer(), nullable=True),
    sa.Column('monthly_json', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('error_message', sa.Text(), nullable=True),
    sa.Column('started_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('completed_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['batch_id'], ['global_batch_jobs.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('batch_id', 'city_id', name='uq_global_batch_city')
    )
    op.create_index(op.f('ix_global_city_results_batch_id'), 'global_city_results', ['batch_id'], unique=False)
    op.create_index(op.f('ix_global_city_results_celery_task_id'), 'global_city_results', ['celery_task_id'], unique=False)
    op.create_index(op.f('ix_global_city_results_city_id'), 'global_city_results', ['city_id'], unique=False)
    op.create_index(op.f('ix_global_city_results_status'), 'global_city_results', ['status'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_global_city_results_status'), table_name='global_city_results')
    op.drop_index(op.f('ix_global_city_results_city_id'), table_name='global_city_results')
    op.drop_index(op.f('ix_global_city_results_celery_task_id'), table_name='global_city_results')
    op.drop_index(op.f('ix_global_city_results_batch_id'), table_name='global_city_results')
    op.drop_table('global_city_results')
    op.drop_index(op.f('ix_global_batch_jobs_status'), table_name='global_batch_jobs')
    op.drop_index(op.f('ix_global_batch_jobs_celery_group_id'), table_name='global_batch_jobs')
    op.drop_table('global_batch_jobs')
    # ### end Alembic commands ###

```

### File: `backend/alembic/versions/a1f4c2d9e7b3_stage4_material_library_links.py`
```python
"""stage4 material library links and constraints

Revision ID: a1f4c2d9e7b3
Revises: c7d2e9f4a1b8
Create Date: 2026-10-20 10:00:00.000000

Adds
* CHECK constraints that make every stored material version a valid
  MaterialInput (IR energy sum, Re,cl range).
* Nullable FK columns on simulation_jobs and global_batch_jobs recording
  which material versions a request was resolved against.

The upgrade refuses to run while rows violate the new constraints, instead
of silently failing half-way through.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'a1f4c2d9e7b3'
down_revision: Union[str, Sequence[str], None] = 'c7d2e9f4a1b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


JOB_TABLES = ("simulation_jobs", "global_batch_jobs")
LINK_COLUMNS = ("control_material_version_id", "rc_material_version_id")


def _assert_no_violations() -> None:
    bind = op.get_bind()

    checks = {
        "evaporative_resistance_m2pa_w outside [0, 1000]": (
            "SELECT count(*) FROM material_versions "
            "WHERE evaporative_resistance_m2pa_w IS NOT NULL "
            "AND (evaporative_resistance_m2pa_w < 0 "
            "OR evaporative_resistance_m2pa_w > 1000)"
        ),
        "infrared_emissivity + infrared_transmittance > 1": (
            "SELECT count(*) FROM material_versions "
            "WHERE infrared_emissivity + infrared_transmittance > 1.000001"
        ),
    }

    problems = [
        f"{label}: {count} row(s)"
        for label, sql in checks.items()
        if (count := bind.execute(sa.text(sql)).scalar_one())
    ]

    if problems:
        raise RuntimeError(
            "Cannot apply Stage 4 constraints; fix these material versions "
            "first: " + "; ".join(problems)
        )


def upgrade() -> None:
    _assert_no_violations()

    op.create_check_constraint(
        'ck_material_evaporative_resistance',
        'material_versions',
        'evaporative_resistance_m2pa_w IS NULL OR '
        '(evaporative_resistance_m2pa_w >= 0 '
        'AND evaporative_resistance_m2pa_w <= 1000)',
    )
    op.create_check_constraint(
        'ck_material_ir_energy_sum',
        'material_versions',
        'infrared_emissivity + infrared_transmittance <= 1.000001',
    )

    for table in JOB_TABLES:
        for column in LINK_COLUMNS:
            op.add_column(table, sa.Column(column, sa.String(length=36), nullable=True))
            op.create_foreign_key(
                f'fk_{table}_{column}',
                table,
                'material_versions',
                [column],
                ['id'],
                ondelete='SET NULL',
            )
            op.create_index(f'ix_{table}_{column}', table, [column])


def downgrade() -> None:
    for table in JOB_TABLES:
        for column in LINK_COLUMNS:
            op.drop_index(f'ix_{table}_{column}', table_name=table)
            op.drop_constraint(f'fk_{table}_{column}', table, type_='foreignkey')
            op.drop_column(table, column)

    op.drop_constraint('ck_material_ir_energy_sum', 'material_versions', type_='check')
    op.drop_constraint('ck_material_evaporative_resistance', 'material_versions', type_='check')
```

### File: `backend/alembic/versions/b4d8e2a6c1f3_stage_inverse_optimization_jobs.py`
```python
"""inverse optimization jobs

Revision ID: b4d8e2a6c1f3
Revises: f0a1b2c3d4e5
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = "b4d8e2a6c1f3"
down_revision: Union[str, Sequence[str], None] = "f0a1b2c3d4e5"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "optimization_jobs",
        sa.Column("id", sa.String(36), nullable=False),
        sa.Column("celery_task_id", sa.String(255), nullable=True),
        sa.Column("name", sa.String(200), nullable=False),
        sa.Column("city_id", sa.String(100), nullable=False),
        sa.Column("status", sa.String(30), nullable=False),
        sa.Column("stage", sa.String(100), nullable=False),
        sa.Column("progress", sa.Integer(), server_default="0", nullable=False),
        sa.Column("evaluation_count", sa.Integer(), server_default="0", nullable=False),
        sa.Column("request_json", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("history_json", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("result_json", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("error_message", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("attempt", sa.Integer(), server_default="0", nullable=False),
        sa.Column("lease_owner", sa.String(100), nullable=True),
        sa.Column("lease_expires_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("last_heartbeat_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("cancel_requested_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("control_material_version_id", sa.String(36), nullable=True),
        sa.Column("base_material_version_id", sa.String(36), nullable=True),
        sa.ForeignKeyConstraint(["control_material_version_id"], ["material_versions.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["base_material_version_id"], ["material_versions.id"], ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_optimization_jobs_status", "optimization_jobs", ["status"])
    op.create_index("ix_optimization_jobs_city_id", "optimization_jobs", ["city_id"])
    op.create_index("ix_optimization_jobs_celery_task_id", "optimization_jobs", ["celery_task_id"])
    op.create_index("ix_optimization_jobs_lease_reap", "optimization_jobs", ["status", "lease_expires_at"])
    op.create_index("ix_optimization_jobs_control_material_version_id", "optimization_jobs", ["control_material_version_id"])
    op.create_index("ix_optimization_jobs_base_material_version_id", "optimization_jobs", ["base_material_version_id"])


def downgrade() -> None:
    op.drop_table("optimization_jobs")
```

### File: `backend/alembic/versions/b83aed15c819_add_material_version_and_spectrum_tables.py`
```python
"""add material version and spectrum tables

Revision ID: b83aed15c819
Revises: 933e5fc5bb27
Create Date: 2026-08-12 09:46:37.814874

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b83aed15c819'
down_revision: Union[str, Sequence[str], None] = '933e5fc5bb27'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('materials',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('slug', sa.String(length=200), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('institution', sa.String(length=255), nullable=True),
    sa.Column('is_archived', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_materials_is_archived'), 'materials', ['is_archived'], unique=False)
    op.create_index(op.f('ix_materials_name'), 'materials', ['name'], unique=False)
    op.create_index(op.f('ix_materials_slug'), 'materials', ['slug'], unique=True)
    op.create_table('material_versions',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('material_id', sa.String(length=36), nullable=False),
    sa.Column('version_number', sa.Integer(), nullable=False),
    sa.Column('mode', sa.String(length=50), nullable=False),
    sa.Column('clothing_insulation_clo', sa.Float(), nullable=False),
    sa.Column('evaporative_resistance_m2pa_w', sa.Float(), nullable=True),
    sa.Column('solar_reflectance', sa.Float(), nullable=False),
    sa.Column('solar_transmittance', sa.Float(), nullable=False),
    sa.Column('infrared_emissivity', sa.Float(), nullable=False),
    sa.Column('infrared_transmittance', sa.Float(), nullable=False),
    sa.Column('projected_solar_area_factor', sa.Float(), nullable=False),
    sa.Column('absorbed_solar_to_body_fraction', sa.Float(), nullable=False),
    sa.Column('areal_density_g_m2', sa.Float(), nullable=True),
    sa.Column('specific_heat_j_kgk', sa.Float(), nullable=True),
    sa.Column('source_type', sa.String(length=50), nullable=False),
    sa.Column('source_reference', sa.Text(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.CheckConstraint('infrared_emissivity >= 0 AND infrared_emissivity <= 1', name='ck_material_ir_emissivity'),
    sa.CheckConstraint('infrared_transmittance >= 0 AND infrared_transmittance <= 1', name='ck_material_ir_transmittance'),
    sa.CheckConstraint('solar_reflectance + solar_transmittance <= 1.000001', name='ck_material_solar_energy_sum'),
    sa.CheckConstraint('solar_reflectance >= 0 AND solar_reflectance <= 1', name='ck_material_solar_reflectance'),
    sa.CheckConstraint('solar_transmittance >= 0 AND solar_transmittance <= 1', name='ck_material_solar_transmittance'),
    sa.ForeignKeyConstraint(['material_id'], ['materials.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('material_id', 'version_number', name='uq_material_version_number')
    )
    op.create_index(op.f('ix_material_versions_material_id'), 'material_versions', ['material_id'], unique=False)
    op.create_table('material_spectra',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('material_version_id', sa.String(length=36), nullable=False),
    sa.Column('spectrum_type', sa.String(length=50), nullable=False),
    sa.Column('wavelength_unit', sa.String(length=20), nullable=False),
    sa.Column('points_json', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('point_count', sa.Integer(), nullable=False),
    sa.Column('minimum_wavelength_um', sa.Float(), nullable=False),
    sa.Column('maximum_wavelength_um', sa.Float(), nullable=False),
    sa.Column('original_filename', sa.String(length=255), nullable=False),
    sa.Column('file_checksum_sha256', sa.String(length=64), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['material_version_id'], ['material_versions.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('material_version_id', 'spectrum_type', name='uq_material_version_spectrum_type')
    )
    op.create_index(op.f('ix_material_spectra_material_version_id'), 'material_spectra', ['material_version_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_material_spectra_material_version_id'), table_name='material_spectra')
    op.drop_table('material_spectra')
    op.drop_index(op.f('ix_material_versions_material_id'), table_name='material_versions')
    op.drop_table('material_versions')
    op.drop_index(op.f('ix_materials_slug'), table_name='materials')
    op.drop_index(op.f('ix_materials_name'), table_name='materials')
    op.drop_index(op.f('ix_materials_is_archived'), table_name='materials')
    op.drop_table('materials')
    # ### end Alembic commands ###

```

### File: `backend/alembic/versions/c7d2e9f4a1b8_stage3_material_version_clothing_area_factor.py`
```python
"""stage3 material version clothing area factor

Revision ID: c7d2e9f4a1b8
Revises: 18a914bf4989
Create Date: 2026-10-06 10:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7d2e9f4a1b8'
down_revision: Union[str, Sequence[str], None] = '18a914bf4989'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'material_versions',
        sa.Column('clothing_area_factor', sa.Float(), nullable=True),
    )
    op.create_check_constraint(
        'ck_material_clothing_area_factor',
        'material_versions',
        'clothing_area_factor IS NULL OR '
        '(clothing_area_factor >= 1.0 AND clothing_area_factor <= 2.0)',
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        'ck_material_clothing_area_factor',
        'material_versions',
        type_='check',
    )
    op.drop_column('material_versions', 'clothing_area_factor')
```

### File: `backend/alembic/versions/d7e1f3a9b2c4_stage10_material_ir_window_emissivity.py`
```python
"""stage10 material infrared window emissivity

Revision ID: d7e1f3a9b2c4
Revises: b4d8e2a6c1f3
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "d7e1f3a9b2c4"
down_revision: Union[str, Sequence[str], None] = "b4d8e2a6c1f3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "material_versions",
        sa.Column("infrared_emissivity_window", sa.Float(), nullable=True),
    )
    op.create_check_constraint(
        "ck_material_ir_emissivity_window",
        "material_versions",
        "infrared_emissivity_window IS NULL OR "
        "(infrared_emissivity_window >= 0 AND infrared_emissivity_window <= 1)",
    )
    op.create_check_constraint(
        "ck_material_ir_window_energy_sum",
        "material_versions",
        "infrared_emissivity_window IS NULL OR "
        "infrared_emissivity_window + infrared_transmittance <= 1.000001",
    )


def downgrade() -> None:
    op.drop_constraint("ck_material_ir_window_energy_sum", "material_versions", type_="check")
    op.drop_constraint("ck_material_ir_emissivity_window", "material_versions", type_="check")
    op.drop_column("material_versions", "infrared_emissivity_window")
```

### File: `backend/alembic/versions/df85b07c9163_add_stage_4_4_checkpoint_and_analytics_.py`
```python
"""add stage 4 4 checkpoint and analytics fields

Revision ID: df85b07c9163
Revises: e4ee64441802
Create Date: 2026-09-08 20:45:43.789201

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'df85b07c9163'
down_revision: Union[str, Sequence[str], None] = 'e4ee64441802'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('global_city_results', sa.Column('completed_month_count', sa.Integer(), server_default='0', nullable=False))
    op.add_column('global_city_results', sa.Column('last_checkpoint_month', sa.Integer(), nullable=True))
    op.add_column('global_city_results', sa.Column('resumed_from_checkpoint', sa.Boolean(), server_default='false', nullable=False))
    op.add_column('global_city_results', sa.Column('last_heartbeat_at', sa.DateTime(timezone=True), nullable=True))
    op.add_column('global_city_results', sa.Column('skin_improvement_p50_c', sa.Float(), nullable=True))
    op.add_column('global_city_results', sa.Column('skin_improvement_p90_c', sa.Float(), nullable=True))
    op.add_column('global_city_results', sa.Column('skin_improvement_p95_c', sa.Float(), nullable=True))
    op.add_column('global_city_results', sa.Column('core_improvement_p50_c', sa.Float(), nullable=True))
    op.add_column('global_city_results', sa.Column('core_improvement_p90_c', sa.Float(), nullable=True))
    op.add_column('global_city_results', sa.Column('core_improvement_p95_c', sa.Float(), nullable=True))
    op.add_column('global_city_results', sa.Column('heatwave_event_count', sa.Integer(), nullable=True))
    op.add_column('global_city_results', sa.Column('longest_heatwave_days', sa.Integer(), nullable=True))
    op.add_column('global_city_results', sa.Column('analytics_json', postgresql.JSONB(astext_type=sa.Text()), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('global_city_results', 'analytics_json')
    op.drop_column('global_city_results', 'longest_heatwave_days')
    op.drop_column('global_city_results', 'heatwave_event_count')
    op.drop_column('global_city_results', 'core_improvement_p95_c')
    op.drop_column('global_city_results', 'core_improvement_p90_c')
    op.drop_column('global_city_results', 'core_improvement_p50_c')
    op.drop_column('global_city_results', 'skin_improvement_p95_c')
    op.drop_column('global_city_results', 'skin_improvement_p90_c')
    op.drop_column('global_city_results', 'skin_improvement_p50_c')
    op.drop_column('global_city_results', 'last_heartbeat_at')
    op.drop_column('global_city_results', 'resumed_from_checkpoint')
    op.drop_column('global_city_results', 'last_checkpoint_month')
    op.drop_column('global_city_results', 'completed_month_count')
    # ### end Alembic commands ###

```

### File: `backend/alembic/versions/e3b8c1d5f702_stage12_ground_facing_emissivity.py`
```python
"""Stage 12: ground-facing longwave emissivity (ADR 0010).

Revision ID: e3b8c1d5f702
Revises: d7e1f3a9b2c4
"""

import sqlalchemy as sa
from alembic import op

revision = "e3b8c1d5f702"
down_revision = "d7e1f3a9b2c4"  # replace with the output of `alembic heads` if different
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "material_versions",
        sa.Column("infrared_emissivity_ground_facing", sa.Float(), nullable=True),
    )
    op.create_check_constraint(
        "ck_material_ir_ground_facing",
        "material_versions",
        "infrared_emissivity_ground_facing IS NULL OR "
        "(infrared_emissivity_ground_facing >= 0 AND infrared_emissivity_ground_facing <= 1)",
    )
    op.create_check_constraint(
        "ck_material_ir_ground_facing_energy_sum",
        "material_versions",
        "infrared_emissivity_ground_facing IS NULL OR "
        "infrared_emissivity_ground_facing + infrared_transmittance <= 1.000001",
    )


def downgrade() -> None:
    op.drop_constraint("ck_material_ir_ground_facing_energy_sum", "material_versions", type_="check")
    op.drop_constraint("ck_material_ir_ground_facing", "material_versions", type_="check")
    op.drop_column("material_versions", "infrared_emissivity_ground_facing")
```

### File: `backend/alembic/versions/e4ee64441802_add_stage_4_2_exposure_and_retry_fields.py`
```python
"""add stage 4 2 exposure and retry fields

Revision ID: e4ee64441802
Revises: 9e0b460c56c3
Create Date: 2026-09-06 03:53:31.078902

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4ee64441802'
down_revision: Union[str, Sequence[str], None] = '9e0b460c56c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('global_city_results', sa.Column('exposure_coverage_percent', sa.Float(), nullable=True))
    op.add_column('global_city_results', sa.Column('sampled_day_count', sa.Integer(), nullable=True))
    op.add_column('global_city_results', sa.Column('eligible_sample_count', sa.Integer(), nullable=True))
    op.add_column('global_city_results', sa.Column('retry_count', sa.Integer(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('global_city_results', 'retry_count')
    op.drop_column('global_city_results', 'eligible_sample_count')
    op.drop_column('global_city_results', 'sampled_day_count')
    op.drop_column('global_city_results', 'exposure_coverage_percent')
    # ### end Alembic commands ###

```

### File: `backend/alembic/versions/f0a1b2c3d4e5_stage9_job_leases_and_checkpoint_provenance.py`
```python
"""stage9 job leases and checkpoint provenance

Revision ID: f0a1b2c3d4e5
Revises: 165a424d6ba1
Create Date: 2026-11-06 10:00:00.000000

* simulation_jobs gains the same lease columns as global_city_results so the
  single-job worker path has the same redelivery / crash guarantees.
* global_city_checkpoints records which model version, parameter fingerprint
  and request hash produced each row. A resumed worker only trusts rows whose
  provenance matches the current batch; legacy rows (NULL) are recomputed.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "f0a1b2c3d4e5"
down_revision: Union[str, Sequence[str], None] = "165a424d6ba1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("simulation_jobs", sa.Column("attempt", sa.Integer(), server_default="0", nullable=False))
    op.add_column("simulation_jobs", sa.Column("lease_owner", sa.String(length=100), nullable=True))
    op.add_column("simulation_jobs", sa.Column("lease_expires_at", sa.DateTime(timezone=True), nullable=True))
    op.add_column("simulation_jobs", sa.Column("last_heartbeat_at", sa.DateTime(timezone=True), nullable=True))
    op.create_index("ix_simulation_jobs_lease_reap", "simulation_jobs", ["status", "lease_expires_at"])

    op.add_column("global_city_checkpoints", sa.Column("model_version", sa.String(length=20), nullable=True))
    op.add_column("global_city_checkpoints", sa.Column("parameter_fingerprint", sa.String(length=64), nullable=True))
    op.add_column("global_city_checkpoints", sa.Column("request_sha256", sa.String(length=64), nullable=True))


def downgrade() -> None:
    op.drop_column("global_city_checkpoints", "request_sha256")
    op.drop_column("global_city_checkpoints", "parameter_fingerprint")
    op.drop_column("global_city_checkpoints", "model_version")

    op.drop_index("ix_simulation_jobs_lease_reap", table_name="simulation_jobs")
    op.drop_column("simulation_jobs", "last_heartbeat_at")
    op.drop_column("simulation_jobs", "lease_expires_at")
    op.drop_column("simulation_jobs", "lease_owner")
    op.drop_column("simulation_jobs", "attempt")
```

### File: `backend/app/__init__.py`
```python

```

### File: `backend/app/api/__init__.py`
```python

```

### File: `backend/app/api/benchmarks.py`
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.simulation import (
    GaggeBenchmarkRequest,
    GaggeBenchmarkResponse,
)
from app.services.gagge_benchmark import run_gagge_benchmark
from app.services.material_resolution import resolve_request_materials


router = APIRouter(
    prefix="/api/v1/benchmarks",
    tags=["benchmarks"],
)


@router.post(
    "/gagge",
    response_model=GaggeBenchmarkResponse,
)
def compare_with_gagge(
    request: GaggeBenchmarkRequest,
    session: Session = Depends(get_db),
) -> GaggeBenchmarkResponse:
    request = resolve_request_materials(
        session, request, fields=("material",)
    )

    try:
        return run_gagge_benchmark(request)
    except (ValueError, RuntimeError) as error:
        raise HTTPException(
            status_code=500,
            detail=f"Gagge benchmark calculation failed：{error}",
        ) from error
```

### File: `backend/app/api/errors.py`
```python
# app/api/errors.py
"""Application-wide exception handlers."""

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.services.material_resolution import MaterialResolutionError


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(MaterialResolutionError)
    async def handle_material_resolution_error(
        _: Request,
        error: MaterialResolutionError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            content={"detail": error.to_detail()},
        )
```

### File: `backend/app/api/global_batches.py`
```python
from datetime import (
    datetime,
    timezone,
)
import asyncio
import json

import anyio
from celery import group
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    status,
    Request,
)
from fastapi.responses import Response,StreamingResponse
from sqlalchemy import (
    delete,
    func,
    select,
)
from sqlalchemy.orm import (
    Session,
    selectinload,
)

from app.core.cities import (
    get_city,
    list_cities,
)
from app.db.session import get_db, SessionLocal
from app.models.global_batch import (
    GlobalBatchJob,
    GlobalCityCheckpoint,
    GlobalCityResult,
)
from app.services.job_state import (
    CityStatus,
    assert_batch_transition,
    assert_city_transition,
    BatchStatus,
)

from app.services.leases import db_now
from app.services.stored_requests import load_stored_request
from app.schemas.global_batch import (
    GlobalBatchCreate,
    GlobalBatchDetail,
    GlobalBatchEstimateResponse,
    GlobalBatchListResponse,
    GlobalBatchResponse,
    CityCheckpointListResponse, 
    GlobalBatchProgressEvent
)
from app.services.annual_sampling import (
    estimate_sample_count,
)
from app.services.execution_profile import (
    resolve_execution_profile,
    resolve_queue_name,
)
from app.services.global_batch_export import (
    build_batch_export_zip,
    build_batch_geojson,
)
from app.services.global_batch_service import (
    batch_to_detail,
    batch_to_response,
    refresh_batch_status,
    batch_progress_event,
    city_checkpoints_to_response,
    load_checkpoint_months,
)
from app.services.material_resolution import (
    linked_material_version_ids,
    resolve_request_materials,
)
from app.worker.celery_app import celery_app
from app.worker.tasks import (
    run_global_city_analysis_task,
)

router = APIRouter(
    prefix="/api/v1/global-batches",
    tags=["global-batches"],
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def load_batch(
    session: Session,
    batch_id: str,
) -> GlobalBatchJob | None:
    return session.scalar(
        select(GlobalBatchJob)
        .options(
            selectinload(
                GlobalBatchJob.city_results
            )
        )
        .where(
            GlobalBatchJob.id == batch_id
        )
    )


def submit_city_tasks(
    *,
    city_results: list[GlobalCityResult],
    queue_name: str,
):
    celery_group = group(
        run_global_city_analysis_task.s(
            result.id
        ).set(
            queue=queue_name
        )
        for result in city_results
    )

    return celery_group.apply_async()


@router.get("/cities")
def get_supported_cities() -> dict:
    return {
        "items": [
            {
                "id": city.id,
                "name": city.name,
                "country": city.country,
                "latitude": city.latitude,
                "longitude": city.longitude,
                "elevation_m": city.elevation_m,
                "timezone": city.timezone,
                "climate_type": city.climate_type,
            }
            for city in list_cities()
        ]
    }


@router.post(
    "/estimate",
    response_model=GlobalBatchEstimateResponse,
)
def estimate_global_batch(
    request: GlobalBatchCreate,
) -> GlobalBatchEstimateResponse:
    samples_per_city = estimate_sample_count(
        request
    )

    city_count = len(request.city_ids)

    month_count = (
        request.end_month
        - request.start_month
        + 1
    )

    total_samples = (
        samples_per_city
        * city_count
    )

    resolved_profile = resolve_execution_profile(
        request
    )

    resolved_queue = resolve_queue_name(
        request
    )

    heatwave_analysis_available = (
        request.enable_heatwave_analysis
        and request.analysis_resolution == "daily"
        and request.daily_stride_days == 1
    )

    return GlobalBatchEstimateResponse(
        city_count=city_count,
        month_count=month_count,
        samples_per_city=samples_per_city,
        total_samples=total_samples,
        thermal_simulation_count=(
            total_samples * 2
        ),
        estimated_weather_requests=(
            city_count * month_count
        ),
        analysis_resolution=(
            request.analysis_resolution
        ),
        resolved_execution_profile=(
            resolved_profile
        ),
        resolved_queue=resolved_queue,
        checkpoint_count_per_city=month_count,
        heatwave_analysis_available=(
            heatwave_analysis_available
        ),
    )


@router.post(
    "",
    response_model=GlobalBatchResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
def create_global_batch(
    request: GlobalBatchCreate,
    session: Session = Depends(get_db),
) -> GlobalBatchResponse:
    cities = []

    for city_id in request.city_ids:
        try:
            cities.append(
                get_city(city_id)
            )
        except ValueError as error:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                detail=str(error),
            ) from error

    request = resolve_request_materials(session, request)
    control_version_id, rc_version_id = linked_material_version_ids(request)

    queue_name = resolve_queue_name(request)

    batch = GlobalBatchJob(
        status="queued",
        stage="creating_city_tasks",
        progress=0,
        total_city_count=len(cities),
        request_json=request.model_dump(mode="json"),
        control_material_version_id=control_version_id,
        rc_material_version_id=rc_version_id,
    )

    session.add(batch)
    session.flush()

    city_results: list[GlobalCityResult] = []

    for city in cities:
        city_result = GlobalCityResult(
            batch_id=batch.id,
            city_id=city.id,
            city_name=city.name,
            country=city.country,
            latitude=city.latitude,
            longitude=city.longitude,
            status="queued",
            stage="queued",
            progress=0,
            completed_month_count=0,
            resumed_from_checkpoint=False,
        )

        session.add(city_result)
        city_results.append(city_result)

    session.commit()

    try:
        group_result = submit_city_tasks(
            city_results=city_results,
            queue_name=queue_name,
        )

        batch.celery_group_id = group_result.id
        batch.stage = "queued"

        for city_result, async_result in zip(
            city_results,
            group_result.results,
            strict=True,
        ):
            city_result.celery_task_id = (
                async_result.id
            )

        session.commit()
        session.refresh(batch)

    except Exception as error:
        now = utc_now()

        batch.status = "failed"
        batch.stage = "queue_submission_failed"
        batch.error_message = str(error)[:4000]
        batch.completed_at = now

        for result in city_results:
            result.status = "failed"
            result.stage = "queue_submission_failed"
            result.error_message = str(
                error
            )[:4000]
            result.completed_at = now

        session.commit()

        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=(
                "Unable to submit global batch "
                f"to Celery: {error}"
            ),
        ) from error

    return batch_to_response(batch)


@router.get(
    "",
    response_model=GlobalBatchListResponse,
)
def list_global_batches(
    limit: int = Query(
        default=20,
        ge=1,
        le=100,
    ),
    offset: int = Query(
        default=0,
        ge=0,
    ),
    session: Session = Depends(get_db),
) -> GlobalBatchListResponse:
    total = session.scalar(
        select(func.count())
        .select_from(GlobalBatchJob)
    ) or 0

    batches = session.scalars(
        select(GlobalBatchJob)
        .order_by(
            GlobalBatchJob.created_at.desc()
        )
        .offset(offset)
        .limit(limit)
    ).all()

    return GlobalBatchListResponse(
        items=[
            batch_to_response(batch)
            for batch in batches
        ],
        total=total,
        limit=limit,
        offset=offset,
    )


@router.get("/{batch_id}", response_model=GlobalBatchDetail)
def get_global_batch(batch_id: str, session: Session = Depends(get_db)) -> GlobalBatchDetail:
    batch = load_batch(session, batch_id)
    if batch is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Global batch not found")
    return batch_to_detail(
        batch,
        checkpoint_months=load_checkpoint_months(session, batch.id),
        now=db_now(session),
    )

PROGRESS_COLUMNS = (
    GlobalCityResult.id, GlobalCityResult.batch_id, GlobalCityResult.city_id,
    GlobalCityResult.status, GlobalCityResult.stage, GlobalCityResult.progress,
    GlobalCityResult.retry_count, GlobalCityResult.completed_month_count,
    GlobalCityResult.last_checkpoint_month, GlobalCityResult.last_heartbeat_at,
    GlobalCityResult.lease_owner, GlobalCityResult.lease_expires_at,
    GlobalCityResult.error_message,
)

TERMINAL_BATCH_STATUSES = {"completed", "partial_completed", "failed", "cancelled"}


@router.get(
    "/{batch_id}/cities/{city_result_id}/checkpoints",
    response_model=CityCheckpointListResponse,
)
def list_city_checkpoints(
    batch_id: str,
    city_result_id: str,
    session: Session = Depends(get_db),
) -> CityCheckpointListResponse:
    batch = session.get(GlobalBatchJob, batch_id)
    if batch is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Global batch not found")

    city_result = session.scalar(
        select(GlobalCityResult).where(
            GlobalCityResult.id == city_result_id,
            GlobalCityResult.batch_id == batch_id,
        )
    )
    if city_result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="City result not found")

    return city_checkpoints_to_response(session, batch=batch, city_result=city_result)


def load_batch_progress_snapshot(batch_id: str) -> GlobalBatchProgressEvent | None:
    with SessionLocal() as session:
        batch = session.scalar(
            select(GlobalBatchJob)
            .options(selectinload(GlobalBatchJob.city_results).load_only(*PROGRESS_COLUMNS))
            .where(GlobalBatchJob.id == batch_id)
        )
        if batch is None:
            return None
        return batch_progress_event(batch, load_checkpoint_months(session, batch_id), now=db_now(session))


@router.get("/{batch_id}/events")
async def global_batch_events(batch_id: str, request: Request) -> StreamingResponse:
    """Server-sent progress. Emits ``progress`` when the lightweight snapshot
    changes and a final ``terminal`` event; clients fetch the full detail
    themselves when city counts change."""
    initial = await anyio.to_thread.run_sync(load_batch_progress_snapshot, batch_id)
    if initial is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Global batch not found")

    async def event_generator():
        previous_payload: str | None = None

        while True:
            if await request.is_disconnected():
                break

            snapshot = await anyio.to_thread.run_sync(load_batch_progress_snapshot, batch_id)
            if snapshot is None:
                yield 'event: error\ndata: {"detail":"batch not found"}\n\n'
                break

            payload = json.dumps(snapshot.model_dump(mode="json"), ensure_ascii=False)

            if payload != previous_payload:
                yield f"event: progress\ndata: {payload}\n\n"
                previous_payload = payload

            if snapshot.batch.status in TERMINAL_BATCH_STATUSES:
                yield f"event: terminal\ndata: {payload}\n\n"
                break

            await asyncio.sleep(2)

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )

@router.post(
    "/{batch_id}/cancel",
    response_model=GlobalBatchResponse,
)
def cancel_global_batch(
    batch_id: str,
    session: Session = Depends(get_db),
) -> GlobalBatchResponse:
    batch = load_batch(
        session,
        batch_id,
    )

    if batch is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Global batch not found",
        )

    if batch.status in {
        "completed",
        "partial_completed",
        "failed",
        "cancelled",
    }:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "Batch in terminal state "
                "cannot be cancelled"
            ),
        )

    now = utc_now()

    batch.status = "cancelling"
    batch.stage = (
        "waiting_for_cooperative_cancel"
    )
    batch.cancel_requested_at = batch.cancel_requested_at or now

    for result in batch.city_results:
        if result.status == "queued":
            result.status = "cancelled"
            result.stage = "cancelled"
            result.progress = 100
            result.last_heartbeat_at = now
            result.completed_at = now

        if (
            result.celery_task_id
            and result.status != "completed"
        ):
            celery_app.control.revoke(
                result.celery_task_id,
                terminate=False,
            )

    session.commit()

    refresh_batch_status(
        session,
        batch.id,
    )

    session.refresh(batch)

    return batch_to_response(batch)


@router.get(
    "/{batch_id}/geojson",
)
def get_global_batch_geojson(
    batch_id: str,
    session: Session = Depends(get_db),
) -> dict:
    batch = load_batch(
        session,
        batch_id,
    )

    if batch is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Global batch not found",
        )

    return build_batch_geojson(batch)


@router.get(
    "/{batch_id}/export",
)
def export_global_batch(
    batch_id: str,
    session: Session = Depends(get_db),
) -> Response:
    batch = load_batch(
        session,
        batch_id,
    )

    if batch is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Global batch not found",
        )

    export_content = build_batch_export_zip(
        batch
    )

    filename = (
        f"global-climate-adaptation-"
        f"{batch.id}.zip"
    )

    return Response(
        content=export_content,
        media_type="application/zip",
        headers={
            "Content-Disposition": (
                f'attachment; filename="{filename}"'
            ),
        },
    )


@router.post(
    "/{batch_id}/retry-failed",
    response_model=GlobalBatchResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
def retry_failed_cities(
    batch_id: str,
    session: Session = Depends(get_db),
) -> GlobalBatchResponse:
    batch = load_batch(
        session,
        batch_id,
    )

    if batch is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Global batch not found",
        )

    if batch.status not in {
        "failed",
        "partial_completed",
    }:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "Only failed or partially completed "
                "batches can be retried"
            ),
        )

    failed_results = [
        result
        for result in batch.city_results
        if result.status == "failed"
    ]

    if not failed_results:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "The batch contains no failed cities"
            ),
        )

    request = load_stored_request(GlobalBatchCreate, batch.request_json)

    queue_name = resolve_queue_name(
        request
    )

    now = utc_now()

    for result in failed_results:
        assert_city_transition(result.status, CityStatus.QUEUED)

        has_checkpoints = session.scalar(
            select(func.count()).select_from(GlobalCityCheckpoint)
            .where(GlobalCityCheckpoint.city_result_id == result.id)
        ) or 0

        result.status = CityStatus.QUEUED
        result.stage = "queued_for_retry"
        result.progress = 0
        result.retry_count += 1

        result.error_message = None
        result.completed_at = None
        result.last_heartbeat_at = None
        result.lease_owner = None
        result.lease_expires_at = None

        for column in (
            "climate_adaptation_rate_percent", "exposure_coverage_percent",
            "annual_average_skin_improvement_c", "annual_average_core_improvement_c",
            "maximum_skin_improvement_c", "effective_cooling_hours",
            "sampled_day_count", "eligible_sample_count",
            "evaluated_weighted_days", "beneficial_weighted_days",
            "skin_improvement_p50_c", "skin_improvement_p90_c", "skin_improvement_p95_c",
            "core_improvement_p50_c", "core_improvement_p90_c", "core_improvement_p95_c",
            "heatwave_event_count", "longest_heatwave_days", "analytics_json",
        ):
            setattr(result, column, None)

        if request.resume_from_checkpoint:
            # Hint only; the worker decides after checking provenance.
            result.resumed_from_checkpoint = bool(result.monthly_json) or has_checkpoints > 0
        else:
            # The user asked for a clean recomputation: remove the durable rows
            # so the worker cannot resume from them.
            session.execute(
                delete(GlobalCityCheckpoint).where(GlobalCityCheckpoint.city_result_id == result.id)
            )
            result.monthly_json = None
            result.completed_month_count = 0
            result.last_checkpoint_month = None
            result.resumed_from_checkpoint = False
            result.started_at = None

    assert_batch_transition(batch.status, BatchStatus.RUNNING)
    batch.status = BatchStatus.RUNNING
    batch.stage = "retrying_failed_cities"

    already_processed_count = (
        batch.total_city_count
        - len(failed_results)
    )

    batch.progress = round(
        already_processed_count
        / max(1, batch.total_city_count)
        * 100
    )

    batch.failed_city_count = 0
    batch.completed_at = None
    batch.error_message = None
    batch.started_at = (
        batch.started_at or now
    )

    session.commit()

    try:
        group_result = submit_city_tasks(
            city_results=failed_results,
            queue_name=queue_name,
        )

        batch.celery_group_id = group_result.id

        for result, async_result in zip(
            failed_results,
            group_result.results,
            strict=True,
        ):
            result.celery_task_id = (
                async_result.id
            )

        session.commit()
        session.refresh(batch)

    except Exception as error:
        batch.status = "partial_completed"
        batch.stage = "retry_submission_failed"
        batch.error_message = str(
            error
        )[:4000]

        for result in failed_results:
            result.status = "failed"
            result.stage = (
                "retry_submission_failed"
            )
            result.error_message = str(
                error
            )[:4000]
            result.completed_at = now

        session.commit()

        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=(
                "Unable to submit retry tasks: "
                f"{error}"
            ),
        ) from error

    return batch_to_response(batch)
```

### File: `backend/app/api/materials.py`
```python
from typing import Annotated

from fastapi import (
    APIRouter, Depends, File, Form, HTTPException, Query, Response, UploadFile, status,
)

from sqlalchemy import delete, func, or_, select

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import (
    Session,
    selectinload,
)

from app.models.global_batch import GlobalBatchJob
from app.models.optimization_job import OptimizationJob
from app.models.simulation_job import SimulationJob

from app.db.session import get_db
from app.models.material import (
    Material,
    MaterialSpectrum,
    MaterialVersion,
)
from app.schemas.material import (
    MaterialCreate,
    MaterialListItem,
    MaterialListResponse,
    MaterialResponse,
    MaterialUpdate,
    MaterialVersionCreate,
    MaterialVersionResponse,
    SpectrumResponse,
    SpectrumSummary,
    MaterialVersionListItem,
    MaterialVersionListResponse,
)
from app.services.material_resolution import (
    MaterialVersionNotFoundError,
    load_material_version,
    material_input_from_version,
)
from app.schemas.simulation import MaterialInput
from app.services.spectrum_parser import (
    parse_spectrum_csv,
)

from app.schemas.material import SpectrumBandSummary
from app.services.planck import EMISSIVITY_REFERENCE_K
from app.services.spectral_summary import summarize_ir_spectrum

router = APIRouter(
    prefix="/api/v1/materials",
    tags=["materials"],
)


def load_material(
    session: Session,
    material_id: str,
) -> Material | None:
    return session.scalar(
        select(Material)
        .options(
            selectinload(Material.versions)
            .selectinload(MaterialVersion.spectra)
        )
        .where(Material.id == material_id)
    )

def version_column_values(request: MaterialVersionCreate) -> dict:
    """Map the API payload to MaterialVersion column names."""
    values = request.model_dump(mode="json")
    values["parameter_sources_json"] = values.pop("parameter_sources")
    return values


@router.get(
    "/versions",
    response_model=MaterialVersionListResponse,
)
def list_material_versions(
    include_archived: bool = False,
    material_id: str | None = None,
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
    session: Session = Depends(get_db),
) -> MaterialVersionListResponse:
    """Flat list of versions for simulation-form pickers (Stage 4)."""
    filters = []

    if not include_archived:
        filters.append(Material.is_archived.is_(False))

    if material_id:
        filters.append(MaterialVersion.material_id == material_id)

    total = session.scalar(
        select(func.count())
        .select_from(MaterialVersion)
        .join(MaterialVersion.material)
        .where(*filters)
    ) or 0

    versions = session.scalars(
        select(MaterialVersion)
        .join(MaterialVersion.material)
        .options(selectinload(MaterialVersion.material))
        .where(*filters)
        .order_by(
            Material.name.asc(),
            MaterialVersion.version_number.desc(),
        )
        .offset(offset)
        .limit(limit)
    ).all()

    return MaterialVersionListResponse(
        items=[
            MaterialVersionListItem(
                id=version.id,
                material_id=version.material_id,
                material_name=version.material.name,
                material_slug=version.material.slug,
                version_number=version.version_number,
                mode=version.mode,
                clothing_insulation_clo=version.clothing_insulation_clo,
                evaporative_resistance_m2pa_w=version.evaporative_resistance_m2pa_w,
                clothing_area_factor=version.clothing_area_factor,
                solar_reflectance=version.solar_reflectance,
                solar_transmittance=version.solar_transmittance,
                infrared_emissivity=version.infrared_emissivity,
                infrared_transmittance=version.infrared_transmittance,
                source_type=version.source_type,
                is_archived=version.material.is_archived,
                created_at=version.created_at,
                infrared_emissivity_window=version.infrared_emissivity_window,
                infrared_emissivity_ground_facing=version.infrared_emissivity_ground_facing,
            )
            for version in versions
        ],
        total=total,
        limit=limit,
        offset=offset,
    )

@router.post(
    "",
    response_model=MaterialResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_material(
    request: MaterialCreate,
    session: Session = Depends(get_db),
) -> MaterialResponse:
    material = Material(
        name=request.name,
        slug=request.slug,
        description=request.description,
        institution=request.institution,
    )

    version = MaterialVersion(
        version_number=1,
        **version_column_values(request.initial_version),
    )

    material.versions.append(version)
    session.add(material)

    try:
        session.commit()
    except IntegrityError as error:
        session.rollback()

        raise HTTPException(
            status_code=409,
            detail="The material slug already exists",
        ) from error

    created = load_material(
        session,
        material.id,
    )

    if created is None:
        raise HTTPException(
            status_code=500,
            detail="Failed to reload the created material",
        )

    return MaterialResponse.model_validate(
        created
    )


@router.get(
    "",
    response_model=MaterialListResponse,
)
def list_materials(
    include_archived: bool = False,
    search: str | None = None,
    limit: int = Query(
        default=20,
        ge=1,
        le=100,
    ),
    offset: int = Query(
        default=0,
        ge=0,
    ),
    session: Session = Depends(get_db),
) -> MaterialListResponse:
    filters = []

    if not include_archived:
        filters.append(
            Material.is_archived.is_(False)
        )

    if search:
        filters.append(
            Material.name.ilike(
                f"%{search.strip()}%"
            )
        )

    total = session.scalar(
        select(func.count())
        .select_from(Material)
        .where(*filters)
    ) or 0

    materials = session.scalars(
        select(Material)
        .options(
            selectinload(Material.versions)
        )
        .where(*filters)
        .order_by(Material.created_at.desc())
        .offset(offset)
        .limit(limit)
    ).all()

    items = []

    for material in materials:
        latest_version = max(
            (
                version.version_number
                for version in material.versions
            ),
            default=None,
        )

        items.append(
            MaterialListItem(
                id=material.id,
                name=material.name,
                slug=material.slug,
                institution=material.institution,
                is_archived=material.is_archived,
                latest_version_number=latest_version,
                created_at=material.created_at,
            )
        )

    return MaterialListResponse(
        items=items,
        total=total,
        limit=limit,
        offset=offset,
    )


@router.get(
    "/{material_id}",
    response_model=MaterialResponse,
)
def get_material(
    material_id: str,
    session: Session = Depends(get_db),
) -> MaterialResponse:
    material = load_material(
        session,
        material_id,
    )

    if material is None:
        raise HTTPException(
            status_code=404,
            detail="Material not found",
        )

    return MaterialResponse.model_validate(
        material
    )


@router.patch("/{material_id}", response_model=MaterialResponse)
def update_material(
    material_id: str,
    request: MaterialUpdate,
    session: Session = Depends(get_db),
) -> MaterialResponse:
    material = session.get(Material, material_id)
    if material is None:
        raise HTTPException(status_code=404, detail="Material not found")

    for field, value in request.model_dump(exclude_unset=True).items():
        setattr(material, field, value)

    try:
        session.commit()
    except IntegrityError as error:
        session.rollback()
        raise HTTPException(
            status_code=409, detail="Material update conflicts with existing data"
        ) from error

    return MaterialResponse.model_validate(load_material(session, material_id))

def count_material_references(session: Session, material_id: str) -> dict[str, int]:
    """Jobs whose control, RC, or optimization base garment used any version of this material."""
    version_ids = select(MaterialVersion.id).where(MaterialVersion.material_id == material_id)

    def count(model) -> int:
        return session.scalar(
            select(func.count()).select_from(model).where(
                or_(
                    model.control_material_version_id.in_(version_ids),
                    model.rc_material_version_id.in_(version_ids),
                )
            )
        ) or 0

    optimization_count = session.scalar(
        select(func.count()).select_from(OptimizationJob).where(
            or_(
                OptimizationJob.control_material_version_id.in_(version_ids),
                OptimizationJob.base_material_version_id.in_(version_ids),
            )
        )
    ) or 0

    return {
        "simulation_job_count": count(SimulationJob),
        "global_batch_count": count(GlobalBatchJob),
        "optimization_job_count": optimization_count,
    }


@router.delete(
    "/{material_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
)
def delete_material(material_id: str, session: Session = Depends(get_db)) -> Response:
    """Hard delete, only when no simulation references any of its versions.

    The job FKs are ON DELETE SET NULL, so deleting a referenced material would
    silently detach provenance. Referenced materials must be archived instead.
    """
    if session.get(Material, material_id) is None:
        raise HTTPException(status_code=404, detail="Material not found")

    references = count_material_references(session, material_id)
    if (
        references["simulation_job_count"]
        or references["global_batch_count"]
        or references["optimization_job_count"]
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                "code": "MATERIAL_IN_USE",
                "message": (
                    "Versions of this material are referenced by "
                    f"{references['simulation_job_count']} simulation job(s), "
                    f"{references['global_batch_count']} global batch(es), and "
                    f"{references['optimization_job_count']} optimization job(s). "
                    "Archive it instead: archived materials are hidden from lists "
                    "and pickers but keep their provenance."
                ),
                **references,
            },
        )

    # Versions and spectra go with it via ON DELETE CASCADE.
    session.execute(delete(Material).where(Material.id == material_id))
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post(
    "/{material_id}/versions",
    response_model=MaterialVersionResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_material_version(
    material_id: str,
    request: MaterialVersionCreate,
    session: Session = Depends(get_db),
) -> MaterialVersionResponse:
    material = session.get(
        Material,
        material_id,
    )

    if material is None:
        raise HTTPException(
            status_code=404,
            detail="Material not found",
        )

    latest_version = session.scalar(
        select(
            func.max(
                MaterialVersion.version_number
            )
        )
        .where(
            MaterialVersion.material_id
            == material_id
        )
    ) or 0

    version = MaterialVersion(
        material_id=material_id,
        version_number=latest_version + 1,
        **version_column_values(request),
    )

    session.add(version)
    session.commit()
    session.refresh(version)

    return MaterialVersionResponse.model_validate(
        version
    )


@router.get(
    "/versions/{version_id}/simulation-input",
    response_model=MaterialInput,
)
def material_version_to_simulation_input(
    version_id: str,
    session: Session = Depends(get_db),
) -> MaterialInput:
    try:
        version = load_material_version(session, version_id)
    except MaterialVersionNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail="Material version not found",
        ) from error

    # MaterialVersionInvalidError propagates to the global 422 handler.
    return material_input_from_version(version)


@router.post(
    "/versions/{version_id}/spectra",
    response_model=SpectrumResponse,
)
async def upload_material_spectrum(
    version_id: str,
    spectrum_type: Annotated[
        str,
        Form(),
    ],
    file: Annotated[
        UploadFile,
        File(),
    ],
    session: Session = Depends(get_db),
) -> SpectrumResponse:
    allowed_types = {
        "solar_reflectance",
        "solar_transmittance",
        "mir_emissivity",
        "mir_transmittance",
    }

    if spectrum_type not in allowed_types:
        raise HTTPException(
            status_code=422,
            detail="Unsupported spectrum type",
        )

    version = session.get(
        MaterialVersion,
        version_id,
    )

    if version is None:
        raise HTTPException(
            status_code=404,
            detail="Material version not found",
        )

    if not file.filename:
        raise HTTPException(
            status_code=422,
            detail="Missing filename",
        )

    if not file.filename.lower().endswith(
        ".csv"
    ):
        raise HTTPException(
            status_code=422,
            detail="Only CSV files are accepted",
        )

    file_bytes = await file.read()

    try:
        parsed = parse_spectrum_csv(
            file_bytes
        )
    except ValueError as error:
        raise HTTPException(
            status_code=422,
            detail=str(error),
        ) from error

    spectrum = session.scalar(
        select(MaterialSpectrum)
        .where(
            MaterialSpectrum.material_version_id
            == version_id,
            MaterialSpectrum.spectrum_type
            == spectrum_type,
        )
    )

    if spectrum is None:
        spectrum = MaterialSpectrum(
            material_version_id=version_id,
            spectrum_type=spectrum_type,
            wavelength_unit="um",
            points_json=parsed.points,
            point_count=len(parsed.points),
            minimum_wavelength_um=(
                parsed.minimum_wavelength_um
            ),
            maximum_wavelength_um=(
                parsed.maximum_wavelength_um
            ),
            original_filename=file.filename,
            file_checksum_sha256=(
                parsed.checksum_sha256
            ),
        )

        session.add(spectrum)
    else:
        spectrum.points_json = parsed.points
        spectrum.point_count = len(
            parsed.points
        )
        spectrum.minimum_wavelength_um = (
            parsed.minimum_wavelength_um
        )
        spectrum.maximum_wavelength_um = (
            parsed.maximum_wavelength_um
        )
        spectrum.original_filename = (
            file.filename
        )
        spectrum.file_checksum_sha256 = (
            parsed.checksum_sha256
        )

    session.commit()
    session.refresh(spectrum)

    return SpectrumResponse(
        summary=SpectrumSummary.model_validate(
            spectrum
        ),
        points=parsed.points,
    )


@router.get(
    "/versions/{version_id}/spectra/{spectrum_type}",
    response_model=SpectrumResponse,
)
def get_material_spectrum(
    version_id: str,
    spectrum_type: str,
    session: Session = Depends(get_db),
) -> SpectrumResponse:
    spectrum = session.scalar(
        select(MaterialSpectrum)
        .where(
            MaterialSpectrum.material_version_id
            == version_id,
            MaterialSpectrum.spectrum_type
            == spectrum_type,
        )
    )

    if spectrum is None:
        raise HTTPException(
            status_code=404,
            detail="Spectrum data not found",
        )

    return SpectrumResponse(
        summary=SpectrumSummary.model_validate(
            spectrum
        ),
        points=spectrum.points_json,
    )

@router.get(
    "/versions/{version_id}/spectra/{spectrum_type}/band-summary",
    response_model=SpectrumBandSummary,
)
def get_spectrum_band_summary(
    version_id: str,
    spectrum_type: str,
    temperature_k: float = Query(default=EMISSIVITY_REFERENCE_K, ge=200.0, le=400.0),
    session: Session = Depends(get_db),
) -> SpectrumBandSummary:
    if spectrum_type not in {"mir_emissivity", "mir_transmittance"}:
        raise HTTPException(status_code=422, detail="Band summary is defined for IR spectra only")

    spectrum = session.scalar(
        select(MaterialSpectrum).where(
            MaterialSpectrum.material_version_id == version_id,
            MaterialSpectrum.spectrum_type == spectrum_type,
        )
    )
    if spectrum is None:
        raise HTTPException(status_code=404, detail="Spectrum data not found")

    return summarize_ir_spectrum(
        spectrum.points_json, spectrum_type=spectrum_type, temperature_k=temperature_k
    )
```

### File: `backend/app/api/model.py`
```python
"""Read-only endpoints exposing model constants, defaults and input metadata."""

from fastapi import APIRouter, HTTPException

from app.schemas.environment import EnvironmentAssumptions
from app.schemas.provenance import (
    MaterialFieldManifest,
    ModelMetadata,
    ModelParameter,
    ModelParameterManifest,
)
from app.services.material_fields import build_material_field_manifest
from app.services.model_parameters import (
    MODEL_PARAMETERS,
    build_model_metadata,
    build_model_parameter_manifest,
)
from app.schemas.environment import ENVIRONMENT_PRESETS, EnvironmentAssumptions, preset_assumptions


router = APIRouter(prefix="/api/v1/model", tags=["model"])


@router.get("/metadata", response_model=ModelMetadata)
def get_model_metadata() -> ModelMetadata:
    """Version and fingerprint of the active parameter set."""
    return build_model_metadata()


@router.get("/parameters", response_model=ModelParameterManifest)
def get_model_parameters() -> ModelParameterManifest:
    return build_model_parameter_manifest()


@router.get("/parameters/{name}", response_model=ModelParameter)
def get_model_parameter(name: str) -> ModelParameter:
    parameter = MODEL_PARAMETERS.get(name)

    if parameter is None:
        raise HTTPException(
            status_code=404,
            detail=f"Unknown model parameter: {name}",
        )

    return parameter


@router.get("/material-fields", response_model=MaterialFieldManifest)
def get_material_fields() -> MaterialFieldManifest:
    """Bounds, units, defaults and derivation rules of MaterialInput."""
    return build_material_field_manifest()


@router.get(
    "/environment-assumptions/defaults",
    response_model=EnvironmentAssumptions,
)
def get_default_environment_assumptions() -> EnvironmentAssumptions:
    return EnvironmentAssumptions()

@router.get(
    "/environment-assumptions/presets",
    response_model=dict[str, EnvironmentAssumptions],
)
def get_environment_presets() -> dict[str, EnvironmentAssumptions]:
    return {name: preset_assumptions(name) for name in ENVIRONMENT_PRESETS}
```

### File: `backend/app/api/ops.py`
```python
"""Operational health (Stage 8). Read-only; safe to poll every few seconds."""

from __future__ import annotations

import logging

from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.time import utc_now
from app.db.session import get_db
from app.models.global_batch import GlobalBatchJob, GlobalCityResult
from app.schemas.ops import LeaseSummary, OpsStatusResponse, WorkerStatus
from app.worker.celery_app import celery_app


logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/ops", tags=["ops"])

INSPECT_TIMEOUT_SECONDS = 1.0


def inspect_workers(timeout: float = INSPECT_TIMEOUT_SECONDS) -> tuple[bool, list[WorkerStatus]]:
    """Ping Celery workers. Broker failures are reported, never raised."""
    try:
        inspector = celery_app.control.inspect(timeout=timeout)
        pong = inspector.ping() or {}
        active = inspector.active() or {}
        reserved = inspector.reserved() or {}
    except Exception as error:  # noqa: BLE001 - kombu raises many transport-specific types
        logger.warning("Celery inspect failed: %s", error)
        return False, []

    workers = [
        WorkerStatus(
            name=name,
            active_task_count=len(active.get(name, []) or []),
            reserved_task_count=len(reserved.get(name, []) or []),
        )
        for name in sorted(pong)
    ]
    return True, workers


def summarize_leases(session: Session) -> LeaseSummary:
    now = utc_now()

    city_counts = dict(
        session.execute(
            select(GlobalCityResult.status, func.count())
            .group_by(GlobalCityResult.status)
        ).all()
    )

    live = session.scalar(
        select(func.count()).select_from(GlobalCityResult).where(
            GlobalCityResult.lease_owner.is_not(None),
            GlobalCityResult.lease_expires_at > now,
        )
    ) or 0

    expired = session.scalar(
        select(func.count()).select_from(GlobalCityResult).where(
            GlobalCityResult.status == "running",
            GlobalCityResult.lease_expires_at.is_not(None),
            GlobalCityResult.lease_expires_at <= now,
        )
    ) or 0

    batch_counts = dict(
        session.execute(
            select(GlobalBatchJob.status, func.count()).group_by(GlobalBatchJob.status)
        ).all()
    )

    return LeaseSummary(
        running_cities=city_counts.get("running", 0),
        queued_cities=city_counts.get("queued", 0),
        live_leases=live,
        expired_leases=expired,
        running_batches=batch_counts.get("running", 0),
        cancelling_batches=batch_counts.get("cancelling", 0),
    )


@router.get("/status", response_model=OpsStatusResponse)
def ops_status(session: Session = Depends(get_db)) -> OpsStatusResponse:
    broker_reachable, workers = inspect_workers()

    return OpsStatusResponse(
        checked_at=utc_now(),
        broker_reachable=broker_reachable,
        worker_count=len(workers),
        workers=workers,
        leases=summarize_leases(session),
        lease_ttl_seconds=settings.CITY_LEASE_TTL_SECONDS,
        heartbeat_interval_seconds=settings.CITY_HEARTBEAT_SECONDS,
        reaper_interval_seconds=settings.LEASE_REAPER_INTERVAL_SECONDS,
        worst_case_recovery_seconds=(
            settings.CITY_LEASE_TTL_SECONDS + settings.LEASE_REAPER_INTERVAL_SECONDS
        ),
    )
```

### File: `backend/app/api/optimizations.py`
```python
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.cities import get_city
from app.core.time import utc_now
from app.db.session import get_db
from app.models.optimization_job import OptimizationJob
from app.schemas.optimization import (
    OptimizationCreate,
    OptimizationEstimate,
    OptimizationJobDetail,
    OptimizationJobListResponse,
    OptimizationJobResponse,
)
from app.services.leases import db_now
from app.services.material_resolution import resolve_request_materials
from app.services.optimization.jobs import optimization_to_detail, optimization_to_response
from app.services.optimization.search_space import build_search_space
from app.services.optimization.service import estimate_optimization
from app.worker.celery_app import celery_app
from app.worker.optimization_tasks import run_optimization_task


router = APIRouter(prefix="/api/v1/optimizations", tags=["optimizations"])

TERMINAL = {"completed", "failed", "cancelled"}
MATERIAL_FIELDS = ("control_material", "base_material")


def _validate(request: OptimizationCreate) -> None:
    try:
        get_city(request.city_id)
        build_search_space(request)
    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail=str(error)) from error


@router.post("/estimate", response_model=OptimizationEstimate)
def estimate(request: OptimizationCreate, session: Session = Depends(get_db)) -> OptimizationEstimate:
    request = resolve_request_materials(session, request, fields=MATERIAL_FIELDS)
    _validate(request)
    return estimate_optimization(request)


@router.post("", response_model=OptimizationJobResponse, status_code=status.HTTP_202_ACCEPTED)
def create_optimization(request: OptimizationCreate, session: Session = Depends(get_db)) -> OptimizationJobResponse:
    request = resolve_request_materials(session, request, fields=MATERIAL_FIELDS)
    _validate(request)

    job = OptimizationJob(
        name=request.name, city_id=request.city_id,
        status="queued", stage="queued", progress=0,
        request_json=request.model_dump(mode="json"),
        control_material_version_id=request.control_material.material_version_id,
        base_material_version_id=request.base_material.material_version_id,
    )
    session.add(job)
    session.commit()
    session.refresh(job)

    try:
        job.celery_task_id = run_optimization_task.delay(job.id).id
        session.commit()
        session.refresh(job)
    except Exception as error:
        job.status, job.stage = "failed", "queue_submission_failed"
        job.error_message = str(error)[:4000]
        session.commit()
        raise HTTPException(status_code=503, detail=f"Unable to submit optimization: {error}") from error

    return optimization_to_response(job, now=db_now(session))


@router.get("", response_model=OptimizationJobListResponse)
def list_optimizations(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    session: Session = Depends(get_db),
) -> OptimizationJobListResponse:
    total = session.scalar(select(func.count()).select_from(OptimizationJob)) or 0
    jobs = session.scalars(
        select(OptimizationJob).order_by(OptimizationJob.created_at.desc()).offset(offset).limit(limit)
    ).all()
    now = db_now(session)
    return OptimizationJobListResponse(
        items=[optimization_to_response(j, now=now) for j in jobs], total=total, limit=limit, offset=offset
    )


@router.get("/{job_id}", response_model=OptimizationJobDetail)
def get_optimization(job_id: str, session: Session = Depends(get_db)) -> OptimizationJobDetail:
    job = session.get(OptimizationJob, job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Optimization job not found")
    return optimization_to_detail(job, now=db_now(session))


@router.post("/{job_id}/cancel", response_model=OptimizationJobResponse)
def cancel_optimization(job_id: str, session: Session = Depends(get_db)) -> OptimizationJobResponse:
    job = session.get(OptimizationJob, job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Optimization job not found")
    if job.status in TERMINAL:
        raise HTTPException(status_code=409, detail="Optimization job in terminal state cannot be cancelled")

    now = utc_now()
    job.cancel_requested_at = job.cancel_requested_at or now
    if job.status == "queued":
        job.status, job.stage, job.completed_at = "cancelled", "cancelled", now
    else:
        job.status, job.stage = "cancelling", "waiting_for_cooperative_cancel"

    if job.celery_task_id:
        celery_app.control.revoke(job.celery_task_id, terminate=False)

    session.commit()
    session.refresh(job)
    return optimization_to_response(job, now=db_now(session))
```

### File: `backend/app/api/router.py`
```python
# app/api/router.py
"""Top-level API router. The only place routers are aggregated."""

from fastapi import APIRouter

from app.api import benchmarks, global_batches, materials, model, ops, simulations, weather, optimizations


api_router = APIRouter()

for router in (
    simulations.router,
    benchmarks.router,
    weather.router,
    materials.router,
    global_batches.router,
    model.router,
    ops.router,
    optimizations.router,
):
    api_router.include_router(router)
```

### File: `backend/app/api/simulations.py`
```python
import asyncio
import json

import anyio
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    Request,
    status,
)
from fastapi.responses import Response, StreamingResponse
from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session
from app.services.scenario_summary import build_simulation_summary
from app.services.leases import db_now

from app.core.cities import get_city
from app.db.session import SessionLocal, get_db
from app.models.simulation_job import SimulationJob
from app.schemas.job import (
    SimulationJobDetail,
    SimulationJobListResponse,
    SimulationJobResponse,
)
from app.schemas.simulation import (
    SimulationRequest,
    SimulationResponse,
    SimulationSummary,
    WeatherSimulationRequest,
    WeatherSimulationResponse,
)
from app.services.job_service import (
    get_job_or_none,
    job_to_detail,
    job_to_response,
)
from app.services.material_resolution import (
    linked_material_version_ids,
    resolve_request_materials,
)
from app.services.model_parameters import build_model_metadata
from app.services.result_export import export_result_csv, export_result_json
from app.services.result_storage import load_simulation_result
from app.services.two_node import MODEL_VERSION, simulate_material
from app.services.weather import get_historical_weather
from app.services.weather_quality import WeatherDataError
from app.services.weather_simulation import (
    execute_weather_simulation_with_weather,
)
from app.worker.celery_app import celery_app
from app.worker.tasks import run_weather_simulation_task

router = APIRouter(
    prefix="/api/v1/simulations",
    tags=["simulations"],
)
from app.services.environment_model import required_weather_variables

@router.post("/run", response_model=SimulationResponse)
def run_simulation(
    request: SimulationRequest,
    session: Session = Depends(get_db),
) -> SimulationResponse:
    # Stage 4: resolve material library references before the physics runs.
    # MaterialResolutionError -> 422 via app.api.errors.
    request = resolve_request_materials(session, request)

    try:
        control_result = simulate_material(
            duration_minutes=request.duration_minutes,
            output_interval_minutes=(
                request.output_interval_minutes
            ),
            environment=request.environment,
            person=request.person,
            material=request.control_material,
        )

        rc_result = simulate_material(
            duration_minutes=request.duration_minutes,
            output_interval_minutes=(
                request.output_interval_minutes
            ),
            environment=request.environment,
            person=request.person,
            material=request.rc_material,
        )
    except RuntimeError as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        ) from error

    final_skin_improvement = (
        control_result.final_skin_temperature_c
        - rc_result.final_skin_temperature_c
    )

    final_core_improvement = (
        control_result.final_core_temperature_c
        - rc_result.final_core_temperature_c
    )

    control_skin_average = sum(
        point.skin_temperature_c
        for point in control_result.time_series
    ) / len(control_result.time_series)

    rc_skin_average = sum(
        point.skin_temperature_c
        for point in rc_result.time_series
    ) / len(rc_result.time_series)

    return SimulationResponse(
        model_name="RC transient two-node prototype",
        model_version=MODEL_VERSION,
        city=request.city,
        duration_minutes=request.duration_minutes,
        control=control_result,
        radiative_cooling=rc_result,
        summary=build_simulation_summary(control_result, rc_result),
        warning=(
            "These results are from a simplified transient prototype "
            "and have not yet been validated using thermal manikins, human "
            "trials, or JOS-3 benchmarks. They are not suitable for medical, "
            "occupational safety, or product certification purposes."
        ),
        model_metadata=build_model_metadata(),
    )

@router.post("/run-weather", response_model=WeatherSimulationResponse)
async def run_weather_simulation(
    request: WeatherSimulationRequest,
    session: Session = Depends(get_db),
) -> WeatherSimulationResponse:
    request = await anyio.to_thread.run_sync(
        resolve_request_materials, session, request
    )
    try:
        city = get_city(request.city_id)
        weather = await get_historical_weather(
            city=city,
            start_time_local=request.start_time_local,
            duration_minutes=request.duration_minutes,
            extra_variables=required_weather_variables(request.environment_assumptions),
        )

        # Stage 2: the service owns environment assumptions, model version,
        # model metadata and the environment note, so the synchronous
        # endpoint and the Celery job path produce identical responses.
        return execute_weather_simulation_with_weather(
            request=request,
            weather=weather,
            city_name=city.name,
        )

    except WeatherDataError as error:
        raise HTTPException(
            status_code=422,
            detail=error.to_detail(),
        ) from error
    except ValueError as error:
        raise HTTPException(
            status_code=422,
            detail=str(error),
        ) from error
    except RuntimeError as error:
        raise HTTPException(
            status_code=502,
            detail=str(error),
        ) from error

@router.post("/jobs", response_model=SimulationJobResponse, status_code=status.HTTP_202_ACCEPTED)
def create_simulation_job(
    request: WeatherSimulationRequest,
    session: Session = Depends(get_db),
) -> SimulationJobResponse:
    request = resolve_request_materials(session, request)
    control_version_id, rc_version_id = linked_material_version_ids(request)

    job = SimulationJob(
        city_id=request.city_id,
        status="queued",
        stage="queued",
        progress=0,
        request_json=request.model_dump(mode="json"),  # resolved request
        control_material_version_id=control_version_id,
        rc_material_version_id=rc_version_id,
    )

    session.add(job)
    session.commit()
    session.refresh(job)

    try:
        celery_result = (
            run_weather_simulation_task.delay(
                job.id
            )
        )

        job.celery_task_id = celery_result.id
        session.commit()
        session.refresh(job)

    except Exception as error:
        job.status = "failed"
        job.stage = "queue_submission_failed"
        job.error_message = str(error)
        session.commit()

        raise HTTPException(
            status_code=503,
            detail=(
                "Unable to submit task to Celery:"
                f"{error}"
            ),
        ) from error

    return job_to_response(job)

@router.get("/jobs", response_model=SimulationJobListResponse)
def list_simulation_jobs(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    material_version_id: str | None = Query(
        default=None,
        description="Only jobs whose control or RC garment used this version",
    ),
    session: Session = Depends(get_db),
) -> SimulationJobListResponse:
    filters = []

    if material_version_id:
        filters.append(
            or_(
                SimulationJob.control_material_version_id == material_version_id,
                SimulationJob.rc_material_version_id == material_version_id,
            )
        )

    total = session.scalar(
        select(func.count()).select_from(SimulationJob).where(*filters)
    ) or 0

    jobs = session.scalars(
        select(SimulationJob)
        .where(*filters)
        .order_by(SimulationJob.created_at.desc())
        .offset(offset)
        .limit(limit)
    ).all()
    now = db_now(session)

    return SimulationJobListResponse(
        items=[job_to_response(job, now=now) for job in jobs],
        total=total,
        limit=limit,
        offset=offset,
    )
    
@router.get(
    "/jobs/{job_id}",
    response_model=SimulationJobDetail,
)
def get_simulation_job(
    job_id: str,
    session: Session = Depends(get_db),
) -> SimulationJobDetail:
    job = get_job_or_none(
        session,
        job_id,
    )

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Unable to find simulation job",
        )

    return job_to_detail(job, now=db_now(session))

@router.get(
    "/jobs/{job_id}/result",
    response_model=WeatherSimulationResponse,
)
def get_simulation_result(
    job_id: str,
    session: Session = Depends(get_db),
) -> WeatherSimulationResponse:
    job = get_job_or_none(
        session,
        job_id,
    )

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Unable to find simulation job",
        )

    if job.status != "completed":
        raise HTTPException(
            status_code=409,
            detail=(
                "Simulation not yet completed, "
                f"current status: {job.status}"
            ),
        )

    if not job.result_path:
        raise HTTPException(
            status_code=500,
            detail="Simulation completed but missing result path",
        )

    try:
        return load_simulation_result(
            job.result_path
        )
    except FileNotFoundError as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        ) from error
        
@router.post(
    "/jobs/{job_id}/cancel",
    response_model=SimulationJobResponse,
)
def cancel_simulation_job(
    job_id: str,
    session: Session = Depends(get_db),
) -> SimulationJobResponse:
    job = get_job_or_none(
        session,
        job_id,
    )

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Unable to find simulation job",
        )

    if job.status in {
        "completed",
        "failed",
        "cancelled",
    }:
        raise HTTPException(
            status_code=409,
            detail=(
                "Simulation job in terminal state cannot be cancelled"
            ),
        )

    if job.celery_task_id:
        celery_app.control.revoke(
            job.celery_task_id,
            terminate=False,
        )

    if job.status == "queued":
        job.status = "cancelled"
        job.stage = "cancelled"
    else:
        job.status = "cancelling"
        job.stage = (
            "waiting_for_cooperative_cancel"
        )

    session.commit()
    session.refresh(job)

    return job_to_response(job)

TERMINAL_JOB_STATUSES = {
    "completed",
    "failed",
    "cancelled",
}


def load_job_snapshot(
    job_id: str,
) -> SimulationJobResponse | None:
    with SessionLocal() as session:
        job = session.get(
            SimulationJob,
            job_id,
        )

        if job is None:
            return None

        return job_to_response(job)


@router.get(
    "/jobs/{job_id}/events",
)
async def simulation_job_events(
    job_id: str,
    request: Request,
) -> StreamingResponse:
    initial = await anyio.to_thread.run_sync(
        load_job_snapshot,
        job_id,
    )

    if initial is None:
        raise HTTPException(
            status_code=404,
            detail="Unable to find simulation job",
        )

    async def event_generator():
        previous_payload: str | None = None

        while True:
            if await request.is_disconnected():
                break

            snapshot = (
                await anyio.to_thread.run_sync(
                    load_job_snapshot,
                    job_id,
                )
            )

            if snapshot is None:
                yield (
                    "event: error\n"
                    'data: {"detail":"job not found"}\n\n'
                )
                break

            payload = json.dumps(
                snapshot.model_dump(
                    mode="json"
                ),
                ensure_ascii=False,
            )

            if payload != previous_payload:
                yield (
                    "event: progress\n"
                    f"data: {payload}\n\n"
                )

                previous_payload = payload

            if snapshot.status in (
                TERMINAL_JOB_STATUSES
            ):
                yield (
                    "event: terminal\n"
                    f"data: {payload}\n\n"
                )
                break

            await asyncio.sleep(1)

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
    

@router.get(
    "/jobs/{job_id}/export",
)
def export_simulation_result(
    job_id: str,
    format: str = Query(
        default="csv",
        pattern="^(csv|json)$",
    ),
    session: Session = Depends(get_db),
) -> Response:
    job = get_job_or_none(
        session,
        job_id,
    )

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Unable to find simulation job",
        )

    if job.status != "completed":
        raise HTTPException(
            status_code=409,
            detail="Simulation not yet completed",
        )

    if not job.result_path:
        raise HTTPException(
            status_code=500,
            detail="Simulation completed but missing result path",
        )

    try:
        result = load_simulation_result(
            job.result_path
        )
    except FileNotFoundError as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        ) from error

    if format == "json":
        content = export_result_json(result)
        media_type = "application/json"
        filename = f"simulation-{job_id}.json"
    else:
        content = export_result_csv(result)
        media_type = "text/csv"
        filename = f"simulation-{job_id}.csv"

    return Response(
        content=content.encode("utf-8-sig"),
        media_type=media_type,
        headers={
            "Content-Disposition": (
                f'attachment; filename="{filename}"'
            )
        },
    )

```

### File: `backend/app/api/weather.py`
```python
from datetime import datetime

from fastapi import APIRouter, HTTPException, Query

from app.core.cities import CITIES, get_city
from app.schemas.weather import (
    CityResponse,
    WeatherTimeSeries,
)
from app.services.weather import (
    city_to_response,
    get_historical_weather,
)

from app.services.weather_quality import WeatherDataError

router = APIRouter(
    prefix="/api/v1/weather",
    tags=["weather"],
)


@router.get(
    "/cities",
    response_model=list[CityResponse],
)
def list_cities() -> list[CityResponse]:
    return [
        city_to_response(city)
        for city in CITIES.values()
    ]


@router.get(
    "/history",
    response_model=WeatherTimeSeries,
)
async def weather_history(
    city_id: str = Query(...),
    start_time_local: datetime = Query(...),
    duration_minutes: int = Query(
        default=120,
        ge=1,
        le=1440,
    ),
) -> WeatherTimeSeries:
    try:
        city = get_city(city_id)

        return await get_historical_weather(
            city=city,
            start_time_local=start_time_local,
            duration_minutes=duration_minutes,
        )
    except WeatherDataError as error:
        raise HTTPException(
            status_code=422,
            detail=error.to_detail(),
        ) from error
    except ValueError as error:
        raise HTTPException(
            status_code=422,
            detail=str(error),
        ) from error
    except RuntimeError as error:
        raise HTTPException(
            status_code=502,
            detail=str(error),
        ) from error
```

### File: `backend/app/core/__init__.py`
```python

```

### File: `backend/app/core/cities.py`
```python
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class CityConfig:
    id: str
    name: str
    country: str
    latitude: float
    longitude: float
    elevation_m: float
    timezone: str
    climate_type: str


CITIES: dict[str, CityConfig] = {
    "dubai": CityConfig(
        id="dubai",
        name="Dubai",
        country="United Arab Emirates",
        latitude=25.2048,
        longitude=55.2708,
        elevation_m=16.0,
        timezone="Asia/Dubai",
        climate_type="hot_dry",
    ),
    "guangzhou": CityConfig(
        id="guangzhou",
        name="Guangzhou",
        country="China",
        latitude=23.1291,
        longitude=113.2644,
        elevation_m=21.0,
        timezone="Asia/Shanghai",
        climate_type="hot_humid",
    ),
    "lhasa": CityConfig(
        id="lhasa",
        name="Lhasa",
        country="China",
        latitude=29.6520,
        longitude=91.1721,
        elevation_m=3650.0,
        timezone="Asia/Shanghai",
        climate_type="high_altitude_solar",
    ),
    "singapore": CityConfig(
        id="singapore",
        name="Singapore",
        country="Singapore",
        latitude=1.3521,
        longitude=103.8198,
        elevation_m=15.0,
        timezone="Asia/Singapore",
        climate_type="equatorial_humid",
    ),
    "delhi": CityConfig(
        id="delhi",
        name="Delhi",
        country="India",
        latitude=28.6139,
        longitude=77.2090,
        elevation_m=216.0,
        timezone="Asia/Kolkata",
        climate_type="hot_semi_arid",
    ),
    "riyadh": CityConfig(
        id="riyadh",
        name="Riyadh",
        country="Saudi Arabia",
        latitude=24.7136,
        longitude=46.6753,
        elevation_m=612.0,
        timezone="Asia/Riyadh",
        climate_type="hot_desert",
    ),
    "cairo": CityConfig(
        id="cairo",
        name="Cairo",
        country="Egypt",
        latitude=30.0444,
        longitude=31.2357,
        elevation_m=23.0,
        timezone="Africa/Cairo",
        climate_type="hot_desert",
    ),
    "lagos": CityConfig(
        id="lagos",
        name="Lagos",
        country="Nigeria",
        latitude=6.5244,
        longitude=3.3792,
        elevation_m=41.0,
        timezone="Africa/Lagos",
        climate_type="tropical_humid",
    ),
    "nairobi": CityConfig(
        id="nairobi",
        name="Nairobi",
        country="Kenya",
        latitude=-1.2921,
        longitude=36.8219,
        elevation_m=1795.0,
        timezone="Africa/Nairobi",
        climate_type="tropical_highland",
    ),
    "phoenix": CityConfig(
        id="phoenix",
        name="Phoenix",
        country="United States",
        latitude=33.4484,
        longitude=-112.0740,
        elevation_m=331.0,
        timezone="America/Phoenix",
        climate_type="hot_desert",
    ),
    "houston": CityConfig(
        id="houston",
        name="Houston",
        country="United States",
        latitude=29.7604,
        longitude=-95.3698,
        elevation_m=13.0,
        timezone="America/Chicago",
        climate_type="humid_subtropical",
    ),
    "mexico-city": CityConfig(
        id="mexico-city",
        name="Mexico City",
        country="Mexico",
        latitude=19.4326,
        longitude=-99.1332,
        elevation_m=2240.0,
        timezone="America/Mexico_City",
        climate_type="subtropical_highland",
    ),
    "manaus": CityConfig(
        id="manaus",
        name="Manaus",
        country="Brazil",
        latitude=-3.1190,
        longitude=-60.0217,
        elevation_m=92.0,
        timezone="America/Manaus",
        climate_type="equatorial_humid",
    ),
    "sao-paulo": CityConfig(
        id="sao-paulo",
        name="São Paulo",
        country="Brazil",
        latitude=-23.5505,
        longitude=-46.6333,
        elevation_m=760.0,
        timezone="America/Sao_Paulo",
        climate_type="humid_subtropical",
    ),
    "darwin": CityConfig(
        id="darwin",
        name="Darwin",
        country="Australia",
        latitude=-12.4634,
        longitude=130.8456,
        elevation_m=31.0,
        timezone="Australia/Darwin",
        climate_type="tropical_savanna",
    ),
    "sydney": CityConfig(
        id="sydney",
        name="Sydney",
        country="Australia",
        latitude=-33.8688,
        longitude=151.2093,
        elevation_m=58.0,
        timezone="Australia/Sydney",
        climate_type="humid_subtropical",
    ),
}


def get_city(city_id: str) -> CityConfig:
    normalized_id = city_id.strip().lower()

    if normalized_id not in CITIES:
        supported = ", ".join(sorted(CITIES))

        raise ValueError(
            f"City not supported '{city_id}'. "
            f"Currently supported: {supported}"
        )

    return CITIES[normalized_id]


def list_cities() -> list[CityConfig]:
    return sorted(
        CITIES.values(),
        key=lambda city: (
            city.country,
            city.name,
        ),
    )


def city_to_dict(
    city: CityConfig,
) -> dict[str, str | float]:
    return asdict(city)
```

### File: `backend/app/core/config.py`
```python
"""Application settings."""

from functools import lru_cache
from pathlib import Path
from pydantic import Field


from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


BACKEND_DIRECTORY = Path(__file__).resolve().parents[2]


def split_csv_setting(value: str) -> list[str]:
    """Split a comma-separated application setting."""
    return [
        item.strip()
        for item in value.split(",")
        if item.strip()
    ]


class Settings(BaseSettings):
    app_name: str = "Radiative Cooling Simulation API"
    app_env: str = "development"

    database_url: str = (
        "postgresql+psycopg://"
        "rc_user:rc_password@localhost:5432/"
        "radiative_cooling"
    )

    celery_broker_url: str = "redis://localhost:6379/0"
    celery_result_backend: str = "redis://localhost:6379/1"

    frontend_origin: str = "http://localhost:3000"

    result_directory: Path = (
        BACKEND_DIRECTORY / "data" / "results"
    )

    # Leave this empty to use the operating system temporary directory.
    numba_cache_dir: str | None = Field(
        default=None,
        validation_alias="NUMBA_CACHE_DIR",
    )

    cors_origins: str = "http://localhost:3000"
    cors_methods: str = (
        "GET,POST,PUT,PATCH,DELETE,OPTIONS"
    )
    cors_headers: str = (
        "Accept,Authorization,Content-Type,Origin,"
        "X-Requested-With,Last-Event-ID"
    )
    cors_expose_headers: str = "Content-Disposition"
    cors_allow_credentials: bool = True

    model_config = SettingsConfigDict(
        env_file=BACKEND_DIRECTORY / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
    
    weather_lock_redis_url: str = (
        "redis://localhost:6379/2"
    )

    weather_lock_timeout_seconds: int = 180
    weather_lock_blocking_timeout_seconds: int = 190

    @property
    def cors_origin_list(self) -> list[str]:
        return split_csv_setting(self.cors_origins)

    @property
    def cors_method_list(self) -> list[str]:
        return [
            method.upper()
            for method in split_csv_setting(
                self.cors_methods
            )
        ]

    @property
    def cors_header_list(self) -> list[str]:
        return split_csv_setting(self.cors_headers)

    @property
    def cors_exposed_header_list(self) -> list[str]:
        return split_csv_setting(
            self.cors_expose_headers
        )
    
    # Stage 7 reliability
    CITY_LEASE_TTL_SECONDS: int = 180        # lease 有效期
    CITY_HEARTBEAT_SECONDS: int = 30         # 續約間隔，需 << TTL
    CITY_MAX_RETRIES: int = 3                # retry_count 上限
    LEASE_REAPER_INTERVAL_SECONDS: int = 60  # beat 週期
    CHECKPOINT_EVERY_MONTHS: int = 1         # 目前每月一筆


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return the cached application settings."""
    application_settings = Settings()

    application_settings.result_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    return application_settings


# Keep this alias for modules that still import `settings` directly.
settings = get_settings()
```

### File: `backend/app/core/cors.py`
```python
"""Central CORS middleware configuration."""

from __future__ import annotations

from collections.abc import Sequence

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def normalize_values(values: Sequence[str]) -> list[str]:
    """Remove blank and duplicate configuration values."""
    normalized: list[str] = []
    seen: set[str] = set()

    for value in values:
        item = value.strip()

        if not item or item in seen:
            continue

        normalized.append(item)
        seen.add(item)

    return normalized


def add_cors_middleware(
    application: FastAPI,
    *,
    origins: Sequence[str],
    methods: Sequence[str],
    headers: Sequence[str],
    expose_headers: Sequence[str],
    allow_credentials: bool,
) -> None:
    """Register CORS middleware exactly once."""
    already_registered = any(
        getattr(middleware, "cls", None) is CORSMiddleware
        for middleware in application.user_middleware
    )

    if already_registered:
        raise RuntimeError(
            "CORS middleware has already been registered."
        )

    normalized_origins = normalize_values(origins)
    normalized_methods = [
        method.upper()
        for method in normalize_values(methods)
    ]
    normalized_headers = normalize_values(headers)
    normalized_exposed_headers = normalize_values(expose_headers)

    if not normalized_origins:
        raise ValueError(
            "At least one CORS origin must be configured."
        )

    if not normalized_methods:
        raise ValueError(
            "At least one CORS method must be configured."
        )

    if allow_credentials:
        wildcard_fields = {
            "origins": normalized_origins,
            "methods": normalized_methods,
            "headers": normalized_headers,
        }

        for field_name, values in wildcard_fields.items():
            if "*" in values:
                raise ValueError(
                    "CORS wildcard values cannot be used for "
                    f"{field_name} when credentials are enabled."
                )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=normalized_origins,
        allow_credentials=allow_credentials,
        allow_methods=normalized_methods,
        allow_headers=normalized_headers,
        expose_headers=normalized_exposed_headers,
    )
```

### File: `backend/app/core/runtime.py`
```python
"""Process-level runtime configuration."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path
from typing import Final


APPLICATION_CACHE_DIRECTORY_NAME: Final = (
    "radiative-cooling-platform"
)
NUMBA_CACHE_DIRECTORY_NAME: Final = "numba"
NUMBA_CACHE_ENVIRONMENT_VARIABLE: Final = "NUMBA_CACHE_DIR"

PathValue = str | os.PathLike[str]


def _read_path_value(
    value: PathValue | None,
) -> str | None:
    """Convert a path-like value into non-empty text."""
    if value is None:
        return None

    raw_value = os.fspath(value)

    if not isinstance(raw_value, str):
        raise TypeError("Path values must resolve to text.")

    normalized_value = raw_value.strip()

    return normalized_value or None


def normalize_path(path_value: PathValue) -> Path:
    """Expand and convert a path into an absolute path."""
    normalized_value = _read_path_value(path_value)

    if normalized_value is None:
        raise ValueError("A non-empty path is required.")

    expanded_value = os.path.expandvars(
        os.path.expanduser(normalized_value)
    )

    path = Path(expanded_value)

    if not path.is_absolute():
        path = Path.cwd() / path

    return path.resolve(strict=False)


def _prepare_cache_directory(
    cache_directory: Path,
) -> None:
    """Create the cache directory and verify write access."""
    try:
        cache_directory.mkdir(
            mode=0o700,
            parents=True,
            exist_ok=True,
        )

        if not cache_directory.is_dir():
            raise NotADirectoryError(
                f"{cache_directory} is not a directory."
            )

        with tempfile.NamedTemporaryFile(
            mode="w+b",
            prefix=".numba-cache-write-test-",
            dir=cache_directory,
        ) as probe_file:
            probe_file.write(b"ok")
            probe_file.flush()

    except OSError as error:
        raise RuntimeError(
            "Unable to create or write to the Numba cache "
            f"directory at {cache_directory}."
        ) from error


def configure_numba_cache(
    configured_directory: PathValue | None = None,
    *,
    temporary_root: PathValue | None = None,
) -> Path:
    """Configure a writable cross-platform Numba cache.

    Directory precedence:

    1. The process NUMBA_CACHE_DIR environment variable.
    2. The configured_directory argument.
    3. An application-specific system temporary directory.
    """
    environment_directory = _read_path_value(
        os.environ.get(NUMBA_CACHE_ENVIRONMENT_VARIABLE)
    )
    settings_directory = _read_path_value(
        configured_directory
    )

    if environment_directory is not None:
        cache_directory = normalize_path(
            environment_directory
        )
    elif settings_directory is not None:
        cache_directory = normalize_path(
            settings_directory
        )
    else:
        temporary_root_value = _read_path_value(
            temporary_root
        )

        if temporary_root_value is not None:
            root_directory = normalize_path(
                temporary_root_value
            )
        else:
            root_directory = normalize_path(
                tempfile.gettempdir()
            )

        cache_directory = (
            root_directory
            / APPLICATION_CACHE_DIRECTORY_NAME
            / NUMBA_CACHE_DIRECTORY_NAME
        ).resolve(strict=False)

    _prepare_cache_directory(cache_directory)

    os.environ[NUMBA_CACHE_ENVIRONMENT_VARIABLE] = str(
        cache_directory
    )

    return cache_directory


def configure_runtime(
    numba_cache_dir: PathValue | None = None,
) -> Path:
    """Configure process-level runtime directories."""
    return configure_numba_cache(
        configured_directory=numba_cache_dir,
    )
```

### File: `backend/app/core/time.py`
```python
from datetime import datetime, timezone


def utc_now() -> datetime:
    """Timezone-aware UTC now. Shared by API layer and Celery tasks."""
    return datetime.now(timezone.utc)
```

### File: `backend/app/db/__init__.py`
```python

```

### File: `backend/app/db/base.py`
```python
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
```

### File: `backend/app/db/session.py`
```python
from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import (
    Session,
    sessionmaker,
)

from app.core.config import settings


engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)


def get_db() -> Generator[Session, None, None]:
    with SessionLocal() as session:
        yield session
```

### File: `backend/app/main.py`
```python
"""FastAPI application entry point."""

from datetime import datetime, timezone

from fastapi import FastAPI

from app.core.config import get_settings
from app.core.cors import add_cors_middleware
from app.core.runtime import configure_runtime


settings = get_settings()

# Must run before any module that imports Numba (pythermalcomfort).
configure_runtime(numba_cache_dir=settings.numba_cache_dir)

from app.api.errors import register_exception_handlers  # noqa: E402
from app.api.router import api_router  # noqa: E402


app = FastAPI(
    title="Global Radiative Cooling Clothing Climate Adaptation API",
    description=(
        "Backend API for simulating and evaluating radiative cooling "
        "clothing under global climate conditions."
    ),
    version="0.4.0",
)

add_cors_middleware(
    app,
    origins=settings.cors_origin_list,
    methods=settings.cors_method_list,
    headers=settings.cors_header_list,
    expose_headers=settings.cors_exposed_header_list,
    allow_credentials=settings.cors_allow_credentials,
)

register_exception_handlers(app)

app.include_router(api_router)


@app.get("/api/v1/health")
def health_check():
    return {
        "status": "healthy",
        "service": "radiative-cooling-api",
        "version": app.version,
        "time": datetime.now(timezone.utc).isoformat(),
    }
```

### File: `backend/app/models/__init__.py`
```python
from app.models.material import (
    Material,
    MaterialSpectrum,
    MaterialVersion,
)
from app.models.simulation_job import SimulationJob

from app.models.global_batch import GlobalBatchJob, GlobalCityCheckpoint, GlobalCityResult

from app.models.optimization_job import OptimizationJob

__all__ = [
    "GlobalBatchJob",
    "GlobalCityResult",
    "Material",
    "MaterialSpectrum",
    "MaterialVersion",
    "SimulationJob",
    "GlobalCityCheckpoint",
    "OptimizationJob",
]
```

### File: `backend/app/models/global_batch.py`
```python
from datetime import datetime
from uuid import uuid4

from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Index,          # new
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

    # Stage 7. Job-level state machine + lease.
    attempt: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
        server_default="0",
    )

    lease_owner: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    lease_expires_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        index=True,
    )

    last_heartbeat_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    cancel_requested_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

class GlobalCityResult(Base):
    __tablename__ = "global_city_results"

    __table_args__ = (
        UniqueConstraint(
            "batch_id",
            "city_id",
            name="uq_global_batch_city",
        ),
        Index(
            "ix_global_city_results_lease_reap",
            "status",
            "lease_expires_at",
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

    exposure_coverage_percent: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
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

    maximum_skin_improvement_c: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    effective_cooling_hours: Mapped[float | None] = mapped_column(
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

    completed_month_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
        server_default="0",
    )

    last_checkpoint_month: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    resumed_from_checkpoint: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default="false",
    )

    last_heartbeat_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    lease_owner: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    lease_expires_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    checkpoints: Mapped[list["GlobalCityCheckpoint"]] = relationship(
        back_populates="city_result",
        cascade="all, delete-orphan",
        order_by="GlobalCityCheckpoint.month",
    )

    skin_improvement_p50_c: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    skin_improvement_p90_c: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    skin_improvement_p95_c: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    core_improvement_p50_c: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    core_improvement_p90_c: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    core_improvement_p95_c: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    heatwave_event_count: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    longest_heatwave_days: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    monthly_json: Mapped[list | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    analytics_json: Mapped[dict | None] = mapped_column(
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
    
class GlobalCityCheckpoint(Base):
    """Durable per-month checkpoint so a retried city task can resume
    without re-reading a half-written monthly_json."""

    __tablename__ = "global_city_checkpoints"

    __table_args__ = (
        UniqueConstraint(
            "city_result_id",
            "month",
            name="uq_global_city_checkpoint_month",
        ),
    )

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    city_result_id: Mapped[str] = mapped_column(
        ForeignKey(
            "global_city_results.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    month: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    # retry_count of the city at the time this checkpoint was written
    attempt: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
        server_default="0",
    )

    payload_json: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    city_result: Mapped["GlobalCityResult"] = relationship(
        back_populates="checkpoints",
    )
    # Stage 9. Provenance of the computation that produced this row.
    # NULL on rows written before Stage 9; such rows are never resumed from.
    model_version: Mapped[str | None] = mapped_column(String(20), nullable=True)
    parameter_fingerprint: Mapped[str | None] = mapped_column(String(64), nullable=True)
    request_sha256: Mapped[str | None] = mapped_column(String(64), nullable=True)
```

### File: `backend/app/models/material.py`
```python
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
        UniqueConstraint("material_id", "version_number", name="uq_material_version_number"),
        CheckConstraint("solar_reflectance >= 0 AND solar_reflectance <= 1", name="ck_material_solar_reflectance"),
        CheckConstraint("solar_transmittance >= 0 AND solar_transmittance <= 1", name="ck_material_solar_transmittance"),
        CheckConstraint("infrared_emissivity >= 0 AND infrared_emissivity <= 1", name="ck_material_ir_emissivity"),
        CheckConstraint("infrared_transmittance >= 0 AND infrared_transmittance <= 1", name="ck_material_ir_transmittance"),
        CheckConstraint("solar_reflectance + solar_transmittance <= 1.000001", name="ck_material_solar_energy_sum"),
        # Stage 3 (migration c7d2e9f4a1b8) — mirrored here so autogenerate stays clean.
        CheckConstraint(
            "clothing_area_factor IS NULL OR "
            "(clothing_area_factor >= 1.0 AND clothing_area_factor <= 2.0)",
            name="ck_material_clothing_area_factor",
        ),
        # Stage 4 (migration a1f4c2d9e7b3).
        CheckConstraint(
            "infrared_emissivity + infrared_transmittance <= 1.000001",
            name="ck_material_ir_energy_sum",
        ),
        CheckConstraint(
            "evaporative_resistance_m2pa_w IS NULL OR "
            "(evaporative_resistance_m2pa_w >= 0 AND evaporative_resistance_m2pa_w <= 1000)",
            name="ck_material_evaporative_resistance",
        ),
        # Stage 10 (migration d7e1f3a9b2c4).
        CheckConstraint(
            "infrared_emissivity_window IS NULL OR "
            "(infrared_emissivity_window >= 0 AND infrared_emissivity_window <= 1)",
            name="ck_material_ir_emissivity_window",
        ),
        CheckConstraint(
            "infrared_emissivity_window IS NULL OR "
            "infrared_emissivity_window + infrared_transmittance <= 1.000001",
            name="ck_material_ir_window_energy_sum",
        ),
        # Stage 12 (migration e3b8c1d5f702).
        CheckConstraint(
            "infrared_emissivity_ground_facing IS NULL OR "
            "(infrared_emissivity_ground_facing >= 0 AND infrared_emissivity_ground_facing <= 1)",
            name="ck_material_ir_ground_facing",
        ),
        CheckConstraint(
            "infrared_emissivity_ground_facing IS NULL OR "
            "infrared_emissivity_ground_facing + infrared_transmittance <= 1.000001",
            name="ck_material_ir_ground_facing_energy_sum",
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

    # Stage 3. Measured clothing area factor f_cl; None -> derived from clo.
    clothing_area_factor: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
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

    # Stage 10. Atmospheric-window emissivity; None -> gray emitter.
    infrared_emissivity_window: Mapped[float | None] = mapped_column(Float, nullable=True)

    # Stage 12. Gray emissivity of the ground-facing zone; None -> uniform garment.
    infrared_emissivity_ground_facing: Mapped[float | None] = mapped_column(Float, nullable=True)
    
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

    # Stage 2: per-parameter provenance, keyed by MaterialInput field name.
    parameter_sources_json: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True,
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
```

### File: `backend/app/models/optimization_job.py`
```python
from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, ForeignKey, Index, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class OptimizationJob(Base):
    __tablename__ = "optimization_jobs"
    __table_args__ = (
        Index("ix_optimization_jobs_lease_reap", "status", "lease_expires_at"),
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    celery_task_id: Mapped[str | None] = mapped_column(String(255), nullable=True, index=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    city_id: Mapped[str] = mapped_column(String(100), nullable=False, index=True)

    status: Mapped[str] = mapped_column(String(30), nullable=False, default="queued", index=True)
    stage: Mapped[str] = mapped_column(String(100), nullable=False, default="queued")
    progress: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default="0")
    evaluation_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default="0")

    request_json: Mapped[dict] = mapped_column(JSONB, nullable=False)
    history_json: Mapped[list | None] = mapped_column(JSONB, nullable=True)
    result_json: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now()
    )
    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    attempt: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default="0")
    lease_owner: Mapped[str | None] = mapped_column(String(100), nullable=True)
    lease_expires_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    last_heartbeat_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    cancel_requested_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    control_material_version_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("material_versions.id", ondelete="SET NULL"), nullable=True, index=True
    )
    base_material_version_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("material_versions.id", ondelete="SET NULL"), nullable=True, index=True
    )
```

### File: `backend/app/models/simulation_job.py`
```python
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
```

### File: `backend/app/schemas/__init__.py`
```python

```

### File: `backend/app/schemas/environment.py`
```python
"""Explicit rules for deriving boundary conditions that ERA5 does not provide
(Stage 2; Stage 5 ground albedo; Stage 11 physical sky and ground, ADR 0008).

Defaults reproduce the Stage 1 estimates exactly.

``mean_radiant_temperature`` in EnvironmentInput is used by the model only as
the longwave temperature of the NON-SKY part of the view. The legacy rule
``air_plus_solar_linear`` raises it with GHI although body shortwave is
computed explicitly since Stage 5, i.e. it counts the sun twice (ADR 0008).
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


MeanRadiantTemperatureMethod = Literal[
    "air_plus_solar_linear",   # legacy: T_air + min(cap, gain * GHI)
    "equal_to_air",            # shaded / indoor-like
    "ground_energy_balance",   # Stage 11: steady ground surface balance
]

SkyTemperatureMethod = Literal[
    "humidity_offset",   # T_sky = T_air - (base + range * (1 - RH))
    "fixed_offset",      # T_sky = T_air - fixed_offset
    "swinbank",          # T_sky[K] = 0.0552 * T_air[K]^1.5 (clear sky)
    "brutsaert_cloud",   # Stage 11: Brutsaert + cloud fraction
]

RadiationTimeConvention = Literal[
    "instantaneous_linear",
    "preceding_hour_mean_step",
]

_STAGE1 = {"source_type": "assumed", "reference": "Stage 1 prototype"}


class EnvironmentAssumptions(BaseModel):
    model_config = ConfigDict(extra="forbid")

    mean_radiant_temperature_method: MeanRadiantTemperatureMethod = Field(
        default="ground_energy_balance",
        json_schema_extra={"source_type": "assumed", "reference": "ADR 0008, ADR 0009"},
    )
    solar_mrt_gain_k_per_w_m2: float = Field(
        default=0.012, ge=0.0, le=0.05,
        description="MRT rise per W/m^2 of GHI (air_plus_solar_linear only)",
        json_schema_extra=_STAGE1,
    )
    solar_mrt_gain_cap_k: float = Field(
        default=15.0, ge=0.0, le=40.0,
        description="Upper bound of the solar MRT rise",
        json_schema_extra=_STAGE1,
    )

    sky_temperature_method: SkyTemperatureMethod = Field(
        default="brutsaert_cloud",
        json_schema_extra={"source_type": "assumed", "reference": "ADR 0008, ADR 0009"},
    )
    sky_offset_base_k: float = Field(
        default=5.0, ge=0.0, le=40.0,
        description="humidity_offset: depression at 100 % RH", json_schema_extra=_STAGE1,
    )
    sky_offset_humidity_range_k: float = Field(
        default=10.0, ge=0.0, le=40.0,
        description="humidity_offset: additional depression at 0 % RH", json_schema_extra=_STAGE1,
    )
    fixed_sky_offset_k: float = Field(
        default=15.0, ge=0.0, le=50.0,
        description="fixed_offset: T_air - T_sky", json_schema_extra=_STAGE1,
    )

    sky_view_factor: float = Field(
        default=0.5, ge=0.0, le=1.0,
        description="Fraction of the body's radiative view occupied by sky",
        json_schema_extra={
            "source_type": "assumed",
            "reference": "Standing person on an open, unobstructed site",
        },
    )

    wind_speed_scaling_factor: float = Field(
        default=1.0, gt=0.0, le=1.5,
        description=(
            "Multiplier from ERA5 10 m wind to body-height wind. 1.0 keeps "
            "Stage 1 behaviour; ~0.67 approximates 1.1 m height via a "
            "logarithmic profile over open terrain."
        ),
        json_schema_extra=_STAGE1,
    )

    ground_albedo: float = Field(
        default=0.2, ge=0.0, le=1.0,
        description="Shortwave reflectance of the ground surface",
        json_schema_extra={
            "source_type": "assumed",
            "reference": "Typical dry soil / urban pavement (0.15-0.25)",
        },
    )

    radiation_time_convention: RadiationTimeConvention = Field(
        default="instantaneous_linear",
        json_schema_extra={
            "source_type": "assumed",
            "reference": "Open-Meteo hourly parameter definition (preceding hour mean)",
        },
    )

    # Stage 11 (ADR 0008), ground_energy_balance only.
    ground_emissivity: float = Field(
        default=0.95, ge=0.8, le=1.0,
        description="Longwave emissivity of the ground surface",
        json_schema_extra={
            "source_type": "assumed",
            "reference": "Typical soil, asphalt and concrete (0.92-0.97)",
        },
    )
    ground_soil_conductance_w_m2k: float = Field(
        default=15.0, ge=2.0, le=200.0,
        description=(
            "Effective conductance between the ground surface and the ERA5 "
            "0-7 cm soil layer (k/d)"
        ),
        json_schema_extra={
            "source_type": "assumed",
            "reference": "Order of magnitude for dry soil to pavement; not measured",
        },
    )

    # Stage 12 (ADR 0010). Used only by garments with a ground-facing emissivity.
    zone_view_separation: float = Field(
        default=0.5, ge=0.0, le=1.0,
        description=(
            "How strongly the sky-facing and ground-facing garment zones see different "
            "hemispheres: 0 = both see the body-average mix, 1 = perfect partition"
        ),
        json_schema_extra={
            "source_type": "assumed",
            "reference": "ADR 0010; idealised two-zone garment, not measured",
        },
    )
    
    def describe(self) -> list[str]:
        """Human-readable summary written into ``environment_model_note``."""
        if self.mean_radiant_temperature_method == "air_plus_solar_linear":
            mrt = (
                f"T_mrt = T_air + min({self.solar_mrt_gain_cap_k} K, "
                f"{self.solar_mrt_gain_k_per_w_m2} K/(W/m^2) * GHI)"
            )
        elif self.mean_radiant_temperature_method == "ground_energy_balance":
            mrt = (
                "Non-sky surroundings = ground surface temperature from "
                "(1 - rho_g) GHI + eps_g sigma T_sky^4 = eps_g sigma T_g^4 "
                "+ h_g (T_g - T_air) + K (T_g - T_soil,0-7cm), "
                f"eps_g = {self.ground_emissivity}, "
                f"K = {self.ground_soil_conductance_w_m2k} W/(m^2 K)"
            )
        else:
            mrt = "T_mrt = T_air"

        if self.sky_temperature_method == "humidity_offset":
            sky = (
                f"T_sky = T_air - ({self.sky_offset_base_k} K + "
                f"{self.sky_offset_humidity_range_k} K * (1 - RH))"
            )
        elif self.sky_temperature_method == "fixed_offset":
            sky = f"T_sky = T_air - {self.fixed_sky_offset_k} K"
        elif self.sky_temperature_method == "brutsaert_cloud":
            sky = (
                "T_sky = eps_sky^0.25 T_air, eps_sky = c + (1 - c) * 1.24 "
                "(e_a/T_air)^(1/7), c = ERA5 total cloud cover "
                "(Brutsaert 1975; Crawford & Duchon 1999 form)"
            )
        else:
            sky = "T_sky[K] = 0.0552 * T_air[K]^1.5 (Swinbank 1963, clear sky)"

        if self.radiation_time_convention == "preceding_hour_mean_step":
            radiation = (
                "GHI/DNI/DHI are treated as preceding-hour means held constant "
                "over (t-1h, t] (energy-conserving)."
            )
        else:
            radiation = (
                "GHI/DNI/DHI hourly means are treated as instantaneous values at "
                "the stamped hour and interpolated linearly (approximation; "
                "shifts the solar profile by up to 30 min)."
            )

        return [
            "Air temperature, relative humidity, 10 m wind speed and GHI are "
            "taken from ERA5 via Open-Meteo.",
            mrt,
            sky,
            f"Sky view factor = {self.sky_view_factor}",
            f"Body-height wind = {self.wind_speed_scaling_factor} * ERA5 10 m wind",
            "Direct normal and diffuse horizontal irradiance are taken from "
            "ERA5; the body-incident shortwave follows ASHRAE 55 Appendix C "
            "geometry (ADR 0006).",
            f"Ground albedo = {self.ground_albedo}",
            radiation,
            f"Zone view separation = {self.zone_view_separation} "
            "(two-zone garments only, ADR 0010)",
        ]

EnvironmentPresetName = Literal["open_ground_physical", "legacy_stage1"]

# Overrides on top of the schema defaults. open_ground_physical IS the default.
ENVIRONMENT_PRESETS: dict[str, dict[str, object]] = {
    "open_ground_physical": {},
    "legacy_stage1": {
        "mean_radiant_temperature_method": "air_plus_solar_linear",
        "sky_temperature_method": "humidity_offset",
    },
}

LEGACY_PRESET: EnvironmentPresetName = "legacy_stage1"


def preset_assumptions(name: str) -> EnvironmentAssumptions:
    try:
        overrides = ENVIRONMENT_PRESETS[name]
    except KeyError as error:
        raise ValueError(
            f"Unknown environment preset '{name}'. Known: {sorted(ENVIRONMENT_PRESETS)}"
        ) from error
    return EnvironmentAssumptions(**overrides)
```

### File: `backend/app/schemas/global_batch.py`
```python
from datetime import datetime
from typing import Literal
from app.schemas.environment import EnvironmentAssumptions

from pydantic import (
    BaseModel,
    Field,
    model_validator,
)

from app.schemas.simulation import (
    MaterialInput,
    PersonInput,
)


GlobalBatchStatus = Literal[
    "queued",
    "running",
    "cancelling",
    "cancelled",
    "completed",
    "partial_completed",
    "failed",
]

GlobalCityStatus = Literal[
    "queued",
    "running",
    "cancelled",
    "completed",
    "failed",
]

ExposureMatchMode = Literal[
    "all",
    "any",
]

AnalysisResolution = Literal[
    "representative",
    "daily",
]

ExecutionProfile = Literal[
    "auto",
    "standard",
    "large",
]

LeaseState = Literal["none", "live", "expired"]

class GlobalBatchCreate(BaseModel):
    name: str = Field(
        default="Global multi-day climate adaptation analysis",
        min_length=1,
        max_length=200,
    )

    city_ids: list[str] = Field(
        min_length=1,
        max_length=100,
    )

    year: int = Field(
        default=2023,
        ge=1940,
        le=2100,
    )

    start_month: int = Field(
        default=1,
        ge=1,
        le=12,
    )

    end_month: int = Field(
        default=12,
        ge=1,
        le=12,
    )

    analysis_resolution: AnalysisResolution = "representative"

    # Number of representative sample days per month.
    sample_days_per_month: int = Field(
        default=3,
        ge=1,
        le=7,
    )

    # Sampling interval used in daily analysis mode.
    # 1 means every day, 2 means every two days, and so on.
    daily_stride_days: int = Field(
        default=1,
        ge=1,
        le=7,
    )

    execution_profile: ExecutionProfile = "auto"

    resume_from_checkpoint: bool = True

    enable_heatwave_analysis: bool = True

    heatwave_temperature_threshold_c: float = Field(
        default=35.0,
        ge=-20.0,
        le=70.0,
    )

    heatwave_minimum_consecutive_days: int = Field(
        default=3,
        ge=2,
        le=30,
    )

    # Retained for backward compatibility with Stage 4.1 requests.
    representative_day: int | None = Field(
        default=None,
        ge=1,
        le=28,
    )

    local_start_hour: int = Field(
        default=12,
        ge=0,
        le=23,
    )

    duration_minutes: int = Field(
        default=120,
        ge=30,
        le=1440,
    )

    output_interval_minutes: int = Field(
        default=10,
        ge=1,
        le=60,
    )

    minimum_skin_improvement_c: float = Field(
        default=0.2,
        ge=-5.0,
        le=10.0,
    )

    minimum_air_temperature_c: float | None = Field(
        default=30.0,
        ge=-50.0,
        le=70.0,
    )

    minimum_solar_radiation_w_m2: float | None = Field(
        default=300.0,
        ge=0.0,
        le=1500.0,
    )

    exposure_match_mode: ExposureMatchMode = "all"

    person: PersonInput
    control_material: MaterialInput
    rc_material: MaterialInput
    environment_assumptions: EnvironmentAssumptions = Field(
        default_factory=EnvironmentAssumptions
    )

    @model_validator(mode="after")
    def validate_request(self) -> "GlobalBatchCreate":
        normalized_ids = [
            city_id.strip().lower()
            for city_id in self.city_ids
        ]

        if any(not city_id for city_id in normalized_ids):
            raise ValueError(
                "city_ids cannot contain empty city identifiers"
            )

        if len(normalized_ids) != len(set(normalized_ids)):
            raise ValueError(
                "city_ids cannot contain duplicate cities"
            )

        if self.start_month > self.end_month:
            raise ValueError(
                "start_month cannot be greater than end_month"
            )

        if (
            "representative_day" in self.model_fields_set
            and "sample_days_per_month" not in self.model_fields_set
        ):
            self.sample_days_per_month = 1

        self.city_ids = normalized_ids
        return self


class DailyAdaptationResult(BaseModel):
    sample_date_local: datetime
    weight_days: int = Field(ge=1)

    mean_air_temperature_c: float
    maximum_air_temperature_c: float = Field(
        description="Maximum over the exposure window only"
    )

    # Stage 6. Maximum over the local calendar day; basis for heatwave
    # detection. None on checkpoints written before Stage 6.
    daily_maximum_air_temperature_c: float | None = None

    mean_solar_radiation_w_m2: float
    maximum_solar_radiation_w_m2: float

    exposure_eligible: bool
    beneficial: bool

    average_skin_improvement_c: float
    final_skin_improvement_c: float
    average_core_improvement_c: float
    maximum_skin_improvement_c: float

    weather_from_cache: bool

# Stage 12. Exposure-window means of the longwave boundary temperatures.
    mean_sky_temperature_c: float | None = None
    mean_surround_temperature_c: float | None = None

class SkippedSample(BaseModel):
    """A planned sample day that could not be simulated for data reasons."""

    sample_date_local: datetime
    weight_days: int = Field(ge=1)
    reason_code: str
    message: str
    
class MonthlyAdaptationResult(BaseModel):
    month: int = Field(ge=1, le=12)

    sampled_day_count: int = 1
    eligible_sample_count: int = 0

    total_weighted_days: int = 0
    evaluated_weighted_days: int = 0
    beneficial_weighted_days: int = 0

    exposure_coverage_percent: float = 0.0
    climate_adaptation_rate_percent: float | None = None

    average_skin_improvement_c: float | None = None
    average_core_improvement_c: float | None = None
    maximum_skin_improvement_c: float | None = None

    samples: list[DailyAdaptationResult] = Field(default_factory=list)

    # Stage 1: samples skipped because of weather data problems.
    # Defaults keep previously stored checkpoints loadable.
    skipped_samples: list[SkippedSample] = Field(default_factory=list)
    skipped_weighted_days: int = 0

    # Stage 4.1 backward compatibility.
    representative_date_local: datetime | None = None
    weight_days: int | None = None
    final_skin_improvement_c: float | None = None
    beneficial: bool | None = None


class HeatwaveEvent(BaseModel):
    start_date_local: datetime
    end_date_local: datetime

    duration_days: int = Field(ge=1)

    mean_maximum_air_temperature_c: float
    peak_air_temperature_c: float

    mean_skin_improvement_c: float
    p90_skin_improvement_c: float

    beneficial_day_count: int = Field(ge=0)


class GlobalCityResultResponse(BaseModel):
    id: str
    batch_id: str
    celery_task_id: str | None

    city_id: str
    city_name: str
    country: str
    latitude: float
    longitude: float

    status: GlobalCityStatus
    stage: str
    progress: int

    climate_adaptation_rate_percent: float | None
    exposure_coverage_percent: float | None

    annual_average_skin_improvement_c: float | None
    annual_average_core_improvement_c: float | None
    maximum_skin_improvement_c: float | None
    effective_cooling_hours: float | None

    sampled_day_count: int | None
    eligible_sample_count: int | None

    evaluated_weighted_days: int | None
    beneficial_weighted_days: int | None

    completed_month_count: int = 0
    last_checkpoint_month: int | None = None
    resumed_from_checkpoint: bool = False
    last_heartbeat_at: datetime | None = None

    skin_improvement_p50_c: float | None = None
    skin_improvement_p90_c: float | None = None
    skin_improvement_p95_c: float | None = None

    core_improvement_p50_c: float | None = None
    core_improvement_p90_c: float | None = None
    core_improvement_p95_c: float | None = None

    heatwave_event_count: int | None = None
    longest_heatwave_days: int | None = None
    heatwave_events: list[HeatwaveEvent] | None = None

    data_quality: dict | None = None
    metric_definitions: dict | None = None
    
    retry_count: int
    monthly_results: list[MonthlyAdaptationResult] | None

    error_message: str | None
    started_at: datetime | None
    completed_at: datetime | None

    # Stage 8. Lease visibility; derived server-side so clients never compare clocks.
    lease_owner: str | None = None
    lease_expires_at: datetime | None = None
    lease_state: LeaseState = "none"
    # Months with a durable checkpoint row (source of truth for resume).
    checkpoint_months: list[int] = Field(default_factory=list)

    # Stage 9. Why heatwave analysis is or is not available for THIS result
    # (configuration or data), so the UI never guesses from the request alone.
    heatwave_analysis_available: bool | None = None
    heatwave_unavailable_reason: str | None = None
    heatwave_temperature_basis: str | None = None

class GlobalBatchResponse(BaseModel):
    id: str
    celery_group_id: str | None

    status: GlobalBatchStatus
    stage: str
    progress: int

    total_city_count: int
    completed_city_count: int
    failed_city_count: int
    cancelled_city_count: int

    summary: dict | None
    error_message: str | None

    created_at: datetime
    updated_at: datetime
    started_at: datetime | None
    completed_at: datetime | None
    # Stage 4. Set when the request referenced material library versions.
    control_material_version_id: str | None = None
    rc_material_version_id: str | None = None

    # Stage 8. Batch-level Stage 7 state.
    attempt: int = 0
    lease_owner: str | None = None
    lease_expires_at: datetime | None = None
    last_heartbeat_at: datetime | None = None
    cancel_requested_at: datetime | None = None
class GlobalBatchDetail(GlobalBatchResponse):
    request: GlobalBatchCreate
    city_results: list[GlobalCityResultResponse]


class GlobalBatchListResponse(BaseModel):
    items: list[GlobalBatchResponse]
    total: int
    limit: int
    offset: int


class GlobalBatchEstimateResponse(BaseModel):
    city_count: int
    month_count: int
    samples_per_city: int
    total_samples: int
    thermal_simulation_count: int
    estimated_weather_requests: int

    analysis_resolution: AnalysisResolution

    resolved_execution_profile: ExecutionProfile
    resolved_queue: str

    checkpoint_count_per_city: int
    heatwave_analysis_available: bool
    
class GlobalCityProgress(BaseModel):
    """Lightweight per-city row streamed over SSE; never carries monthly payloads."""

    id: str
    city_id: str
    status: GlobalCityStatus
    stage: str
    progress: int
    retry_count: int
    completed_month_count: int
    last_checkpoint_month: int | None
    last_heartbeat_at: datetime | None
    lease_owner: str | None
    lease_expires_at: datetime | None
    lease_state: LeaseState
    checkpoint_months: list[int]
    error_message: str | None


class GlobalBatchProgressEvent(BaseModel):
    batch: GlobalBatchResponse
    cities: list[GlobalCityProgress]


class CityCheckpointResponse(BaseModel):
    id: str
    month: int
    attempt: int
    created_at: datetime
    payload_sha256: str
    sampled_day_count: int
    skipped_sample_count: int
    # Stage 9
    model_version: str | None = None
    parameter_fingerprint: str | None = None
    provenance_matches_batch: bool = False
    mismatch_reason: str | None = None

class CityCheckpointListResponse(BaseModel):
    batch_id: str
    city_result_id: str
    city_id: str
    start_month: int
    end_month: int
    items: list[CityCheckpointResponse]
    # First month a resumed worker would compute; == end_month + 1 when complete.
    resume_from_month: int
```

### File: `backend/app/schemas/job.py`
```python
from datetime import datetime
from typing import Literal

from pydantic import BaseModel

from app.schemas.simulation import (
    WeatherSimulationRequest,
)


JobStatus = Literal[
    "queued",
    "running",
    "cancelling",
    "cancelled",
    "completed",
    "failed",
]

LeaseState = Literal["none", "live", "expired"]


class SimulationJobResponse(BaseModel):
    id: str
    celery_task_id: str | None
    status: JobStatus
    stage: str
    progress: int
    city_id: str

    summary: dict | None
    error_message: str | None

    created_at: datetime
    updated_at: datetime
    started_at: datetime | None
    completed_at: datetime | None
    # Stage 4. Set when the request referenced material library versions.
    control_material_version_id: str | None = None
    rc_material_version_id: str | None = None
    # Stage 9
    attempt: int = 0
    lease_owner: str | None = None
    lease_expires_at: datetime | None = None
    last_heartbeat_at: datetime | None = None
    lease_state: LeaseState = "none"
    
class SimulationJobDetail(
    SimulationJobResponse
):
    request: WeatherSimulationRequest


class SimulationJobListResponse(BaseModel):
    items: list[SimulationJobResponse]
    total: int
    limit: int
    offset: int
```

### File: `backend/app/schemas/material.py`
```python
from datetime import datetime
from typing import Literal
from app.schemas.provenance import (
    ParameterSource,
    validate_parameter_source_keys,
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    model_validator,
    field_validator,
)

_NON_NULLABLE_UPDATE_FIELDS = frozenset({"name", "is_archived"})

MaterialMode = Literal[
    "ordinary",
    "opaque_emitter",
    "infrared_transparent",
    "hybrid",
]

SpectrumType = Literal[
    "solar_reflectance",
    "solar_transmittance",
    "mir_emissivity",
    "mir_transmittance",
]


class MaterialVersionCreate(BaseModel):
    mode: MaterialMode = "opaque_emitter"

    clothing_insulation_clo: float = Field(
        default=0.5,
        ge=0,
        le=5,
    )

    evaporative_resistance_m2pa_w: float | None = Field(
        default=None,
        ge=0,
        le=1000,
    )

    clothing_area_factor: float | None = Field(default=None, ge=1.0, le=2.0)

    solar_reflectance: float = Field(
        default=0.5,
        ge=0,
        le=1,
    )

    solar_transmittance: float = Field(
        default=0,
        ge=0,
        le=1,
    )

    infrared_emissivity: float = Field(
        default=0.9,
        ge=0,
        le=1,
    )

    infrared_emissivity_window: float | None = Field(default=None, ge=0, le=1)
    
    infrared_emissivity_ground_facing: float | None = Field(default=None, ge=0, le=1)
    
    infrared_transmittance: float = Field(
        default=0,
        ge=0,
        le=1,
    )

    projected_solar_area_factor: float = Field(
        default=0.25,
        ge=0,
        le=1,
    )

    absorbed_solar_to_body_fraction: float = Field(
        default=0.35,
        ge=0,
        le=1,
        description=(
            "DEPRECATED since Stage 5 (ADR 0005): ignored by the physics. "
            "Kept so stored requests and library versions keep loading."
        ),
    )

    areal_density_g_m2: float | None = Field(
        default=None,
        ge=0,
    )

    specific_heat_j_kgk: float | None = Field(
        default=None,
        ge=0,
    )

    source_type: str = Field(
        default="manual",
        max_length=50,
    )

    source_reference: str | None = None
    notes: str | None = None
    parameter_sources: dict[str, ParameterSource] | None = None

# 3. MaterialVersionCreate validator: also check provenance keys
    @model_validator(mode="after")
    def validate_version(self):
        if self.solar_reflectance + self.solar_transmittance > 1.0 + 1e-6:
            raise ValueError(
                "solar_reflectance + solar_transmittance cannot be greater than 1"
            )
        if self.infrared_emissivity + self.infrared_transmittance > 1.0 + 1e-6:
            raise ValueError(
                "infrared_emissivity + infrared_transmittance cannot be greater than 1"
            )
        if self.infrared_emissivity_window is not None:
            from app.schemas.simulation import _check_spectral_emissivity
            _check_spectral_emissivity(
                self.infrared_emissivity,
                self.infrared_emissivity_window,
                self.infrared_transmittance,
            )
        ground = self.infrared_emissivity_ground_facing
        if ground is not None and ground + self.infrared_transmittance > 1.0 + 1e-6:
            raise ValueError(
                "infrared_emissivity_ground_facing + infrared_transmittance cannot be greater than 1"
            )
        validate_parameter_source_keys(self.parameter_sources)
        return self


class MaterialCreate(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=200,
    )

    slug: str = Field(
        min_length=1,
        max_length=200,
        pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$",
    )

    description: str | None = None
    institution: str | None = None

    initial_version: MaterialVersionCreate


class MaterialUpdate(BaseModel):
    """PATCH /materials/{id}: metadata only.

    * Omitted keys are left unchanged; ``description``/``institution`` may be
      cleared with null or "".
    * ``slug`` is immutable (it is the stable identifier); physical values live
      in immutable versions -> POST /materials/{id}/versions.
    """

    model_config = ConfigDict(extra="forbid")

    name: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = None
    institution: str | None = Field(default=None, max_length=255)
    is_archived: bool | None = None

    @field_validator("name", mode="before")
    @classmethod
    def _strip_name(cls, value):
        return value.strip() if isinstance(value, str) else value

    @field_validator("description", "institution", mode="before")
    @classmethod
    def _blank_to_none(cls, value):
        if isinstance(value, str):
            return value.strip() or None
        return value

    @model_validator(mode="after")
    def _reject_null_for_required(self) -> "MaterialUpdate":
        for field in self.model_fields_set & _NON_NULLABLE_UPDATE_FIELDS:
            if getattr(self, field) is None:
                raise ValueError(f"'{field}' cannot be null")
        return self


class SpectrumSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    spectrum_type: str
    wavelength_unit: str
    point_count: int
    minimum_wavelength_um: float
    maximum_wavelength_um: float
    original_filename: str
    file_checksum_sha256: str
    created_at: datetime


class MaterialVersionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id: str
    material_id: str
    version_number: int
    mode: str

    clothing_insulation_clo: float
    evaporative_resistance_m2pa_w: float | None
    
    solar_reflectance: float
    solar_transmittance: float
    infrared_emissivity: float
    infrared_transmittance: float
    infrared_emissivity_ground_facing: float | None = None
    
    projected_solar_area_factor: float
    absorbed_solar_to_body_fraction: float

    areal_density_g_m2: float | None
    specific_heat_j_kgk: float | None

    source_type: str
    source_reference: str | None
    notes: str | None

    clothing_area_factor: float | None = None

    created_at: datetime
    spectra: list[SpectrumSummary] = []
    parameter_sources: dict[str, ParameterSource] | None = Field(
        default=None,
        validation_alias="parameter_sources_json",
    )
    infrared_emissivity_window: float | None = None


class MaterialResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    slug: str
    description: str | None
    institution: str | None
    is_archived: bool
    created_at: datetime
    updated_at: datetime

    versions: list[MaterialVersionResponse]


class MaterialListItem(BaseModel):
    id: str
    name: str
    slug: str
    institution: str | None
    is_archived: bool
    latest_version_number: int | None
    created_at: datetime


class MaterialListResponse(BaseModel):
    items: list[MaterialListItem]
    total: int
    limit: int
    offset: int


class SpectrumPoint(BaseModel):
    wavelength_um: float
    value: float


class SpectrumResponse(BaseModel):
    summary: SpectrumSummary
    points: list[SpectrumPoint]

class MaterialVersionListItem(BaseModel):
    """Flat row for version pickers: one line per material version."""

    id: str
    material_id: str
    material_name: str
    material_slug: str
    version_number: int
    mode: str

    clothing_insulation_clo: float
    evaporative_resistance_m2pa_w: float | None
    clothing_area_factor: float | None
    solar_reflectance: float
    solar_transmittance: float
    infrared_emissivity: float
    infrared_transmittance: float
    infrared_emissivity_ground_facing: float | None = None

    source_type: str
    is_archived: bool
    created_at: datetime
    infrared_emissivity_window: float | None = None


class MaterialVersionListResponse(BaseModel):
    items: list[MaterialVersionListItem]
    total: int
    limit: int
    offset: int

class SpectrumBandSummary(BaseModel):
    """Planck-weighted band averages of one IR spectrum (Stage 10)."""

    spectrum_type: str
    temperature_k: float
    window_lower_um: float
    window_upper_um: float
    measured_lower_um: float
    measured_upper_um: float
    window_average: float | None
    window_coverage: float            # share of the window's blackbody emission covered
    broadband_average: float | None   # over the measured range
    broadband_coverage: float         # share of total blackbody emission covered
    outside_window_average: float | None
```

### File: `backend/app/schemas/ops.py`
```python
"""Operational health of the asynchronous pipeline (Stage 8)."""

from datetime import datetime

from pydantic import BaseModel, Field


class WorkerStatus(BaseModel):
    name: str
    active_task_count: int
    reserved_task_count: int


class LeaseSummary(BaseModel):
    running_cities: int
    queued_cities: int
    live_leases: int
    expired_leases: int
    running_batches: int
    cancelling_batches: int


class OpsStatusResponse(BaseModel):
    checked_at: datetime
    broker_reachable: bool
    worker_count: int
    workers: list[WorkerStatus] = Field(default_factory=list)
    leases: LeaseSummary
    lease_ttl_seconds: int
    heartbeat_interval_seconds: int
    reaper_interval_seconds: int
    # Upper bound on time-to-recovery after a hard worker kill.
    worst_case_recovery_seconds: int
```

### File: `backend/app/schemas/optimization.py`
```python
"""Inverse design: target performance -> material parameter requirements (Stage 3, 10)."""

from __future__ import annotations

import calendar
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, model_validator

from app.schemas.environment import EnvironmentAssumptions
from app.schemas.simulation import MaterialInput, PersonInput


DecisionVariableName = Literal[
    "solar_reflectance",
    "solar_transmittance",
    "infrared_emissivity",
    "infrared_emissivity_window",
    "infrared_emissivity_outside_window",
    "infrared_emissivity_ground_facing",
    "infrared_transmittance",
    "clothing_insulation_clo",
    "evaporative_resistance_m2pa_w",
]

VARIABLE_LIMITS: dict[str, tuple[float, float]] = {
    "solar_reflectance": (0.0, 1.0),
    "solar_transmittance": (0.0, 1.0),
    "infrared_emissivity": (0.0, 1.0),
    "infrared_emissivity_window": (0.0, 1.0),
    "infrared_emissivity_outside_window": (0.0, 1.0),
    "infrared_emissivity_ground_facing": (0.0, 1.0),
    "infrared_transmittance": (0.0, 1.0),
    "clothing_insulation_clo": (0.0, 2.0),
    "evaporative_resistance_m2pa_w": (0.0, 200.0),
}

DemandDirection = Literal["increasing", "decreasing"]

# Which end of each range is harder to make ("increasing": larger = more
# demanding). Conventions only; override per variable.
DEFAULT_DEMAND_DIRECTION: dict[str, DemandDirection] = {
    "solar_reflectance": "increasing",
    "solar_transmittance": "decreasing",
    "infrared_emissivity": "increasing",
    "infrared_emissivity_window": "increasing",
    "infrared_emissivity_outside_window": "decreasing",
    "infrared_emissivity_ground_facing": "decreasing",
    "infrared_transmittance": "increasing",
    "clothing_insulation_clo": "decreasing",
    "evaporative_resistance_m2pa_w": "decreasing",
}

EMISSIVITY_BAND_VARIABLES = frozenset(
    {"infrared_emissivity_window", "infrared_emissivity_outside_window"}
)

MetricName = Literal[
    "mean_skin_temperature_c",
    "peak_skin_temperature_c",
    "peak_core_temperature_c",
    "skin_exceedance_fraction",
    "core_exceedance_fraction",
    "skin_excess_degree_hours",
    "core_excess_degree_hours",
    "mean_skin_cooling_c",
    "mean_core_cooling_c",
]

ObjectiveName = Literal[
    "mean_skin_temperature_c",
    "peak_skin_temperature_c",
    "peak_core_temperature_c",
    "skin_exceedance_fraction",
    "core_exceedance_fraction",
    "skin_excess_degree_hours",
    "core_excess_degree_hours",
    "mean_skin_cooling_c",
    "mean_core_cooling_c",
    "material_demand",
]

OptimizationStatus = Literal["queued", "running", "cancelling", "cancelled", "completed", "failed"]
LeaseState = Literal["none", "live", "expired"]
ObjectiveTrend = Literal["improves", "worsens", "flat", "mixed"]


class DecisionVariable(BaseModel):
    name: DecisionVariableName
    lower: float
    upper: float
    demand_direction: DemandDirection | None = None
    demand_weight: float = Field(default=1.0, gt=0, le=10)

    @model_validator(mode="after")
    def check_bounds(self) -> "DecisionVariable":
        low, high = VARIABLE_LIMITS[self.name]
        if not (low <= self.lower < self.upper <= high):
            raise ValueError(
                f"{self.name}: bounds must satisfy {low} <= lower < upper <= {high}"
            )
        return self


class MetricConstraint(BaseModel):
    metric: MetricName
    operator: Literal["<=", ">="] = "<="
    threshold: float
    # Violation is divided by this before constraints are summed. None -> metric default.
    scale: float | None = Field(default=None, gt=0)


class OptimizationObjective(BaseModel):
    metric: ObjectiveName = "skin_excess_degree_hours"
    sense: Literal["minimize", "maximize"] = "minimize"


class RequirementMapSpec(BaseModel):
    x_variable: DecisionVariableName = "solar_reflectance"
    y_variable: DecisionVariableName = "infrared_emissivity"
    resolution: int = Field(default=11, ge=3, le=21)


class OptimizationCreate(BaseModel):
    name: str = Field(default="Material requirement search", min_length=1, max_length=200)
    city_id: str = Field(min_length=1)
    year: int = Field(default=2023, ge=1940, le=2100)
    months: list[int] = Field(default_factory=lambda: [8], min_length=1, max_length=12)
    sample_days_per_month: int = Field(default=3, ge=1, le=31)
    local_start_hour: int = Field(default=12, ge=0, le=23)
    duration_minutes: int = Field(default=120, ge=30, le=480)
    output_interval_minutes: int = Field(default=5, ge=1, le=30)

    skin_threshold_c: float = Field(default=35.0, ge=30.0, le=42.0)
    core_threshold_c: float = Field(default=38.0, ge=36.5, le=41.0)

    person: PersonInput
    control_material: MaterialInput
    base_material: MaterialInput
    environment_assumptions: EnvironmentAssumptions = Field(default_factory=EnvironmentAssumptions)

    variables: list[DecisionVariable] = Field(min_length=1, max_length=6)
    objective: OptimizationObjective = Field(default_factory=OptimizationObjective)
    constraints: list[MetricConstraint] = Field(default_factory=list, max_length=6)

    algorithm: Literal["differential_evolution"] = "differential_evolution"
    population_multiplier: int = Field(default=10, ge=4, le=30)
    max_generations: int = Field(default=30, ge=1, le=200)
    seed: int | None = 42
    # Stage 10
    secondary_demand_weight: float = Field(
        default=1e-3, ge=0, le=1,
        description="Weight of material_demand added to feasible objectives so ties "
                    "resolve to the least demanding design",
    )
    convergence_tolerance: float = Field(
        default=1e-4, gt=0, le=1,
        description="Absolute DE tolerance on the normalised objective",
    )

    requirement_map: RequirementMapSpec | None = Field(default_factory=RequirementMapSpec)

    @model_validator(mode="after")
    def validate_request(self) -> "OptimizationCreate":
        self.city_id = self.city_id.strip().lower()

        if any(m < 1 or m > 12 for m in self.months) or len(set(self.months)) != len(self.months):
            raise ValueError("months must be unique values between 1 and 12")
        self.months = sorted(self.months)

        names = [v.name for v in self.variables]
        if len(set(names)) != len(names):
            raise ValueError("variables cannot contain duplicate names")

        if "infrared_emissivity" in names and EMISSIVITY_BAND_VARIABLES & set(names):
            raise ValueError(
                "infrared_emissivity (gray study) cannot be combined with "
                "infrared_emissivity_window / infrared_emissivity_outside_window"
            )
        if "infrared_emissivity" in names and self.base_material.infrared_emissivity_window is not None:
            raise ValueError(
                "base_material is a selective emitter; optimise "
                "infrared_emissivity_window / infrared_emissivity_outside_window instead"
            )

        spec = self.requirement_map
        if spec is not None:
            if spec.x_variable == spec.y_variable:
                raise ValueError("requirement_map axes must differ")
            missing = {spec.x_variable, spec.y_variable} - set(names)
            if missing:
                raise ValueError(
                    "requirement_map axes must be decision variables: " + ", ".join(sorted(missing))
                )
        return self

    def samples_per_month(self, month: int) -> int:
        return min(self.sample_days_per_month, calendar.monthrange(self.year, month)[1])


class OptimizationEstimate(BaseModel):
    variable_count: int
    population_size: int
    optimizer_evaluation_budget: int
    requirement_map_evaluations: int
    sample_count: int
    thermal_simulation_budget: int
    weather_requests: int
    corner_evaluations: int = 0
    sensitivity_evaluations: int = 0


class EvaluationMetrics(BaseModel):
    sample_count: int
    mean_skin_temperature_c: float
    peak_skin_temperature_c: float
    peak_core_temperature_c: float
    skin_exceedance_fraction: float
    core_exceedance_fraction: float
    mean_skin_cooling_c: float
    mean_core_cooling_c: float
    # Stage 10. Optional so results stored before Stage 10 still load.
    skin_excess_degree_hours: float | None = None
    core_excess_degree_hours: float | None = None


class CandidateEvaluation(BaseModel):
    parameters: dict[str, float]
    metrics: EvaluationMetrics | None
    objective_value: float | None
    constraint_violation: float | None   # normalised, summed
    feasible: bool
    # Stage 10
    constraint_excess: dict[str, float] = Field(default_factory=dict)  # native units, > 0 = violated
    material_demand: float | None = None


class GenerationRecord(BaseModel):
    generation: int
    penalised_objective: float
    best_parameters: dict[str, float]
    best_metric_value: float | None
    best_feasible: bool
    evaluation_count: int


class RequirementCell(BaseModel):
    x: float
    y: float
    metric_value: float
    constraint_violation: float
    feasible: bool


class FrontierPoint(BaseModel):
    y: float
    minimum_x: float | None  # deprecated alias of required_x
    required_x: float | None = None


class RequirementMapResult(BaseModel):
    x_variable: DecisionVariableName
    y_variable: DecisionVariableName
    x_values: list[float]
    y_values: list[float]
    cells: list[list[RequirementCell | None]]
    frontier: list[FrontierPoint]
    minimum_x_at_max_y: float | None
    minimum_y_at_max_x: float | None
    fixed_parameters: dict[str, float]
    # Stage 10
    x_demand_direction: DemandDirection = "increasing"
    y_demand_direction: DemandDirection = "increasing"
    required_x_at_best_y: float | None = None
    required_y_at_best_x: float | None = None
    objective_trend_x: ObjectiveTrend | None = None
    objective_trend_y: ObjectiveTrend | None = None
    plateau_fraction: float | None = None
    metric_min: float | None = None
    metric_max: float | None = None


class ParameterSensitivity(BaseModel):
    """Central difference at the reported optimum, scaled to the whole range."""

    name: DecisionVariableName
    probe_low: float
    probe_high: float
    full_range_effects: dict[str, float]


class SkippedOptimizationSample(BaseModel):
    sample_date_local: datetime
    reason_code: str
    message: str


class OptimizationResult(BaseModel):
    verdict: Literal["feasible", "infeasible", "unconstrained"]
    message: str
    objective: OptimizationObjective
    constraints: list[MetricConstraint]
    best: CandidateEvaluation
    baseline: CandidateEvaluation
    optical_upper_bound: CandidateEvaluation | None  # most demanding design
    best_corner: CandidateEvaluation | None = None
    requirement_map: RequirementMapResult | None
    sample_count: int
    skipped_samples: list[SkippedOptimizationSample]
    weather_payload_sha256: dict[str, str | None]
    evaluation_count: int
    simulation_count: int
    generations: int
    algorithm: str
    algorithm_message: str
    elapsed_seconds: float
    model_version: str
    parameter_fingerprint: str
    # Stage 10
    warnings: list[str] = Field(default_factory=list)
    sensitivities: list[ParameterSensitivity] = Field(default_factory=list)
    objective_reference: float | None = None
    objective_scale: float | None = None


class OptimizationJobResponse(BaseModel):
    id: str
    celery_task_id: str | None
    name: str
    city_id: str
    status: OptimizationStatus
    stage: str
    progress: int
    evaluation_count: int
    error_message: str | None
    created_at: datetime
    updated_at: datetime
    started_at: datetime | None
    completed_at: datetime | None
    attempt: int = 0
    lease_owner: str | None = None
    lease_expires_at: datetime | None = None
    last_heartbeat_at: datetime | None = None
    lease_state: LeaseState = "none"
    cancel_requested_at: datetime | None = None
    control_material_version_id: str | None = None
    base_material_version_id: str | None = None


class OptimizationJobDetail(OptimizationJobResponse):
    request: OptimizationCreate
    history: list[GenerationRecord]
    result: OptimizationResult | None


class OptimizationJobListResponse(BaseModel):
    items: list[OptimizationJobResponse]
    total: int
    limit: int
    offset: int
```

### File: `backend/app/schemas/provenance.py`
```python
"""Provenance types shared by material inputs, the model parameter registry
and simulation responses (Stage 2), plus the material field manifest (Stage 4).
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


SourceType = Literal[
    "measured",      # measured on the actual sample
    "manufacturer",  # datasheet value
    "literature",    # published value, reference required
    "standard",      # ISO / ASHRAE / CODATA
    "derived",       # computed from other inputs by this platform
    "assumed",       # engineering assumption without measurement
    "manual",        # legacy default of the materials API
]

# Every MaterialInput field that enters the physics. Order is the display
# order used by the field manifest and by conflict reports.
MATERIAL_PHYSICAL_FIELD_ORDER: tuple[str, ...] = (
    "clothing_insulation_clo",
    "evaporative_resistance_m2pa_w",
    "clothing_area_factor",
    "solar_reflectance",
    "solar_transmittance",
    "infrared_emissivity",
    "infrared_emissivity_window",   # Stage 10
    "infrared_emissivity_ground_facing",   # Stage 12
    "infrared_transmittance",
    "projected_solar_area_factor",
)

MATERIAL_PHYSICAL_FIELDS = frozenset(MATERIAL_PHYSICAL_FIELD_ORDER)

# Kept in the schema and the database for backward compatibility, but no longer
# read by the physics (Stage 5, ADR 0005). Accepted in parameter_sources so
# stored versions keep loading; never verified against a library version and
# never listed in the field manifest.
MATERIAL_DEPRECATED_FIELDS = frozenset({"absorbed_solar_to_body_fraction"})


def validate_parameter_source_keys(
    sources: Mapping[str, object] | None,
) -> None:
    if not sources:
        return

    unknown = set(sources) - MATERIAL_PHYSICAL_FIELDS - MATERIAL_DEPRECATED_FIELDS

    if unknown:
        raise ValueError(
            "parameter_sources refers to unknown material fields: "
            + ", ".join(sorted(unknown))
        )


class ParameterSource(BaseModel):
    """Provenance of one numeric input."""

    model_config = ConfigDict(extra="forbid")

    source_type: SourceType = "assumed"
    reference: str | None = Field(default=None, max_length=500)
    note: str | None = Field(default=None, max_length=1000)


class ModelParameter(BaseModel):
    """A physical constant used by the thermal model."""

    model_config = ConfigDict(frozen=True)

    name: str
    value: float
    unit: str
    description: str
    source_type: SourceType
    reference: str
    note: str | None = None


class ModelMetadata(BaseModel):
    """Written into every simulation response for traceability."""

    parameter_set_version: str
    parameter_set_sha256: str


class ModelParameterManifest(ModelMetadata):
    parameters: list[ModelParameter]


class MaterialFieldDescriptor(BaseModel):
    """Machine-readable description of one physical material field (Stage 4).

    Generated from ``MaterialInput`` so that the frontend can render forms and
    provenance editors without duplicating bounds, units or defaults.
    """

    model_config = ConfigDict(frozen=True)

    name: str
    unit: str
    description: str
    minimum: float | None
    maximum: float | None
    default: float | None
    nullable: bool
    derived_when_null: str | None = None


class MaterialFieldManifest(ModelMetadata):
    source_types: list[SourceType]
    fields: list[MaterialFieldDescriptor]
```

### File: `backend/app/schemas/simulation.py`
```python
from pydantic import BaseModel, Field, model_validator

from datetime import datetime

from app.schemas.weather import WeatherTimeSeries

from app.schemas.environment import EnvironmentAssumptions

from app.schemas.provenance import (  # replace the existing provenance import
    MATERIAL_PHYSICAL_FIELD_ORDER,
    MATERIAL_PHYSICAL_FIELDS,
    ModelMetadata,
    ParameterSource,
    validate_parameter_source_keys,
)

__all__ = ["MATERIAL_PHYSICAL_FIELDS", "MATERIAL_PHYSICAL_FIELD_ORDER"]  # re-export

from typing import Literal

BodyPosition = Literal["standing", "sitting"]

class EnvironmentInput(BaseModel):
    air_temperature_c: float = Field(default=38.0, ge=-50, le=70)
    mean_radiant_temperature_c: float = Field(default=45.0, ge=-50, le=150)
    sky_temperature_c: float | None = Field(default=None, ge=-100, le=70)
    relative_humidity_percent: float = Field(default=40.0, ge=0, le=100)
    wind_speed_m_s: float = Field(default=1.5, ge=0, le=30)
    solar_radiation_w_m2: float = Field(
        default=800.0, ge=0, le=1500,
        description="Global horizontal irradiance (GHI)",
    )
    sky_view_factor: float = Field(default=0.5, ge=0, le=1)
    
    # Stage 5 (ADR 0006). Optional beam/diffuse split; supply both or neither.
    direct_normal_irradiance_w_m2: float | None = Field(
        default=None, ge=0, le=1500,
        description="Direct normal irradiance (DNI) on a plane facing the sun",
    )
    diffuse_horizontal_irradiance_w_m2: float | None = Field(
        default=None, ge=0, le=1500,
        description="Diffuse horizontal irradiance (DHI) from the sky vault",
    )
    ground_albedo: float = Field(
        default=0.2, ge=0, le=1,
        description="Shortwave reflectance of the ground (reflected-diffuse term)",
    )
    # Stage 12 (ADR 0010).
    zone_view_separation: float = Field(
        default=0.5, ge=0, le=1,
        description="Hemisphere separation of the two garment zones (two-zone garments only)",
    )
    
    @model_validator(mode="after")
    def validate_solar_split(self):
        has_dni = self.direct_normal_irradiance_w_m2 is not None
        has_dhi = self.diffuse_horizontal_irradiance_w_m2 is not None

        if has_dni != has_dhi:
            raise ValueError(
                "direct_normal_irradiance_w_m2 and "
                "diffuse_horizontal_irradiance_w_m2 must be supplied together"
            )

        return self

    @property
    def has_solar_split(self) -> bool:
        return self.direct_normal_irradiance_w_m2 is not None

class PersonInput(BaseModel):
    met: float = Field(default=2.6, ge=0.7, le=10)
    body_surface_area_m2: float = Field(default=1.8, ge=1.0, le=3.0)
    body_mass_kg: float = Field(default=70.0, ge=30.0, le=200.0)
    initial_core_temperature_c: float = Field(default=36.8, ge=34, le=40)
    initial_skin_temperature_c: float = Field(default=33.7, ge=20, le=40)

    # Stage 5 (ADR 0006). Selects A_r/A_D for longwave and diffuse shortwave.
    position: BodyPosition = Field(
        default="standing",
        description="Posture; selects the effective radiation area ratio",
    )

def _check_spectral_emissivity(broadband: float, window: float, transmittance: float) -> None:
    from app.services.planck import outside_window_emissivity  # lazy: avoid layering cycle

    if window + transmittance > 1.0 + 1e-6:
        raise ValueError(
            "infrared_emissivity_window + infrared_transmittance cannot be greater than 1"
        )
    outside = outside_window_emissivity(broadband, window)
    if outside < -1e-6 or outside + transmittance > 1.0 + 1e-6:
        raise ValueError(
            "infrared_emissivity and infrared_emissivity_window imply an "
            f"out-of-window emissivity of {outside:.3f}, outside "
            "[0, 1 - infrared_transmittance]"
        )
class MaterialInput(BaseModel):
    """Garment parameters for one scenario.

    ``material_version_id`` links the input to an immutable material library
    version. When it is set, the API resolves it (Stage 4, PR-4):
    * physical fields that are omitted are filled from the stored version;
    * physical fields that are supplied must equal the stored version,
      otherwise the request is rejected with MATERIAL_PARAMETER_CONFLICT;
    * provenance fields are filled from the stored version when omitted.
    """

    name: str = Field(min_length=1, max_length=100)

    clothing_insulation_clo: float = Field(
        default=0.5, ge=0, le=5,
        description="Intrinsic dry thermal insulation of the garment",
        json_schema_extra={"unit": "clo"},
    )

    # Stage 2. Intrinsic clothing evaporative resistance Re,cl.
    evaporative_resistance_m2pa_w: float | None = Field(
        default=None, ge=0, le=1000,
        description="Intrinsic evaporative resistance Re,cl of the garment",
        json_schema_extra={
            "unit": "m^2 Pa/W",
            "derived_when_null": "R_cl / (LR * i_cl)",
        },
    )

    # Stage 3. Measured clothing area factor f_cl.
    clothing_area_factor: float | None = Field(
        default=None, ge=1.0, le=2.0,
        description="Clothing area factor f_cl = A_cl / A_D",
        json_schema_extra={
            "unit": "-",
            "derived_when_null": "1 + clothing_area_factor_slope * clo",
        },
    )

    solar_reflectance: float = Field(
        default=0.5, ge=0, le=1,
        description="Hemispherical solar reflectance (0.3-2.5 um)",
        json_schema_extra={"unit": "-"},
    )
    solar_transmittance: float = Field(
        default=0, ge=0, le=1,
        description="Hemispherical solar transmittance (0.3-2.5 um)",
        json_schema_extra={"unit": "-"},
    )
    infrared_emissivity: float = Field(
        default=0.9, ge=0, le=1,
        description=(
            "Broadband longwave emissivity of the outer surface "
            "(Planck-weighted at emissivity_reference_temperature)"
        ),
        json_schema_extra={"unit": "-"},
    )

    # Stage 10 (ADR 0007). Emissivity inside the atmospheric window.
    infrared_emissivity_window: float | None = Field(
        default=None, ge=0, le=1,
        description="Longwave emissivity averaged over the atmospheric window (8-13 um)",
        json_schema_extra={
            "unit": "-",
            "derived_when_null": "gray emitter: equals infrared_emissivity",
        },
    )

    # Stage 12 (ADR 0010). Gray emissivity of the ground-facing garment zone.
    infrared_emissivity_ground_facing: float | None = Field(
        default=None, ge=0, le=1,
        description="Longwave emissivity of the garment zone facing the ground and surroundings",
        json_schema_extra={
            "unit": "-",
            "derived_when_null": "uniform garment: same longwave optics on every zone",
        },
    )
    
    # Stage 2. Longwave transmittance of the textile (IR-transparent designs).
    infrared_transmittance: float = Field(
        default=0.0, ge=0, le=1,
        description="Longwave transmittance of the textile (8-13 um)",
        json_schema_extra={"unit": "-"},
    )

    projected_solar_area_factor: float = Field(
        default=0.25, ge=0, le=1,
        description="Projected area factor A_p / A_D for direct solar radiation",
        json_schema_extra={"unit": "-"},
    )
    absorbed_solar_to_body_fraction: float = Field(
        default=0.35, ge=0, le=1,
        description=(
            "DEPRECATED since Stage 5 (ADR 0005): ignored by the physics. "
            "Kept so stored requests and library versions keep loading."
        ),
        json_schema_extra={"unit": "-", "deprecated": True},
    )

    # Provenance (no effect on the physics).
    material_version_id: str | None = Field(
        default=None,
        description="Material library version this input was taken from",
    )
    source_type: str | None = Field(default=None, max_length=50)
    source_reference: str | None = None
    # Stage 2. Per-parameter provenance keyed by field name.
    parameter_sources: dict[str, ParameterSource] | None = None

    @model_validator(mode="after")
    def validate_optical_properties(self):
        if self.solar_reflectance + self.solar_transmittance > 1.0 + 1e-6:
            raise ValueError(
                "solar_reflectance + solar_transmittance cannot be greater than 1"
            )

        if self.infrared_emissivity + self.infrared_transmittance > 1.0 + 1e-6:
            raise ValueError(
                "infrared_emissivity + infrared_transmittance cannot be greater than 1"
            )
        if self.infrared_emissivity_window is not None:
            _check_spectral_emissivity(
                self.infrared_emissivity,
                self.infrared_emissivity_window,
                self.infrared_transmittance,
            )
            
        ground = self.infrared_emissivity_ground_facing
        if ground is not None and ground + self.infrared_transmittance > 1.0 + 1e-6:
            raise ValueError(
                "infrared_emissivity_ground_facing + infrared_transmittance cannot be greater than 1"
            )
            
        validate_parameter_source_keys(self.parameter_sources)

        return self


class SimulationRequest(BaseModel):
    city: str = Field(default="Dubai", min_length=1)
    duration_minutes: int = Field(
        default=120,
        ge=1,
        le=1440,
    )
    output_interval_minutes: int = Field(
        default=1,
        ge=1,
        le=60,
    )
    environment: EnvironmentInput
    person: PersonInput
    control_material: MaterialInput
    rc_material: MaterialInput

class EnergyDiagnostics(BaseModel):
    stored_energy_change_j_m2: float
    integrated_net_heat_j_m2: float
    energy_residual_j_m2: float
    normalized_residual_percent: float
    maximum_core_step_c: float = Field(
        description="Largest core temperature change between two consecutive "
        "audit-grid samples (NOT the solver's internal step)."
    )
    maximum_skin_step_c: float = Field(
        description="Largest skin temperature change between two consecutive "
        "audit-grid samples (NOT the solver's internal step)."
    )
    solver_function_evaluations: int
    # Stage 6. None on results stored before the audit grid existed.
    diagnostic_interval_seconds: float | None = None
    
class TimeSeriesPoint(BaseModel):
    minute: float
    core_temperature_c: float
    skin_temperature_c: float
    convection_w_m2: float
    longwave_radiation_w_m2: float
    evaporation_w_m2: float
    absorbed_solar_w_m2: float
    core_to_skin_w_m2: float
    # Stage 2 diagnostics. Optional so stored results still load.
    maximum_evaporation_w_m2: float | None = None
    skin_wettedness: float | None = None
    # Stage 3 diagnostics.
    clothing_surface_temperature_c: float | None = None
    skin_blood_flow_kg_h_m2: float | None = None
    # Stage 5 diagnostics.
    solar_incident_w_m2: float | None = None
    solar_absorbed_by_textile_w_m2: float | None = None
    solar_transmitted_w_m2: float | None = None
    # Stage 10: net window-band longwave loss (selective emitters only).
    longwave_window_w_m2: float | None = None
    # Stage 11: boundary conditions actually used (same for both garments).
    sky_temperature_c: float | None = None
    surround_temperature_c: float | None = None

class ClothingSummary(BaseModel):
    """Resolved clothing quantities actually used by the solver."""

    dry_resistance_m2k_w: float
    evaporative_resistance_m2pa_w: float
    evaporative_resistance_source: Literal["material_input", "derived_from_clo"]
    infrared_transmittance: float
    # Stage 3
    clothing_area_factor: float | None = None
    clothing_area_factor_source: (
        Literal["material_input", "derived_from_clo"] | None
    ) = None
    # Stage 10
    infrared_emissivity_window: float | None = None
    infrared_emissivity_outside_window: float | None = None
    # Stage 12
    infrared_emissivity_ground_facing: float | None = None

class BodyThermalSummary(BaseModel):
    """Heat capacities derived from PersonInput (Stage 3, ADR 0001)."""

    body_mass_kg: float
    body_surface_area_m2: float
    core_heat_capacity_j_m2k: float
    skin_heat_capacity_j_m2k: float
    # Stage 5
    position: BodyPosition | None = None
    effective_radiation_area_ratio: float | None = None

class ScenarioResult(BaseModel):
    material_name: str
    time_series: list[TimeSeriesPoint]
    final_core_temperature_c: float
    final_skin_temperature_c: float
    peak_core_temperature_c: float
    peak_skin_temperature_c: float
    diagnostics: EnergyDiagnostics
    # Stage 2
    clothing: ClothingSummary | None = None
    assumptions_applied: list[str] = Field(default_factory=list)
    # Stage 3
    body: BodyThermalSummary | None = None


class SimulationSummary(BaseModel):
    final_skin_temperature_improvement_c: float
    final_core_temperature_improvement_c: float
    average_skin_temperature_improvement_c: float
    # Stage 6. Optional so results stored before PR-1a still load.
    averaging_method: str | None = Field(
        default=None,
        description=(
            "How the average improvement was computed. "
            "'time_weighted_trapezoid' = trapezoidal mean over the exposure "
            "window; None = legacy arithmetic mean over output points."
        ),
    )



class SimulationResponse(BaseModel):
    model_name: str
    model_version: str
    city: str
    duration_minutes: int
    control: ScenarioResult
    radiative_cooling: ScenarioResult
    summary: SimulationSummary
    warning: str
    # Stage 2. Optional so previously stored results still load.
    model_metadata: ModelMetadata | None = None

class BenchmarkTolerances(BaseModel):
    """Acceptance thresholds on the maximum absolute trajectory difference."""

    core_temperature_c: float = Field(default=0.3, gt=0, le=5)
    skin_temperature_c: float = Field(default=1.0, gt=0, le=10)
    
class GaggeBenchmarkRequest(BaseModel):
    duration_minutes: int = Field(default=60, ge=1, le=240)
    environment: EnvironmentInput
    person: PersonInput
    material: MaterialInput
    tolerances: BenchmarkTolerances = Field(default_factory=BenchmarkTolerances)

class GaggeModelOutput(BaseModel):
    core_temperature_c: float
    skin_temperature_c: float
    skin_evaporation_w_m2: float
    skin_heat_loss_w_m2: float
    respiratory_heat_loss_w_m2: float
    skin_blood_flow_kg_h_m2: float
    skin_wettedness: float
    standard_effective_temperature_c: float


class PrototypeBenchmarkOutput(BaseModel):
    core_temperature_c: float
    skin_temperature_c: float
    evaporation_w_m2: float
    skin_wettedness: float
    skin_blood_flow_kg_h_m2: float
    energy_residual_percent: float

class BenchmarkSeriesPoint(BaseModel):
    minute: int
    prototype_core_temperature_c: float
    prototype_skin_temperature_c: float
    prototype_evaporation_w_m2: float
    reference_core_temperature_c: float
    reference_skin_temperature_c: float
    reference_evaporation_w_m2: float
    
class BenchmarkMetric(BaseModel):
    final_difference_c: float
    maximum_absolute_difference_c: float
    root_mean_square_difference_c: float
    tolerance_c: float
    passed: bool
    
class ReferencePortParity(BaseModel):
    """Port vs. library after 60 minutes (the only duration the library runs)."""

    library_core_temperature_c: float
    port_core_temperature_c: float
    library_skin_temperature_c: float
    port_skin_temperature_c: float
    maximum_absolute_difference_c: float
    
class GaggeBenchmarkResponse(BaseModel):
    reference_model: str
    reference_library: str
    reference_library_version: str
    environment_note: str
    alignment_applied: list[str]
    prototype: PrototypeBenchmarkOutput
    gagge: GaggeModelOutput
    # Kept for backward compatibility with Stage 2 clients.
    difference_core_temperature_c: float
    difference_skin_temperature_c: float
    # Stage 3
    core_temperature: BenchmarkMetric
    skin_temperature: BenchmarkMetric
    passed: bool
    time_series: list[BenchmarkSeriesPoint]
    reference_port_parity: ReferencePortParity
    warning: str
class WeatherSimulationRequest(BaseModel):
    city_id: str = Field(
        default="dubai",
        min_length=1,
    )
    start_time_local: datetime
    duration_minutes: int = Field(
        default=120,
        ge=1,
        le=1440,
    )
    output_interval_minutes: int = Field(
        default=1,
        ge=1,
        le=60,
    )
    person: PersonInput
    control_material: MaterialInput
    rc_material: MaterialInput
    environment_assumptions: EnvironmentAssumptions = Field(
        default_factory=EnvironmentAssumptions
    )

class WeatherSimulationResponse(
    SimulationResponse
):
    weather: WeatherTimeSeries
    environment_model_note: str
    environment_assumptions: EnvironmentAssumptions | None = None
```

### File: `backend/app/schemas/weather.py`
```python
from datetime import datetime

from pydantic import BaseModel, Field, model_validator


class CityResponse(BaseModel):
    id: str
    name: str
    country: str
    latitude: float
    longitude: float
    elevation_m: float
    timezone: str
    climate_type: str


class WeatherPoint(BaseModel):
    timestamp: datetime

    air_temperature_c: float
    relative_humidity_percent: float
    wind_speed_m_s: float

    ghi_w_m2: float
    direct_radiation_w_m2: float
    diffuse_radiation_w_m2: float
    dni_w_m2: float
    # Stage 11. Only present when requested (see environment_model.required_weather_variables).
    cloud_cover_percent: float | None = None
    soil_temperature_c: float | None = None


class WeatherGap(BaseModel):
    """A break in the hourly timeline between two consecutive points."""

    start: datetime
    end: datetime
    missing_steps: int = Field(ge=1)


class WeatherQualityReport(BaseModel):
    """Result of normalising a raw weather timeline (Stage 1, PR-1)."""

    expected_step_seconds: int = Field(gt=0)
    point_count: int = Field(ge=0)
    first_timestamp: datetime | None = None
    last_timestamp: datetime | None = None
    was_sorted: bool = True
    duplicates_removed: int = 0
    gaps: list[WeatherGap] = Field(default_factory=list)
    notes: list[str] = Field(default_factory=list)


class WeatherSourceMetadata(BaseModel):
    provider: str
    dataset: str
    model: str
    latitude: float
    longitude: float
    elevation_m: float
    timezone: str
    downloaded_at: datetime
    from_cache: bool
    attribution: str

    # Stage 1 additions. Optional so previously stored results still load.
    payload_sha256: str | None = None
    quality: WeatherQualityReport | None = None


class WeatherTimeSeries(BaseModel):
    city: CityResponse
    requested_start_time: datetime
    requested_end_time: datetime
    points: list[WeatherPoint]
    source: WeatherSourceMetadata

    @model_validator(mode="after")
    def validate_points(self):
        if len(self.points) < 2:
            raise ValueError(
                "Dynamic simulation requires at least two weather data points"
            )

        timestamps = [point.timestamp for point in self.points]

        for previous, current in zip(timestamps, timestamps[1:]):
            if current <= previous:
                raise ValueError(
                    "Weather time series must be strictly increasing in time "
                    "(sorted, no duplicate timestamps)"
                )

        return self


class WeatherHistoryQuery(BaseModel):
    city_id: str
    start_time_local: datetime
    duration_minutes: int = Field(
        default=120,
        ge=1,
        le=1440,
    )
```

### File: `backend/app/services/__init__.py`
```python

```

### File: `backend/app/services/annual_sampling.py`
```python
import calendar
import math
from dataclasses import dataclass
from datetime import date

from app.schemas.global_batch import (
    GlobalBatchCreate,
)


@dataclass(frozen=True)
class SamplingDay:
    date_local: date
    weight_days: int


def assign_nearest_day_weights(
    *,
    days_in_month: int,
    sample_days: list[int],
) -> list[tuple[int, int]]:
    if days_in_month < 1:
        raise ValueError(
            "days_in_month must be at least 1"
        )

    normalized_days = sorted(
        {
            max(
                1,
                min(days_in_month, day),
            )
            for day in sample_days
        }
    )

    if not normalized_days:
        raise ValueError(
            "sample_days cannot be empty"
        )

    weights = {
        day: 0
        for day in normalized_days
    }

    for calendar_day in range(
        1,
        days_in_month + 1,
    ):
        nearest_sample = min(
            normalized_days,
            key=lambda sample_day: (
                abs(sample_day - calendar_day),
                sample_day,
            ),
        )

        weights[nearest_sample] += 1

    return [
        (
            sample_day,
            weights[sample_day],
        )
        for sample_day in normalized_days
    ]


def build_weighted_sample_days(
    *,
    days_in_month: int,
    sample_count: int,
    legacy_representative_day: int | None = None,
) -> list[tuple[int, int]]:
    sample_count = max(
        1,
        min(sample_count, days_in_month),
    )

    if (
        sample_count == 1
        and legacy_representative_day is not None
    ):
        sample_days = [
            min(
                legacy_representative_day,
                days_in_month,
            )
        ]
    else:
        sample_days: list[int] = []

        for index in range(sample_count):
            sample_day = round(
                (index + 0.5)
                * days_in_month
                / sample_count
            )

            sample_day = max(
                1,
                min(days_in_month, sample_day),
            )

            if sample_day not in sample_days:
                sample_days.append(sample_day)

        candidate = 1

        while len(sample_days) < sample_count:
            if candidate not in sample_days:
                sample_days.append(candidate)

            candidate += 1

        sample_days.sort()

    return assign_nearest_day_weights(
        days_in_month=days_in_month,
        sample_days=sample_days,
    )


def build_daily_stride_sample_days(
    *,
    days_in_month: int,
    stride_days: int,
) -> list[tuple[int, int]]:
    stride_days = max(
        1,
        min(stride_days, 7),
    )

    sample_days = list(
        range(
            1,
            days_in_month + 1,
            stride_days,
        )
    )

    return assign_nearest_day_weights(
        days_in_month=days_in_month,
        sample_days=sample_days,
    )


def build_month_sampling_plan(
    *,
    request: GlobalBatchCreate,
    month: int,
) -> list[SamplingDay]:
    days_in_month = calendar.monthrange(
        request.year,
        month,
    )[1]

    if request.analysis_resolution == "daily":
        weighted_days = (
            build_daily_stride_sample_days(
                days_in_month=days_in_month,
                stride_days=request.daily_stride_days,
            )
        )
    else:
        weighted_days = build_weighted_sample_days(
            days_in_month=days_in_month,
            sample_count=(
                request.sample_days_per_month
            ),
            legacy_representative_day=(
                request.representative_day
            ),
        )

    return [
        SamplingDay(
            date_local=date(
                request.year,
                month,
                day,
            ),
            weight_days=weight,
        )
        for day, weight in weighted_days
    ]


def build_annual_sampling_plan(
    request: GlobalBatchCreate,
) -> list[SamplingDay]:
    plan: list[SamplingDay] = []

    for month in range(
        request.start_month,
        request.end_month + 1,
    ):
        plan.extend(
            build_month_sampling_plan(
                request=request,
                month=month,
            )
        )

    return plan


def estimate_sample_count(
    request: GlobalBatchCreate,
) -> int:
    if request.analysis_resolution == "daily":
        return sum(
            math.ceil(
                calendar.monthrange(
                    request.year,
                    month,
                )[1]
                / request.daily_stride_days
            )
            for month in range(
                request.start_month,
                request.end_month + 1,
            )
        )

    return (
        request.end_month
        - request.start_month
        + 1
    ) * request.sample_days_per_month
```

### File: `backend/app/services/body.py`
```python
"""Body thermal mass (Stage 3, ADR 0001).

C_core = m * c_p * (1 - alpha) / A_D          [J/(m^2 K)]
C_skin = m * c_p * alpha / A_D

alpha is kept constant (Gagge 1986 initial value 0.1). Gagge lets alpha vary
with skin blood flow; a constant keeps the capacities state-independent so the
energy-balance diagnostics remain exact.
"""

from __future__ import annotations

from dataclasses import dataclass

from app.schemas.simulation import PersonInput
from app.services.model_parameters import get_parameter_value


BODY_SPECIFIC_HEAT = get_parameter_value("body_specific_heat")
SKIN_MASS_FRACTION = get_parameter_value("skin_mass_fraction")


@dataclass(frozen=True)
class BodyHeatCapacities:
    core_j_m2k: float
    skin_j_m2k: float

    @property
    def total_j_m2k(self) -> float:
        return self.core_j_m2k + self.skin_j_m2k


def body_heat_capacities(person: PersonInput) -> BodyHeatCapacities:
    total = BODY_SPECIFIC_HEAT * person.body_mass_kg / person.body_surface_area_m2
    return BodyHeatCapacities(
        core_j_m2k=total * (1.0 - SKIN_MASS_FRACTION),
        skin_j_m2k=total * SKIN_MASS_FRACTION,
    )
```

### File: `backend/app/services/checkpoints.py`
```python
"""Durable monthly checkpoints with provenance (Stage 9).

A checkpoint row is only trusted when it was produced by the same model
version, the same parameter fingerprint and the same physics-relevant request
as the batch being resumed. Anything else is reported in ``discarded`` and
recomputed. Rows written before Stage 9 carry NULL provenance and are never
resumed from.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.orm import Session

from app.models.global_batch import GlobalCityCheckpoint, GlobalCityResult
from app.schemas.global_batch import GlobalBatchCreate
from app.services.reproducibility import canonical_json, parameter_fingerprint
from app.services.two_node import MODEL_VERSION


# Fields that do not change the per-city physics and must not invalidate a
# checkpoint when a batch is retried.
REQUEST_HASH_EXCLUDED_FIELDS = frozenset(
    {"name", "city_ids", "execution_profile", "resume_from_checkpoint"}
)


def request_sha256(request: GlobalBatchCreate) -> str:
    payload = request.model_dump(mode="json", exclude=set(REQUEST_HASH_EXCLUDED_FIELDS))
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class CheckpointProvenance:
    model_version: str
    parameter_fingerprint: str
    request_sha256: str

    @classmethod
    def for_request(cls, request: GlobalBatchCreate) -> "CheckpointProvenance":
        return cls(
            model_version=MODEL_VERSION,
            parameter_fingerprint=parameter_fingerprint(request.environment_assumptions),
            request_sha256=request_sha256(request),
        )

    def mismatch_reason(self, row: GlobalCityCheckpoint) -> str | None:
        if row.model_version is None or row.parameter_fingerprint is None or row.request_sha256 is None:
            return "legacy checkpoint without provenance (written before Stage 9)"
        if row.model_version != self.model_version:
            return f"model_version {row.model_version} != {self.model_version}"
        if row.parameter_fingerprint != self.parameter_fingerprint:
            return "parameter_fingerprint differs"
        if row.request_sha256 != self.request_sha256:
            return "request parameters differ"
        return None


@dataclass
class ResumeState:
    next_month: int
    payloads: list[dict] = field(default_factory=list)
    discarded: list[dict] = field(default_factory=list)  # {"month": int, "reason": str}


def upsert_month_checkpoint(
    session: Session,
    *,
    city_result_id: str,
    owner: str,
    month: int,
    attempt: int,
    payload: dict,
    provenance: CheckpointProvenance,
) -> bool:
    """Stage the checkpoint row in the current transaction.

    Returns False (and stages nothing) when ``owner`` does not hold the city
    lease. The caller must commit via ``heartbeat_city_lease`` in the same
    session so that row and heartbeat land (or roll back) together.
    """
    owns = session.scalar(
        select(GlobalCityResult.id).where(
            GlobalCityResult.id == city_result_id,
            GlobalCityResult.lease_owner == owner,
        )
    )
    if owns is None:
        return False

    values = {
        "city_result_id": city_result_id,
        "month": month,
        "attempt": attempt,
        "payload_json": payload,
        "model_version": provenance.model_version,
        "parameter_fingerprint": provenance.parameter_fingerprint,
        "request_sha256": provenance.request_sha256,
    }
    session.execute(
        pg_insert(GlobalCityCheckpoint)
        .values(**values)
        .on_conflict_do_update(
            constraint="uq_global_city_checkpoint_month",
            set_={k: v for k, v in values.items() if k not in ("city_result_id", "month")},
        )
    )
    return True


def load_resume_state(
    session: Session,
    city_result_id: str,
    *,
    start_month: int,
    provenance: CheckpointProvenance,
) -> ResumeState:
    """Trusted contiguous prefix of checkpoints starting at ``start_month``.

    The prefix ends at the first hole or provenance mismatch. Every row after
    that is discarded; each one reports its *own* reason (provenance first,
    then contiguity) so the operator sees why a month was recomputed instead
    of a cascade of "hole" messages.
    """
    rows = session.scalars(
        select(GlobalCityCheckpoint)
        .where(GlobalCityCheckpoint.city_result_id == city_result_id)
        .order_by(GlobalCityCheckpoint.month)
    ).all()

    state = ResumeState(next_month=start_month)
    prefix_open = True

    for row in rows:
        if row.month < start_month:
            state.discarded.append({"month": row.month, "reason": "outside requested range"})
            continue

        reason = provenance.mismatch_reason(row)
        if reason is not None:
            state.discarded.append({"month": row.month, "reason": reason})
            prefix_open = False
            continue

        if not prefix_open or row.month > state.next_month:
            state.discarded.append({
                "month": row.month,
                "reason": f"not contiguous with the resumable prefix (resume restarts at month {state.next_month})",
            })
            prefix_open = False
            continue

        state.payloads.append(row.payload_json)
        state.next_month += 1

    return state
```

### File: `backend/app/services/climate_adaptation.py`
```python
"""Per-city annual climate adaptation analysis.

Stage 1 changes
---------------
* Exposure statistics (mean / max air temperature and GHI) are computed over
  the exposure window only via ``compute_exposure_window_statistics``, never
  over the padded ``weather.points`` buffer.
* Skin/core improvement averages use time-weighted integration.
* Sample days whose weather fails validation are recorded as skipped instead
  of aborting the whole city.
* The duplicate ``build_weighted_sample_days`` was removed; the canonical
  implementation lives in ``annual_sampling`` and is re-exported here.
* ``effective_cooling_hours`` keeps its numeric field (DB column, CSV) but
  an explicit definition is emitted in ``metric_definitions``.
"""

from collections.abc import Callable
from datetime import datetime, timedelta
from typing import Any, TypedDict

from app.core.cities import get_city
from app.schemas.global_batch import (
    DailyAdaptationResult,
    GlobalBatchCreate,
    MonthlyAdaptationResult,
    SkippedSample,
)
from app.schemas.simulation import WeatherSimulationRequest
from app.services.annual_sampling import (  # noqa: F401 (re-export)
    build_annual_sampling_plan,
    build_month_sampling_plan,
    build_weighted_sample_days,
)
from app.services.climate_analytics import build_city_analytics
from app.services.exposure_statistics import (
    compute_daily_maximum_air_temperature,
    compute_exposure_window_statistics,
    time_weighted_mean,
)
from app.services.scenario_summary import pair_scenarios
from app.services.weather import (
    get_historical_weather_range,
    slice_weather_time_series,
)
from app.services.weather_quality import WeatherDataError
from app.services.weather_simulation import (
    execute_weather_simulation_with_weather,
)

from app.services.environment_model import required_weather_variables

__all__ = [
    "analyze_city_climate_adaptation",
    "build_metric_definitions",
    "build_weighted_sample_days",
    "is_exposure_eligible",
    "summarize_month",
]


ProgressCallback = Callable[[int, str], None]

CheckpointCallback = Callable[
    [list[MonthlyAdaptationResult], int, int],
    None,
]

class DataQualitySummary(TypedDict):
    skipped_sample_count: int
    skipped_weighted_days: float
    skip_reasons: dict[str, int]
    monthly_weather_payload_sha256: dict[str, str | None]


class CityClimateAdaptationSummary(TypedDict):
    city_id: str
    city_name: str
    country: str
    latitude: float
    longitude: float
    climate_adaptation_rate_percent: float | None
    exposure_coverage_percent: float
    annual_average_skin_improvement_c: float | None
    annual_average_core_improvement_c: float | None
    maximum_skin_improvement_c: float | None
    effective_cooling_hours: float
    sampled_day_count: int
    eligible_sample_count: int
    evaluated_weighted_days: float
    beneficial_weighted_days: float
    completed_month_count: int
    skin_improvement_p50_c: float | None
    skin_improvement_p90_c: float | None
    skin_improvement_p95_c: float | None
    core_improvement_p50_c: float | None
    core_improvement_p90_c: float | None
    core_improvement_p95_c: float | None
    heatwave_analysis_available: bool
    heatwave_unavailable_reason: str | None
    heatwave_temperature_basis: str | None
    heatwave_event_count: int
    longest_heatwave_days: int
    heatwave_events: list[dict[str, Any]]
    data_quality: DataQualitySummary
    metric_definitions: dict[str, Any]
    monthly_results: list[dict[str, Any]]

def build_metric_definitions(request: GlobalBatchCreate) -> dict:
    """Machine-readable definitions of derived metrics (see docs/metrics.md)."""
    return {
        "effective_cooling_hours": {
            "display_name": (
                "Estimated beneficial exposure hours under the configured "
                "daily exposure scenario"
            ),
            "formula": "beneficial_weighted_days * duration_minutes / 60",
            "interpretation": (
                "Sum over sampled days (weighted by the calendar days each "
                "sample represents) of the configured daily exposure "
                "duration, counted only when the sample is exposure-eligible "
                "and its time-weighted mean skin-temperature improvement is "
                ">= minimum_skin_improvement_c. It is not a measurement of "
                "hours during which cooling physically occurred."
            ),
            "inputs": {
                "local_start_hour": request.local_start_hour,
                "duration_minutes": request.duration_minutes,
                "minimum_skin_improvement_c": (
                    request.minimum_skin_improvement_c
                ),
                "minimum_air_temperature_c": (
                    request.minimum_air_temperature_c
                ),
                "minimum_solar_radiation_w_m2": (
                    request.minimum_solar_radiation_w_m2
                ),
                "exposure_match_mode": request.exposure_match_mode,
            },
            "statistics_window": (
                "[local_start_hour, local_start_hour + duration_minutes]; "
                "padding hours are excluded"
            ),
        }
    }


def round_optional(value: float | None, digits: int = 4) -> float | None:
    if value is None:
        return None
    return round(value, digits)


def is_exposure_eligible(
    *,
    mean_air_temperature_c: float,
    mean_solar_radiation_w_m2: float,
    request: GlobalBatchCreate,
) -> bool:
    conditions: list[bool] = []

    if request.minimum_air_temperature_c is not None:
        conditions.append(
            mean_air_temperature_c >= request.minimum_air_temperature_c
        )

    if request.minimum_solar_radiation_w_m2 is not None:
        conditions.append(
            mean_solar_radiation_w_m2
            >= request.minimum_solar_radiation_w_m2
        )

    if not conditions:
        return True

    if request.exposure_match_mode == "any":
        return any(conditions)

    return all(conditions)


def get_next_month_start(*, year: int, month: int) -> datetime:
    if month == 12:
        return datetime(year + 1, 1, 1)
    return datetime(year, month + 1, 1)


def summarize_skip_reasons(
    skipped: list[SkippedSample],
) -> dict[str, int]:
    reasons: dict[str, int] = {}
    for item in skipped:
        reasons[item.reason_code] = reasons.get(item.reason_code, 0) + 1
    return reasons


def summarize_month(
    *,
    month: int,
    samples: list[DailyAdaptationResult],
    skipped: list[SkippedSample] | None = None,
) -> MonthlyAdaptationResult:
    skipped = list(skipped or [])

    total_weighted_days = sum(s.weight_days for s in samples)

    eligible_samples = [s for s in samples if s.exposure_eligible]

    evaluated_weighted_days = sum(s.weight_days for s in eligible_samples)

    beneficial_weighted_days = sum(
        s.weight_days for s in samples if s.beneficial
    )

    exposure_coverage_percent = (
        evaluated_weighted_days / total_weighted_days * 100.0
        if total_weighted_days
        else 0.0
    )

    climate_adaptation_rate_percent = (
        beneficial_weighted_days / evaluated_weighted_days * 100.0
        if evaluated_weighted_days
        else None
    )

    average_skin_improvement_c = (
        sum(s.average_skin_improvement_c * s.weight_days for s in eligible_samples)
        / evaluated_weighted_days
        if evaluated_weighted_days
        else None
    )

    average_core_improvement_c = (
        sum(s.average_core_improvement_c * s.weight_days for s in eligible_samples)
        / evaluated_weighted_days
        if evaluated_weighted_days
        else None
    )

    maximum_skin_improvement_c = (
        max(s.maximum_skin_improvement_c for s in eligible_samples)
        if eligible_samples
        else None
    )

    return MonthlyAdaptationResult(
        month=month,
        sampled_day_count=len(samples),
        eligible_sample_count=len(eligible_samples),
        total_weighted_days=total_weighted_days,
        evaluated_weighted_days=evaluated_weighted_days,
        beneficial_weighted_days=beneficial_weighted_days,
        exposure_coverage_percent=round(exposure_coverage_percent, 4),
        climate_adaptation_rate_percent=round_optional(
            climate_adaptation_rate_percent
        ),
        average_skin_improvement_c=round_optional(average_skin_improvement_c),
        average_core_improvement_c=round_optional(average_core_improvement_c),
        maximum_skin_improvement_c=round_optional(maximum_skin_improvement_c),
        samples=samples,
        skipped_samples=skipped,
        skipped_weighted_days=sum(s.weight_days for s in skipped),
    )


def normalize_initial_monthly_results(
    *,
    request: GlobalBatchCreate,
    results: list[MonthlyAdaptationResult] | None,
) -> list[MonthlyAdaptationResult]:
    if not results:
        return []

    results_by_month: dict[int, MonthlyAdaptationResult] = {}

    for result in results:
        if request.start_month <= result.month <= request.end_month:
            results_by_month[result.month] = result

    return [results_by_month[m] for m in sorted(results_by_month)]


async def analyze_city_climate_adaptation(
    *,
    city_id: str,
    request: GlobalBatchCreate,
    progress_callback: ProgressCallback | None = None,
    checkpoint_callback: CheckpointCallback | None = None,
    initial_monthly_results: list[MonthlyAdaptationResult] | None = None,
) -> CityClimateAdaptationSummary:
    city = get_city(city_id)

    annual_plan = build_annual_sampling_plan(request)

    if not annual_plan:
        raise RuntimeError("No sampling dates were generated")

    total_sample_count = len(annual_plan)

    monthly_results = normalize_initial_monthly_results(
        request=request,
        results=initial_monthly_results,
    )

    completed_months = {r.month for r in monthly_results}

    completed_sample_count = sum(
        r.sampled_day_count + len(r.skipped_samples)
        for r in monthly_results
    )

    monthly_weather_payload_sha256: dict[str, str | None] = {}

    def report(progress: int, stage: str) -> None:
        if progress_callback is not None:
            progress_callback(max(0, min(progress, 100)), stage)

    def progress_now() -> int:
        return max(
            1,
            round(completed_sample_count / total_sample_count * 92),
        )

    for month in range(request.start_month, request.end_month + 1):
        if month in completed_months:
            report(
                progress_now(),
                f"restored_checkpoint_{request.year}-{month:02d}",
            )
            continue

        month_plan = build_month_sampling_plan(request=request, month=month)

        month_start = datetime(request.year, month, 1, 0, 0, 0)

        next_month_start = get_next_month_start(
            year=request.year, month=month
        )

        # The final simulation day may continue into the next month.
        prefetch_end = next_month_start + timedelta(
            hours=request.local_start_hour,
            minutes=request.duration_minutes,
        )

        report(
            progress_now(),
            f"prefetching_weather_{request.year}-{month:02d}",
        )

        # Monthly prefetch: do not require whole-month coverage here; each
        # sample slice enforces coverage for its own exposure window.
        month_weather = await get_historical_weather_range(
            city=city, start_time_local=month_start, end_time_local=prefetch_end,
            padding_hours=1, require_window_coverage=False,
            extra_variables=required_weather_variables(request.environment_assumptions),
        )

        monthly_weather_payload_sha256[f"{month:02d}"] = (
            month_weather.source.payload_sha256
        )

        month_samples: list[DailyAdaptationResult] = []
        month_skipped: list[SkippedSample] = []

        for sample_day in month_plan:
            start_time_local = datetime(
                sample_day.date_local.year,
                sample_day.date_local.month,
                sample_day.date_local.day,
                request.local_start_hour,
                0,
                0,
            )

            report(
                progress_now(),
                f"analyzing_{start_time_local:%Y-%m-%d}",
            )

            try:
                sample_weather = slice_weather_time_series(
                    weather=month_weather,
                    start_time_local=start_time_local,
                    duration_minutes=request.duration_minutes,
                    padding_hours=1,
                )

                simulation_request = WeatherSimulationRequest(
                    city_id=city.id,
                    start_time_local=start_time_local,
                    duration_minutes=request.duration_minutes,
                    output_interval_minutes=request.output_interval_minutes,
                    person=request.person,
                    control_material=request.control_material,
                    rc_material=request.rc_material,
                    environment_assumptions=request.environment_assumptions,
                )

                simulation = execute_weather_simulation_with_weather(
                    request=simulation_request,
                    weather=sample_weather,
                )

            except WeatherDataError as error:
                month_skipped.append(
                    SkippedSample(
                        sample_date_local=start_time_local,
                        weight_days=sample_day.weight_days,
                        reason_code=error.code,
                        message=str(error)[:500],
                    )
                )
                completed_sample_count += 1
                continue
            
            paired = pair_scenarios(simulation.control, simulation.radiative_cooling)

            exposure = compute_exposure_window_statistics(sample_weather)
            daily_maximum_air_temperature_c = compute_daily_maximum_air_temperature(
                month_weather,
                local_date=sample_day.date_local,
                timezone_name=city.timezone,
            )

            average_skin_improvement_c = paired.average_skin_c
            average_core_improvement_c = paired.average_core_c
            maximum_skin_improvement_c = paired.maximum_skin_c
            final_skin_improvement_c = paired.final_skin_c
            
            exposure_eligible = is_exposure_eligible(
                mean_air_temperature_c=exposure.mean_air_temperature_c,
                mean_solar_radiation_w_m2=exposure.mean_solar_radiation_w_m2,
                request=request,
            )

            beneficial = (
                exposure_eligible
                and average_skin_improvement_c
                >= request.minimum_skin_improvement_c
            )

            month_samples.append(
                DailyAdaptationResult(
                    sample_date_local=start_time_local,
                    weight_days=sample_day.weight_days,
                    mean_air_temperature_c=round(
                        exposure.mean_air_temperature_c, 4
                    ),
                    maximum_air_temperature_c=round(
                        exposure.maximum_air_temperature_c, 4
                    ),
                    mean_solar_radiation_w_m2=round(
                        exposure.mean_solar_radiation_w_m2, 4
                    ),
                    maximum_solar_radiation_w_m2=round(
                        exposure.maximum_solar_radiation_w_m2, 4
                    ),
                    exposure_eligible=exposure_eligible,
                    beneficial=beneficial,
                    average_skin_improvement_c=round(
                        average_skin_improvement_c, 4
                    ),
                    final_skin_improvement_c=round(
                        final_skin_improvement_c,
                        4,
                    ),
                    average_core_improvement_c=round(
                        average_core_improvement_c, 4
                    ),
                    maximum_skin_improvement_c=round(
                        maximum_skin_improvement_c, 4
                    ),
                    weather_from_cache=month_weather.source.from_cache,
                    daily_maximum_air_temperature_c=round_optional(daily_maximum_air_temperature_c),
                    mean_sky_temperature_c=_series_mean(simulation.radiative_cooling, "sky_temperature_c"),
                    mean_surround_temperature_c=_series_mean(
                        simulation.radiative_cooling, "surround_temperature_c"
                    ),
                )
            )

            completed_sample_count += 1

        monthly_result = summarize_month(
            month=month,
            samples=month_samples,
            skipped=month_skipped,
        )

        monthly_results.append(monthly_result)
        monthly_results.sort(key=lambda r: r.month)
        completed_months.add(month)

        if checkpoint_callback is not None:
            checkpoint_callback(
                list(monthly_results),
                month,
                completed_sample_count,
            )

    all_samples = [s for m in monthly_results for s in m.samples]
    all_skipped = [s for m in monthly_results for s in m.skipped_samples]

    eligible_samples = [s for s in all_samples if s.exposure_eligible]

    total_weighted_days = sum(s.weight_days for s in all_samples)

    evaluated_weighted_days = sum(s.weight_days for s in eligible_samples)

    beneficial_weighted_days = sum(
        s.weight_days for s in all_samples if s.beneficial
    )

    exposure_coverage_percent = (
        evaluated_weighted_days / total_weighted_days * 100.0
        if total_weighted_days
        else 0.0
    )

    climate_adaptation_rate_percent = (
        beneficial_weighted_days / evaluated_weighted_days * 100.0
        if evaluated_weighted_days
        else None
    )

    annual_average_skin_improvement_c = (
        sum(s.average_skin_improvement_c * s.weight_days for s in eligible_samples)
        / evaluated_weighted_days
        if evaluated_weighted_days
        else None
    )

    annual_average_core_improvement_c = (
        sum(s.average_core_improvement_c * s.weight_days for s in eligible_samples)
        / evaluated_weighted_days
        if evaluated_weighted_days
        else None
    )

    maximum_skin_improvement_c = (
        max(s.maximum_skin_improvement_c for s in eligible_samples)
        if eligible_samples
        else None
    )

    effective_cooling_hours = (
        beneficial_weighted_days * request.duration_minutes / 60.0
    )

    analytics = build_city_analytics(samples=all_samples, request=request)

    report(96, "generating_city_summary")

    return {
        "city_id": city.id,
        "city_name": city.name,
        "country": city.country,
        "latitude": city.latitude,
        "longitude": city.longitude,
        "climate_adaptation_rate_percent": round_optional(
            climate_adaptation_rate_percent
        ),
        "exposure_coverage_percent": round(exposure_coverage_percent, 4),
        "annual_average_skin_improvement_c": round_optional(
            annual_average_skin_improvement_c
        ),
        "annual_average_core_improvement_c": round_optional(
            annual_average_core_improvement_c
        ),
        "maximum_skin_improvement_c": round_optional(
            maximum_skin_improvement_c
        ),
        "effective_cooling_hours": round(effective_cooling_hours, 2),
        "sampled_day_count": len(all_samples),
        "eligible_sample_count": len(eligible_samples),
        "evaluated_weighted_days": evaluated_weighted_days,
        "beneficial_weighted_days": beneficial_weighted_days,
        "completed_month_count": len(monthly_results),
        # Analytics 分位數欄位 (防護 Key 不存在)
        "skin_improvement_p50_c": analytics.get("skin_improvement_p50_c"),
        "skin_improvement_p90_c": analytics.get("skin_improvement_p90_c"),
        "skin_improvement_p95_c": analytics.get("skin_improvement_p95_c"),
        "core_improvement_p50_c": analytics.get("core_improvement_p50_c"),
        "core_improvement_p90_c": analytics.get("core_improvement_p90_c"),
        "core_improvement_p95_c": analytics.get("core_improvement_p95_c"),
        # Analytics 熱浪分析欄位 (包含條件性與預設 Key，固定回傳 schema)
        "heatwave_analysis_available": analytics.get(
            "heatwave_analysis_available", False
        ),
        "heatwave_unavailable_reason": analytics.get(
            "heatwave_unavailable_reason"
        ),
        "heatwave_temperature_basis": analytics.get(
            "heatwave_temperature_basis"
        ),
        "heatwave_event_count": analytics.get("heatwave_event_count", 0),
        "longest_heatwave_days": analytics.get("longest_heatwave_days", 0),
        "heatwave_events": analytics.get("heatwave_events", []),
        "data_quality": {
            "skipped_sample_count": len(all_skipped),
            "skipped_weighted_days": sum(s.weight_days for s in all_skipped),
            "skip_reasons": summarize_skip_reasons(all_skipped),
            "monthly_weather_payload_sha256": monthly_weather_payload_sha256,
        },
        "metric_definitions": build_metric_definitions(request),
        "monthly_results": [
            r.model_dump(mode="json") for r in monthly_results
        ],
    }

def _series_mean(result, attribute: str) -> float | None:
    points = [
        (p.minute, getattr(p, attribute))
        for p in result.time_series
        if getattr(p, attribute, None) is not None
    ]
    if not points:
        return None
    return round(time_weighted_mean([m for m, _ in points], [v for _, v in points]), 4)
```

### File: `backend/app/services/climate_analytics.py`
```python
from __future__ import annotations

import math
from datetime import timedelta
from typing import Iterable

from app.schemas.global_batch import (
    DailyAdaptationResult,
    GlobalBatchCreate,
    HeatwaveEvent,
)

HEATWAVE_TEMPERATURE_BASIS = "local_calendar_day_maximum_air_temperature"

def _daily_maximum(sample: DailyAdaptationResult) -> float:
    if sample.daily_maximum_air_temperature_c is None:
        raise ValueError(
            "Heatwave detection requires daily_maximum_air_temperature_c "
            f"(missing for {sample.sample_date_local.date()})"
        )
    return sample.daily_maximum_air_temperature_c

def weighted_percentile(
    values: Iterable[tuple[float, int]],
    percentile: float,
) -> float | None:
    normalized = sorted(
        (
            float(value),
            int(weight),
        )
        for value, weight in values
        if weight > 0 and math.isfinite(value)
    )

    if not normalized:
        return None

    if percentile < 0.0 or percentile > 100.0:
        raise ValueError(
            "percentile must be between 0 and 100"
        )

    total_weight = sum(
        weight
        for _, weight in normalized
    )

    target_weight = (
        percentile
        / 100.0
        * total_weight
    )

    cumulative_weight = 0

    for value, weight in normalized:
        cumulative_weight += weight

        if cumulative_weight >= target_weight:
            return value

    return normalized[-1][0]


def round_optional(
    value: float | None,
    digits: int = 4,
) -> float | None:
    if value is None:
        return None

    return round(value, digits)


def build_heatwave_event(
    samples: list[DailyAdaptationResult],
) -> HeatwaveEvent:
    temperatures = [_daily_maximum(s) for s in samples]

    skin_improvements = [
        sample.average_skin_improvement_c
        for sample in samples
    ]

    p90 = weighted_percentile(
        (
            (
                improvement,
                1,
            )
            for improvement in skin_improvements
        ),
        percentile=90,
    )

    return HeatwaveEvent(
        start_date_local=samples[0].sample_date_local,
        end_date_local=samples[-1].sample_date_local,
        duration_days=len(samples),
        mean_maximum_air_temperature_c=round(
            sum(temperatures) / len(temperatures),
            4,
        ),
        peak_air_temperature_c=round(
            max(temperatures),
            4,
        ),
        mean_skin_improvement_c=round(
            sum(skin_improvements)
            / len(skin_improvements),
            4,
        ),
        p90_skin_improvement_c=round(
            p90 or 0.0,
            4,
        ),
        beneficial_day_count=sum(
            1
            for sample in samples
            if sample.beneficial
        ),
    )


def detect_heatwave_events(
    *,
    samples: list[DailyAdaptationResult],
    temperature_threshold_c: float,
    minimum_consecutive_days: int,
) -> list[HeatwaveEvent]:
    ordered_samples = sorted(
        samples,
        key=lambda sample: sample.sample_date_local,
    )

    events: list[HeatwaveEvent] = []
    current_event: list[DailyAdaptationResult] = []

    def flush_event() -> None:
        nonlocal current_event

        if (
            len(current_event)
            >= minimum_consecutive_days
        ):
            events.append(
                build_heatwave_event(
                    current_event
                )
            )

        current_event = []

    for sample in ordered_samples:
        qualifies = _daily_maximum(sample) >= temperature_threshold_c

        if not qualifies:
            flush_event()
            continue

        if current_event:
            expected_date = (
                current_event[-1].sample_date_local
                + timedelta(days=1)
            ).date()

            if (
                sample.sample_date_local.date()
                != expected_date
            ):
                flush_event()

        current_event.append(sample)

    flush_event()

    return events


def build_city_analytics(
    *,
    samples: list[DailyAdaptationResult],
    request: GlobalBatchCreate,
) -> dict:
    eligible_samples = [
        sample
        for sample in samples
        if sample.exposure_eligible
    ]

    skin_values = [
        (
            sample.average_skin_improvement_c,
            sample.weight_days,
        )
        for sample in eligible_samples
    ]

    core_values = [
        (
            sample.average_core_improvement_c,
            sample.weight_days,
        )
        for sample in eligible_samples
    ]

    configuration_allows_heatwave = (
        request.enable_heatwave_analysis
        and request.analysis_resolution == "daily"
        and request.daily_stride_days == 1
    )
    daily_maximum_available = all(
        s.daily_maximum_air_temperature_c is not None for s in samples
    )

    heatwave_available = configuration_allows_heatwave and daily_maximum_available

    heatwave_unavailable_reason: str | None = None
    if not configuration_allows_heatwave:
        heatwave_unavailable_reason = "requires daily resolution with a one-day stride"
    elif not daily_maximum_available:
        heatwave_unavailable_reason = (
            "one or more samples lack a full-day maximum "
            "(checkpoint predates Stage 6 or weather did not cover the day)"
        )

    heatwave_events: list[HeatwaveEvent] = []

    if heatwave_available:
        heatwave_events = detect_heatwave_events(
            samples=samples,
            temperature_threshold_c=(
                request
                .heatwave_temperature_threshold_c
            ),
            minimum_consecutive_days=(
                request
                .heatwave_minimum_consecutive_days
            ),
        )

    longest_heatwave_days = (
        max(
            event.duration_days
            for event in heatwave_events
        )
        if heatwave_events
        else 0
    )

    return {
        "skin_improvement_p50_c": round_optional(
            weighted_percentile(
                skin_values,
                50,
            )
        ),
        "skin_improvement_p90_c": round_optional(
            weighted_percentile(
                skin_values,
                90,
            )
        ),
        "skin_improvement_p95_c": round_optional(
            weighted_percentile(
                skin_values,
                95,
            )
        ),
        "core_improvement_p50_c": round_optional(
            weighted_percentile(
                core_values,
                50,
            )
        ),
        "core_improvement_p90_c": round_optional(
            weighted_percentile(
                core_values,
                90,
            )
        ),
        "core_improvement_p95_c": round_optional(
            weighted_percentile(
                core_values,
                95,
            )
        ),
        "heatwave_analysis_available": heatwave_available,
        "heatwave_unavailable_reason": heatwave_unavailable_reason,
        "heatwave_temperature_basis": HEATWAVE_TEMPERATURE_BASIS,

        "heatwave_event_count": (
            len(heatwave_events)
            if heatwave_available
            else None
        ),
        "longest_heatwave_days": (
            longest_heatwave_days
            if heatwave_available
            else None
        ),
        "heatwave_events": [
            event.model_dump(
                mode="json"
            )
            for event in heatwave_events
        ],
    }
```

### File: `backend/app/services/clothing.py`
```python
"""Clothing dry and evaporative resistances and area factor (Stage 3).

Dry pathway (see two_node.clothing_surface_temperature_c)
    (T_sk - T_cl) / R_cl = f_cl * [h_c (T_cl - T_a) + eps_cl sigma (T_cl^4 - T_env^4)]

Evaporative pathway
    E_max = (P_sk - P_a) / (Re,cl + Re,a)          [W/m^2]
    Re,a  = 1 / (LR * f_cl * h_c)                  [m^2 kPa/W]
    Re,cl = material value, or R_cl / (LR * i_cl)  when not supplied

f_cl = material value, or 1 + clothing_area_factor_slope * clo.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from app.schemas.simulation import MaterialInput
from app.services.model_parameters import get_parameter_value


CLO_TO_SI = get_parameter_value("clo_to_si")
LEWIS_RELATION = get_parameter_value("lewis_relation")
CLOTHING_VAPOR_PERMEATION_EFFICIENCY = get_parameter_value(
    "clothing_vapor_permeation_efficiency"
)
CLOTHING_AREA_FACTOR_SLOPE = get_parameter_value("clothing_area_factor_slope")

ParameterSourceLabel = Literal["material_input", "derived_from_clo"]


@dataclass(frozen=True)
class ClothingResistances:
    dry_resistance_m2k_w: float
    evaporative_resistance_m2kpa_w: float
    evaporative_resistance_source: ParameterSourceLabel
    infrared_transmittance: float
    area_factor: float
    area_factor_source: ParameterSourceLabel
    infrared_emissivity_window: float | None = None   # ← 新增
    
    @property
    def evaporative_resistance_m2pa_w(self) -> float:
        return self.evaporative_resistance_m2kpa_w * 1000.0

    @property
    def is_nude(self) -> bool:
        return self.dry_resistance_m2k_w <= 0.0


def derive_evaporative_resistance_m2pa_w(clothing_insulation_clo: float) -> float:
    """Re,cl = R_cl / (LR * i_cl), expressed in m^2 Pa/W."""
    dry_resistance = CLO_TO_SI * clothing_insulation_clo
    return (
        dry_resistance
        / (LEWIS_RELATION * CLOTHING_VAPOR_PERMEATION_EFFICIENCY)
        * 1000.0
    )


def derive_clothing_area_factor(clothing_insulation_clo: float) -> float:
    """f_cl = 1 + slope * clo."""
    return 1.0 + CLOTHING_AREA_FACTOR_SLOPE * clothing_insulation_clo


def resolve_clothing(material: MaterialInput) -> ClothingResistances:
    dry_resistance = CLO_TO_SI * material.clothing_insulation_clo

    if material.evaporative_resistance_m2pa_w is not None:
        evaporative_m2pa_w = material.evaporative_resistance_m2pa_w
        evaporative_source: ParameterSourceLabel = "material_input"
    else:
        evaporative_m2pa_w = derive_evaporative_resistance_m2pa_w(
            material.clothing_insulation_clo
        )
        evaporative_source = "derived_from_clo"

    if material.clothing_area_factor is not None:
        area_factor = material.clothing_area_factor
        area_factor_source: ParameterSourceLabel = "material_input"
    else:
        area_factor = derive_clothing_area_factor(material.clothing_insulation_clo)
        area_factor_source = "derived_from_clo"

    return ClothingResistances(
        dry_resistance_m2k_w=dry_resistance,
        evaporative_resistance_m2kpa_w=evaporative_m2pa_w / 1000.0,
        evaporative_resistance_source=evaporative_source,
        infrared_transmittance=material.infrared_transmittance,
        area_factor=area_factor,
        area_factor_source=area_factor_source,
        infrared_emissivity_window=material.infrared_emissivity_window,  # ← 新增
    )


def air_layer_evaporative_resistance_m2kpa_w(
    convection_coefficient: float,
    area_factor: float,
) -> float:
    return 1.0 / (LEWIS_RELATION * area_factor * convection_coefficient)


def maximum_evaporation_w_m2(
    clothing: ClothingResistances,
    convection_coefficient: float,
    skin_vapor_pressure_kpa: float,
    ambient_vapor_pressure_kpa: float,
) -> float:
    total_resistance = (
        clothing.evaporative_resistance_m2kpa_w
        + air_layer_evaporative_resistance_m2kpa_w(
            convection_coefficient, clothing.area_factor
        )
    )
    return max(
        0.0,
        (skin_vapor_pressure_kpa - ambient_vapor_pressure_kpa) / total_resistance,
    )


def assumptions_applied(
    clothing: ClothingResistances,
    *,
    solar_split_available: bool = False,
) -> list[str]:
    notes: list[str] = []

    if clothing.evaporative_resistance_source == "derived_from_clo":
        notes.append(
            "evaporative_resistance_m2pa_w not supplied; derived as "
            f"R_cl / (LR * i_cl) with i_cl = {CLOTHING_VAPOR_PERMEATION_EFFICIENCY} "
            f"-> {clothing.evaporative_resistance_m2pa_w:.2f} m^2 Pa/W"
        )

    if clothing.area_factor_source == "derived_from_clo":
        notes.append(
            "clothing_area_factor not supplied; derived as "
            f"1 + {CLOTHING_AREA_FACTOR_SLOPE} * clo -> {clothing.area_factor:.4f}"
        )

    if clothing.infrared_transmittance > 0.0:
        notes.append(
            "infrared_transmittance > 0: transmitted skin emission is a parallel "
            "path that bypasses the clothing surface balance (first-order model)"
        )

    notes.append(
        "solar radiation absorbed by the textile enters the clothing surface "
        "balance; transmitted solar reaches the skin node directly. "
        "absorbed_solar_to_body_fraction is ignored (ADR 0005)"
    )

    if solar_split_available:
        notes.append(
            "body-incident shortwave = f_p * DNI + 0.5 f_eff F_sky DHI "
            "+ 0.5 f_eff rho_g GHI (ASHRAE 55 Appendix C geometry, ADR 0006)"
        )
    else:
        notes.append(
            "no beam/diffuse split supplied; GHI treated as beam on the "
            "projected area (legacy Stage 0-4 geometry, ADR 0006)"
        )

    return notes
```

### File: `backend/app/services/environment.py`
```python
"""Explicit rules for deriving boundary conditions that ERA5 does not provide
(Stage 2; Stage 5 ground albedo; Stage 11 physical sky and ground, ADR 0008).

Defaults reproduce the Stage 1 estimates exactly.

``mean_radiant_temperature`` in EnvironmentInput is used by the model only as
the longwave temperature of the NON-SKY part of the view. The legacy rule
``air_plus_solar_linear`` raises it with GHI although body shortwave is
computed explicitly since Stage 5, i.e. it counts the sun twice (ADR 0008).
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


MeanRadiantTemperatureMethod = Literal[
    "air_plus_solar_linear",   # legacy: T_air + min(cap, gain * GHI)
    "equal_to_air",            # shaded / indoor-like
    "ground_energy_balance",   # Stage 11: steady ground surface balance
]

SkyTemperatureMethod = Literal[
    "humidity_offset",   # T_sky = T_air - (base + range * (1 - RH))
    "fixed_offset",      # T_sky = T_air - fixed_offset
    "swinbank",          # T_sky[K] = 0.0552 * T_air[K]^1.5 (clear sky)
    "brutsaert_cloud",   # Stage 11: Brutsaert + cloud fraction
]

RadiationTimeConvention = Literal[
    "instantaneous_linear",
    "preceding_hour_mean_step",
]

_STAGE1 = {"source_type": "assumed", "reference": "Stage 1 prototype"}


class EnvironmentAssumptions(BaseModel):
    model_config = ConfigDict(extra="forbid")

    mean_radiant_temperature_method: MeanRadiantTemperatureMethod = Field(
        default="air_plus_solar_linear", json_schema_extra=_STAGE1,
    )
    solar_mrt_gain_k_per_w_m2: float = Field(
        default=0.012, ge=0.0, le=0.05,
        description="MRT rise per W/m^2 of GHI (air_plus_solar_linear only)",
        json_schema_extra=_STAGE1,
    )
    solar_mrt_gain_cap_k: float = Field(
        default=15.0, ge=0.0, le=40.0,
        description="Upper bound of the solar MRT rise",
        json_schema_extra=_STAGE1,
    )

    sky_temperature_method: SkyTemperatureMethod = Field(
        default="humidity_offset", json_schema_extra=_STAGE1,
    )
    sky_offset_base_k: float = Field(
        default=5.0, ge=0.0, le=40.0,
        description="humidity_offset: depression at 100 % RH", json_schema_extra=_STAGE1,
    )
    sky_offset_humidity_range_k: float = Field(
        default=10.0, ge=0.0, le=40.0,
        description="humidity_offset: additional depression at 0 % RH", json_schema_extra=_STAGE1,
    )
    fixed_sky_offset_k: float = Field(
        default=15.0, ge=0.0, le=50.0,
        description="fixed_offset: T_air - T_sky", json_schema_extra=_STAGE1,
    )

    sky_view_factor: float = Field(
        default=0.5, ge=0.0, le=1.0,
        description="Fraction of the body's radiative view occupied by sky",
        json_schema_extra={
            "source_type": "assumed",
            "reference": "Standing person on an open, unobstructed site",
        },
    )

    wind_speed_scaling_factor: float = Field(
        default=1.0, gt=0.0, le=1.5,
        description=(
            "Multiplier from ERA5 10 m wind to body-height wind. 1.0 keeps "
            "Stage 1 behaviour; ~0.67 approximates 1.1 m height via a "
            "logarithmic profile over open terrain."
        ),
        json_schema_extra=_STAGE1,
    )

    ground_albedo: float = Field(
        default=0.2, ge=0.0, le=1.0,
        description="Shortwave reflectance of the ground surface",
        json_schema_extra={
            "source_type": "assumed",
            "reference": "Typical dry soil / urban pavement (0.15-0.25)",
        },
    )

    radiation_time_convention: RadiationTimeConvention = Field(
        default="instantaneous_linear",
        json_schema_extra={
            "source_type": "assumed",
            "reference": "Open-Meteo hourly parameter definition (preceding hour mean)",
        },
    )

    # Stage 11 (ADR 0008), ground_energy_balance only.
    ground_emissivity: float = Field(
        default=0.95, ge=0.8, le=1.0,
        description="Longwave emissivity of the ground surface",
        json_schema_extra={
            "source_type": "assumed",
            "reference": "Typical soil, asphalt and concrete (0.92-0.97)",
        },
    )
    ground_soil_conductance_w_m2k: float = Field(
        default=15.0, ge=2.0, le=200.0,
        description=(
            "Effective conductance between the ground surface and the ERA5 "
            "0-7 cm soil layer (k/d)"
        ),
        json_schema_extra={
            "source_type": "assumed",
            "reference": "Order of magnitude for dry soil to pavement; not measured",
        },
    )

    def describe(self) -> list[str]:
        """Human-readable summary written into ``environment_model_note``."""
        if self.mean_radiant_temperature_method == "air_plus_solar_linear":
            mrt = (
                f"T_mrt = T_air + min({self.solar_mrt_gain_cap_k} K, "
                f"{self.solar_mrt_gain_k_per_w_m2} K/(W/m^2) * GHI)"
            )
        elif self.mean_radiant_temperature_method == "ground_energy_balance":
            mrt = (
                "Non-sky surroundings = ground surface temperature from "
                "(1 - rho_g) GHI + eps_g sigma T_sky^4 = eps_g sigma T_g^4 "
                "+ h_g (T_g - T_air) + K (T_g - T_soil,0-7cm), "
                f"eps_g = {self.ground_emissivity}, "
                f"K = {self.ground_soil_conductance_w_m2k} W/(m^2 K)"
            )
        else:
            mrt = "T_mrt = T_air"

        if self.sky_temperature_method == "humidity_offset":
            sky = (
                f"T_sky = T_air - ({self.sky_offset_base_k} K + "
                f"{self.sky_offset_humidity_range_k} K * (1 - RH))"
            )
        elif self.sky_temperature_method == "fixed_offset":
            sky = f"T_sky = T_air - {self.fixed_sky_offset_k} K"
        elif self.sky_temperature_method == "brutsaert_cloud":
            sky = (
                "T_sky = eps_sky^0.25 T_air, eps_sky = c + (1 - c) * 1.24 "
                "(e_a/T_air)^(1/7), c = ERA5 total cloud cover "
                "(Brutsaert 1975; Crawford & Duchon 1999 form)"
            )
        else:
            sky = "T_sky[K] = 0.0552 * T_air[K]^1.5 (Swinbank 1963, clear sky)"

        if self.radiation_time_convention == "preceding_hour_mean_step":
            radiation = (
                "GHI/DNI/DHI are treated as preceding-hour means held constant "
                "over (t-1h, t] (energy-conserving)."
            )
        else:
            radiation = (
                "GHI/DNI/DHI hourly means are treated as instantaneous values at "
                "the stamped hour and interpolated linearly (approximation; "
                "shifts the solar profile by up to 30 min)."
            )

        return [
            "Air temperature, relative humidity, 10 m wind speed and GHI are "
            "taken from ERA5 via Open-Meteo.",
            mrt,
            sky,
            f"Sky view factor = {self.sky_view_factor}",
            f"Body-height wind = {self.wind_speed_scaling_factor} * ERA5 10 m wind",
            "Direct normal and diffuse horizontal irradiance are taken from "
            "ERA5; the body-incident shortwave follows ASHRAE 55 Appendix C "
            "geometry (ADR 0006).",
            f"Ground albedo = {self.ground_albedo}",
            radiation,
        ]
```

### File: `backend/app/services/environment_model.py`
```python
"""Derive model boundary conditions from ERA5 variables (Stage 2, 11)."""

from __future__ import annotations

from app.schemas.environment import EnvironmentAssumptions
from app.schemas.simulation import EnvironmentInput
from app.services.ground_surface import (
    brutsaert_cloud_sky_temperature_c,
    solve_ground_surface_temperature_c,
)
from app.services.model_parameters import get_parameter_value
from app.services.weather_quality import WeatherMissingVariableError


SWINBANK_COEFFICIENT = get_parameter_value("swinbank_coefficient")
KELVIN_OFFSET = 273.15

CLOUD_COVER = "cloud_cover"
SOIL_TEMPERATURE = "soil_temperature_0_to_7cm"


def required_weather_variables(assumptions: EnvironmentAssumptions) -> tuple[str, ...]:
    """Open-Meteo hourly variables needed beyond the Stage 10 set. Empty for defaults,
    so default requests, caches and payload hashes are unchanged."""
    needed: list[str] = []
    if assumptions.sky_temperature_method == "brutsaert_cloud":
        needed.append(CLOUD_COVER)
    if assumptions.mean_radiant_temperature_method == "ground_energy_balance":
        needed.append(SOIL_TEMPERATURE)
    return tuple(needed)


def _require(value: float | None, name: str) -> float:
    if value is None:
        raise WeatherMissingVariableError(
            f"Weather variable {name} is required by the selected environment "
            "assumptions but is missing",
            context={"variable": name},
        )
    return float(value)


def _sky_temperature_c(
    air: float, relative_humidity: float, cloud: float | None, a: EnvironmentAssumptions
) -> float:
    if a.sky_temperature_method == "humidity_offset":
        return air - (
            a.sky_offset_base_k + a.sky_offset_humidity_range_k * (1.0 - relative_humidity / 100.0)
        )
    if a.sky_temperature_method == "fixed_offset":
        return air - a.fixed_sky_offset_k
    if a.sky_temperature_method == "brutsaert_cloud":
        return brutsaert_cloud_sky_temperature_c(air, relative_humidity, _require(cloud, CLOUD_COVER))
    return SWINBANK_COEFFICIENT * (air + KELVIN_OFFSET) ** 1.5 - KELVIN_OFFSET


def derive_environment(
    *,
    air_temperature_c: float,
    relative_humidity_percent: float,
    wind_speed_m_s: float,
    ghi_w_m2: float,
    assumptions: EnvironmentAssumptions,
    direct_normal_irradiance_w_m2: float | None = None,
    diffuse_horizontal_irradiance_w_m2: float | None = None,
    cloud_cover_percent: float | None = None,
    soil_temperature_c: float | None = None,
) -> EnvironmentInput:
    air = float(air_temperature_c)
    ghi = max(0.0, float(ghi_w_m2))
    relative_humidity = min(100.0, max(0.0, float(relative_humidity_percent)))
    wind = max(0.0, float(wind_speed_m_s)) * assumptions.wind_speed_scaling_factor
    zone_view_separation = assumptions.zone_view_separation
    sky = _sky_temperature_c(air, relative_humidity, cloud_cover_percent, assumptions)

    method = assumptions.mean_radiant_temperature_method
    if method == "air_plus_solar_linear":
        mean_radiant = air + min(
            assumptions.solar_mrt_gain_cap_k,
            assumptions.solar_mrt_gain_k_per_w_m2 * ghi,
        )
    elif method == "ground_energy_balance":
        mean_radiant = solve_ground_surface_temperature_c(
            air_c=air,
            sky_c=sky,
            ghi_w_m2=ghi,
            albedo=assumptions.ground_albedo,
            wind_speed_m_s=wind,
            soil_c=_require(soil_temperature_c, SOIL_TEMPERATURE),
            emissivity=assumptions.ground_emissivity,
            conductance_w_m2k=assumptions.ground_soil_conductance_w_m2k,
        )
    else:
        mean_radiant = air

    dni = None if direct_normal_irradiance_w_m2 is None else max(0.0, float(direct_normal_irradiance_w_m2))
    dhi = None if diffuse_horizontal_irradiance_w_m2 is None else max(0.0, float(diffuse_horizontal_irradiance_w_m2))
    if (dni is None) != (dhi is None):
        raise ValueError("DNI and DHI must be supplied together")

    return EnvironmentInput(
        air_temperature_c=air,
        mean_radiant_temperature_c=mean_radiant,
        sky_temperature_c=sky,
        relative_humidity_percent=relative_humidity,
        wind_speed_m_s=wind,
        solar_radiation_w_m2=ghi,
        sky_view_factor=assumptions.sky_view_factor,
        direct_normal_irradiance_w_m2=dni,
        diffuse_horizontal_irradiance_w_m2=dhi,
        ground_albedo=assumptions.ground_albedo,
        zone_view_separation=zone_view_separation,   # was missing
    )
```

### File: `backend/app/services/execution_profile.py`
```python
from app.schemas.global_batch import (
    ExecutionProfile,
    GlobalBatchCreate,
)
from app.services.annual_sampling import (
    estimate_sample_count,
)


def resolve_execution_profile(
    request: GlobalBatchCreate,
) -> ExecutionProfile:
    if request.execution_profile != "auto":
        return request.execution_profile

    samples_per_city = estimate_sample_count(
        request
    )

    if (
        samples_per_city >= 180
        or len(request.city_ids) >= 20
    ):
        return "large"

    return "standard"


def resolve_queue_name(
    request: GlobalBatchCreate,
) -> str:
    profile = resolve_execution_profile(
        request
    )

    if profile == "large":
        return "global_large"

    return "global_standard"
```

### File: `backend/app/services/exposure_statistics.py`
```python
"""Exposure-window statistics (Stage 1, PR-3).

Scenario-level weather statistics are computed strictly over the exposure
window ``[requested_start_time, requested_end_time]`` using time-weighted
(trapezoidal) integration of the piecewise-linear hourly series. They are
therefore invariant to the interpolation padding attached to
``weather.points``.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from datetime import datetime, date, time, timedelta, timezone
from zoneinfo import ZoneInfo

import numpy as np

from app.schemas.weather import WeatherTimeSeries
from app.services.weather_quality import (
    WeatherInsufficientCoverageError,
)


@dataclass(frozen=True)
class ExposureWindowStatistics:
    window_start: datetime
    window_end: datetime
    mean_air_temperature_c: float
    maximum_air_temperature_c: float
    mean_solar_radiation_w_m2: float
    maximum_solar_radiation_w_m2: float


def time_weighted_mean(
    times: Sequence[float],
    values: Sequence[float],
) -> float:
    """Trapezoidal time average. Falls back to the arithmetic mean for a
    single point or a zero-length span."""
    t = np.asarray(times, dtype=float)
    y = np.asarray(values, dtype=float)

    if t.size == 0:
        raise ValueError("Cannot average an empty series")

    if t.size == 1 or t[-1] <= t[0]:
        return float(np.mean(y))

    return float(np.trapezoid(y, t) / (t[-1] - t[0]))


def _window_knots(
    relative_seconds: np.ndarray,
    start_s: float,
    end_s: float,
) -> np.ndarray:
    inside = relative_seconds[
        (relative_seconds > start_s) & (relative_seconds < end_s)
    ]
    return np.concatenate(([start_s], inside, [end_s]))


def compute_exposure_window_statistics(
    weather: WeatherTimeSeries,
    *,
    window_start: datetime | None = None,
    window_end: datetime | None = None,
) -> ExposureWindowStatistics:
    """Time-weighted mean / maximum over the exposure window only."""
    window_start = window_start or weather.requested_start_time
    window_end = window_end or weather.requested_end_time

    if window_end <= window_start:
        raise ValueError("window_end must be after window_start")

    origin = weather.points[0].timestamp

    relative_seconds = np.asarray(
        [elapsed_seconds(p.timestamp, origin) for p in weather.points],
        dtype=float,
    )

    start_s = elapsed_seconds(window_start, origin)
    end_s = elapsed_seconds(window_end, origin)

    if start_s < relative_seconds[0] - 1e-6 or end_s > relative_seconds[-1] + 1e-6:
        raise WeatherInsufficientCoverageError(
            "Weather series does not cover the requested statistics window "
            f"{window_start.isoformat()} to {window_end.isoformat()}"
        )

    knots = _window_knots(relative_seconds, start_s, end_s)

    temperatures = np.interp(
        knots,
        relative_seconds,
        [p.air_temperature_c for p in weather.points],
    )

    ghi = np.maximum(
        0.0,
        np.interp(
            knots,
            relative_seconds,
            [p.ghi_w_m2 for p in weather.points],
        ),
    )

    return ExposureWindowStatistics(
        window_start=window_start,
        window_end=window_end,
        mean_air_temperature_c=time_weighted_mean(knots, temperatures),
        maximum_air_temperature_c=float(temperatures.max()),
        mean_solar_radiation_w_m2=time_weighted_mean(knots, ghi),
        maximum_solar_radiation_w_m2=float(ghi.max()),
    )
    
def elapsed_seconds(later: datetime, earlier: datetime) -> float:
    """UTC-based elapsed time. Safe across tzinfo objects and DST transitions
    (plain aware-datetime subtraction ignores tzinfo when both share it)."""
    return later.timestamp() - earlier.timestamp()


def compute_daily_maximum_air_temperature(
    weather: WeatherTimeSeries,
    *,
    local_date: date,
    timezone_name: str,
) -> float | None:
    """Maximum air temperature over one local calendar day [00:00, 24:00).

    Returns None when the series does not fully bracket the day, so that a
    partial day is never reported as a daily maximum. Used for heatwave
    detection (Stage 6); the exposure-window maximum is a different quantity.
    """
    tz = ZoneInfo(timezone_name)
    day_start = datetime.combine(local_date, time(0), tzinfo=tz)
    day_end = datetime.combine(local_date + timedelta(days=1), time(0), tzinfo=tz)

    points = weather.points
    if elapsed_seconds(points[0].timestamp, day_start) > 1e-6:
        return None
    if elapsed_seconds(day_end, points[-1].timestamp) > 1e-6:
        return None

    origin = points[0].timestamp
    relative = np.asarray([elapsed_seconds(p.timestamp, origin) for p in points])
    temperatures = np.asarray([p.air_temperature_c for p in points])

    start_s = elapsed_seconds(day_start, origin)
    end_s = elapsed_seconds(day_end, origin)

    knots = _window_knots(relative, start_s, end_s)
    return float(np.interp(knots, relative, temperatures).max())
```

### File: `backend/app/services/gagge_benchmark.py`
```python
"""Transient comparison of the platform prototype with the Gagge two-node model.

Alignment
---------
The Gagge model has a single radiant temperature, no solar term, a fixed
clothing emissivity of 0.95 and derives Re,cl and f_cl from clo. The prototype
run is therefore configured so that both models see the same boundary
conditions; every alignment step is reported in ``alignment_applied``.
This is a diagnostic comparison, not an equivalence proof: convection
correlations, the clothing surface balance and the wettedness bookkeeping
differ by design.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

import numpy as np
from pythermalcomfort.models import two_nodes_gagge

from app.schemas.simulation import (
    BenchmarkMetric,
    BenchmarkSeriesPoint,
    GaggeBenchmarkRequest,
    GaggeBenchmarkResponse,
    GaggeModelOutput,
    PrototypeBenchmarkOutput,
    ReferencePortParity,
)
from app.services.gagge_reference import run_gagge_reference
from app.services.two_node import simulate_material


LIBRARY_DURATION_MINUTES = 60
REFERENCE_CLOTHING_EMISSIVITY = 0.95


def _to_float(value: object) -> float:
    """Convert a Python float, NumPy scalar or single-element array to float."""
    if hasattr(value, "item"):
        return float(value.item())
    return float(value)


def _library_version() -> str:
    try:
        return version("pythermalcomfort")
    except PackageNotFoundError:
        return "unknown"


def _metric(
    prototype: np.ndarray,
    reference: np.ndarray,
    tolerance: float,
) -> BenchmarkMetric:
    difference = prototype - reference
    maximum = float(np.max(np.abs(difference)))
    return BenchmarkMetric(
        final_difference_c=round(float(difference[-1]), 4),
        maximum_absolute_difference_c=round(maximum, 4),
        root_mean_square_difference_c=round(float(np.sqrt(np.mean(difference**2))), 4),
        tolerance_c=tolerance,
        passed=maximum <= tolerance,
    )


def run_gagge_benchmark(request: GaggeBenchmarkRequest) -> GaggeBenchmarkResponse:
    alignment: list[str] = []

    # --- boundary conditions the reference model can represent ----------------
    environment = request.environment.model_copy(
        update={
            "solar_radiation_w_m2": 0.0,
            "direct_normal_irradiance_w_m2": 0.0,
            "diffuse_horizontal_irradiance_w_m2": 0.0,
            "sky_view_factor": 0.0,
            "sky_temperature_c": request.environment.mean_radiant_temperature_c,
        }
    )
    alignment.append("solar_radiation_w_m2 set to 0 (reference has no solar term)")
    alignment.append(
        "sky_view_factor set to 0 and sky temperature set equal to the mean "
        "radiant temperature (reference has a single radiant temperature)"
    )

    material = request.material.model_copy(
        update={
            "infrared_emissivity": REFERENCE_CLOTHING_EMISSIVITY,
            "infrared_transmittance": 0.0,
            "evaporative_resistance_m2pa_w": None,
            "clothing_area_factor": None,
            "infrared_emissivity_window": None,
            "infrared_emissivity_ground_facing": None,
        }
    )
    alignment.append(
        f"infrared_emissivity set to {REFERENCE_CLOTHING_EMISSIVITY} and "
        "infrared_transmittance to 0 (fixed in the reference)"
    )
    alignment.append(
        "evaporative_resistance_m2pa_w and clothing_area_factor derived from clo "
        "(the reference accepts clo only), and the material is treated as gray, "
        "and the material is treated as a uniform gray emitter"
    )

    # --- prototype ------------------------------------------------------------
    prototype = simulate_material(
        duration_minutes=request.duration_minutes,
        output_interval_minutes=1,
        environment=environment,
        person=request.person,
        material=material,
    )

    # --- reference trajectory (port) ------------------------------------------
    reference_kwargs = dict(
        tdb=environment.air_temperature_c,
        tr=environment.mean_radiant_temperature_c,
        v=environment.wind_speed_m_s,
        rh=environment.relative_humidity_percent,
        met=request.person.met,
        clo=material.clothing_insulation_clo,
        wme=0.0,
        body_surface_area=request.person.body_surface_area_m2,
        body_mass_kg=request.person.body_mass_kg,
        p_atm=101325.0,
        position=request.person.position,
        max_skin_blood_flow=90.0,
        max_sweating=500.0,
    )

    reference = run_gagge_reference(
        duration_minutes=request.duration_minutes, **reference_kwargs
    )

    # --- library result: SET and port parity (60 min, 70 kg) ------------------
    library = two_nodes_gagge(
        tdb=environment.air_temperature_c,
        tr=environment.mean_radiant_temperature_c,
        v=max(environment.wind_speed_m_s, 0.01),
        rh=environment.relative_humidity_percent,
        met=request.person.met,
        clo=material.clothing_insulation_clo,
        wme=0,
        body_surface_area=request.person.body_surface_area_m2,
        p_atm=101325,
        position=request.person.position,
        max_skin_blood_flow=90,
        max_sweating=500,
        round_output=False,
    )

    parity_reference = run_gagge_reference(
        duration_minutes=LIBRARY_DURATION_MINUTES,
        **{**reference_kwargs, "body_mass_kg": 70.0},
    ).final

    library_core = _to_float(library.t_core)
    library_skin = _to_float(library.t_skin)

    parity = ReferencePortParity(
        library_core_temperature_c=round(library_core, 4),
        port_core_temperature_c=round(parity_reference.core_temperature_c, 4),
        library_skin_temperature_c=round(library_skin, 4),
        port_skin_temperature_c=round(parity_reference.skin_temperature_c, 4),
        maximum_absolute_difference_c=round(
            max(
                abs(library_core - parity_reference.core_temperature_c),
                abs(library_skin - parity_reference.skin_temperature_c),
            ),
            4,
        ),
    )

    if request.person.body_mass_kg != 70.0:
        alignment.append(
            "reference trajectory uses body_mass_kg from the request; the library "
            "value (SET, parity) is fixed at 70 kg"
        )

    # --- align the two series minute by minute --------------------------------
    prototype_points = prototype.time_series
    reference_points = reference.points

    if len(prototype_points) != len(reference_points):
        raise RuntimeError(
            "Benchmark series length mismatch: "
            f"{len(prototype_points)} prototype vs {len(reference_points)} reference"
        )

    series = [
        BenchmarkSeriesPoint(
            minute=int(round(p.minute)),
            prototype_core_temperature_c=p.core_temperature_c,
            prototype_skin_temperature_c=p.skin_temperature_c,
            prototype_evaporation_w_m2=p.evaporation_w_m2,
            reference_core_temperature_c=round(r.core_temperature_c, 4),
            reference_skin_temperature_c=round(r.skin_temperature_c, 4),
            reference_evaporation_w_m2=round(r.skin_evaporation_w_m2, 4),
        )
        for p, r in zip(prototype_points, reference_points, strict=True)
    ]

    core_metric = _metric(
        np.asarray([s.prototype_core_temperature_c for s in series]),
        np.asarray([s.reference_core_temperature_c for s in series]),
        request.tolerances.core_temperature_c,
    )
    skin_metric = _metric(
        np.asarray([s.prototype_skin_temperature_c for s in series]),
        np.asarray([s.reference_skin_temperature_c for s in series]),
        request.tolerances.skin_temperature_c,
    )

    final_prototype = prototype_points[-1]
    final_reference = reference.final

    return GaggeBenchmarkResponse(
        reference_model="Gagge Two-Node",
        reference_library="pythermalcomfort",
        reference_library_version=_library_version(),
        environment_note=(
            "Boundary conditions were aligned to what the Gagge two-node model "
            "can represent; see alignment_applied."
        ),
        alignment_applied=alignment,
        prototype=PrototypeBenchmarkOutput(
            core_temperature_c=prototype.final_core_temperature_c,
            skin_temperature_c=prototype.final_skin_temperature_c,
            evaporation_w_m2=final_prototype.evaporation_w_m2,
            skin_wettedness=final_prototype.skin_wettedness or 0.0,
            skin_blood_flow_kg_h_m2=final_prototype.skin_blood_flow_kg_h_m2 or 0.0,
            energy_residual_percent=prototype.diagnostics.normalized_residual_percent,
        ),
        gagge=GaggeModelOutput(
            core_temperature_c=round(final_reference.core_temperature_c, 4),
            skin_temperature_c=round(final_reference.skin_temperature_c, 4),
            skin_evaporation_w_m2=round(final_reference.skin_evaporation_w_m2, 4),
            skin_heat_loss_w_m2=round(
                final_reference.skin_evaporation_w_m2
                + final_reference.sensible_heat_loss_w_m2,
                4,
            ),
            respiratory_heat_loss_w_m2=round(reference.respiratory_heat_loss_w_m2, 4),
            skin_blood_flow_kg_h_m2=round(final_reference.skin_blood_flow_kg_h_m2, 4),
            skin_wettedness=round(final_reference.skin_wettedness, 4),
            standard_effective_temperature_c=_to_float(library.set),
        ),
        difference_core_temperature_c=core_metric.final_difference_c,
        difference_skin_temperature_c=skin_metric.final_difference_c,
        core_temperature=core_metric,
        skin_temperature=skin_metric,
        passed=core_metric.passed and skin_metric.passed,
        time_series=series,
        reference_port_parity=parity,
        warning=(
            "Diagnostic comparison, not an equivalence verification. Both models "
            "share body heat capacity, the effective radiation area ratio and the "
            "Gagge 1986 controllers; they still differ in the convection "
            "correlation (8.3 v^0.5 vs 8.6 v^0.53 with a metabolic floor), the "
            "exact vs linearised radiation exchange, and the skin wettedness "
            "bookkeeping once w reaches w_max."
        ),
    )
```

### File: `backend/app/services/gagge_reference.py`
```python
"""Minute-by-minute Gagge two-node reference model.

This is a port of the algorithm used by ``pythermalcomfort.models.two_nodes_gagge``
(Tartarini & Schiavon 2020, MIT licence), which itself follows Gagge, Fobelets &
Berglund (1986) and the ASHRAE 55 SET reference procedure. The library returns
only the state after 60 minutes for a fixed 70 kg body; this port exposes the
full trajectory, the exposure duration and the body mass so the platform
prototype can be compared minute by minute.

Parity with the library at 60 minutes and 70 kg is enforced by
``tests/test_gagge_reference.py``. Do not "improve" the physics here: the value
of this module is that it reproduces the reference exactly, quirks included.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import exp
from typing import Literal


BodyPosition = Literal["standing", "sitting"]

MET_FACTOR_W_M2 = 58.2
STEFAN_BOLTZMANN = 5.6697e-8
SWEATING_COEFFICIENT = 170.0
VASODILATION_COEFFICIENT = 120.0
VASOCONSTRICTION_COEFFICIENT = 0.5
SKIN_NEUTRAL_C = 33.7
CORE_NEUTRAL_C = 36.8
SKIN_BLOOD_FLOW_NEUTRAL = 6.3
BODY_SPECIFIC_HEAT_WH_KGK = 0.97
CLOTHING_EMISSIVITY = 0.95
SURFACE_ITERATION_LIMIT = 150


def saturation_vapor_pressure_torr(temperature_c: float) -> float:
    return exp(18.6686 - 4030.183 / (temperature_c + 235.0))


@dataclass(frozen=True)
class GaggeReferencePoint:
    minute: int
    core_temperature_c: float
    skin_temperature_c: float
    skin_evaporation_w_m2: float
    sensible_heat_loss_w_m2: float
    skin_blood_flow_kg_h_m2: float
    skin_wettedness: float


@dataclass(frozen=True)
class GaggeReferenceResult:
    points: list[GaggeReferencePoint]
    respiratory_heat_loss_w_m2: float
    maximum_skin_wettedness: float

    @property
    def final(self) -> GaggeReferencePoint:
        return self.points[-1]


def run_gagge_reference(
    *,
    tdb: float,
    tr: float,
    v: float,
    rh: float,
    met: float,
    clo: float,
    wme: float = 0.0,
    body_surface_area: float = 1.8258,
    body_mass_kg: float = 70.0,
    p_atm: float = 101325.0,
    position: BodyPosition = "standing",
    max_skin_blood_flow: float = 90.0,
    max_sweating: float = 500.0,
    duration_minutes: int = 60,
    w_max: float | None = None,
) -> GaggeReferenceResult:
    if duration_minutes < 1:
        raise ValueError("duration_minutes must be at least 1")

    air_speed = max(v, 0.1)
    vapor_pressure = rh * saturation_vapor_pressure_torr(tdb) / 100.0  # torr

    alfa = 0.1
    body_neutral_c = alfa * SKIN_NEUTRAL_C + (1.0 - alfa) * CORE_NEUTRAL_C

    t_skin = SKIN_NEUTRAL_C
    t_core = CORE_NEUTRAL_C
    m_bl = SKIN_BLOOD_FLOW_NEUTRAL

    e_skin = 0.1 * met  # library initialisation (kept for parity)
    q_sensible = 0.0
    w = 0.0

    pressure_atm = p_atm / 101325.0
    r_clo = 0.155 * clo
    f_a_cl = 1.0 + 0.15 * clo
    lr = 2.2 / pressure_atm  # Lewis ratio, C/torr
    rm = (met - wme) * MET_FACTOR_W_M2
    m = met * MET_FACTOR_W_M2

    i_cl = 0.45 if clo > 0 else 1.0

    if w_max is None:
        w_max = (
            0.59 * air_speed ** -0.08 if clo > 0 else 0.38 * air_speed ** -0.29
        )

    h_cc = 3.0 * pressure_atm ** 0.53
    h_fc = 8.600001 * (air_speed * pressure_atm) ** 0.53
    h_cc = max(h_cc, h_fc)
    if met > 0.85:
        h_cc = max(h_cc, 5.66 * (met - 0.85) ** 0.39)

    h_r = 4.7
    h_t = h_r + h_cc
    r_a = 1.0 / (f_a_cl * h_t)
    t_op = (h_r * tr + h_cc * tdb) / h_t

    q_res = 0.0023 * m * (44.0 - vapor_pressure)
    c_res = 0.0014 * m * (34.0 - tdb)

    radiation_area_ratio = 0.7 if position == "sitting" else 0.73

    points = [
        GaggeReferencePoint(
            minute=0,
            core_temperature_c=t_core,
            skin_temperature_c=t_skin,
            skin_evaporation_w_m2=e_skin,
            sensible_heat_loss_w_m2=q_sensible,
            skin_blood_flow_kg_h_m2=m_bl,
            skin_wettedness=w,
        )
    ]

    for minute in range(1, duration_minutes + 1):
        # Clothing surface temperature with a temperature-dependent h_r.
        t_cl = (r_a * t_skin + r_clo * t_op) / (r_a + r_clo)
        for _ in range(SURFACE_ITERATION_LIMIT):
            h_r = (
                4.0 * CLOTHING_EMISSIVITY * STEFAN_BOLTZMANN
                * ((t_cl + tr) / 2.0 + 273.15) ** 3.0
                * radiation_area_ratio
            )
            h_t = h_r + h_cc
            r_a = 1.0 / (f_a_cl * h_t)
            t_op = (h_r * tr + h_cc * tdb) / h_t
            t_cl_new = (r_a * t_skin + r_clo * t_op) / (r_a + r_clo)
            converged = abs(t_cl_new - t_cl) <= 0.01
            t_cl = t_cl_new
            if converged:
                break
        else:
            raise RuntimeError("Gagge reference: clothing temperature did not converge")

        q_sensible = (t_skin - t_op) / (r_a + r_clo)
        hf_cs = (t_core - t_skin) * (5.28 + 1.163 * m_bl)
        s_core = m - hf_cs - q_res - c_res - wme
        s_skin = hf_cs - q_sensible - e_skin

        tc_sk = BODY_SPECIFIC_HEAT_WH_KGK * alfa * body_mass_kg
        tc_cr = BODY_SPECIFIC_HEAT_WH_KGK * (1.0 - alfa) * body_mass_kg
        t_skin += s_skin * body_surface_area / (tc_sk * 60.0)
        t_core += s_core * body_surface_area / (tc_cr * 60.0)
        t_body = alfa * t_skin + (1.0 - alfa) * t_core

        sk_sig = t_skin - SKIN_NEUTRAL_C
        warm_sk = max(sk_sig, 0.0)
        colds = max(-sk_sig, 0.0)
        c_reg_sig = t_core - CORE_NEUTRAL_C
        c_warm = max(c_reg_sig, 0.0)
        c_cold = max(-c_reg_sig, 0.0)
        warm_b = max(t_body - body_neutral_c, 0.0)

        m_bl = (SKIN_BLOOD_FLOW_NEUTRAL + VASODILATION_COEFFICIENT * c_warm) / (
            1.0 + VASOCONSTRICTION_COEFFICIENT * colds
        )
        m_bl = min(max(m_bl, 0.5), max_skin_blood_flow)

        m_rsw = min(SWEATING_COEFFICIENT * warm_b * exp(warm_sk / 10.7), max_sweating)
        e_rsw = 0.68 * m_rsw

        r_ea = 1.0 / (lr * f_a_cl * h_cc)
        r_ecl = r_clo / (lr * i_cl)
        e_max = (saturation_vapor_pressure_torr(t_skin) - vapor_pressure) / (r_ea + r_ecl)
        if e_max == 0.0:
            e_max = 0.001  # library guard against division by zero

        p_rsw = e_rsw / e_max
        w = 0.06 + 0.94 * p_rsw
        e_diff = w * e_max - e_rsw
        if w > w_max:
            w = w_max
            p_rsw = w_max / 0.94
            e_rsw = p_rsw * e_max
            e_diff = 0.06 * (1.0 - p_rsw) * e_max
        if e_max < 0.0:
            e_diff = 0.0
            e_rsw = 0.0
            w = w_max

        e_skin = e_rsw + e_diff
        met_shivering = 19.4 * colds * c_cold
        m = rm + met_shivering
        alfa = 0.0417737 + 0.7451833 / (m_bl + 0.585417)

        points.append(
            GaggeReferencePoint(
                minute=minute,
                core_temperature_c=t_core,
                skin_temperature_c=t_skin,
                skin_evaporation_w_m2=e_skin,
                sensible_heat_loss_w_m2=q_sensible,
                skin_blood_flow_kg_h_m2=m_bl,
                skin_wettedness=w,
            )
        )

    return GaggeReferenceResult(
        points=points,
        respiratory_heat_loss_w_m2=q_res + c_res,
        maximum_skin_wettedness=w_max,
    )
```

### File: `backend/app/services/global_batch_export.py`
```python
import csv
import io
import json
import zipfile
from typing import Any

from app.models.global_batch import (
    GlobalBatchJob,
    GlobalCityResult,
)

def get_attribute(
    obj: Any,
    name: str,
    default: Any = None,
) -> Any:
    return getattr(
        obj,
        name,
        default,
    )

def get_heatwave_events(
    result: GlobalCityResult,
) -> list[dict[str, Any]]:
    analytics = get_attribute(
        result,
        "analytics_json",
        {},
    ) or {}

    if not isinstance(analytics, dict):
        return []

    events = analytics.get(
        "heatwave_events",
        [],
    )

    if not isinstance(events, list):
        return []

    return [
        event
        for event in events
        if isinstance(event, dict)
    ]

def build_geojson_properties(
    result: GlobalCityResult,
) -> dict[str, Any]:
    return {
        "city_id": get_attribute(
            result,
            "city_id",
        ),
        "city_name": get_attribute(
            result,
            "city_name",
        ),
        "country": get_attribute(
            result,
            "country",
        ),
        "status": get_attribute(
            result,
            "status",
        ),
        "climate_adaptation_rate_percent": (
            get_attribute(
                result,
                "climate_adaptation_rate_percent",
            )
        ),
        "exposure_coverage_percent": (
            get_attribute(
                result,
                "exposure_coverage_percent",
            )
        ),
        "annual_average_skin_improvement_c": (
            get_attribute(
                result,
                "annual_average_skin_improvement_c",
            )
        ),
        "annual_average_core_improvement_c": (
            get_attribute(
                result,
                "annual_average_core_improvement_c",
            )
        ),
        "maximum_skin_improvement_c": (
            get_attribute(
                result,
                "maximum_skin_improvement_c",
            )
        ),
        "effective_cooling_hours": (
            get_attribute(
                result,
                "effective_cooling_hours",
            )
        ),
        "sampled_day_count": get_attribute(
            result,
            "sampled_day_count",
            0,
        ),
        "eligible_sample_count": get_attribute(
            result,
            "eligible_sample_count",
            0,
        ),
        "evaluated_weighted_days": get_attribute(
            result,
            "evaluated_weighted_days",
            0,
        ),
        "beneficial_weighted_days": get_attribute(
            result,
            "beneficial_weighted_days",
            0,
        ),
        "skin_improvement_p50_c": get_attribute(
            result,
            "skin_improvement_p50_c",
        ),
        "skin_improvement_p90_c": get_attribute(
            result,
            "skin_improvement_p90_c",
        ),
        "skin_improvement_p95_c": get_attribute(
            result,
            "skin_improvement_p95_c",
        ),
        "core_improvement_p50_c": get_attribute(
            result,
            "core_improvement_p50_c",
        ),
        "core_improvement_p90_c": get_attribute(
            result,
            "core_improvement_p90_c",
        ),
        "core_improvement_p95_c": get_attribute(
            result,
            "core_improvement_p95_c",
        ),
        "heatwave_event_count": get_attribute(
            result,
            "heatwave_event_count",
            0,
        ),
        "longest_heatwave_days": get_attribute(
            result,
            "longest_heatwave_days",
            0,
        ),
    }

def build_batch_geojson(
    batch: GlobalBatchJob,
) -> dict[str, Any]:
    request = batch.request_json or {}

    analysis_resolution = request.get(
        "analysis_resolution",
        "representative",
    )

    heatwave_analysis_available = (
        request.get(
            "enable_heatwave_analysis",
            True,
        )
        and analysis_resolution == "daily"
        and request.get(
            "daily_stride_days",
            1,
        ) == 1
    )

    features = []

    for result in (
        get_attribute(
            batch,
            "city_results",
            [],
        ) or []
    ):
        if result.status != "completed":
            continue

        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        result.longitude,
                        result.latitude,
                    ],
                },
                "properties": (
                    build_geojson_properties(
                        result
                    )
                ),
            }
        )

    return {
        "type": "FeatureCollection",
        "metadata": {
            "batch_id": batch.id,
            "status": batch.status,
            "year": request.get("year"),
            "method": (
                "daily_heat_exposure_weighted"
                if analysis_resolution == "daily"
                else (
                    "representative_day_"
                    "heat_exposure_weighted"
                )
            ),
            "analysis_resolution": (
                analysis_resolution
            ),
            "sample_days_per_month": (
                request.get(
                    "sample_days_per_month",
                    1,
                )
            ),
            "daily_stride_days": (
                request.get(
                    "daily_stride_days",
                    1,
                )
            ),
            "execution_profile": (
                request.get(
                    "execution_profile",
                    "auto",
                )
            ),
            "heatwave_analysis_available": (
                heatwave_analysis_available
            ),
            "mean_radiant_temperature_method": (
                (request.get("environment_assumptions") or {}).get(
                    "mean_radiant_temperature_method",
                    "air_plus_solar_linear",
                )
            ),
            "sky_temperature_method": (
                (request.get("environment_assumptions") or {}).get(
                    "sky_temperature_method",
                    "humidity_offset",
                )
            ),
        },
        "features": features,
    }


def build_city_summary_csv(
    batch: GlobalBatchJob,
) -> str:
    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow(
        [
            "batch_id",
            "city_result_id",
            "city_id",
            "city_name",
            "country",
            "status",
            "stage",
            "progress",
            "latitude",
            "longitude",
            "climate_adaptation_rate_percent",
            "exposure_coverage_percent",
            "annual_average_skin_improvement_c",
            "annual_average_core_improvement_c",
            "maximum_skin_improvement_c",
            "effective_cooling_hours",
            "sampled_day_count",
            "eligible_sample_count",
            "evaluated_weighted_days",
            "beneficial_weighted_days",
            "skin_improvement_p50_c",
            "skin_improvement_p90_c",
            "skin_improvement_p95_c",
            "core_improvement_p50_c",
            "core_improvement_p90_c",
            "core_improvement_p95_c",
            "heatwave_event_count",
            "longest_heatwave_days",
            "completed_month_count",
            "last_checkpoint_month",
            "resumed_from_checkpoint",
            "last_heartbeat_at",
            "retry_count",
            "started_at",
            "completed_at",
            "error_message",
        ]
    )

    city_results = get_attribute(
        batch,
        "city_results",
        [],
    ) or []

    batch_id = get_attribute(
        batch,
        "id",
    )

    for result in city_results:
        status = get_attribute(
            result,
            "status",
        )

        writer.writerow(
            [
                batch_id,
                get_attribute(
                    result,
                    "id",
                ),
                get_attribute(
                    result,
                    "city_id",
                ),
                get_attribute(
                    result,
                    "city_name",
                ),
                get_attribute(
                    result,
                    "country",
                ),
                status,
                get_attribute(
                    result,
                    "stage",
                    status,
                ),
                get_attribute(
                    result,
                    "progress",
                    (
                        100
                        if status == "completed"
                        else 0
                    ),
                ),
                get_attribute(
                    result,
                    "latitude",
                ),
                get_attribute(
                    result,
                    "longitude",
                ),
                get_attribute(
                    result,
                    (
                        "climate_adaptation_"
                        "rate_percent"
                    ),
                ),
                get_attribute(
                    result,
                    "exposure_coverage_percent",
                ),
                get_attribute(
                    result,
                    (
                        "annual_average_skin_"
                        "improvement_c"
                    ),
                ),
                get_attribute(
                    result,
                    (
                        "annual_average_core_"
                        "improvement_c"
                    ),
                ),
                get_attribute(
                    result,
                    "maximum_skin_improvement_c",
                ),
                get_attribute(
                    result,
                    "effective_cooling_hours",
                    0,
                ),
                get_attribute(
                    result,
                    "sampled_day_count",
                    0,
                ),
                get_attribute(
                    result,
                    "eligible_sample_count",
                    0,
                ),
                get_attribute(
                    result,
                    "evaluated_weighted_days",
                    0,
                ),
                get_attribute(
                    result,
                    "beneficial_weighted_days",
                    0,
                ),
                get_attribute(
                    result,
                    "skin_improvement_p50_c",
                ),
                get_attribute(
                    result,
                    "skin_improvement_p90_c",
                ),
                get_attribute(
                    result,
                    "skin_improvement_p95_c",
                ),
                get_attribute(
                    result,
                    "core_improvement_p50_c",
                ),
                get_attribute(
                    result,
                    "core_improvement_p90_c",
                ),
                get_attribute(
                    result,
                    "core_improvement_p95_c",
                ),
                get_attribute(
                    result,
                    "heatwave_event_count",
                    0,
                ),
                get_attribute(
                    result,
                    "longest_heatwave_days",
                    0,
                ),
                get_attribute(
                    result,
                    "completed_month_count",
                    0,
                ),
                get_attribute(
                    result,
                    "last_checkpoint_month",
                ),
                get_attribute(
                    result,
                    "resumed_from_checkpoint",
                    False,
                ),
                get_attribute(
                    result,
                    "last_heartbeat_at",
                ),
                get_attribute(
                    result,
                    "retry_count",
                    0,
                ),
                get_attribute(
                    result,
                    "started_at",
                ),
                get_attribute(
                    result,
                    "completed_at",
                ),
                get_attribute(
                    result,
                    "error_message",
                ),
            ]
        )

    return output.getvalue()


def build_monthly_results_csv(
    batch: GlobalBatchJob,
) -> str:
    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow(
        [
            "batch_id",
            "city_id",
            "city_name",
            "country",
            "month",
            "sampled_day_count",
            "eligible_sample_count",
            "total_weighted_days",
            "evaluated_weighted_days",
            "beneficial_weighted_days",
            "exposure_coverage_percent",
            "climate_adaptation_rate_percent",
            "average_skin_improvement_c",
            "average_core_improvement_c",
            "maximum_skin_improvement_c",
        ]
    )

    for result in (
        get_attribute(
            batch,
            "city_results",
            [],
        ) or []
    ):
        monthly_results = (
            result.monthly_json or []
        )

        for monthly_result in monthly_results:
            if not isinstance(
                monthly_result,
                dict,
            ):
                continue

            writer.writerow(
                [
                    batch.id,
                    result.city_id,
                    result.city_name,
                    result.country,
                    monthly_result.get(
                        "month"
                    ),
                    monthly_result.get(
                        "sampled_day_count"
                    ),
                    monthly_result.get(
                        "eligible_sample_count"
                    ),
                    monthly_result.get(
                        "total_weighted_days"
                    ),
                    monthly_result.get(
                        "evaluated_weighted_days"
                    ),
                    monthly_result.get(
                        "beneficial_weighted_days"
                    ),
                    monthly_result.get(
                        "exposure_coverage_percent"
                    ),
                    monthly_result.get(
                        (
                            "climate_adaptation_"
                            "rate_percent"
                        )
                    ),
                    monthly_result.get(
                        (
                            "average_skin_"
                            "improvement_c"
                        )
                    ),
                    monthly_result.get(
                        (
                            "average_core_"
                            "improvement_c"
                        )
                    ),
                    monthly_result.get(
                        (
                            "maximum_skin_"
                            "improvement_c"
                        )
                    ),
                ]
            )

    return output.getvalue()


def normalize_month_samples(
    monthly_result: dict[str, Any],
) -> list[dict[str, Any]]:
    samples = monthly_result.get(
        "samples",
        [],
    )

    if isinstance(samples, list) and samples:
        return [
            sample
            for sample in samples
            if isinstance(sample, dict)
        ]

    representative_date = (
        monthly_result.get(
            "representative_date_local"
        )
    )

    if not representative_date:
        return []

    return [
        {
            "sample_date_local": (
                representative_date
            ),
            "weight_days": (
                monthly_result.get(
                    "weight_days",
                    1,
                )
            ),
            "mean_air_temperature_c": None,
            "maximum_air_temperature_c": None,
            "mean_solar_radiation_w_m2": None,
            "maximum_solar_radiation_w_m2": None,
            "exposure_eligible": True,
            "beneficial": (
                monthly_result.get(
                    "beneficial"
                )
            ),
            "average_skin_improvement_c": (
                monthly_result.get(
                    (
                        "average_skin_"
                        "improvement_c"
                    )
                )
            ),
            "final_skin_improvement_c": (
                monthly_result.get(
                    (
                        "final_skin_"
                        "improvement_c"
                    )
                )
            ),
            "average_core_improvement_c": (
                monthly_result.get(
                    (
                        "average_core_"
                        "improvement_c"
                    )
                )
            ),
            "maximum_skin_improvement_c": (
                monthly_result.get(
                    (
                        "maximum_skin_"
                        "improvement_c"
                    )
                )
            ),
            "weather_from_cache": None,
        }
    ]


def build_sample_results_csv(
    batch: GlobalBatchJob,
) -> str:
    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow(
        [
            "batch_id",
            "city_id",
            "city_name",
            "country",
            "month",
            "sample_date_local",
            "weight_days",
            "mean_air_temperature_c",
            "maximum_air_temperature_c",
            "daily_maximum_air_temperature_c",
            "mean_solar_radiation_w_m2",
            "maximum_solar_radiation_w_m2",
            "exposure_eligible",
            "beneficial",
            "average_skin_improvement_c",
            "final_skin_improvement_c",
            "average_core_improvement_c",
            "maximum_skin_improvement_c",
            "mean_sky_temperature_c", 
            "mean_surround_temperature_c",
            "weather_from_cache",
        ]
    )

    for result in (
        get_attribute(
            batch,
            "city_results",
            [],
        ) or []
    ):
        monthly_results = (
            result.monthly_json or []
        )

        for monthly_result in monthly_results:
            if not isinstance(
                monthly_result,
                dict,
            ):
                continue

            month = monthly_result.get(
                "month"
            )

            samples = normalize_month_samples(
                monthly_result
            )

            for sample in samples:
                writer.writerow(
                    [
                        batch.id,
                        result.city_id,
                        result.city_name,
                        result.country,
                        month,
                        sample.get(
                            "sample_date_local"
                        ),
                        sample.get(
                            "weight_days"
                        ),
                        sample.get(
                            "mean_air_temperature_c"
                        ),
                        sample.get(
                            (
                                "maximum_air_temperature_c"
                            )
                        ),
                        sample.get(
                            "daily_maximum_air_temperature_c"
                        ),
                        sample.get(
                            (
                                "mean_solar_"
                                "radiation_w_m2"
                            )
                        ),
                        sample.get(
                            (
                                "maximum_solar_"
                                "radiation_w_m2"
                            )
                        ),
                        sample.get(
                            "exposure_eligible"
                        ),
                        sample.get(
                            "beneficial"
                        ),
                        sample.get(
                            (
                                "average_skin_"
                                "improvement_c"
                            )
                        ),
                        sample.get(
                            (
                                "final_skin_"
                                "improvement_c"
                            )
                        ),
                        sample.get(
                            (
                                "average_core_"
                                "improvement_c"
                            )
                        ),
                        sample.get(
                            (
                                "maximum_skin_"
                                "improvement_c"
                            )
                        ),
                        # Stage 12
                        sample.get("mean_sky_temperature_c"),
                        sample.get("mean_surround_temperature_c"),
                        sample.get("weather_from_cache"),
                    ]
                )

    return output.getvalue()


def build_heatwave_events_csv(
    batch: GlobalBatchJob,
) -> str:
    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow(
        [
            "batch_id",
            "city_id",
            "city_name",
            "country",
            "event_number",
            "start_date_local",
            "end_date_local",
            "duration_days",
            "mean_maximum_air_temperature_c",
            "peak_air_temperature_c",
            "mean_skin_improvement_c",
            "p90_skin_improvement_c",
            "beneficial_day_count",
        ]
    )

    for result in (
        get_attribute(
            batch,
            "city_results",
            [],
        ) or []
    ):
        events = get_heatwave_events(
            result
        )

        for event_number, event in enumerate(
            events,
            start=1,
        ):
            writer.writerow(
                [
                    batch.id,
                    result.city_id,
                    result.city_name,
                    result.country,
                    event_number,
                    event.get(
                        "start_date_local"
                    ),
                    event.get(
                        "end_date_local"
                    ),
                    event.get(
                        "duration_days"
                    ),
                    event.get(
                        (
                            "mean_maximum_air_"
                            "temperature_c"
                        )
                    ),
                    event.get(
                        "peak_air_temperature_c"
                    ),
                    event.get(
                        (
                            "mean_skin_"
                            "improvement_c"
                        )
                    ),
                    event.get(
                        (
                            "p90_skin_"
                            "improvement_c"
                        )
                    ),
                    event.get(
                        "beneficial_day_count"
                    ),
                ]
            )

    return output.getvalue()

def build_city_result_json(
    result: GlobalCityResult,
) -> dict[str, Any]:
    analytics = get_attribute(
        result,
        "analytics_json",
        {},
    ) or {}

    if not isinstance(analytics, dict):
        analytics = {}

    status = get_attribute(
        result,
        "status",
    )

    return {
        "id": get_attribute(
            result,
            "id",
        ),
        "batch_id": get_attribute(
            result,
            "batch_id",
        ),
        "celery_task_id": get_attribute(
            result,
            "celery_task_id",
        ),
        "city_id": get_attribute(
            result,
            "city_id",
        ),
        "city_name": get_attribute(
            result,
            "city_name",
        ),
        "country": get_attribute(
            result,
            "country",
        ),
        "latitude": get_attribute(
            result,
            "latitude",
        ),
        "longitude": get_attribute(
            result,
            "longitude",
        ),
        "status": status,
        "stage": get_attribute(
            result,
            "stage",
            status,
        ),
        "progress": get_attribute(
            result,
            "progress",
            100 if status == "completed" else 0,
        ),
        "climate_adaptation_rate_percent": (
            get_attribute(
                result,
                "climate_adaptation_rate_percent",
            )
        ),
        "exposure_coverage_percent": (
            get_attribute(
                result,
                "exposure_coverage_percent",
            )
        ),
        "annual_average_skin_improvement_c": (
            get_attribute(
                result,
                "annual_average_skin_improvement_c",
            )
        ),
        "annual_average_core_improvement_c": (
            get_attribute(
                result,
                "annual_average_core_improvement_c",
            )
        ),
        "maximum_skin_improvement_c": (
            get_attribute(
                result,
                "maximum_skin_improvement_c",
            )
        ),
        "effective_cooling_hours": get_attribute(
            result,
            "effective_cooling_hours",
            0,
        ),
        "sampled_day_count": get_attribute(
            result,
            "sampled_day_count",
            0,
        ),
        "eligible_sample_count": get_attribute(
            result,
            "eligible_sample_count",
            0,
        ),
        "evaluated_weighted_days": get_attribute(
            result,
            "evaluated_weighted_days",
            0,
        ),
        "beneficial_weighted_days": get_attribute(
            result,
            "beneficial_weighted_days",
            0,
        ),
        "completed_month_count": get_attribute(
            result,
            "completed_month_count",
            0,
        ),
        "last_checkpoint_month": get_attribute(
            result,
            "last_checkpoint_month",
        ),
        "resumed_from_checkpoint": get_attribute(
            result,
            "resumed_from_checkpoint",
            False,
        ),
        "last_heartbeat_at": get_attribute(
            result,
            "last_heartbeat_at",
        ),
        "skin_improvement_percentiles_c": {
            "p50": get_attribute(
                result,
                "skin_improvement_p50_c",
            ),
            "p90": get_attribute(
                result,
                "skin_improvement_p90_c",
            ),
            "p95": get_attribute(
                result,
                "skin_improvement_p95_c",
            ),
        },
        "core_improvement_percentiles_c": {
            "p50": get_attribute(
                result,
                "core_improvement_p50_c",
            ),
            "p90": get_attribute(
                result,
                "core_improvement_p90_c",
            ),
            "p95": get_attribute(
                result,
                "core_improvement_p95_c",
            ),
        },
        "heatwave_event_count": get_attribute(
            result,
            "heatwave_event_count",
            0,
        ),
        "longest_heatwave_days": get_attribute(
            result,
            "longest_heatwave_days",
            0,
        ),
        "heatwave_analysis_available": (
            analytics.get(
                "heatwave_analysis_available",
                False,
            )
        ),
        "heatwave_events": get_heatwave_events(
            result
        ),
        "retry_count": get_attribute(
            result,
            "retry_count",
            0,
        ),
        "monthly_results": get_attribute(
            result,
            "monthly_json",
            [],
        ) or [],
        "data_quality": analytics.get("data_quality", {}),
        "metric_definitions": analytics.get("metric_definitions", {}),
        "heatwave_unavailable_reason": analytics.get("heatwave_unavailable_reason"),
        "lease_owner": get_attribute(result, "lease_owner"),
        "lease_expires_at": get_attribute(result, "lease_expires_at"),
        "error_message": get_attribute(
            result,
            "error_message",
        ),
        "started_at": get_attribute(
            result,
            "started_at",
        ),
        "completed_at": get_attribute(
            result,
            "completed_at",
        ),
    }

def build_batch_json(
    batch: GlobalBatchJob,
) -> dict[str, Any]:
    city_results = get_attribute(
        batch,
        "city_results",
        [],
    ) or []

    status = get_attribute(
        batch,
        "status",
    )

    return {
        "id": getattr(
            batch,
            "id",
            None,
        ),
        "celery_group_id": getattr(
            batch,
            "celery_group_id",
            None,
        ),
        "status": status,
        "stage": getattr(
            batch,
            "stage",
            status,
        ),
        "progress": getattr(
            batch,
            "progress",
            100 if status == "completed" else 0,
        ),
        "total_city_count": getattr(
            batch,
            "total_city_count",
            len(city_results),
        ),
        "completed_city_count": getattr(
            batch,
            "completed_city_count",
            sum(
                1
                for result in city_results
                if getattr(
                    result,
                    "status",
                    None,
                ) == "completed"
            ),
        ),
        "failed_city_count": getattr(
            batch,
            "failed_city_count",
            sum(
                1
                for result in city_results
                if getattr(
                    result,
                    "status",
                    None,
                ) == "failed"
            ),
        ),
        "cancelled_city_count": getattr(
            batch,
            "cancelled_city_count",
            sum(
                1
                for result in city_results
                if getattr(
                    result,
                    "status",
                    None,
                ) == "cancelled"
            ),
        ),
        "request": get_attribute(
            batch,
            "request_json",
            {},
        ) or {},
        "summary": get_attribute(
            batch,
            "summary_json",
            {},
        ) or {},
        "error_message": getattr(
            batch,
            "error_message",
            None,
        ),
        "created_at": getattr(
            batch,
            "created_at",
            None,
        ),
        "updated_at": getattr(
            batch,
            "updated_at",
            None,
        ),
        "started_at": getattr(
            batch,
            "started_at",
            None,
        ),
        "completed_at": getattr(
            batch,
            "completed_at",
            None,
        ),
        "city_results": [
            build_city_result_json(result)
            for result in city_results
        ],
    }


def build_readme_text(
    batch: GlobalBatchJob,
) -> str:
    request = batch.request_json or {}

    return "\n".join(
        [
            "Global Climate Adaptation Analysis Export",
            "=========================================",
            "",
            f"Batch ID: {batch.id}",
            f"Status: {batch.status}",
            (
                "Analysis resolution: "
                f"{request.get('analysis_resolution', 'representative')}"
            ),
            (
                "Execution profile: "
                f"{request.get('execution_profile', 'auto')}"
            ),
            (
                "Environment: "
                f"{request.get('mean_radiant_temperature_method', 'air_plus_solar_linear')}"
                f" / "
                f"{request.get('sky_temperature_method', 'humidity_offset')}"
            ),
            "",
            "Files",
            "-----",
            "",
            "city-summary.csv",
            (
                "One row per city containing annual, "
                "checkpoint, percentile, and heatwave "
                "summary metrics."
            ),
            "",
            "monthly-results.csv",
            (
                "One row per city and month containing "
                "weighted monthly adaptation metrics."
            ),
            "",
            "sample-results.csv",
            (
                "One row per sampled day containing "
                "weather exposure and thermal "
                "improvement metrics."
            ),
            "",
            "heatwave-events.csv",
            (
                "One row per detected heatwave event. "
                "This file may contain only its header "
                "when heatwave analysis is unavailable "
                "or no event was detected."
            ),
            "",
            "results.geojson",
            (
                "Completed city results represented as "
                "GeoJSON point features."
            ),
            "",
            "results.json",
            (
                "Complete batch request, summary, city "
                "analytics, monthly results, and "
                "heatwave events."
            ),
            "",
        ]
    )


def build_batch_export_zip(
    batch: GlobalBatchJob,
) -> bytes:
    memory_file = io.BytesIO()

    batch_json = build_batch_json(
        batch
    )

    with zipfile.ZipFile(
        memory_file,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
    ) as archive:
        archive.writestr(
            "README.txt",
            build_readme_text(batch),
        )

        archive.writestr(
            "city-summary.csv",
            build_city_summary_csv(batch),
        )

        archive.writestr(
            "monthly-results.csv",
            build_monthly_results_csv(batch),
        )

        archive.writestr(
            "sample-results.csv",
            build_sample_results_csv(batch),
        )

        archive.writestr(
            "heatwave-events.csv",
            build_heatwave_events_csv(batch),
        )

        archive.writestr(
            "results.geojson",
            json.dumps(
                build_batch_geojson(batch),
                ensure_ascii=False,
                indent=2,
                default=str,
            ),
        )

        archive.writestr(
            "results.json",
            json.dumps(
                batch_json,
                ensure_ascii=False,
                indent=2,
                default=str,
            ),
        )

    return memory_file.getvalue()
```

### File: `backend/app/services/global_batch_service.py`
```python
from datetime import datetime, timezone

from sqlalchemy import (
    func,
    select,
)
from sqlalchemy.orm import Session
from app.core.time import utc_now
from app.models.global_batch import GlobalBatchJob, GlobalCityCheckpoint, GlobalCityResult

from app.schemas.global_batch import (
    CityCheckpointListResponse,
    CityCheckpointResponse,
    GlobalBatchDetail,
    GlobalBatchProgressEvent,
    GlobalBatchResponse,
    GlobalCityProgress,
    GlobalCityResultResponse,
    GlobalBatchCreate,
    LeaseState,
)
from app.services.checkpoints import CheckpointProvenance, load_resume_state
from app.services.leases import db_now, derive_lease_state  # noqa: F401 (re-exported)
from app.services.stored_requests import load_stored_request
from collections import defaultdict
import hashlib
import json

TERMINAL_CITY_STATUSES = {
    "completed",
    "failed",
    "cancelled",
}

def load_checkpoint_months(session: Session, batch_id: str) -> dict[str, list[int]]:
    """city_result_id -> sorted months with a durable checkpoint. Months only;
    payloads are never loaded here."""
    rows = session.execute(
        select(GlobalCityCheckpoint.city_result_id, GlobalCityCheckpoint.month)
        .join(GlobalCityResult, GlobalCityResult.id == GlobalCityCheckpoint.city_result_id)
        .where(GlobalCityResult.batch_id == batch_id)
        .order_by(GlobalCityCheckpoint.month)
    ).all()
    months: dict[str, list[int]] = defaultdict(list)
    for city_result_id, month in rows:
        months[city_result_id].append(month)
    return dict(months)

def city_result_to_response(
    result: GlobalCityResult,
    *,
    checkpoint_months: list[int] | None = None,
    now: datetime | None = None,
) -> GlobalCityResultResponse:
    analytics = result.analytics_json or {}
    return GlobalCityResultResponse(
        id=result.id,
        batch_id=result.batch_id,
        celery_task_id=result.celery_task_id,
        city_id=result.city_id,
        city_name=result.city_name,
        country=result.country,
        latitude=result.latitude,
        longitude=result.longitude,
        status=result.status,
        stage=result.stage,
        progress=result.progress,
        climate_adaptation_rate_percent=(
            result.climate_adaptation_rate_percent
        ),
        exposure_coverage_percent=(
            result.exposure_coverage_percent
        ),
        annual_average_skin_improvement_c=(
            result.annual_average_skin_improvement_c
        ),
        annual_average_core_improvement_c=(
            result.annual_average_core_improvement_c
        ),
        maximum_skin_improvement_c=(
            result.maximum_skin_improvement_c
        ),
        effective_cooling_hours=(
            result.effective_cooling_hours
        ),
        sampled_day_count=result.sampled_day_count,
        eligible_sample_count=(
            result.eligible_sample_count
        ),
        evaluated_weighted_days=(
            result.evaluated_weighted_days
        ),
        beneficial_weighted_days=(
            result.beneficial_weighted_days
        ),
        completed_month_count=(
            result.completed_month_count
        ),
        last_checkpoint_month=(
            result.last_checkpoint_month
        ),
        resumed_from_checkpoint=(
            result.resumed_from_checkpoint
        ),
        last_heartbeat_at=(
            result.last_heartbeat_at
        ),
        skin_improvement_p50_c=(
            result.skin_improvement_p50_c
        ),
        skin_improvement_p90_c=(
            result.skin_improvement_p90_c
        ),
        skin_improvement_p95_c=(
            result.skin_improvement_p95_c
        ),
        core_improvement_p50_c=(
            result.core_improvement_p50_c
        ),
        core_improvement_p90_c=(
            result.core_improvement_p90_c
        ),
        core_improvement_p95_c=(
            result.core_improvement_p95_c
        ),
        heatwave_event_count=(
            result.heatwave_event_count
        ),
        longest_heatwave_days=(
            result.longest_heatwave_days
        ),
        heatwave_events=(
            (
                result.analytics_json or {}
            ).get(
                "heatwave_events"
            )
        ),
        retry_count=result.retry_count,
        monthly_results=result.monthly_json,
        error_message=result.error_message,
        started_at=result.started_at,
        completed_at=result.completed_at,
        data_quality=analytics.get("data_quality"),
        metric_definitions=analytics.get("metric_definitions"),
        heatwave_analysis_available=analytics.get("heatwave_analysis_available"),
        heatwave_unavailable_reason=analytics.get("heatwave_unavailable_reason"),
        heatwave_temperature_basis=analytics.get("heatwave_temperature_basis"),
        # Stage 8
        lease_owner=getattr(result, "lease_owner", None),
        lease_expires_at=getattr(result, "lease_expires_at", None),
        lease_state=derive_lease_state(
            getattr(result, "lease_owner", None),
            getattr(result, "lease_expires_at", None),
            now,
        ),
        checkpoint_months=list(checkpoint_months or []),
    )


def batch_to_response(batch: GlobalBatchJob) -> GlobalBatchResponse:
    return GlobalBatchResponse(
        id=batch.id,
        celery_group_id=batch.celery_group_id,
        status=batch.status,
        stage=batch.stage,
        progress=batch.progress,
        total_city_count=batch.total_city_count,
        completed_city_count=(
            batch.completed_city_count
        ),
        failed_city_count=batch.failed_city_count,
        cancelled_city_count=(
            batch.cancelled_city_count
        ),
        summary=batch.summary_json,
        error_message=batch.error_message,
        created_at=batch.created_at,
        updated_at=batch.updated_at,
        started_at=batch.started_at,
        completed_at=batch.completed_at,
        control_material_version_id=getattr(batch, "control_material_version_id", None),
        rc_material_version_id=getattr(batch, "rc_material_version_id", None),
        # Stage 8
        attempt=getattr(batch, "attempt", 0) or 0,
        lease_owner=getattr(batch, "lease_owner", None),
        lease_expires_at=getattr(batch, "lease_expires_at", None),
        last_heartbeat_at=getattr(batch, "last_heartbeat_at", None),
        cancel_requested_at=getattr(batch, "cancel_requested_at", None),
    )


def batch_to_detail(
    batch: GlobalBatchJob,
    *,
    checkpoint_months: dict[str, list[int]] | None = None,
    now: datetime | None = None,
) -> GlobalBatchDetail:
    now = now or utc_now()
    months = checkpoint_months or {}
    return GlobalBatchDetail(
        **batch_to_response(batch).model_dump(),
        request=load_stored_request(GlobalBatchCreate, batch.request_json),
        city_results=[
            city_result_to_response(item, checkpoint_months=months.get(item.id), now=now)
            for item in batch.city_results
        ],
    )

def batch_progress_event(
    batch: GlobalBatchJob,
    checkpoint_months: dict[str, list[int]] | None = None,
    now: datetime | None = None,
) -> GlobalBatchProgressEvent:
    now = now or utc_now()
    months = checkpoint_months or {}
    return GlobalBatchProgressEvent(
        batch=batch_to_response(batch),
        cities=[
            GlobalCityProgress(
                id=item.id,
                city_id=item.city_id,
                status=item.status,
                stage=item.stage,
                progress=item.progress,
                retry_count=item.retry_count,
                completed_month_count=item.completed_month_count,
                last_checkpoint_month=item.last_checkpoint_month,
                last_heartbeat_at=item.last_heartbeat_at,
                lease_owner=getattr(item, "lease_owner", None),
                lease_expires_at=getattr(item, "lease_expires_at", None),
                lease_state=derive_lease_state(
                    getattr(item, "lease_owner", None),
                    getattr(item, "lease_expires_at", None),
                    now,
                ),
                checkpoint_months=list(months.get(item.id, [])),
                error_message=item.error_message,
            )
            for item in batch.city_results
        ],
    )

def _payload_sha256(payload: dict) -> str:
    serialized = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def city_checkpoints_to_response(
    session: Session, *, batch: GlobalBatchJob, city_result: GlobalCityResult,
) -> CityCheckpointListResponse:
    request = load_stored_request(GlobalBatchCreate, batch.request_json)
    provenance = CheckpointProvenance.for_request(request)

    rows = session.scalars(
        select(GlobalCityCheckpoint)
        .where(GlobalCityCheckpoint.city_result_id == city_result.id)
        .order_by(GlobalCityCheckpoint.month)
    ).all()

    resume = load_resume_state(
        session, city_result.id, start_month=request.start_month, provenance=provenance
    )

    return CityCheckpointListResponse(
        batch_id=batch.id,
        city_result_id=city_result.id,
        city_id=city_result.city_id,
        start_month=request.start_month,
        end_month=request.end_month,
        resume_from_month=resume.next_month,
        items=[
            CityCheckpointResponse(
                id=row.id,
                month=row.month,
                attempt=row.attempt,
                created_at=row.created_at,
                payload_sha256=_payload_sha256(row.payload_json),
                sampled_day_count=int((row.payload_json or {}).get("sampled_day_count", 0)),
                skipped_sample_count=len((row.payload_json or {}).get("skipped_samples", [])),
                model_version=row.model_version,
                parameter_fingerprint=row.parameter_fingerprint,
                provenance_matches_batch=provenance.mismatch_reason(row) is None,
                mismatch_reason=provenance.mismatch_reason(row),
            )
            for row in rows
        ],
    )
    
    
def refresh_batch_status(
    session: Session,
    batch_id: str,
) -> None:
    batch = session.scalar(
        select(GlobalBatchJob)
        .where(GlobalBatchJob.id == batch_id)
        .with_for_update()
    )

    if batch is None:
        return

    status_counts = dict(
        session.execute(
            select(
                GlobalCityResult.status,
                func.count(GlobalCityResult.id),
            )
            .where(
                GlobalCityResult.batch_id == batch_id
            )
            .group_by(GlobalCityResult.status)
        ).all()
    )

    completed = status_counts.get(
        "completed",
        0,
    )
    failed = status_counts.get(
        "failed",
        0,
    )
    cancelled = status_counts.get(
        "cancelled",
        0,
    )
    running = status_counts.get(
        "running",
        0,
    )

    processed = (
        completed
        + failed
        + cancelled
    )

    batch.completed_city_count = completed
    batch.failed_city_count = failed
    batch.cancelled_city_count = cancelled

    if batch.total_city_count > 0:
        batch.progress = round(
            processed
            / batch.total_city_count
            * 100
        )

    if running > 0 and batch.status == "queued":
        batch.status = "running"
        batch.stage = "analyzing_cities"
        batch.started_at = datetime.now(
            timezone.utc
        )

    if processed < batch.total_city_count:
        session.commit()
        return

    batch.progress = 100
    batch.completed_at = datetime.now(
        timezone.utc
    )

    if cancelled == batch.total_city_count:
        batch.status = "cancelled"
        batch.stage = "cancelled"

    elif completed == 0:
        batch.status = "failed"
        batch.stage = "failed"

    elif failed > 0 or cancelled > 0:
        batch.status = "partial_completed"
        batch.stage = "partial_completed"

    else:
        batch.status = "completed"
        batch.stage = "completed"

    completed_results = session.scalars(
        select(GlobalCityResult).where(
            GlobalCityResult.batch_id == batch_id,
            GlobalCityResult.status == "completed",
        )
    ).all()

    if completed_results:
        rates = [
            item.climate_adaptation_rate_percent
            for item in completed_results
            if (
                item.climate_adaptation_rate_percent
                is not None
            )
        ]

        skin_values = [
            item.annual_average_skin_improvement_c
            for item in completed_results
            if (
                item.annual_average_skin_improvement_c
                is not None
            )
        ]

        coverage_values = [
            item.exposure_coverage_percent
            for item in completed_results
            if item.exposure_coverage_percent is not None
        ]
        
        batch.summary_json = {
            "completed_city_count": len(
                completed_results
            ),
            "mean_climate_adaptation_rate_percent": (
                round(
                    sum(rates) / len(rates),
                    4,
                )
                if rates
                else None
            ),
            "mean_exposure_coverage_percent": (
                round(
                    sum(coverage_values)
                    / len(coverage_values),
                    4,
                )
                if coverage_values
                else None
            ),
            "mean_annual_skin_improvement_c": (
                round(
                    sum(skin_values)
                    / len(skin_values),
                    4,
                )
                if skin_values
                else None
            ),
        }

    session.commit()

def reconcile_batch(db: Session, batch_id: str) -> None:
    """Kept for callers; refresh_batch_status is the single implementation."""
    refresh_batch_status(db, batch_id)
```

### File: `backend/app/services/ground_surface.py`
```python
"""Sky emissivity with cloud and steady ground surface temperature (ADR 0008).

Ground balance per unit horizontal area (positive terms leave the surface):

    (1 - rho_g) GHI + eps_g sigma T_sky^4
        = eps_g sigma T_g^4 + h_g (T_g - T_a) + K (T_g - T_soil)

f(T_g) = left - right is strictly decreasing and concave, so Newton from any
start converges monotonically after the first step.
"""

from __future__ import annotations

from app.services.model_parameters import get_parameter_value as _param
from app.services.psychrometrics import vapor_pressure_kpa


SIGMA = _param("stefan_boltzmann_constant")
BRUTSAERT_COEFFICIENT = _param("brutsaert_coefficient")
BRUTSAERT_EXPONENT = _param("brutsaert_exponent")
GROUND_H0 = _param("ground_convection_still_air_coefficient")
GROUND_H1 = _param("ground_convection_wind_coefficient")

KELVIN_OFFSET = 273.15

# Numerical (not physical) settings.
MINIMUM_VAPOR_PRESSURE_HPA = 0.1
NEWTON_TOLERANCE_K = 1e-6
NEWTON_MAX_ITERATIONS = 50


def brutsaert_cloud_sky_emissivity(
    air_temperature_c: float,
    relative_humidity_percent: float,
    cloud_cover_percent: float,
) -> float:
    air_k = air_temperature_c + KELVIN_OFFSET
    e_hpa = max(
        MINIMUM_VAPOR_PRESSURE_HPA,
        vapor_pressure_kpa(air_temperature_c, relative_humidity_percent) * 10.0,
    )
    clear = min(1.0, BRUTSAERT_COEFFICIENT * (e_hpa / air_k) ** BRUTSAERT_EXPONENT)
    cloud = min(1.0, max(0.0, cloud_cover_percent / 100.0))
    return cloud + (1.0 - cloud) * clear


def brutsaert_cloud_sky_temperature_c(
    air_temperature_c: float,
    relative_humidity_percent: float,
    cloud_cover_percent: float,
) -> float:
    emissivity = brutsaert_cloud_sky_emissivity(
        air_temperature_c, relative_humidity_percent, cloud_cover_percent
    )
    return emissivity ** 0.25 * (air_temperature_c + KELVIN_OFFSET) - KELVIN_OFFSET


def ground_convection_coefficient(wind_speed_m_s: float) -> float:
    return GROUND_H0 + GROUND_H1 * max(0.0, wind_speed_m_s)


def ground_energy_residual(
    ground_c: float,
    *,
    air_c: float,
    sky_c: float,
    ghi_w_m2: float,
    albedo: float,
    wind_speed_m_s: float,
    soil_c: float,
    emissivity: float,
    conductance_w_m2k: float,
) -> float:
    t = ground_c + KELVIN_OFFSET
    gains = (1.0 - albedo) * max(0.0, ghi_w_m2) + emissivity * SIGMA * (sky_c + KELVIN_OFFSET) ** 4
    losses = (
        emissivity * SIGMA * t**4
        + ground_convection_coefficient(wind_speed_m_s) * (ground_c - air_c)
        + conductance_w_m2k * (ground_c - soil_c)
    )
    return gains - losses


def solve_ground_surface_temperature_c(
    *,
    air_c: float,
    sky_c: float,
    ghi_w_m2: float,
    albedo: float,
    wind_speed_m_s: float,
    soil_c: float,
    emissivity: float,
    conductance_w_m2k: float,
) -> float:
    h = ground_convection_coefficient(wind_speed_m_s)
    kwargs = dict(
        air_c=air_c, sky_c=sky_c, ghi_w_m2=ghi_w_m2, albedo=albedo,
        wind_speed_m_s=wind_speed_m_s, soil_c=soil_c,
        emissivity=emissivity, conductance_w_m2k=conductance_w_m2k,
    )

    t = max(air_c, soil_c)
    for _ in range(NEWTON_MAX_ITERATIONS):
        f = ground_energy_residual(t, **kwargs)
        slope = -4.0 * emissivity * SIGMA * (t + KELVIN_OFFSET) ** 3 - h - conductance_w_m2k
        step = f / slope
        t -= step
        if abs(step) < NEWTON_TOLERANCE_K:
            return t

    raise RuntimeError(
        f"Ground surface balance did not converge (T_a = {air_c:.2f} C, GHI = {ghi_w_m2:.0f})"
    )
```

### File: `backend/app/services/job_service.py`
```python
from sqlalchemy.orm import Session
from datetime import datetime
from app.services.leases import derive_lease_state
from app.services.stored_requests import load_stored_request

from app.models.simulation_job import (
    SimulationJob,
)
from app.schemas.job import (
    SimulationJobDetail,
    SimulationJobResponse,
)
from app.schemas.simulation import (
    WeatherSimulationRequest,
)



def job_to_response(job: SimulationJob, *, now: datetime | None = None) -> SimulationJobResponse:
    return SimulationJobResponse(
        id=job.id,
        celery_task_id=job.celery_task_id,
        status=job.status,
        stage=job.stage,
        progress=job.progress,
        city_id=job.city_id,
        summary=job.summary_json,
        error_message=job.error_message,
        created_at=job.created_at,
        updated_at=job.updated_at,
        started_at=job.started_at,
        completed_at=job.completed_at,
        control_material_version_id=getattr(job, "control_material_version_id", None),
        rc_material_version_id=getattr(job, "rc_material_version_id", None),
        attempt=getattr(job, "attempt", 0) or 0,
        lease_owner=getattr(job, "lease_owner", None),
        lease_expires_at=getattr(job, "lease_expires_at", None),
        last_heartbeat_at=getattr(job, "last_heartbeat_at", None),
        lease_state=derive_lease_state(
            getattr(job, "lease_owner", None), getattr(job, "lease_expires_at", None), now
        ),
    )


def job_to_detail(job: SimulationJob, *, now: datetime | None = None) -> SimulationJobDetail:
    return SimulationJobDetail(
        **job_to_response(job, now=now).model_dump(),
        request=load_stored_request(WeatherSimulationRequest, job.request_json)
    )


def get_job_or_none(
    session: Session,
    job_id: str,
) -> SimulationJob | None:
    return session.get(
        SimulationJob,
        job_id,
    )
```

### File: `backend/app/services/job_state.py`
```python
"""Status enums and legal transitions for batches, cities and single jobs.

Every status write in the worker and the API goes through ``assert_*``;
an illegal transition is a programming error, not a runtime condition.
"""

from enum import StrEnum


class BatchStatus(StrEnum):
    QUEUED = "queued"
    RUNNING = "running"
    CANCELLING = "cancelling"
    COMPLETED = "completed"
    PARTIAL_COMPLETED = "partial_completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class CityStatus(StrEnum):
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class JobStatus(StrEnum):
    QUEUED = "queued"
    RUNNING = "running"
    CANCELLING = "cancelling"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    FAILED = "failed"


BATCH_TRANSITIONS: dict[BatchStatus, frozenset[BatchStatus]] = {
    BatchStatus.QUEUED: frozenset({
        BatchStatus.RUNNING, BatchStatus.CANCELLING, BatchStatus.CANCELLED, BatchStatus.FAILED,
    }),
    BatchStatus.RUNNING: frozenset({
        BatchStatus.COMPLETED, BatchStatus.PARTIAL_COMPLETED, BatchStatus.FAILED,
        BatchStatus.CANCELLING, BatchStatus.CANCELLED,
    }),
    BatchStatus.CANCELLING: frozenset({
        BatchStatus.CANCELLED, BatchStatus.PARTIAL_COMPLETED, BatchStatus.COMPLETED, BatchStatus.FAILED,
    }),
    # POST /retry-failed re-opens a batch.
    BatchStatus.FAILED: frozenset({BatchStatus.RUNNING}),
    BatchStatus.PARTIAL_COMPLETED: frozenset({BatchStatus.RUNNING}),
    BatchStatus.COMPLETED: frozenset(),
    BatchStatus.CANCELLED: frozenset(),
}

TERMINAL_BATCH = frozenset({
    BatchStatus.COMPLETED, BatchStatus.PARTIAL_COMPLETED, BatchStatus.FAILED, BatchStatus.CANCELLED,
})

CITY_TRANSITIONS: dict[CityStatus, frozenset[CityStatus]] = {
    CityStatus.QUEUED: frozenset({CityStatus.RUNNING, CityStatus.CANCELLED}),
    # RUNNING -> QUEUED: lease expired (reaper) or retryable failure.
    CityStatus.RUNNING: frozenset({
        CityStatus.COMPLETED, CityStatus.FAILED, CityStatus.CANCELLED, CityStatus.QUEUED,
    }),
    CityStatus.COMPLETED: frozenset(),
    # FAILED -> QUEUED: explicit POST /retry-failed (Stage 9; was missing).
    CityStatus.FAILED: frozenset({CityStatus.QUEUED}),
    CityStatus.CANCELLED: frozenset(),
}

TERMINAL_CITY = frozenset({CityStatus.COMPLETED, CityStatus.FAILED, CityStatus.CANCELLED})

JOB_TRANSITIONS: dict[JobStatus, frozenset[JobStatus]] = {
    JobStatus.QUEUED: frozenset({JobStatus.RUNNING, JobStatus.CANCELLED, JobStatus.FAILED}),
    # RUNNING -> QUEUED: lease expired, re-queued by the reaper.
    JobStatus.RUNNING: frozenset({
        JobStatus.COMPLETED, JobStatus.FAILED, JobStatus.CANCELLING, JobStatus.CANCELLED, JobStatus.QUEUED,
    }),
    # Cancel requested while the worker was finishing: any terminal outcome is legal.
    JobStatus.CANCELLING: frozenset({JobStatus.CANCELLED, JobStatus.COMPLETED, JobStatus.FAILED}),
    JobStatus.COMPLETED: frozenset(),
    JobStatus.FAILED: frozenset(),
    JobStatus.CANCELLED: frozenset(),
}

TERMINAL_JOB = frozenset({JobStatus.COMPLETED, JobStatus.FAILED, JobStatus.CANCELLED})


class IllegalTransition(Exception):
    pass


def assert_batch_transition(current: str, target: str) -> None:
    if BatchStatus(target) not in BATCH_TRANSITIONS[BatchStatus(current)]:
        raise IllegalTransition(f"batch {current} -> {target}")


def assert_city_transition(current: str, target: str) -> None:
    if CityStatus(target) not in CITY_TRANSITIONS[CityStatus(current)]:
        raise IllegalTransition(f"city {current} -> {target}")


def assert_job_transition(current: str, target: str) -> None:
    if JobStatus(target) not in JOB_TRANSITIONS[JobStatus(current)]:
        raise IllegalTransition(f"job {current} -> {target}")


def derive_batch_status(
    counts: dict[str, int],
    total: int,
    cancel_requested: bool = False,
) -> BatchStatus | None:
    """Same rule as global_batch_service.refresh_batch_status.

    Returns None while any city is still pending. ``cancel_requested`` makes
    a batch that produced nothing report CANCELLED rather than FAILED.
    """
    completed = counts.get("completed", 0)
    failed = counts.get("failed", 0)
    cancelled = counts.get("cancelled", 0)

    if completed + failed + cancelled < total:
        return None
    if cancelled == total:
        return BatchStatus.CANCELLED
    if completed == 0:
        return BatchStatus.CANCELLED if cancel_requested else BatchStatus.FAILED
    if failed or cancelled:
        return BatchStatus.PARTIAL_COMPLETED
    return BatchStatus.COMPLETED
```

### File: `backend/app/services/leases.py`
```python
"""Row-level leases for GlobalCityResult (Stage 7) and SimulationJob (Stage 9).

Contract
--------
* ``acquire_*`` is one atomic UPDATE ... RETURNING. A caller that gets False
  must exit without writing anything: another worker owns the row, or the row
  is terminal.
* ``heartbeat_*`` is the only way a worker writes to its row. It is guarded by
  ``lease_owner == owner``; when the guard fails the whole transaction is
  rolled back (so anything staged in the same session, e.g. a checkpoint
  upsert, is discarded too) and False is returned.
* All time comparisons use the database clock (``func.now()``) so that the
  API, the workers and the reaper agree regardless of host clock drift.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any

from sqlalchemy import func, or_, select, update
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.time import utc_now
from app.models.global_batch import GlobalCityResult
from app.models.simulation_job import SimulationJob
from app.services.job_state import CityStatus, JobStatus
from app.models.optimization_job import OptimizationJob



LeaseState = str  # "none" | "live" | "expired"


def db_now(session: Session) -> datetime:
    """Database clock; the reference for every lease comparison."""
    return session.scalar(select(func.now()))


def derive_lease_state(
    owner: str | None,
    expires_at: datetime | None,
    now: datetime | None = None,
) -> LeaseState:
    if owner is None or expires_at is None:
        return "none"
    now = now or utc_now()
    return "live" if expires_at > now else "expired"


def _ttl() -> timedelta:
    return timedelta(seconds=settings.CITY_LEASE_TTL_SECONDS)


def _acquire(
    session: Session,
    model: Any,
    row_id: str,
    owner: str,
    active_statuses: tuple[str, ...],
    running_status: str,
) -> bool:
    stmt = (
        update(model)
        .where(
            model.id == row_id,
            model.status.in_(active_statuses),
            or_(
                model.lease_owner.is_(None),
                model.lease_expires_at < func.now(),
                model.lease_owner == owner,  # re-entrant for the same owner
            ),
        )
        .values(
            lease_owner=owner,
            lease_expires_at=func.now() + _ttl(),
            last_heartbeat_at=func.now(),
            status=running_status,
            started_at=func.coalesce(model.started_at, func.now()),
        )
        .returning(model.id)
    )
    got = session.execute(stmt).scalar_one_or_none()
    session.commit()
    return got is not None


def _heartbeat(session: Session, model: Any, row_id: str, owner: str, values: dict[str, Any]) -> bool:
    payload: dict[str, Any] = {
        "last_heartbeat_at": func.now(),
        "lease_expires_at": func.now() + _ttl(),
    }
    payload.update(values)  # caller values win

    result = session.execute(
        update(model)
        .where(model.id == row_id, model.lease_owner == owner)
        .values(**payload)
    )

    if result.rowcount == 1:
        session.commit()
        return True

    # Lease lost: discard everything staged in this transaction.
    session.rollback()
    return False


def _release(session: Session, model: Any, row_id: str, owner: str) -> None:
    session.execute(
        update(model)
        .where(model.id == row_id, model.lease_owner == owner)
        .values(lease_owner=None, lease_expires_at=None)
    )
    session.commit()


# --- cities -----------------------------------------------------------------

def acquire_city_lease(session: Session, city_result_id: str, owner: str) -> bool:
    return _acquire(
        session, GlobalCityResult, city_result_id, owner,
        (CityStatus.QUEUED, CityStatus.RUNNING), CityStatus.RUNNING,
    )


def heartbeat_city_lease(session: Session, city_result_id: str, owner: str, **values: Any) -> bool:
    return _heartbeat(session, GlobalCityResult, city_result_id, owner, values)


def release_city_lease(session: Session, city_result_id: str, owner: str) -> None:
    _release(session, GlobalCityResult, city_result_id, owner)


# --- single simulation jobs -------------------------------------------------

def acquire_job_lease(session: Session, job_id: str, owner: str) -> bool:
    return _acquire(
        session, SimulationJob, job_id, owner,
        (JobStatus.QUEUED, JobStatus.RUNNING), JobStatus.RUNNING,
    )


def heartbeat_job_lease(session: Session, job_id: str, owner: str, **values: Any) -> bool:
    return _heartbeat(session, SimulationJob, job_id, owner, values)


def release_job_lease(session: Session, job_id: str, owner: str) -> None:
    _release(session, SimulationJob, job_id, owner)
    
def acquire_optimization_lease(session: Session, job_id: str, owner: str) -> bool:
    return _acquire(
        session, OptimizationJob, job_id, owner,
        (JobStatus.QUEUED, JobStatus.RUNNING), JobStatus.RUNNING,
    )


def heartbeat_optimization_lease(session: Session, job_id: str, owner: str, **values: Any) -> bool:
    return _heartbeat(session, OptimizationJob, job_id, owner, values)


def release_optimization_lease(session: Session, job_id: str, owner: str) -> None:
    _release(session, OptimizationJob, job_id, owner)
```

### File: `backend/app/services/longwave.py`
```python
"""Two-band longwave exchange: atmospheric window (8-13 um) vs. rest (ADR 0007).

Gray materials (infrared_emissivity_window is None) never use this module's
band arithmetic: two_node keeps the single-band formula for them, so every
existing result is unchanged.

Sky model: outside the window the near-surface atmosphere is treated as
opaque at air temperature; inside the window its emissivity eps_sky,W is
chosen so that the broadband sky radiance equals sigma T_sky^4 from the
configured sky-temperature method.
"""

from __future__ import annotations

from dataclasses import dataclass

from app.schemas.simulation import EnvironmentInput, MaterialInput
from app.services.model_parameters import get_parameter_value as _param
from app.services.planck import (
    WINDOW_LOWER_UM,
    WINDOW_UPPER_UM,
    band_fraction,
    band_power_k4,
    outside_window_emissivity,
)


KELVIN_OFFSET = 273.15
FALLBACK_SKY_OFFSET = _param("fallback_sky_temperature_offset")


@dataclass(frozen=True)
class LongwaveOptics:
    broadband: float
    window: float
    outside: float
    selective: bool


def resolve_longwave_optics(material: MaterialInput) -> LongwaveOptics:
    emissivity = material.infrared_emissivity
    window = material.infrared_emissivity_window

    if window is None:
        return LongwaveOptics(emissivity, emissivity, emissivity, False)

    # The schema has already rejected values outside [0, 1] beyond 1e-6.
    outside = min(1.0, max(0.0, outside_window_emissivity(emissivity, window)))
    return LongwaveOptics(emissivity, window, outside, True)


@dataclass(frozen=True)
class RadiantField:
    """Incoming longwave per band, divided by sigma (K^4)."""

    window_k4: float
    outside_k4: float
    sky_window_emissivity: float

    @property
    def total_k4(self) -> float:
        return self.window_k4 + self.outside_k4


def sky_window_emissivity(air_k: float, sky_k: float) -> float:
    fw = band_fraction(air_k)
    total = (sky_k / air_k) ** 4
    return min(1.0, max(0.0, (total - (1.0 - fw)) / fw))


def radiant_field(
    environment: EnvironmentInput,
    sky_view_factor: float | None = None,
) -> RadiantField:
    air_k = environment.air_temperature_c + KELVIN_OFFSET
    sky_c = environment.sky_temperature_c
    if sky_c is None:
        sky_c = environment.air_temperature_c - FALLBACK_SKY_OFFSET
    sky_k = sky_c + KELVIN_OFFSET
    surround_k = environment.mean_radiant_temperature_c + KELVIN_OFFSET
    f_sky = environment.sky_view_factor if sky_view_factor is None else sky_view_factor

    fw_air = band_fraction(air_k)
    eps_sky_w = sky_window_emissivity(air_k, sky_k)
    sky_window = eps_sky_w * fw_air * air_k**4
    sky_outside = (1.0 - fw_air) * air_k**4

    surround_window, _ = band_power_k4(surround_k)
    surround_total = surround_k**4

    return RadiantField(
        window_k4=f_sky * sky_window + (1.0 - f_sky) * surround_window,
        outside_k4=f_sky * sky_outside + (1.0 - f_sky) * (surround_total - surround_window),
        sky_window_emissivity=eps_sky_w,
    )


def net_exchange_k4(
    optics: LongwaveOptics,
    field: RadiantField,
    temperature_k: float,
) -> tuple[float, float, float]:
    """(net emission - absorption, its T-derivative, window-band part), / sigma."""
    window_emission, window_slope = band_power_k4(temperature_k)
    total_emission = temperature_k**4
    total_slope = 4.0 * temperature_k**3

    net_window = optics.window * (window_emission - field.window_k4)
    net_outside = optics.outside * (
        (total_emission - window_emission) - field.outside_k4
    )
    derivative = (
        optics.window * window_slope
        + optics.outside * (total_slope - window_slope)
    )
    return net_window + net_outside, derivative, net_window


def longwave_notes(optics: LongwaveOptics) -> list[str]:
    if not optics.selective:
        return []
    return [
        "selective longwave emitter: eps_W = "
        f"{optics.window:.3f} ({WINDOW_LOWER_UM:g}-{WINDOW_UPPER_UM:g} um), "
        f"eps_N = {optics.outside:.3f} (derived from broadband "
        f"{optics.broadband:.3f}); sky outside the window is treated as opaque "
        "at air temperature (ADR 0007)"
    ]

# --------------------------------------------------------------------------
# Two-zone garment (Stage 12, ADR 0010)
# --------------------------------------------------------------------------

def surroundings_fourth_power_k4(
    environment: EnvironmentInput,
    sky_view_factor: float | None = None,
) -> float:
    """F T_sky^4 + (1 - F) T_surround^4 for a given sky view (K^4)."""
    f = environment.sky_view_factor if sky_view_factor is None else sky_view_factor
    sky_c = environment.sky_temperature_c
    if sky_c is None:
        sky_c = environment.air_temperature_c - FALLBACK_SKY_OFFSET
    sky_k = sky_c + KELVIN_OFFSET
    surround_k = environment.mean_radiant_temperature_c + KELVIN_OFFSET
    return f * sky_k**4 + (1.0 - f) * surround_k**4


def zone_sky_views(sky_view_factor: float, separation: float) -> tuple[float, float]:
    """(sky view of the sky-facing zone, of the ground-facing zone).

    Zone areas are F and 1 - F, so F * up + (1 - F) * down == F for every s.
    """
    f, s = sky_view_factor, separation
    return f + s * (1.0 - f), f * (1.0 - s)


@dataclass(frozen=True)
class PreparedZone:
    name: str
    area_fraction: float
    sky_view_factor: float
    optics: LongwaveOptics
    field: RadiantField | None     # selective zones only
    surroundings_k4: float         # gray zones (and diagnostics)


def prepare_longwave_zones(
    material: MaterialInput,
    environment: EnvironmentInput,
    optics: LongwaveOptics,
) -> tuple[PreparedZone, ...] | None:
    """None for a uniform garment, so the Stage 11 code path is used unchanged."""
    ground = material.infrared_emissivity_ground_facing
    if ground is None:
        return None

    f = environment.sky_view_factor
    up_view, down_view = zone_sky_views(f, environment.zone_view_separation)
    ground_optics = LongwaveOptics(ground, ground, ground, False)

    zones: list[PreparedZone] = []
    for name, area, view, zone_optics in (
        ("sky_facing", f, up_view, optics),
        ("ground_facing", 1.0 - f, down_view, ground_optics),
    ):
        if area <= 0.0:
            continue
        zones.append(
            PreparedZone(
                name=name,
                area_fraction=area,
                sky_view_factor=view,
                optics=zone_optics,
                field=radiant_field(environment, sky_view_factor=view) if zone_optics.selective else None,
                surroundings_k4=surroundings_fourth_power_k4(environment, view),
            )
        )
    return tuple(zones)


def zoned_exchange_k4(
    zones: tuple[PreparedZone, ...],
    temperature_k: float,
) -> tuple[float, float, float | None]:
    """Area-weighted (net, d net/dT, window part) over zones, / sigma."""
    net = slope = 0.0
    window: float | None = None
    for zone in zones:
        if zone.field is not None:
            n, s, w = net_exchange_k4(zone.optics, zone.field, temperature_k)
            window = (window or 0.0) + zone.area_fraction * w
        else:
            eps = zone.optics.broadband
            n = eps * (temperature_k**4 - zone.surroundings_k4)
            s = 4.0 * eps * temperature_k**3
        net += zone.area_fraction * n
        slope += zone.area_fraction * s
    return net, slope, window


def zone_notes(zones: tuple[PreparedZone, ...] | None) -> list[str]:
    if not zones:
        return []
    parts = "; ".join(
        f"{z.name}: area {z.area_fraction:.2f}, sky view {z.sky_view_factor:.2f}, "
        f"eps {z.optics.broadband:.2f}{' (selective)' if z.optics.selective else ''}"
        for z in zones
    )
    return [
        f"two-zone garment (ADR 0010): {parts}. Both zones share one clothing "
        "surface temperature; the ground-facing zone is gray."
    ]
```

### File: `backend/app/services/material_fields.py`
```python
"""Material field manifest for ``GET /model/material-fields`` (Stage 4).

Everything is introspected from ``MaterialInput`` so bounds, defaults and
units cannot drift from the validation actually applied to requests.
"""

from __future__ import annotations

import types
from typing import Any, Union, get_args, get_origin

from pydantic.fields import FieldInfo
from pydantic_core import PydanticUndefined

from app.schemas.provenance import (
    MATERIAL_PHYSICAL_FIELD_ORDER,
    MaterialFieldDescriptor,
    MaterialFieldManifest,
    SourceType,
)
from app.schemas.simulation import MaterialInput
from app.services.model_parameters import build_model_metadata


def _bound(field: FieldInfo, attribute: str) -> float | None:
    for item in field.metadata:
        value = getattr(item, attribute, None)
        if value is not None:
            return float(value)
    return None


def _is_nullable(annotation: Any) -> bool:
    origin = get_origin(annotation)
    if origin is Union or origin is types.UnionType:
        return type(None) in get_args(annotation)
    return False


def _default(field: FieldInfo) -> float | None:
    value = field.default
    if value is PydanticUndefined or value is None:
        return None
    return float(value)


def _extra(field: FieldInfo, key: str) -> str | None:
    extra = field.json_schema_extra
    if isinstance(extra, dict):
        value = extra.get(key)
        return str(value) if value is not None else None
    return None


def describe_material_field(name: str) -> MaterialFieldDescriptor:
    field = MaterialInput.model_fields[name]

    return MaterialFieldDescriptor(
        name=name,
        unit=_extra(field, "unit") or "-",
        description=field.description or "",
        minimum=_bound(field, "ge"),
        maximum=_bound(field, "le"),
        default=_default(field),
        nullable=_is_nullable(field.annotation),
        derived_when_null=_extra(field, "derived_when_null"),
    )


def list_material_fields() -> list[MaterialFieldDescriptor]:
    return [describe_material_field(name) for name in MATERIAL_PHYSICAL_FIELD_ORDER]


def build_material_field_manifest() -> MaterialFieldManifest:
    return MaterialFieldManifest(
        **build_model_metadata().model_dump(),
        source_types=list(get_args(SourceType)),
        fields=list_material_fields(),
    )
```

### File: `backend/app/services/material_resolution.py`
```python
"""Resolve ``MaterialInput.material_version_id`` against the material library
(Stage 4, PR-4).

Contract
--------
* No ``material_version_id``      -> the input is returned untouched.
* Unknown id                       -> MaterialVersionNotFoundError (422).
* Physical field supplied and != stored value
                                   -> MaterialParameterConflictError (422).
* Physical field omitted           -> filled from the stored version.
* Provenance fields omitted        -> filled from the stored version.
* Stored version not a valid input -> MaterialVersionInvalidError (422).

Resolution happens once, at the API boundary, and the *resolved* request is
what gets persisted in ``request_json``. Workers never resolve again.
"""

from __future__ import annotations

import math
from typing import Any, TypeVar

from pydantic import BaseModel, ValidationError
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models.material import MaterialVersion
from app.schemas.provenance import MATERIAL_PHYSICAL_FIELD_ORDER
from app.schemas.simulation import MaterialInput


MATERIAL_NAME_MAX_LENGTH = 100
FLOAT_TOLERANCE = 1e-9
PROVENANCE_FIELDS: tuple[str, ...] = (
    "source_type",
    "source_reference",
    "parameter_sources",
)

RequestT = TypeVar("RequestT", bound=BaseModel)


class MaterialResolutionError(ValueError):
    """Base class; mapped to HTTP 422 by ``app.api.errors``."""

    code: str = "MATERIAL_RESOLUTION_ERROR"

    def __init__(
        self,
        message: str,
        *,
        context: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.context: dict[str, Any] = dict(context or {})

    def to_detail(self) -> dict[str, Any]:
        return {"code": self.code, "message": str(self), **self.context}


class MaterialVersionNotFoundError(MaterialResolutionError):
    code = "MATERIAL_VERSION_NOT_FOUND"


class MaterialVersionInvalidError(MaterialResolutionError):
    code = "MATERIAL_VERSION_INVALID"


class MaterialParameterConflictError(MaterialResolutionError):
    code = "MATERIAL_PARAMETER_CONFLICT"


def version_display_name(version: MaterialVersion) -> str:
    name = f"{version.material.name} v{version.version_number}"
    return name[:MATERIAL_NAME_MAX_LENGTH]

# absorbed_solar_to_body_fraction is deprecated (ADR 0005) and not mapped.
def material_input_from_version(version: MaterialVersion) -> MaterialInput:
    """The single mapping from a stored version to a simulation input."""
    try:
        return MaterialInput(
            name=version_display_name(version),
            clothing_insulation_clo=version.clothing_insulation_clo,
            evaporative_resistance_m2pa_w=version.evaporative_resistance_m2pa_w,
            clothing_area_factor=version.clothing_area_factor,
            solar_reflectance=version.solar_reflectance,
            solar_transmittance=version.solar_transmittance,
            infrared_emissivity=version.infrared_emissivity,
            infrared_transmittance=version.infrared_transmittance,
            projected_solar_area_factor=version.projected_solar_area_factor,
            material_version_id=version.id,
            source_type=version.source_type,
            source_reference=version.source_reference,
            parameter_sources=version.parameter_sources_json,
            infrared_emissivity_window=getattr(version, "infrared_emissivity_window", None),
            infrared_emissivity_ground_facing=getattr(version, "infrared_emissivity_ground_facing", None),
        )
    except ValidationError as error:
        first = error.errors()[0]
        raise MaterialVersionInvalidError(
            f"Material version {version.id} cannot be used as a simulation "
            f"input: {first['msg']}",
            context={
                "material_version_id": version.id,
                "field": ".".join(str(part) for part in first["loc"]),
            },
        ) from error


def load_material_version(session: Session, version_id: str) -> MaterialVersion:
    version = session.scalar(
        select(MaterialVersion)
        .options(selectinload(MaterialVersion.material))
        .where(MaterialVersion.id == version_id)
    )

    if version is None:
        raise MaterialVersionNotFoundError(
            f"Material version {version_id} does not exist",
            context={"material_version_id": version_id},
        )

    return version


def _values_differ(requested: float | None, stored: float | None) -> bool:
    if requested is None or stored is None:
        return (requested is None) != (stored is None)

    return not math.isclose(
        float(requested), float(stored),
        rel_tol=FLOAT_TOLERANCE, abs_tol=FLOAT_TOLERANCE,
    )


def resolve_material_input(
    session: Session,
    material: MaterialInput,
) -> MaterialInput:
    if material.material_version_id is None:
        return material

    version = load_material_version(session, material.material_version_id)
    stored = material_input_from_version(version)

    explicit = material.model_fields_set
    conflicts: list[dict[str, Any]] = []
    updates: dict[str, Any] = {}

    for field in MATERIAL_PHYSICAL_FIELD_ORDER:
        requested_value = getattr(material, field)
        stored_value = getattr(stored, field)

        if field in explicit:
            if _values_differ(requested_value, stored_value):
                conflicts.append(
                    {
                        "field": field,
                        "requested": requested_value,
                        "stored": stored_value,
                    }
                )
        else:
            updates[field] = stored_value

    if conflicts:
        names = ", ".join(item["field"] for item in conflicts)
        raise MaterialParameterConflictError(
            f"Request values differ from material version "
            f"{version.id} ({version_display_name(version)}) for: {names}. "
            "Remove material_version_id to simulate a modified garment.",
            context={
                "material_version_id": version.id,
                "conflicts": conflicts,
            },
        )

    for field in PROVENANCE_FIELDS:
        if field not in explicit or getattr(material, field) is None:
            updates[field] = getattr(stored, field)

    try:
        return MaterialInput.model_validate(
            {**material.model_dump(), **updates}
        )
    except ValidationError as error:
        raise MaterialVersionInvalidError(
            f"Resolved material input for version {version.id} is invalid: "
            f"{error.errors()[0]['msg']}",
            context={"material_version_id": version.id},
        ) from error


def resolve_request_materials(
    session: Session,
    request: RequestT,
    *,
    fields: tuple[str, ...] = ("control_material", "rc_material"),
) -> RequestT:
    """Resolve every MaterialInput attribute named in ``fields``.

    Returns the same object when nothing needed resolving, so callers can
    detect "no library involvement" with an identity check.
    """
    updates: dict[str, MaterialInput] = {}

    for field in fields:
        material = getattr(request, field, None)

        if material is None:
            continue

        resolved = resolve_material_input(session, material)

        if resolved is not material:
            updates[field] = resolved

    return request.model_copy(update=updates) if updates else request


def linked_material_version_ids(
    request: BaseModel,
) -> tuple[str | None, str | None]:
    """(control, rc) version ids recorded on the job row."""
    control = getattr(request, "control_material", None)
    rc = getattr(request, "rc_material", None)

    return (
        getattr(control, "material_version_id", None),
        getattr(rc, "material_version_id", None),
    )
```

### File: `backend/app/services/model_parameters.py`
```python
"""Registry of every numeric constant used by the thermal model (Stage 3).

Rules
-----
* ``two_node.py``, ``clothing.py``, ``body.py`` and ``environment_model.py``
  must not contain bare physical constants; they bind values from here.
* Changing any value changes ``model_parameter_set_sha256()``, which is
  written into every simulation response and checked by the golden test.
* ``source_type == "assumed"`` marks values that still need validation.

Stage 3 changes
---------------
* Removed: core_heat_capacity, skin_heat_capacity (derived from body mass),
  linearized_radiative_coefficient (clothing surface temperature is solved),
  sweating_gain_core/skin, skin_blood_flow_core/skin_gain (replaced by the
  Gagge 1986 controllers).
* Added: body_specific_heat, skin_mass_fraction, clothing_area_factor_slope,
  sweating_gain_body, sweating_skin_signal_scale, vasodilation_gain,
  vasoconstriction_gain, maximum_wettedness_*, shivering_coefficient.

Stage 5 changes
---------------
* Renamed: effective_radiation_area_ratio -> effective_radiation_area_ratio_standing;
  added effective_radiation_area_ratio_sitting (selected by PersonInput.position).
* Added: diffuse_hemisphere_fraction (ASHRAE 55 Appendix C shortwave geometry).
"""

from __future__ import annotations

import hashlib
import json

from app.schemas.provenance import (
    ModelMetadata,
    ModelParameter,
    ModelParameterManifest,
    SourceType,
)


MODEL_PARAMETER_SET_VERSION = "5.0.0"

GAGGE_1986 = (
    "Gagge, Fobelets & Berglund (1986). A standard predictive index of "
    "human response to the thermal environment. ASHRAE Trans. 92(2B):709-731"
)
ASHRAE_FUNDAMENTALS = (
    "ASHRAE Handbook - Fundamentals (2017), Chapter 9: Thermal Comfort"
)
ASHRAE_55_SET = (
    "ASHRAE Standard 55-2020, Normative Appendix D (SET reference procedure); "
    "reference implementations: pythermalcomfort.two_nodes_gagge, comf::calc2Node"
)
ISO_7730 = "ISO 7730:2005, Annex D (Fanger 1970 respiratory heat loss)"
PROTOTYPE = "Project prototype value (radiative-cooling-platform, Stage 0-1)"


def _p(
    name: str,
    value: float,
    unit: str,
    description: str,
    source_type: SourceType,
    reference: str,
    note: str | None = None,
) -> ModelParameter:
    return ModelParameter(
        name=name, value=value, unit=unit, description=description,
        source_type=source_type, reference=reference, note=note,
    )


_PARAMETERS: tuple[ModelParameter, ...] = (
    # --- physical constants -------------------------------------------------
    _p("stefan_boltzmann_constant", 5.670374419e-8, "W/(m^2 K^4)",
       "Stefan-Boltzmann constant", "standard", "CODATA 2018"),
    _p("magnus_a", 0.61078, "kPa",
       "Saturation vapour pressure, Tetens/Murray form: a*exp(b*T/(T+c))",
       "literature", "Murray (1967) J. Appl. Meteorol. 6:203-204"),
    _p("magnus_b", 17.2694, "-", "Saturation vapour pressure exponent factor",
       "literature", "Murray (1967) J. Appl. Meteorol. 6:203-204"),
    _p("magnus_c", 237.3, "C", "Saturation vapour pressure denominator offset",
       "literature", "Murray (1967) J. Appl. Meteorol. 6:203-204"),

    # --- body thermal mass (Stage 3, ADR 0001) ------------------------------
    _p("body_specific_heat", 3490.0, "J/(kg K)",
       "Average specific heat of body tissue (0.97 W h/(kg K))",
       "literature", GAGGE_1986),
    _p("skin_mass_fraction", 0.1, "-",
       "Fraction of body mass assigned to the skin node (alpha)",
       "literature", GAGGE_1986,
       "Gagge lets alpha vary with skin blood flow "
       "(alpha = 0.0418 + 0.745/(SKBF + 0.585)). Kept constant here so the "
       "node heat capacities are state-independent."),

    # --- convection ---------------------------------------------------------
    _p("natural_convection_minimum_coefficient", 3.1, "W/(m^2 K)",
       "Lower bound of the convective heat transfer coefficient (still air)",
       "literature", ASHRAE_FUNDAMENTALS + ", Table 6 (seated, v < 0.2 m/s)"),
    _p("forced_convection_coefficient", 8.3, "W/(m^2 K (m/s)^-0.5)",
       "h_c = 8.3 * v^0.5",
       "literature", ASHRAE_FUNDAMENTALS + ", Table 6 (Mitchell 1974: 8.3 v^0.6)",
       "Exponent simplified from 0.6 to 0.5 in this prototype."),

    # --- radiation geometry (Stage 5: posture-dependent, ADR 0006) ----------
    _p("effective_radiation_area_ratio_standing", 0.73, "-",
       "A_r / A_D for a standing person: fraction of the DuBois area exchanging "
       "radiation with the surroundings (longwave, sky-diffuse and "
       "ground-reflected shortwave)",
       "literature",
       "Fanger (1970) Thermal Comfort, McGraw-Hill; " + ASHRAE_FUNDAMENTALS
       + " (0.73 standing); " + ASHRAE_55_SET),
    _p("effective_radiation_area_ratio_sitting", 0.70, "-",
       "A_r / A_D for a seated person",
       "literature",
       "Fanger (1970) Thermal Comfort, McGraw-Hill; " + ASHRAE_FUNDAMENTALS
       + " (0.70 seated); " + ASHRAE_55_SET),
    _p("diffuse_hemisphere_fraction", 0.5, "-",
       "Share of the effective radiation area facing one hemisphere; scales the "
       "sky-diffuse (upper) and ground-reflected (lower) shortwave terms",
       "standard",
       "ASHRAE Standard 55-2020, Normative Appendix C (Arens et al. 2015): "
       "ERF = [0.5 f_eff f_svv (I_diff + I_TH R_floor) + f_p f_bes I_dir] "
       "alpha_SW / alpha_LW"),
   # --- longwave spectral bands (Stage 10, ADR 0007) -----------------------
    _p("second_radiation_constant", 14387.768775, "um K",
       "Planck second radiation constant c2 = h c / k_B",
       "standard", "CODATA 2018"),
    _p("atmospheric_window_lower_um", 8.0, "um",
       "Lower edge of the atmospheric transparency window",
       "literature",
       "Granqvist & Hjortsberg (1981) J. Appl. Phys. 52:4205-4220"),
    _p("atmospheric_window_upper_um", 13.0, "um",
       "Upper edge of the atmospheric transparency window",
       "literature",
       "Granqvist & Hjortsberg (1981) J. Appl. Phys. 52:4205-4220"),
    _p("emissivity_reference_temperature", 305.0, "K",
       "Temperature at which a broadband emissivity is Planck-weighted when it "
       "is split into window and out-of-window bands",
       "assumed", PROTOTYPE,
       "Typical clothing surface temperature outdoors; affects only the "
       "split of selective materials, never gray ones."),
    # --- clothing -----------------------------------------------------------
    _p("clo_to_si", 0.155, "m^2 K/(W clo)", "1 clo = 0.155 m^2 K/W",
       "standard", "ISO 9920:2007"),
    _p("clothing_area_factor_slope", 0.15, "1/clo",
       "f_cl = 1 + slope * clo when the material supplies no measured f_cl",
       "literature", GAGGE_1986 + "; " + ASHRAE_55_SET,
       "ASHRAE Fundamentals Ch. 9 quotes 1 + 0.3 clo (McCullough & Jones "
       "1984). 0.15 is retained for parity with the reference model."),
    _p("lewis_relation", 16.5, "K/kPa",
       "Lewis relation h_e / h_c at sea level",
       "standard", ASHRAE_FUNDAMENTALS),
    _p("clothing_vapor_permeation_efficiency", 0.45, "-",
       "i_cl used to derive Re,cl = R_cl / (LR * i_cl) when the material "
       "does not supply a measured evaporative resistance",
       "literature", GAGGE_1986 + "; ASHRAE 55 SET procedure"),
    _p("skin_emissivity", 0.95, "-",
       "Longwave emissivity of skin, used for radiation transmitted through "
       "IR-transparent textiles",
       "literature", "Steketee (1973) Phys. Med. Biol. 18:686-694"),

    # --- thermoregulation (Gagge 1986 controllers, Stage 3 ADR 0002) --------
    _p("core_setpoint_temperature", 36.8, "C", "Core temperature set point",
       "literature", GAGGE_1986),
    _p("skin_setpoint_temperature", 33.7, "C", "Skin temperature set point",
       "literature", GAGGE_1986),
    _p("sweating_gain_body", 170.0, "g/(h m^2 K)",
       "Regulatory sweating per K of mean-body warm signal (c_sw)",
       "literature", GAGGE_1986),
    _p("sweating_skin_signal_scale", 10.7, "K",
       "Exponential skin modifier of sweating: exp(WSIG_sk / 10.7)",
       "literature", GAGGE_1986),
    _p("maximum_sweat_rate", 500.0, "g/(h m^2)", "Upper bound of sweating",
       "literature", GAGGE_1986),
    _p("latent_heat_of_sweat", 0.68, "W h/g",
       "Converts g/(h m^2) to W/m^2 (h_fg 2430 kJ/kg / 3600)",
       "standard", ASHRAE_FUNDAMENTALS),
    _p("skin_diffusion_fraction", 0.06, "-",
       "Skin diffusion wettedness: w = 0.06 + 0.94 * E_rsw / E_max",
       "literature", GAGGE_1986),
    _p("maximum_wettedness_clothed_coefficient", 0.59, "-",
       "w_max = 0.59 * v^-0.08 for a clothed subject", "literature", GAGGE_1986),
    _p("maximum_wettedness_clothed_exponent", -0.08, "-",
       "Exponent of w_max (clothed)", "literature", GAGGE_1986),
    _p("maximum_wettedness_nude_coefficient", 0.38, "-",
       "w_max = 0.38 * v^-0.29 for a nude subject", "literature", GAGGE_1986),
    _p("maximum_wettedness_nude_exponent", -0.29, "-",
       "Exponent of w_max (nude)", "literature", GAGGE_1986),
    _p("skin_blood_flow_basal", 6.3, "kg/(h m^2)", "Neutral skin blood flow",
       "literature", GAGGE_1986),
    _p("vasodilation_gain", 120.0, "kg/(h m^2 K)",
       "SKBF = (6.3 + c_dil * WSIG_cr) / (1 + c_str * CSIG_sk)",
       "literature", ASHRAE_55_SET,
       "ASHRAE Fundamentals Ch. 9 prints 200; 120 is the value of the "
       "SET reference code and is kept for benchmark parity."),
    _p("vasoconstriction_gain", 0.5, "1/K",
       "c_str in the skin blood flow controller", "literature", GAGGE_1986),
    _p("skin_blood_flow_minimum", 0.5, "kg/(h m^2)", "Lower clamp",
       "literature", GAGGE_1986),
    _p("skin_blood_flow_maximum", 90.0, "kg/(h m^2)", "Upper clamp",
       "literature", GAGGE_1986),
    _p("core_skin_conductance_basal", 5.28, "W/(m^2 K)",
       "Core-to-skin conductance without blood flow",
       "literature", GAGGE_1986),
    _p("blood_heat_capacity_per_flow", 1.163, "W h/(kg K)",
       "Blood c_p per unit flow (4186 J/(kg K) / 3600)",
       "literature", GAGGE_1986),
    _p("shivering_coefficient", 19.4, "W/(m^2 K^2)",
       "M_shiv = 19.4 * CSIG_sk * CSIG_cr", "literature", GAGGE_1986),

    # --- metabolism and respiration -----------------------------------------
    _p("metabolic_rate_per_met", 58.15, "W/m^2", "1 met",
       "standard", "ISO 7730:2005 (58.2 W/m^2); ASHRAE 55 (58.15)"),
    _p("respiratory_latent_coefficient", 1.7e-5, "1/Pa",
       "E_res = c * M * (p_ref - p_a)", "standard", ISO_7730,
       "ISO 7730 uses 1.72e-5."),
    _p("respiratory_reference_vapor_pressure", 5867.0, "Pa",
       "Reference vapour pressure in E_res", "standard", ISO_7730),
    _p("respiratory_sensible_coefficient", 0.0014, "1/K",
       "C_res = c * M * (t_ex - t_a)", "standard", ISO_7730),
    _p("exhaled_air_temperature", 34.0, "C", "t_ex in C_res",
       "standard", ISO_7730),

    # --- environment fallbacks and empirical sky models ---------------------
    _p("fallback_sky_temperature_offset", 15.0, "K",
       "Sky temperature depression used when a fixed environment supplies "
       "no sky temperature", "assumed", PROTOTYPE),
    _p("swinbank_coefficient", 0.0552, "K^-0.5",
       "Clear-sky T_sky[K] = 0.0552 * T_air[K]^1.5",
       "literature", "Swinbank (1963) Q. J. R. Meteorol. Soc. 89:339-348"),
    # --- radiant environment (Stage 11, ADR 0008) ---------------------------
    _p("brutsaert_coefficient", 1.24, "(K/hPa)^(1/7)",
       "Clear-sky emissivity eps = 1.24 (e_a[hPa] / T_a[K])^(1/7)",
       "literature", "Brutsaert (1975) Water Resour. Res. 11:742-744"),
    _p("brutsaert_exponent", 1.0 / 7.0, "-",
       "Exponent of the Brutsaert clear-sky emissivity",
       "literature", "Brutsaert (1975) Water Resour. Res. 11:742-744"),
    _p("ground_convection_still_air_coefficient", 2.8, "W/(m^2 K)",
       "h_g = a + b v for a horizontal ground surface",
       "literature", "Watmuff, Charters & Proctor (1977) COMPLES 2:56"),
    _p("ground_convection_wind_coefficient", 3.0, "W/(m^2 K (m/s))",
       "Wind term b of the ground convection coefficient",
       "literature", "Watmuff, Charters & Proctor (1977) COMPLES 2:56",
       "Evaluated with the body-height wind; a 2 m wind would be slightly lower."),
)


MODEL_PARAMETERS: dict[str, ModelParameter] = {
    parameter.name: parameter for parameter in _PARAMETERS
}

if len(MODEL_PARAMETERS) != len(_PARAMETERS):
    raise RuntimeError("Duplicate model parameter names in registry")


def get_parameter_value(name: str) -> float:
    try:
        return MODEL_PARAMETERS[name].value
    except KeyError as error:
        raise KeyError(f"Unknown model parameter: {name}") from error


def list_model_parameters() -> list[ModelParameter]:
    return list(_PARAMETERS)


def model_parameter_set_sha256() -> str:
    serialized = json.dumps(
        [{"name": p.name, "value": p.value, "unit": p.unit} for p in _PARAMETERS],
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def build_model_metadata() -> ModelMetadata:
    return ModelMetadata(
        parameter_set_version=MODEL_PARAMETER_SET_VERSION,
        parameter_set_sha256=model_parameter_set_sha256(),
    )


def build_model_parameter_manifest() -> ModelParameterManifest:
    return ModelParameterManifest(
        **build_model_metadata().model_dump(),
        parameters=list_model_parameters(),
    )
```

### File: `backend/app/services/optimization/__init__.py`
```python
"""Inverse design (Stage 3, Stage 10)."""
```

### File: `backend/app/services/optimization/evaluator.py`
```python
"""Prepared samples and the pure evaluate(x) used by every search algorithm.

Preparation happens once: weather is fetched and sliced, interpolators are
built, and the control garment is simulated once per sample day. Afterwards
evaluate(x) only integrates the candidate garment.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from datetime import datetime, timedelta

from app.core.cities import get_city
from app.schemas.optimization import EvaluationMetrics, OptimizationCreate
from app.schemas.simulation import MaterialInput, ScenarioResult
from app.services.annual_sampling import build_weighted_sample_days
from app.services.climate_adaptation import get_next_month_start
from app.services.optimization.metrics import compute_metrics
from app.services.optimization.variables import candidate_material, variable_value
from app.services.two_node import simulate_material_with_interpolator
from app.services.weather import get_historical_weather_range, slice_weather_time_series
from app.services.weather_interpolation import WeatherInterpolator
from app.services.weather_quality import WeatherDataError
from app.services.environment_model import required_weather_variables

CACHE_DECIMALS = 6


@dataclass(frozen=True)
class PreparedSample:
    start_time_local: datetime
    weight_days: int
    interpolator: WeatherInterpolator
    control: ScenarioResult


@dataclass
class PreparationReport:
    samples: list[PreparedSample]
    skipped: list[dict] = field(default_factory=list)
    weather_payload_sha256: dict[str, str | None] = field(default_factory=dict)


async def prepare_samples(
    request: OptimizationCreate,
    *,
    progress: Callable[[int, str], None] | None = None,
) -> PreparationReport:
    city = get_city(request.city_id)
    report = PreparationReport(samples=[])

    for index, month in enumerate(request.months):
        if progress:
            progress(1 + round(18 * index / len(request.months)), f"preparing_{request.year}-{month:02d}")

        month_start = datetime(request.year, month, 1)
        prefetch_end = get_next_month_start(year=request.year, month=month) + timedelta(
            hours=request.local_start_hour, minutes=request.duration_minutes
        )
        month_weather = await get_historical_weather_range(
            city=city, start_time_local=month_start, end_time_local=prefetch_end,
            padding_hours=1, require_window_coverage=False,
            extra_variables=required_weather_variables(request.environment_assumptions),
        )
        report.weather_payload_sha256[f"{month:02d}"] = month_weather.source.payload_sha256

        days_in_month = (get_next_month_start(year=request.year, month=month) - month_start).days
        for day, weight in build_weighted_sample_days(
            days_in_month=days_in_month, sample_count=request.sample_days_per_month
        ):
            start = datetime(request.year, month, day, request.local_start_hour)
            try:
                sliced = slice_weather_time_series(
                    weather=month_weather, start_time_local=start,
                    duration_minutes=request.duration_minutes, padding_hours=1,
                )
                interpolator = WeatherInterpolator.from_series(
                    sliced, assumptions=request.environment_assumptions
                )
                control = simulate_material_with_interpolator(
                    request.duration_minutes, request.output_interval_minutes,
                    interpolator, request.person, request.control_material,
                )
            except WeatherDataError as error:
                report.skipped.append({
                    "sample_date_local": start.isoformat(),
                    "reason_code": error.code,
                    "message": str(error)[:500],
                })
                continue

            report.samples.append(PreparedSample(start, weight, interpolator, control))

    if not report.samples:
        raise RuntimeError("No usable sample day: every sample failed weather validation")

    return report


class MaterialEvaluator:
    """evaluate(x) -> metrics. Deterministic, memoised on x rounded to 1e-6."""

    def __init__(
        self,
        request: OptimizationCreate,
        samples: Sequence[PreparedSample],
        *,
        on_evaluation: Callable[[int], None] | None = None,
    ) -> None:
        if not samples:
            raise ValueError("MaterialEvaluator requires at least one prepared sample")
        self.request = request
        self.samples = list(samples)
        self.names: tuple[str, ...] = tuple(v.name for v in request.variables)
        self.on_evaluation = on_evaluation
        self.evaluation_count = 0
        self.simulation_count = 0
        self._cache: dict[tuple[float, ...], EvaluationMetrics | None] = {}

    # --- vector <-> parameters -------------------------------------------
    def key(self, x: Sequence[float]) -> tuple[float, ...]:
        return tuple(round(float(v), CACHE_DECIMALS) for v in x)

    def parameters(self, x: Sequence[float]) -> dict[str, float]:
        return {name: float(value) for name, value in zip(self.names, x, strict=True)}

    def vector(self, parameters: dict[str, float]) -> list[float]:
        return [float(parameters[name]) for name in self.names]

    def base_parameters(self) -> dict[str, float]:
        return {name: variable_value(self.request.base_material, name) for name in self.names}

    def material_for(self, parameters: dict[str, float]) -> MaterialInput | None:
        """Validated candidate, or None when it is physically impossible."""
        try:
            return candidate_material(self.request.base_material, parameters)
        except ValueError:  # pydantic.ValidationError is a ValueError
            return None

    # --- evaluation -------------------------------------------------------
    def evaluate(self, x: Sequence[float]) -> EvaluationMetrics | None:
        key = self.key(x)
        if key in self._cache:
            return self._cache[key]

        material = self.material_for(self.parameters(key))
        if material is None:
            self._cache[key] = None
            return None

        request = self.request
        pairs = []
        for sample in self.samples:
            candidate = simulate_material_with_interpolator(
                request.duration_minutes, request.output_interval_minutes,
                sample.interpolator, request.person, material,
            )
            pairs.append((sample.weight_days, sample.control, candidate))

        metrics = compute_metrics(
            pairs,
            skin_threshold_c=request.skin_threshold_c,
            core_threshold_c=request.core_threshold_c,
        )

        self._cache[key] = metrics
        self.evaluation_count += 1
        self.simulation_count += len(self.samples)

        if self.on_evaluation is not None:
            self.on_evaluation(self.evaluation_count)  # may raise (cancel / lease lost)

        return metrics

    def cached_points(self) -> list[tuple[dict[str, float], EvaluationMetrics]]:
        """Every successfully evaluated point (parameters rounded to the cache key)."""
        return [
            (self.parameters(key), metrics)
            for key, metrics in self._cache.items()
            if metrics is not None
        ]
```

### File: `backend/app/services/optimization/jobs.py`
```python
from datetime import datetime

from app.models.optimization_job import OptimizationJob
from app.schemas.optimization import (
    GenerationRecord,
    OptimizationCreate,
    OptimizationJobDetail,
    OptimizationJobResponse,
    OptimizationResult,
)
from app.services.leases import derive_lease_state
from app.services.stored_requests import load_stored_request

def optimization_to_response(job: OptimizationJob, *, now: datetime | None = None) -> OptimizationJobResponse:
    return OptimizationJobResponse(
        id=job.id, celery_task_id=job.celery_task_id, name=job.name, city_id=job.city_id,
        status=job.status, stage=job.stage, progress=job.progress,
        evaluation_count=job.evaluation_count or 0, error_message=job.error_message,
        created_at=job.created_at, updated_at=job.updated_at,
        started_at=job.started_at, completed_at=job.completed_at,
        attempt=job.attempt or 0, lease_owner=job.lease_owner,
        lease_expires_at=job.lease_expires_at, last_heartbeat_at=job.last_heartbeat_at,
        lease_state=derive_lease_state(job.lease_owner, job.lease_expires_at, now),
        cancel_requested_at=job.cancel_requested_at,
        control_material_version_id=job.control_material_version_id,
        base_material_version_id=job.base_material_version_id,
    )


def optimization_to_detail(job: OptimizationJob, *, now: datetime | None = None) -> OptimizationJobDetail:
    return OptimizationJobDetail(
        **optimization_to_response(job, now=now).model_dump(),
        request=load_stored_request(OptimizationCreate, job.request_json),
        history=[GenerationRecord.model_validate(r) for r in (job.history_json or [])],
        result=None if job.result_json is None else OptimizationResult.model_validate(job.result_json),
    )
```

### File: `backend/app/services/optimization/metrics.py`
```python
"""Exposure-weighted performance metrics of one garment over prepared samples."""

from __future__ import annotations

from collections.abc import Sequence

import numpy as np

from app.schemas.optimization import EvaluationMetrics
from app.schemas.simulation import ScenarioResult
from app.services.exposure_statistics import time_weighted_mean
from app.services.scenario_summary import pair_scenarios


def fraction_above(minutes: Sequence[float], values: Sequence[float], threshold: float) -> float:
    """Exact time fraction a piecewise-linear series spends above ``threshold``."""
    t = np.asarray(minutes, dtype=float)
    y = np.asarray(values, dtype=float)

    if t.size == 0:
        return 0.0
    if t.size == 1 or t[-1] <= t[0]:
        return float(y[0] > threshold)

    above = 0.0
    for t0, t1, y0, y1 in zip(t[:-1], t[1:], y[:-1], y[1:]):
        dt = t1 - t0
        if y0 > threshold and y1 > threshold:
            above += dt
        elif y0 <= threshold and y1 <= threshold:
            continue
        else:
            crossing = (threshold - y0) / (y1 - y0)
            above += dt * (1.0 - crossing) if y1 > threshold else dt * crossing

    return float(above / (t[-1] - t[0]))


def excess_integral(minutes: Sequence[float], values: Sequence[float], threshold: float) -> float:
    """Exact integral of max(0, y - threshold) dt for a piecewise-linear series (K*min)."""
    total = 0.0
    for t0, t1, y0, y1 in zip(minutes[:-1], minutes[1:], values[:-1], values[1:]):
        dt = float(t1) - float(t0)
        a, b = float(y0) - threshold, float(y1) - threshold
        if a >= 0.0 and b >= 0.0:
            total += dt * (a + b) / 2.0
        elif a <= 0.0 and b <= 0.0:
            continue
        else:
            crossing = a / (a - b)
            total += dt * crossing * a / 2.0 if a > 0.0 else dt * (1.0 - crossing) * b / 2.0
    return total


def compute_metrics(
    pairs: Sequence[tuple[int, ScenarioResult, ScenarioResult]],
    *,
    skin_threshold_c: float,
    core_threshold_c: float,
) -> EvaluationMetrics:
    """``pairs`` = (weight_days, control, candidate) per sample day."""
    if not pairs:
        raise ValueError("compute_metrics requires at least one sample")

    weights = np.asarray([w for w, _, _ in pairs], dtype=float)
    mean_skin, skin_exc, core_exc = [], [], []
    skin_dh, core_dh, cooling_skin, cooling_core = [], [], [], []
    peak_skin = peak_core = -np.inf

    for _, control, candidate in pairs:
        minutes = [p.minute for p in candidate.time_series]
        skin = [p.skin_temperature_c for p in candidate.time_series]
        core = [p.core_temperature_c for p in candidate.time_series]

        mean_skin.append(time_weighted_mean(minutes, skin))
        skin_exc.append(fraction_above(minutes, skin, skin_threshold_c))
        core_exc.append(fraction_above(minutes, core, core_threshold_c))
        skin_dh.append(excess_integral(minutes, skin, skin_threshold_c) / 60.0)
        core_dh.append(excess_integral(minutes, core, core_threshold_c) / 60.0)

        paired = pair_scenarios(control, candidate)
        cooling_skin.append(paired.average_skin_c)
        cooling_core.append(paired.average_core_c)

        peak_skin = max(peak_skin, candidate.peak_skin_temperature_c)
        peak_core = max(peak_core, candidate.peak_core_temperature_c)

    def weighted(values: list[float]) -> float:
        return float(np.average(values, weights=weights))

    return EvaluationMetrics(
        sample_count=len(pairs),
        mean_skin_temperature_c=round(weighted(mean_skin), 5),
        peak_skin_temperature_c=round(float(peak_skin), 5),
        peak_core_temperature_c=round(float(peak_core), 5),
        skin_exceedance_fraction=round(weighted(skin_exc), 6),
        core_exceedance_fraction=round(weighted(core_exc), 6),
        skin_excess_degree_hours=round(weighted(skin_dh), 6),
        core_excess_degree_hours=round(weighted(core_dh), 6),
        mean_skin_cooling_c=round(weighted(cooling_skin), 5),
        mean_core_cooling_c=round(weighted(cooling_core), 5),
    )
```

### File: `backend/app/services/optimization/objective.py`
```python
"""Scalarisation (Stage 10): feasibility-first ranking in normalised units.

* Constraint violations are divided by a per-metric scale before summing.
* Feasible:   sign * (value - reference) / scale + w * material_demand
* Infeasible: INFEASIBLE_OFFSET + normalised violation
The reference is the baseline garment, so DE tolerances act on differences of
order one rather than on the absolute magnitude of e.g. 39.5 C.
"""

from __future__ import annotations

from app.schemas.optimization import EvaluationMetrics, MetricConstraint, OptimizationCreate
from app.services.optimization.variables import demand_direction


METRIC_SCALES: dict[str, float] = {
    "mean_skin_temperature_c": 1.0,
    "peak_skin_temperature_c": 1.0,
    "peak_core_temperature_c": 1.0,
    "skin_exceedance_fraction": 0.1,
    "core_exceedance_fraction": 0.1,
    "skin_excess_degree_hours": 0.5,
    "core_excess_degree_hours": 0.5,
    "mean_skin_cooling_c": 1.0,
    "mean_core_cooling_c": 1.0,
    "material_demand": 0.1,
}

INVALID_OBJECTIVE = 1.0e6
INFEASIBLE_OFFSET = 1.0e3
FEASIBILITY_TOLERANCE = 1e-9


def metric_value(metrics: EvaluationMetrics, name: str) -> float:
    value = getattr(metrics, name)
    if value is None:
        raise ValueError(f"metric {name} is not available on this result")
    return float(value)


def constraint_label(constraint: MetricConstraint) -> str:
    return f"{constraint.metric} {constraint.operator} {constraint.threshold:g}"


def constraint_scale(constraint: MetricConstraint) -> float:
    return constraint.scale if constraint.scale is not None else METRIC_SCALES[constraint.metric]


def signed_excess(metrics: EvaluationMetrics, constraint: MetricConstraint) -> float:
    value = metric_value(metrics, constraint.metric)
    return value - constraint.threshold if constraint.operator == "<=" else constraint.threshold - value


def constraint_excess(metrics: EvaluationMetrics, constraints: list[MetricConstraint]) -> dict[str, float]:
    return {constraint_label(c): round(signed_excess(metrics, c), 6) for c in constraints}


def constraint_violation(metrics: EvaluationMetrics, constraints: list[MetricConstraint]) -> float:
    return sum(max(0.0, signed_excess(metrics, c)) / constraint_scale(c) for c in constraints)


def material_demand(parameters: dict[str, float], request: OptimizationCreate) -> float:
    """0 = every variable at its least demanding bound, 1 = all at the most demanding."""
    total = weight = 0.0
    for variable in request.variables:
        span = variable.upper - variable.lower
        x = parameters[variable.name]
        if demand_direction(variable) == "increasing":
            normalised = (x - variable.lower) / span
        else:
            normalised = (variable.upper - x) / span
        total += variable.demand_weight * min(1.0, max(0.0, normalised))
        weight += variable.demand_weight
    return total / weight


def objective_value(
    metrics: EvaluationMetrics, parameters: dict[str, float], request: OptimizationCreate
) -> float:
    if request.objective.metric == "material_demand":
        return material_demand(parameters, request)
    return metric_value(metrics, request.objective.metric)


def is_feasible(metrics: EvaluationMetrics | None, request: OptimizationCreate) -> bool:
    return metrics is not None and (
        constraint_violation(metrics, request.constraints) <= FEASIBILITY_TOLERANCE
    )


class ObjectiveFunction:
    def __init__(self, request: OptimizationCreate, reference: float = 0.0) -> None:
        self.request = request
        self.sign = 1.0 if request.objective.sense == "minimize" else -1.0
        self.scale = METRIC_SCALES[request.objective.metric]
        self.reference = reference
        self.demand_weight = (
            0.0 if request.objective.metric == "material_demand" else request.secondary_demand_weight
        )

    def __call__(self, metrics: EvaluationMetrics | None, parameters: dict[str, float]) -> float:
        if metrics is None:
            return INVALID_OBJECTIVE

        violation = constraint_violation(metrics, self.request.constraints)
        if violation > FEASIBILITY_TOLERANCE:
            return INFEASIBLE_OFFSET + violation

        value = self.sign * (objective_value(metrics, parameters, self.request) - self.reference) / self.scale
        value += self.demand_weight * material_demand(parameters, self.request)
        return min(value, INFEASIBLE_OFFSET - 1.0)
```

### File: `backend/app/services/optimization/requirement_map.py`
```python
"""Grid over two decision variables with the others fixed at the reported optimum."""

from __future__ import annotations

from collections.abc import Callable, Iterable

import numpy as np

from app.schemas.optimization import (
    FrontierPoint,
    OptimizationCreate,
    RequirementCell,
    RequirementMapResult,
)
from app.services.optimization.objective import constraint_violation, is_feasible, metric_value
from app.services.optimization.runner import Evaluator
from app.services.optimization.search_space import SearchSpace


TREND_RELATIVE_TOLERANCE = 1e-3   # of the map metric range; ignores solver noise
PLATEAU_TOLERANCE = 1e-6


def map_metric(request: OptimizationCreate) -> tuple[str, str]:
    """(metric, sense) drawn on the map. material_demand is not a physical metric."""
    if request.objective.metric != "material_demand":
        return request.objective.metric, request.objective.sense
    if request.constraints:
        first = request.constraints[0]
        return first.metric, ("minimize" if first.operator == "<=" else "maximize")
    return "skin_excess_degree_hours", "minimize"


def _least_demanding_feasible(
    values: np.ndarray, line: list[RequirementCell | None], direction: str
) -> float | None:
    order = range(len(values)) if direction == "increasing" else reversed(range(len(values)))
    for i in order:
        cell = line[i]
        if cell is not None and cell.feasible:
            return round(float(values[i]), 6)
    return None


def _most_lenient(values: Iterable[float | None], direction: str) -> float | None:
    present = [v for v in values if v is not None]
    if not present:
        return None
    return min(present) if direction == "increasing" else max(present)


def _trend(
    lines: list[list[RequirementCell | None]], direction: str, sense: str, tolerance: float
) -> str:
    seen: set[str] = set()
    for line in lines:
        ordered = line if direction == "increasing" else list(reversed(line))
        values = [c.metric_value for c in ordered if c is not None]
        for a, b in zip(values, values[1:]):
            gain = (a - b) if sense == "minimize" else (b - a)
            if gain > tolerance:
                seen.add("improves")
            elif gain < -tolerance:
                seen.add("worsens")
    if not seen:
        return "flat"
    return seen.pop() if len(seen) == 1 else "mixed"


def build_requirement_map(
    evaluator: Evaluator,
    request: OptimizationCreate,
    fixed_parameters: dict[str, float],
    *,
    space: SearchSpace,
    on_cell: Callable[[int, int], None] | None = None,
) -> RequirementMapResult:
    spec = request.requirement_map
    if spec is None:
        raise ValueError("request has no requirement_map")

    metric_name, sense = map_metric(request)
    xi, yi = space.index(spec.x_variable), space.index(spec.y_variable)
    x_dir, y_dir = space.directions[xi], space.directions[yi]
    xs = np.linspace(space.lower[xi], space.upper[xi], spec.resolution)
    ys = np.linspace(space.lower[yi], space.upper[yi], spec.resolution)
    total = len(xs) * len(ys)

    cells: list[list[RequirementCell | None]] = []
    done = 0
    for y in ys:
        row: list[RequirementCell | None] = []
        for x in xs:
            parameters = {**fixed_parameters, spec.x_variable: float(x), spec.y_variable: float(y)}
            metrics = evaluator.evaluate([parameters[n] for n in space.names])
            if metrics is None:
                row.append(None)
            else:
                row.append(RequirementCell(
                    x=round(float(x), 6),
                    y=round(float(y), 6),
                    metric_value=metric_value(metrics, metric_name),
                    constraint_violation=constraint_violation(metrics, request.constraints),
                    feasible=is_feasible(metrics, request),
                ))
            done += 1
            if on_cell is not None:
                on_cell(done, total)
        cells.append(row)

    columns = [[cells[j][i] for j in range(len(ys))] for i in range(len(xs))]

    frontier: list[FrontierPoint] = []
    for y, row in zip(ys, cells):
        required = _least_demanding_feasible(xs, row, x_dir)
        frontier.append(FrontierPoint(y=round(float(y), 6), minimum_x=required, required_x=required))

    required_y_per_column = [_least_demanding_feasible(ys, column, y_dir) for column in columns]

    values = [c.metric_value for row in cells for c in row if c is not None]
    metric_min = min(values) if values else None
    metric_max = max(values) if values else None
    spread = (metric_max - metric_min) if values else 0.0
    tolerance = TREND_RELATIVE_TOLERANCE * spread + 1e-12
    plateau = (
        sum(abs(v - metric_min) <= PLATEAU_TOLERANCE * (1.0 + abs(metric_min)) for v in values) / len(values)
        if values else None
    )

    return RequirementMapResult(
        x_variable=spec.x_variable,
        y_variable=spec.y_variable,
        x_values=[round(float(v), 6) for v in xs],
        y_values=[round(float(v), 6) for v in ys],
        cells=cells,
        frontier=frontier,
        # Legacy readings (y at its upper bound / x at its upper bound).
        minimum_x_at_max_y=frontier[-1].required_x,
        minimum_y_at_max_x=required_y_per_column[-1],
        fixed_parameters={k: v for k, v in fixed_parameters.items()
                          if k not in (spec.x_variable, spec.y_variable)},
        x_demand_direction=x_dir,
        y_demand_direction=y_dir,
        required_x_at_best_y=_most_lenient((p.required_x for p in frontier), x_dir),
        required_y_at_best_x=_most_lenient(required_y_per_column, y_dir),
        objective_trend_x=_trend(cells, x_dir, sense, tolerance) if values else None,
        objective_trend_y=_trend(columns, y_dir, sense, tolerance) if values else None,
        plateau_fraction=plateau,
        metric_min=metric_min,
        metric_max=metric_max,
    )
```

### File: `backend/app/services/optimization/runner.py`
```python
"""Differential evolution over the decision vector (scipy)."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Protocol, Sequence

import numpy as np
from scipy.optimize import LinearConstraint, differential_evolution

from app.schemas.optimization import EvaluationMetrics, GenerationRecord, OptimizationCreate
from app.services.optimization.objective import ObjectiveFunction, is_feasible, objective_value
from app.services.optimization.search_space import SearchSpace, build_search_space


class OptimizationCancelled(Exception):
    pass


class Evaluator(Protocol):
    evaluation_count: int

    def evaluate(self, x: Sequence[float]) -> EvaluationMetrics | None: ...
    def parameters(self, x: Sequence[float]) -> dict[str, float]: ...


@dataclass
class DifferentialEvolutionOutcome:
    x: np.ndarray
    fun: float
    message: str
    generations: int
    history: list[GenerationRecord] = field(default_factory=list)


def run_differential_evolution(
    evaluator: Evaluator,
    request: OptimizationCreate,
    *,
    space: SearchSpace | None = None,
    objective: ObjectiveFunction | None = None,
    on_generation: Callable[[GenerationRecord], None] | None = None,
) -> DifferentialEvolutionOutcome:
    space = space or build_search_space(request)
    objective = objective or ObjectiveFunction(request)
    history: list[GenerationRecord] = []

    def fun(x: np.ndarray) -> float:
        return objective(evaluator.evaluate(x), evaluator.parameters(x))

    def callback(intermediate_result) -> None:
        x = np.asarray(intermediate_result.x, dtype=float)
        metrics = evaluator.evaluate(x)  # memoised; no extra physics
        parameters = evaluator.parameters(x)
        record = GenerationRecord(
            generation=len(history) + 1,
            penalised_objective=float(intermediate_result.fun),
            best_parameters=parameters,
            best_metric_value=(
                None if metrics is None else objective_value(metrics, parameters, request)
            ),
            best_feasible=is_feasible(metrics, request),
            evaluation_count=evaluator.evaluation_count,
        )
        history.append(record)
        if on_generation is not None:
            on_generation(record)  # may raise OptimizationCancelled

    constraints = ()
    if space.linear_pairs:
        matrix = np.zeros((len(space.linear_pairs), len(space.names)))
        for row, (i, j) in enumerate(space.linear_pairs):
            matrix[row, i] = matrix[row, j] = 1.0
        constraints = (LinearConstraint(matrix, -np.inf, 1.0),)

    # Stage 10: the objective is normalised (order one, reference = baseline),
    # so convergence is purely absolute. tol=0 removes the relative term that
    # stopped earlier runs after one generation on a ~39.5 C objective.
    result = differential_evolution(
        fun,
        bounds=list(zip(space.lower, space.upper)),
        constraints=constraints,
        popsize=request.population_multiplier,
        maxiter=request.max_generations,
        rng=np.random.default_rng(request.seed),
        init="latinhypercube",
        updating="immediate",
        polish=False,
        tol=0.0,
        atol=request.convergence_tolerance,
        callback=callback,
    )

    return DifferentialEvolutionOutcome(
        x=np.asarray(result.x, dtype=float),
        fun=float(result.fun),
        message=str(result.message),
        generations=len(history),
        history=history,
    )
```

### File: `backend/app/services/optimization/search_space.py`
```python
"""Decision-variable bounds and optical energy constraints x_a + x_b <= 1.

Pairs
-----
* solar:   rho_sol + tau_sol <= 1                          (always)
* gray IR: eps + tau_IR <= 1                               (gray studies)
* band IR: eps_W + tau_IR <= 1 and eps_N + tau_IR <= 1     (selective studies)

A study is "selective" when a band emissivity is a decision variable or the
base garment already carries infrared_emissivity_window. The gray pair is then
implied (eps is a convex combination of eps_W and eps_N) and is not applied.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from app.schemas.optimization import EMISSIVITY_BAND_VARIABLES, OptimizationCreate
from app.services.optimization.variables import demand_direction, variable_value


SOLAR_PAIRS: tuple[tuple[str, str], ...] = (("solar_reflectance", "solar_transmittance"),)
GRAY_IR_PAIRS: tuple[tuple[str, str], ...] = (("infrared_emissivity", "infrared_transmittance"),)
BAND_IR_PAIRS: tuple[tuple[str, str], ...] = (
    ("infrared_emissivity_window", "infrared_transmittance"),
    ("infrared_emissivity_outside_window", "infrared_transmittance"),
)

LOWER_BOUND_SUM_TOLERANCE = 1e-9


@dataclass(frozen=True)
class SearchSpace:
    names: tuple[str, ...]
    lower: np.ndarray
    upper: np.ndarray
    # Index pairs (i, j) with x_i + x_j <= 1 (both are decision variables).
    linear_pairs: tuple[tuple[int, int], ...]
    directions: tuple[str, ...]

    def index(self, name: str) -> int:
        return self.names.index(name)

    def span(self, name: str) -> float:
        i = self.index(name)
        return float(self.upper[i] - self.lower[i])

    def least_demanding_bound(self, name: str) -> float:
        i = self.index(name)
        return float(self.lower[i] if self.directions[i] == "increasing" else self.upper[i])

    def most_demanding_bound(self, name: str) -> float:
        i = self.index(name)
        return float(self.upper[i] if self.directions[i] == "increasing" else self.lower[i])


def is_selective_study(request: OptimizationCreate) -> bool:
    names = {v.name for v in request.variables}
    return bool(EMISSIVITY_BAND_VARIABLES & names) or (
        request.base_material.infrared_emissivity_window is not None
    )


def optical_pairs(request: OptimizationCreate) -> tuple[tuple[str, str], ...]:
    return SOLAR_PAIRS + (BAND_IR_PAIRS if is_selective_study(request) else GRAY_IR_PAIRS)


def build_search_space(request: OptimizationCreate) -> SearchSpace:
    names = tuple(v.name for v in request.variables)
    lower = {v.name: float(v.lower) for v in request.variables}
    upper = {v.name: float(v.upper) for v in request.variables}
    base = request.base_material
    pairs: list[tuple[int, int]] = []

    for a, b in optical_pairs(request):
        has_a, has_b = a in upper, b in upper
        if has_a and has_b:
            pairs.append((names.index(a), names.index(b)))
        elif has_a:
            upper[a] = min(upper[a], 1.0 - variable_value(base, b))
        elif has_b:
            upper[b] = min(upper[b], 1.0 - variable_value(base, a))

        if has_a and has_b and lower[a] + lower[b] > 1.0 + LOWER_BOUND_SUM_TOLERANCE:
            raise ValueError(f"lower bounds of {a} and {b} already sum above 1")

    for name in names:
        if lower[name] >= upper[name]:
            raise ValueError(
                f"{name}: no feasible range left after applying the optical "
                f"energy constraint with the fixed base material "
                f"(lower {lower[name]}, effective upper {upper[name]:.4f})"
            )

    return SearchSpace(
        names=names,
        lower=np.asarray([lower[n] for n in names], dtype=float),
        upper=np.asarray([upper[n] for n in names], dtype=float),
        linear_pairs=tuple(pairs),
        directions=tuple(demand_direction(v) for v in request.variables),
    )

GROUND_IR_PAIRS: tuple[tuple[str, str], ...] = (
    ("infrared_emissivity_ground_facing", "infrared_transmittance"),
)


def has_ground_facing_zone(request: OptimizationCreate) -> bool:
    names = {v.name for v in request.variables}
    return "infrared_emissivity_ground_facing" in names or (
        request.base_material.infrared_emissivity_ground_facing is not None
    )


def optical_pairs(request: OptimizationCreate) -> tuple[tuple[str, str], ...]:
    pairs = SOLAR_PAIRS + (BAND_IR_PAIRS if is_selective_study(request) else GRAY_IR_PAIRS)
    return pairs + (GROUND_IR_PAIRS if has_ground_facing_zone(request) else ())
```

### File: `backend/app/services/optimization/service.py`
```python
"""End-to-end optimization (Stage 10).

Order: baseline -> differential evolution -> corners + most demanding design
-> requirement map -> best point -> sensitivity -> warnings -> verdict.
"""

from __future__ import annotations

import math
from collections.abc import Callable, Sequence
from itertools import product
from time import perf_counter

from app.schemas.optimization import (
    CandidateEvaluation,
    EvaluationMetrics,
    OptimizationCreate,
    OptimizationEstimate,
    OptimizationResult,
    ParameterSensitivity,
    RequirementMapResult,
    SkippedOptimizationSample,
)
from app.services.optimization.evaluator import MaterialEvaluator, PreparationReport
from app.services.optimization.objective import (
    METRIC_SCALES,
    ObjectiveFunction,
    constraint_excess,
    constraint_label,
    constraint_violation,
    is_feasible,
    material_demand,
    objective_value,
)
from app.services.optimization.requirement_map import build_requirement_map
from app.services.optimization.runner import run_differential_evolution
from app.services.optimization.search_space import SearchSpace, build_search_space
from app.services.reproducibility import parameter_fingerprint
from app.services.two_node import MODEL_VERSION


Reporter = Callable[..., None]  # (progress=, stage=, history_record=, force=)

SENSITIVITY_STEP_FRACTION = 0.05
BOUND_TOLERANCE_FRACTION = 1e-3
PLATEAU_WARNING_FRACTION = 0.2
SATURATION_REACH_FRACTION = 0.25
FLAT_OBJECTIVE_FRACTION = 0.01

EFFECT_METRICS: tuple[str, ...] = (
    "mean_skin_temperature_c",
    "peak_skin_temperature_c",
    "peak_core_temperature_c",
    "skin_exceedance_fraction",
    "core_exceedance_fraction",
    "skin_excess_degree_hours",
    "core_excess_degree_hours",
    "mean_skin_cooling_c",
    "mean_core_cooling_c",
)


# --------------------------------------------------------------------------
# Estimate
# --------------------------------------------------------------------------

def estimate_optimization(request: OptimizationCreate) -> OptimizationEstimate:
    n = len(request.variables)
    population = request.population_multiplier * n
    optimizer = population * (request.max_generations + 1)
    grid = request.requirement_map.resolution ** 2 if request.requirement_map else 0
    corners = 2 ** n
    sensitivity = 2 * n
    samples = sum(request.samples_per_month(m) for m in request.months)
    candidates = optimizer + grid + corners + sensitivity + 2  # + baseline + most demanding
    return OptimizationEstimate(
        variable_count=n,
        population_size=population,
        optimizer_evaluation_budget=optimizer,
        requirement_map_evaluations=grid,
        sample_count=samples,
        thermal_simulation_budget=candidates * samples + samples,  # + control once per sample
        weather_requests=len(request.months),
        corner_evaluations=corners,
        sensitivity_evaluations=sensitivity,
    )


# --------------------------------------------------------------------------
# Candidates and ranking
# --------------------------------------------------------------------------

def candidate_from(
    parameters: dict[str, float],
    metrics: EvaluationMetrics | None,
    request: OptimizationCreate,
) -> CandidateEvaluation:
    rounded = {k: round(float(v), 6) for k, v in parameters.items()}
    demand = round(material_demand(parameters, request), 6)
    if metrics is None:
        return CandidateEvaluation(
            parameters=rounded, metrics=None, objective_value=None,
            constraint_violation=None, feasible=False, material_demand=demand,
        )
    return CandidateEvaluation(
        parameters=rounded,
        metrics=metrics,
        objective_value=objective_value(metrics, parameters, request),
        constraint_violation=round(constraint_violation(metrics, request.constraints), 6),
        feasible=is_feasible(metrics, request),
        constraint_excess=constraint_excess(metrics, request.constraints),
        material_demand=demand,
    )


def evaluate_candidate(
    evaluator: MaterialEvaluator,
    request: OptimizationCreate,
    parameters: dict[str, float],
) -> CandidateEvaluation:
    return candidate_from(parameters, evaluator.evaluate(evaluator.vector(parameters)), request)


def candidate_rank(candidate: CandidateEvaluation, request: OptimizationCreate) -> tuple:
    """Lower is better: feasible first, then violation, objective, demand."""
    if candidate.metrics is None or candidate.objective_value is None:
        return (2, math.inf, math.inf, math.inf)
    sign = -1.0 if request.objective.sense == "maximize" else 1.0
    objective = round(sign * candidate.objective_value, 9)
    demand = candidate.material_demand or 0.0
    if candidate.feasible:
        return (0, 0.0, objective, demand)
    return (1, candidate.constraint_violation or 0.0, objective, demand)


def rank_points(
    points: Sequence[tuple[dict[str, float], EvaluationMetrics]],
    request: OptimizationCreate,
) -> CandidateEvaluation | None:
    candidates = [candidate_from(p, m, request) for p, m in points]
    if not candidates:
        return None
    return min(candidates, key=lambda c: candidate_rank(c, request))


def best_evaluated(evaluator: MaterialEvaluator, request: OptimizationCreate) -> CandidateEvaluation | None:
    return rank_points(evaluator.cached_points(), request)


def corner_parameters(space: SearchSpace) -> list[dict[str, float]]:
    """All 2^n corners of the (tightened) search box."""
    return [
        dict(zip(space.names, map(float, combo)))
        for combo in product(*[(lo, hi) for lo, hi in zip(space.lower, space.upper)])
    ]


def most_demanding_parameters(space: SearchSpace) -> dict[str, float]:
    return {name: space.most_demanding_bound(name) for name in space.names}


# --------------------------------------------------------------------------
# Sensitivity
# --------------------------------------------------------------------------

def sensitivity_analysis(
    evaluator: MaterialEvaluator,
    space: SearchSpace,
    best_parameters: dict[str, float],
) -> list[ParameterSensitivity]:
    """Central difference at the optimum, scaled to each variable's full range.

    A probe that is physically impossible falls back to the centre point, so the
    estimate degrades to a one-sided difference instead of being dropped.
    """
    center = evaluator.evaluate(evaluator.vector(best_parameters))
    if center is None:
        return []

    out: list[ParameterSensitivity] = []
    for i, name in enumerate(space.names):
        lower, upper = float(space.lower[i]), float(space.upper[i])
        span = upper - lower
        x = float(best_parameters[name])
        step = SENSITIVITY_STEP_FRACTION * span

        probes: list[tuple[float, EvaluationMetrics]] = []
        for value in (max(lower, x - step), min(upper, x + step)):
            metrics = evaluator.evaluate(evaluator.vector({**best_parameters, name: value}))
            probes.append((value, metrics) if metrics is not None else (x, center))

        (x_low, m_low), (x_high, m_high) = probes
        if x_high - x_low <= 1e-12:
            continue

        effects: dict[str, float] = {}
        for metric in EFFECT_METRICS:
            a, b = getattr(m_low, metric), getattr(m_high, metric)
            if a is None or b is None:
                continue
            effects[metric] = round((b - a) / (x_high - x_low) * span, 6)

        out.append(ParameterSensitivity(
            name=name, probe_low=round(x_low, 6), probe_high=round(x_high, 6),
            full_range_effects=effects,
        ))
    return out


def total_reach(sensitivities: list[ParameterSensitivity], metric: str) -> float:
    """Linearised upper bound on how far the search box can move ``metric``."""
    return sum(abs(s.full_range_effects.get(metric, 0.0)) for s in sensitivities)


# --------------------------------------------------------------------------
# Warnings and verdict
# --------------------------------------------------------------------------

def build_warnings(
    request: OptimizationCreate,
    space: SearchSpace,
    best: CandidateEvaluation,
    baseline: CandidateEvaluation,
    most_demanding: CandidateEvaluation | None,
    requirement_map: RequirementMapResult | None,
    sensitivities: list[ParameterSensitivity],
) -> list[str]:
    warnings: list[str] = []

    # 1. Optimum on a bound.
    at_lower_bound: set[str] = set()
    for i, name in enumerate(space.names):
        span = float(space.upper[i] - space.lower[i])
        x = best.parameters.get(name)
        if x is None:
            continue
        if abs(x - space.lower[i]) <= BOUND_TOLERANCE_FRACTION * span:
            at_lower_bound.add(name)
            warnings.append(
                f"best {name} sits at its lower search bound ({space.lower[i]:g}); "
                "the optimum may lie outside the searched range"
            )
        elif abs(x - space.upper[i]) <= BOUND_TOLERANCE_FRACTION * span:
            warnings.append(
                f"best {name} sits at its upper search bound ({space.upper[i]:g}); "
                "the optimum may lie outside the searched range"
            )

    # 2. Constraints out of reach / saturated threshold metrics.
    for constraint in request.constraints:
        label = constraint_label(constraint)
        excess = best.constraint_excess.get(label, 0.0)
        if excess <= 0:
            continue
        reach = total_reach(sensitivities, constraint.metric)
        if reach < excess:
            warnings.append(
                f"{label}: violated by {excess:.4g}, but the whole search range moves "
                f"{constraint.metric} by only about {reach:.4g} (linearised at the "
                "optimum); the target is out of reach of the selected variables"
            )
        if constraint.metric.endswith("exceedance_fraction") and reach < SATURATION_REACH_FRACTION * excess:
            replacement = constraint.metric.replace("exceedance_fraction", "excess_degree_hours")
            warnings.append(
                f"{constraint.metric} is saturated: the threshold is crossed in almost "
                f"the whole design space, so the metric has no usable gradient. Use "
                f"{replacement}, which keeps one."
            )

    # 3. Flat objective.
    if request.objective.metric != "material_demand" and sensitivities:
        reach = total_reach(sensitivities, request.objective.metric)
        if reach < FLAT_OBJECTIVE_FRACTION * METRIC_SCALES[request.objective.metric]:
            warnings.append(
                f"objective {request.objective.metric} is flat over the search range "
                f"(total linearised effect {reach:.3g}); the reported optimum is arbitrary"
            )

    # 4. Non-monotone performance.
    if (
        request.objective.metric != "material_demand"
        and most_demanding is not None
        and most_demanding.objective_value is not None
        and best.objective_value is not None
        and best.feasible == most_demanding.feasible
    ):
        sign = -1.0 if request.objective.sense == "maximize" else 1.0
        margin = 1e-6 * METRIC_SCALES[request.objective.metric]
        if sign * best.objective_value < sign * most_demanding.objective_value - margin:
            warnings.append(
                "best beats the most demanding design: performance is non-monotone in "
                "at least one variable (check demand directions and the trends below)"
            )

    # 5. Requirement map readings.
    if requirement_map is not None:
        for axis, variable, trend, required in (
            ("x", requirement_map.x_variable, requirement_map.objective_trend_x,
             requirement_map.required_x_at_best_y),
            ("y", requirement_map.y_variable, requirement_map.objective_trend_y,
             requirement_map.required_y_at_best_x),
        ):
            if trend == "mixed":
                warnings.append(
                    f"map metric is non-monotone along {variable}; requirement readings "
                    "are least-demanding feasible values, not thresholds"
                )
            elif trend == "worsens":
                warnings.append(
                    f"performance worsens as {variable} becomes more demanding; its "
                    "demand_direction is probably inverted for this scenario"
                )
            if required is not None and abs(required - space.least_demanding_bound(variable)) <= 1e-9:
                warnings.append(
                    f"{variable} requirement reads at its least demanding bound "
                    f"({required:g}): the true requirement lies beyond the searched range"
                )
        if (requirement_map.plateau_fraction or 0.0) > PLATEAU_WARNING_FRACTION:
            warnings.append(
                f"{requirement_map.plateau_fraction:.0%} of map cells share the minimum; "
                "ties are resolved towards the least demanding design"
            )

    # 6. Baseline tie.
    if all(abs(best.parameters[k] - baseline.parameters.get(k, math.nan)) < 1e-6 for k in best.parameters):
        warnings.append("best equals the baseline garment")

    # 7. Mean radiant temperature proxy (ADR 0007, ADR 0008).
    method = request.environment_assumptions.mean_radiant_temperature_method
    ir_names = {"infrared_emissivity", "infrared_emissivity_window", "infrared_emissivity_outside_window", "infrared_emissivity_ground_facing"}
    if method == "air_plus_solar_linear" and ir_names & set(space.names):
        warnings.append(
            "air_plus_solar_linear adds a GHI term to the non-sky longwave temperature although "
            "body shortwave is computed explicitly, so the sun is counted twice and hot "
            "surroundings are over-stated (ADR 0008). Infrared conclusions should be checked "
            "with mean_radiant_temperature_method = ground_energy_balance."
        )
        for name in ("infrared_emissivity", "infrared_emissivity_outside_window"):
            if name in at_lower_bound:
                warnings.append(
                    f"low {name} is favoured under the double-counting proxy; do not report "
                    "this without the ground_energy_balance rerun"
                )

    # 8. Two-zone garments (ADR 0010).
    if "infrared_emissivity_ground_facing" in space.names:
        s = request.environment_assumptions.zone_view_separation
        if s < 0.05:
            warnings.append(
                "zone_view_separation is ~0: both zones see the same radiant field, so only "
                "the area-weighted emissivity is identifiable; ground-facing and sky-facing "
                "values are not separately meaningful"
            )
        warnings.append(
            f"the ground-facing emissivity requirement depends on the assumed "
            f"zone_view_separation = {s:g} (not measured, ADR 0010); report it together "
            "with the separation sweep of experiment L2"
        )
        
    return warnings


def _verdict(
    request: OptimizationCreate,
    best: CandidateEvaluation,
    most_demanding: CandidateEvaluation | None,
) -> tuple[str, str]:
    metric = request.objective.metric
    value = "n/a" if best.objective_value is None else f"{best.objective_value:.4f}"
    if not request.constraints:
        return "unconstrained", f"No constraints were given; best {metric} = {value}."
    if best.feasible:
        return "feasible", (
            f"All constraints satisfied. Best {metric} = {value} "
            f"(material demand {best.material_demand:.3f})."
        )

    excess = "; ".join(f"{k} (+{v:.4g})" for k, v in best.constraint_excess.items() if v > 0)
    text = (
        "No candidate inside the bounds satisfies the constraints. Smallest normalised "
        f"violation {best.constraint_violation:.4f}: {excess}."
    )
    if most_demanding is not None and most_demanding.metrics is not None and not most_demanding.feasible:
        text += (
            " The most demanding design is also infeasible: the target is beyond the "
            "passive limit of this model for this climate, activity and garment."
        )
    return "infeasible", text


# --------------------------------------------------------------------------
# Orchestration
# --------------------------------------------------------------------------

def execute_optimization(
    request: OptimizationCreate,
    evaluator: MaterialEvaluator,
    preparation: PreparationReport,
    *,
    report: Reporter | None = None,
) -> OptimizationResult:
    started = perf_counter()

    def progress(value: int, stage: str, **extra) -> None:
        if report is not None:
            report(progress=value, stage=stage, **extra)

    space = build_search_space(request)

    # 1. Baseline; it is also the reference of the normalised objective.
    progress(20, "evaluating_baseline", force=True)
    baseline = evaluate_candidate(evaluator, request, evaluator.base_parameters())
    reference = (
        baseline.objective_value
        if baseline.objective_value is not None and request.objective.metric != "material_demand"
        else 0.0
    )
    objective = ObjectiveFunction(request, reference=reference)

    # 2. Differential evolution.
    generations = request.max_generations
    outcome = run_differential_evolution(
        evaluator,
        request,
        space=space,
        objective=objective,
        on_generation=lambda record: progress(
            20 + round(64 * min(record.generation, generations) / generations),
            f"generation_{record.generation}",
            history_record=record,
            force=True,
        ),
    )

    # 3. Corners and the most demanding design (populate the cache).
    progress(84, "evaluating_corners", force=True)
    corners = [evaluate_candidate(evaluator, request, p) for p in corner_parameters(space)]
    corner_best = min(corners, key=lambda c: candidate_rank(c, request))
    most_demanding = evaluate_candidate(evaluator, request, most_demanding_parameters(space))

    anchor = best_evaluated(evaluator, request) or evaluate_candidate(
        evaluator, request, evaluator.parameters(outcome.x)
    )

    # 4. Requirement map with the other variables at the current optimum.
    requirement_map = None
    if request.requirement_map is not None:
        progress(86, "building_requirement_map", force=True)
        requirement_map = build_requirement_map(
            evaluator,
            request,
            anchor.parameters,
            space=space,
            on_cell=lambda done, total: progress(
                86 + round(10 * done / total), "building_requirement_map"
            ),
        )

    # 5. Final reported point over everything evaluated so far.
    best = best_evaluated(evaluator, request) or anchor

    # 6. Sensitivity at that point (probes do not change ``best``).
    progress(97, "sensitivity_analysis", force=True)
    sensitivities = sensitivity_analysis(evaluator, space, best.parameters)

    warnings = build_warnings(
        request, space, best, baseline, most_demanding, requirement_map, sensitivities
    )
    verdict, message = _verdict(request, best, most_demanding)

    return OptimizationResult(
        verdict=verdict,
        message=message,
        objective=request.objective,
        constraints=request.constraints,
        best=best,
        baseline=baseline,
        optical_upper_bound=most_demanding,
        best_corner=corner_best,
        requirement_map=requirement_map,
        sample_count=len(preparation.samples),
        skipped_samples=[SkippedOptimizationSample.model_validate(s) for s in preparation.skipped],
        weather_payload_sha256=preparation.weather_payload_sha256,
        evaluation_count=evaluator.evaluation_count,
        simulation_count=evaluator.simulation_count + len(preparation.samples),
        generations=outcome.generations,
        algorithm=request.algorithm,
        algorithm_message=outcome.message,
        elapsed_seconds=round(perf_counter() - started, 3),
        model_version=MODEL_VERSION,
        parameter_fingerprint=parameter_fingerprint(request.environment_assumptions),
        warnings=warnings,
        sensitivities=sensitivities,
        objective_reference=reference,
        objective_scale=objective.scale,
    )
```

### File: `backend/app/services/optimization/variables.py`
```python
"""Decision-variable semantics shared by search space, evaluator and objective.

Band emissivities
-----------------
* infrared_emissivity_window: eps in 8-13 um. Varying it alone keeps the
  out-of-window emissivity of the base garment fixed.
* infrared_emissivity_outside_window: eps outside the window. Virtual: it is
  mapped to the broadband infrared_emissivity at the reference temperature.
A gray base garment has eps_W = eps_N = infrared_emissivity.
"""

from __future__ import annotations

from app.schemas.optimization import DEFAULT_DEMAND_DIRECTION, DecisionVariable
from app.schemas.simulation import MaterialInput
from app.services.clothing import derive_evaporative_resistance_m2pa_w
from app.services.planck import broadband_emissivity, outside_window_emissivity


WINDOW = "infrared_emissivity_window"
OUTSIDE_WINDOW = "infrared_emissivity_outside_window"

PROVENANCE_RESET = {
    "material_version_id": None,
    "parameter_sources": None,
    "source_type": "derived",
    "source_reference": "optimization candidate",
}


def demand_direction(variable: DecisionVariable) -> str:
    return variable.demand_direction or DEFAULT_DEMAND_DIRECTION[variable.name]


def variable_value(material: MaterialInput, name: str) -> float:
    """Value of a decision variable on a concrete garment (handles virtual ones)."""
    if name in (WINDOW, OUTSIDE_WINDOW):
        window = material.infrared_emissivity_window
        if window is None:
            return float(material.infrared_emissivity)
        if name == WINDOW:
            return float(window)
        return float(outside_window_emissivity(material.infrared_emissivity, window))

    if name == "infrared_emissivity_ground_facing" and material.infrared_emissivity_ground_facing is None:
        # Uniform base garment: the ground-facing zone starts at the broadband value.
        return float(material.infrared_emissivity)
    
    if name == "evaporative_resistance_m2pa_w" and material.evaporative_resistance_m2pa_w is None:
        return float(derive_evaporative_resistance_m2pa_w(material.clothing_insulation_clo))

    return float(getattr(material, name))


def candidate_material(base: MaterialInput, parameters: dict[str, float]) -> MaterialInput:
    """Validated candidate garment. Raises ValueError when physically impossible."""
    update = {name: float(value) for name, value in parameters.items()}
    outside = update.pop(OUTSIDE_WINDOW, None)

    if WINDOW in update or outside is not None:
        window = update.get(WINDOW)
        if window is None:
            window = variable_value(base, WINDOW)
        if outside is None:
            outside = variable_value(base, OUTSIDE_WINDOW)
        update[WINDOW] = window
        update["infrared_emissivity"] = broadband_emissivity(window, outside)

    return MaterialInput.model_validate({**base.model_dump(), **update, **PROVENANCE_RESET})
```

### File: `backend/app/services/planck.py`
```python
"""Planck band integrals (Stage 10, ADR 0007).

F(lambda*T) = integral_0^lambda E_b,lambda d lambda / (sigma T^4).

For zeta = c2/(lambda T) >= 1 the exponential series of Siegel & Howell is
used; for zeta < 1 the Bernoulli series of integral_0^zeta u^3/(e^u-1) du.
Both are accurate to ~1e-12 in their ranges, so no table is needed.
"""

from __future__ import annotations

from math import exp, expm1, pi

from app.services.model_parameters import get_parameter_value as _param


SECOND_RADIATION_CONSTANT = _param("second_radiation_constant")  # um K
WINDOW_LOWER_UM = _param("atmospheric_window_lower_um")
WINDOW_UPPER_UM = _param("atmospheric_window_upper_um")
EMISSIVITY_REFERENCE_K = _param("emissivity_reference_temperature")

# Numerical (not physical) settings.
_NORMALIZATION = 15.0 / pi**4
_SERIES_SWITCH_ZETA = 1.0
_MAX_TERMS = 60
_OVERFLOW_ZETA = 700.0


def _lower_integral(zeta: float) -> float:
    """integral_0^zeta u^3 / (e^u - 1) du, valid for zeta < 2 pi."""
    z2 = zeta * zeta
    return zeta**3 * (
        1.0 / 3.0
        - zeta / 8.0
        + z2 / 60.0
        - z2**2 / 5040.0
        + z2**3 / 272160.0
        - z2**4 / 13305600.0
    )


def _upper_integral(zeta: float) -> float:
    """integral_zeta^inf u^3 / (e^u - 1) du."""
    total = 0.0
    for n in range(1, _MAX_TERMS + 1):
        term = exp(-n * zeta) / n * (
            zeta**3 + 3.0 * zeta**2 / n + 6.0 * zeta / n**2 + 6.0 / n**3
        )
        total += term
        if term <= 1e-16 * total:
            break
    return total


def blackbody_fraction(lambda_t_um_k: float) -> float:
    """Fraction of blackbody emission below wavelength lambda at temperature T."""
    if lambda_t_um_k <= 0.0:
        return 0.0
    zeta = SECOND_RADIATION_CONSTANT / lambda_t_um_k
    if zeta < _SERIES_SWITCH_ZETA:
        return max(0.0, 1.0 - _NORMALIZATION * _lower_integral(zeta))
    if zeta > _OVERFLOW_ZETA:
        return 0.0
    return min(1.0, _NORMALIZATION * _upper_integral(zeta))


def blackbody_fraction_slope(lambda_t_um_k: float) -> float:
    """dF/d(lambda T) in 1/(um K)."""
    if lambda_t_um_k <= 0.0:
        return 0.0
    zeta = SECOND_RADIATION_CONSTANT / lambda_t_um_k
    if zeta > _OVERFLOW_ZETA:
        return 0.0
    return _NORMALIZATION * zeta**4 / (lambda_t_um_k * expm1(zeta))


def band_fraction(
    temperature_k: float,
    lower_um: float = WINDOW_LOWER_UM,
    upper_um: float = WINDOW_UPPER_UM,
) -> float:
    return blackbody_fraction(upper_um * temperature_k) - blackbody_fraction(
        lower_um * temperature_k
    )


def band_power_k4(
    temperature_k: float,
    lower_um: float = WINDOW_LOWER_UM,
    upper_um: float = WINDOW_UPPER_UM,
) -> tuple[float, float]:
    """(band emission / sigma, d/dT of it) in K^4 and K^3."""
    t = temperature_k
    fraction = band_fraction(t, lower_um, upper_um)
    slope = (
        upper_um * blackbody_fraction_slope(upper_um * t)
        - lower_um * blackbody_fraction_slope(lower_um * t)
    )
    return fraction * t**4, 4.0 * t**3 * fraction + t**4 * slope


def outside_window_emissivity(
    broadband: float,
    window: float,
    reference_k: float = EMISSIVITY_REFERENCE_K,
) -> float:
    """eps_N such that F_W eps_W + (1 - F_W) eps_N = eps_broadband at T_ref."""
    fw = band_fraction(reference_k)
    return (broadband - fw * window) / (1.0 - fw)


def broadband_emissivity(
    window: float,
    outside: float,
    reference_k: float = EMISSIVITY_REFERENCE_K,
) -> float:
    fw = band_fraction(reference_k)
    return fw * window + (1.0 - fw) * outside


def planck_shape(wavelength_um: float, temperature_k: float) -> float:
    """Spectral emissive power up to the constant c1 (use for ratios only)."""
    zeta = SECOND_RADIATION_CONSTANT / (wavelength_um * temperature_k)
    if zeta > _OVERFLOW_ZETA:
        return 0.0
    return 1.0 / (wavelength_um**5 * expm1(zeta))
```

### File: `backend/app/services/psychrometrics.py`
```python
"""Psychrometric helpers shared by the body model and the environment model."""

from __future__ import annotations

from math import exp

from app.services.model_parameters import get_parameter_value as _param


MAGNUS_A = _param("magnus_a")
MAGNUS_B = _param("magnus_b")
MAGNUS_C = _param("magnus_c")


def saturation_vapor_pressure_kpa(temperature_c: float) -> float:
    return MAGNUS_A * exp(MAGNUS_B * temperature_c / (temperature_c + MAGNUS_C))


def vapor_pressure_kpa(temperature_c: float, relative_humidity_percent: float) -> float:
    return relative_humidity_percent / 100.0 * saturation_vapor_pressure_kpa(temperature_c)
```

### File: `backend/app/services/reproducibility.py`
```python
"""Helpers for regression ("golden") cases.

Two layers of protection
------------------------
1. Numeric comparison (``compare_regression_payloads``, unchanged): skin/core
   temperatures against the stored fixture, with ``temperature_atol``.
2. Parameter fingerprint (new): a SHA-256 over *every constant that can
   change a result*. Compared exactly, before any number is looked at.

Why the second layer
    A 1 % tweak to one constant can move the 2-hour Dubai case by less than
    ``temperature_atol`` and slip through layer 1. Layer 2 has no tolerance,
    and on mismatch names the key that changed and its old/new value.

What is NOT in the fingerprint
    Library versions. Upgrading numpy in CI must not fail the golden test;
    if the upgrade really changes results, layer 1 still catches it.

Hard limit
    Only constants registered in ``model_parameters.MODEL_PARAMETERS``,
    or ``EnvironmentAssumptions`` are
    visible here. A literal left inside ``two_node.py`` is invisible.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping
from typing import Any

import numpy as np

from app.schemas.environment import EnvironmentAssumptions
from app.schemas.simulation import WeatherSimulationResponse

# Import the module, not the names, so tests can monkeypatch
# ``mp.MODEL_PARAMETERS`` and prove the fingerprint reacts.
from app.services import model_parameters as mp

# Bump only when the *shape* of the snapshot changes (new section, renamed
# key). A changed constant value must bump ``mp.MODEL_PARAMETER_SET_VERSION``.
SNAPSHOT_SCHEMA_VERSION = 1


# --------------------------------------------------------------------------
# Canonical serialisation
# --------------------------------------------------------------------------


def _to_builtin(value: Any) -> Any:
    """Recursively convert numpy / tuple values to JSON builtins.

    Must be idempotent and must agree with a JSON round-trip, because the
    fixture stores the snapshot as JSON and we re-hash it on load.
    """
    if isinstance(value, Mapping):
        return {str(k): _to_builtin(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_to_builtin(v) for v in value]
    if isinstance(value, np.ndarray):
        return [_to_builtin(v) for v in value.tolist()]
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, float) and (value != value or value in (float("inf"), float("-inf"))):
        raise ValueError("Non-finite float in parameter snapshot")
    return value


def canonical_json(obj: Any) -> str:
    """Stable JSON: sorted keys, no whitespace, ASCII only, NaN forbidden."""
    return json.dumps(
        _to_builtin(obj),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    )


# --------------------------------------------------------------------------
# Snapshot and fingerprint
# --------------------------------------------------------------------------


def parameter_snapshot(
    environment_assumptions: EnvironmentAssumptions | None,
) -> dict[str, Any]:
    """Every constant that can change a simulation result, as one dict.

    ``environment_assumptions`` is recorded exactly as given. ``None`` is a
    legitimate value for the constant-environment endpoint; do not
    substitute defaults here.
    """
    return {
        "schema_version": SNAPSHOT_SCHEMA_VERSION,
        "model_parameter_set_version": mp.MODEL_PARAMETER_SET_VERSION,
        "model_parameter_set_sha256": mp.model_parameter_set_sha256(),
        "model_parameters": {
            p.name: p.value for p in mp.list_model_parameters()
        },
        "environment_assumptions": (
            None
            if environment_assumptions is None
            else environment_assumptions.model_dump(mode="json")
        ),
    }


def fingerprint_of_snapshot(snapshot: Mapping[str, Any]) -> str:
    """SHA-256 hex digest of a snapshot (fresh or loaded from a fixture)."""
    return hashlib.sha256(canonical_json(snapshot).encode("utf-8")).hexdigest()


def parameter_fingerprint(
    environment_assumptions: EnvironmentAssumptions | None,
) -> str:
    """Convenience: fingerprint of the *current* constants."""
    return fingerprint_of_snapshot(parameter_snapshot(environment_assumptions))


# --------------------------------------------------------------------------
# Diagnostics
# --------------------------------------------------------------------------


def flatten_snapshot(
    snapshot: Mapping[str, Any],
    prefix: str = "",
) -> dict[str, Any]:
    """``{"a": {"b": 1}}`` -> ``{"a.b": 1}``. Lists stay as leaf values."""
    flat: dict[str, Any] = {}
    for key, value in snapshot.items():
        path = f"{prefix}.{key}" if prefix else str(key)
        if isinstance(value, Mapping):
            flat.update(flatten_snapshot(value, path))
        else:
            flat[path] = value
    return flat


def diff_snapshots(
    expected: Mapping[str, Any],
    actual: Mapping[str, Any],
) -> list[str]:
    """One line per differing key: ``section.key: old -> new``."""
    flat_expected = flatten_snapshot(_to_builtin(expected))
    flat_actual = flatten_snapshot(_to_builtin(actual))

    lines: list[str] = []
    for key in sorted(set(flat_expected) | set(flat_actual)):
        if key not in flat_actual:
            lines.append(f"parameter_snapshot.{key}: REMOVED (was {flat_expected[key]!r})")
        elif key not in flat_expected:
            lines.append(f"parameter_snapshot.{key}: ADDED ({flat_actual[key]!r})")
        elif flat_expected[key] != flat_actual[key]:
            lines.append(
                f"parameter_snapshot.{key}: {flat_expected[key]!r} -> {flat_actual[key]!r}"
            )
    return lines


_REGEN_HINT = (
    "If intentional: bump MODEL_PARAMETER_SET_VERSION in "
    "app/services/model_parameters.py, record the change in "
    "docs/acceptance/<stage>/golden-refresh.md, then regenerate the fixture "
    "(UPDATE_GOLDEN=1 python -m pytest tests/test_golden_dubai_2h.py). "
    "Otherwise revert the constant."
)

def _compare_parameter_fingerprint(
    expected: Mapping[str, Any],
    actual: Mapping[str, Any],
) -> list[str]:
    """Exact fingerprint check, plus a key-level explanation on mismatch."""
    expected_fp = expected.get("parameter_fingerprint")
    expected_snapshot = expected.get("parameter_snapshot")
    actual_fp = actual["parameter_fingerprint"]
    actual_snapshot = actual["parameter_snapshot"]

    # Old fixture predating this check: fail loudly rather than skip.
    if expected_fp is None or expected_snapshot is None:
        return [
            "parameter_fingerprint: fixture has no fingerprint/snapshot; "
            "regenerate it (UPDATE_GOLDEN=1 python -m pytest tests/test_golden_dubai_2h.py)"
        ]

    # Fixture integrity: catches hand-edited snapshots with a stale hash.
    recomputed = fingerprint_of_snapshot(expected_snapshot)
    if recomputed != expected_fp:
        return [
            "parameter_fingerprint: fixture is internally inconsistent "
            f"(stored {expected_fp}, snapshot hashes to {recomputed}); regenerate it"
        ]

    if expected_fp == actual_fp:
        return []

    lines = [
        f"parameter_fingerprint: {expected_fp} != {actual_fp} "
        "(model constants changed since the fixture was recorded)"
    ]
    changes = diff_snapshots(expected_snapshot, actual_snapshot)
    lines.extend(changes or ["parameter_snapshot: no key-level difference found; check canonical_json"])
    lines.append(_REGEN_HINT)
    return lines


# --------------------------------------------------------------------------
# Golden payload
# --------------------------------------------------------------------------


def summarize_result_for_regression(
    result: WeatherSimulationResponse,
    *,
    environment_assumptions: EnvironmentAssumptions | None = None,  # <-- PR-2: if the
) -> dict[str, Any]:
    """Reduce a result to the numeric fields we want to keep stable,
    plus a snapshot/fingerprint of the constants that produced them."""
    assumptions = (
        environment_assumptions
        if environment_assumptions is not None
        else getattr(result, "environment_assumptions", None)
    )
    if assumptions is None:
        # Results stored before Stage 2 were produced by the Stage 1 rules.
        from app.schemas.environment import LEGACY_PRESET, preset_assumptions
        assumptions = preset_assumptions(LEGACY_PRESET)
        
    snapshot = parameter_snapshot(assumptions)
    return {
        "model_version": result.model_version,
        "parameter_fingerprint": fingerprint_of_snapshot(snapshot),
        "parameter_snapshot": snapshot,
        "city": result.city,
        "duration_minutes": result.duration_minutes,
        "summary": result.summary.model_dump(),
        "weather": {
            "point_count": len(result.weather.points),
            "payload_sha256": result.weather.source.payload_sha256,
            "quality": (
                result.weather.source.quality.model_dump(mode="json")
                if result.weather.source.quality
                else None
            ),
        },
        "control": [
            {
                "minute": p.minute,
                "core_temperature_c": p.core_temperature_c,
                "skin_temperature_c": p.skin_temperature_c,
            }
            for p in result.control.time_series
        ],
        "radiative_cooling": [
            {
                "minute": p.minute,
                "core_temperature_c": p.core_temperature_c,
                "skin_temperature_c": p.skin_temperature_c,
            }
            for p in result.radiative_cooling.time_series
        ],
    }

def compare_regression_payloads(
    expected: dict[str, Any],
    actual: dict[str, Any],
    *,
    temperature_atol: float = 1e-6,
) -> list[str]:
    """Return a list of human-readable differences (empty means identical).

    The fingerprint is checked first and exactly. Numeric checks still run
    afterwards so the report shows whether the constant change actually
    moved any temperature.
    """
    differences: list[str] = []

    # --- new: exact constants check -------------------------------------
    differences.extend(_compare_parameter_fingerprint(expected, actual))

    # --- unchanged from here ---------------------------------------------
    for key in ("model_version", "city", "duration_minutes"):
        if expected.get(key) != actual.get(key):
            differences.append(f"{key}: {expected.get(key)!r} != {actual.get(key)!r}")

    for key, value in expected["summary"].items():
        actual_value = actual["summary"].get(key)
        if isinstance(value, (int, float)):
            if actual_value is None or abs(value - actual_value) > temperature_atol:
                differences.append(f"summary.{key}: {value} != {actual_value}")
        else:
            if value != actual_value:
                differences.append(f"summary.{key}: {value!r} != {actual_value!r}")

    for scenario in ("control", "radiative_cooling"):
        expected_points = expected[scenario]
        actual_points = actual[scenario]

        if len(expected_points) != len(actual_points):
            differences.append(
                f"{scenario}: {len(expected_points)} vs {len(actual_points)} points"
            )
            continue

        for index, (e, a) in enumerate(zip(expected_points, actual_points)):
            for field in ("minute", "core_temperature_c", "skin_temperature_c"):
                if abs(e[field] - a[field]) > temperature_atol:
                    differences.append(
                        f"{scenario}[{index}].{field}: {e[field]} != {a[field]}"
                    )

    if expected["weather"]["payload_sha256"] != actual["weather"]["payload_sha256"]:
        differences.append("weather payload sha256 differs")

    return differences
```

### File: `backend/app/services/result_export.py`
```python
import csv
import io
import json
from typing import Any

from app.schemas.simulation import WeatherSimulationResponse


CSV_HEADERS = [
    "minute",
    "control_core_temperature_c",
    "control_skin_temperature_c",
    "rc_core_temperature_c",
    "rc_skin_temperature_c",
    "control_convection_w_m2",
    "rc_convection_w_m2",
    "control_longwave_w_m2",
    "rc_longwave_w_m2",
    "control_evaporation_w_m2",
    "rc_evaporation_w_m2",
    "control_absorbed_solar_w_m2",
    "rc_absorbed_solar_w_m2",
    # Stage 2 / 3 diagnostics; blank for results stored before they existed.
    "control_maximum_evaporation_w_m2",
    "rc_maximum_evaporation_w_m2",
    "control_skin_wettedness",
    "rc_skin_wettedness",
    "control_clothing_surface_temperature_c",
    "rc_clothing_surface_temperature_c",
    # Stage 5
    "control_solar_incident_w_m2",
    "rc_solar_incident_w_m2",
    # Stage 10
    "control_longwave_window_w_m2",
    "rc_longwave_window_w_m2",
    # Stage 11 (boundary conditions; identical for both garments)
    "sky_temperature_c",
    "surround_temperature_c",
]


def _optional(point: Any, name: str) -> Any:
    value = getattr(point, name, None)
    return "" if value is None else value


def export_result_csv(result: WeatherSimulationResponse) -> str:
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(CSV_HEADERS)

    for control, rc in zip(
        result.control.time_series,
        result.radiative_cooling.time_series,
        strict=True,
    ):
        writer.writerow(
            [
                control.minute,
                control.core_temperature_c,
                control.skin_temperature_c,
                rc.core_temperature_c,
                rc.skin_temperature_c,
                control.convection_w_m2,
                rc.convection_w_m2,
                control.longwave_radiation_w_m2,
                rc.longwave_radiation_w_m2,
                control.evaporation_w_m2,
                rc.evaporation_w_m2,
                control.absorbed_solar_w_m2,
                rc.absorbed_solar_w_m2,
                _optional(control, "maximum_evaporation_w_m2"),
                _optional(rc, "maximum_evaporation_w_m2"),
                _optional(control, "skin_wettedness"),
                _optional(rc, "skin_wettedness"),
                _optional(control, "clothing_surface_temperature_c"),
                _optional(rc, "clothing_surface_temperature_c"),
                _optional(control, "solar_incident_w_m2"),
                _optional(rc, "solar_incident_w_m2"),
                _optional(control, "longwave_window_w_m2"),
                _optional(rc, "longwave_window_w_m2"),
                _optional(rc, "sky_temperature_c"),
                _optional(rc, "surround_temperature_c"),
            ]
        )

    return output.getvalue()


def export_result_json(result: WeatherSimulationResponse) -> str:
    return json.dumps(result.model_dump(mode="json"), ensure_ascii=False, indent=2)
```

### File: `backend/app/services/result_storage.py`
```python
import gzip
import json
from pathlib import Path

from app.core.config import settings
from app.schemas.simulation import (
    WeatherSimulationResponse,
)


def save_simulation_result(
    job_id: str,
    result: WeatherSimulationResponse,
) -> Path:
    result_directory = (
        settings.result_directory
    )
    result_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    final_path = (
        result_directory
        / f"{job_id}.json.gz"
    )

    temporary_path = (
        result_directory
        / f"{job_id}.tmp.json.gz"
    )

    with gzip.open(
        temporary_path,
        mode="wt",
        encoding="utf-8",
    ) as file:
        json.dump(
            result.model_dump(mode="json"),
            file,
            ensure_ascii=False,
            separators=(",", ":"),
        )

    temporary_path.replace(final_path)

    return final_path


def load_simulation_result(
    result_path: str,
) -> WeatherSimulationResponse:
    path = Path(result_path)

    if not path.exists():
        raise FileNotFoundError(
            f"The result file does not exist:{path}"
        )

    with gzip.open(
        path,
        mode="rt",
        encoding="utf-8",
    ) as file:
        payload = json.load(file)

    return WeatherSimulationResponse.model_validate(
        payload
    )
```

### File: `backend/app/services/scenario_summary.py`
```python
"""Shared control-vs-RC summary (Stage 6, PR-1a).

Every entry point that compares a control garment with a radiative-cooling
garment -- fixed environment (/simulations/run), single weather run
(/simulations/run-weather, Celery job) and annual sampling
(climate_adaptation) -- must build its summary here. "Average improvement"
therefore has exactly one meaning: the time-weighted (trapezoidal) mean of
the paired temperature difference over the exposure window.

The two series are paired point by point and must share the same time axis;
equal length alone is not sufficient.
"""

from __future__ import annotations

from dataclasses import dataclass

from app.schemas.simulation import ScenarioResult, SimulationSummary
from app.services.exposure_statistics import time_weighted_mean


AVERAGING_METHOD = "time_weighted_trapezoid"
PAIRING_TOLERANCE_MINUTES = 1e-6


class ScenarioPairingError(ValueError):
    """Control and RC time series do not share the same time axis."""


@dataclass(frozen=True)
class PairedImprovement:
    """control - rc at every shared output time (positive = RC is cooler)."""

    minutes: list[float]
    skin_c: list[float]
    core_c: list[float]

    @property
    def average_skin_c(self) -> float:
        return time_weighted_mean(self.minutes, self.skin_c)

    @property
    def average_core_c(self) -> float:
        return time_weighted_mean(self.minutes, self.core_c)

    @property
    def final_skin_c(self) -> float:
        return self.skin_c[-1]

    @property
    def final_core_c(self) -> float:
        return self.core_c[-1]

    @property
    def maximum_skin_c(self) -> float:
        return max(self.skin_c)


def pair_scenarios(control: ScenarioResult, rc: ScenarioResult) -> PairedImprovement:
    control_points = control.time_series
    rc_points = rc.time_series

    if not control_points or not rc_points:
        raise ScenarioPairingError("Cannot summarise an empty time series")

    if len(control_points) != len(rc_points):
        raise ScenarioPairingError(
            f"Series length mismatch: {len(control_points)} control vs "
            f"{len(rc_points)} radiative-cooling points"
        )

    minutes: list[float] = []
    skin: list[float] = []
    core: list[float] = []

    for index, (c, r) in enumerate(zip(control_points, rc_points, strict=True)):
        if abs(c.minute - r.minute) > PAIRING_TOLERANCE_MINUTES:
            raise ScenarioPairingError(
                f"Time axis mismatch at index {index}: "
                f"control minute {c.minute} vs RC minute {r.minute}"
            )
        minutes.append(c.minute)
        skin.append(c.skin_temperature_c - r.skin_temperature_c)
        core.append(c.core_temperature_c - r.core_temperature_c)

    return PairedImprovement(minutes=minutes, skin_c=skin, core_c=core)


def build_simulation_summary(
    control: ScenarioResult,
    rc: ScenarioResult,
) -> SimulationSummary:
    paired = pair_scenarios(control, rc)

    return SimulationSummary(
        final_skin_temperature_improvement_c=round(paired.final_skin_c, 4),
        final_core_temperature_improvement_c=round(paired.final_core_c, 4),
        average_skin_temperature_improvement_c=round(paired.average_skin_c, 4),
        averaging_method=AVERAGING_METHOD,
    )
```

### File: `backend/app/services/solar.py`
```python
"""Shortwave irradiance incident on the clothed body (Stage 5, ADR 0006).

Per unit DuBois area:

    I_body = f_p * DNI                          direct beam on the projected area
           + 0.5 * f_eff * F_sky * DHI          sky diffuse, upper hemisphere
           + 0.5 * f_eff * rho_g * GHI          ground reflected, lower hemisphere

This is the geometry of ASHRAE 55-2020 Normative Appendix C (Arens et al.
2015) with the measured diffuse component instead of the 0.2 * I_dir estimate,
the sky view factor limiting the sky-diffuse term, and f_bes = 1 (no shading).

Legacy path: when the beam/diffuse split is not available the whole GHI is
treated as beam on the projected area (Stage 0-4 geometry). Fixed-environment
requests that do not send DNI/DHI therefore keep their incident irradiance;
only the surface-balance treatment (ADR 0005) changes their results.

Partition at the textile (ADR 0005):
    absorbed by textile   = (1 - rho_sol - tau_sol) * I_body   -> surface balance
    transmitted to skin   = tau_sol * I_body                   -> skin node
"""

from __future__ import annotations

from dataclasses import dataclass

from app.schemas.simulation import EnvironmentInput, MaterialInput
from app.services.model_parameters import get_parameter_value


HEMISPHERE_FRACTION = get_parameter_value("diffuse_hemisphere_fraction")


@dataclass(frozen=True)
class SolarLoad:
    incident_w_m2: float
    direct_w_m2: float
    sky_diffuse_w_m2: float
    ground_reflected_w_m2: float
    absorbed_by_textile_w_m2: float
    transmitted_to_skin_w_m2: float
    split_available: bool

    @property
    def entering_system_w_m2(self) -> float:
        """Solar energy that ends up in the clothing-body system."""
        return self.absorbed_by_textile_w_m2 + self.transmitted_to_skin_w_m2


def solar_absorptance(material: MaterialInput) -> float:
    value = 1.0 - material.solar_reflectance - material.solar_transmittance
    return min(1.0, max(0.0, value))


def solar_load(
    environment: EnvironmentInput,
    material: MaterialInput,
    radiation_area_ratio: float,
) -> SolarLoad:
    ghi = max(0.0, environment.solar_radiation_w_m2)
    projected = material.projected_solar_area_factor

    dni = environment.direct_normal_irradiance_w_m2
    dhi = environment.diffuse_horizontal_irradiance_w_m2

    if dni is None or dhi is None:
        direct = projected * ghi
        sky_diffuse = 0.0
        ground_reflected = 0.0
        split_available = False
    else:
        direct = projected * max(0.0, dni)
        sky_diffuse = (
            HEMISPHERE_FRACTION
            * radiation_area_ratio
            * environment.sky_view_factor
            * max(0.0, dhi)
        )
        ground_reflected = (
            HEMISPHERE_FRACTION
            * radiation_area_ratio
            * environment.ground_albedo
            * ghi
        )
        split_available = True

    incident = direct + sky_diffuse + ground_reflected

    return SolarLoad(
        incident_w_m2=incident,
        direct_w_m2=direct,
        sky_diffuse_w_m2=sky_diffuse,
        ground_reflected_w_m2=ground_reflected,
        absorbed_by_textile_w_m2=solar_absorptance(material) * incident,
        transmitted_to_skin_w_m2=material.solar_transmittance * incident,
        split_available=split_available,
    )
```

### File: `backend/app/services/spectral_summary.py`
```python
"""Planck-weighted band averages of uploaded IR spectra (Stage 10)."""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

from app.schemas.material import SpectrumBandSummary
from app.services.planck import (
    WINDOW_LOWER_UM,
    WINDOW_UPPER_UM,
    blackbody_fraction,
    planck_shape,
)

GRID_POINTS = 401  # numerical: dense sub-grid so the Planck weight is well resolved


@dataclass(frozen=True)
class BandIntegral:
    weighted: float   # integral eps * B
    weight: float     # integral B
    coverage: float   # covered blackbody fraction / target blackbody fraction

    @property
    def average(self) -> float | None:
        return self.weighted / self.weight if self.weight > 0 else None


def band_integral(
    wavelengths: np.ndarray,
    values: np.ndarray,
    lower_um: float,
    upper_um: float,
    temperature_k: float,
) -> BandIntegral:
    lo = max(lower_um, float(wavelengths[0]))
    hi = min(upper_um, float(wavelengths[-1]))
    target = blackbody_fraction(upper_um * temperature_k) - blackbody_fraction(
        lower_um * temperature_k
    )

    if hi <= lo or target <= 0:
        return BandIntegral(0.0, 0.0, 0.0)

    inside = wavelengths[(wavelengths > lo) & (wavelengths < hi)]
    grid = np.unique(np.concatenate([np.linspace(lo, hi, GRID_POINTS), inside]))
    eps = np.interp(grid, wavelengths, values)
    weight = np.asarray([planck_shape(float(w), temperature_k) for w in grid])

    covered = blackbody_fraction(hi * temperature_k) - blackbody_fraction(lo * temperature_k)

    return BandIntegral(
        weighted=float(np.trapezoid(eps * weight, grid)),
        weight=float(np.trapezoid(weight, grid)),
        coverage=covered / target,
    )


def summarize_ir_spectrum(
    points: list[dict],
    *,
    spectrum_type: str,
    temperature_k: float,
) -> SpectrumBandSummary:
    wavelengths = np.asarray([p["wavelength_um"] for p in points], dtype=float)
    values = np.asarray([p["value"] for p in points], dtype=float)

    window = band_integral(wavelengths, values, WINDOW_LOWER_UM, WINDOW_UPPER_UM, temperature_k)
    measured = band_integral(wavelengths, values, 0.0, math.inf, temperature_k)

    outside_weight = measured.weight - window.weight
    outside = (
        (measured.weighted - window.weighted) / outside_weight
        if outside_weight > 1e-12 * max(measured.weight, 1e-300)
        else None
    )

    def rounded(value: float | None) -> float | None:
        return None if value is None else round(value, 5)

    return SpectrumBandSummary(
        spectrum_type=spectrum_type,
        temperature_k=temperature_k,
        window_lower_um=WINDOW_LOWER_UM,
        window_upper_um=WINDOW_UPPER_UM,
        measured_lower_um=float(wavelengths[0]),
        measured_upper_um=float(wavelengths[-1]),
        window_average=rounded(window.average),
        window_coverage=round(window.coverage, 5),
        broadband_average=rounded(measured.average),
        broadband_coverage=round(measured.coverage, 5),
        outside_window_average=rounded(outside),
    )
```

### File: `backend/app/services/spectrum_parser.py`
```python
from __future__ import annotations

import csv
import hashlib
import io
import math
from dataclasses import dataclass


MAX_SPECTRUM_FILE_SIZE = 2 * 1024 * 1024
MAX_SPECTRUM_POINTS = 20_000


@dataclass
class ParsedSpectrum:
    points: list[dict[str, float]]
    checksum_sha256: str
    minimum_wavelength_um: float
    maximum_wavelength_um: float


def _normalize_header(value: str) -> str:
    return (
        value.strip()
        .lower()
        .replace(" ", "_")
        .replace("µ", "u")
        .replace("μ", "u")
    )


def parse_spectrum_csv(
    file_bytes: bytes,
) -> ParsedSpectrum:
    if not file_bytes:
        raise ValueError("Uploaded file is empty")

    if len(file_bytes) > MAX_SPECTRUM_FILE_SIZE:
        raise ValueError(
            "Spectrum CSV cannot exceed 2 MB"
        )

    try:
        text = file_bytes.decode("utf-8-sig")
    except UnicodeDecodeError as error:
        raise ValueError(
            "CSV must use UTF-8 encoding"
        ) from error

    reader = csv.DictReader(
        io.StringIO(text)
    )

    if not reader.fieldnames:
        raise ValueError("CSV is missing headers")

    header_map = {
        _normalize_header(name): name
        for name in reader.fieldnames
    }

    wavelength_candidates = [
        "wavelength_um",
        "wavelength",
        "lambda_um",
    ]

    value_candidates = [
        "value",
        "reflectance",
        "emissivity",
        "transmittance",
    ]

    wavelength_column = next(
        (
            header_map[name]
            for name in wavelength_candidates
            if name in header_map
        ),
        None,
    )

    value_column = next(
        (
            header_map[name]
            for name in value_candidates
            if name in header_map
        ),
        None,
    )

    if wavelength_column is None:
        raise ValueError(
            "CSV must include a 'wavelength_um' column"
        )

    if value_column is None:
        raise ValueError(
            "CSV must include a 'value' column"
        )

    points: list[dict[str, float]] = []

    for row_number, row in enumerate(
        reader,
        start=2,
    ):
        try:
            wavelength = float(
                row[wavelength_column]
            )
            value = float(
                row[value_column]
            )
        except (
            TypeError,
            ValueError,
            KeyError,
        ) as error:
            raise ValueError(
                f"Row {row_number} contains invalid values"
            ) from error

        if not math.isfinite(wavelength):
            raise ValueError(
                f"Row {row_number} wavelength is not a finite value"
            )

        if not math.isfinite(value):
            raise ValueError(
                f"Row {row_number} spectrum value is not a finite value"
            )

        if wavelength <= 0:
            raise ValueError(
                f"Row {row_number} wavelength must be positive"
            )

        if not 0 <= value <= 1:
            raise ValueError(
                f"Row {row_number} spectrum value must be between 0 and 1"
            )

        points.append(
            {
                "wavelength_um": wavelength,
                "value": value,
            }
        )

        if len(points) > MAX_SPECTRUM_POINTS:
            raise ValueError(
                f"Row {row_number} spectrum points cannot exceed 20000"
            )

    if len(points) < 2:
        raise ValueError("Spectrum file must contain at least two data points")

    wavelengths = [point["wavelength_um"] for point in points]

    for position, (previous, current) in enumerate(zip(wavelengths, wavelengths[1:]), start=3):
        if current <= previous:
            raise ValueError(
                f"Row {position}: wavelengths must be strictly increasing and unique"
            )

    return ParsedSpectrum(
        points=points,
        checksum_sha256=hashlib.sha256(
            file_bytes
        ).hexdigest(),
        minimum_wavelength_um=wavelengths[0],
        maximum_wavelength_um=wavelengths[-1],
    )
```

### File: `backend/app/services/stored_requests.py`
```python
"""Load request_json persisted by earlier stages (ADR 0009).

Requests stored before Stage 2 have no ``environment_assumptions`` key. Since
Stage 12 the schema default is the physical environment, so validating those
payloads directly would silently re-interpret them. Every load from the
database goes through ``load_stored_request``.
"""

from __future__ import annotations

from typing import Any, TypeVar

from pydantic import BaseModel

from app.schemas.environment import LEGACY_PRESET, preset_assumptions

ModelT = TypeVar("ModelT", bound=BaseModel)


def with_stored_environment(payload: dict[str, Any] | None) -> dict[str, Any]:
    data = dict(payload or {})
    if data.get("environment_assumptions") is None:
        data["environment_assumptions"] = preset_assumptions(LEGACY_PRESET).model_dump(mode="json")
    return data


def load_stored_request(model: type[ModelT], payload: dict[str, Any] | None) -> ModelT:
    return model.model_validate(with_stored_environment(payload))
```

### File: `backend/app/services/two_node.py`
```python
"""Two-node transient human thermal model.

Stage 5 changes (ADR 0005, ADR 0006)
------------------------------------
* Solar radiation absorbed by the textile is a source term in the clothing
  surface balance; the share reaching the skin is an outcome of that balance.
  ``MaterialInput.absorbed_solar_to_body_fraction`` is ignored.
* Solar transmitted through the textile is deposited on the skin node.
* Incident shortwave uses the beam/diffuse split when available
  (``services.solar``); ``PersonInput.position`` selects A_r/A_D.

Retained from Stage 3: body-mass heat capacities (ADR 0001), Gagge 1986
controllers (ADR 0002), explicit clothing surface temperature (ADR 0003).
Every numeric constant is bound from ``model_parameters``.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass
from math import exp, sqrt

import numpy as np
from scipy.integrate import solve_ivp

from app.schemas.environment import EnvironmentAssumptions
from app.schemas.simulation import (
    BodyPosition,
    BodyThermalSummary,
    ClothingSummary,
    EnergyDiagnostics,
    EnvironmentInput,
    MaterialInput,
    PersonInput,
    ScenarioResult,
    TimeSeriesPoint,
)
from app.schemas.weather import WeatherTimeSeries
from app.services.body import BodyHeatCapacities, body_heat_capacities
from app.services.clothing import (
    ClothingResistances,
    assumptions_applied,
    maximum_evaporation_w_m2,
    resolve_clothing,
)
from app.services.model_parameters import get_parameter_value as _param
from app.services.solar import solar_load
from app.services.weather_interpolation import WeatherInterpolator
from app.services.longwave import (
    LongwaveOptics,
    RadiantField,
    longwave_notes,
    net_exchange_k4,
    radiant_field,
    resolve_longwave_optics,
    PreparedZone, 
    prepare_longwave_zones, 
    surroundings_fourth_power_k4, 
    zone_notes, 
    zoned_exchange_k4
)

from app.services.psychrometrics import saturation_vapor_pressure_kpa

# Version of the physics engine written into every response. Bump together
# with MODEL_PARAMETER_SET_VERSION whenever results change.
MODEL_VERSION = "0.10.0"  # Stage 12: two-zone garment longwave (ADR 0010)

# Bound once at import. The registry is the single source of truth.
SIGMA = _param("stefan_boltzmann_constant")
NATURAL_CONVECTION_MINIMUM = _param("natural_convection_minimum_coefficient")
FORCED_CONVECTION_COEFFICIENT = _param("forced_convection_coefficient")
SKIN_EMISSIVITY = _param("skin_emissivity")
RADIATION_AREA_RATIO_STANDING = _param("effective_radiation_area_ratio_standing")
RADIATION_AREA_RATIO_SITTING = _param("effective_radiation_area_ratio_sitting")
SKIN_MASS_FRACTION = _param("skin_mass_fraction")
CORE_SETPOINT = _param("core_setpoint_temperature")
SKIN_SETPOINT = _param("skin_setpoint_temperature")
SWEATING_GAIN_BODY = _param("sweating_gain_body")
SWEATING_SKIN_SIGNAL_SCALE = _param("sweating_skin_signal_scale")
MAXIMUM_SWEAT_RATE = _param("maximum_sweat_rate")
LATENT_HEAT_PER_GRAM_HOUR = _param("latent_heat_of_sweat")
SKIN_DIFFUSION_FRACTION = _param("skin_diffusion_fraction")
W_MAX_CLOTHED_COEFFICIENT = _param("maximum_wettedness_clothed_coefficient")
W_MAX_CLOTHED_EXPONENT = _param("maximum_wettedness_clothed_exponent")
W_MAX_NUDE_COEFFICIENT = _param("maximum_wettedness_nude_coefficient")
W_MAX_NUDE_EXPONENT = _param("maximum_wettedness_nude_exponent")
SKIN_BLOOD_FLOW_BASAL = _param("skin_blood_flow_basal")
VASODILATION_GAIN = _param("vasodilation_gain")
VASOCONSTRICTION_GAIN = _param("vasoconstriction_gain")
SKIN_BLOOD_FLOW_MINIMUM = _param("skin_blood_flow_minimum")
SKIN_BLOOD_FLOW_MAXIMUM = _param("skin_blood_flow_maximum")
CORE_SKIN_CONDUCTANCE_BASAL = _param("core_skin_conductance_basal")
BLOOD_HEAT_CAPACITY_PER_FLOW = _param("blood_heat_capacity_per_flow")
SHIVERING_COEFFICIENT = _param("shivering_coefficient")
METABOLIC_RATE_PER_MET = _param("metabolic_rate_per_met")
RESPIRATORY_LATENT_COEFFICIENT = _param("respiratory_latent_coefficient")
RESPIRATORY_REFERENCE_PRESSURE = _param("respiratory_reference_vapor_pressure")
RESPIRATORY_SENSIBLE_COEFFICIENT = _param("respiratory_sensible_coefficient")
EXHALED_AIR_TEMPERATURE = _param("exhaled_air_temperature")
FALLBACK_SKY_OFFSET = _param("fallback_sky_temperature_offset")


KELVIN_OFFSET = 273.15
BODY_SETPOINT = (
    SKIN_MASS_FRACTION * SKIN_SETPOINT + (1.0 - SKIN_MASS_FRACTION) * CORE_SETPOINT
)

# Numerical (not physical) settings.
SOLVER_METHOD = "RK45"
SOLVER_RTOL = 1e-6
SOLVER_ATOL = 1e-8
SOLVER_MAX_STEP_SECONDS = 60.0
SURFACE_TEMPERATURE_TOLERANCE_K = 1e-5
SURFACE_TEMPERATURE_MAX_ITERATIONS = 30
NUDE_RESISTANCE_THRESHOLD_M2K_W = 1e-6
# Gagge's w_max correlations were fitted for v >= 0.1 m/s.
MINIMUM_WIND_FOR_WETTEDNESS_M_S = 0.1

EnvironmentAt = Callable[[float], EnvironmentInput]


@dataclass
class HeatFluxes:
    convection: float
    longwave_radiation: float
    longwave_transmitted: float
    evaporation: float
    maximum_evaporation: float
    skin_wettedness: float
    maximum_skin_wettedness: float
    solar_incident: float
    solar_absorbed_by_textile: float
    solar_transmitted: float
    absorbed_solar: float  # solar entering the clothing-body system
    core_to_skin: float
    respiration: float
    metabolism: float
    skin_blood_flow: float
    clothing_surface_temperature_c: float
    radiation_area_ratio: float
    # Stage 10 (selective emitters only)
    longwave_window: float | None = None
    sky_window_emissivity: float | None = None

    @property
    def net_body_gain(self) -> float:
        """Whole-body net heat gain; core_to_skin is internal and cancels."""
        return (
            self.metabolism
            - self.respiration
            + self.absorbed_solar
            - self.convection
            - self.longwave_radiation
            - self.evaporation
        )


def clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(value, upper))


def effective_radiation_area_ratio(position: BodyPosition) -> float:
    """A_r / A_D for the given posture (ADR 0006)."""
    if position == "sitting":
        return RADIATION_AREA_RATIO_SITTING
    return RADIATION_AREA_RATIO_STANDING



def convection_coefficient_w_m2k(wind_speed_m_s: float) -> float:
    return max(
        NATURAL_CONVECTION_MINIMUM,
        FORCED_CONVECTION_COEFFICIENT * sqrt(max(wind_speed_m_s, 0.0)),
    )


def environment_radiant_fourth_power_k4(environment: EnvironmentInput) -> float:
    """F_sky * T_sky^4 + (1 - F_sky) * T_mrt^4 in K^4."""
    sky_temperature_c = environment.sky_temperature_c
    if sky_temperature_c is None:
        sky_temperature_c = environment.air_temperature_c - FALLBACK_SKY_OFFSET

    sky_k = sky_temperature_c + KELVIN_OFFSET
    radiant_k = environment.mean_radiant_temperature_c + KELVIN_OFFSET
    f = environment.sky_view_factor

    return f * sky_k**4 + (1.0 - f) * radiant_k**4

def clothing_surface_temperature_c(
    *,
    skin_temperature_c: float,
    air_temperature_c: float,
    environment_fourth_k4: float,
    clothing: ClothingResistances,
    convection_coefficient: float,
    emissivity: float,
    radiation_area_ratio: float,
    absorbed_solar_w_m2: float = 0.0,
    optics: LongwaveOptics | None = None,
    field: RadiantField | None = None,
    zones: Sequence[PreparedZone] | None = None,
) -> float:
    """Solve the clothing surface balance (ADR 0003 + 0005 + 0007).

    Gray path: (A_r/A_D) eps sigma (T_cl^4 - T_env^4). Selective path: the
    same balance with window and out-of-window bands. Both emission terms
    increase with T_cl, so the residual stays strictly decreasing.
    """
    if clothing.dry_resistance_m2k_w < NUDE_RESISTANCE_THRESHOLD_M2K_W:
        return skin_temperature_c

    selective = optics is not None and optics.selective and field is not None

    resistance = clothing.dry_resistance_m2k_w
    area_factor = clothing.area_factor
    skin_k = skin_temperature_c + KELVIN_OFFSET
    air_k = air_temperature_c + KELVIN_OFFSET
    gray_factor = radiation_area_ratio * emissivity * SIGMA

    t = skin_k

    for _ in range(SURFACE_TEMPERATURE_MAX_ITERATIONS):
        if zones is not None:
            net, net_slope, _ = zoned_exchange_k4(tuple(zones), t)
            emission = radiation_area_ratio * SIGMA * net
            emission_slope = radiation_area_ratio * SIGMA * net_slope
        elif selective:
            net, net_slope, _ = net_exchange_k4(optics, field, t)
            emission = radiation_area_ratio * SIGMA * net
            emission_slope = radiation_area_ratio * SIGMA * net_slope
        else:
            emission = gray_factor * (t**4 - environment_fourth_k4)
            emission_slope = 4.0 * gray_factor * t**3

        residual = (
            (skin_k - t) / resistance
            + absorbed_solar_w_m2
            - area_factor * (convection_coefficient * (t - air_k) + emission)
        )
        derivative = -1.0 / resistance - area_factor * (
            convection_coefficient + emission_slope
        )
        step = residual / derivative
        t -= step

        if abs(step) < SURFACE_TEMPERATURE_TOLERANCE_K:
            return t - KELVIN_OFFSET

    raise RuntimeError(
        "Clothing surface temperature iteration did not converge "
        f"(T_sk = {skin_temperature_c:.3f} C, T_a = {air_temperature_c:.3f} C, "
        f"S_abs = {absorbed_solar_w_m2:.1f} W/m^2)"
    )

def maximum_skin_wettedness(wind_speed_m_s: float, clothing: ClothingResistances) -> float:
    v = max(wind_speed_m_s, MINIMUM_WIND_FOR_WETTEDNESS_M_S)
    if clothing.is_nude:
        w_max = W_MAX_NUDE_COEFFICIENT * v**W_MAX_NUDE_EXPONENT
    else:
        w_max = W_MAX_CLOTHED_COEFFICIENT * v**W_MAX_CLOTHED_EXPONENT
    return clamp(w_max, SKIN_DIFFUSION_FRACTION, 1.0)


def calculate_fluxes(
    core_temperature_c: float,
    skin_temperature_c: float,
    environment: EnvironmentInput,
    person: PersonInput,
    material: MaterialInput,
    clothing: ClothingResistances | None = None,
    optics: LongwaveOptics | None = None,
) -> HeatFluxes:
    if clothing is None:
        clothing = resolve_clothing(material)
    if optics is None:
        optics = resolve_longwave_optics(material)

    air_temperature_c = environment.air_temperature_c
    area_ratio = effective_radiation_area_ratio(person.position)

    # --- thermoregulatory signals (Gagge 1986) ------------------------------
    warm_skin = max(skin_temperature_c - SKIN_SETPOINT, 0.0)
    cold_skin = max(SKIN_SETPOINT - skin_temperature_c, 0.0)
    warm_core = max(core_temperature_c - CORE_SETPOINT, 0.0)
    cold_core = max(CORE_SETPOINT - core_temperature_c, 0.0)

    body_temperature_c = (
        SKIN_MASS_FRACTION * skin_temperature_c
        + (1.0 - SKIN_MASS_FRACTION) * core_temperature_c
    )
    warm_body = max(body_temperature_c - BODY_SETPOINT, 0.0)

    # --- solar (ADR 0005 / 0006) --------------------------------------------
    solar = solar_load(environment, material, area_ratio)

    # --- dry heat: clothing surface balance with the solar source -----------
    convection_coefficient = convection_coefficient_w_m2k(environment.wind_speed_m_s)

    zones = prepare_longwave_zones(material, environment, optics)
    if zones is not None:
        field = None
        environment_fourth = surroundings_fourth_power_k4(environment)
    elif optics.selective:
        field = radiant_field(environment)
        environment_fourth = field.total_k4
    else:
        field = None
        environment_fourth = environment_radiant_fourth_power_k4(environment)

    surface_c = clothing_surface_temperature_c(
        skin_temperature_c=skin_temperature_c,
        air_temperature_c=air_temperature_c,
        environment_fourth_k4=environment_fourth,
        clothing=clothing,
        convection_coefficient=convection_coefficient,
        emissivity=material.infrared_emissivity,
        radiation_area_ratio=area_ratio,
        absorbed_solar_w_m2=solar.absorbed_by_textile_w_m2,
        optics=optics,
        field=field,
        zones=zones,
    )
    surface_k = surface_c + KELVIN_OFFSET
    skin_k = skin_temperature_c + KELVIN_OFFSET

    convection = clothing.area_factor * convection_coefficient * (
        surface_c - air_temperature_c
    )

    longwave_window: float | None = None
    if zones is not None:
        net, _, net_window = zoned_exchange_k4(zones, surface_k)
        scale = clothing.area_factor * area_ratio * SIGMA
        longwave_surface = scale * net
        longwave_window = None if net_window is None else scale * net_window
    elif field is not None:
        net, _, net_window = net_exchange_k4(optics, field, surface_k)
        longwave_surface = clothing.area_factor * area_ratio * SIGMA * net
        longwave_window = clothing.area_factor * area_ratio * SIGMA * net_window
    else:
        longwave_surface = (
            clothing.area_factor
            * area_ratio
            * material.infrared_emissivity
            * SIGMA
            * (surface_k**4 - environment_fourth)
        )

    # Skin emission transmitted through an IR-transparent textile sees the
    # body-average field (zone views are area-consistent, ADR 0010).
    longwave_transmitted = (
        area_ratio
        * clothing.infrared_transmittance
        * SKIN_EMISSIVITY
        * SIGMA
        * (skin_k**4 - environment_fourth)
    )

    longwave_radiation = longwave_surface + longwave_transmitted

    # --- evaporation --------------------------------------------------------
    ambient_vapor_pressure_kpa = (
        environment.relative_humidity_percent / 100.0
        * saturation_vapor_pressure_kpa(air_temperature_c)
    )
    skin_vapor_pressure_kpa = saturation_vapor_pressure_kpa(skin_temperature_c)

    maximum_evaporation = maximum_evaporation_w_m2(
        clothing,
        convection_coefficient,
        skin_vapor_pressure_kpa,
        ambient_vapor_pressure_kpa,
    )

    regulatory_sweating_g_h_m2 = min(
        SWEATING_GAIN_BODY * warm_body * exp(warm_skin / SWEATING_SKIN_SIGNAL_SCALE),
        MAXIMUM_SWEAT_RATE,
    )
    regulatory_evaporation = regulatory_sweating_g_h_m2 * LATENT_HEAT_PER_GRAM_HOUR

    w_max = maximum_skin_wettedness(environment.wind_speed_m_s, clothing)

    if maximum_evaporation <= 0.0:
        skin_wettedness = w_max
        evaporation = 0.0
    else:
        sweat_ratio = regulatory_evaporation / maximum_evaporation
        skin_wettedness = min(
            SKIN_DIFFUSION_FRACTION + (1.0 - SKIN_DIFFUSION_FRACTION) * sweat_ratio,
            w_max,
        )
        evaporation = skin_wettedness * maximum_evaporation

    # --- core <-> skin ------------------------------------------------------
    skin_blood_flow = clamp(
        (SKIN_BLOOD_FLOW_BASAL + VASODILATION_GAIN * warm_core)
        / (1.0 + VASOCONSTRICTION_GAIN * cold_skin),
        SKIN_BLOOD_FLOW_MINIMUM,
        SKIN_BLOOD_FLOW_MAXIMUM,
    )

    core_skin_conductance = (
        CORE_SKIN_CONDUCTANCE_BASAL + BLOOD_HEAT_CAPACITY_PER_FLOW * skin_blood_flow
    )

    core_to_skin = core_skin_conductance * (core_temperature_c - skin_temperature_c)

    # --- metabolism and respiration -----------------------------------------
    metabolism = (
        person.met * METABOLIC_RATE_PER_MET
        + SHIVERING_COEFFICIENT * cold_skin * cold_core
    )

    respiration_latent = max(
        0.0,
        RESPIRATORY_LATENT_COEFFICIENT
        * metabolism
        * (RESPIRATORY_REFERENCE_PRESSURE - ambient_vapor_pressure_kpa * 1000.0),
    )

    respiration_sensible = (
        RESPIRATORY_SENSIBLE_COEFFICIENT
        * metabolism
        * (EXHALED_AIR_TEMPERATURE - air_temperature_c)
    )

    respiration = max(0.0, respiration_latent + respiration_sensible)

    return HeatFluxes(
        convection=convection,
        longwave_radiation=longwave_radiation,
        longwave_transmitted=longwave_transmitted,
        evaporation=evaporation,
        maximum_evaporation=maximum_evaporation,
        skin_wettedness=skin_wettedness,
        maximum_skin_wettedness=w_max,
        solar_incident=solar.incident_w_m2,
        solar_absorbed_by_textile=solar.absorbed_by_textile_w_m2,
        solar_transmitted=solar.transmitted_to_skin_w_m2,
        absorbed_solar=solar.entering_system_w_m2,
        core_to_skin=core_to_skin,
        respiration=respiration,
        metabolism=metabolism,
        skin_blood_flow=skin_blood_flow,
        clothing_surface_temperature_c=surface_c,
        radiation_area_ratio=area_ratio,
        longwave_window=longwave_window,
        sky_window_emissivity=None if field is None else field.sky_window_emissivity,
    )


def _output_times(duration_seconds: float, interval_seconds: float) -> np.ndarray:
    times = np.arange(0.0, duration_seconds + 0.1, interval_seconds)
    if times[-1] < duration_seconds:
        times = np.append(times, duration_seconds)
    return times


def _energy_diagnostics(
    times_seconds: np.ndarray,
    core_temperatures: np.ndarray,
    skin_temperatures: np.ndarray,
    net_heat_fluxes: np.ndarray,
    solver_function_evaluations: int,
    capacities: BodyHeatCapacities,
) -> EnergyDiagnostics:
    integrated_net_heat = float(np.trapezoid(net_heat_fluxes, times_seconds))

    stored_energy_change = float(
        capacities.core_j_m2k * (core_temperatures[-1] - core_temperatures[0])
        + capacities.skin_j_m2k * (skin_temperatures[-1] - skin_temperatures[0])
    )

    residual = stored_energy_change - integrated_net_heat
    denominator = max(abs(stored_energy_change), abs(integrated_net_heat), 1.0)

    def max_step(values: np.ndarray) -> float:
        return float(np.max(np.abs(np.diff(values)))) if len(values) > 1 else 0.0

    return EnergyDiagnostics(
        stored_energy_change_j_m2=round(stored_energy_change, 4),
        integrated_net_heat_j_m2=round(integrated_net_heat, 4),
        energy_residual_j_m2=round(residual, 4),
        normalized_residual_percent=round(abs(residual) / denominator * 100.0, 6),
        maximum_core_step_c=round(max_step(core_temperatures), 6),
        maximum_skin_step_c=round(max_step(skin_temperatures), 6),
        solver_function_evaluations=int(solver_function_evaluations),
        diagnostic_interval_seconds=DIAGNOSTIC_INTERVAL_SECONDS,
    )


def _integrate(
    *,
    duration_minutes: int,
    output_interval_minutes: int,
    environment_at: EnvironmentAt,
    person: PersonInput,
    material: MaterialInput,
    failure_label: str,
) -> ScenarioResult:
    clothing = resolve_clothing(material)
    optics = resolve_longwave_optics(material)
    capacities = body_heat_capacities(person)
    area_ratio = effective_radiation_area_ratio(person.position)
    initial_environment = environment_at(0.0)
    solar_split_available = initial_environment.has_solar_split
    initial_zones = prepare_longwave_zones(material, initial_environment, optics)

    duration_seconds = duration_minutes * 60.0
    output_times = _output_times(duration_seconds, output_interval_minutes * 60.0)
    eval_times = _diagnostic_times(duration_seconds, output_times)

    def derivatives(time_seconds: float, state: np.ndarray) -> list[float]:
        fluxes = calculate_fluxes(
            core_temperature_c=float(state[0]),
            skin_temperature_c=float(state[1]),
            environment=environment_at(float(time_seconds)),
            person=person,
            material=material,
            clothing=clothing,
            optics=optics,
        )

        core_storage = fluxes.metabolism - fluxes.respiration - fluxes.core_to_skin
        # absorbed_solar = textile absorption (routed through the surface
        # balance, which already raised convection/longwave) + transmission.
        skin_storage = (
            fluxes.core_to_skin
            + fluxes.absorbed_solar
            - fluxes.convection
            - fluxes.longwave_radiation
            - fluxes.evaporation
        )

        return [
            core_storage / capacities.core_j_m2k,
            skin_storage / capacities.skin_j_m2k,
        ]
        
    solution = solve_ivp(
        fun=derivatives,
        t_span=(0.0, duration_seconds),
        y0=[person.initial_core_temperature_c, person.initial_skin_temperature_c],
        t_eval=eval_times,
        method=SOLVER_METHOD,
        rtol=SOLVER_RTOL,
        atol=SOLVER_ATOL,
        max_step=SOLVER_MAX_STEP_SECONDS,
    )

    if not solution.success:
        raise RuntimeError(f"{failure_label}: {solution.message}")

    times = np.asarray(solution.t, dtype=float)
    core_array = np.asarray(solution.y[0], dtype=float)
    skin_array = np.asarray(solution.y[1], dtype=float)
    is_output = np.isin(times, output_times)

    time_series: list[TimeSeriesPoint] = []
    net_heat: list[float] = []

    for time_seconds, core_c, skin_c, emit in zip(times, core_array, skin_array, is_output, strict=True):
        environment = environment_at(float(time_seconds))
        fluxes = calculate_fluxes(
            core_temperature_c=float(core_c),
            skin_temperature_c=float(skin_c),
            environment=environment,
            person=person,
            material=material,
            clothing=clothing,
            optics=optics,
        )
        net_heat.append(fluxes.net_body_gain)

        if not emit:
            continue

        sky_c = environment.sky_temperature_c
        if sky_c is None:
            sky_c = environment.air_temperature_c - FALLBACK_SKY_OFFSET

        time_series.append(
            TimeSeriesPoint(
                minute=round(float(time_seconds) / 60.0, 4),
                core_temperature_c=round(float(core_c), 4),
                skin_temperature_c=round(float(skin_c), 4),
                convection_w_m2=round(fluxes.convection, 4),
                longwave_radiation_w_m2=round(fluxes.longwave_radiation, 4),
                evaporation_w_m2=round(fluxes.evaporation, 4),
                absorbed_solar_w_m2=round(fluxes.absorbed_solar, 4),
                core_to_skin_w_m2=round(fluxes.core_to_skin, 4),
                maximum_evaporation_w_m2=round(fluxes.maximum_evaporation, 4),
                skin_wettedness=round(fluxes.skin_wettedness, 4),
                clothing_surface_temperature_c=round(fluxes.clothing_surface_temperature_c, 4),
                skin_blood_flow_kg_h_m2=round(fluxes.skin_blood_flow, 4),
                solar_incident_w_m2=round(fluxes.solar_incident, 4),
                solar_absorbed_by_textile_w_m2=round(fluxes.solar_absorbed_by_textile, 4),
                solar_transmitted_w_m2=round(fluxes.solar_transmitted, 4),
                longwave_window_w_m2=(
                    None if fluxes.longwave_window is None else round(fluxes.longwave_window, 4)
                ),
                sky_temperature_c=round(sky_c, 4),
                surround_temperature_c=round(environment.mean_radiant_temperature_c, 4),
            )
        )

    diagnostics = _energy_diagnostics(
        times, core_array, skin_array, np.asarray(net_heat), solution.nfev, capacities
    )

    return ScenarioResult(
        material_name=material.name,
        time_series=time_series,
        final_core_temperature_c=time_series[-1].core_temperature_c,
        final_skin_temperature_c=time_series[-1].skin_temperature_c,
        peak_core_temperature_c=round(float(core_array.max()), 4),
        peak_skin_temperature_c=round(float(skin_array.max()), 4),
        diagnostics=diagnostics,
        clothing=ClothingSummary(
            dry_resistance_m2k_w=round(clothing.dry_resistance_m2k_w, 6),
            evaporative_resistance_m2pa_w=round(clothing.evaporative_resistance_m2pa_w, 4),
            evaporative_resistance_source=clothing.evaporative_resistance_source,
            infrared_transmittance=clothing.infrared_transmittance,
            clothing_area_factor=round(clothing.area_factor, 6),
            clothing_area_factor_source=clothing.area_factor_source,
            infrared_emissivity_window=round(optics.window, 6) if optics.selective else None,
            infrared_emissivity_outside_window=round(optics.outside, 6) if optics.selective else None,
            infrared_emissivity_ground_facing=material.infrared_emissivity_ground_facing,
        ),
        assumptions_applied=(
            assumptions_applied(clothing, solar_split_available=solar_split_available)
            + longwave_notes(optics) + zone_notes(initial_zones)
        ),
        body=BodyThermalSummary(
            body_mass_kg=person.body_mass_kg,
            body_surface_area_m2=person.body_surface_area_m2,
            core_heat_capacity_j_m2k=round(capacities.core_j_m2k, 2),
            skin_heat_capacity_j_m2k=round(capacities.skin_j_m2k, 2),
            position=person.position,
            effective_radiation_area_ratio=area_ratio,
        ),
    )


def simulate_material(
    duration_minutes: int,
    output_interval_minutes: int,
    environment: EnvironmentInput,
    person: PersonInput,
    material: MaterialInput,
) -> ScenarioResult:
    return _integrate(
        duration_minutes=duration_minutes,
        output_interval_minutes=output_interval_minutes,
        environment_at=lambda _time_seconds: environment,
        person=person,
        material=material,
        failure_label="Fixed-environment numerical solution failed",
    )

def simulate_material_with_interpolator(
    duration_minutes: int,
    output_interval_minutes: int,
    interpolator: WeatherInterpolator,
    person: PersonInput,
    material: MaterialInput,
) -> ScenarioResult:
    """Same physics as simulate_material_with_weather, but reuses a prebuilt
    interpolator (optimization evaluates thousands of garments per window)."""
    interpolator.ensure_covers(0.0, duration_minutes * 60.0)

    return _integrate(
        duration_minutes=duration_minutes,
        output_interval_minutes=output_interval_minutes,
        environment_at=interpolator.environment_at,
        person=person,
        material=material,
        failure_label="Weather-driven numerical solution failed",
    )

def simulate_material_with_weather(
    duration_minutes: int,
    output_interval_minutes: int,
    weather: WeatherTimeSeries,
    person: PersonInput,
    material: MaterialInput,
    assumptions: EnvironmentAssumptions | None = None,
) -> ScenarioResult:
    interpolator = WeatherInterpolator.from_series(
        weather, assumptions=assumptions or EnvironmentAssumptions()
    )
    return simulate_material_with_interpolator(
        duration_minutes, output_interval_minutes, interpolator, person, material
    )
    
# Numerical (not physical) settings.
DIAGNOSTIC_INTERVAL_SECONDS = 60.0  # energy audit grid, independent of output interval


def _diagnostic_times(duration_seconds: float, output_times: np.ndarray) -> np.ndarray:
    """Union of a fixed 60 s audit grid and the requested output times.

    solve_ivp chooses its steps independently of t_eval, so evaluating on a
    denser grid does not change the trajectory at the output times; it only
    makes the energy-balance integral independent of output_interval_minutes.
    """
    fine = np.arange(0.0, duration_seconds + 0.1, DIAGNOSTIC_INTERVAL_SECONDS)
    if fine[-1] < duration_seconds:
        fine = np.append(fine, duration_seconds)
    return np.unique(np.concatenate([fine, output_times]))
```

### File: `backend/app/services/weather.py`
```python
from __future__ import annotations

import hashlib
import json
import logging
from datetime import (
    date,
    datetime,
    timedelta,
    timezone,
)
from datetime import timezone as dt_timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import httpx

from app.core.cities import CityConfig
from app.schemas.weather import (
    CityResponse,
    WeatherPoint,
    WeatherSourceMetadata,
    WeatherTimeSeries,
)

import asyncio
import os
from uuid import uuid4

from redis.asyncio import Redis

from redis.exceptions import RedisError  # add near the redis import

from app.core.config import BACKEND_DIRECTORY, settings   # 合併原本的 settings import

from app.services.weather_quality import (
    DEFAULT_STEP_SECONDS,
    WeatherInsufficientCoverageError,
    ensure_window_covered,
    normalize_timeline,
    payload_sha256,
)

OPEN_METEO_ARCHIVE_URL = (
    "https://archive-api.open-meteo.com/v1/archive"
)

HOURLY_VARIABLES = [
    "temperature_2m",
    "relative_humidity_2m",
    "wind_speed_10m",
    "shortwave_radiation",
    "direct_radiation",
    "diffuse_radiation",
    "direct_normal_irradiance",
]
# Stage 11: requested only when the environment assumptions need them, so the
# default request (and therefore the cache key and payload hash) is unchanged.
OPTIONAL_HOURLY_VARIABLES: dict[str, str] = {
    "cloud_cover": "cloud_cover_percent",
    "soil_temperature_0_to_7cm": "soil_temperature_c",
}

CACHE_DIRECTORY = BACKEND_DIRECTORY / "data" / "cache" / "weather"


def city_to_response(
    city: CityConfig,
) -> CityResponse:
    return CityResponse(
        id=city.id,
        name=city.name,
        country=city.country,
        latitude=city.latitude,
        longitude=city.longitude,
        elevation_m=city.elevation_m,
        timezone=city.timezone,
        climate_type=city.climate_type,
    )


def normalize_local_datetime(
    value: datetime,
    timezone_name: str,
) -> datetime:
    city_timezone = ZoneInfo(timezone_name)

    if value.tzinfo is None:
        return value.replace(
            tzinfo=city_timezone
        )

    return value.astimezone(city_timezone)


def validate_archive_date(
    end_time: datetime,
) -> None:
    # ERA5 通常約有五天延遲。
    latest_safe_date = (
        datetime.now(timezone.utc).date()
        - timedelta(days=5)
    )

    if end_time.date() > latest_safe_date:
        raise ValueError(
            "ERA5 historical data are typically delayed by approximately "
            "five days. Please select a date no later than "
            f"{latest_safe_date.isoformat()}."
        )


def build_request_params(
    city: CityConfig,
    start_date: date,
    end_date: date,
    extra_variables: tuple[str, ...] = (),
) -> dict[str, str | float]:
    unknown = set(extra_variables) - set(OPTIONAL_HOURLY_VARIABLES)
    if unknown:
        raise ValueError(f"Unsupported weather variables: {sorted(unknown)}")

    hourly = HOURLY_VARIABLES + sorted(set(extra_variables))
    return {
        "latitude": city.latitude,
        "longitude": city.longitude,
        "elevation": city.elevation_m,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "hourly": ",".join(hourly),
        "timezone": city.timezone,
        "wind_speed_unit": "ms",
        "temperature_unit": "celsius",
        "models": "era5",
        "cell_selection": "land",
    }


def build_cache_path(
    params: dict[str, str | float],
) -> Path:
    serialized = json.dumps(
        params,
        sort_keys=True,
        ensure_ascii=True,
    )

    digest = hashlib.sha256(
        serialized.encode("utf-8")
    ).hexdigest()[:20]

    return CACHE_DIRECTORY / f"{digest}.json"

def read_cached_payload(
    cache_path: Path,
) -> dict | None:
    if not cache_path.exists():
        return None

    try:
        return json.loads(
            cache_path.read_text(
                encoding="utf-8"
            )
        )
    except (
        OSError,
        json.JSONDecodeError,
    ):
        return None


def write_cached_payload_atomic(
    cache_path: Path,
    payload: dict,
) -> None:
    temporary_path = cache_path.with_name(
        f"{cache_path.name}."
        f"{uuid4().hex}.tmp"
    )

    temporary_path.write_text(
        json.dumps(
            payload,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    os.replace(
        temporary_path,
        cache_path,
    )


def build_weather_lock_name(
    cache_path: Path,
) -> str:
    return (
        "weather-download-lock:"
        f"{cache_path.stem}"
    )

async def request_open_meteo(
    params: dict[str, str | float],
) -> tuple[dict, bool]:
    cache_path = build_cache_path(
        params
    )

    CACHE_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )

    cached_payload = read_cached_payload(
        cache_path
    )

    if cached_payload is not None:
        return cached_payload, True

    redis_client = Redis.from_url(
        settings.weather_lock_redis_url,
        decode_responses=True,
    )

    lock = redis_client.lock(
        build_weather_lock_name(
            cache_path
        ),
        timeout=(
            settings
            .weather_lock_timeout_seconds
        ),
        blocking_timeout=(
            settings
            .weather_lock_blocking_timeout_seconds
        ),
    )

    acquired = False

    try:
        acquired = await lock.acquire()

        if not acquired:
            raise RuntimeError(
                "Timed out while waiting for "
                "the weather download lock"
            )

        cached_payload = read_cached_payload(
            cache_path
        )

        if cached_payload is not None:
            return cached_payload, True

        payload = await download_open_meteo_payload(
            params
        )

        write_cached_payload_atomic(
            cache_path,
            payload,
        )

        return payload, False

    except (RedisError, OSError):
        # Redis is unreachable or timed out. redis-py raises RedisError
        # subclasses (NOT the builtin ConnectionError); OSError covers socket
        # level failures. Weather must stay available without the lock.
        cached_payload = read_cached_payload(cache_path)
        if cached_payload is not None:
            return cached_payload, True
        payload = await download_open_meteo_payload(params)
        write_cached_payload_atomic(cache_path, payload)
        return payload, False

    finally:
        if acquired:
            try:
                await lock.release()
            except Exception:
                pass

        await redis_client.aclose()

def require_hourly_array(
    hourly: dict,
    name: str,
    expected_length: int,
) -> list:
    values = hourly.get(name)

    if values is None:
        raise RuntimeError(
            f"Open-Meteo response is missing variable: {name}"
        )

    if len(values) != expected_length:
        raise RuntimeError(
            f"Open-Meteo variable {name} has inconsistent length"
        )

    return values


def safe_float(
    value: object,
    variable_name: str,
    index: int,
) -> float:
    if value is None:
        raise RuntimeError(
            f"{variable_name} is missing at index {index}"
        )

    return float(value)

logger = logging.getLogger(__name__)


def to_utc(value: datetime) -> datetime:
    if value.tzinfo is None:
        raise ValueError("to_utc requires an aware datetime")
    return value.astimezone(dt_timezone.utc)


def payload_timezone(payload: dict, city: CityConfig):
    """Fixed offset Open-Meteo applied when rendering local time strings.

    Open-Meteo returns one utc_offset_seconds per response and renders every
    hourly time string with it. Re-applying the same fixed offset is the exact
    inverse; ZoneInfo(city.timezone) is not, because on a DST fall-back day it
    maps two different instants to the same wall-clock string.
    """
    offset = payload.get("utc_offset_seconds")
    if offset is None:
        logger.warning(
            "Open-Meteo payload lacks utc_offset_seconds; falling back to "
            "ZoneInfo(%s). DST days may be mis-parsed.", city.timezone,
        )
        return ZoneInfo(city.timezone)
    return dt_timezone(timedelta(seconds=int(offset)))

def parse_weather_points(
    payload: dict,
    city: CityConfig,
) -> list[WeatherPoint]:
    hourly = payload.get("hourly")

    if not hourly:
        raise RuntimeError(
            "Open-Meteo response is missing hourly data"
        )

    times = hourly.get("time", [])
    expected_length = len(times)

    if expected_length == 0:
        raise RuntimeError(
            "Open-Meteo response is missing weather time points"
        )

    temperature = require_hourly_array(
        hourly,
        "temperature_2m",
        expected_length,
    )
    humidity = require_hourly_array(
        hourly,
        "relative_humidity_2m",
        expected_length,
    )
    wind_speed = require_hourly_array(
        hourly,
        "wind_speed_10m",
        expected_length,
    )
    ghi = require_hourly_array(
        hourly,
        "shortwave_radiation",
        expected_length,
    )
    direct = require_hourly_array(
        hourly,
        "direct_radiation",
        expected_length,
    )
    diffuse = require_hourly_array(
        hourly,
        "diffuse_radiation",
        expected_length,
    )
    dni = require_hourly_array(
        hourly,
        "direct_normal_irradiance",
        expected_length,
    )

    optional_series: dict[str, list] = {}
    for api_name, field_name in OPTIONAL_HOURLY_VARIABLES.items():
        values = hourly.get(api_name)
        if values is None:
            continue
        if len(values) != expected_length:
            raise RuntimeError(f"Open-Meteo variable {api_name} has inconsistent length")
        optional_series[field_name] = values
        
    tz = payload_timezone(payload, city)
    points: list[WeatherPoint] = []

    for index, timestamp_text in enumerate(times):
        # Open-Meteo 在指定 timezone 時返回當地時間，
        # 字符串本身通常不附帶 UTC offset。
        timestamp = datetime.fromisoformat(timestamp_text).replace(tzinfo=tz)

        points.append(
            WeatherPoint(
                timestamp=timestamp,
                air_temperature_c=safe_float(
                    temperature[index],
                    "temperature_2m",
                    index,
                ),
                relative_humidity_percent=safe_float(
                    humidity[index],
                    "relative_humidity_2m",
                    index,
                ),
                wind_speed_m_s=safe_float(
                    wind_speed[index],
                    "wind_speed_10m",
                    index,
                ),
                ghi_w_m2=max(
                    0.0,
                    safe_float(
                        ghi[index],
                        "shortwave_radiation",
                        index,
                    ),
                ),
                direct_radiation_w_m2=max(
                    0.0,
                    safe_float(
                        direct[index],
                        "direct_radiation",
                        index,
                    ),
                ),
                diffuse_radiation_w_m2=max(
                    0.0,
                    safe_float(
                        diffuse[index],
                        "diffuse_radiation",
                        index,
                    ),
                ),
                dni_w_m2=max(
                    0.0,
                    safe_float(
                        dni[index],
                        "direct_normal_irradiance",
                        index,
                    ),
                ),
                **{
                    field: (None if values[index] is None else float(values[index]))
                    for field, values in optional_series.items()
                },
            )
        )

    return points


async def get_historical_weather(
    city: CityConfig,
    start_time_local: datetime,
    duration_minutes: int,
    extra_variables: tuple[str, ...] = (),
) -> WeatherTimeSeries:
    start_time = normalize_local_datetime(start_time_local, city.timezone)
    end_time = (to_utc(start_time) + timedelta(minutes=duration_minutes)).astimezone(
        ZoneInfo(city.timezone)
    )
    return await get_historical_weather_range(
        city=city,
        start_time_local=start_time,
        end_time_local=end_time,
        padding_hours=1,
        extra_variables=extra_variables,
    )

async def get_historical_weather_range(
    *,
    city: CityConfig,
    start_time_local: datetime,
    end_time_local: datetime,
    padding_hours: int = 1,
    require_window_coverage: bool = True,
    extra_variables: tuple[str, ...] = (),
) -> WeatherTimeSeries:
    """Fetch, normalise and validate an ERA5 series for a local time range.

    ``require_window_coverage=True`` (default) rejects any response that does
    not fully bracket ``[start, end]`` or that has a gap inside it. Callers
    that prefetch a long range and slice it later (monthly analysis) pass
    ``False``; each slice then enforces coverage for its own window.
    """
    start_time = normalize_local_datetime(
        start_time_local,
        city.timezone,
    )

    end_time = normalize_local_datetime(
        end_time_local,
        city.timezone,
    )

    if end_time <= start_time:
        raise ValueError(
            "end_time_local must be after start_time_local"
        )

    validate_archive_date(end_time)

    query_start = start_time - timedelta(hours=padding_hours)
    query_end = end_time + timedelta(hours=padding_hours)

    params = build_request_params(
        city=city,
        start_date=query_start.date(),
        end_date=query_end.date(),
        extra_variables=extra_variables,
    )
    
    payload, from_cache = await request_open_meteo(params)

    raw_points = parse_weather_points(payload, city)

    cleaned_points, quality = normalize_timeline(
        raw_points,
        expected_step_seconds=DEFAULT_STEP_SECONDS,  # hourly data was requested; never infer
    )
    
    if require_window_coverage:
        ensure_window_covered(
            cleaned_points,
            window_start=start_time,
            window_end=end_time,
            step_seconds=quality.expected_step_seconds,
            label=f"Open-Meteo weather for {city.name}",
        )

    selected_points = [
        point
        for point in cleaned_points
        if query_start <= point.timestamp <= query_end
    ]

    if not require_window_coverage and len(selected_points) < 2:
        raise WeatherInsufficientCoverageError(
            f"Open-Meteo returned fewer than two weather points for "
            f"{city.name} between {query_start.isoformat()} and "
            f"{query_end.isoformat()}"
        )

    return WeatherTimeSeries(
        city=city_to_response(city),
        requested_start_time=start_time,
        requested_end_time=end_time,
        points=selected_points,
        source=WeatherSourceMetadata(
            provider="Open-Meteo",
            dataset="Historical Weather API",
            model="ERA5",
            latitude=float(payload.get("latitude", city.latitude)),
            longitude=float(payload.get("longitude", city.longitude)),
            elevation_m=float(payload.get("elevation", city.elevation_m)),
            timezone=payload.get("timezone", city.timezone),
            downloaded_at=datetime.now(timezone.utc),
            from_cache=from_cache,
            attribution=(
                "Weather data by Open-Meteo.com; "
                "underlying reanalysis: ERA5."
            ),
            payload_sha256=payload_sha256(payload),
            quality=quality,
        ),
    )

def slice_weather_time_series(
    *,
    weather: WeatherTimeSeries,
    start_time_local: datetime,
    duration_minutes: int,
    padding_hours: int = 1,
) -> WeatherTimeSeries:
    """Cut a padded sub-series and enforce coverage of the exposure window."""
    start_time = normalize_local_datetime(
        start_time_local,
        weather.city.timezone,
    )

    end_time = (to_utc(start_time) + timedelta(minutes=duration_minutes)).astimezone(
        ZoneInfo(weather.city.timezone)
    )
    
    step_seconds = (
        weather.source.quality.expected_step_seconds
        if weather.source.quality is not None
        else DEFAULT_STEP_SECONDS
    )
    # Validate against the FULL prefetched series first, so that a window
    # outside the data reports "does not cover" rather than "fewer than two".
    ensure_window_covered(
        weather.points,
        window_start=start_time,
        window_end=end_time,
        step_seconds=step_seconds,
        label="Prefetched weather",
    )

    query_start = start_time - timedelta(hours=padding_hours)
    query_end = end_time + timedelta(hours=padding_hours)

    selected_points = [
        point
        for point in weather.points
        if query_start <= point.timestamp <= query_end
    ]

    return WeatherTimeSeries(
        city=weather.city,
        requested_start_time=start_time,
        requested_end_time=end_time,
        points=selected_points,
        source=weather.source,
    )

async def download_open_meteo_payload(
    params: dict[str, str | float],
) -> dict:
    async with httpx.AsyncClient(
        timeout=httpx.Timeout(60.0),
    ) as client:
        response = await client.get(
            OPEN_METEO_ARCHIVE_URL,
            params=params,
        )

    if response.status_code != 200:
        try:
            error_body = response.json()
            reason = error_body.get(
                "reason",
                response.text,
            )
        except ValueError:
            reason = response.text

        raise RuntimeError(
            "Open-Meteo request failed: "
            f"HTTP {response.status_code}: "
            f"{reason}"
        )

    return response.json()
```

### File: `backend/app/services/weather_interpolation.py`
```python
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from app.schemas.environment import EnvironmentAssumptions
from app.schemas.simulation import EnvironmentInput
from app.schemas.weather import WeatherTimeSeries
from app.services.environment_model import (
    CLOUD_COVER,
    SOIL_TEMPERATURE,
    derive_environment,
    required_weather_variables,
)
from app.services.weather_quality import (
    WeatherInsufficientCoverageError,
    WeatherMissingVariableError,
)


BOUNDS_TOLERANCE_SECONDS = 1e-6

_POINT_FIELD = {CLOUD_COVER: "cloud_cover_percent", SOIL_TEMPERATURE: "soil_temperature_c"}


class InterpolationOutOfRangeError(WeatherInsufficientCoverageError):
    code = "WEATHER_INTERPOLATION_OUT_OF_RANGE"


@dataclass
class WeatherInterpolator:
    relative_seconds: np.ndarray
    temperatures: np.ndarray
    humidities: np.ndarray
    wind_speeds: np.ndarray
    ghi_values: np.ndarray
    assumptions: EnvironmentAssumptions = field(default_factory=EnvironmentAssumptions)
    dni_values: np.ndarray | None = None
    dhi_values: np.ndarray | None = None
    # Stage 11 (instantaneous variables, linear interpolation)
    cloud_values: np.ndarray | None = None
    soil_values: np.ndarray | None = None

    def __post_init__(self) -> None:
        arrays = [self.relative_seconds, self.temperatures, self.humidities, self.wind_speeds, self.ghi_values]
        arrays += [a for a in (self.dni_values, self.dhi_values, self.cloud_values, self.soil_values) if a is not None]

        if len({len(a) for a in arrays}) != 1:
            raise ValueError("All interpolation arrays must have the same length")
        if len(self.relative_seconds) < 2:
            raise WeatherInsufficientCoverageError("Interpolation requires at least two weather points")
        if not np.all(np.diff(self.relative_seconds) > 0):
            raise ValueError("relative_seconds must be strictly increasing")

        required = required_weather_variables(self.assumptions)
        if CLOUD_COVER in required and self.cloud_values is None:
            raise WeatherMissingVariableError("cloud_cover is required but was not provided",
                                              context={"variable": CLOUD_COVER})
        if SOIL_TEMPERATURE in required and self.soil_values is None:
            raise WeatherMissingVariableError("soil temperature is required but was not provided",
                                              context={"variable": SOIL_TEMPERATURE})

    @property
    def t_min(self) -> float:
        return float(self.relative_seconds[0])

    @property
    def t_max(self) -> float:
        return float(self.relative_seconds[-1])

    def ensure_covers(self, start_seconds: float, end_seconds: float) -> None:
        if (
            start_seconds < self.t_min - BOUNDS_TOLERANCE_SECONDS
            or end_seconds > self.t_max + BOUNDS_TOLERANCE_SECONDS
        ):
            raise WeatherInsufficientCoverageError(
                "Weather data cover "
                f"[{self.t_min:.0f} s, {self.t_max:.0f} s] relative to the "
                "requested start, but the simulation requires "
                f"[{start_seconds:.0f} s, {end_seconds:.0f} s]",
                context={
                    "available_start_seconds": f"{self.t_min:.0f}",
                    "available_end_seconds": f"{self.t_max:.0f}",
                    "required_start_seconds": f"{start_seconds:.0f}",
                    "required_end_seconds": f"{end_seconds:.0f}",
                },
            )

    @staticmethod
    def _optional_array(weather: WeatherTimeSeries, variable: str, required: bool) -> np.ndarray | None:
        name = _POINT_FIELD[variable]
        values = [getattr(p, name) for p in weather.points]
        if all(v is None for v in values):
            return None
        if any(v is None for v in values):
            if required:
                raise WeatherMissingVariableError(
                    f"{variable} has missing values inside the simulated window",
                    context={"variable": variable},
                )
            return None
        return np.asarray(values, dtype=float)

    @classmethod
    def from_series(
        cls,
        weather: WeatherTimeSeries,
        *,
        check_requested_window: bool = True,
        assumptions: EnvironmentAssumptions | None = None,
    ) -> "WeatherInterpolator":
        assumptions = assumptions or EnvironmentAssumptions()
        required = required_weather_variables(assumptions)
        start_time = weather.requested_start_time

        interpolator = cls(
            relative_seconds=np.asarray(
                [p.timestamp.timestamp() - start_time.timestamp() for p in weather.points], dtype=float
            ),
            temperatures=np.asarray([p.air_temperature_c for p in weather.points], dtype=float),
            humidities=np.asarray([p.relative_humidity_percent for p in weather.points], dtype=float),
            wind_speeds=np.asarray([p.wind_speed_m_s for p in weather.points], dtype=float),
            ghi_values=np.asarray([p.ghi_w_m2 for p in weather.points], dtype=float),
            assumptions=assumptions,
            dni_values=np.asarray([p.dni_w_m2 for p in weather.points], dtype=float),
            dhi_values=np.asarray([p.diffuse_radiation_w_m2 for p in weather.points], dtype=float),
            cloud_values=cls._optional_array(weather, CLOUD_COVER, CLOUD_COVER in required),
            soil_values=cls._optional_array(weather, SOIL_TEMPERATURE, SOIL_TEMPERATURE in required),
        )

        if check_requested_window:
            interpolator.ensure_covers(
                0.0, weather.requested_end_time.timestamp() - start_time.timestamp()
            )
        return interpolator

    def _check_bounds(self, elapsed_seconds: float) -> None:
        if (
            elapsed_seconds < self.t_min - BOUNDS_TOLERANCE_SECONDS
            or elapsed_seconds > self.t_max + BOUNDS_TOLERANCE_SECONDS
        ):
            raise InterpolationOutOfRangeError(
                f"Requested time {elapsed_seconds:.3f} s is outside the "
                f"weather data range [{self.t_min:.0f} s, {self.t_max:.0f} s]",
                context={
                    "requested_seconds": f"{elapsed_seconds:.3f}",
                    "available_start_seconds": f"{self.t_min:.0f}",
                    "available_end_seconds": f"{self.t_max:.0f}",
                },
            )

    def _interpolate(self, values: np.ndarray, elapsed_seconds: float) -> float:
        return float(np.interp(elapsed_seconds, self.relative_seconds, values))

    def _interpolate_optional(self, values: np.ndarray | None, elapsed_seconds: float) -> float | None:
        return None if values is None else self._interpolate(values, elapsed_seconds)

    def _interpolate_radiation(self, values: np.ndarray, elapsed_seconds: float) -> float:
        if self.assumptions.radiation_time_convention == "instantaneous_linear":
            return self._interpolate(values, elapsed_seconds)
        index = int(np.searchsorted(self.relative_seconds, elapsed_seconds, side="left"))
        index = min(max(index, 0), len(values) - 1)
        return float(values[index])

    def environment_at(self, elapsed_seconds: float) -> EnvironmentInput:
        self._check_bounds(elapsed_seconds)
        return derive_environment(
            air_temperature_c=self._interpolate(self.temperatures, elapsed_seconds),
            relative_humidity_percent=self._interpolate(self.humidities, elapsed_seconds),
            wind_speed_m_s=self._interpolate(self.wind_speeds, elapsed_seconds),
            ghi_w_m2=self._interpolate_radiation(self.ghi_values, elapsed_seconds),
            direct_normal_irradiance_w_m2=(
                None if self.dni_values is None
                else self._interpolate_radiation(self.dni_values, elapsed_seconds)
            ),
            diffuse_horizontal_irradiance_w_m2=(
                None if self.dhi_values is None
                else self._interpolate_radiation(self.dhi_values, elapsed_seconds)
            ),
            cloud_cover_percent=self._interpolate_optional(self.cloud_values, elapsed_seconds),
            soil_temperature_c=self._interpolate_optional(self.soil_values, elapsed_seconds),
            assumptions=self.assumptions,
        )
```

### File: `backend/app/services/weather_quality.py`
```python
"""Weather timeline validation (Stage 1, PR-1).

Every weather series that reaches the thermal model must pass through
``normalize_timeline`` (sort / de-duplicate / detect gaps). The exposure
window that is actually simulated must additionally pass
``ensure_window_covered``, which rejects any series that does not fully
bracket the window or that has a missing step inside it.

Design decisions
----------------
* Errors subclass ``ValueError`` so the existing API handlers map them to
  HTTP 422 without changes. Each error carries a stable ``code`` string.
* No interpolation across missing hours is performed silently. A gap inside
  the exposure window is always an error.
* Timestamps must be timezone-aware. Naive timestamps are rejected rather
  than guessed.
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from collections.abc import Sequence
from datetime import datetime, timedelta

from app.schemas.weather import (
    WeatherGap,
    WeatherPoint,
    WeatherQualityReport,
)


DEFAULT_STEP_SECONDS = 3600
STEP_TOLERANCE_FRACTION = 0.001


class WeatherDataError(ValueError):
    """Base class for weather-data problems that invalidate a simulation."""

    code: str = "WEATHER_DATA_ERROR"

    def __init__(
        self,
        message: str,
        *,
        context: dict[str, str] | None = None,
    ) -> None:
        super().__init__(message)
        self.context: dict[str, str] = dict(context or {})

    def to_detail(self) -> dict[str, str]:
        """Structured payload for HTTP error responses."""
        return {
            "code": self.code,
            "message": str(self),
            **self.context,
        }


class WeatherNaiveTimestampError(WeatherDataError):
    code = "WEATHER_NAIVE_TIMESTAMP"


class WeatherDuplicateConflictError(WeatherDataError):
    code = "WEATHER_DUPLICATE_CONFLICT"


class WeatherGapInWindowError(WeatherDataError):
    code = "WEATHER_GAP_IN_WINDOW"


class WeatherInsufficientCoverageError(WeatherDataError):
    code = "WEATHER_INSUFFICIENT_COVERAGE"


def payload_sha256(payload: dict) -> str:
    """Deterministic hash of a provider payload for reproducibility records."""
    serialized = json.dumps(
        payload,
        sort_keys=True,
        ensure_ascii=True,
        separators=(",", ":"),
        default=str,
    )
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def infer_step_seconds(timestamps: Sequence[datetime]) -> int:
    """Return the most common positive spacing, defaulting to one hour."""
    if len(timestamps) < 2:
        return DEFAULT_STEP_SECONDS

    diffs = Counter(
        int((later - earlier).total_seconds())
        for earlier, later in zip(timestamps, timestamps[1:])
        if later > earlier
    )

    if not diffs:
        return DEFAULT_STEP_SECONDS

    return diffs.most_common(1)[0][0]


def _values_without_timestamp(point: WeatherPoint) -> dict:
    return point.model_dump(exclude={"timestamp"})


def detect_gaps(
    points: Sequence[WeatherPoint],
    step_seconds: int,
) -> list[WeatherGap]:
    """Find consecutive pairs spaced by more than one expected step."""
    step = timedelta(seconds=step_seconds)
    tolerance = timedelta(
        seconds=step_seconds * (1.0 + STEP_TOLERANCE_FRACTION)
    )

    gaps: list[WeatherGap] = []

    for previous, current in zip(points, points[1:]):
        delta_seconds = current.timestamp.timestamp() - previous.timestamp.timestamp()

        if delta_seconds > step_seconds * (1.0 + STEP_TOLERANCE_FRACTION):
            missing_steps = int(round(delta_seconds / step_seconds)) - 1
            gaps.append(WeatherGap(start=previous.timestamp, end=current.timestamp,
                                missing_steps=max(1, missing_steps)))
    return gaps


def normalize_timeline(
    points: Sequence[WeatherPoint],
    *,
    expected_step_seconds: int | None = None,
) -> tuple[list[WeatherPoint], WeatherQualityReport]:
    """Sort, de-duplicate and audit a raw weather timeline.

    Returns the cleaned points and a report. Raises on conditions that
    cannot be repaired safely (naive timestamps, conflicting duplicates).
    Gaps are recorded in the report but not raised here; use
    ``ensure_window_covered`` for the window that is actually simulated.
    """
    notes: list[str] = []

    if not points:
        return [], WeatherQualityReport(
            expected_step_seconds=(
                expected_step_seconds or DEFAULT_STEP_SECONDS
            ),
            point_count=0,
            notes=["input timeline is empty"],
        )

    for point in points:
        timestamp = point.timestamp

        if timestamp.tzinfo is None or timestamp.utcoffset() is None:
            raise WeatherNaiveTimestampError(
                "Weather timestamps must be timezone-aware; "
                f"received naive timestamp {timestamp.isoformat()}",
                context={"timestamp": timestamp.isoformat()},
            )

    timestamps = [point.timestamp for point in points]

    was_sorted = all(
        later >= earlier
        for earlier, later in zip(timestamps, timestamps[1:])
    )

    ordered = sorted(points, key=lambda point: point.timestamp)

    if not was_sorted:
        notes.append("input points were not sorted; sorted by timestamp")

    deduplicated: list[WeatherPoint] = []
    duplicates_removed = 0

    for point in ordered:
        if (
            deduplicated
            and deduplicated[-1].timestamp == point.timestamp
        ):
            if _values_without_timestamp(
                deduplicated[-1]
            ) == _values_without_timestamp(point):
                duplicates_removed += 1
                continue

            raise WeatherDuplicateConflictError(
                "Conflicting weather values share the same timestamp "
                f"{point.timestamp.isoformat()}",
                context={"timestamp": point.timestamp.isoformat()},
            )

        deduplicated.append(point)

    if duplicates_removed:
        notes.append(
            f"removed {duplicates_removed} identical duplicate timestamp(s)"
        )

    step_seconds = expected_step_seconds or infer_step_seconds(
        [point.timestamp for point in deduplicated]
    )

    gaps = detect_gaps(deduplicated, step_seconds)

    if gaps:
        notes.append(f"detected {len(gaps)} gap(s) in the timeline")

    report = WeatherQualityReport(
        expected_step_seconds=step_seconds,
        point_count=len(deduplicated),
        first_timestamp=deduplicated[0].timestamp,
        last_timestamp=deduplicated[-1].timestamp,
        was_sorted=was_sorted,
        duplicates_removed=duplicates_removed,
        gaps=gaps,
        notes=notes,
    )

    return deduplicated, report


def ensure_window_covered(
    points: Sequence[WeatherPoint],
    *,
    window_start: datetime,
    window_end: datetime,
    step_seconds: int = DEFAULT_STEP_SECONDS,
    label: str = "Weather series",
) -> None:
    """Raise unless ``points`` fully bracket ``[window_start, window_end]``.

    ``points`` must already be normalised (sorted, unique timestamps).
    Linear interpolation needs a point at or before the window start and a
    point at or after the window end, with no missing step in between.
    """
    if window_end <= window_start:
        raise ValueError("window_end must be after window_start")

    if len(points) < 2:
        raise WeatherInsufficientCoverageError(
            f"{label} has fewer than two points",
            context={
                "window_start": window_start.isoformat(),
                "window_end": window_end.isoformat(),
            },
        )

    first = points[0].timestamp
    last = points[-1].timestamp

    if first > window_start or last < window_end:
        raise WeatherInsufficientCoverageError(
            f"{label} does not cover the exposure window "
            f"{window_start.isoformat()} to {window_end.isoformat()}; "
            f"available data spans {first.isoformat()} to {last.isoformat()}",
            context={
                "window_start": window_start.isoformat(),
                "window_end": window_end.isoformat(),
                "available_start": first.isoformat(),
                "available_end": last.isoformat(),
            },
        )

    for gap in detect_gaps(points, step_seconds):
        overlaps_window = (
            gap.end > window_start and gap.start < window_end
        )

        if overlaps_window:
            raise WeatherGapInWindowError(
                f"{label} has a gap of {gap.missing_steps} missing step(s) "
                f"between {gap.start.isoformat()} and {gap.end.isoformat()} "
                "inside the exposure window",
                context={
                    "gap_start": gap.start.isoformat(),
                    "gap_end": gap.end.isoformat(),
                    "missing_steps": str(gap.missing_steps),
                },
            )

class WeatherMissingVariableError(WeatherDataError):
    code = "WEATHER_MISSING_VARIABLE"
```

### File: `backend/app/services/weather_simulation.py`
```python
from collections.abc import Callable

from app.core.cities import get_city
from app.schemas.simulation import (
    SimulationSummary,
    WeatherSimulationRequest,
    WeatherSimulationResponse,
)
from app.services.scenario_summary import build_simulation_summary
from app.schemas.weather import (
    WeatherTimeSeries,
)
from app.services.two_node import (
    MODEL_VERSION, simulate_material_with_weather,
)
from app.services.weather import (
    get_historical_weather,
)

from app.services.model_parameters import build_model_metadata

from app.services.environment_model import required_weather_variables

MODEL_NAME = "Weather-driven transient two-node prototype"

ProgressCallback = Callable[
    [int, str],
    None,
]

RESULT_WARNING = (
    "This result comes from a weather-driven simplified human thermal "
    "balance prototype. Verification through thermal manikin or human "
    "experiments is still required."
)

def execute_weather_simulation_with_weather(
    *,
    request: WeatherSimulationRequest,
    weather: WeatherTimeSeries,
    city_name: str | None = None,
    progress_callback: ProgressCallback | None = None,
) -> WeatherSimulationResponse:
    def report(progress: int, stage: str) -> None:
        if progress_callback is not None:
            progress_callback(progress, stage)

    if city_name is None:
        city_name = get_city(request.city_id).name

    assumptions = request.environment_assumptions

    report(30, "running_control_simulation")
    control_result = simulate_material_with_weather(
        duration_minutes=request.duration_minutes,
        output_interval_minutes=request.output_interval_minutes,
        weather=weather,
        person=request.person,
        material=request.control_material,
        assumptions=assumptions,
    )

    report(65, "running_radiative_cooling_simulation")
    rc_result = simulate_material_with_weather(
        duration_minutes=request.duration_minutes,
        output_interval_minutes=request.output_interval_minutes,
        weather=weather,
        person=request.person,
        material=request.rc_material,
        assumptions=assumptions,
    )

    report(90, "generating_summary")


    return WeatherSimulationResponse(
        model_name=MODEL_NAME,
        model_version=MODEL_VERSION,
        city=city_name,
        duration_minutes=request.duration_minutes,
        control=control_result,
        radiative_cooling=rc_result,
        summary=build_simulation_summary(control_result, rc_result),
        warning=RESULT_WARNING,
        weather=weather,
        environment_model_note=" ".join(assumptions.describe()),
        environment_assumptions=assumptions,
        model_metadata=build_model_metadata(),
    )


async def execute_weather_simulation(
    request: WeatherSimulationRequest,
    progress_callback: ProgressCallback | None = None,
) -> WeatherSimulationResponse:
    def report(
        progress: int,
        stage: str,
    ) -> None:
        if progress_callback is not None:
            progress_callback(
                progress,
                stage,
            )

    city = get_city(request.city_id)

    report(
        10,
        "downloading_weather",
    )

    weather = await get_historical_weather(
        city=city,
        start_time_local=request.start_time_local,
        duration_minutes=request.duration_minutes,
        extra_variables=required_weather_variables(request.environment_assumptions),
    )

    return execute_weather_simulation_with_weather(
        request=request,
        weather=weather,
        city_name=city.name,
        progress_callback=progress_callback,
    )
```

### File: `backend/app/utils/date_defaults.py`
```python
"""Dynamic application date defaults."""

from __future__ import annotations

from datetime import date, datetime


def get_previous_complete_year(
    today: date | None = None,
) -> int:
    """Return the year before the current calendar year."""
    current_date = today or date.today()
    return current_date.year - 1


def get_default_simulation_datetime(
    now: datetime | None = None,
) -> datetime:
    """Return the representative datetime in the previous year."""
    current_datetime = now or datetime.now().astimezone()

    return datetime(
        year=current_datetime.year - 1,
        month=7,
        day=15,
        hour=10,
        minute=0,
        second=0,
        microsecond=0,
        tzinfo=current_datetime.tzinfo,
    )
```

### File: `backend/app/worker/__init__.py`
```python

```

### File: `backend/app/worker/celery_app.py`
```python
from celery import Celery
from kombu import Queue

from app.core.config import settings


celery_app = Celery(
    "radiative_cooling_worker",
    broker=settings.celery_broker_url,
    backend=settings.celery_result_backend,
    include=["app.worker.tasks", "app.worker.optimization_tasks"],
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_acks_late=True,
    task_reject_on_worker_lost=True,
    worker_prefetch_multiplier=1,
    broker_connection_retry_on_startup=True,
    result_expires=3600,
    task_queues=(
        Queue("default"),
        Queue("global_standard"),
        Queue("global_large"),
        Queue("optimization"),
    ),
    task_default_queue="default",
    task_routes={
        "simulation.run_weather": {"queue": "default"},
        "global_batch.run_city": {"queue": "global_standard"},
        "optimization.run": {"queue": "optimization"},
    },
)

# One entry per reaper task. Two entries pointing at the same task run it twice.
celery_app.conf.beat_schedule = {
    "reap-expired-city-leases": {
        "task": "global_batch.reap_expired_leases",
        "schedule": settings.LEASE_REAPER_INTERVAL_SECONDS,
        "options": {"queue": "default"},
    },
    "reap-expired-job-leases": {
        "task": "simulation.reap_expired_leases",
        "schedule": settings.LEASE_REAPER_INTERVAL_SECONDS,
        "options": {"queue": "default"},
    },
    "reap-expired-optimization-leases": {
        "task": "optimization.reap_expired_leases",
        "schedule": settings.LEASE_REAPER_INTERVAL_SECONDS,
        "options": {"queue": "default"},
    },
}
```

### File: `backend/app/worker/optimization_tasks.py`
```python
"""Inverse optimization task. Same lease/cancel contract as the other tasks.

Heartbeats are emitted from inside evaluate() (throttled), so a single long
generation can never outlive the lease TTL. Cancellation latency is bounded
by CITY_HEARTBEAT_SECONDS. No checkpoints: a reaped job restarts from scratch.
"""

from __future__ import annotations

import asyncio
import logging
import time

from celery import Task
from sqlalchemy import func, select

from app.core.config import settings
from app.core.time import utc_now
from app.db.session import SessionLocal
from app.models.optimization_job import OptimizationJob
from app.schemas.optimization import GenerationRecord, OptimizationCreate
from app.services.job_state import JobStatus, assert_job_transition
from app.services.leases import (
    acquire_optimization_lease,
    heartbeat_optimization_lease,
    release_optimization_lease,
)
from app.services.optimization.evaluator import MaterialEvaluator, prepare_samples
from app.services.optimization.runner import OptimizationCancelled
from app.services.optimization.service import execute_optimization
from app.worker.celery_app import celery_app
from app.worker.tasks import LeaseLostError, _owner_id
from app.services.stored_requests import load_stored_request

logger = logging.getLogger(__name__)

OPTIMIZATION_QUEUE = "optimization"


class OptimizationReporter:
    """Throttled, owner-guarded writes of progress, history and cancel checks."""

    def __init__(self, job_id: str, owner: str) -> None:
        self.job_id = job_id
        self.owner = owner
        self.interval = settings.CITY_HEARTBEAT_SECONDS
        self.last = 0.0
        self.progress = 0
        self.stage = "initializing"
        self.history: list[dict] = []
        self.evaluations = 0

    def __call__(
        self,
        *,
        progress: int | None = None,
        stage: str | None = None,
        history_record: GenerationRecord | None = None,
        evaluations: int | None = None,
        force: bool = False,
    ) -> None:
        if progress is not None:
            self.progress = max(self.progress, min(99, int(progress)))
        if stage is not None:
            self.stage = stage
        if history_record is not None:
            self.history.append(history_record.model_dump(mode="json"))
            self.evaluations = history_record.evaluation_count
        if evaluations is not None:
            self.evaluations = evaluations

        if not force and time.monotonic() - self.last < self.interval:
            return
        self.flush()

    def flush(self) -> None:
        with SessionLocal() as session:
            row = session.execute(
                select(OptimizationJob.status, OptimizationJob.cancel_requested_at)
                .where(OptimizationJob.id == self.job_id)
            ).one_or_none()
            if row is None:
                raise RuntimeError(f"Optimization job not found: {self.job_id}")
            if row.cancel_requested_at is not None or row.status in {JobStatus.CANCELLING, JobStatus.CANCELLED}:
                raise OptimizationCancelled()

            ok = heartbeat_optimization_lease(
                session, self.job_id, self.owner,
                stage=self.stage[:100], progress=self.progress,
                history_json=list(self.history), evaluation_count=self.evaluations,
            )
        if not ok:
            raise LeaseLostError()
        self.last = time.monotonic()


def _finish(session, job_id: str, owner: str, target: JobStatus, **values) -> bool:
    current = session.scalar(
        select(OptimizationJob.status).where(
            OptimizationJob.id == job_id, OptimizationJob.lease_owner == owner
        )
    )
    if current is None:
        return False
    assert_job_transition(current, target)
    return heartbeat_optimization_lease(
        session, job_id, owner, status=target, stage=target, completed_at=func.now(), **values
    )


@celery_app.task(bind=True, name="optimization.run", acks_late=True, reject_on_worker_lost=True)
def run_optimization_task(self: Task, job_id: str) -> dict:
    owner = _owner_id(self)
    lease_lost = False

    with SessionLocal() as session:
        if not acquire_optimization_lease(session, job_id, owner):
            return {"job_id": job_id, "status": "skipped", "reason": "lease_not_acquired"}

    try:
        with SessionLocal() as session:
            job = session.get(OptimizationJob, job_id)
            if job is None:
                raise RuntimeError(f"Optimization job not found: {job_id}")
            request = load_stored_request(OptimizationCreate, job.request_json)
            ok = heartbeat_optimization_lease(
                session, job_id, owner,
                stage="preparing_samples", progress=1, error_message=None,
                history_json=[], evaluation_count=0, result_json=None,
                attempt=OptimizationJob.attempt + 1,
            )
        if not ok:
            raise LeaseLostError()

        reporter = OptimizationReporter(job_id, owner)

        preparation = asyncio.run(
            prepare_samples(request, progress=lambda p, s: reporter(progress=p, stage=s))
        )
        evaluator = MaterialEvaluator(
            request, preparation.samples,
            on_evaluation=lambda count: reporter(evaluations=count),
        )
        result = execute_optimization(request, evaluator, preparation, report=reporter)
        reporter(force=True)  # last cancel check, flush history

        with SessionLocal() as session:
            ok = _finish(
                session, job_id, owner, JobStatus.COMPLETED,
                progress=100, error_message=None,
                evaluation_count=result.evaluation_count,
                history_json=reporter.history,
                result_json=result.model_dump(mode="json"),
            )
        if not ok:
            raise LeaseLostError()
        return {"job_id": job_id, "status": "completed", "verdict": result.verdict}

    except LeaseLostError:
        lease_lost = True
        return {"job_id": job_id, "status": "lease_lost"}

    except OptimizationCancelled:
        with SessionLocal() as session:
            _finish(session, job_id, owner, JobStatus.CANCELLED)
        return {"job_id": job_id, "status": "cancelled"}

    except Exception as error:
        logger.exception("optimization job %s failed", job_id)
        with SessionLocal() as session:
            _finish(session, job_id, owner, JobStatus.FAILED, error_message=str(error)[:4000])
        raise

    finally:
        if not lease_lost:
            with SessionLocal() as session:
                release_optimization_lease(session, job_id, owner)


@celery_app.task(name="optimization.reap_expired_leases")
def reap_expired_optimization_leases() -> dict:
    requeued: list[str] = []
    failed: list[str] = []

    with SessionLocal() as session:
        stale = session.scalars(
            select(OptimizationJob)
            .where(
                OptimizationJob.status.in_([JobStatus.RUNNING, JobStatus.CANCELLING]),
                OptimizationJob.lease_expires_at < func.now(),
            )
            .with_for_update(skip_locked=True)
        ).all()

        for job in stale:
            if job.status == JobStatus.CANCELLING:
                assert_job_transition(job.status, JobStatus.CANCELLED)
                job.status, job.stage, job.completed_at = JobStatus.CANCELLED, "cancelled", utc_now()
            elif job.attempt < settings.CITY_MAX_RETRIES:
                assert_job_transition(job.status, JobStatus.QUEUED)
                job.status, job.stage = JobStatus.QUEUED, "retry_scheduled"
                requeued.append(job.id)
            else:
                assert_job_transition(job.status, JobStatus.FAILED)
                job.status, job.stage = JobStatus.FAILED, "failed"
                job.error_message = f"lease expired after {job.attempt} attempt(s)"
                job.completed_at = utc_now()
                failed.append(job.id)
            job.lease_owner = None
            job.lease_expires_at = None

        session.commit()

    for job_id in requeued:
        run_optimization_task.apply_async(args=[job_id], queue=OPTIMIZATION_QUEUE)

    return {"requeued": requeued, "failed": failed}
```

### File: `backend/app/worker/tasks.py`
```python
"""Celery tasks (Stage 9).

Both task families share one reliability contract:

* a row-level lease is acquired atomically before any work; a redelivered
  message that cannot acquire it exits silently (idempotent);
* every write is guarded by ``lease_owner == owner`` and rolled back when the
  guard fails; after ``LeaseLostError`` nothing is written;
* cancellation is cooperative and checked at every heartbeat;
* status changes go through ``job_state``;
* re-queued work keeps its original Celery queue.
"""

from __future__ import annotations

import asyncio
import logging
import os
import socket
import time

from celery import Task
from sqlalchemy import func, select, update

from app.core.config import settings
from app.core.time import utc_now
from app.db.session import SessionLocal
from app.models.global_batch import GlobalBatchJob, GlobalCityResult
from app.models.simulation_job import SimulationJob
from app.schemas.global_batch import GlobalBatchCreate, MonthlyAdaptationResult
from app.schemas.simulation import WeatherSimulationRequest
from app.services.annual_sampling import estimate_sample_count
from app.services.checkpoints import (
    CheckpointProvenance,
    load_resume_state,
    upsert_month_checkpoint,
)
from app.services.climate_adaptation import analyze_city_climate_adaptation
from app.services.execution_profile import resolve_queue_name
from app.services.global_batch_service import refresh_batch_status
from app.services.job_state import (
    BatchStatus,
    CityStatus,
    JobStatus,
    assert_batch_transition,
    assert_city_transition,
    assert_job_transition,
)
from app.services.leases import (
    acquire_city_lease,
    acquire_job_lease,
    heartbeat_city_lease,
    heartbeat_job_lease,
    release_city_lease,
    release_job_lease,
)
from app.services.result_storage import save_simulation_result
from app.services.weather_simulation import execute_weather_simulation
from app.worker.celery_app import celery_app
from app.services.stored_requests import load_stored_request

logger = logging.getLogger(__name__)

SINGLE_JOB_QUEUE = "default"


class JobCancelledError(Exception):
    pass


class GlobalBatchCancelledError(Exception):
    pass


class LeaseLostError(Exception):
    """The lease was reaped or taken by another worker. Do not write anything."""


def _owner_id(task: Task) -> str:
    return f"{socket.gethostname()}:{os.getpid()}:{task.request.id}"


# ---------------------------------------------------------------------------
# Single simulation job helpers (kept for tests and ad-hoc tooling)
# ---------------------------------------------------------------------------

def update_job(job_id: str, **values: object) -> None:
    """Unconditional update. Not used by the task itself any more; the task
    writes through ``heartbeat_job_lease`` so writes are owner-guarded."""
    with SessionLocal() as session:
        job = session.get(SimulationJob, job_id)
        if job is None:
            raise RuntimeError(f"Simulation task not found:{job_id}")
        for field, value in values.items():
            setattr(job, field, value)
        session.commit()


def ensure_not_cancelled(job_id: str) -> None:
    with SessionLocal() as session:
        job = session.get(SimulationJob, job_id)
        if job is None:
            raise RuntimeError(f"Simulation task not found:{job_id}")
        if job.status in {JobStatus.CANCELLING, JobStatus.CANCELLED}:
            raise JobCancelledError()


def _finish_job_as_owner(session, job_id: str, owner: str, target: JobStatus, **values: object) -> bool:
    current = session.scalar(
        select(SimulationJob.status).where(
            SimulationJob.id == job_id, SimulationJob.lease_owner == owner
        )
    )
    if current is None:
        return False
    assert_job_transition(current, target)
    return heartbeat_job_lease(
        session, job_id, owner,
        status=target, stage=target, completed_at=func.now(), **values,
    )


@celery_app.task(
    bind=True,
    name="simulation.run_weather",
    acks_late=True,
    reject_on_worker_lost=True,
)
def run_weather_simulation_task(self: Task, job_id: str) -> dict:
    owner = _owner_id(self)
    lease_lost = False

    with SessionLocal() as session:
        if not acquire_job_lease(session, job_id, owner):
            return {"job_id": job_id, "status": "skipped", "reason": "lease_not_acquired"}

    try:
        with SessionLocal() as session:
            job = session.get(SimulationJob, job_id)
            if job is None:
                raise RuntimeError(f"Simulation task not found:{job_id}")
            request = load_stored_request(WeatherSimulationRequest, job.request_json)

            ok = heartbeat_job_lease(
                session, job_id, owner,
                stage="initializing", progress=2, error_message=None,
                attempt=SimulationJob.attempt + 1,
            )
        if not ok:
            lease_lost = True
            raise LeaseLostError()

        def report(progress: int, stage: str) -> None:
            nonlocal lease_lost
            ensure_not_cancelled(job_id)

            self.update_state(
                state="PROGRESS",
                meta={"job_id": job_id, "progress": progress, "stage": stage},
            )
            with SessionLocal() as session:
                beat_ok = heartbeat_job_lease(session, job_id, owner, stage=stage, progress=progress)
            if not beat_ok:
                lease_lost = True
                raise LeaseLostError()

        result = asyncio.run(execute_weather_simulation(request=request, progress_callback=report))

        report(95, "saving_result")
        result_path = save_simulation_result(job_id=job_id, result=result)

        with SessionLocal() as session:
            ensure_not_cancelled(job_id)
            ok = _finish_job_as_owner(
                session, job_id, owner, JobStatus.COMPLETED,
                progress=100,
                summary_json=result.summary.model_dump(mode="json"),
                result_path=str(result_path),
                error_message=None,
            )
        if not ok:
            lease_lost = True
            raise LeaseLostError()

        return {"job_id": job_id, "status": "completed"}

    except LeaseLostError:
        return {"job_id": job_id, "status": "lease_lost"}

    except JobCancelledError:
        with SessionLocal() as session:
            _finish_job_as_owner(session, job_id, owner, JobStatus.CANCELLED)
        return {"job_id": job_id, "status": "cancelled"}

    except Exception as error:
        logger.exception("simulation job %s failed", job_id)
        with SessionLocal() as session:
            _finish_job_as_owner(
                session, job_id, owner, JobStatus.FAILED,
                error_message=str(error)[:4000],
            )
        raise

    finally:
        if not lease_lost:
            with SessionLocal() as session:
                release_job_lease(session, job_id, owner)


@celery_app.task(name="simulation.reap_expired_leases")
def reap_expired_job_leases() -> dict:
    """Re-queue (or fail) single jobs whose worker died without releasing."""
    requeued: list[str] = []
    failed: list[str] = []

    with SessionLocal() as session:
        stale = session.scalars(
            select(SimulationJob)
            .where(
                SimulationJob.status.in_([JobStatus.RUNNING, JobStatus.CANCELLING]),
                SimulationJob.lease_expires_at < func.now(),
            )
            .with_for_update(skip_locked=True)
        ).all()

        for job in stale:
            if job.status == JobStatus.CANCELLING:
                assert_job_transition(job.status, JobStatus.CANCELLED)
                job.status = JobStatus.CANCELLED
                job.stage = "cancelled"
                job.completed_at = utc_now()
            elif job.attempt < settings.CITY_MAX_RETRIES:
                assert_job_transition(job.status, JobStatus.QUEUED)
                job.status = JobStatus.QUEUED
                job.stage = "retry_scheduled"
                requeued.append(job.id)
            else:
                assert_job_transition(job.status, JobStatus.FAILED)
                job.status = JobStatus.FAILED
                job.stage = "failed"
                job.error_message = f"lease expired after {job.attempt} attempt(s)"
                job.completed_at = utc_now()
                failed.append(job.id)
            job.lease_owner = None
            job.lease_expires_at = None

        session.commit()

    for job_id in requeued:
        run_weather_simulation_task.apply_async(args=[job_id], queue=SINGLE_JOB_QUEUE)

    return {"requeued": requeued, "failed": failed}


# ---------------------------------------------------------------------------
# Global batch city task
# ---------------------------------------------------------------------------

def _batch_cancel_requested(session, batch_id: str) -> bool:
    row = session.execute(
        select(GlobalBatchJob.status, GlobalBatchJob.cancel_requested_at)
        .where(GlobalBatchJob.id == batch_id)
    ).one_or_none()
    if row is None:
        raise RuntimeError(f"Global batch not found: {batch_id}")
    status, cancel_requested_at = row
    return cancel_requested_at is not None or status in {BatchStatus.CANCELLING, BatchStatus.CANCELLED}


def _finish_city_as_owner(session, city_result_id: str, owner: str, target: CityStatus, **values: object) -> bool:
    assert_city_transition(CityStatus.RUNNING, target)
    return heartbeat_city_lease(
        session, city_result_id, owner,
        status=target, stage=target, completed_at=func.now(), **values,
    )


def _fail_or_requeue_city(session, city_result_id: str, owner: str, error: Exception) -> bool:
    """True -> set back to queued and must be re-submitted; False -> terminal failed."""
    retry_count = session.scalar(
        select(GlobalCityResult.retry_count).where(
            GlobalCityResult.id == city_result_id, GlobalCityResult.lease_owner == owner
        )
    )
    if retry_count is None:
        return False  # not ours any more

    message = str(error)[:4000]

    if retry_count < settings.CITY_MAX_RETRIES:
        assert_city_transition(CityStatus.RUNNING, CityStatus.QUEUED)
        return heartbeat_city_lease(
            session, city_result_id, owner,
            status=CityStatus.QUEUED,
            stage="retry_scheduled",
            error_message=message,
            retry_count=GlobalCityResult.retry_count + 1,
        )

    _finish_city_as_owner(session, city_result_id, owner, CityStatus.FAILED, error_message=message)
    return False


@celery_app.task(
    bind=True,
    name="global_batch.run_city",
    acks_late=True,
    reject_on_worker_lost=True,
)
def run_global_city_analysis_task(self: Task, city_result_id: str) -> dict:
    owner = _owner_id(self)
    batch_id: str | None = None
    queue_name = "global_standard"
    lease_lost = False

    with SessionLocal() as session:
        if not acquire_city_lease(session, city_result_id, owner):
            return {"city_result_id": city_result_id, "status": "skipped", "reason": "lease_not_acquired"}

    try:
        with SessionLocal() as session:
            city_result = session.get(GlobalCityResult, city_result_id)
            if city_result is None:
                raise RuntimeError(f"Global city result not found: {city_result_id}")
            batch = session.get(GlobalBatchJob, city_result.batch_id)
            if batch is None:
                raise RuntimeError(f"Global batch not found: {city_result.batch_id}")

            batch_id = batch.id
            request = load_stored_request(GlobalBatchCreate, batch.request_json)
            queue_name = resolve_queue_name(request)
            city_id = city_result.city_id
            provenance = CheckpointProvenance.for_request(request)

            if _batch_cancel_requested(session, batch_id):
                raise GlobalBatchCancelledError()

            # The API decides whether checkpoints exist (it deletes them when
            # the user opts out of resuming); the worker always trusts the
            # provenance-checked contiguous prefix that remains.
            resume = load_resume_state(
                session, city_result_id,
                start_month=request.start_month, provenance=provenance,
            )
            initial_monthly_results = [
                MonthlyAdaptationResult.model_validate(item) for item in resume.payloads
            ]
            checkpoints_discarded = list(resume.discarded)

            city_result.stage = "initializing"
            city_result.progress = 1
            city_result.completed_at = None
            city_result.error_message = None
            city_result.resumed_from_checkpoint = bool(initial_monthly_results)

            if batch.status != BatchStatus.RUNNING:
                assert_batch_transition(batch.status, BatchStatus.RUNNING)
                batch.status = BatchStatus.RUNNING
                batch.stage = "analyzing_cities"
                batch.started_at = batch.started_at or utc_now()
                batch.completed_at = None

            session.commit()

        total_sample_count = max(1, estimate_sample_count(request))
        heartbeat_interval = settings.CITY_HEARTBEAT_SECONDS
        last_beat = time.monotonic()
        last_stage: str | None = None

        def report(progress: int, stage: str) -> None:
            nonlocal last_beat, last_stage, lease_lost
            progress = max(0, min(progress, 100))
            self.update_state(
                state="PROGRESS",
                meta={
                    "batch_id": batch_id, "city_result_id": city_result_id,
                    "city_id": city_id, "progress": progress, "stage": stage,
                },
            )
            if time.monotonic() - last_beat < heartbeat_interval and stage == last_stage:
                return

            with SessionLocal() as session:
                if _batch_cancel_requested(session, batch_id):
                    raise GlobalBatchCancelledError()
                ok = heartbeat_city_lease(session, city_result_id, owner, stage=stage, progress=progress)
            if not ok:
                lease_lost = True
                raise LeaseLostError()

            last_beat = time.monotonic()
            last_stage = stage

        def save_checkpoint(
            monthly_results: list[MonthlyAdaptationResult],
            completed_month: int,
            completed_sample_count: int,
        ) -> None:
            nonlocal last_beat, lease_lost

            checkpoint_progress = max(1, min(92, round(completed_sample_count / total_sample_count * 92)))
            stage = f"checkpoint_saved_{request.year}-{completed_month:02d}"

            month_payload = next(
                (m.model_dump(mode="json") for m in monthly_results if m.month == completed_month),
                monthly_results[-1].model_dump(mode="json"),
            )
            all_payloads = [m.model_dump(mode="json") for m in monthly_results]

            with SessionLocal() as session:
                if _batch_cancel_requested(session, batch_id):
                    raise GlobalBatchCancelledError()

                retry_count = session.scalar(
                    select(GlobalCityResult.retry_count).where(GlobalCityResult.id == city_result_id)
                )

                # (a) checkpoint row staged, owner-guarded ...
                staged = upsert_month_checkpoint(
                    session,
                    city_result_id=city_result_id, owner=owner,
                    month=completed_month, attempt=retry_count or 0,
                    payload=month_payload, provenance=provenance,
                )
                if not staged:
                    session.rollback()
                    ok = False
                else:
                    # (b) ... and committed together with the heartbeat; a lost
                    # lease rolls (a) back as well.
                    ok = heartbeat_city_lease(
                        session, city_result_id, owner,
                        monthly_json=all_payloads,
                        completed_month_count=len(monthly_results),
                        last_checkpoint_month=completed_month,
                        stage=stage,
                        progress=func.greatest(GlobalCityResult.progress, checkpoint_progress),
                    )

            if not ok:
                lease_lost = True
                raise LeaseLostError()

            last_beat = time.monotonic()
            self.update_state(
                state="PROGRESS",
                meta={
                    "batch_id": batch_id, "city_result_id": city_result_id, "city_id": city_id,
                    "progress": checkpoint_progress, "stage": stage, "completed_month": completed_month,
                },
            )

        analysis = asyncio.run(
            analyze_city_climate_adaptation(
                city_id=city_id,
                request=request,
                progress_callback=report,
                checkpoint_callback=save_checkpoint,
                initial_monthly_results=initial_monthly_results,
            )
        )

        monthly_json = analysis["monthly_results"]
        last_month = max(item["month"] for item in monthly_json) if monthly_json else None

        data_quality = dict(analysis.get("data_quality", {}))
        data_quality["checkpoints_discarded"] = checkpoints_discarded
        data_quality["checkpoint_provenance"] = {
            "model_version": provenance.model_version,
            "parameter_fingerprint": provenance.parameter_fingerprint,
            "request_sha256": provenance.request_sha256,
        }

        with SessionLocal() as session:
            if _batch_cancel_requested(session, batch_id):
                raise GlobalBatchCancelledError()

            ok = _finish_city_as_owner(
                session, city_result_id, owner, CityStatus.COMPLETED,
                progress=100,
                error_message=None,
                climate_adaptation_rate_percent=analysis["climate_adaptation_rate_percent"],
                exposure_coverage_percent=analysis["exposure_coverage_percent"],
                annual_average_skin_improvement_c=analysis["annual_average_skin_improvement_c"],
                annual_average_core_improvement_c=analysis["annual_average_core_improvement_c"],
                maximum_skin_improvement_c=analysis["maximum_skin_improvement_c"],
                effective_cooling_hours=analysis["effective_cooling_hours"],
                sampled_day_count=analysis["sampled_day_count"],
                eligible_sample_count=analysis["eligible_sample_count"],
                evaluated_weighted_days=analysis["evaluated_weighted_days"],
                beneficial_weighted_days=analysis["beneficial_weighted_days"],
                skin_improvement_p50_c=analysis["skin_improvement_p50_c"],
                skin_improvement_p90_c=analysis["skin_improvement_p90_c"],
                skin_improvement_p95_c=analysis["skin_improvement_p95_c"],
                core_improvement_p50_c=analysis["core_improvement_p50_c"],
                core_improvement_p90_c=analysis["core_improvement_p90_c"],
                core_improvement_p95_c=analysis["core_improvement_p95_c"],
                heatwave_event_count=analysis["heatwave_event_count"],
                longest_heatwave_days=analysis["longest_heatwave_days"],
                analytics_json={
                    "heatwave_analysis_available": analysis.get("heatwave_analysis_available", False),
                    "heatwave_unavailable_reason": analysis.get("heatwave_unavailable_reason"),
                    "heatwave_temperature_basis": analysis.get("heatwave_temperature_basis"),
                    "heatwave_events": analysis.get("heatwave_events", []),
                    "data_quality": data_quality,
                    "metric_definitions": analysis.get("metric_definitions", {}),
                },
                monthly_json=monthly_json,
                completed_month_count=analysis["completed_month_count"],
                last_checkpoint_month=last_month,
            )
            if not ok:
                lease_lost = True
                raise LeaseLostError()

            refresh_batch_status(session, batch_id)

        return {"batch_id": batch_id, "city_result_id": city_result_id, "status": "completed"}

    except LeaseLostError:
        return {"batch_id": batch_id, "city_result_id": city_result_id, "status": "lease_lost"}

    except GlobalBatchCancelledError:
        if batch_id is not None:
            with SessionLocal() as session:
                _finish_city_as_owner(session, city_result_id, owner, CityStatus.CANCELLED, progress=100)
                refresh_batch_status(session, batch_id)
        return {"batch_id": batch_id, "city_result_id": city_result_id, "status": "cancelled"}

    except Exception as error:
        logger.exception("city %s failed", city_result_id)
        requeue = False
        if batch_id is not None:
            with SessionLocal() as session:
                requeue = _fail_or_requeue_city(session, city_result_id, owner, error)
                refresh_batch_status(session, batch_id)

        if requeue:
            run_global_city_analysis_task.apply_async(
                args=[city_result_id],
                countdown=settings.CITY_HEARTBEAT_SECONDS,
                queue=queue_name,  # keep the original queue
            )
            return {
                "batch_id": batch_id, "city_result_id": city_result_id,
                "status": "requeued", "error": str(error)[:500],
            }
        raise

    finally:
        if not lease_lost:
            with SessionLocal() as session:
                release_city_lease(session, city_result_id, owner)


@celery_app.task(name="global_batch.reap_expired_leases")
def reap_expired_leases() -> dict:
    requeued: list[tuple[str, str]] = []  # (city_result_id, queue)
    touched_batches: set[str] = set()

    with SessionLocal() as db:
        stale = db.scalars(
            select(GlobalCityResult)
            .where(
                GlobalCityResult.status == CityStatus.RUNNING,
                GlobalCityResult.lease_expires_at < func.now(),
            )
            .with_for_update(skip_locked=True)
        ).all()

        queue_by_batch: dict[str, str] = {}

        for city in stale:
            if city.batch_id not in queue_by_batch:
                batch = db.get(GlobalBatchJob, city.batch_id)
                queue_by_batch[city.batch_id] = load_stored_request(GlobalBatchCreate, batch.request_json)

            if city.retry_count < settings.CITY_MAX_RETRIES:
                assert_city_transition(city.status, CityStatus.QUEUED)
                city.status = CityStatus.QUEUED
                city.stage = "lease_expired_requeued"
                city.retry_count += 1
                requeued.append((city.id, queue_by_batch[city.batch_id]))
            else:
                assert_city_transition(city.status, CityStatus.FAILED)
                city.status = CityStatus.FAILED
                city.stage = "failed"
                city.error_message = f"lease expired after {city.retry_count} retries"
                city.completed_at = utc_now()

            city.lease_owner = None
            city.lease_expires_at = None
            touched_batches.add(city.batch_id)

        db.commit()

        for batch_id in touched_batches:
            refresh_batch_status(db, batch_id)

    for city_result_id, queue in requeued:
        run_global_city_analysis_task.apply_async(args=[city_result_id], queue=queue)

    return {"requeued": [c for c, _ in requeued], "batches": sorted(touched_batches)}
```

### File: `backend/scripts/capture_weather_fixture.py`
```python
"""Download one Open-Meteo payload and freeze it as a test fixture.

Usage (from backend/):
    python scripts/capture_weather_fixture.py tests/fixtures/dubai_2h
"""

import asyncio
import hashlib
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.core.cities import get_city  # noqa: E402
from app.schemas.simulation import WeatherSimulationRequest  # noqa: E402
from app.services.weather import (  # noqa: E402
    build_request_params,
    download_open_meteo_payload,
    normalize_local_datetime,
)


async def main(fixture_dir: Path) -> None:
    request = WeatherSimulationRequest.model_validate(
        json.loads((fixture_dir / "request.json").read_text(encoding="utf-8"))
    )

    city = get_city(request.city_id)

    start = normalize_local_datetime(request.start_time_local, city.timezone)
    end = start + timedelta(minutes=request.duration_minutes)

    params = build_request_params(
        city=city,
        start_date=(start - timedelta(hours=1)).date(),
        end_date=(end + timedelta(hours=1)).date(),
    )

    payload = await download_open_meteo_payload(params)

    raw = json.dumps(payload, sort_keys=True, ensure_ascii=True, separators=(",", ":"))
    (fixture_dir / "open_meteo_payload.json").write_text(raw, encoding="utf-8")
    (fixture_dir / "open_meteo_payload.sha256").write_text(
        hashlib.sha256(raw.encode("utf-8")).hexdigest() + "\n", encoding="utf-8"
    )
    (fixture_dir / "request_params.json").write_text(
        json.dumps(params, indent=2, sort_keys=True), encoding="utf-8"
    )

    print(f"captured {len(payload['hourly']['time'])} hourly points into {fixture_dir}")
    print(f"captured at {datetime.utcnow().isoformat()}Z")


if __name__ == "__main__":
    asyncio.run(main(Path(sys.argv[1])))
```

### File: `backend/scripts/compare_batches.py`
```python
"""Compare annual city metrics of two global batches (Stage 12 L4).

Usage: python scripts/compare_batches.py <batch_a> <batch_b> [--tolerance 1e-4]
Exit code 1 if any metric differs by more than the tolerance.
"""

from __future__ import annotations

import argparse
import sys

import httpx

FIELDS = (
    "annual_average_skin_improvement_c",
    "annual_average_core_improvement_c",
    "climate_adaptation_rate_percent",
    "exposure_coverage_percent",
)


def load(client: httpx.Client, batch_id: str) -> dict[str, dict]:
    r = client.get(f"/api/v1/global-batches/{batch_id}")
    r.raise_for_status()
    return {c["city_id"]: c for c in r.json()["city_results"] if c["status"] == "completed"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("a")
    parser.add_argument("b")
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument("--tolerance", type=float, default=1e-4)
    args = parser.parse_args()

    with httpx.Client(base_url=args.base_url, timeout=60) as client:
        a, b = load(client, args.a), load(client, args.b)

    worst = 0.0
    for city in sorted(set(a) | set(b)):
        if city not in a or city not in b:
            print(f"{city:12s} only in {'A' if city in a else 'B'}")
            worst = float("inf")
            continue
        for field in FIELDS:
            va, vb = a[city][field], b[city][field]
            if va is None or vb is None:
                same = va == vb
                diff = 0.0 if same else float("inf")
            else:
                diff = abs(va - vb)
            worst = max(worst, diff)
            print(f"{city:12s} {field:36s} {va!s:>10} {vb!s:>10} diff {diff:.2e}")

    print(f"max diff {worst:.2e} (tolerance {args.tolerance:g})")
    sys.exit(0 if worst <= args.tolerance else 1)


if __name__ == "__main__":
    main()
```

### File: `backend/scripts/inspect_radiant_environment.py`
```python
"""Hour-by-hour sky and surroundings temperatures, legacy vs physical (Stage 11 K1).

Usage (from backend/): python scripts/inspect_radiant_environment.py dubai 2023-07-15
Writes docs/acceptance/stage-11-radiant/k1-<city>-<date>.csv and prints checks.
"""

from __future__ import annotations

import argparse
import asyncio
import csv
from datetime import datetime
from pathlib import Path

from app.core.cities import get_city
from app.schemas.environment import EnvironmentAssumptions
from app.services.environment_model import required_weather_variables
from app.services.weather import get_historical_weather
from app.services.weather_interpolation import WeatherInterpolator

LEGACY = EnvironmentAssumptions()
PHYSICAL = EnvironmentAssumptions(
    mean_radiant_temperature_method="ground_energy_balance",
    sky_temperature_method="brutsaert_cloud",
)
OUT = Path("docs/acceptance/stage-11-radiant")


async def main(city_id: str, day: str) -> None:
    city = get_city(city_id)
    weather = await get_historical_weather(
        city, datetime.fromisoformat(f"{day}T00:00"), 1380,
        extra_variables=required_weather_variables(PHYSICAL),
    )
    legacy = WeatherInterpolator.from_series(weather, assumptions=LEGACY)
    physical = WeatherInterpolator.from_series(weather, assumptions=PHYSICAL)

    rows = []
    for hour in range(0, 24):
        t = hour * 3600.0
        if t > physical.t_max:
            break
        a, b = legacy.environment_at(t), physical.environment_at(t)
        cloud = float(physical.cloud_values[(abs(physical.relative_seconds - t)).argmin()])
        rows.append({
            "hour": hour, "air_c": round(b.air_temperature_c, 2), "rh": round(b.relative_humidity_percent, 1),
            "ghi": round(b.solar_radiation_w_m2, 0), "cloud_pct": round(cloud, 0),
            "sky_legacy_c": round(a.sky_temperature_c, 2), "sky_physical_c": round(b.sky_temperature_c, 2),
            "surround_legacy_c": round(a.mean_radiant_temperature_c, 2),
            "surround_physical_c": round(b.mean_radiant_temperature_c, 2),
        })

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"k1-{city_id}-{day}.csv"
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    def check(label: str, ok: bool) -> None:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")

    night = [r for r in rows if r["hour"] <= 5]
    sunny = [r for r in rows if r["ghi"] >= 600]
    clear = [r for r in rows if r["cloud_pct"] <= 10]
    overcast = [r for r in rows if r["cloud_pct"] >= 90]
    check("night: |T_ground - T_air| <= 6 K",
          all(abs(r["surround_physical_c"] - r["air_c"]) <= 6 for r in night))
    check("sunny hours: T_ground > T_air", all(r["surround_physical_c"] > r["air_c"] for r in sunny))
    check("clear hours: sky depression 8-35 K",
          all(8 <= r["air_c"] - r["sky_physical_c"] <= 35 for r in clear) if clear else True)
    check("overcast hours: sky depression <= 6 K",
          all(r["air_c"] - r["sky_physical_c"] <= 6 for r in overcast) if overcast else True)
    print(f"wrote {path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("city")
    parser.add_argument("date")
    args = parser.parse_args()
    asyncio.run(main(args.city, args.date))
```

### File: `backend/scripts/inspect_zoned_garment.py`
```python
"""Uniform vs two-zone RC garment on one hot day (Stage 12 L1).

Usage (from backend/): python scripts/inspect_zoned_garment.py dubai 2023-07-15
"""

from __future__ import annotations

import argparse
import asyncio
import csv
from datetime import datetime
from pathlib import Path

from app.core.cities import get_city
from app.schemas.environment import EnvironmentAssumptions
from app.schemas.simulation import MaterialInput, PersonInput
from app.services.environment_model import required_weather_variables
from app.services.exposure_statistics import time_weighted_mean
from app.services.two_node import simulate_material_with_weather
from app.services.weather import get_historical_weather

OUT = Path("docs/acceptance/stage-12-defaults-zones")
PERSON = PersonInput(met=2.6)
BASE = dict(name="RC", clothing_insulation_clo=0.4, solar_reflectance=0.92, infrared_emissivity=0.95)


def mean(result, attribute: str) -> float:
    points = [(p.minute, getattr(p, attribute)) for p in result.time_series]
    return round(time_weighted_mean([m for m, _ in points], [v for _, v in points]), 3)


async def main(city_id: str, day: str) -> None:
    city = get_city(city_id)
    rows = []
    for s in (0.0, 0.25, 0.5, 0.75, 1.0):
        assumptions = EnvironmentAssumptions(zone_view_separation=s)
        weather = await get_historical_weather(
            city, datetime.fromisoformat(f"{day}T12:00"), 120,
            extra_variables=required_weather_variables(assumptions),
        )
        for label, ground in (("uniform", None), ("eps_g 0.5", 0.5), ("eps_g 0.1", 0.1)):
            material = MaterialInput(**BASE, infrared_emissivity_ground_facing=ground)
            result = simulate_material_with_weather(120, 5, weather, PERSON, material, assumptions)
            rows.append({
                "separation": s, "garment": label,
                "mean_skin_c": mean(result, "skin_temperature_c"),
                "final_core_c": result.final_core_temperature_c,
                "mean_clothing_surface_c": mean(result, "clothing_surface_temperature_c"),
                "mean_surround_c": mean(result, "surround_temperature_c"),
                "mean_sky_c": mean(result, "sky_temperature_c"),
            })
            print(rows[-1])

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"l1-{city_id}-{day}.csv"
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("city")
    parser.add_argument("date")
    args = parser.parse_args()
    asyncio.run(main(args.city, args.date))
```

### File: `backend/scripts/render_model_parameters_doc.py`
```python
"""Render docs/model-parameters.md from the registry."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.services.model_parameters import (  # noqa: E402
    MODEL_PARAMETER_SET_VERSION,
    list_model_parameters,
    model_parameter_set_sha256,
)

lines = [
    "# Model parameters",
    "",
    f"Parameter set version: `{MODEL_PARAMETER_SET_VERSION}`  ",
    f"SHA-256: `{model_parameter_set_sha256()}`",
    "",
    "Generated by `scripts/render_model_parameters_doc.py`. Do not edit by hand.",
    "",
    "| name | value | unit | source type | reference | note |",
    "|---|---|---|---|---|---|",
]

for p in list_model_parameters():
    lines.append(
        f"| `{p.name}` | {p.value:g} | {p.unit} | {p.source_type} | {p.reference} | {p.note or ''} |"
    )

Path(sys.argv[1]).write_text("\n".join(lines) + "\n", encoding="utf-8")
```

### File: `backend/scripts/run_stage10_experiments.py`
```python
"""Submit the Stage 10 acceptance runs.

Usage (from backend/, API and an optimization worker running):
    python scripts/run_stage10_experiments.py
    python scripts/run_stage10_experiments.py --only F1,F2,H
Then: python scripts/summarize_optimizations.py --out docs/acceptance/stage-10-spectral
"""

from __future__ import annotations

import argparse

import httpx

PERSON = {"met": 2.6, "body_mass_kg": 70, "body_surface_area_m2": 1.8,
          "initial_core_temperature_c": 36.8, "initial_skin_temperature_c": 33.7, "position": "standing"}
CONTROL = {"name": "Conventional clothing", "clothing_insulation_clo": 0.5, "solar_reflectance": 0.3,
           "solar_transmittance": 0, "infrared_emissivity": 0.9, "projected_solar_area_factor": 0.25}
RC = {"name": "RC candidate", "clothing_insulation_clo": 0.4, "solar_reflectance": 0.9,
      "solar_transmittance": 0, "infrared_emissivity": 0.95, "projected_solar_area_factor": 0.25}

RHO = {"name": "solar_reflectance", "lower": 0.3, "upper": 0.98}
EPS = {"name": "infrared_emissivity", "lower": 0.5, "upper": 0.99}
EPS_WIDE = {"name": "infrared_emissivity", "lower": 0.05, "upper": 0.99}
EPS_W = {"name": "infrared_emissivity_window", "lower": 0.5, "upper": 0.99}
EPS_N = {"name": "infrared_emissivity_outside_window", "lower": 0.05, "upper": 0.99}
EQUAL_TO_AIR = {"mean_radiant_temperature_method": "equal_to_air"}


def c(metric, operator, threshold):
    return {"metric": metric, "operator": operator, "threshold": threshold}


def request(name, city, months, variables, objective, constraints, *,
            map_axes=None, seed=42, assumptions=None, tolerance=1e-4):
    return {
        "name": name, "city_id": city, "year": 2023, "months": months,
        "sample_days_per_month": 3, "local_start_hour": 12, "duration_minutes": 120,
        "output_interval_minutes": 5, "skin_threshold_c": 35, "core_threshold_c": 38,
        "person": PERSON, "control_material": CONTROL, "base_material": RC,
        "environment_assumptions": assumptions or {},
        "variables": variables,
        "objective": {"metric": objective[0], "sense": objective[1]},
        "constraints": constraints,
        "population_multiplier": 10, "max_generations": 30, "seed": seed,
        "secondary_demand_weight": 1e-3, "convergence_tolerance": tolerance,
        "requirement_map": (
            {"x_variable": map_axes[0], "y_variable": map_axes[1], "resolution": 11} if map_axes else None
        ),
    }


GZ_CONSTRAINTS = [c("skin_exceedance_fraction", "<=", 0.1), c("peak_core_temperature_c", "<=", 38)]
RHO_EPS_MAP = ("solar_reflectance", "infrared_emissivity")

EXPERIMENTS = {
    "F1": request("S10-F1 Guangzhou Aug exceedance (rerun Exp-B)", "guangzhou", [8], [RHO, EPS],
                  ("skin_exceedance_fraction", "minimize"), GZ_CONSTRAINTS, map_axes=RHO_EPS_MAP),
    "F2": request("S10-F2 Guangzhou Aug degree-hours", "guangzhou", [8], [RHO, EPS],
                  ("skin_excess_degree_hours", "minimize"), [c("peak_core_temperature_c", "<=", 38)],
                  map_axes=RHO_EPS_MAP),
    "G1": request("S10-G1 Dubai Jul gray eps, MRT air+solar", "dubai", [7], [EPS_WIDE],
                  ("peak_core_temperature_c", "minimize"), []),
    "G2": request("S10-G2 Dubai Jul gray eps, MRT = air", "dubai", [7], [EPS_WIDE],
                  ("peak_core_temperature_c", "minimize"), [], assumptions=EQUAL_TO_AIR),
    "H1": request("S10-H1 Dubai Jul selective, MRT air+solar", "dubai", [7], [RHO, EPS_W, EPS_N],
                  ("skin_excess_degree_hours", "minimize"), [c("peak_core_temperature_c", "<=", 38)],
                  map_axes=("infrared_emissivity_window", "infrared_emissivity_outside_window")),
    "H2": request("S10-H2 Dubai Jul selective, MRT = air", "dubai", [7], [RHO, EPS_W, EPS_N],
                  ("skin_excess_degree_hours", "minimize"), [c("peak_core_temperature_c", "<=", 38)],
                  map_axes=("infrared_emissivity_window", "infrared_emissivity_outside_window"),
                  assumptions=EQUAL_TO_AIR),
    **{
        f"I-s{seed}": request(f"S10-I Lhasa Jul material demand seed {seed}", "lhasa", [7], [RHO, EPS],
                              ("material_demand", "minimize"), GZ_CONSTRAINTS,
                              map_axes=RHO_EPS_MAP, seed=seed)
        for seed in (42, 1, 2, 3, 4, 5)
    },
    **{
        f"J-{tol:g}": request(f"S10-J Dubai Jul peak core, atol {tol:g}", "dubai", [7], [EPS_WIDE],
                              ("peak_core_temperature_c", "minimize"), [], tolerance=tol)
        for tol in (1e-3, 1e-4, 1e-5)
    },
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument("--only", default="")
    args = parser.parse_args()
    selected = [k for k in EXPERIMENTS if not args.only or k in args.only.split(",")]

    with httpx.Client(base_url=args.base_url, timeout=60) as client:
        for key in selected:
            response = client.post("/api/v1/optimizations", json=EXPERIMENTS[key])
            response.raise_for_status()
            print(f"{key:8s} {response.json()['id']}  {EXPERIMENTS[key]['name']}")


if __name__ == "__main__":
    main()
```

### File: `backend/scripts/run_stage11_experiments.py`
```python
"""Stage 11 acceptance runs. Usage (from backend/): python scripts/run_stage11_experiments.py [--only G3,H3]"""

from __future__ import annotations

import argparse

import httpx

from run_stage10_experiments import CONTROL, EPS_N, EPS_W, EPS_WIDE, PERSON, RC, RHO, EPS, c, request

PHYSICAL = {"mean_radiant_temperature_method": "ground_energy_balance",
            "sky_temperature_method": "brutsaert_cloud"}
CORE = [c("peak_core_temperature_c", "<=", 38)]

OPTIMIZATIONS = {
    "G3": request("S11-G3 Dubai Jul gray eps, physical env", "dubai", [7], [EPS_WIDE],
                  ("peak_core_temperature_c", "minimize"), [], assumptions=PHYSICAL),
    **{
        f"G3-k{k}": request(f"S11-G3 Dubai Jul gray eps, physical env, K={k}", "dubai", [7], [EPS_WIDE],
                            ("peak_core_temperature_c", "minimize"), [],
                            assumptions={**PHYSICAL, "ground_soil_conductance_w_m2k": k})
        for k in (5, 40)
    },
    "H3": request("S11-H3 Dubai Jul selective, physical env", "dubai", [7], [RHO, EPS_W, EPS_N],
                  ("skin_excess_degree_hours", "minimize"), CORE,
                  map_axes=("infrared_emissivity_window", "infrared_emissivity_outside_window"),
                  assumptions=PHYSICAL),
    "F3": request("S11-F3 Guangzhou Aug degree-hours, physical env", "guangzhou", [8], [RHO, EPS],
                  ("skin_excess_degree_hours", "minimize"), CORE,
                  map_axes=("solar_reflectance", "infrared_emissivity"), assumptions=PHYSICAL),
}


def batch(name: str, assumptions: dict) -> dict:
    return {
        "name": name, "city_ids": ["dubai", "guangzhou", "lhasa"], "year": 2023,
        "start_month": 7, "end_month": 7, "analysis_resolution": "representative",
        "sample_days_per_month": 3, "local_start_hour": 12, "duration_minutes": 120,
        "output_interval_minutes": 10, "person": PERSON, "control_material": CONTROL,
        "rc_material": RC, "environment_assumptions": assumptions,
    }


BATCHES = {"K5-legacy": batch("S11-K5 legacy env", {}), "K5-physical": batch("S11-K5 physical env", PHYSICAL)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument("--only", default="")
    args = parser.parse_args()
    keep = lambda key: not args.only or key in args.only.split(",")  # noqa: E731

    with httpx.Client(base_url=args.base_url, timeout=60) as client:
        for key, body in OPTIMIZATIONS.items():
            if keep(key):
                r = client.post("/api/v1/optimizations", json=body)
                r.raise_for_status()
                print(f"{key:10s} optimization {r.json()['id']}")
        for key, body in BATCHES.items():
            if keep(key):
                r = client.post("/api/v1/global-batches", json=body)
                r.raise_for_status()
                print(f"{key:10s} batch        {r.json()['id']}")


if __name__ == "__main__":
    main()
```

### File: `backend/scripts/run_stage12_experiments.py`
```python
"""Stage 12 acceptance runs. Usage (from backend/): python scripts/run_stage12_experiments.py [--only L2-s50,L4]"""

from __future__ import annotations

import argparse

import httpx

from run_stage10_experiments import EPS_N, EPS_W, EPS_WIDE, RHO, c, request
from run_stage11_experiments import batch

GROUND = {"name": "infrared_emissivity_ground_facing", "lower": 0.05, "upper": 0.99}
CORE = [c("peak_core_temperature_c", "<=", 38)]
PHYSICAL = {"mean_radiant_temperature_method": "ground_energy_balance",
            "sky_temperature_method": "brutsaert_cloud"}

OPTIMIZATIONS = {
    **{
        f"L2-s{round(s * 100)}": request(
            f"S12-L2 Dubai Jul eps + eps_g, s={s}", "dubai", [7], [EPS_WIDE, GROUND],
            ("peak_core_temperature_c", "minimize"), [],
            map_axes=("infrared_emissivity", "infrared_emissivity_ground_facing"),
            assumptions={**PHYSICAL, "zone_view_separation": s},
        )
        for s in (0.0, 0.25, 0.5, 0.75)
    },
    "L3": request("S12-L3 Dubai Jul selective + eps_g", "dubai", [7], [RHO, EPS_W, EPS_N, GROUND],
                  ("skin_excess_degree_hours", "minimize"), CORE,
                  map_axes=("infrared_emissivity_window", "infrared_emissivity_ground_facing"),
                  assumptions=PHYSICAL),
    "L5": request("S12-L5 Guangzhou Aug eps + eps_g", "guangzhou", [8], [RHO, EPS_WIDE, GROUND],
                  ("skin_excess_degree_hours", "minimize"), CORE,
                  map_axes=("infrared_emissivity", "infrared_emissivity_ground_facing"),
                  assumptions=PHYSICAL),
}

# L4: omitting assumptions must now equal the explicit Stage 11 physical batch (K5-physical).
BATCHES = {"L4": batch("S12-L4 default env", {})}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument("--only", default="")
    args = parser.parse_args()
    keep = lambda key: not args.only or key in args.only.split(",")  # noqa: E731

    with httpx.Client(base_url=args.base_url, timeout=60) as client:
        for key, body in OPTIMIZATIONS.items():
            if keep(key):
                r = client.post("/api/v1/optimizations", json=body)
                r.raise_for_status()
                print(f"{key:8s} optimization {r.json()['id']}")
        for key, body in BATCHES.items():
            if keep(key):
                body = {k: v for k, v in body.items() if k != "environment_assumptions" or v}
                r = client.post("/api/v1/global-batches", json=body)
                r.raise_for_status()
                print(f"{key:8s} batch        {r.json()['id']}")


if __name__ == "__main__":
    main()
```

### File: `backend/scripts/summarize_optimizations.py`
```python
"""Summarize completed optimization jobs (Markdown + JSON).

Aligned with the current OptimizationJobDetail / OptimizationResult /
RequirementMapResult schemas (plateau_fraction on the map, best_corner,
simulation_count, multi-variable optical space, etc.).

Usage (from backend/, API running):
    python scripts/summarize_optimizations.py --out docs/acceptance/stage-optimization
"""

from __future__ import annotations

import argparse
import json
import statistics
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import httpx

KEY_METRICS = (
    "peak_skin_temperature_c",
    "skin_exceedance_fraction",
    "peak_core_temperature_c",
    "mean_skin_cooling_c",
)

# Grouping keys
GROUP_EXCLUDE = {"name", "seed"}  # same setup, different seed
CURVE_EXCLUDE = GROUP_EXCLUDE | {"population_multiplier"}

# Common optical / clothing variables that may appear in best.parameters
PARAM_KEYS_OF_INTEREST = (
    "solar_reflectance",
    "solar_transmittance",
    "infrared_emissivity",
    "infrared_emissivity_window",
    "infrared_emissivity_outside_window",
    "infrared_emissivity_ground_facing",
    "infrared_transmittance",
    "clothing_insulation_clo",
    "evaporative_resistance_m2pa_w",
)


def fetch_details(client: httpx.Client, max_workers: int = 8) -> list[dict]:
    """Paginate list endpoint, then fetch completed job details in parallel."""
    items: list[dict] = []
    offset = 0
    while True:
        page = client.get(
            "/api/v1/optimizations",
            params={"limit": 100, "offset": offset},
        ).json()
        batch = page.get("items") or []
        items.extend(batch)
        offset += len(batch)
        total = page.get("total", offset)
        if not batch or offset >= total:
            break

    completed_ids = [i["id"] for i in items if i.get("status") == "completed"]
    if not completed_ids:
        return []

    details: list[dict] = []

    def _get(job_id: str) -> dict:
        return client.get(f"/api/v1/optimizations/{job_id}").json()

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(_get, jid): jid for jid in completed_ids}
        for fut in as_completed(futures):
            try:
                details.append(fut.result())
            except Exception as exc:  # noqa: BLE001
                print(f"warn: failed to fetch {futures[fut]}: {exc}")

    # Stable order by name then id for reproducible summaries
    details.sort(key=lambda d: (d.get("name") or "", d.get("id") or ""))
    return details


def group_key(request: dict, exclude: set[str]) -> str:
    return json.dumps(
        {k: v for k, v in request.items() if k not in exclude},
        sort_keys=True,
        default=str,
    )


def safe_get(d: dict | None, *keys: str, default: Any = None) -> Any:
    cur: Any = d
    for k in keys:
        if not isinstance(cur, dict):
            return default
        cur = cur.get(k)
        if cur is None:
            return default
    return cur


def summarize(detail: dict) -> dict:
    req = detail.get("request") or {}
    res = detail.get("result") or {}
    best = res.get("best") or {}
    upper = res.get("optical_upper_bound")
    rmap = res.get("requirement_map")
    baseline = res.get("baseline") or {}
    best_corner = res.get("best_corner")

    variables = req.get("variables") or []
    lower = {v["name"]: v.get("lower") for v in variables if isinstance(v, dict)}

    constraints = req.get("constraints") or []
    constraint_str = "; ".join(
        f'{c.get("metric")} {c.get("operator")} {c.get("threshold")}'
        for c in constraints
        if isinstance(c, dict)
    )

    best_params = best.get("parameters") or {}
    best_metrics = best.get("metrics")

    row: dict[str, Any] = {
        "name": detail.get("name"),
        "id": (detail.get("id") or "")[:8],
        "city": req.get("city_id"),
        "months": req.get("months"),
        "seed": req.get("seed"),
        "mult": req.get("population_multiplier"),
        "constraints": constraint_str,
        "verdict": res.get("verdict"),
        "algorithm": res.get("algorithm"),
        "model_version": res.get("model_version"),
        "best": {k: round(v, 4) for k, v in best_params.items() if isinstance(v, (int, float))},
        "best_objective": best.get("objective_value"),
        "best_violation": best.get("constraint_violation"),
        "best_feasible": best.get("feasible"),
        "best_metrics": (
            {k: best_metrics[k] for k in KEY_METRICS if k in best_metrics}
            if isinstance(best_metrics, dict)
            else None
        ),
        "baseline_feasible": baseline.get("feasible"),
        "upper_feasible": upper.get("feasible") if upper else None,
        "upper_violation": upper.get("constraint_violation") if upper else None,
        "upper_peak_skin": safe_get(upper, "metrics", "peak_skin_temperature_c"),
        "best_corner_feasible": best_corner.get("feasible") if best_corner else None,
        "best_corner_params": (
            {k: round(v, 4) for k, v in (best_corner.get("parameters") or {}).items()
             if isinstance(v, (int, float))}
            if best_corner
            else None
        ),
        "evaluations": res.get("evaluation_count"),
        "simulations": res.get("simulation_count"),
        "sample_count": res.get("sample_count"),
        "generations": res.get("generations"),
        "seconds": res.get("elapsed_seconds"),
        "warnings": res.get("warnings") or [],
        "sensitivities": res.get("sensitivities") or [],
        "parameter_fingerprint": res.get("parameter_fingerprint"),
    }

    if rmap:
        # Prefer server-computed plateau_fraction; fall back only if absent
        plateau = rmap.get("plateau_fraction")
        if plateau is None:
            cells_flat = [c for r in (rmap.get("cells") or []) for c in r if c]
            values = [c["metric_value"] for c in cells_flat if "metric_value" in c]
            if values:
                low = min(values)
                plateau = sum(abs(v - low) < 1e-6 for v in values) / len(values)

        cells = [c for r in (rmap.get("cells") or []) for c in r if c]
        n_cells = len(cells) or 1
        x_var = rmap.get("x_variable")
        y_var = rmap.get("y_variable")

        row.update({
            "map": f"{x_var} × {y_var}" if x_var and y_var else None,
            "min_x_at_max_y": rmap.get("minimum_x_at_max_y"),
            "min_y_at_max_x": rmap.get("minimum_y_at_max_x"),
            "required_x_at_best_y": rmap.get("required_x_at_best_y"),
            "required_y_at_best_x": rmap.get("required_y_at_best_x"),
            "objective_trend": [
                rmap.get("objective_trend_x"),
                rmap.get("objective_trend_y"),
            ],
            "x_demand_direction": rmap.get("x_demand_direction"),
            "y_demand_direction": rmap.get("y_demand_direction"),
            "metric_min": rmap.get("metric_min"),
            "metric_max": rmap.get("metric_max"),
            "plateau_fraction": plateau,
            "feasible_cell_share": round(
                sum(1 for c in cells if c.get("feasible")) / n_cells, 3
            ),
            # Lower bound already feasible → true requirement lies below the searched range
            "x_lower_bound_binding": (
                rmap.get("minimum_x_at_max_y") == lower.get(x_var)
                if x_var and lower.get(x_var) is not None
                else None
            ),
            "y_lower_bound_binding": (
                rmap.get("minimum_y_at_max_x") == lower.get(y_var)
                if y_var and lower.get(y_var) is not None
                else None
            ),
            "frontier": rmap.get("frontier"),
            "fixed_parameters": rmap.get("fixed_parameters"),
        })
    else:
        row["plateau_fraction"] = None

    return row


def stats(values: list[float]) -> str:
    clean = [v for v in values if v is not None and isinstance(v, (int, float))]
    if not clean:
        return "—"
    if len(clean) < 2:
        return f"{clean[0]:.4f}"
    return f"{statistics.mean(clean):.4f} ± {statistics.stdev(clean):.4f}"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Summarize completed optimization jobs from the running API."
    )
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=8, help="Parallel detail fetches")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    with httpx.Client(base_url=args.base_url, timeout=120.0) as client:
        details = fetch_details(client, max_workers=args.workers)

    if not details:
        print("No completed optimization jobs found.")
        (args.out / "optimization-summary.md").write_text(
            "# No completed jobs\n", encoding="utf-8"
        )
        (args.out / "optimization-summary.json").write_text(
            json.dumps({"runs": [], "curves": []}, indent=2), encoding="utf-8"
        )
        return

    rows = [summarize(d) for d in details]

    # --- Markdown table ---
    header = (
        "| name | verdict | best | objective | violation | "
        "upper feasible (viol) | min x @ max y | min y @ max x | "
        "x lower binding | plateau |"
    )
    sep = "|---|---|---|---|---|---|---|---|---|---|"
    lines: list[str] = [header, sep]

    for r in rows:
        lines.append(
            f'| {r["name"]} | {r["verdict"]} | {r["best"]} | {r["best_objective"]} | '
            f'{r["best_violation"]} | {r["upper_feasible"]} ({r["upper_violation"]}) | '
            f'{r.get("min_x_at_max_y")} | {r.get("min_y_at_max_x")} | '
            f'{r.get("x_lower_bound_binding")} | {r["plateau_fraction"]} |'
        )
        pf = r.get("plateau_fraction")
        if pf is not None and pf > 0.2:
            lines.append(
                f'|  ⚠ {r["name"]}: {pf:.0%} of map cells share the minimum; '
                f"the reported optimum is arbitrary |||||||||"
            )

    # --- Seed groups (generalised over any parameters present) ---
    seeds: dict[str, list[dict]] = defaultdict(list)
    for d, r in zip(details, rows):
        seeds[group_key(d.get("request") or {}, GROUP_EXCLUDE)].append(r)

    lines += ["", "## Seed groups", ""]
    # Dynamic columns from parameters that actually appear
    param_cols = [
        k for k in PARAM_KEYS_OF_INTEREST
        if any(k in (g.get("best") or {}) for group in seeds.values() for g in group)
    ]
    seed_header = "| first name | n | " + " | ".join(param_cols) + " | objective |"
    seed_sep = "|---|" + "---|" * (len(param_cols) + 2)
    lines += [seed_header, seed_sep]

    for group in seeds.values():
        if len(group) < 2:
            continue
        cells = [group[0]["name"], str(len(group))]
        for pk in param_cols:
            vals = [g["best"].get(pk) for g in group if pk in (g.get("best") or {})]
            cells.append(stats(vals))  # type: ignore[arg-type]
        objs = [g["best_objective"] for g in group if g.get("best_objective") is not None]
        cells.append(stats(objs))  # type: ignore[arg-type]
        lines.append("| " + " | ".join(cells) + " |")

    # --- Convergence curves ---
    curves: dict[str, list[dict]] = defaultdict(list)
    for d in details:
        hist = d.get("history") or []
        curves[group_key(d.get("request") or {}, CURVE_EXCLUDE)].append({
            "name": d.get("name"),
            "multiplier": (d.get("request") or {}).get("population_multiplier"),
            "seed": (d.get("request") or {}).get("seed"),
            "curve": [
                (h.get("evaluation_count"), h.get("penalised_objective"))
                for h in hist
                if isinstance(h, dict)
            ],
        })

    md_path = args.out / "optimization-summary.md"
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    json_path = args.out / "optimization-summary.json"
    json_path.write_text(
        json.dumps({"runs": rows, "curves": list(curves.values())}, indent=2, default=str),
        encoding="utf-8",
    )

    print("\n".join(lines))
    print(f"\nWrote {md_path} and {json_path} ({len(rows)} runs)")


if __name__ == "__main__":
    main()
```

