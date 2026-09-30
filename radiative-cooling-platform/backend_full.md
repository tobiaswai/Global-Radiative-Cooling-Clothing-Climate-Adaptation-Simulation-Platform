# Complete Backend Source Code (`backend/` - Excluding `data/`)

## Directory Structure
```text
backend/alembic.ini
backend/alembic/README
backend/alembic/env.py
backend/alembic/script.py.mako
backend/alembic/versions/18a914bf4989_stage2_material_version_parameter_.py
backend/alembic/versions/5c968a541440_stage2_material_version_parameter_.py
backend/alembic/versions/933e5fc5bb27_create_simulation_jobs.py
backend/alembic/versions/9e0b460c56c3_add_global_batch_analysis_tables.py
backend/alembic/versions/a1f4c2d9e7b3_stage4_material_library_links.py
backend/alembic/versions/b83aed15c819_add_material_version_and_spectrum_tables.py
backend/alembic/versions/c7d2e9f4a1b8_stage3_material_version_clothing_area_factor.py
backend/alembic/versions/df85b07c9163_add_stage_4_4_checkpoint_and_analytics_.py
backend/alembic/versions/e4ee64441802_add_stage_4_2_exposure_and_retry_fields.py
backend/app/__init__.py
backend/app/api/__init__.py
backend/app/api/benchmarks.py
backend/app/api/errors.py
backend/app/api/global_batches.py
backend/app/api/materials.py
backend/app/api/model.py
backend/app/api/router.py
backend/app/api/routes/simulation_events.py
backend/app/api/routes/simulation_jobs.py
backend/app/api/simulations.py
backend/app/api/weather.py
backend/app/core/__init__.py
backend/app/core/cities.py
backend/app/core/config.py
backend/app/core/cors.py
backend/app/core/runtime.py
backend/app/db/__init__.py
backend/app/db/base.py
backend/app/db/session.py
backend/app/main.py
backend/app/models/__init__.py
backend/app/models/global_batch.py
backend/app/models/material.py
backend/app/models/simulation_job.py
backend/app/schemas/__init__.py
backend/app/schemas/environment.py
backend/app/schemas/global_batch.py
backend/app/schemas/job.py
backend/app/schemas/material.py
backend/app/schemas/provenance.py
backend/app/schemas/simulation.py
backend/app/schemas/weather.py
backend/app/services/__init__.py
backend/app/services/annual_sampling.py
backend/app/services/body.py
backend/app/services/climate_adaptation.py
backend/app/services/climate_analytics.py
backend/app/services/clothing.py
backend/app/services/environment_model.py
backend/app/services/execution_profile.py
backend/app/services/exposure_statistics.py
backend/app/services/gagge_benchmark.py
backend/app/services/gagge_reference.py
backend/app/services/global_batch_export.py
backend/app/services/global_batch_service.py
backend/app/services/job_service.py
backend/app/services/material_fields.py
backend/app/services/material_resolution.py
backend/app/services/model_parameters.py
backend/app/services/reproducibility.py
backend/app/services/result_export.py
backend/app/services/result_storage.py
backend/app/services/spectrum_parser.py
backend/app/services/two_node.py
backend/app/services/weather.py
backend/app/services/weather_interpolation.py
backend/app/services/weather_quality.py
backend/app/services/weather_simulation.py
backend/app/utils/date_defaults.py
backend/app/worker/__init__.py
backend/app/worker/celery_app.py
backend/app/worker/tasks.py
backend/chinese-text-inventory.txt
backend/coverage.xml
backend/docs/acceptance/legacy-stage-3-two-node-prototype/energy-residual.txt
backend/docs/acceptance/legacy-stage-3-two-node-prototype/pytest-all.txt
backend/docs/acceptance/stage-2/golden-refresh.md
backend/docs/acceptance/stage-3-reference-comparison/golden-refresh.md
backend/docs/acceptance/stage-3-reference-comparison/pytest-all.txt
backend/docs/acceptance/stage-4-material-library/pytest-all.txt
backend/docs/decisions/0001-body-surface-area.md
backend/docs/decisions/0002-gagge-controllers.md
backend/docs/decisions/0003-clothing-surface-balance.md
backend/docs/decisions/0004-material-library-provenance.md
backend/docs/environment-assumptions.md
backend/docs/model-parameters.md
backend/package-lock.json
backend/package.json
backend/pyproject.toml
backend/requirements.txt
backend/run-tests.sh
backend/scripts/capture_weather_fixture.py
backend/scripts/export_openapi.py
backend/scripts/render_model_parameters_doc.py
backend/tests/__init__.py
backend/tests/conftest.py
backend/tests/core/test_numba_cache_integration.py
backend/tests/core/test_runtime.py
backend/tests/fixtures/dubai_2h/expected_results.json
backend/tests/fixtures/dubai_2h/open_meteo_payload.json
backend/tests/fixtures/dubai_2h/open_meteo_payload.sha256
backend/tests/fixtures/dubai_2h/request.json
backend/tests/fixtures/dubai_2h/request_params.json
backend/tests/test_api.py
backend/tests/test_body.py
backend/tests/test_cities.py
backend/tests/test_climate_adaptation.py
backend/tests/test_climate_scenarios.py
backend/tests/test_clothing.py
backend/tests/test_cors.py
backend/tests/test_environment_model.py
backend/tests/test_exposure_statistics.py
backend/tests/test_gagge_benchmark.py
backend/tests/test_gagge_reference.py
backend/tests/test_global_batch_geojson.py
backend/tests/test_golden_dubai_2h.py
backend/tests/test_job_service.py
backend/tests/test_material_fields.py
backend/tests/test_material_resolution.py
backend/tests/test_materials_api.py
backend/tests/test_model_parameters.py
backend/tests/test_parameter_participation.py
backend/tests/test_physics.py
backend/tests/test_result_export.py
backend/tests/test_result_storage.py
backend/tests/test_route_registration.py
backend/tests/test_spectrum_parser.py
backend/tests/test_stage_4_2_export.py
backend/tests/test_stage_4_2_exposure.py
backend/tests/test_stage_4_2_sampling.py
backend/tests/test_stage_4_3_estimate.py
backend/tests/test_stage_4_3_sampling.py
backend/tests/test_stage_4_3_weather_slice.py
backend/tests/test_stage_4_4_analytics.py
backend/tests/test_stage_4_4_checkpoint.py
backend/tests/test_two_node.py
backend/tests/test_weather_api.py
backend/tests/test_weather_interpolation.py
backend/tests/test_weather_quality.py
backend/tests/test_weather_service.py
backend/tests/test_weather_simulation.py
backend/tests/test_worker_tasks.py
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

from celery import group
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    status,
)
from fastapi.responses import Response
from sqlalchemy import (
    func,
    or_,
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
from app.db.session import get_db
from app.models.global_batch import (
    GlobalBatchJob,
    GlobalCityResult,
)
from app.schemas.global_batch import (
    GlobalBatchCreate,
    GlobalBatchDetail,
    GlobalBatchEstimateResponse,
    GlobalBatchListResponse,
    GlobalBatchResponse,
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
)
from app.worker.celery_app import celery_app
from app.worker.tasks import (
    run_global_city_analysis_task,
)

from app.services.material_resolution import (
    linked_material_version_ids,
    resolve_request_materials,
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

    queue_name = resolve_queue_name(
        request
    )

    batch = GlobalBatchJob(
        status="queued",
        stage="creating_city_tasks",
        progress=0,
        total_city_count=len(cities),
        request_json=request.model_dump(
            mode="json"
        ),
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


@router.get(
    "/{batch_id}",
    response_model=GlobalBatchDetail,
)
def get_global_batch(
    batch_id: str,
    session: Session = Depends(get_db),
) -> GlobalBatchDetail:
    batch = load_batch(
        session,
        batch_id,
    )

    if batch is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Global batch not found",
        )

    return batch_to_detail(batch)


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

    request = GlobalBatchCreate.model_validate(
        batch.request_json
    )

    queue_name = resolve_queue_name(
        request
    )

    now = utc_now()

    for result in failed_results:
        checkpoint_available = bool(
            result.monthly_json
        )

        result.status = "queued"
        result.stage = "queued_for_retry"
        result.progress = 0
        result.retry_count += 1

        result.error_message = None
        result.completed_at = None
        result.last_heartbeat_at = None

        result.climate_adaptation_rate_percent = None
        result.exposure_coverage_percent = None

        result.annual_average_skin_improvement_c = None
        result.annual_average_core_improvement_c = None
        result.maximum_skin_improvement_c = None
        result.effective_cooling_hours = None

        result.sampled_day_count = None
        result.eligible_sample_count = None
        result.evaluated_weighted_days = None
        result.beneficial_weighted_days = None

        result.skin_improvement_p50_c = None
        result.skin_improvement_p90_c = None
        result.skin_improvement_p95_c = None

        result.core_improvement_p50_c = None
        result.core_improvement_p90_c = None
        result.core_improvement_p95_c = None

        result.heatwave_event_count = None
        result.longest_heatwave_days = None
        result.analytics_json = None

        if request.resume_from_checkpoint:
            result.resumed_from_checkpoint = (
                checkpoint_available
            )
        else:
            result.monthly_json = None
            result.completed_month_count = 0
            result.last_checkpoint_month = None
            result.resumed_from_checkpoint = False
            result.started_at = None

    batch.status = "running"
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
    APIRouter,
    Depends,
    File,
    Form,
    HTTPException,
    Query,
    UploadFile,
    status,
)
from sqlalchemy import (
    func,
    select,
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import (
    Session,
    selectinload,
)

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


@router.patch(
    "/{material_id}",
    response_model=MaterialResponse,
)
def update_material(
    material_id: str,
    request: MaterialUpdate,
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

    update_data = request.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(material, field, value)

    session.commit()

    updated = load_material(
        session,
        material_id,
    )

    return MaterialResponse.model_validate(
        updated
    )


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
```

### File: `backend/app/api/router.py`
```python
# app/api/router.py
"""Top-level API router. The only place routers are aggregated."""

from fastapi import APIRouter

from app.api import (
    benchmarks,
    global_batches,
    materials,
    model,
    simulations,
    weather,
)


api_router = APIRouter()

for router in (
    simulations.router,
    benchmarks.router,
    weather.router,
    materials.router,
    global_batches.router,
    model.router,
):
    api_router.include_router(router)
```

### File: `backend/app/api/routes/simulation_events.py`
```python
"""Simulation event streaming API routes."""

from fastapi import APIRouter


router = APIRouter()

# Move existing SSE decorators and handlers here unchanged.
```

### File: `backend/app/api/routes/simulation_jobs.py`
```python
"""Simulation job API routes."""

from fastapi import APIRouter


router = APIRouter()

# Move existing job decorators and handlers here unchanged.
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
from app.services.two_node import simulate_material
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
        model_version="0.1.0",
        city=request.city,
        duration_minutes=request.duration_minutes,
        control=control_result,
        radiative_cooling=rc_result,
        summary=SimulationSummary(
            final_skin_temperature_improvement_c=round(
                final_skin_improvement,
                4,
            ),
            final_core_temperature_improvement_c=round(
                final_core_improvement,
                4,
            ),
            average_skin_temperature_improvement_c=round(
                control_skin_average - rc_skin_average,
                4,
            ),
        ),
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

    return SimulationJobListResponse(
        items=[
            job_to_response(job)
            for job in jobs
        ],
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

    return job_to_detail(job)

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
    version="0.3.0",
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
from app.models.global_batch import (
    GlobalBatchJob,
    GlobalCityResult,
)
from app.models.material import (
    Material,
    MaterialSpectrum,
    MaterialVersion,
)
from app.models.simulation_job import SimulationJob

__all__ = [
    "GlobalBatchJob",
    "GlobalCityResult",
    "Material",
    "MaterialSpectrum",
    "MaterialVersion",
    "SimulationJob",
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
```

### File: `backend/app/schemas/__init__.py`
```python

```

### File: `backend/app/schemas/environment.py`
```python
"""Explicit rules for deriving boundary conditions that ERA5 does not
provide: mean radiant temperature, sky temperature, sky view factor and
body-height wind (Stage 2).

Defaults reproduce the Stage 1 empirical estimates exactly, so introducing
this model does not change existing results.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


MeanRadiantTemperatureMethod = Literal[
    "air_plus_solar_linear",  # T_mrt = T_air + min(cap, gain * GHI)
    "equal_to_air",           # T_mrt = T_air (shaded / indoor-like)
]

SkyTemperatureMethod = Literal[
    "humidity_offset",  # T_sky = T_air - (base + range * (1 - RH))
    "fixed_offset",     # T_sky = T_air - fixed_offset
    "swinbank",         # T_sky[K] = 0.0552 * T_air[K]^1.5 (clear sky)
]


class EnvironmentAssumptions(BaseModel):
    model_config = ConfigDict(extra="forbid")

    mean_radiant_temperature_method: MeanRadiantTemperatureMethod = Field(
        default="air_plus_solar_linear",
        json_schema_extra={"source_type": "assumed", "reference": "Stage 1 prototype"},
    )
    solar_mrt_gain_k_per_w_m2: float = Field(
        default=0.012, ge=0.0, le=0.05,
        description="MRT rise per W/m^2 of GHI (air_plus_solar_linear only)",
        json_schema_extra={"source_type": "assumed", "reference": "Stage 1 prototype"},
    )
    solar_mrt_gain_cap_k: float = Field(
        default=15.0, ge=0.0, le=40.0,
        description="Upper bound of the solar MRT rise",
        json_schema_extra={"source_type": "assumed", "reference": "Stage 1 prototype"},
    )

    sky_temperature_method: SkyTemperatureMethod = Field(
        default="humidity_offset",
        json_schema_extra={"source_type": "assumed", "reference": "Stage 1 prototype"},
    )
    sky_offset_base_k: float = Field(
        default=5.0, ge=0.0, le=40.0,
        description="humidity_offset: depression at 100 % RH",
        json_schema_extra={"source_type": "assumed", "reference": "Stage 1 prototype"},
    )
    sky_offset_humidity_range_k: float = Field(
        default=10.0, ge=0.0, le=40.0,
        description="humidity_offset: additional depression at 0 % RH",
        json_schema_extra={"source_type": "assumed", "reference": "Stage 1 prototype"},
    )
    fixed_sky_offset_k: float = Field(
        default=15.0, ge=0.0, le=50.0,
        description="fixed_offset: T_air - T_sky",
        json_schema_extra={"source_type": "assumed", "reference": "Stage 1 prototype"},
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
        json_schema_extra={"source_type": "assumed", "reference": "Stage 1 prototype"},
    )

    def describe(self) -> list[str]:
        """Human-readable summary written into ``environment_model_note``."""
        if self.mean_radiant_temperature_method == "air_plus_solar_linear":
            mrt = (
                f"T_mrt = T_air + min({self.solar_mrt_gain_cap_k} K, "
                f"{self.solar_mrt_gain_k_per_w_m2} K/(W/m^2) * GHI)"
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
        else:
            sky = "T_sky[K] = 0.0552 * T_air[K]^1.5 (Swinbank 1963, clear sky)"

        return [
            "Air temperature, relative humidity, 10 m wind speed and GHI are "
            "taken from ERA5 via Open-Meteo.",
            mrt,
            sky,
            f"Sky view factor = {self.sky_view_factor}",
            f"Body-height wind = {self.wind_speed_scaling_factor} * ERA5 10 m wind",
        ]
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
    maximum_air_temperature_c: float

    mean_solar_radiation_w_m2: float
    maximum_solar_radiation_w_m2: float

    exposure_eligible: bool
    beneficial: bool

    average_skin_improvement_c: float
    final_skin_improvement_c: float
    average_core_improvement_c: float
    maximum_skin_improvement_c: float

    weather_from_cache: bool

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
)


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
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=200,
    )

    description: str | None = None
    institution: str | None = None
    is_archived: bool | None = None


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

    source_type: str
    is_archived: bool
    created_at: datetime


class MaterialVersionListResponse(BaseModel):
    items: list[MaterialVersionListItem]
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
    "infrared_transmittance",
    "projected_solar_area_factor",
    "absorbed_solar_to_body_fraction",
)

MATERIAL_PHYSICAL_FIELDS = frozenset(MATERIAL_PHYSICAL_FIELD_ORDER)


def validate_parameter_source_keys(
    sources: Mapping[str, object] | None,
) -> None:
    """Reject provenance entries that do not name a physical material field."""
    if not sources:
        return

    unknown = set(sources) - MATERIAL_PHYSICAL_FIELDS

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

class EnvironmentInput(BaseModel):
    air_temperature_c: float = Field(
        default=38.0,
        ge=-50,
        le=70,
    )
    mean_radiant_temperature_c: float = Field(
        default=45.0,
        ge=-50,
        le=100,
    )
    sky_temperature_c: float | None = Field(
        default=None,
        ge=-100,
        le=70,
    )
    relative_humidity_percent: float = Field(
        default=40.0,
        ge=0,
        le=100,
    )
    wind_speed_m_s: float = Field(
        default=1.5,
        ge=0,
        le=30,
    )
    solar_radiation_w_m2: float = Field(
        default=800.0,
        ge=0,
        le=1500,
    )
    sky_view_factor: float = Field(
        default=0.5,
        ge=0,
        le=1,
    )


class PersonInput(BaseModel):
    met: float = Field(default=2.6, ge=0.7, le=10)

    body_surface_area_m2: float = Field(default=1.8, ge=1.0, le=3.0)

    # Stage 3. Heat capacities are derived from body mass (ADR 0001).
    # 70 kg / 1.8 m^2 reproduces the Gagge two-node lumped value.
    body_mass_kg: float = Field(default=70.0, ge=30.0, le=200.0)

    initial_core_temperature_c: float = Field(default=36.8, ge=34, le=40)
    initial_skin_temperature_c: float = Field(default=33.7, ge=20, le=40)

MATERIAL_PHYSICAL_FIELDS = frozenset(
    {
        "clothing_insulation_clo",
        "evaporative_resistance_m2pa_w",
        "clothing_area_factor",
        "solar_reflectance",
        "solar_transmittance",
        "infrared_emissivity",
        "infrared_transmittance",
        "projected_solar_area_factor",
        "absorbed_solar_to_body_fraction",
    }
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
        description="Longwave emissivity of the outer surface (8-13 um)",
        json_schema_extra={"unit": "-"},
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
            "Fraction of solar radiation absorbed by the textile that reaches "
            "the skin node (ADR 0003)"
        ),
        json_schema_extra={"unit": "-"},
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
    maximum_core_step_c: float
    maximum_skin_step_c: float
    solver_function_evaluations: int
    
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

class BodyThermalSummary(BaseModel):
    """Heat capacities derived from PersonInput (Stage 3, ADR 0001)."""

    body_mass_kg: float
    body_surface_area_m2: float
    core_heat_capacity_j_m2k: float
    skin_heat_capacity_j_m2k: float

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
    compute_exposure_window_statistics,
    time_weighted_mean,
)
from app.services.weather import (
    get_historical_weather_range,
    slice_weather_time_series,
)
from app.services.weather_quality import WeatherDataError
from app.services.weather_simulation import (
    execute_weather_simulation_with_weather,
)


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
) -> dict:
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
            city=city,
            start_time_local=month_start,
            end_time_local=prefetch_end,
            padding_hours=1,
            require_window_coverage=False,
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

            paired_points = list(
                zip(
                    simulation.control.time_series,
                    simulation.radiative_cooling.time_series,
                    strict=True,
                )
            )

            if not paired_points:
                raise RuntimeError("Simulation returned no paired points")

            minutes = [control.minute for control, _ in paired_points]

            skin_improvements = [
                control.skin_temperature_c - radiative.skin_temperature_c
                for control, radiative in paired_points
            ]

            core_improvements = [
                control.core_temperature_c - radiative.core_temperature_c
                for control, radiative in paired_points
            ]

            # Exposure statistics strictly over [start, start + duration].
            exposure = compute_exposure_window_statistics(sample_weather)

            average_skin_improvement_c = time_weighted_mean(
                minutes, skin_improvements
            )
            average_core_improvement_c = time_weighted_mean(
                minutes, core_improvements
            )
            maximum_skin_improvement_c = max(skin_improvements)

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
                        simulation.summary.final_skin_temperature_improvement_c,
                        4,
                    ),
                    average_core_improvement_c=round(
                        average_core_improvement_c, 4
                    ),
                    maximum_skin_improvement_c=round(
                        maximum_skin_improvement_c, 4
                    ),
                    weather_from_cache=month_weather.source.from_cache,
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
        "skin_improvement_p50_c": analytics["skin_improvement_p50_c"],
        "skin_improvement_p90_c": analytics["skin_improvement_p90_c"],
        "skin_improvement_p95_c": analytics["skin_improvement_p95_c"],
        "core_improvement_p50_c": analytics["core_improvement_p50_c"],
        "core_improvement_p90_c": analytics["core_improvement_p90_c"],
        "core_improvement_p95_c": analytics["core_improvement_p95_c"],
        "heatwave_analysis_available": analytics["heatwave_analysis_available"],
        "heatwave_event_count": analytics["heatwave_event_count"],
        "longest_heatwave_days": analytics["longest_heatwave_days"],
        "heatwave_events": analytics["heatwave_events"],
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
    temperatures = [
        sample.maximum_air_temperature_c
        for sample in samples
    ]

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
        qualifies = (
            sample.maximum_air_temperature_c
            >= temperature_threshold_c
        )

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

    heatwave_available = (
        request.enable_heatwave_analysis
        and request.analysis_resolution == "daily"
        and request.daily_stride_days == 1
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
        "heatwave_analysis_available": (
            heatwave_available
        ),
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


def assumptions_applied(clothing: ClothingResistances) -> list[str]:
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
        "absorbed solar radiation is deposited on the skin node via "
        "absorbed_solar_to_body_fraction and does not enter the clothing "
        "surface balance (ADR 0003)"
    )

    return notes
```

### File: `backend/app/services/environment_model.py`
```python
"""Derive model boundary conditions from ERA5 variables (Stage 2)."""

from __future__ import annotations

from app.schemas.environment import EnvironmentAssumptions
from app.schemas.simulation import EnvironmentInput
from app.services.model_parameters import get_parameter_value


SWINBANK_COEFFICIENT = get_parameter_value("swinbank_coefficient")
KELVIN_OFFSET = 273.15


def derive_environment(
    *,
    air_temperature_c: float,
    relative_humidity_percent: float,
    wind_speed_m_s: float,
    ghi_w_m2: float,
    assumptions: EnvironmentAssumptions,
) -> EnvironmentInput:
    air = float(air_temperature_c)
    ghi = max(0.0, float(ghi_w_m2))
    relative_humidity = min(100.0, max(0.0, float(relative_humidity_percent)))
    wind = max(0.0, float(wind_speed_m_s)) * assumptions.wind_speed_scaling_factor

    if assumptions.mean_radiant_temperature_method == "air_plus_solar_linear":
        mean_radiant = air + min(
            assumptions.solar_mrt_gain_cap_k,
            assumptions.solar_mrt_gain_k_per_w_m2 * ghi,
        )
    else:
        mean_radiant = air

    if assumptions.sky_temperature_method == "humidity_offset":
        sky = air - (
            assumptions.sky_offset_base_k
            + assumptions.sky_offset_humidity_range_k
            * (1.0 - relative_humidity / 100.0)
        )
    elif assumptions.sky_temperature_method == "fixed_offset":
        sky = air - assumptions.fixed_sky_offset_k
    else:
        sky = SWINBANK_COEFFICIENT * (air + KELVIN_OFFSET) ** 1.5 - KELVIN_OFFSET

    return EnvironmentInput(
        air_temperature_c=air,
        mean_radiant_temperature_c=mean_radiant,
        sky_temperature_c=sky,
        relative_humidity_percent=relative_humidity,
        wind_speed_m_s=wind,
        solar_radiation_w_m2=ghi,
        sky_view_factor=assumptions.sky_view_factor,
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
from datetime import datetime

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
        [(p.timestamp - origin).total_seconds() for p in weather.points],
        dtype=float,
    )

    start_s = (window_start - origin).total_seconds()
    end_s = (window_end - origin).total_seconds()

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
        }
    )
    alignment.append(
        f"infrared_emissivity set to {REFERENCE_CLOTHING_EMISSIVITY} and "
        "infrared_transmittance to 0 (fixed in the reference)"
    )
    alignment.append(
        "evaporative_resistance_m2pa_w and clothing_area_factor derived from clo "
        "(the reference accepts clo only)"
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
        position="standing",
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
        position="standing",
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
            "mean_solar_radiation_w_m2",
            "maximum_solar_radiation_w_m2",
            "exposure_eligible",
            "beneficial",
            "average_skin_improvement_c",
            "final_skin_improvement_c",
            "average_core_improvement_c",
            "maximum_skin_improvement_c",
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
                                "maximum_air_"
                                "temperature_c"
                            )
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
                        sample.get(
                            "weather_from_cache"
                        ),
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

from app.models.global_batch import (
    GlobalBatchJob,
    GlobalCityResult,
)
from app.schemas.global_batch import (
    GlobalBatchDetail,
    GlobalBatchResponse,
    GlobalCityResultResponse,
)


TERMINAL_CITY_STATUSES = {
    "completed",
    "failed",
    "cancelled",
}


def city_result_to_response(
    result: GlobalCityResult,
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
    )


def batch_to_response(
    batch: GlobalBatchJob,
) -> GlobalBatchResponse:
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
    )


def batch_to_detail(
    batch: GlobalBatchJob,
) -> GlobalBatchDetail:
    return GlobalBatchDetail(
        **batch_to_response(batch).model_dump(),
        request=batch.request_json,
        city_results=[
            city_result_to_response(item)
            for item in batch.city_results
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


```

### File: `backend/app/services/job_service.py`
```python
from sqlalchemy.orm import Session

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


def job_to_response(
    job: SimulationJob,
) -> SimulationJobResponse:
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
    )


def job_to_detail(
    job: SimulationJob,
) -> SimulationJobDetail:
    return SimulationJobDetail(
        **job_to_response(job).model_dump(),
        request=WeatherSimulationRequest.model_validate(
            job.request_json
        ),
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
            absorbed_solar_to_body_fraction=(
                version.absorbed_solar_to_body_fraction
            ),
            material_version_id=version.id,
            source_type=version.source_type,
            source_reference=version.source_reference,
            parameter_sources=version.parameter_sources_json,
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


MODEL_PARAMETER_SET_VERSION = "3.0.0"

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

   # --- longwave radiation geometry ----------------------------------------
    _p("effective_radiation_area_ratio", 0.73, "-",
       "A_r / A_D: fraction of the DuBois area exchanging longwave radiation "
       "with the surroundings (standing person)",
       "literature",
       "Fanger (1970) Thermal Comfort, McGraw-Hill; " + ASHRAE_FUNDAMENTALS
       + " (0.70 seated, 0.73 standing); " + ASHRAE_55_SET,
       "Applied to the clothing surface emission and to skin emission "
       "transmitted through IR-transparent textiles. Posture is fixed at "
       "standing; a PersonInput.position field is Stage 4 work."),
    
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
# key). A changed constant value must bump ``mp.MODEL_VERSION`` instead.
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
    "(UPDATE_GOLDEN=1 pytest tests/test_golden_dubai_2h.py). "
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
            "regenerate it (python -m scripts.regenerate_golden)"
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
        # Stage 1 results stored before PR-2 carry no assumptions block.
        assumptions = EnvironmentAssumptions()
        
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
        if abs(value - actual["summary"][key]) > temperature_atol:
            differences.append(f"summary.{key}: {value} != {actual['summary'][key]}")

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
        raise ValueError(
            f"Row {row_number} spectrum file must contain at least two data points"
        )

    wavelengths = [
        point["wavelength_um"]
        for point in points
    ]

    for previous, current in zip(
        wavelengths,
        wavelengths[1:],
        strict=False,
    ):
        if current <= previous:
            raise ValueError(
                f"Row {row_number} wavelengths must be strictly increasing and unique"
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

### File: `backend/app/services/two_node.py`
```python
"""Two-node transient human thermal model.

Stage 3 changes
---------------
* Node heat capacities are derived from body mass and surface area
  (``body.body_heat_capacities``, ADR 0001).
* The clothing surface temperature is solved explicitly; the clothing area
  factor f_cl enters both the dry and the evaporative pathway (ADR 0003).
  The linearised radiative coefficient is gone.
* Thermoregulation uses the Gagge (1986) controllers: sweating on the
  mean-body warm signal with the exponential skin modifier, skin blood flow
  with vasodilation/vasoconstriction, a critical skin wettedness w_max and
  shivering (ADR 0002).
* Every numeric constant is bound from ``model_parameters`` (unit + source).
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from math import exp, sqrt

import numpy as np
from scipy.integrate import solve_ivp

from app.schemas.environment import EnvironmentAssumptions
from app.schemas.simulation import (
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
from app.services.weather_interpolation import WeatherInterpolator


# Bound once at import. The registry is the single source of truth.
SIGMA = _param("stefan_boltzmann_constant")
NATURAL_CONVECTION_MINIMUM = _param("natural_convection_minimum_coefficient")
FORCED_CONVECTION_COEFFICIENT = _param("forced_convection_coefficient")
SKIN_EMISSIVITY = _param("skin_emissivity")
RADIATION_AREA_RATIO = _param("effective_radiation_area_ratio")
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
MAGNUS_A = _param("magnus_a")
MAGNUS_B = _param("magnus_b")
MAGNUS_C = _param("magnus_c")

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
    absorbed_solar: float
    core_to_skin: float
    respiration: float
    metabolism: float
    skin_blood_flow: float
    clothing_surface_temperature_c: float

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


def saturation_vapor_pressure_kpa(temperature_c: float) -> float:
    return MAGNUS_A * exp(MAGNUS_B * temperature_c / (temperature_c + MAGNUS_C))


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
) -> float:
    """Solve (T_sk - T_cl)/R_cl = f_cl [h_c (T_cl - T_a) + eps sigma (T_cl^4 - T_env^4)].

    The residual is strictly decreasing and concave in T_cl, so Newton's method
    started at T_sk converges monotonically after at most one overshoot.
    """
    if clothing.dry_resistance_m2k_w < NUDE_RESISTANCE_THRESHOLD_M2K_W:
        return skin_temperature_c

    resistance = clothing.dry_resistance_m2k_w
    area_factor = clothing.area_factor
    skin_k = skin_temperature_c + KELVIN_OFFSET
    air_k = air_temperature_c + KELVIN_OFFSET

    t = skin_k

    radiative_factor = RADIATION_AREA_RATIO * emissivity * SIGMA

    for _ in range(SURFACE_TEMPERATURE_MAX_ITERATIONS):
        emission = radiative_factor * (t**4 - environment_fourth_k4)
        residual = (skin_k - t) / resistance - area_factor * (
            convection_coefficient * (t - air_k) + emission
        )
        derivative = -1.0 / resistance - area_factor * (
            convection_coefficient + 4.0 * radiative_factor * t**3
        )
        step = residual / derivative
        t -= step

        if abs(step) < SURFACE_TEMPERATURE_TOLERANCE_K:
            return t - KELVIN_OFFSET

    raise RuntimeError(
        "Clothing surface temperature iteration did not converge "
        f"(T_sk = {skin_temperature_c:.3f} C, T_a = {air_temperature_c:.3f} C)"
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
) -> HeatFluxes:
    if clothing is None:
        clothing = resolve_clothing(material)

    air_temperature_c = environment.air_temperature_c

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

    # --- dry heat: clothing surface balance ---------------------------------
    convection_coefficient = convection_coefficient_w_m2k(environment.wind_speed_m_s)
    environment_fourth = environment_radiant_fourth_power_k4(environment)

    surface_c = clothing_surface_temperature_c(
        skin_temperature_c=skin_temperature_c,
        air_temperature_c=air_temperature_c,
        environment_fourth_k4=environment_fourth,
        clothing=clothing,
        convection_coefficient=convection_coefficient,
        emissivity=material.infrared_emissivity,
    )
    surface_k = surface_c + KELVIN_OFFSET
    skin_k = skin_temperature_c + KELVIN_OFFSET

    convection = clothing.area_factor * convection_coefficient * (
        surface_c - air_temperature_c
    )

    longwave_surface = (
        clothing.area_factor
        * RADIATION_AREA_RATIO
        * material.infrared_emissivity
        * SIGMA
        * (surface_k**4 - environment_fourth)
    )

    # Skin emission transmitted directly through an IR-transparent textile.
    longwave_transmitted = (
        RADIATION_AREA_RATIO
        * clothing.infrared_transmittance
        * SKIN_EMISSIVITY
        * SIGMA
        * (skin_k**4 - environment_fourth)
    )

    longwave_radiation = longwave_surface + longwave_transmitted

    # --- solar (ADR 0003: deposited on the skin node) -----------------------
    solar_absorptance = clamp(
        1.0 - material.solar_reflectance - material.solar_transmittance, 0.0, 1.0
    )

    absorbed_solar = (
        solar_absorptance
        * environment.solar_radiation_w_m2
        * material.projected_solar_area_factor
        * material.absorbed_solar_to_body_fraction
    )

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
        absorbed_solar=absorbed_solar,
        core_to_skin=core_to_skin,
        respiration=respiration,
        metabolism=metabolism,
        skin_blood_flow=skin_blood_flow,
        clothing_surface_temperature_c=surface_c,
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
    capacities = body_heat_capacities(person)

    duration_seconds = duration_minutes * 60.0
    output_times = _output_times(duration_seconds, output_interval_minutes * 60.0)

    def derivatives(time_seconds: float, state: np.ndarray) -> list[float]:
        fluxes = calculate_fluxes(
            core_temperature_c=float(state[0]),
            skin_temperature_c=float(state[1]),
            environment=environment_at(float(time_seconds)),
            person=person,
            material=material,
            clothing=clothing,
        )

        core_storage = fluxes.metabolism - fluxes.respiration - fluxes.core_to_skin
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
        t_eval=output_times,
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

    time_series: list[TimeSeriesPoint] = []
    net_heat: list[float] = []

    for time_seconds, core_c, skin_c in zip(times, core_array, skin_array, strict=True):
        fluxes = calculate_fluxes(
            core_temperature_c=float(core_c),
            skin_temperature_c=float(skin_c),
            environment=environment_at(float(time_seconds)),
            person=person,
            material=material,
            clothing=clothing,
        )

        net_heat.append(fluxes.net_body_gain)

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
                clothing_surface_temperature_c=round(
                    fluxes.clothing_surface_temperature_c, 4
                ),
                skin_blood_flow_kg_h_m2=round(fluxes.skin_blood_flow, 4),
            )
        )

    diagnostics = _energy_diagnostics(
        times, core_array, skin_array, np.asarray(net_heat), solution.nfev, capacities
    )

    core_temperatures = [p.core_temperature_c for p in time_series]
    skin_temperatures = [p.skin_temperature_c for p in time_series]

    return ScenarioResult(
        material_name=material.name,
        time_series=time_series,
        final_core_temperature_c=core_temperatures[-1],
        final_skin_temperature_c=skin_temperatures[-1],
        peak_core_temperature_c=max(core_temperatures),
        peak_skin_temperature_c=max(skin_temperatures),
        diagnostics=diagnostics,
        clothing=ClothingSummary(
            dry_resistance_m2k_w=round(clothing.dry_resistance_m2k_w, 6),
            evaporative_resistance_m2pa_w=round(clothing.evaporative_resistance_m2pa_w, 4),
            evaporative_resistance_source=clothing.evaporative_resistance_source,
            infrared_transmittance=clothing.infrared_transmittance,
            clothing_area_factor=round(clothing.area_factor, 6),
            clothing_area_factor_source=clothing.area_factor_source,
        ),
        assumptions_applied=assumptions_applied(clothing),
        body=BodyThermalSummary(
            body_mass_kg=person.body_mass_kg,
            body_surface_area_m2=person.body_surface_area_m2,
            core_heat_capacity_j_m2k=round(capacities.core_j_m2k, 2),
            skin_heat_capacity_j_m2k=round(capacities.skin_j_m2k, 2),
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

    interpolator.ensure_covers(0.0, duration_minutes * 60.0)

    return _integrate(
        duration_minutes=duration_minutes,
        output_interval_minutes=output_interval_minutes,
        environment_at=interpolator.environment_at,
        person=person,
        material=material,
        failure_label="Weather-driven numerical solution failed",
    )
```

### File: `backend/app/services/weather.py`
```python
from __future__ import annotations

import hashlib
import json
from datetime import (
    date,
    datetime,
    timedelta,
    timezone,
)
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

from app.core.config import settings

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

CACHE_DIRECTORY = Path("data/cache/weather")


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
) -> dict[str, str | float]:
    return {
        "latitude": city.latitude,
        "longitude": city.longitude,
        "elevation": city.elevation_m,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "hourly": ",".join(HOURLY_VARIABLES),
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

    except (
        ConnectionError,
        TimeoutError,
    ):
        # Redis failure must not make weather
        # simulation completely unavailable.
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

    city_timezone = ZoneInfo(city.timezone)
    points: list[WeatherPoint] = []

    for index, timestamp_text in enumerate(times):
        # Open-Meteo 在指定 timezone 時返回當地時間，
        # 字符串本身通常不附帶 UTC offset。
        timestamp = datetime.fromisoformat(
            timestamp_text
        ).replace(tzinfo=city_timezone)

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
            )
        )

    return points


async def get_historical_weather(
    city: CityConfig,
    start_time_local: datetime,
    duration_minutes: int,
) -> WeatherTimeSeries:
    start_time = normalize_local_datetime(
        start_time_local,
        city.timezone,
    )

    end_time = start_time + timedelta(
        minutes=duration_minutes
    )

    return await get_historical_weather_range(
        city=city,
        start_time_local=start_time,
        end_time_local=end_time,
        padding_hours=1,
    )

async def get_historical_weather_range(
    *,
    city: CityConfig,
    start_time_local: datetime,
    end_time_local: datetime,
    padding_hours: int = 1,
    require_window_coverage: bool = True,
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
    )

    payload, from_cache = await request_open_meteo(params)

    raw_points = parse_weather_points(payload, city)

    cleaned_points, quality = normalize_timeline(raw_points)

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

    end_time = start_time + timedelta(minutes=duration_minutes)

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

from dataclasses import dataclass, field  # Stage 2: `field` added

import numpy as np

from app.schemas.environment import EnvironmentAssumptions  # Stage 2
from app.schemas.simulation import EnvironmentInput
from app.schemas.weather import WeatherTimeSeries
from app.services.environment_model import derive_environment  # Stage 2
from app.services.weather_quality import (
    WeatherInsufficientCoverageError,
)


BOUNDS_TOLERANCE_SECONDS = 1e-6


class InterpolationOutOfRangeError(WeatherInsufficientCoverageError):
    code = "WEATHER_INTERPOLATION_OUT_OF_RANGE"


@dataclass
class WeatherInterpolator:
    relative_seconds: np.ndarray
    temperatures: np.ndarray
    humidities: np.ndarray
    wind_speeds: np.ndarray
    ghi_values: np.ndarray

    # Stage 2. Must stay the last field: dataclass fields with defaults
    # cannot precede fields without defaults. Existing keyword-based
    # constructions (see tests/test_weather_interpolation.py) remain valid.
    assumptions: EnvironmentAssumptions = field(
        default_factory=EnvironmentAssumptions
    )

    def __post_init__(self) -> None:
        arrays = (
            self.relative_seconds,
            self.temperatures,
            self.humidities,
            self.wind_speeds,
            self.ghi_values,
        )

        lengths = {len(array) for array in arrays}

        if len(lengths) != 1:
            raise ValueError(
                "All interpolation arrays must have the same length"
            )

        if len(self.relative_seconds) < 2:
            raise WeatherInsufficientCoverageError(
                "Interpolation requires at least two weather points"
            )

        if not np.all(np.diff(self.relative_seconds) > 0):
            raise ValueError(
                "relative_seconds must be strictly increasing"
            )

    @property
    def t_min(self) -> float:
        return float(self.relative_seconds[0])

    @property
    def t_max(self) -> float:
        return float(self.relative_seconds[-1])

    def ensure_covers(
        self,
        start_seconds: float,
        end_seconds: float,
    ) -> None:
        """Raise unless ``[start_seconds, end_seconds]`` lies inside the data."""
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

    @classmethod
    def from_series(
        cls,
        weather: WeatherTimeSeries,
        *,
        check_requested_window: bool = True,
        assumptions: EnvironmentAssumptions | None = None,  # Stage 2
    ) -> "WeatherInterpolator":
        start_time = weather.requested_start_time

        relative_seconds = np.asarray(
            [
                (point.timestamp - start_time).total_seconds()
                for point in weather.points
            ],
            dtype=float,
        )

        interpolator = cls(
            relative_seconds=relative_seconds,
            temperatures=np.asarray(
                [p.air_temperature_c for p in weather.points], dtype=float
            ),
            humidities=np.asarray(
                [p.relative_humidity_percent for p in weather.points],
                dtype=float,
            ),
            wind_speeds=np.asarray(
                [p.wind_speed_m_s for p in weather.points], dtype=float
            ),
            ghi_values=np.asarray(
                [p.ghi_w_m2 for p in weather.points], dtype=float
            ),
            assumptions=assumptions or EnvironmentAssumptions(),  # Stage 2
        )

        if check_requested_window:
            required_end = (
                weather.requested_end_time - start_time
            ).total_seconds()

            interpolator.ensure_covers(0.0, required_end)

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

    def _interpolate(
        self,
        values: np.ndarray,
        elapsed_seconds: float,
    ) -> float:
        return float(
            np.interp(
                elapsed_seconds,
                self.relative_seconds,
                values,
            )
        )

    def environment_at(
        self,
        elapsed_seconds: float,
    ) -> EnvironmentInput:
        """Interpolate the ERA5 variables and derive the model boundary
        conditions according to ``self.assumptions``.

        Stage 2: the mean radiant temperature, sky temperature, sky view
        factor and wind scaling rules live in ``environment_model``; this
        method only interpolates.
        """
        self._check_bounds(elapsed_seconds)

        return derive_environment(
            air_temperature_c=self._interpolate(
                self.temperatures, elapsed_seconds
            ),
            relative_humidity_percent=self._interpolate(
                self.humidities, elapsed_seconds
            ),
            wind_speed_m_s=self._interpolate(
                self.wind_speeds, elapsed_seconds
            ),
            ghi_w_m2=self._interpolate(
                self.ghi_values, elapsed_seconds
            ),
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
        delta = current.timestamp - previous.timestamp

        if delta > tolerance:
            missing_steps = int(round(delta / step)) - 1

            gaps.append(
                WeatherGap(
                    start=previous.timestamp,
                    end=current.timestamp,
                    missing_steps=max(1, missing_steps),
                )
            )

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
from app.schemas.weather import (
    WeatherTimeSeries,
)
from app.services.two_node import (
    simulate_material_with_weather,
)
from app.services.weather import (
    get_historical_weather,
)

from app.services.model_parameters import build_model_metadata

MODEL_NAME = "Weather-driven transient two-node prototype"
MODEL_VERSION = "0.5.0"  # Stage 2: explicit Re,cl, IR transmittance, assumptions
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

    control_average = sum(
        p.skin_temperature_c for p in control_result.time_series
    ) / len(control_result.time_series)
    rc_average = sum(
        p.skin_temperature_c for p in rc_result.time_series
    ) / len(rc_result.time_series)

    return WeatherSimulationResponse(
        model_name=MODEL_NAME,
        model_version=MODEL_VERSION,
        city=city_name,
        duration_minutes=request.duration_minutes,
        control=control_result,
        radiative_cooling=rc_result,
        summary=SimulationSummary(
            final_skin_temperature_improvement_c=round(
                control_result.final_skin_temperature_c
                - rc_result.final_skin_temperature_c, 4
            ),
            final_core_temperature_improvement_c=round(
                control_result.final_core_temperature_c
                - rc_result.final_core_temperature_c, 4
            ),
            average_skin_temperature_improvement_c=round(
                control_average - rc_average, 4
            ),
        ),
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
        start_time_local=(
            request.start_time_local
        ),
        duration_minutes=(
            request.duration_minutes
        ),
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
    include=[
        "app.worker.tasks",
    ],
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
    ),
    task_default_queue="default",
    task_routes={
        "simulation.run_weather": {
            "queue": "default",
        },
        "global_batch.run_city": {
            "queue": "global_standard",
        },
    },
)
```

### File: `backend/app/worker/tasks.py`
```python
import asyncio
from datetime import (
    datetime,
    timezone,
)

from celery import Task

from app.db.session import SessionLocal
from app.models.global_batch import (
    GlobalBatchJob,
    GlobalCityResult,
)
from app.models.simulation_job import (
    SimulationJob,
)
from app.schemas.global_batch import (
    GlobalBatchCreate,
    MonthlyAdaptationResult,
)
from app.schemas.simulation import (
    WeatherSimulationRequest,
)
from app.services.annual_sampling import (
    estimate_sample_count,
)
from app.services.climate_adaptation import (
    analyze_city_climate_adaptation,
)
from app.services.global_batch_service import (
    refresh_batch_status,
)
from app.services.result_storage import (
    save_simulation_result,
)
from app.services.weather_simulation import (
    execute_weather_simulation,
)
from app.worker.celery_app import (
    celery_app,
)


class JobCancelledError(Exception):
    pass


class GlobalBatchCancelledError(Exception):
    pass


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def update_job(
    job_id: str,
    **values: object,
) -> None:
    with SessionLocal() as session:
        job = session.get(
            SimulationJob,
            job_id,
        )

        if job is None:
            raise RuntimeError(
                f"Simulation task not found:{job_id}"
            )

        for field, value in values.items():
            setattr(job, field, value)

        session.commit()


def ensure_not_cancelled(
    job_id: str,
) -> None:
    with SessionLocal() as session:
        job = session.get(
            SimulationJob,
            job_id,
        )

        if job is None:
            raise RuntimeError(
                f"Simulation task not found:{job_id}"
            )

        if job.status in {
            "cancelling",
            "cancelled",
        }:
            raise JobCancelledError()


@celery_app.task(
    bind=True,
    name="simulation.run_weather",
    acks_late=True,
)
def run_weather_simulation_task(
    self: Task,
    job_id: str,
) -> dict:
    try:
        with SessionLocal() as session:
            job = session.get(
                SimulationJob,
                job_id,
            )

            if job is None:
                raise RuntimeError(
                    f"Simulation task not found:{job_id}"
                )

            request = WeatherSimulationRequest.model_validate(
                job.request_json
            )

        update_job(
            job_id,
            status="running",
            stage="initializing",
            progress=2,
            started_at=utc_now(),
            error_message=None,
        )

        def report(
            progress: int,
            stage: str,
        ) -> None:
            ensure_not_cancelled(job_id)

            update_job(
                job_id,
                status="running",
                stage=stage,
                progress=progress,
            )

            self.update_state(
                state="PROGRESS",
                meta={
                    "job_id": job_id,
                    "progress": progress,
                    "stage": stage,
                },
            )

        result = asyncio.run(
            execute_weather_simulation(
                request=request,
                progress_callback=report,
            )
        )

        ensure_not_cancelled(job_id)

        update_job(
            job_id,
            stage="saving_result",
            progress=95,
        )

        result_path = save_simulation_result(
            job_id=job_id,
            result=result,
        )

        update_job(
            job_id,
            status="completed",
            stage="completed",
            progress=100,
            summary_json=result.summary.model_dump(
                mode="json"
            ),
            result_path=str(result_path),
            completed_at=utc_now(),
        )

        return {
            "job_id": job_id,
            "status": "completed",
        }

    except JobCancelledError:
        update_job(
            job_id,
            status="cancelled",
            stage="cancelled",
            completed_at=utc_now(),
        )

        return {
            "job_id": job_id,
            "status": "cancelled",
        }

    except Exception as error:
        update_job(
            job_id,
            status="failed",
            stage="failed",
            error_message=str(error)[:4000],
            completed_at=utc_now(),
        )
        raise


def ensure_global_batch_not_cancelled(
    batch_id: str,
) -> None:
    with SessionLocal() as session:
        batch = session.get(
            GlobalBatchJob,
            batch_id,
        )

        if batch is None:
            raise RuntimeError(
                f"Global batch not found: {batch_id}"
            )

        if batch.status in {
            "cancelling",
            "cancelled",
        }:
            raise GlobalBatchCancelledError()


@celery_app.task(
    bind=True,
    name="global_batch.run_city",
    acks_late=True,
)
def run_global_city_analysis_task(
    self: Task,
    city_result_id: str,
) -> dict:
    batch_id: str | None = None

    try:
        with SessionLocal() as session:
            city_result = session.get(
                GlobalCityResult,
                city_result_id,
            )

            if city_result is None:
                raise RuntimeError(
                    "Global city result not found: "
                    f"{city_result_id}"
                )

            batch = session.get(
                GlobalBatchJob,
                city_result.batch_id,
            )

            if batch is None:
                raise RuntimeError(
                    "Global batch not found: "
                    f"{city_result.batch_id}"
                )

            batch_id = batch.id

            request = GlobalBatchCreate.model_validate(
                batch.request_json
            )

            city_id = city_result.city_id

            initial_monthly_results: list[
                MonthlyAdaptationResult
            ] = []

            if (
                request.resume_from_checkpoint
                and city_result.monthly_json
            ):
                initial_monthly_results = [
                    MonthlyAdaptationResult.model_validate(
                        item
                    )
                    for item in city_result.monthly_json
                ]

            now = utc_now()

            city_result.status = "running"
            city_result.stage = "initializing"
            city_result.progress = 1
            city_result.started_at = (
                city_result.started_at or now
            )
            city_result.completed_at = None
            city_result.last_heartbeat_at = now
            city_result.error_message = None
            city_result.resumed_from_checkpoint = bool(
                initial_monthly_results
            )

            if batch.status in {
                "queued",
                "failed",
                "partial_completed",
            }:
                batch.status = "running"
                batch.stage = "analyzing_cities"
                batch.started_at = (
                    batch.started_at or now
                )
                batch.completed_at = None

            session.commit()

        if batch_id is None:
            raise RuntimeError(
                "Global batch ID was not initialized"
            )

        total_sample_count = max(
            1,
            estimate_sample_count(request),
        )

        def report(
            progress: int,
            stage: str,
        ) -> None:
            ensure_global_batch_not_cancelled(
                batch_id
            )

            heartbeat = utc_now()

            with SessionLocal() as session:
                result = session.get(
                    GlobalCityResult,
                    city_result_id,
                )

                if result is None:
                    raise RuntimeError(
                        "Global city result disappeared"
                    )

                result.status = "running"
                result.stage = stage
                result.progress = max(
                    0,
                    min(progress, 100),
                )
                result.last_heartbeat_at = heartbeat

                session.commit()

            self.update_state(
                state="PROGRESS",
                meta={
                    "batch_id": batch_id,
                    "city_result_id": city_result_id,
                    "city_id": city_id,
                    "progress": progress,
                    "stage": stage,
                    "last_heartbeat_at": (
                        heartbeat.isoformat()
                    ),
                },
            )

        def save_checkpoint(
            monthly_results: list[
                MonthlyAdaptationResult
            ],
            completed_month: int,
            completed_sample_count: int,
        ) -> None:
            ensure_global_batch_not_cancelled(
                batch_id
            )

            heartbeat = utc_now()

            checkpoint_progress = max(
                1,
                min(
                    92,
                    round(
                        completed_sample_count
                        / total_sample_count
                        * 92
                    ),
                ),
            )

            with SessionLocal() as session:
                result = session.get(
                    GlobalCityResult,
                    city_result_id,
                )

                if result is None:
                    raise RuntimeError(
                        "Global city result disappeared"
                    )

                result.monthly_json = [
                    monthly_result.model_dump(
                        mode="json"
                    )
                    for monthly_result in monthly_results
                ]

                result.completed_month_count = len(
                    monthly_results
                )
                result.last_checkpoint_month = (
                    completed_month
                )
                result.last_heartbeat_at = heartbeat
                result.stage = (
                    f"checkpoint_saved_"
                    f"{request.year}-"
                    f"{completed_month:02d}"
                )
                result.progress = max(
                    result.progress,
                    checkpoint_progress,
                )

                session.commit()

            self.update_state(
                state="PROGRESS",
                meta={
                    "batch_id": batch_id,
                    "city_result_id": city_result_id,
                    "city_id": city_id,
                    "progress": checkpoint_progress,
                    "stage": (
                        f"checkpoint_saved_"
                        f"{request.year}-"
                        f"{completed_month:02d}"
                    ),
                    "completed_month": completed_month,
                },
            )

        analysis = asyncio.run(
            analyze_city_climate_adaptation(
                city_id=city_id,
                request=request,
                progress_callback=report,
                checkpoint_callback=save_checkpoint,
                initial_monthly_results=(
                    initial_monthly_results
                ),
            )
        )

        ensure_global_batch_not_cancelled(
            batch_id
        )

        completed_at = utc_now()

        with SessionLocal() as session:
            result = session.get(
                GlobalCityResult,
                city_result_id,
            )

            if result is None:
                raise RuntimeError(
                    "Global city result disappeared"
                )

            result.status = "completed"
            result.stage = "completed"
            result.progress = 100

            result.climate_adaptation_rate_percent = (
                analysis[
                    "climate_adaptation_rate_percent"
                ]
            )

            result.exposure_coverage_percent = (
                analysis[
                    "exposure_coverage_percent"
                ]
            )

            result.annual_average_skin_improvement_c = (
                analysis[
                    "annual_average_skin_improvement_c"
                ]
            )

            result.annual_average_core_improvement_c = (
                analysis[
                    "annual_average_core_improvement_c"
                ]
            )

            result.maximum_skin_improvement_c = analysis[
                "maximum_skin_improvement_c"
            ]

            result.effective_cooling_hours = analysis[
                "effective_cooling_hours"
            ]

            result.sampled_day_count = analysis[
                "sampled_day_count"
            ]

            result.eligible_sample_count = analysis[
                "eligible_sample_count"
            ]

            result.evaluated_weighted_days = analysis[
                "evaluated_weighted_days"
            ]

            result.beneficial_weighted_days = analysis[
                "beneficial_weighted_days"
            ]

            result.skin_improvement_p50_c = analysis[
                "skin_improvement_p50_c"
            ]

            result.skin_improvement_p90_c = analysis[
                "skin_improvement_p90_c"
            ]

            result.skin_improvement_p95_c = analysis[
                "skin_improvement_p95_c"
            ]

            result.core_improvement_p50_c = analysis[
                "core_improvement_p50_c"
            ]

            result.core_improvement_p90_c = analysis[
                "core_improvement_p90_c"
            ]

            result.core_improvement_p95_c = analysis[
                "core_improvement_p95_c"
            ]

            result.heatwave_event_count = analysis[
                "heatwave_event_count"
            ]

            result.longest_heatwave_days = analysis[
                "longest_heatwave_days"
            ]
            
            result.analytics_json = {
                "heatwave_analysis_available": analysis[
                    "heatwave_analysis_available"
                ],
                "heatwave_events": analysis["heatwave_events"],
                "data_quality": analysis["data_quality"],
                "metric_definitions": analysis["metric_definitions"],
            }

            result.monthly_json = analysis[
                "monthly_results"
            ]

            result.completed_month_count = analysis[
                "completed_month_count"
            ]

            if result.monthly_json:
                result.last_checkpoint_month = max(
                    item["month"]
                    for item in result.monthly_json
                )

            result.error_message = None
            result.last_heartbeat_at = completed_at
            result.completed_at = completed_at

            session.commit()

            refresh_batch_status(
                session,
                batch_id,
            )

        return {
            "batch_id": batch_id,
            "city_result_id": city_result_id,
            "status": "completed",
        }

    except GlobalBatchCancelledError:
        if batch_id is not None:
            with SessionLocal() as session:
                result = session.get(
                    GlobalCityResult,
                    city_result_id,
                )

                if result is not None:
                    now = utc_now()

                    result.status = "cancelled"
                    result.stage = "cancelled"
                    result.progress = 100
                    result.last_heartbeat_at = now
                    result.completed_at = now

                    session.commit()

                refresh_batch_status(
                    session,
                    batch_id,
                )

        return {
            "batch_id": batch_id,
            "city_result_id": city_result_id,
            "status": "cancelled",
        }

    except Exception as error:
        if batch_id is not None:
            with SessionLocal() as session:
                result = session.get(
                    GlobalCityResult,
                    city_result_id,
                )

                if result is not None:
                    now = utc_now()

                    result.status = "failed"
                    result.stage = "failed"
                    result.error_message = str(
                        error
                    )[:4000]
                    result.last_heartbeat_at = now
                    result.completed_at = now

                    session.commit()

                refresh_batch_status(
                    session,
                    batch_id,
                )

        raise
```

### File: `backend/chinese-text-inventory.txt`
```
./alembic/env.py:10:# 必須導入模型，才能註冊到 Base.metadata。
./app/api/benchmarks.py:30:            detail=f"Gagge 基準計算失敗：{error}",
./app/api/materials.py:97:            detail="材料 slug 已存在",
./app/api/materials.py:108:            detail="材料建立後無法重新讀取",
./app/api/materials.py:212:            detail="找不到材料",
./app/api/materials.py:237:            detail="找不到材料",
./app/api/materials.py:277:            detail="找不到材料",
./app/api/materials.py:330:            detail="找不到材料版本",
./app/api/materials.py:385:            detail="不支持的光譜類型",
./app/api/materials.py:396:            detail="找不到材料版本",
./app/api/materials.py:402:            detail="缺少文件名稱",
./app/api/materials.py:410:            detail="只接受 CSV 文件",
./app/api/materials.py:506:            detail="找不到光譜資料",
./app/api/simulations.py:105:            "本結果來自簡化瞬態原型，尚未完成熱人偶、"
./app/api/simulations.py:106:            "人體實驗或 JOS-3 基準驗證，不可用於醫療、"
./app/api/simulations.py:107:            "職業安全或產品認證。"
./app/api/simulations.py:210:            "這是氣象驅動的簡化人體熱平衡原型，"
./app/api/simulations.py:211:            "尚未完成 JOS-3、熱人偶或人體實驗驗證。"
./app/api/simulations.py:215:            "氣溫、濕度、風速和短波輻射來自 ERA5；"
./app/api/simulations.py:216:            "平均輻射溫度和有效天空溫度目前使用"
./app/api/simulations.py:217:            "經驗公式估計。"
./app/api/simulations.py:308:                "無法將任務提交給Celery："
./app/api/simulations.py:371:            detail="找不到模擬任務",
./app/api/simulations.py:392:            detail="找不到模擬任務",
./app/api/simulations.py:399:                "模擬尚未完成，"
./app/api/simulations.py:400:                f"目前狀態：{job.status}"
./app/api/simulations.py:407:            detail="任務完成但缺少結果路徑",
./app/api/simulations.py:436:            detail="找不到模擬任務",
./app/api/simulations.py:447:                "終止狀態的任務不能取消"
./app/api/simulations.py:508:            detail="找不到模擬任務",
./app/api/simulations.py:594:            detail="找不到模擬任務",
./app/api/simulations.py:600:            detail="模擬尚未完成",
./app/api/simulations.py:606:            detail="任務缺少結果文件",
./app/core/cities.py:56:            f"不支持城市 '{city_id}'。"
./app/core/cities.py:57:            f"目前支持：{supported}"
./app/main.py:26:        "輻射製冷服裝全球氣候適應性模擬平台後端"
./app/schemas/material.py:104:                "solar_transmittance 不能大於 1"
./app/schemas/simulation.py:107:                "solar_reflectance + solar_transmittance 不能大於 1"
./app/schemas/weather.py:54:                "動態模擬至少需要兩個氣象時間點"
./app/schemas/weather.py:64:                "氣象時間序列必須按時間升序排列"
./app/services/gagge_benchmark.py:14:    將 Python float、NumPy scalar 或單元素陣列轉為 float。
./app/services/gagge_benchmark.py:27:    將自研原型與 pythermalcomfort Gagge Two-Node 比較。
./app/services/gagge_benchmark.py:29:    注意：
./app/services/gagge_benchmark.py:30:    Gagge 的標準接口不直接處理材料太陽光譜屬性，
./app/services/gagge_benchmark.py:31:    因此基準情景會把太陽輻射設為零。
./app/services/gagge_benchmark.py:92:            "為確保模型邊界條件可比較，"
./app/services/gagge_benchmark.py:93:            "基準計算已將直接太陽輻射設為 0 W/m²。"
./app/services/gagge_benchmark.py:153:            "這是模型診斷比較，不是等價性驗證。"
./app/services/gagge_benchmark.py:154:            "自研原型與 Gagge 模型的熱容量、"
./app/services/gagge_benchmark.py:155:            "服裝模型、血流控制和蒸發控制方程不同。"
./app/services/result_storage.py:57:            f"結果文件不存在：{path}"
./app/services/spectrum_parser.py:36:        raise ValueError("上傳文件為空")
./app/services/spectrum_parser.py:40:            "光譜 CSV 不能超過 2 MB"
./app/services/spectrum_parser.py:47:            "CSV 必須使用 UTF-8 編碼"
./app/services/spectrum_parser.py:55:        raise ValueError("CSV 缺少表頭")
./app/services/spectrum_parser.py:95:            "CSV 必須包含 wavelength_um 欄位"
./app/services/spectrum_parser.py:100:            "CSV 必須包含 value 欄位"
./app/services/spectrum_parser.py:122:                f"第 {row_number} 行包含無效數值"
./app/services/spectrum_parser.py:127:                f"第 {row_number} 行波長不是有限數值"
./app/services/spectrum_parser.py:132:                f"第 {row_number} 行光譜值不是有限數值"
./app/services/spectrum_parser.py:137:                f"第 {row_number} 行波長必須大於 0"
./app/services/spectrum_parser.py:142:                f"第 {row_number} 行光譜值必須位於 0 至 1"
./app/services/spectrum_parser.py:154:                "光譜點數不能超過 20000"
./app/services/spectrum_parser.py:159:            "光譜文件至少需要兩個數據點"
./app/services/spectrum_parser.py:174:                "波長必須嚴格遞增且不能重複"
./app/services/two_node.py:26:# 人體核心與皮膚的面積歸一化有效熱容量，J/(m²·K)
./app/services/two_node.py:48:    Magnus 型近似飽和水汽壓，單位 kPa。
./app/services/two_node.py:81:    # 強制對流與自然對流中取較大者
./app/services/two_node.py:85:    # 服裝熱阻造成皮膚熱量傳到外表面的衰減
./app/services/two_node.py:254:    計算整個模擬期間的人體總能量守恆殘差。
./app/services/two_node.py:256:    人體核心與皮膚之間的熱交換 core_to_skin 是內部熱流，
./app/services/two_node.py:257:    在人體總能量平衡中會互相抵消，因此不放入總淨熱流。
./app/services/two_node.py:447:            f"數值求解失敗：{solution.message}"
./app/services/two_node.py:621:            f"動態氣象數值求解失敗："
./app/services/weather.py:74:    # ERA5 通常約有五天延遲。
./app/services/weather.py:82:            "ERA5 歷史數據通常有約 5 天延遲。"
./app/services/weather.py:83:            f"請選擇不晚於 {latest_safe_date.isoformat()} "
./app/services/weather.py:84:            "的日期。"
./app/services/weather.py:162:            "Open-Meteo 請求失敗："
./app/services/weather.py:188:            f"Open-Meteo 回應缺少變量：{name}"
./app/services/weather.py:193:            f"氣象變量 {name} 長度不一致"
./app/services/weather.py:206:            f"{variable_name} 在索引 {index} 缺失"
./app/services/weather.py:220:            "Open-Meteo 回應缺少 hourly 數據"
./app/services/weather.py:228:            "Open-Meteo 沒有返回氣象時間點"
./app/services/weather.py:271:        # Open-Meteo 在指定 timezone 時返回當地時間，
./app/services/weather.py:272:        # 字符串本身通常不附帶 UTC offset。
./app/services/weather.py:349:    # 前後各多取得一小時，供線性插值使用。
./app/services/weather.py:376:            "氣象數據不足，無法進行時間插值"
./app/services/weather_interpolation.py:108:        # MVP 經驗估計：
./app/services/weather_interpolation.py:109:        # 戶外平均輻射溫度會因短波太陽輻射上升。
./app/services/weather_interpolation.py:115:        # Open-Meteo 歷史接口未直接提供有效天空溫度，
./app/services/weather_interpolation.py:116:        # 第一版按濕度估計天空相對空氣的溫差。
./app/services/weather_simulation.py:141:            "本結果來自氣象驅動的簡化人體"
./app/services/weather_simulation.py:142:            "熱平衡原型，尚未完成JOS-3、"
./app/services/weather_simulation.py:143:            "熱人偶或人體實驗驗證。"
./app/services/weather_simulation.py:147:            "氣溫、濕度、風速及短波輻射"
./app/services/weather_simulation.py:148:            "來自ERA5；平均輻射溫度和有效"
./app/services/weather_simulation.py:149:            "天空溫度目前使用經驗公式估計。"
./app/worker/tasks.py:40:                f"找不到模擬任務：{job_id}"
./app/worker/tasks.py:60:                f"找不到模擬任務：{job_id}"
./app/worker/tasks.py:88:                    f"找不到模擬任務：{job_id}"
./docs/acceptance/stage-3/pytest-all.txt:7:開始執行測試...
./run-tests.sh:11:  echo "錯誤：找不到 $PYTHON"
./run-tests.sh:12:  echo "請先在 backend 目錄建立 .venv"
./run-tests.sh:27:echo "開始執行測試..."
./tests/test_climate_scenarios.py:84:    ), f"{name} 能量殘差過大"
./tests/test_result_export.py:12:    # 可使用現有模擬 fixture 建立結果，
./tests/test_result_export.py:13:    # 或在此使用已保存的測試結果 fixture。
./tests/test_spectrum_parser.py:40:        match="0 至 1",
./tests/test_spectrum_parser.py:55:        match="嚴格遞增",

```

### File: `backend/coverage.xml`
```
<?xml version="1.0" ?>
<coverage version="7.15.3" timestamp="1788165731429" lines-valid="1200" lines-covered="909" line-rate="0.7575" branches-covered="0" branches-valid="0" branch-rate="0" complexity="0">
	<!-- Generated by coverage.py: https://coverage.readthedocs.io/en/7.15.3 -->
	<!-- Based on https://raw.githubusercontent.com/cobertura/web/master/htdocs/xml/coverage-04.dtd -->
	<sources>
		<source>C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend\app</source>
	</sources>
	<packages>
		<package name="." line-rate="1" branch-rate="0" complexity="0">
			<classes>
				<class name="__init__.py" filename="__init__.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines/>
				</class>
				<class name="main.py" filename="main.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="2" hits="1"/>
						<line number="3" hits="1"/>
						<line number="5" hits="1"/>
						<line number="6" hits="1"/>
						<line number="8" hits="1"/>
						<line number="13" hits="1"/>
						<line number="14" hits="1"/>
						<line number="17" hits="1"/>
						<line number="18" hits="1"/>
						<line number="19" hits="1"/>
						<line number="20" hits="1"/>
						<line number="23" hits="1"/>
						<line number="32" hits="1"/>
						<line number="43" hits="1"/>
						<line number="44" hits="1"/>
						<line number="45" hits="1"/>
						<line number="46" hits="1"/>
						<line number="48" hits="1"/>
						<line number="49" hits="1"/>
						<line number="50" hits="1"/>
						<line number="59" hits="1"/>
						<line number="61" hits="1"/>
					</lines>
				</class>
			</classes>
		</package>
		<package name="api" line-rate="0.36" branch-rate="0" complexity="0">
			<classes>
				<class name="__init__.py" filename="api/__init__.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines/>
				</class>
				<class name="benchmarks.py" filename="api/benchmarks.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="3" hits="1"/>
						<line number="7" hits="1"/>
						<line number="12" hits="1"/>
						<line number="18" hits="1"/>
						<line number="22" hits="1"/>
						<line number="25" hits="1"/>
						<line number="26" hits="1"/>
						<line number="27" hits="1"/>
						<line number="28" hits="1"/>
					</lines>
				</class>
				<class name="materials.py" filename="api/materials.py" complexity="0" line-rate="0.25" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="3" hits="1"/>
						<line number="13" hits="1"/>
						<line number="17" hits="1"/>
						<line number="18" hits="1"/>
						<line number="23" hits="1"/>
						<line number="24" hits="1"/>
						<line number="29" hits="1"/>
						<line number="40" hits="1"/>
						<line number="41" hits="1"/>
						<line number="46" hits="1"/>
						<line number="52" hits="1"/>
						<line number="56" hits="0"/>
						<line number="66" hits="1"/>
						<line number="71" hits="1"/>
						<line number="75" hits="0"/>
						<line number="82" hits="0"/>
						<line number="87" hits="0"/>
						<line number="88" hits="0"/>
						<line number="90" hits="0"/>
						<line number="91" hits="0"/>
						<line number="92" hits="0"/>
						<line number="93" hits="0"/>
						<line number="95" hits="0"/>
						<line number="100" hits="0"/>
						<line number="105" hits="0"/>
						<line number="106" hits="0"/>
						<line number="111" hits="0"/>
						<line number="116" hits="1"/>
						<line number="120" hits="1"/>
						<line number="134" hits="0"/>
						<line number="136" hits="0"/>
						<line number="137" hits="0"/>
						<line number="141" hits="0"/>
						<line number="142" hits="0"/>
						<line number="148" hits="0"/>
						<line number="154" hits="0"/>
						<line number="165" hits="0"/>
						<line number="167" hits="0"/>
						<line number="168" hits="0"/>
						<line number="176" hits="0"/>
						<line number="188" hits="0"/>
						<line number="196" hits="1"/>
						<line number="200" hits="1"/>
						<line number="204" hits="0"/>
						<line number="209" hits="0"/>
						<line number="210" hits="0"/>
						<line number="215" hits="0"/>
						<line number="220" hits="1"/>
						<line number="224" hits="1"/>
						<line number="229" hits="0"/>
						<line number="234" hits="0"/>
						<line number="235" hits="0"/>
						<line number="240" hits="0"/>
						<line number="244" hits="0"/>
						<line number="245" hits="0"/>
						<line number="247" hits="0"/>
						<line number="249" hits="0"/>
						<line number="254" hits="0"/>
						<line number="259" hits="1"/>
						<line number="264" hits="1"/>
						<line number="269" hits="0"/>
						<line number="274" hits="0"/>
						<line number="275" hits="0"/>
						<line number="280" hits="0"/>
						<line number="292" hits="0"/>
						<line number="298" hits="0"/>
						<line number="299" hits="0"/>
						<line number="300" hits="0"/>
						<line number="302" hits="0"/>
						<line number="307" hits="1"/>
						<line number="311" hits="1"/>
						<line number="315" hits="0"/>
						<line number="327" hits="0"/>
						<line number="328" hits="0"/>
						<line number="333" hits="0"/>
						<line number="359" hits="1"/>
						<line number="363" hits="1"/>
						<line number="375" hits="0"/>
						<line number="382" hits="0"/>
						<line number="383" hits="0"/>
						<line number="388" hits="0"/>
						<line number="393" hits="0"/>
						<line number="394" hits="0"/>
						<line number="399" hits="0"/>
						<line number="400" hits="0"/>
						<line number="405" hits="0"/>
						<line number="408" hits="0"/>
						<line number="413" hits="0"/>
						<line number="415" hits="0"/>
						<line number="416" hits="0"/>
						<line number="419" hits="0"/>
						<line number="420" hits="0"/>
						<line number="425" hits="0"/>
						<line number="435" hits="0"/>
						<line number="436" hits="0"/>
						<line number="454" hits="0"/>
						<line number="456" hits="0"/>
						<line number="457" hits="0"/>
						<line number="460" hits="0"/>
						<line number="463" hits="0"/>
						<line number="466" hits="0"/>
						<line number="469" hits="0"/>
						<line number="473" hits="0"/>
						<line number="474" hits="0"/>
						<line number="476" hits="0"/>
						<line number="484" hits="1"/>
						<line number="488" hits="1"/>
						<line number="493" hits="0"/>
						<line number="503" hits="0"/>
						<line number="504" hits="0"/>
						<line number="509" hits="0"/>
					</lines>
				</class>
				<class name="simulations.py" filename="api/simulations.py" complexity="0" line-rate="0.325" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="3" hits="1"/>
						<line number="4" hits="1"/>
						<line number="8" hits="1"/>
						<line number="12" hits="1"/>
						<line number="16" hits="1"/>
						<line number="21" hits="1"/>
						<line number="24" hits="1"/>
						<line number="30" hits="1"/>
						<line number="34" hits="1"/>
						<line number="37" hits="1"/>
						<line number="38" hits="1"/>
						<line number="48" hits="1"/>
						<line number="57" hits="0"/>
						<line number="58" hits="0"/>
						<line number="63" hits="1"/>
						<line number="68" hits="1"/>
						<line number="73" hits="1"/>
						<line number="78" hits="1"/>
						<line number="83" hits="1"/>
						<line number="112" hits="1"/>
						<line number="116" hits="1"/>
						<line number="119" hits="0"/>
						<line number="120" hits="0"/>
						<line number="122" hits="0"/>
						<line number="132" hits="0"/>
						<line number="146" hits="0"/>
						<line number="159" hits="0"/>
						<line number="160" hits="0"/>
						<line number="164" hits="0"/>
						<line number="165" hits="0"/>
						<line number="170" hits="0"/>
						<line number="175" hits="0"/>
						<line number="180" hits="0"/>
						<line number="224" hits="1"/>
						<line number="225" hits="1"/>
						<line number="227" hits="1"/>
						<line number="228" hits="1"/>
						<line number="235" hits="1"/>
						<line number="238" hits="1"/>
						<line number="239" hits="1"/>
						<line number="241" hits="1"/>
						<line number="245" hits="1"/>
						<line number="248" hits="1"/>
						<line number="253" hits="1"/>
						<line number="258" hits="1"/>
						<line number="261" hits="1"/>
						<line number="264" hits="1"/>
						<line number="268" hits="1"/>
						<line number="273" hits="1"/>
						<line number="277" hits="0"/>
						<line number="287" hits="0"/>
						<line number="288" hits="0"/>
						<line number="289" hits="0"/>
						<line number="291" hits="0"/>
						<line number="292" hits="0"/>
						<line number="298" hits="0"/>
						<line number="299" hits="0"/>
						<line number="300" hits="0"/>
						<line number="302" hits="0"/>
						<line number="303" hits="0"/>
						<line number="304" hits="0"/>
						<line number="305" hits="0"/>
						<line number="306" hits="0"/>
						<line number="308" hits="0"/>
						<line number="316" hits="0"/>
						<line number="318" hits="1"/>
						<line number="322" hits="1"/>
						<line number="334" hits="0"/>
						<line number="339" hits="0"/>
						<line number="348" hits="0"/>
						<line number="358" hits="1"/>
						<line number="362" hits="1"/>
						<line number="366" hits="0"/>
						<line number="371" hits="0"/>
						<line number="372" hits="0"/>
						<line number="377" hits="0"/>
						<line number="379" hits="1"/>
						<line number="383" hits="1"/>
						<line number="387" hits="0"/>
						<line number="392" hits="0"/>
						<line number="393" hits="0"/>
						<line number="398" hits="0"/>
						<line number="399" hits="0"/>
						<line number="407" hits="0"/>
						<line number="408" hits="0"/>
						<line number="413" hits="0"/>
						<line number="414" hits="0"/>
						<line number="417" hits="0"/>
						<line number="418" hits="0"/>
						<line number="423" hits="1"/>
						<line number="427" hits="1"/>
						<line number="431" hits="0"/>
						<line number="436" hits="0"/>
						<line number="437" hits="0"/>
						<line number="442" hits="0"/>
						<line number="447" hits="0"/>
						<line number="454" hits="0"/>
						<line number="455" hits="0"/>
						<line number="460" hits="0"/>
						<line number="461" hits="0"/>
						<line number="462" hits="0"/>
						<line number="464" hits="0"/>
						<line number="465" hits="0"/>
						<line number="469" hits="0"/>
						<line number="470" hits="0"/>
						<line number="472" hits="0"/>
						<line number="474" hits="1"/>
						<line number="481" hits="1"/>
						<line number="484" hits="0"/>
						<line number="485" hits="0"/>
						<line number="490" hits="0"/>
						<line number="491" hits="0"/>
						<line number="493" hits="0"/>
						<line number="496" hits="1"/>
						<line number="499" hits="1"/>
						<line number="503" hits="0"/>
						<line number="508" hits="0"/>
						<line number="509" hits="0"/>
						<line number="514" hits="0"/>
						<line number="515" hits="0"/>
						<line number="517" hits="0"/>
						<line number="518" hits="0"/>
						<line number="519" hits="0"/>
						<line number="521" hits="0"/>
						<line number="528" hits="0"/>
						<line number="529" hits="0"/>
						<line number="533" hits="0"/>
						<line number="535" hits="0"/>
						<line number="542" hits="0"/>
						<line number="543" hits="0"/>
						<line number="548" hits="0"/>
						<line number="550" hits="0"/>
						<line number="553" hits="0"/>
						<line number="557" hits="0"/>
						<line number="559" hits="0"/>
						<line number="561" hits="0"/>
						<line number="571" hits="1"/>
						<line number="573" hits="1"/>
						<line number="578" hits="1"/>
						<line number="581" hits="1"/>
						<line number="589" hits="0"/>
						<line number="594" hits="0"/>
						<line number="595" hits="0"/>
						<line number="600" hits="0"/>
						<line number="601" hits="0"/>
						<line number="606" hits="0"/>
						<line number="607" hits="0"/>
						<line number="612" hits="0"/>
						<line number="613" hits="0"/>
						<line number="616" hits="0"/>
						<line number="617" hits="0"/>
						<line number="622" hits="0"/>
						<line number="623" hits="0"/>
						<line number="624" hits="0"/>
						<line number="625" hits="0"/>
						<line number="627" hits="0"/>
						<line number="628" hits="0"/>
						<line number="629" hits="0"/>
						<line number="631" hits="0"/>
					</lines>
				</class>
				<class name="weather.py" filename="api/weather.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="3" hits="1"/>
						<line number="5" hits="1"/>
						<line number="6" hits="1"/>
						<line number="10" hits="1"/>
						<line number="16" hits="1"/>
						<line number="22" hits="1"/>
						<line number="26" hits="1"/>
						<line number="27" hits="1"/>
						<line number="33" hits="1"/>
						<line number="37" hits="1"/>
						<line number="46" hits="1"/>
						<line number="47" hits="1"/>
						<line number="49" hits="1"/>
						<line number="54" hits="1"/>
						<line number="55" hits="1"/>
						<line number="59" hits="1"/>
						<line number="60" hits="1"/>
					</lines>
				</class>
			</classes>
		</package>
		<package name="core" line-rate="1" branch-rate="0" complexity="0">
			<classes>
				<class name="__init__.py" filename="core/__init__.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines/>
				</class>
				<class name="cities.py" filename="core/cities.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="4" hits="1"/>
						<line number="5" hits="1"/>
						<line number="6" hits="1"/>
						<line number="7" hits="1"/>
						<line number="8" hits="1"/>
						<line number="9" hits="1"/>
						<line number="10" hits="1"/>
						<line number="11" hits="1"/>
						<line number="12" hits="1"/>
						<line number="13" hits="1"/>
						<line number="16" hits="1"/>
						<line number="50" hits="1"/>
						<line number="51" hits="1"/>
						<line number="53" hits="1"/>
						<line number="54" hits="1"/>
						<line number="55" hits="1"/>
						<line number="60" hits="1"/>
					</lines>
				</class>
				<class name="config.py" filename="core/config.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="3" hits="1"/>
						<line number="9" hits="1"/>
						<line number="12" hits="1"/>
						<line number="13" hits="1"/>
						<line number="16" hits="1"/>
						<line number="18" hits="1"/>
						<line number="24" hits="1"/>
						<line number="27" hits="1"/>
						<line number="31" hits="1"/>
						<line number="35" hits="1"/>
						<line number="39" hits="1"/>
						<line number="46" hits="1"/>
						<line number="47" hits="1"/>
					</lines>
				</class>
			</classes>
		</package>
		<package name="db" line-rate="0.8333" branch-rate="0" complexity="0">
			<classes>
				<class name="__init__.py" filename="db/__init__.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines/>
				</class>
				<class name="base.py" filename="db/base.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="4" hits="1"/>
						<line number="5" hits="1"/>
					</lines>
				</class>
				<class name="session.py" filename="db/session.py" complexity="0" line-rate="0.7778" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="3" hits="1"/>
						<line number="4" hits="1"/>
						<line number="9" hits="1"/>
						<line number="12" hits="1"/>
						<line number="17" hits="1"/>
						<line number="24" hits="1"/>
						<line number="25" hits="0"/>
						<line number="26" hits="0"/>
					</lines>
				</class>
			</classes>
		</package>
		<package name="models" line-rate="1" branch-rate="0" complexity="0">
			<classes>
				<class name="__init__.py" filename="models/__init__.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="6" hits="1"/>
						<line number="8" hits="1"/>
					</lines>
				</class>
				<class name="material.py" filename="models/material.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="2" hits="1"/>
						<line number="4" hits="1"/>
						<line number="16" hits="1"/>
						<line number="17" hits="1"/>
						<line number="23" hits="1"/>
						<line number="26" hits="1"/>
						<line number="27" hits="1"/>
						<line number="29" hits="1"/>
						<line number="35" hits="1"/>
						<line number="41" hits="1"/>
						<line number="48" hits="1"/>
						<line number="53" hits="1"/>
						<line number="58" hits="1"/>
						<line number="66" hits="1"/>
						<line number="72" hits="1"/>
						<line number="79" hits="1"/>
						<line number="86" hits="1"/>
						<line number="87" hits="1"/>
						<line number="89" hits="1"/>
						<line number="121" hits="1"/>
						<line number="127" hits="1"/>
						<line number="136" hits="1"/>
						<line number="141" hits="1"/>
						<line number="147" hits="1"/>
						<line number="152" hits="1"/>
						<line number="159" hits="1"/>
						<line number="164" hits="1"/>
						<line number="170" hits="1"/>
						<line number="175" hits="1"/>
						<line number="181" hits="1"/>
						<line number="187" hits="1"/>
						<line number="195" hits="1"/>
						<line number="200" hits="1"/>
						<line number="205" hits="1"/>
						<line number="211" hits="1"/>
						<line number="216" hits="1"/>
						<line number="221" hits="1"/>
						<line number="227" hits="1"/>
						<line number="231" hits="1"/>
						<line number="237" hits="1"/>
						<line number="238" hits="1"/>
						<line number="240" hits="1"/>
						<line number="248" hits="1"/>
						<line number="254" hits="1"/>
						<line number="263" hits="1"/>
						<line number="268" hits="1"/>
						<line number="274" hits="1"/>
						<line number="279" hits="1"/>
						<line number="284" hits="1"/>
						<line number="289" hits="1"/>
						<line number="294" hits="1"/>
						<line number="299" hits="1"/>
						<line number="304" hits="1"/>
						<line number="310" hits="1"/>
					</lines>
				</class>
				<class name="simulation_job.py" filename="models/simulation_job.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="2" hits="1"/>
						<line number="4" hits="1"/>
						<line number="11" hits="1"/>
						<line number="12" hits="1"/>
						<line number="17" hits="1"/>
						<line number="20" hits="1"/>
						<line number="21" hits="1"/>
						<line number="23" hits="1"/>
						<line number="29" hits="1"/>
						<line number="37" hits="1"/>
						<line number="44" hits="1"/>
						<line number="50" hits="1"/>
						<line number="56" hits="1"/>
						<line number="62" hits="1"/>
						<line number="67" hits="1"/>
						<line number="74" hits="1"/>
						<line number="81" hits="1"/>
						<line number="88" hits="1"/>
						<line number="94" hits="1"/>
						<line number="101" hits="1"/>
						<line number="108" hits="1"/>
					</lines>
				</class>
			</classes>
		</package>
		<package name="schemas" line-rate="0.9826" branch-rate="0" complexity="0">
			<classes>
				<class name="__init__.py" filename="schemas/__init__.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines/>
				</class>
				<class name="job.py" filename="schemas/job.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="2" hits="1"/>
						<line number="4" hits="1"/>
						<line number="6" hits="1"/>
						<line number="11" hits="1"/>
						<line number="21" hits="1"/>
						<line number="22" hits="1"/>
						<line number="23" hits="1"/>
						<line number="24" hits="1"/>
						<line number="25" hits="1"/>
						<line number="26" hits="1"/>
						<line number="27" hits="1"/>
						<line number="29" hits="1"/>
						<line number="30" hits="1"/>
						<line number="32" hits="1"/>
						<line number="33" hits="1"/>
						<line number="34" hits="1"/>
						<line number="35" hits="1"/>
						<line number="38" hits="1"/>
						<line number="41" hits="1"/>
						<line number="44" hits="1"/>
						<line number="45" hits="1"/>
						<line number="46" hits="1"/>
						<line number="47" hits="1"/>
						<line number="48" hits="1"/>
					</lines>
				</class>
				<class name="material.py" filename="schemas/material.py" complexity="0" line-rate="0.9694" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="2" hits="1"/>
						<line number="4" hits="1"/>
						<line number="12" hits="1"/>
						<line number="19" hits="1"/>
						<line number="27" hits="1"/>
						<line number="28" hits="1"/>
						<line number="30" hits="1"/>
						<line number="36" hits="1"/>
						<line number="41" hits="1"/>
						<line number="47" hits="1"/>
						<line number="53" hits="1"/>
						<line number="59" hits="1"/>
						<line number="65" hits="1"/>
						<line number="71" hits="1"/>
						<line number="77" hits="1"/>
						<line number="82" hits="1"/>
						<line number="87" hits="1"/>
						<line number="92" hits="1"/>
						<line number="93" hits="1"/>
						<line number="95" hits="1"/>
						<line number="96" hits="1"/>
						<line number="97" hits="0"/>
						<line number="102" hits="0"/>
						<line number="107" hits="0"/>
						<line number="110" hits="1"/>
						<line number="111" hits="1"/>
						<line number="116" hits="1"/>
						<line number="122" hits="1"/>
						<line number="123" hits="1"/>
						<line number="125" hits="1"/>
						<line number="128" hits="1"/>
						<line number="129" hits="1"/>
						<line number="135" hits="1"/>
						<line number="136" hits="1"/>
						<line number="137" hits="1"/>
						<line number="140" hits="1"/>
						<line number="141" hits="1"/>
						<line number="143" hits="1"/>
						<line number="144" hits="1"/>
						<line number="145" hits="1"/>
						<line number="146" hits="1"/>
						<line number="147" hits="1"/>
						<line number="148" hits="1"/>
						<line number="149" hits="1"/>
						<line number="150" hits="1"/>
						<line number="151" hits="1"/>
						<line number="154" hits="1"/>
						<line number="155" hits="1"/>
						<line number="157" hits="1"/>
						<line number="158" hits="1"/>
						<line number="159" hits="1"/>
						<line number="160" hits="1"/>
						<line number="162" hits="1"/>
						<line number="163" hits="1"/>
						<line number="165" hits="1"/>
						<line number="166" hits="1"/>
						<line number="167" hits="1"/>
						<line number="168" hits="1"/>
						<line number="170" hits="1"/>
						<line number="171" hits="1"/>
						<line number="173" hits="1"/>
						<line number="174" hits="1"/>
						<line number="176" hits="1"/>
						<line number="177" hits="1"/>
						<line number="178" hits="1"/>
						<line number="180" hits="1"/>
						<line number="181" hits="1"/>
						<line number="184" hits="1"/>
						<line number="185" hits="1"/>
						<line number="187" hits="1"/>
						<line number="188" hits="1"/>
						<line number="189" hits="1"/>
						<line number="190" hits="1"/>
						<line number="191" hits="1"/>
						<line number="192" hits="1"/>
						<line number="193" hits="1"/>
						<line number="194" hits="1"/>
						<line number="196" hits="1"/>
						<line number="199" hits="1"/>
						<line number="200" hits="1"/>
						<line number="201" hits="1"/>
						<line number="202" hits="1"/>
						<line number="203" hits="1"/>
						<line number="204" hits="1"/>
						<line number="205" hits="1"/>
						<line number="206" hits="1"/>
						<line number="209" hits="1"/>
						<line number="210" hits="1"/>
						<line number="211" hits="1"/>
						<line number="212" hits="1"/>
						<line number="213" hits="1"/>
						<line number="216" hits="1"/>
						<line number="217" hits="1"/>
						<line number="218" hits="1"/>
						<line number="221" hits="1"/>
						<line number="222" hits="1"/>
						<line number="223" hits="1"/>
					</lines>
				</class>
				<class name="simulation.py" filename="schemas/simulation.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="3" hits="1"/>
						<line number="5" hits="1"/>
						<line number="7" hits="1"/>
						<line number="8" hits="1"/>
						<line number="13" hits="1"/>
						<line number="18" hits="1"/>
						<line number="23" hits="1"/>
						<line number="28" hits="1"/>
						<line number="33" hits="1"/>
						<line number="38" hits="1"/>
						<line number="45" hits="1"/>
						<line number="46" hits="1"/>
						<line number="51" hits="1"/>
						<line number="56" hits="1"/>
						<line number="61" hits="1"/>
						<line number="68" hits="1"/>
						<line number="69" hits="1"/>
						<line number="70" hits="1"/>
						<line number="75" hits="1"/>
						<line number="80" hits="1"/>
						<line number="85" hits="1"/>
						<line number="90" hits="1"/>
						<line number="95" hits="1"/>
						<line number="101" hits="1"/>
						<line number="102" hits="1"/>
						<line number="103" hits="1"/>
						<line number="105" hits="1"/>
						<line number="106" hits="1"/>
						<line number="110" hits="1"/>
						<line number="113" hits="1"/>
						<line number="114" hits="1"/>
						<line number="115" hits="1"/>
						<line number="120" hits="1"/>
						<line number="125" hits="1"/>
						<line number="126" hits="1"/>
						<line number="127" hits="1"/>
						<line number="128" hits="1"/>
						<line number="130" hits="1"/>
						<line number="131" hits="1"/>
						<line number="132" hits="1"/>
						<line number="133" hits="1"/>
						<line number="134" hits="1"/>
						<line number="135" hits="1"/>
						<line number="136" hits="1"/>
						<line number="137" hits="1"/>
						<line number="139" hits="1"/>
						<line number="140" hits="1"/>
						<line number="141" hits="1"/>
						<line number="142" hits="1"/>
						<line number="143" hits="1"/>
						<line number="144" hits="1"/>
						<line number="145" hits="1"/>
						<line number="146" hits="1"/>
						<line number="147" hits="1"/>
						<line number="150" hits="1"/>
						<line number="151" hits="1"/>
						<line number="152" hits="1"/>
						<line number="153" hits="1"/>
						<line number="154" hits="1"/>
						<line number="155" hits="1"/>
						<line number="156" hits="1"/>
						<line number="157" hits="1"/>
						<line number="160" hits="1"/>
						<line number="161" hits="1"/>
						<line number="162" hits="1"/>
						<line number="163" hits="1"/>
						<line number="166" hits="1"/>
						<line number="167" hits="1"/>
						<line number="168" hits="1"/>
						<line number="169" hits="1"/>
						<line number="170" hits="1"/>
						<line number="171" hits="1"/>
						<line number="172" hits="1"/>
						<line number="173" hits="1"/>
						<line number="174" hits="1"/>
						<line number="178" hits="1"/>
						<line number="179" hits="1"/>
						<line number="184" hits="1"/>
						<line number="185" hits="1"/>
						<line number="186" hits="1"/>
						<line number="189" hits="1"/>
						<line number="190" hits="1"/>
						<line number="191" hits="1"/>
						<line number="192" hits="1"/>
						<line number="193" hits="1"/>
						<line number="194" hits="1"/>
						<line number="195" hits="1"/>
						<line number="196" hits="1"/>
						<line number="197" hits="1"/>
						<line number="200" hits="1"/>
						<line number="201" hits="1"/>
						<line number="202" hits="1"/>
						<line number="203" hits="1"/>
						<line number="204" hits="1"/>
						<line number="207" hits="1"/>
						<line number="208" hits="1"/>
						<line number="209" hits="1"/>
						<line number="210" hits="1"/>
						<line number="211" hits="1"/>
						<line number="212" hits="1"/>
						<line number="213" hits="1"/>
						<line number="214" hits="1"/>
						<line number="215" hits="1"/>
						<line number="217" hits="1"/>
						<line number="218" hits="1"/>
						<line number="222" hits="1"/>
						<line number="223" hits="1"/>
						<line number="228" hits="1"/>
						<line number="233" hits="1"/>
						<line number="234" hits="1"/>
						<line number="235" hits="1"/>
						<line number="238" hits="1"/>
						<line number="241" hits="1"/>
						<line number="242" hits="1"/>
					</lines>
				</class>
				<class name="weather.py" filename="schemas/weather.py" complexity="0" line-rate="0.9592" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="3" hits="1"/>
						<line number="6" hits="1"/>
						<line number="7" hits="1"/>
						<line number="8" hits="1"/>
						<line number="9" hits="1"/>
						<line number="10" hits="1"/>
						<line number="11" hits="1"/>
						<line number="12" hits="1"/>
						<line number="13" hits="1"/>
						<line number="14" hits="1"/>
						<line number="17" hits="1"/>
						<line number="18" hits="1"/>
						<line number="20" hits="1"/>
						<line number="21" hits="1"/>
						<line number="22" hits="1"/>
						<line number="24" hits="1"/>
						<line number="25" hits="1"/>
						<line number="26" hits="1"/>
						<line number="27" hits="1"/>
						<line number="30" hits="1"/>
						<line number="31" hits="1"/>
						<line number="32" hits="1"/>
						<line number="33" hits="1"/>
						<line number="34" hits="1"/>
						<line number="35" hits="1"/>
						<line number="36" hits="1"/>
						<line number="37" hits="1"/>
						<line number="38" hits="1"/>
						<line number="39" hits="1"/>
						<line number="40" hits="1"/>
						<line number="43" hits="1"/>
						<line number="44" hits="1"/>
						<line number="45" hits="1"/>
						<line number="46" hits="1"/>
						<line number="47" hits="1"/>
						<line number="48" hits="1"/>
						<line number="50" hits="1"/>
						<line number="51" hits="1"/>
						<line number="52" hits="1"/>
						<line number="53" hits="0"/>
						<line number="57" hits="1"/>
						<line number="62" hits="1"/>
						<line number="63" hits="0"/>
						<line number="67" hits="1"/>
						<line number="70" hits="1"/>
						<line number="71" hits="1"/>
						<line number="72" hits="1"/>
						<line number="73" hits="1"/>
					</lines>
				</class>
			</classes>
		</package>
		<package name="services" line-rate="0.8321" branch-rate="0" complexity="0">
			<classes>
				<class name="__init__.py" filename="services/__init__.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines/>
				</class>
				<class name="gagge_benchmark.py" filename="services/gagge_benchmark.py" complexity="0" line-rate="0.9333" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="3" hits="1"/>
						<line number="9" hits="1"/>
						<line number="12" hits="1"/>
						<line number="17" hits="1"/>
						<line number="18" hits="1"/>
						<line number="20" hits="0"/>
						<line number="23" hits="1"/>
						<line number="34" hits="1"/>
						<line number="42" hits="1"/>
						<line number="50" hits="1"/>
						<line number="77" hits="1"/>
						<line number="81" hits="1"/>
						<line number="84" hits="1"/>
						<line number="88" hits="1"/>
					</lines>
				</class>
				<class name="job_service.py" filename="services/job_service.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="3" hits="1"/>
						<line number="6" hits="1"/>
						<line number="10" hits="1"/>
						<line number="15" hits="1"/>
						<line number="18" hits="1"/>
						<line number="34" hits="1"/>
						<line number="37" hits="1"/>
						<line number="45" hits="1"/>
						<line number="49" hits="1"/>
					</lines>
				</class>
				<class name="result_export.py" filename="services/result_export.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="2" hits="1"/>
						<line number="3" hits="1"/>
						<line number="5" hits="1"/>
						<line number="10" hits="1"/>
						<line number="13" hits="1"/>
						<line number="15" hits="1"/>
						<line number="17" hits="1"/>
						<line number="35" hits="1"/>
						<line number="38" hits="1"/>
						<line number="42" hits="1"/>
						<line number="47" hits="1"/>
						<line number="65" hits="1"/>
						<line number="68" hits="1"/>
						<line number="71" hits="1"/>
					</lines>
				</class>
				<class name="result_storage.py" filename="services/result_storage.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="2" hits="1"/>
						<line number="3" hits="1"/>
						<line number="5" hits="1"/>
						<line number="6" hits="1"/>
						<line number="11" hits="1"/>
						<line number="15" hits="1"/>
						<line number="18" hits="1"/>
						<line number="23" hits="1"/>
						<line number="28" hits="1"/>
						<line number="33" hits="1"/>
						<line number="38" hits="1"/>
						<line number="45" hits="1"/>
						<line number="47" hits="1"/>
						<line number="50" hits="1"/>
						<line number="53" hits="1"/>
						<line number="55" hits="1"/>
						<line number="56" hits="1"/>
						<line number="60" hits="1"/>
						<line number="65" hits="1"/>
						<line number="67" hits="1"/>
					</lines>
				</class>
				<class name="spectrum_parser.py" filename="services/spectrum_parser.py" complexity="0" line-rate="0.9839" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="3" hits="1"/>
						<line number="4" hits="1"/>
						<line number="5" hits="1"/>
						<line number="6" hits="1"/>
						<line number="7" hits="1"/>
						<line number="10" hits="1"/>
						<line number="11" hits="1"/>
						<line number="14" hits="1"/>
						<line number="15" hits="1"/>
						<line number="16" hits="1"/>
						<line number="17" hits="1"/>
						<line number="18" hits="1"/>
						<line number="19" hits="1"/>
						<line number="22" hits="1"/>
						<line number="23" hits="1"/>
						<line number="32" hits="1"/>
						<line number="35" hits="1"/>
						<line number="36" hits="1"/>
						<line number="38" hits="1"/>
						<line number="39" hits="1"/>
						<line number="43" hits="1"/>
						<line number="44" hits="1"/>
						<line number="45" hits="1"/>
						<line number="46" hits="1"/>
						<line number="50" hits="1"/>
						<line number="54" hits="1"/>
						<line number="55" hits="0"/>
						<line number="57" hits="1"/>
						<line number="62" hits="1"/>
						<line number="68" hits="1"/>
						<line number="75" hits="1"/>
						<line number="84" hits="1"/>
						<line number="93" hits="1"/>
						<line number="94" hits="1"/>
						<line number="98" hits="1"/>
						<line number="99" hits="1"/>
						<line number="103" hits="1"/>
						<line number="105" hits="1"/>
						<line number="109" hits="1"/>
						<line number="110" hits="1"/>
						<line number="113" hits="1"/>
						<line number="116" hits="1"/>
						<line number="121" hits="1"/>
						<line number="125" hits="1"/>
						<line number="126" hits="1"/>
						<line number="130" hits="1"/>
						<line number="131" hits="1"/>
						<line number="135" hits="1"/>
						<line number="136" hits="1"/>
						<line number="140" hits="1"/>
						<line number="141" hits="1"/>
						<line number="145" hits="1"/>
						<line number="152" hits="1"/>
						<line number="153" hits="1"/>
						<line number="157" hits="1"/>
						<line number="158" hits="1"/>
						<line number="162" hits="1"/>
						<line number="167" hits="1"/>
						<line number="172" hits="1"/>
						<line number="173" hits="1"/>
						<line number="177" hits="1"/>
					</lines>
				</class>
				<class name="two_node.py" filename="services/two_node.py" complexity="0" line-rate="0.7315" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="3" hits="1"/>
						<line number="4" hits="1"/>
						<line number="6" hits="1"/>
						<line number="7" hits="1"/>
						<line number="9" hits="1"/>
						<line number="10" hits="1"/>
						<line number="14" hits="1"/>
						<line number="24" hits="1"/>
						<line number="27" hits="1"/>
						<line number="28" hits="1"/>
						<line number="31" hits="1"/>
						<line number="32" hits="1"/>
						<line number="33" hits="1"/>
						<line number="34" hits="1"/>
						<line number="35" hits="1"/>
						<line number="36" hits="1"/>
						<line number="37" hits="1"/>
						<line number="38" hits="1"/>
						<line number="39" hits="1"/>
						<line number="42" hits="1"/>
						<line number="43" hits="1"/>
						<line number="46" hits="1"/>
						<line number="50" hits="1"/>
						<line number="56" hits="1"/>
						<line number="63" hits="1"/>
						<line number="64" hits="1"/>
						<line number="68" hits="1"/>
						<line number="69" hits="1"/>
						<line number="70" hits="0"/>
						<line number="72" hits="1"/>
						<line number="75" hits="1"/>
						<line number="77" hits="1"/>
						<line number="82" hits="1"/>
						<line number="83" hits="1"/>
						<line number="86" hits="1"/>
						<line number="92" hits="1"/>
						<line number="98" hits="1"/>
						<line number="99" hits="1"/>
						<line number="100" hits="1"/>
						<line number="102" hits="1"/>
						<line number="103" hits="1"/>
						<line number="105" hits="1"/>
						<line number="114" hits="1"/>
						<line number="123" hits="1"/>
						<line number="129" hits="1"/>
						<line number="134" hits="1"/>
						<line number="136" hits="1"/>
						<line number="143" hits="1"/>
						<line number="149" hits="1"/>
						<line number="155" hits="1"/>
						<line number="159" hits="1"/>
						<line number="166" hits="1"/>
						<line number="176" hits="1"/>
						<line number="183" hits="1"/>
						<line number="186" hits="1"/>
						<line number="188" hits="1"/>
						<line number="193" hits="1"/>
						<line number="201" hits="1"/>
						<line number="205" hits="1"/>
						<line number="210" hits="1"/>
						<line number="212" hits="1"/>
						<line number="216" hits="1"/>
						<line number="223" hits="1"/>
						<line number="229" hits="1"/>
						<line number="234" hits="1"/>
						<line number="244" hits="1"/>
						<line number="260" hits="1"/>
						<line number="262" hits="1"/>
						<line number="267" hits="1"/>
						<line number="275" hits="1"/>
						<line number="284" hits="1"/>
						<line number="286" hits="1"/>
						<line number="291" hits="1"/>
						<line number="298" hits="1"/>
						<line number="311" hits="1"/>
						<line number="316" hits="1"/>
						<line number="322" hits="1"/>
						<line number="328" hits="1"/>
						<line number="334" hits="1"/>
						<line number="340" hits="1"/>
						<line number="370" hits="1"/>
						<line number="377" hits="1"/>
						<line number="379" hits="1"/>
						<line number="385" hits="1"/>
						<line number="386" hits="0"/>
						<line number="391" hits="1"/>
						<line number="396" hits="1"/>
						<line number="400" hits="1"/>
						<line number="401" hits="1"/>
						<line number="403" hits="1"/>
						<line number="411" hits="1"/>
						<line number="417" hits="1"/>
						<line number="425" hits="1"/>
						<line number="428" hits="1"/>
						<line number="432" hits="1"/>
						<line number="434" hits="1"/>
						<line number="445" hits="1"/>
						<line number="446" hits="0"/>
						<line number="450" hits="1"/>
						<line number="455" hits="1"/>
						<line number="460" hits="1"/>
						<line number="473" hits="1"/>
						<line number="475" hits="1"/>
						<line number="476" hits="1"/>
						<line number="477" hits="1"/>
						<line number="479" hits="1"/>
						<line number="487" hits="1"/>
						<line number="521" hits="1"/>
						<line number="525" hits="1"/>
						<line number="530" hits="1"/>
						<line number="540" hits="1"/>
						<line number="547" hits="0"/>
						<line number="551" hits="0"/>
						<line number="553" hits="0"/>
						<line number="559" hits="0"/>
						<line number="560" hits="0"/>
						<line number="565" hits="0"/>
						<line number="570" hits="0"/>
						<line number="574" hits="0"/>
						<line number="578" hits="0"/>
						<line number="579" hits="0"/>
						<line number="581" hits="0"/>
						<line number="589" hits="0"/>
						<line number="595" hits="0"/>
						<line number="603" hits="0"/>
						<line number="608" hits="0"/>
						<line number="619" hits="0"/>
						<line number="620" hits="0"/>
						<line number="625" hits="0"/>
						<line number="626" hits="0"/>
						<line number="628" hits="0"/>
						<line number="631" hits="0"/>
						<line number="634" hits="0"/>
						<line number="638" hits="0"/>
						<line number="642" hits="0"/>
						<line number="650" hits="0"/>
						<line number="659" hits="0"/>
						<line number="696" hits="0"/>
						<line number="700" hits="0"/>
						<line number="704" hits="0"/>
						<line number="709" hits="0"/>
						<line number="716" hits="0"/>
						<line number="723" hits="0"/>
						<line number="728" hits="0"/>
						<line number="734" hits="0"/>
						<line number="774" hits="0"/>
						<line number="778" hits="0"/>
						<line number="783" hits="0"/>
					</lines>
				</class>
				<class name="weather.py" filename="services/weather.py" complexity="0" line-rate="0.7033" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="3" hits="1"/>
						<line number="4" hits="1"/>
						<line number="5" hits="1"/>
						<line number="11" hits="1"/>
						<line number="12" hits="1"/>
						<line number="14" hits="1"/>
						<line number="16" hits="1"/>
						<line number="17" hits="1"/>
						<line number="25" hits="1"/>
						<line number="29" hits="1"/>
						<line number="39" hits="1"/>
						<line number="42" hits="1"/>
						<line number="45" hits="1"/>
						<line number="57" hits="1"/>
						<line number="61" hits="1"/>
						<line number="63" hits="1"/>
						<line number="64" hits="1"/>
						<line number="68" hits="0"/>
						<line number="71" hits="1"/>
						<line number="75" hits="1"/>
						<line number="80" hits="1"/>
						<line number="81" hits="0"/>
						<line number="88" hits="1"/>
						<line number="93" hits="1"/>
						<line number="108" hits="1"/>
						<line number="111" hits="0"/>
						<line number="117" hits="0"/>
						<line number="121" hits="0"/>
						<line number="124" hits="1"/>
						<line number="127" hits="0"/>
						<line number="128" hits="0"/>
						<line number="133" hits="0"/>
						<line number="134" hits="0"/>
						<line number="143" hits="0"/>
						<line number="146" hits="0"/>
						<line number="151" hits="0"/>
						<line number="152" hits="0"/>
						<line number="153" hits="0"/>
						<line number="154" hits="0"/>
						<line number="158" hits="0"/>
						<line number="159" hits="0"/>
						<line number="161" hits="0"/>
						<line number="166" hits="0"/>
						<line number="168" hits="0"/>
						<line number="176" hits="0"/>
						<line number="179" hits="1"/>
						<line number="184" hits="1"/>
						<line number="186" hits="1"/>
						<line number="187" hits="0"/>
						<line number="191" hits="1"/>
						<line number="192" hits="0"/>
						<line number="196" hits="1"/>
						<line number="199" hits="1"/>
						<line number="204" hits="1"/>
						<line number="205" hits="0"/>
						<line number="209" hits="1"/>
						<line number="212" hits="1"/>
						<line number="216" hits="1"/>
						<line number="218" hits="1"/>
						<line number="219" hits="0"/>
						<line number="223" hits="1"/>
						<line number="224" hits="1"/>
						<line number="226" hits="1"/>
						<line number="227" hits="0"/>
						<line number="231" hits="1"/>
						<line number="236" hits="1"/>
						<line number="241" hits="1"/>
						<line number="246" hits="1"/>
						<line number="251" hits="1"/>
						<line number="256" hits="1"/>
						<line number="261" hits="1"/>
						<line number="267" hits="1"/>
						<line number="268" hits="1"/>
						<line number="270" hits="1"/>
						<line number="273" hits="1"/>
						<line number="277" hits="1"/>
						<line number="330" hits="1"/>
						<line number="333" hits="1"/>
						<line number="338" hits="1"/>
						<line number="343" hits="1"/>
						<line number="347" hits="1"/>
						<line number="350" hits="1"/>
						<line number="351" hits="1"/>
						<line number="353" hits="1"/>
						<line number="359" hits="1"/>
						<line number="363" hits="1"/>
						<line number="368" hits="1"/>
						<line number="374" hits="1"/>
						<line number="375" hits="0"/>
						<line number="379" hits="1"/>
					</lines>
				</class>
				<class name="weather_interpolation.py" filename="services/weather_interpolation.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="3" hits="1"/>
						<line number="5" hits="1"/>
						<line number="7" hits="1"/>
						<line number="8" hits="1"/>
						<line number="11" hits="1"/>
						<line number="12" hits="1"/>
						<line number="13" hits="1"/>
						<line number="14" hits="1"/>
						<line number="15" hits="1"/>
						<line number="16" hits="1"/>
						<line number="17" hits="1"/>
						<line number="19" hits="1"/>
						<line number="20" hits="1"/>
						<line number="24" hits="1"/>
						<line number="26" hits="1"/>
						<line number="36" hits="1"/>
						<line number="68" hits="1"/>
						<line number="73" hits="1"/>
						<line number="81" hits="1"/>
						<line number="85" hits="1"/>
						<line number="90" hits="1"/>
						<line number="95" hits="1"/>
						<line number="100" hits="1"/>
						<line number="110" hits="1"/>
						<line number="117" hits="1"/>
						<line number="129" hits="1"/>
					</lines>
				</class>
				<class name="weather_simulation.py" filename="services/weather_simulation.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="3" hits="1"/>
						<line number="4" hits="1"/>
						<line number="9" hits="1"/>
						<line number="12" hits="1"/>
						<line number="17" hits="1"/>
						<line number="23" hits="1"/>
						<line number="28" hits="1"/>
						<line number="32" hits="1"/>
						<line number="33" hits="1"/>
						<line number="38" hits="1"/>
						<line number="40" hits="1"/>
						<line number="45" hits="1"/>
						<line number="55" hits="1"/>
						<line number="60" hits="1"/>
						<line number="74" hits="1"/>
						<line number="79" hits="1"/>
						<line number="93" hits="1"/>
						<line number="98" hits="1"/>
						<line number="103" hits="1"/>
						<line number="108" hits="1"/>
					</lines>
				</class>
			</classes>
		</package>
		<package name="worker" line-rate="0.5818" branch-rate="0" complexity="0">
			<classes>
				<class name="__init__.py" filename="worker/__init__.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines/>
				</class>
				<class name="celery_app.py" filename="worker/celery_app.py" complexity="0" line-rate="1" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="3" hits="1"/>
						<line number="6" hits="1"/>
						<line number="15" hits="1"/>
					</lines>
				</class>
				<class name="tasks.py" filename="worker/tasks.py" complexity="0" line-rate="0.549" branch-rate="0">
					<methods/>
					<lines>
						<line number="1" hits="1"/>
						<line number="2" hits="1"/>
						<line number="4" hits="1"/>
						<line number="6" hits="1"/>
						<line number="7" hits="1"/>
						<line number="10" hits="1"/>
						<line number="13" hits="1"/>
						<line number="16" hits="1"/>
						<line number="19" hits="1"/>
						<line number="24" hits="1"/>
						<line number="25" hits="1"/>
						<line number="28" hits="1"/>
						<line number="32" hits="1"/>
						<line number="33" hits="1"/>
						<line number="38" hits="1"/>
						<line number="39" hits="1"/>
						<line number="43" hits="1"/>
						<line number="44" hits="1"/>
						<line number="46" hits="1"/>
						<line number="49" hits="1"/>
						<line number="52" hits="1"/>
						<line number="53" hits="1"/>
						<line number="58" hits="1"/>
						<line number="59" hits="1"/>
						<line number="63" hits="1"/>
						<line number="67" hits="1"/>
						<line number="70" hits="1"/>
						<line number="75" hits="1"/>
						<line number="79" hits="0"/>
						<line number="80" hits="0"/>
						<line number="81" hits="0"/>
						<line number="86" hits="0"/>
						<line number="87" hits="0"/>
						<line number="91" hits="0"/>
						<line number="98" hits="0"/>
						<line number="109" hits="0"/>
						<line number="113" hits="0"/>
						<line number="115" hits="0"/>
						<line number="122" hits="0"/>
						<line number="131" hits="0"/>
						<line number="138" hits="0"/>
						<line number="140" hits="0"/>
						<line number="146" hits="0"/>
						<line number="151" hits="0"/>
						<line number="167" hits="0"/>
						<line number="172" hits="0"/>
						<line number="173" hits="0"/>
						<line number="182" hits="0"/>
						<line number="187" hits="0"/>
						<line number="188" hits="0"/>
						<line number="198" hits="0"/>
					</lines>
				</class>
			</classes>
		</package>
	</packages>
</coverage>

```

### File: `backend/docs/acceptance/legacy-stage-3-two-node-prototype/energy-residual.txt`
```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend
configfile: pyproject.toml
plugins: anyio-4.14.2, cov-7.1.0
collecting ... collected 1 item

tests/test_two_node.py::test_energy_balance_residual_is_small PASSED

============================== warnings summary ===============================
.venv\Lib\site-packages\fastapi\testclient.py:1
  C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend\.venv\Lib\site-packages\fastapi\testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================== 1 passed, 1 warning in 0.02s =========================

```

### File: `backend/docs/acceptance/legacy-stage-3-two-node-prototype/pytest-all.txt`
```
Python:
C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend\.venv\Scripts\python.exe
Numba cache:
C:/nc
pythermalcomfort:
C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend\.venv\Lib\site-packages\pythermalcomfort\__init__.py
開始執行測試...
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend
configfile: pyproject.toml
testpaths: tests
plugins: anyio-4.14.2, cov-7.1.0
collecting ... collected 27 items

tests/test_api.py::test_health_endpoint PASSED                           [  3%]
tests/test_api.py::test_simulation_endpoint PASSED                       [  7%]
tests/test_api.py::test_invalid_material_is_rejected PASSED              [ 11%]
tests/test_api.py::test_identical_material_api_improvement_is_zero PASSED [ 14%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[hot_dry-42.0-20.0-2.0-900.0] PASSED [ 18%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[hot_humid-34.0-85.0-1.0-700.0] PASSED [ 22%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[high_altitude_solar-24.0-25.0-2.5-1000.0] PASSED [ 25%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[night-30.0-60.0-0.5-0.0] PASSED [ 29%]
tests/test_gagge_benchmark.py::test_gagge_benchmark_returns_finite_values PASSED [ 33%]
tests/test_gagge_benchmark.py::test_gagge_output_is_in_broad_range PASSED [ 37%]
tests/test_gagge_benchmark.py::test_gagge_benchmark_api PASSED           [ 40%]
tests/test_physics.py::test_saturation_pressure_increases_with_temperature PASSED [ 44%]
tests/test_physics.py::test_saturation_pressure_near_reference_value PASSED [ 48%]
tests/test_physics.py::test_invalid_optical_sum_is_rejected PASSED       [ 51%]
tests/test_physics.py::test_higher_reflectance_reduces_solar_absorption PASSED [ 55%]
tests/test_physics.py::test_flux_calculation_is_finite[0.0] PASSED       [ 59%]
tests/test_physics.py::test_flux_calculation_is_finite[0.1] PASSED       [ 62%]
tests/test_physics.py::test_flux_calculation_is_finite[1.0] PASSED       [ 66%]
tests/test_physics.py::test_flux_calculation_is_finite[3.0] PASSED       [ 70%]
tests/test_physics.py::test_flux_calculation_is_finite[8.0] PASSED       [ 74%]
tests/test_two_node.py::test_simulation_returns_expected_number_of_points PASSED [ 77%]
tests/test_two_node.py::test_initial_temperatures_are_preserved PASSED   [ 81%]
tests/test_two_node.py::test_all_temperatures_are_finite PASSED          [ 85%]
tests/test_two_node.py::test_temperature_stays_in_broad_physiological_range PASSED [ 88%]
tests/test_two_node.py::test_energy_balance_residual_is_small PASSED     [ 92%]
tests/test_two_node.py::test_rc_material_reduces_skin_temperature PASSED [ 96%]
tests/test_two_node.py::test_identical_materials_produce_identical_results PASSED [100%]

============================== warnings summary ===============================
.venv\Lib\site-packages\fastapi\testclient.py:1
  C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend\.venv\Lib\site-packages\fastapi\testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================== 27 passed, 1 warning in 0.31s ========================

```

### File: `backend/docs/acceptance/stage-2/golden-refresh.md`
```
# Stage 2 golden refresh (Dubai 2023-07-15 12:00, 2 h)

Cause: evaporation limited by explicit Re,cl. Previous factor 1/(1 + 0.45·clo·h_c)
was equivalent to Re,cl ≈ 27.3·clo m²·Pa/W; new default derivation R_cl/(LR·i_cl)
with i_cl = 0.45 gives Re,cl ≈ 20.9·clo m²·Pa/W (control 0.5 clo: 13.6 → 10.4;
RC 0.4 clo: 10.9 → 8.4). Expect slightly lower skin temperatures for both garments.

| metric | before | after | delta |
|---|---|---|---|
| final_skin_temperature_improvement_c | 1.3193 | <fill> | |
| final_core_temperature_improvement_c | 0.6571 | <fill> | |
| average_skin_temperature_improvement_c | 0.9531 | <fill> | |

model_parameter_set_sha256: <fill>
```

### File: `backend/docs/acceptance/stage-3-reference-comparison/golden-refresh.md`
```
# Stage 3 golden refresh (Dubai 2023-07-15 12:00, 2 h)

Causes (all intentional, see ADR 0001-0003):
1. Heat capacities 280 -> 135.7 kJ/(m^2 K) (70 kg / 1.8 m^2). Transients are
   roughly twice as fast; the 2 h case is closer to steady state.
2. Explicit clothing surface temperature with f_cl = 1 + 0.15 clo replaces the
   linearised coupling factor.
3. Gagge 1986 controllers replace the prototype's linear gains.

| metric | before (2.0.0) | after (3.0.0) | delta |
|---|---|---|---|
| final_skin_temperature_improvement_c | 0.7846 | <fill> | |
| final_core_temperature_improvement_c | 0.1362 | <fill> | |
| average_skin_temperature_improvement_c | 0.43 | <fill> | |

model_parameter_set_sha256: ebc0c642... -> <fill>
Gagge benchmark (default fixture, 60 min): core max|dT| = <fill> C, skin max|dT| = <fill> C
Reference port parity (60 min, 70 kg): max|dT| = <fill> C
```

### File: `backend/docs/acceptance/stage-3-reference-comparison/pytest-all.txt`
```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend
configfile: pyproject.toml
testpaths: tests
plugins: anyio-4.14.2, asyncio-1.4.0, cov-7.1.0
asyncio: mode=Mode.AUTO, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 203 items

tests/core/test_numba_cache_integration.py::test_numba_writes_cache_files_to_configured_directory PASSED [  0%]
tests/core/test_runtime.py::test_uses_configured_cache_directory PASSED  [  0%]
tests/core/test_runtime.py::test_environment_variable_takes_precedence PASSED [  1%]
tests/core/test_runtime.py::test_uses_cross_platform_temporary_default PASSED [  1%]
tests/core/test_runtime.py::test_creates_missing_parent_directories PASSED [  2%]
tests/test_api.py::test_health_endpoint PASSED                           [  2%]
tests/test_api.py::test_simulation_endpoint PASSED                       [  3%]
tests/test_api.py::test_invalid_material_is_rejected PASSED              [  3%]
tests/test_api.py::test_identical_material_api_improvement_is_zero PASSED [  4%]
tests/test_body.py::test_default_person_reproduces_gagge_lumped_value PASSED [  4%]
tests/test_body.py::test_heavier_person_has_larger_capacity_per_area PASSED [  5%]
tests/test_body.py::test_larger_surface_area_lowers_capacity_per_area PASSED [  5%]
tests/test_cities.py::test_get_city_returns_supported_city PASSED        [  6%]
tests/test_cities.py::test_get_city_normalizes_case_and_spaces PASSED    [  6%]
tests/test_cities.py::test_all_configured_cities_can_be_loaded[dubai] PASSED [  7%]
tests/test_cities.py::test_all_configured_cities_can_be_loaded[guangzhou] PASSED [  7%]
tests/test_cities.py::test_all_configured_cities_can_be_loaded[lhasa] PASSED [  8%]
tests/test_cities.py::test_get_city_rejects_unknown_city PASSED          [  8%]
tests/test_cities.py::test_unknown_city_error_lists_supported_cities PASSED [  9%]
tests/test_climate_adaptation.py::test_global_batch_month_range PASSED   [  9%]
tests/test_climate_adaptation.py::test_global_batch_rejects_duplicate_cities PASSED [ 10%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[hot_dry-42.0-20.0-2.0-900.0] PASSED [ 10%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[hot_humid-34.0-85.0-1.0-700.0] PASSED [ 11%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[high_altitude_solar-24.0-25.0-2.5-1000.0] PASSED [ 11%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[night-30.0-60.0-0.5-0.0] PASSED [ 12%]
tests/test_clothing.py::test_derived_evaporative_resistance_matches_formula PASSED [ 12%]
tests/test_clothing.py::test_none_resistance_is_derived_and_flagged PASSED [ 13%]
tests/test_clothing.py::test_explicit_resistance_overrides_derivation PASSED [ 13%]
tests/test_clothing.py::test_higher_resistance_lowers_maximum_evaporation PASSED [ 14%]
tests/test_clothing.py::test_explicit_derived_value_reproduces_none_result PASSED [ 14%]
tests/test_clothing.py::test_impermeable_garment_ends_warmer PASSED      [ 15%]
tests/test_clothing.py::test_infrared_transmittance_amplifies_longwave_exchange PASSED [ 15%]
tests/test_clothing.py::test_area_factor_is_derived_and_flagged PASSED   [ 16%]
tests/test_clothing.py::test_explicit_area_factor_overrides_derivation PASSED [ 16%]
tests/test_clothing.py::test_clothing_surface_balance_is_consistent PASSED [ 17%]
tests/test_clothing.py::test_nude_surface_temperature_equals_skin PASSED [ 17%]
tests/test_clothing.py::test_emissivity_plus_transmittance_above_one_is_rejected PASSED [ 18%]
tests/test_clothing.py::test_unknown_parameter_source_key_is_rejected PASSED [ 18%]
tests/test_cors.py::test_allows_configured_origin PASSED                 [ 19%]
tests/test_cors.py::test_allows_configured_preflight_request PASSED      [ 19%]
tests/test_cors.py::test_rejects_unknown_preflight_origin PASSED         [ 20%]
tests/test_cors.py::test_rejects_duplicate_cors_registration PASSED      [ 20%]
tests/test_cors.py::test_main_application_registers_cors_once PASSED     [ 21%]
tests/test_environment_model.py::test_defaults_reproduce_stage_1_formulas PASSED [ 21%]
tests/test_environment_model.py::test_swinbank_clear_sky PASSED          [ 22%]
tests/test_environment_model.py::test_wind_scaling_and_negative_inputs_are_clamped PASSED [ 22%]
tests/test_environment_model.py::test_describe_mentions_every_active_rule PASSED [ 23%]
tests/test_exposure_statistics.py::test_time_weighted_mean_matches_trapezoid PASSED [ 23%]
tests/test_exposure_statistics.py::test_statistics_use_exposure_window_not_padded_points PASSED [ 24%]
tests/test_exposure_statistics.py::test_statistics_are_invariant_to_padding[1] PASSED [ 24%]
tests/test_exposure_statistics.py::test_statistics_are_invariant_to_padding[3] PASSED [ 25%]
tests/test_exposure_statistics.py::test_statistics_are_invariant_to_padding[6] PASSED [ 25%]
tests/test_exposure_statistics.py::test_half_hour_start_uses_interpolated_boundary PASSED [ 26%]
tests/test_gagge_benchmark.py::test_gagge_benchmark_returns_finite_values PASSED [ 26%]
tests/test_gagge_benchmark.py::test_gagge_output_is_in_broad_range PASSED [ 27%]
tests/test_gagge_benchmark.py::test_gagge_benchmark_api PASSED           [ 27%]
tests/test_gagge_benchmark.py::test_gagge_api_converts_service_error_to_500 PASSED [ 28%]
tests/test_gagge_benchmark.py::test_benchmark_returns_aligned_transient_series PASSED [ 28%]
tests/test_gagge_benchmark.py::test_default_case_is_within_stage_3_tolerances PASSED [ 29%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[38.0-45.0-1.5-40.0-2.6-0.5] PASSED [ 29%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[30.0-30.0-0.3-60.0-1.2-0.6] PASSED [ 30%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[42.0-42.0-2.0-20.0-2.0-0.4] PASSED [ 30%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[34.0-36.0-1.0-85.0-1.8-0.5] PASSED [ 31%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[25.0-25.0-0.1-50.0-1.0-1.0] PASSED [ 31%]
tests/test_gagge_reference.py::test_port_returns_one_point_per_minute_plus_initial_state PASSED [ 32%]
tests/test_gagge_reference.py::test_heavier_body_warms_more_slowly PASSED [ 32%]
tests/test_global_batch_geojson.py::test_geojson_structure PASSED        [ 33%]
tests/test_golden_dubai_2h.py::test_dubai_two_hour_golden_case PASSED    [ 33%]
tests/test_job_service.py::test_job_to_response_maps_job_fields PASSED   [ 33%]
tests/test_job_service.py::test_job_to_detail_validates_saved_request PASSED [ 34%]
tests/test_job_service.py::test_get_job_or_none_uses_session_get PASSED  [ 34%]
tests/test_job_service.py::test_get_job_or_none_returns_none PASSED      [ 35%]
tests/test_model_parameters.py::test_every_parameter_has_unit_and_reference PASSED [ 35%]
tests/test_model_parameters.py::test_manifest_sha_is_stable_and_hex PASSED [ 36%]
tests/test_model_parameters.py::test_unknown_parameter_raises PASSED     [ 36%]
tests/test_model_parameters.py::test_model_parameter_endpoint PASSED     [ 37%]
tests/test_model_parameters.py::test_default_assumptions_endpoint PASSED [ 37%]
tests/test_parameter_participation.py::test_every_material_field_participates[absorbed_solar_to_body_fraction-0.6] PASSED [ 38%]
tests/test_parameter_participation.py::test_every_material_field_participates[clothing_area_factor-1.4] PASSED [ 38%]
tests/test_parameter_participation.py::test_every_material_field_participates[clothing_insulation_clo-0.9] PASSED [ 39%]
tests/test_parameter_participation.py::test_every_material_field_participates[evaporative_resistance_m2pa_w-40.0] PASSED [ 39%]
tests/test_parameter_participation.py::test_every_material_field_participates[infrared_emissivity-0.5] PASSED [ 40%]
tests/test_parameter_participation.py::test_every_material_field_participates[infrared_transmittance-0.15] PASSED [ 40%]
tests/test_parameter_participation.py::test_every_material_field_participates[projected_solar_area_factor-0.4] PASSED [ 41%]
tests/test_parameter_participation.py::test_every_material_field_participates[solar_reflectance-0.7] PASSED [ 41%]
tests/test_parameter_participation.py::test_every_material_field_participates[solar_transmittance-0.2] PASSED [ 42%]
tests/test_parameter_participation.py::test_every_person_field_participates[body_mass_kg-95.0] PASSED [ 42%]
tests/test_parameter_participation.py::test_every_person_field_participates[body_surface_area_m2-2.4] PASSED [ 43%]
tests/test_parameter_participation.py::test_every_person_field_participates[initial_core_temperature_c-37.4] PASSED [ 43%]
tests/test_parameter_participation.py::test_every_person_field_participates[initial_skin_temperature_c-31.0] PASSED [ 44%]
tests/test_parameter_participation.py::test_every_person_field_participates[met-1.2] PASSED [ 44%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update0-perturbed_update0] PASSED [ 45%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update1-perturbed_update1] PASSED [ 45%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update2-perturbed_update2] PASSED [ 46%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update3-perturbed_update3] PASSED [ 46%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update4-perturbed_update4] PASSED [ 47%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update5-perturbed_update5] PASSED [ 47%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update6-perturbed_update6] PASSED [ 48%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update7-perturbed_update7] PASSED [ 48%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update8-perturbed_update8] PASSED [ 49%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update9-perturbed_update9] PASSED [ 49%]
tests/test_physics.py::test_saturation_pressure_increases_with_temperature PASSED [ 50%]
tests/test_physics.py::test_saturation_pressure_near_reference_value PASSED [ 50%]
tests/test_physics.py::test_invalid_optical_sum_is_rejected PASSED       [ 51%]
tests/test_physics.py::test_higher_reflectance_reduces_solar_absorption PASSED [ 51%]
tests/test_physics.py::test_flux_calculation_is_finite[0.0] PASSED       [ 52%]
tests/test_physics.py::test_flux_calculation_is_finite[0.1] PASSED       [ 52%]
tests/test_physics.py::test_flux_calculation_is_finite[1.0] PASSED       [ 53%]
tests/test_physics.py::test_flux_calculation_is_finite[3.0] PASSED       [ 53%]
tests/test_physics.py::test_flux_calculation_is_finite[8.0] PASSED       [ 54%]
tests/test_result_export.py::test_missing_stage_3_diagnostics_export_as_blank_cells PASSED [ 54%]
tests/test_result_export.py::test_stage_3_diagnostics_are_exported_when_present PASSED [ 55%]
tests/test_result_export.py::test_result_csv_contains_expected_headers PASSED [ 55%]
tests/test_result_export.py::test_result_csv_contains_control_and_rc_values PASSED [ 56%]
tests/test_result_export.py::test_result_csv_with_empty_time_series_contains_only_headers PASSED [ 56%]
tests/test_result_export.py::test_result_csv_rejects_different_time_series_lengths PASSED [ 57%]
tests/test_result_export.py::test_result_json_serializes_model_dump_as_unicode PASSED [ 57%]
tests/test_result_storage.py::test_save_simulation_result_creates_gzip_json_file PASSED [ 58%]
tests/test_result_storage.py::test_save_simulation_result_creates_missing_directory PASSED [ 58%]
tests/test_result_storage.py::test_save_simulation_result_removes_temporary_file PASSED [ 59%]
tests/test_result_storage.py::test_save_simulation_result_preserves_unicode PASSED [ 59%]
tests/test_result_storage.py::test_save_simulation_result_replaces_existing_file PASSED [ 60%]
tests/test_result_storage.py::test_load_simulation_result_reads_and_validates_payload PASSED [ 60%]
tests/test_result_storage.py::test_load_simulation_result_raises_for_missing_file PASSED [ 61%]
tests/test_spectrum_parser.py::test_parse_valid_spectrum_csv PASSED      [ 61%]
tests/test_spectrum_parser.py::test_reject_value_above_one PASSED        [ 62%]
tests/test_spectrum_parser.py::test_reject_unsorted_wavelengths PASSED   [ 62%]
tests/test_spectrum_parser.py::test_parse_spectrum_returns_checksum PASSED [ 63%]
tests/test_spectrum_parser.py::test_parse_normalizes_header_names PASSED [ 63%]
tests/test_spectrum_parser.py::test_reject_empty_spectrum PASSED         [ 64%]
tests/test_spectrum_parser.py::test_reject_non_utf8_spectrum PASSED      [ 64%]
tests/test_spectrum_parser.py::test_reject_missing_wavelength_column PASSED [ 65%]
tests/test_spectrum_parser.py::test_reject_missing_value_column PASSED   [ 65%]
tests/test_spectrum_parser.py::test_reject_invalid_numeric_values[not-a-number,0.8] PASSED [ 66%]
tests/test_spectrum_parser.py::test_reject_invalid_numeric_values[0.3,not-a-number] PASSED [ 66%]
tests/test_spectrum_parser.py::test_reject_invalid_spectrum_ranges[nan,0.8-wavelength] PASSED [ 66%]
tests/test_spectrum_parser.py::test_reject_invalid_spectrum_ranges[0.3,nan-spectrum value] PASSED [ 67%]
tests/test_spectrum_parser.py::test_reject_invalid_spectrum_ranges[-0.3,0.8-positive] PASSED [ 67%]
tests/test_spectrum_parser.py::test_reject_invalid_spectrum_ranges[0.3,-0.1-between 0 and 1] PASSED [ 68%]
tests/test_spectrum_parser.py::test_reject_single_data_point PASSED      [ 68%]
tests/test_spectrum_parser.py::test_reject_file_above_size_limit PASSED  [ 69%]
tests/test_spectrum_parser.py::test_reject_too_many_points PASSED        [ 69%]
tests/test_stage_4_2_export.py::test_export_contains_required_files PASSED [ 70%]
tests/test_stage_4_2_exposure.py::test_all_mode_requires_all_thresholds PASSED [ 70%]
tests/test_stage_4_2_exposure.py::test_any_mode_requires_one_threshold PASSED [ 71%]
tests/test_stage_4_2_exposure.py::test_no_threshold_means_all_samples_eligible PASSED [ 71%]
tests/test_stage_4_2_sampling.py::test_three_samples_cover_entire_month PASSED [ 72%]
tests/test_stage_4_2_sampling.py::test_one_legacy_sample_uses_requested_day PASSED [ 72%]
tests/test_stage_4_2_sampling.py::test_sample_count_cannot_exceed_month_days PASSED [ 73%]
tests/test_stage_4_3_estimate.py::test_daily_batch_estimate PASSED       [ 73%]
tests/test_stage_4_3_sampling.py::test_daily_stride_one_has_one_sample_per_day PASSED [ 74%]
tests/test_stage_4_3_sampling.py::test_daily_stride_seven_covers_month PASSED [ 74%]
tests/test_stage_4_3_sampling.py::test_leap_year_daily_plan_has_366_samples PASSED [ 75%]
tests/test_stage_4_3_sampling.py::test_month_plan_returns_actual_dates PASSED [ 75%]
tests/test_stage_4_3_weather_slice.py::test_slice_weather_includes_padding PASSED [ 76%]
tests/test_stage_4_3_weather_slice.py::test_slice_fails_when_range_not_covered PASSED [ 76%]
tests/test_stage_4_4_analytics.py::test_weighted_percentile PASSED       [ 77%]
tests/test_stage_4_4_analytics.py::test_weighted_percentile_uses_weights PASSED [ 77%]
tests/test_stage_4_4_analytics.py::test_detects_consecutive_heatwave PASSED [ 78%]
tests/test_stage_4_4_analytics.py::test_non_consecutive_hot_days_are_not_heatwave PASSED [ 78%]
tests/test_stage_4_4_checkpoint.py::test_retry_preserves_checkpoint_when_enabled PASSED [ 79%]
tests/test_stage_4_4_checkpoint.py::test_monthly_checkpoint_round_trip PASSED [ 79%]
tests/test_two_node.py::test_simulation_returns_expected_number_of_points PASSED [ 80%]
tests/test_two_node.py::test_initial_temperatures_are_preserved PASSED   [ 80%]
tests/test_two_node.py::test_all_temperatures_are_finite PASSED          [ 81%]
tests/test_two_node.py::test_temperature_stays_in_broad_physiological_range PASSED [ 81%]
tests/test_two_node.py::test_energy_balance_residual_is_small PASSED     [ 82%]
tests/test_two_node.py::test_rc_material_reduces_skin_temperature PASSED [ 82%]
tests/test_two_node.py::test_identical_materials_produce_identical_results PASSED [ 83%]
tests/test_weather_api.py::test_weather_cities_endpoint PASSED           [ 83%]
tests/test_weather_api.py::test_weather_history_endpoint PASSED          [ 84%]
tests/test_weather_api.py::test_weather_history_rejects_unknown_city PASSED [ 84%]
tests/test_weather_api.py::test_weather_history_converts_service_error_to_502 PASSED [ 85%]
tests/test_weather_api.py::test_weather_history_validates_duration[0] PASSED [ 85%]
tests/test_weather_api.py::test_weather_history_validates_duration[1441] PASSED [ 86%]
tests/test_weather_interpolation.py::test_weather_interpolation_at_start PASSED [ 86%]
tests/test_weather_interpolation.py::test_weather_interpolation_at_half_hour PASSED [ 87%]
tests/test_weather_interpolation.py::test_environment_clamps_negative_wind_and_solar PASSED [ 87%]
tests/test_weather_interpolation.py::test_mean_radiant_temperature_increase_is_capped PASSED [ 88%]
tests/test_weather_interpolation.py::test_interpolation_outside_range_raises PASSED [ 88%]
tests/test_weather_interpolation.py::test_interpolation_at_exact_boundaries_is_allowed PASSED [ 89%]
tests/test_weather_interpolation.py::test_from_series_rejects_series_not_covering_requested_window PASSED [ 89%]
tests/test_weather_quality.py::test_unsorted_input_is_sorted_and_noted PASSED [ 90%]
tests/test_weather_quality.py::test_identical_duplicate_is_removed PASSED [ 90%]
tests/test_weather_quality.py::test_conflicting_duplicate_is_rejected PASSED [ 91%]
tests/test_weather_quality.py::test_naive_timestamp_is_rejected PASSED   [ 91%]
tests/test_weather_quality.py::test_gap_is_reported_but_not_raised_by_normalize PASSED [ 92%]
tests/test_weather_quality.py::test_window_with_gap_inside_is_rejected PASSED [ 92%]
tests/test_weather_quality.py::test_window_outside_gap_is_accepted PASSED [ 93%]
tests/test_weather_quality.py::test_missing_tail_is_rejected PASSED      [ 93%]
tests/test_weather_quality.py::test_exact_boundaries_are_accepted PASSED [ 94%]
tests/test_weather_service.py::test_historical_weather_with_mock PASSED  [ 94%]
tests/test_weather_simulation.py::test_execute_weather_simulation PASSED [ 95%]
tests/test_weather_simulation.py::test_execute_weather_simulation_without_callback PASSED [ 95%]
tests/test_worker_tasks.py::test_update_job_updates_fields_and_commits PASSED [ 96%]
tests/test_worker_tasks.py::test_update_job_rejects_missing_job PASSED   [ 96%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_accepts_active_status[queued] PASSED [ 97%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_accepts_active_status[running] PASSED [ 97%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_accepts_active_status[completed] PASSED [ 98%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_accepts_active_status[failed] PASSED [ 98%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_raises_for_cancelled_job[cancelling] PASSED [ 99%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_raises_for_cancelled_job[cancelled] PASSED [ 99%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_rejects_missing_job PASSED [100%]

============================= 203 passed in 2.83s =============================

```

### File: `backend/docs/acceptance/stage-4-material-library/pytest-all.txt`
```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\lenovo\Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform\radiative-cooling-platform\backend
configfile: pyproject.toml
testpaths: tests
plugins: anyio-4.14.2, asyncio-1.4.0, cov-7.1.0
asyncio: mode=Mode.AUTO, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 229 items

tests/core/test_numba_cache_integration.py::test_numba_writes_cache_files_to_configured_directory PASSED [  0%]
tests/core/test_runtime.py::test_uses_configured_cache_directory PASSED  [  0%]
tests/core/test_runtime.py::test_environment_variable_takes_precedence PASSED [  1%]
tests/core/test_runtime.py::test_uses_cross_platform_temporary_default PASSED [  1%]
tests/core/test_runtime.py::test_creates_missing_parent_directories PASSED [  2%]
tests/test_api.py::test_health_endpoint PASSED                           [  2%]
tests/test_api.py::test_simulation_endpoint PASSED                       [  3%]
tests/test_api.py::test_invalid_material_is_rejected PASSED              [  3%]
tests/test_api.py::test_identical_material_api_improvement_is_zero PASSED [  3%]
tests/test_body.py::test_default_person_reproduces_gagge_lumped_value PASSED [  4%]
tests/test_body.py::test_heavier_person_has_larger_capacity_per_area PASSED [  4%]
tests/test_body.py::test_larger_surface_area_lowers_capacity_per_area PASSED [  5%]
tests/test_cities.py::test_get_city_returns_supported_city PASSED        [  5%]
tests/test_cities.py::test_get_city_normalizes_case_and_spaces PASSED    [  6%]
tests/test_cities.py::test_all_configured_cities_can_be_loaded[dubai] PASSED [  6%]
tests/test_cities.py::test_all_configured_cities_can_be_loaded[guangzhou] PASSED [  6%]
tests/test_cities.py::test_all_configured_cities_can_be_loaded[lhasa] PASSED [  7%]
tests/test_cities.py::test_get_city_rejects_unknown_city PASSED          [  7%]
tests/test_cities.py::test_unknown_city_error_lists_supported_cities PASSED [  8%]
tests/test_climate_adaptation.py::test_global_batch_month_range PASSED   [  8%]
tests/test_climate_adaptation.py::test_global_batch_rejects_duplicate_cities PASSED [  9%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[hot_dry-42.0-20.0-2.0-900.0] PASSED [  9%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[hot_humid-34.0-85.0-1.0-700.0] PASSED [ 10%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[high_altitude_solar-24.0-25.0-2.5-1000.0] PASSED [ 10%]
tests/test_climate_scenarios.py::test_typical_climate_scenarios_run_successfully[night-30.0-60.0-0.5-0.0] PASSED [ 10%]
tests/test_clothing.py::test_derived_evaporative_resistance_matches_formula PASSED [ 11%]
tests/test_clothing.py::test_none_resistance_is_derived_and_flagged PASSED [ 11%]
tests/test_clothing.py::test_explicit_resistance_overrides_derivation PASSED [ 12%]
tests/test_clothing.py::test_higher_resistance_lowers_maximum_evaporation PASSED [ 12%]
tests/test_clothing.py::test_explicit_derived_value_reproduces_none_result PASSED [ 13%]
tests/test_clothing.py::test_impermeable_garment_ends_warmer PASSED      [ 13%]
tests/test_clothing.py::test_infrared_transmittance_amplifies_longwave_exchange PASSED [ 13%]
tests/test_clothing.py::test_area_factor_is_derived_and_flagged PASSED   [ 14%]
tests/test_clothing.py::test_explicit_area_factor_overrides_derivation PASSED [ 14%]
tests/test_clothing.py::test_clothing_surface_balance_is_consistent PASSED [ 15%]
tests/test_clothing.py::test_nude_surface_temperature_equals_skin PASSED [ 15%]
tests/test_clothing.py::test_emissivity_plus_transmittance_above_one_is_rejected PASSED [ 16%]
tests/test_clothing.py::test_unknown_parameter_source_key_is_rejected PASSED [ 16%]
tests/test_cors.py::test_allows_configured_origin PASSED                 [ 17%]
tests/test_cors.py::test_allows_configured_preflight_request PASSED      [ 17%]
tests/test_cors.py::test_rejects_unknown_preflight_origin PASSED         [ 17%]
tests/test_cors.py::test_rejects_duplicate_cors_registration PASSED      [ 18%]
tests/test_cors.py::test_main_application_registers_cors_once PASSED     [ 18%]
tests/test_environment_model.py::test_defaults_reproduce_stage_1_formulas PASSED [ 19%]
tests/test_environment_model.py::test_swinbank_clear_sky PASSED          [ 19%]
tests/test_environment_model.py::test_wind_scaling_and_negative_inputs_are_clamped PASSED [ 20%]
tests/test_environment_model.py::test_describe_mentions_every_active_rule PASSED [ 20%]
tests/test_exposure_statistics.py::test_time_weighted_mean_matches_trapezoid PASSED [ 20%]
tests/test_exposure_statistics.py::test_statistics_use_exposure_window_not_padded_points PASSED [ 21%]
tests/test_exposure_statistics.py::test_statistics_are_invariant_to_padding[1] PASSED [ 21%]
tests/test_exposure_statistics.py::test_statistics_are_invariant_to_padding[3] PASSED [ 22%]
tests/test_exposure_statistics.py::test_statistics_are_invariant_to_padding[6] PASSED [ 22%]
tests/test_exposure_statistics.py::test_half_hour_start_uses_interpolated_boundary PASSED [ 23%]
tests/test_gagge_benchmark.py::test_gagge_benchmark_returns_finite_values PASSED [ 23%]
tests/test_gagge_benchmark.py::test_gagge_output_is_in_broad_range PASSED [ 24%]
tests/test_gagge_benchmark.py::test_gagge_benchmark_api PASSED           [ 24%]
tests/test_gagge_benchmark.py::test_gagge_api_converts_service_error_to_500 PASSED [ 24%]
tests/test_gagge_benchmark.py::test_benchmark_returns_aligned_transient_series PASSED [ 25%]
tests/test_gagge_benchmark.py::test_default_case_is_within_stage_3_tolerances PASSED [ 25%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[38.0-45.0-1.5-40.0-2.6-0.5] PASSED [ 26%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[30.0-30.0-0.3-60.0-1.2-0.6] PASSED [ 26%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[42.0-42.0-2.0-20.0-2.0-0.4] PASSED [ 27%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[34.0-36.0-1.0-85.0-1.8-0.5] PASSED [ 27%]
tests/test_gagge_reference.py::test_port_matches_library_after_sixty_minutes[25.0-25.0-0.1-50.0-1.0-1.0] PASSED [ 27%]
tests/test_gagge_reference.py::test_port_returns_one_point_per_minute_plus_initial_state PASSED [ 28%]
tests/test_gagge_reference.py::test_heavier_body_warms_more_slowly PASSED [ 28%]
tests/test_global_batch_geojson.py::test_geojson_structure PASSED        [ 29%]
tests/test_golden_dubai_2h.py::test_dubai_two_hour_golden_case PASSED    [ 29%]
tests/test_job_service.py::test_job_to_response_maps_job_fields PASSED   [ 30%]
tests/test_job_service.py::test_job_to_detail_validates_saved_request PASSED [ 30%]
tests/test_job_service.py::test_get_job_or_none_uses_session_get PASSED  [ 31%]
tests/test_job_service.py::test_get_job_or_none_returns_none PASSED      [ 31%]
tests/test_material_fields.py::test_manifest_covers_every_physical_field_in_order PASSED [ 31%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[clothing_insulation_clo] PASSED [ 32%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[evaporative_resistance_m2pa_w] PASSED [ 32%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[clothing_area_factor] PASSED [ 33%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[solar_reflectance] PASSED [ 33%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[solar_transmittance] PASSED [ 34%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[infrared_emissivity] PASSED [ 34%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[infrared_transmittance] PASSED [ 34%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[projected_solar_area_factor] PASSED [ 35%]
tests/test_material_fields.py::test_manifest_bounds_match_validation[absorbed_solar_to_body_fraction] PASSED [ 35%]
tests/test_material_fields.py::test_nullable_fields_declare_their_derivation PASSED [ 36%]
tests/test_material_resolution.py::test_input_without_version_id_is_returned_untouched PASSED [ 36%]
tests/test_material_resolution.py::test_omitted_fields_are_hydrated_from_the_version PASSED [ 37%]
tests/test_material_resolution.py::test_matching_explicit_values_are_accepted PASSED [ 37%]
tests/test_material_resolution.py::test_conflicting_explicit_value_is_rejected PASSED [ 37%]
tests/test_material_resolution.py::test_explicit_null_against_stored_value_is_a_conflict PASSED [ 38%]
tests/test_material_resolution.py::test_unknown_version_raises PASSED    [ 38%]
tests/test_material_resolution.py::test_legacy_version_outside_bounds_is_reported PASSED [ 39%]
tests/test_material_resolution.py::test_display_name_is_truncated_to_input_limit PASSED [ 39%]
tests/test_material_resolution.py::test_request_level_resolution_only_replaces_linked_materials PASSED [ 40%]
tests/test_materials_api.py::test_material_library_round_trip PASSED     [ 40%]
tests/test_materials_api.py::test_version_with_unknown_provenance_key_is_rejected_on_write PASSED [ 41%]
tests/test_model_parameters.py::test_every_parameter_has_unit_and_reference PASSED [ 41%]
tests/test_model_parameters.py::test_manifest_sha_is_stable_and_hex PASSED [ 41%]
tests/test_model_parameters.py::test_unknown_parameter_raises PASSED     [ 42%]
tests/test_model_parameters.py::test_model_parameter_endpoint PASSED     [ 42%]
tests/test_model_parameters.py::test_default_assumptions_endpoint PASSED [ 43%]
tests/test_model_parameters.py::test_model_metadata_endpoint PASSED      [ 43%]
tests/test_model_parameters.py::test_single_parameter_endpoint PASSED    [ 44%]
tests/test_model_parameters.py::test_material_fields_endpoint PASSED     [ 44%]
tests/test_parameter_participation.py::test_every_material_field_participates[absorbed_solar_to_body_fraction-0.6] PASSED [ 44%]
tests/test_parameter_participation.py::test_every_material_field_participates[clothing_area_factor-1.4] PASSED [ 45%]
tests/test_parameter_participation.py::test_every_material_field_participates[clothing_insulation_clo-0.9] PASSED [ 45%]
tests/test_parameter_participation.py::test_every_material_field_participates[evaporative_resistance_m2pa_w-40.0] PASSED [ 46%]
tests/test_parameter_participation.py::test_every_material_field_participates[infrared_emissivity-0.5] PASSED [ 46%]
tests/test_parameter_participation.py::test_every_material_field_participates[infrared_transmittance-0.15] PASSED [ 47%]
tests/test_parameter_participation.py::test_every_material_field_participates[projected_solar_area_factor-0.4] PASSED [ 47%]
tests/test_parameter_participation.py::test_every_material_field_participates[solar_reflectance-0.7] PASSED [ 48%]
tests/test_parameter_participation.py::test_every_material_field_participates[solar_transmittance-0.2] PASSED [ 48%]
tests/test_parameter_participation.py::test_every_person_field_participates[body_mass_kg-95.0] PASSED [ 48%]
tests/test_parameter_participation.py::test_every_person_field_participates[body_surface_area_m2-2.4] PASSED [ 49%]
tests/test_parameter_participation.py::test_every_person_field_participates[initial_core_temperature_c-37.4] PASSED [ 49%]
tests/test_parameter_participation.py::test_every_person_field_participates[initial_skin_temperature_c-31.0] PASSED [ 50%]
tests/test_parameter_participation.py::test_every_person_field_participates[met-1.2] PASSED [ 50%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update0-perturbed_update0] PASSED [ 51%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update1-perturbed_update1] PASSED [ 51%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update2-perturbed_update2] PASSED [ 51%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update3-perturbed_update3] PASSED [ 52%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update4-perturbed_update4] PASSED [ 52%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update5-perturbed_update5] PASSED [ 53%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update6-perturbed_update6] PASSED [ 53%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update7-perturbed_update7] PASSED [ 54%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update8-perturbed_update8] PASSED [ 54%]
tests/test_parameter_participation.py::test_every_environment_assumption_participates[baseline_update9-perturbed_update9] PASSED [ 55%]
tests/test_physics.py::test_saturation_pressure_increases_with_temperature PASSED [ 55%]
tests/test_physics.py::test_saturation_pressure_near_reference_value PASSED [ 55%]
tests/test_physics.py::test_invalid_optical_sum_is_rejected PASSED       [ 56%]
tests/test_physics.py::test_higher_reflectance_reduces_solar_absorption PASSED [ 56%]
tests/test_physics.py::test_flux_calculation_is_finite[0.0] PASSED       [ 57%]
tests/test_physics.py::test_flux_calculation_is_finite[0.1] PASSED       [ 57%]
tests/test_physics.py::test_flux_calculation_is_finite[1.0] PASSED       [ 58%]
tests/test_physics.py::test_flux_calculation_is_finite[3.0] PASSED       [ 58%]
tests/test_physics.py::test_flux_calculation_is_finite[8.0] PASSED       [ 58%]
tests/test_result_export.py::test_missing_stage_3_diagnostics_export_as_blank_cells PASSED [ 59%]
tests/test_result_export.py::test_stage_3_diagnostics_are_exported_when_present PASSED [ 59%]
tests/test_result_export.py::test_result_csv_contains_expected_headers PASSED [ 60%]
tests/test_result_export.py::test_result_csv_contains_control_and_rc_values PASSED [ 60%]
tests/test_result_export.py::test_result_csv_with_empty_time_series_contains_only_headers PASSED [ 61%]
tests/test_result_export.py::test_result_csv_rejects_different_time_series_lengths PASSED [ 61%]
tests/test_result_export.py::test_result_json_serializes_model_dump_as_unicode PASSED [ 62%]
tests/test_result_storage.py::test_save_simulation_result_creates_gzip_json_file PASSED [ 62%]
tests/test_result_storage.py::test_save_simulation_result_creates_missing_directory PASSED [ 62%]
tests/test_result_storage.py::test_save_simulation_result_removes_temporary_file PASSED [ 63%]
tests/test_result_storage.py::test_save_simulation_result_preserves_unicode PASSED [ 63%]
tests/test_result_storage.py::test_save_simulation_result_replaces_existing_file PASSED [ 64%]
tests/test_result_storage.py::test_load_simulation_result_reads_and_validates_payload PASSED [ 64%]
tests/test_result_storage.py::test_load_simulation_result_raises_for_missing_file PASSED [ 65%]
tests/test_route_registration.py::test_method_and_path_pairs_are_unique PASSED [ 65%]
tests/test_spectrum_parser.py::test_parse_valid_spectrum_csv PASSED      [ 65%]
tests/test_spectrum_parser.py::test_reject_value_above_one PASSED        [ 66%]
tests/test_spectrum_parser.py::test_reject_unsorted_wavelengths PASSED   [ 66%]
tests/test_spectrum_parser.py::test_parse_spectrum_returns_checksum PASSED [ 67%]
tests/test_spectrum_parser.py::test_parse_normalizes_header_names PASSED [ 67%]
tests/test_spectrum_parser.py::test_reject_empty_spectrum PASSED         [ 68%]
tests/test_spectrum_parser.py::test_reject_non_utf8_spectrum PASSED      [ 68%]
tests/test_spectrum_parser.py::test_reject_missing_wavelength_column PASSED [ 68%]
tests/test_spectrum_parser.py::test_reject_missing_value_column PASSED   [ 69%]
tests/test_spectrum_parser.py::test_reject_invalid_numeric_values[not-a-number,0.8] PASSED [ 69%]
tests/test_spectrum_parser.py::test_reject_invalid_numeric_values[0.3,not-a-number] PASSED [ 70%]
tests/test_spectrum_parser.py::test_reject_invalid_spectrum_ranges[nan,0.8-wavelength] PASSED [ 70%]
tests/test_spectrum_parser.py::test_reject_invalid_spectrum_ranges[0.3,nan-spectrum value] PASSED [ 71%]
tests/test_spectrum_parser.py::test_reject_invalid_spectrum_ranges[-0.3,0.8-positive] PASSED [ 71%]
tests/test_spectrum_parser.py::test_reject_invalid_spectrum_ranges[0.3,-0.1-between 0 and 1] PASSED [ 72%]
tests/test_spectrum_parser.py::test_reject_single_data_point PASSED      [ 72%]
tests/test_spectrum_parser.py::test_reject_file_above_size_limit PASSED  [ 72%]
tests/test_spectrum_parser.py::test_reject_too_many_points PASSED        [ 73%]
tests/test_stage_4_2_export.py::test_export_contains_required_files PASSED [ 73%]
tests/test_stage_4_2_exposure.py::test_all_mode_requires_all_thresholds PASSED [ 74%]
tests/test_stage_4_2_exposure.py::test_any_mode_requires_one_threshold PASSED [ 74%]
tests/test_stage_4_2_exposure.py::test_no_threshold_means_all_samples_eligible PASSED [ 75%]
tests/test_stage_4_2_sampling.py::test_three_samples_cover_entire_month PASSED [ 75%]
tests/test_stage_4_2_sampling.py::test_one_legacy_sample_uses_requested_day PASSED [ 75%]
tests/test_stage_4_2_sampling.py::test_sample_count_cannot_exceed_month_days PASSED [ 76%]
tests/test_stage_4_3_estimate.py::test_daily_batch_estimate PASSED       [ 76%]
tests/test_stage_4_3_sampling.py::test_daily_stride_one_has_one_sample_per_day PASSED [ 77%]
tests/test_stage_4_3_sampling.py::test_daily_stride_seven_covers_month PASSED [ 77%]
tests/test_stage_4_3_sampling.py::test_leap_year_daily_plan_has_366_samples PASSED [ 78%]
tests/test_stage_4_3_sampling.py::test_month_plan_returns_actual_dates PASSED [ 78%]
tests/test_stage_4_3_weather_slice.py::test_slice_weather_includes_padding PASSED [ 79%]
tests/test_stage_4_3_weather_slice.py::test_slice_fails_when_range_not_covered PASSED [ 79%]
tests/test_stage_4_4_analytics.py::test_weighted_percentile PASSED       [ 79%]
tests/test_stage_4_4_analytics.py::test_weighted_percentile_uses_weights PASSED [ 80%]
tests/test_stage_4_4_analytics.py::test_detects_consecutive_heatwave PASSED [ 80%]
tests/test_stage_4_4_analytics.py::test_non_consecutive_hot_days_are_not_heatwave PASSED [ 81%]
tests/test_stage_4_4_checkpoint.py::test_retry_preserves_checkpoint_when_enabled PASSED [ 81%]
tests/test_stage_4_4_checkpoint.py::test_monthly_checkpoint_round_trip PASSED [ 82%]
tests/test_two_node.py::test_simulation_returns_expected_number_of_points PASSED [ 82%]
tests/test_two_node.py::test_initial_temperatures_are_preserved PASSED   [ 82%]
tests/test_two_node.py::test_all_temperatures_are_finite PASSED          [ 83%]
tests/test_two_node.py::test_temperature_stays_in_broad_physiological_range PASSED [ 83%]
tests/test_two_node.py::test_energy_balance_residual_is_small PASSED     [ 84%]
tests/test_two_node.py::test_rc_material_reduces_skin_temperature PASSED [ 84%]
tests/test_two_node.py::test_identical_materials_produce_identical_results PASSED [ 85%]
tests/test_weather_api.py::test_weather_cities_endpoint PASSED           [ 85%]
tests/test_weather_api.py::test_weather_history_endpoint PASSED          [ 86%]
tests/test_weather_api.py::test_weather_history_rejects_unknown_city PASSED [ 86%]
tests/test_weather_api.py::test_weather_history_converts_service_error_to_502 PASSED [ 86%]
tests/test_weather_api.py::test_weather_history_validates_duration[0] PASSED [ 87%]
tests/test_weather_api.py::test_weather_history_validates_duration[1441] PASSED [ 87%]
tests/test_weather_interpolation.py::test_weather_interpolation_at_start PASSED [ 88%]
tests/test_weather_interpolation.py::test_weather_interpolation_at_half_hour PASSED [ 88%]
tests/test_weather_interpolation.py::test_environment_clamps_negative_wind_and_solar PASSED [ 89%]
tests/test_weather_interpolation.py::test_mean_radiant_temperature_increase_is_capped PASSED [ 89%]
tests/test_weather_interpolation.py::test_interpolation_outside_range_raises PASSED [ 89%]
tests/test_weather_interpolation.py::test_interpolation_at_exact_boundaries_is_allowed PASSED [ 90%]
tests/test_weather_interpolation.py::test_from_series_rejects_series_not_covering_requested_window PASSED [ 90%]
tests/test_weather_quality.py::test_unsorted_input_is_sorted_and_noted PASSED [ 91%]
tests/test_weather_quality.py::test_identical_duplicate_is_removed PASSED [ 91%]
tests/test_weather_quality.py::test_conflicting_duplicate_is_rejected PASSED [ 92%]
tests/test_weather_quality.py::test_naive_timestamp_is_rejected PASSED   [ 92%]
tests/test_weather_quality.py::test_gap_is_reported_but_not_raised_by_normalize PASSED [ 93%]
tests/test_weather_quality.py::test_window_with_gap_inside_is_rejected PASSED [ 93%]
tests/test_weather_quality.py::test_window_outside_gap_is_accepted PASSED [ 93%]
tests/test_weather_quality.py::test_missing_tail_is_rejected PASSED      [ 94%]
tests/test_weather_quality.py::test_exact_boundaries_are_accepted PASSED [ 94%]
tests/test_weather_service.py::test_historical_weather_with_mock PASSED  [ 95%]
tests/test_weather_simulation.py::test_execute_weather_simulation PASSED [ 95%]
tests/test_weather_simulation.py::test_execute_weather_simulation_without_callback PASSED [ 96%]
tests/test_worker_tasks.py::test_update_job_updates_fields_and_commits PASSED [ 96%]
tests/test_worker_tasks.py::test_update_job_rejects_missing_job PASSED   [ 96%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_accepts_active_status[queued] PASSED [ 97%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_accepts_active_status[running] PASSED [ 97%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_accepts_active_status[completed] PASSED [ 98%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_accepts_active_status[failed] PASSED [ 98%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_raises_for_cancelled_job[cancelling] PASSED [ 99%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_raises_for_cancelled_job[cancelled] PASSED [ 99%]
tests/test_worker_tasks.py::test_ensure_not_cancelled_rejects_missing_job PASSED [100%]

============================= 229 passed in 3.03s =============================

```

### File: `backend/docs/decisions/0001-body-surface-area.md`
```
# ADR 0001: body_surface_area_m2 is currently informational — RESOLVED (Stage 3)

Finding (Stage 2): heat capacities were fixed per m^2 (245 + 35 kJ/(m^2 K)), so
`PersonInput.body_surface_area_m2` had no effect and the lumped value was
about 2x the Gagge two-node value for 70 kg / 1.8 m^2.

Resolution (Stage 3, PR-1): `PersonInput.body_mass_kg` (default 70) added.
C_core = m c_p (1 - alpha) / A_D, C_skin = m c_p alpha / A_D with
c_p = 3490 J/(kg K) and alpha = 0.1 (Gagge 1986). Default person gives
135.7 kJ/(m^2 K), matching the reference model. alpha is kept constant
(Gagge varies it with skin blood flow) so node capacities are state-independent
and the energy diagnostics stay exact. `test_body_surface_area_participates`
xfail removed; both fields are now covered by test_parameter_participation.
```

### File: `backend/docs/decisions/0002-gagge-controllers.md`
```
# ADR 0002: adopt the Gagge (1986) thermoregulatory controllers

Context: the prototype used separate linear gains for sweating and skin blood
flow (170/200 g/(h m^2 K), 75/20 kg/(h m^2 K)) marked `assumed`. A transient
comparison with the reference cannot separate controller differences from
clothing/radiation differences while these remain arbitrary.

Decision: use the controllers of Gagge, Fobelets & Berglund (1986) as
implemented in the ASHRAE 55 SET reference procedure:
- m_rsw = 170 * WSIG_body * exp(WSIG_sk / 10.7), <= 500 g/(h m^2)
- SKBF  = (6.3 + 120 * WSIG_cr) / (1 + 0.5 * CSIG_sk), clamped [0.5, 90]
- w     = min(0.06 + 0.94 E_rsw / E_max, w_max), w_max = 0.59 v^-0.08 (clothed)
- M_shiv = 19.4 * CSIG_sk * CSIG_cr
All constants are `literature`. The platform's contribution is the clothing
optical/radiative model, not thermoregulation.

Known difference kept: when w is capped, the reference sets
E_skin = (0.06 + w_max) E_max; the prototype uses E_skin = w_max E_max.
```

### File: `backend/docs/decisions/0003-clothing-surface-balance.md`
```
# ADR 0003: explicit clothing surface temperature; solar stays on the skin node

Decision: solve (T_sk - T_cl)/R_cl = f_cl [h_c (T_cl - T_a) + eps sigma (T_cl^4 - T_env^4)]
each evaluation (Newton, monotone). f_cl = material value or 1 + 0.15 clo, and
also enters Re,a = 1/(LR f_cl h_c). The `assumed` linearised h_r is removed.
T_cl is exported (`clothing_surface_temperature_c`) because it governs the net
sky radiation of a radiative-cooling garment.

Kept simplification: absorbed solar is still deposited on the skin via
`absorbed_solar_to_body_fraction` and does not enter the surface balance.
Moving it to the surface would remove a MaterialInput field and a DB column
and requires spectral data; scheduled for Stage 4. Recorded in
`assumptions_applied` of every result.

Effective radiation area (added after the first Stage 3 benchmark run): the
surface balance and both longwave terms are scaled by A_r/A_D = 0.73
(Fanger 1970, standing). Without it the prototype exchanged ~37 % more
longwave radiation than the reference, which appeared as a +0.30 K core bias
after 60 min in the default benchmark scenario (T_mrt = 45 C > T_cl).
```

### File: `backend/docs/decisions/0004-material-library-provenance.md`
```
# ADR 0004: material library references are resolved server-side and verified

Context: `MaterialInput.material_version_id` existed since Stage 2 but had no
effect; any client could claim a version while sending different numbers.

Decision (Stage 4, PR-4):
- Resolution happens once at the API boundary (`services/material_resolution`).
  Omitted physical fields are hydrated from the immutable version; supplied
  fields must match (rel/abs 1e-9) or the request fails with
  `MATERIAL_PARAMETER_CONFLICT`. Provenance fields are hydrated when omitted.
- The resolved request is what is persisted; workers never touch the library.
- `simulation_jobs` / `global_batch_jobs` record the version ids (FK, SET NULL)
  so a material version can list the simulations that used it.
- Every stored version must be a valid `MaterialInput`: write bounds and DB
  CHECK constraints now mirror the input schema.

Not changed: physics, `MODEL_PARAMETER_SET_VERSION` (3.0.0), golden fixture.
```

### File: `backend/docs/environment-assumptions.md`
```
# Environment assumptions

ERA5 (via Open-Meteo) supplies air temperature, RH, 10 m wind and GHI.
Everything else the two-node model needs is derived by
`app/services/environment_model.py` using `EnvironmentAssumptions`, which is
part of every weather-driven request and echoed in every response.

| field | default | what it controls | status |
|---|---|---|---|
| mean_radiant_temperature_method | air_plus_solar_linear | T_mrt = T_air + min(cap, gain·GHI) | assumed (Stage 1 prototype) |
| solar_mrt_gain_k_per_w_m2 / solar_mrt_gain_cap_k | 0.012 / 15 | slope and cap above | assumed |
| sky_temperature_method | humidity_offset | T_sky = T_air − (5 + 10·(1−RH)) | assumed |
| sky_temperature_method = swinbank | — | clear-sky T_sky = 0.0552·T_air[K]^1.5 (Swinbank 1963) | literature |
| sky_view_factor | 0.5 | share of view occupied by sky | assumed; open site |
| wind_speed_scaling_factor | 1.0 | 10 m → body height | assumed; 0.67 ≈ log profile to 1.1 m |

What these do **not** represent: cloud-cover dependent sky emissivity,
ground surface temperature, urban canyon geometry, direct/diffuse split
(the solar term uses GHI only).
```

### File: `backend/docs/model-parameters.md`
```
# Model parameters

Parameter set version: `3.0.0`  
SHA-256: `5e0cbe090c73d0c64f563d0eee0001d268a9d85a2d9aa0b3d17dd353caa8bcb3`

Generated by `scripts/render_model_parameters_doc.py`. Do not edit by hand.

| name | value | unit | source type | reference | note |
|---|---|---|---|---|---|
| `stefan_boltzmann_constant` | 5.67037e-08 | W/(m^2 K^4) | standard | CODATA 2018 |  |
| `magnus_a` | 0.61078 | kPa | literature | Murray (1967) J. Appl. Meteorol. 6:203-204 |  |
| `magnus_b` | 17.2694 | - | literature | Murray (1967) J. Appl. Meteorol. 6:203-204 |  |
| `magnus_c` | 237.3 | C | literature | Murray (1967) J. Appl. Meteorol. 6:203-204 |  |
| `body_specific_heat` | 3490 | J/(kg K) | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `skin_mass_fraction` | 0.1 | - | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 | Gagge lets alpha vary with skin blood flow (alpha = 0.0418 + 0.745/(SKBF + 0.585)). Kept constant here so the node heat capacities are state-independent. |
| `natural_convection_minimum_coefficient` | 3.1 | W/(m^2 K) | literature | ASHRAE Handbook - Fundamentals (2017), Chapter 9: Thermal Comfort, Table 6 (seated, v < 0.2 m/s) |  |
| `forced_convection_coefficient` | 8.3 | W/(m^2 K (m/s)^-0.5) | literature | ASHRAE Handbook - Fundamentals (2017), Chapter 9: Thermal Comfort, Table 6 (Mitchell 1974: 8.3 v^0.6) | Exponent simplified from 0.6 to 0.5 in this prototype. |
| `effective_radiation_area_ratio` | 0.73 | - | literature | Fanger (1970) Thermal Comfort, McGraw-Hill; ASHRAE Handbook - Fundamentals (2017), Chapter 9: Thermal Comfort (0.70 seated, 0.73 standing); ASHRAE Standard 55-2020, Normative Appendix D (SET reference procedure); reference implementations: pythermalcomfort.two_nodes_gagge, comf::calc2Node | Applied to the clothing surface emission and to skin emission transmitted through IR-transparent textiles. Posture is fixed at standing; a PersonInput.position field is Stage 4 work. |
| `clo_to_si` | 0.155 | m^2 K/(W clo) | standard | ISO 9920:2007 |  |
| `clothing_area_factor_slope` | 0.15 | 1/clo | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731; ASHRAE Standard 55-2020, Normative Appendix D (SET reference procedure); reference implementations: pythermalcomfort.two_nodes_gagge, comf::calc2Node | ASHRAE Fundamentals Ch. 9 quotes 1 + 0.3 clo (McCullough & Jones 1984). 0.15 is retained for parity with the reference model. |
| `lewis_relation` | 16.5 | K/kPa | standard | ASHRAE Handbook - Fundamentals (2017), Chapter 9: Thermal Comfort |  |
| `clothing_vapor_permeation_efficiency` | 0.45 | - | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731; ASHRAE 55 SET procedure |  |
| `skin_emissivity` | 0.95 | - | literature | Steketee (1973) Phys. Med. Biol. 18:686-694 |  |
| `core_setpoint_temperature` | 36.8 | C | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `skin_setpoint_temperature` | 33.7 | C | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `sweating_gain_body` | 170 | g/(h m^2 K) | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `sweating_skin_signal_scale` | 10.7 | K | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `maximum_sweat_rate` | 500 | g/(h m^2) | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `latent_heat_of_sweat` | 0.68 | W h/g | standard | ASHRAE Handbook - Fundamentals (2017), Chapter 9: Thermal Comfort |  |
| `skin_diffusion_fraction` | 0.06 | - | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `maximum_wettedness_clothed_coefficient` | 0.59 | - | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `maximum_wettedness_clothed_exponent` | -0.08 | - | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `maximum_wettedness_nude_coefficient` | 0.38 | - | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `maximum_wettedness_nude_exponent` | -0.29 | - | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `skin_blood_flow_basal` | 6.3 | kg/(h m^2) | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `vasodilation_gain` | 120 | kg/(h m^2 K) | literature | ASHRAE Standard 55-2020, Normative Appendix D (SET reference procedure); reference implementations: pythermalcomfort.two_nodes_gagge, comf::calc2Node | ASHRAE Fundamentals Ch. 9 prints 200; 120 is the value of the SET reference code and is kept for benchmark parity. |
| `vasoconstriction_gain` | 0.5 | 1/K | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `skin_blood_flow_minimum` | 0.5 | kg/(h m^2) | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `skin_blood_flow_maximum` | 90 | kg/(h m^2) | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `core_skin_conductance_basal` | 5.28 | W/(m^2 K) | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `blood_heat_capacity_per_flow` | 1.163 | W h/(kg K) | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `shivering_coefficient` | 19.4 | W/(m^2 K^2) | literature | Gagge, Fobelets & Berglund (1986). A standard predictive index of human response to the thermal environment. ASHRAE Trans. 92(2B):709-731 |  |
| `metabolic_rate_per_met` | 58.15 | W/m^2 | standard | ISO 7730:2005 (58.2 W/m^2); ASHRAE 55 (58.15) |  |
| `respiratory_latent_coefficient` | 1.7e-05 | 1/Pa | standard | ISO 7730:2005, Annex D (Fanger 1970 respiratory heat loss) | ISO 7730 uses 1.72e-5. |
| `respiratory_reference_vapor_pressure` | 5867 | Pa | standard | ISO 7730:2005, Annex D (Fanger 1970 respiratory heat loss) |  |
| `respiratory_sensible_coefficient` | 0.0014 | 1/K | standard | ISO 7730:2005, Annex D (Fanger 1970 respiratory heat loss) |  |
| `exhaled_air_temperature` | 34 | C | standard | ISO 7730:2005, Annex D (Fanger 1970 respiratory heat loss) |  |
| `fallback_sky_temperature_offset` | 15 | K | assumed | Project prototype value (radiative-cooling-platform, Stage 0-1) |  |
| `swinbank_coefficient` | 0.0552 | K^-0.5 | literature | Swinbank (1963) Q. J. R. Meteorol. Soc. 89:339-348 |  |

```

### File: `backend/package-lock.json`
```json
{
  "name": "backend",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "devDependencies": {
        "@types/plotly.js": "^3.0.10",
        "@types/react-plotly.js": "^2.6.4"
      }
    },
    "node_modules/@types/plotly.js": {
      "version": "3.0.10",
      "resolved": "https://registry.npmjs.org/@types/plotly.js/-/plotly.js-3.0.10.tgz",
      "integrity": "sha512-q+MgO4aajC2HrO7FllTYWzrpdfbTjboSMfjkz/aXKjg1v7HNo1zMEFfAW7quKfk6SL+bH74A5ThBEps/7hZxOA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/react": {
      "version": "19.2.18",
      "resolved": "https://registry.npmjs.org/@types/react/-/react-19.2.18.tgz",
      "integrity": "sha512-AnzbBERsrLKtk2XSfTbYRLjQPdy116Sty4q+T+Bp3IC4l6jNBvreVPAHmpq9qhXQM7CXZPjLVmGMw9sy+hxQ3w==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "csstype": "^3.2.2"
      }
    },
    "node_modules/@types/react-plotly.js": {
      "version": "2.6.4",
      "resolved": "https://registry.npmjs.org/@types/react-plotly.js/-/react-plotly.js-2.6.4.tgz",
      "integrity": "sha512-AU6w1u3qEGM0NmBA69PaOgNc0KPFA/+qkH6Uu9EBTJ45/WYOUoXi9AF5O15PRM2klpHSiHAAs4WnlI+OZAFmUA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/plotly.js": "*",
        "@types/react": "*"
      }
    },
    "node_modules/csstype": {
      "version": "3.2.3",
      "resolved": "https://registry.npmjs.org/csstype/-/csstype-3.2.3.tgz",
      "integrity": "sha512-z1HGKcYy2xA8AGQfwrn0PAy+PB7X/GSj3UVJW9qKyn43xWa+gl5nXmU4qqLMRzWVLFC8KusUX8T/0kCiOYpAIQ==",
      "dev": true,
      "license": "MIT"
    }
  }
}

```

### File: `backend/package.json`
```json
{
  "devDependencies": {
    "@types/plotly.js": "^3.0.10",
    "@types/react-plotly.js": "^2.6.4"
  }
}

```

### File: `backend/pyproject.toml`
```toml
[tool.pytest.ini_options]
strict_markers = true
asyncio_mode = "auto"
testpaths = ["tests"]
python_files = ["test_*.py"]
python_functions = ["test_*"]
addopts = [
    "-ra",
    "--strict-markers",
    "--strict-config",
]
markers = [
    "unit: marks fast, isolated unit tests",
    "integration: marks tests involving multiple components or external interfaces",
    "benchmark: marks model comparison and benchmark tests",
    "asyncio: mark a test as an asyncio coroutine",
    "api: marks API endpoint and request-response tests",
]
filterwarnings = [
    "error",
]
```

### File: `backend/requirements.txt`
```
alembic==1.18.5
amqp==5.3.1
annotated-doc==0.0.5
annotated-types==0.8.0
anyio==4.14.2
billiard==4.2.4
celery==5.6.3
certifi==2026.7.22
charset-normalizer==3.5.1
click==8.4.2
click-didyoumean==0.3.1
click-plugins==1.1.1.2
click-repl==0.3.0
colorama==0.4.6
coverage==7.15.3
detect-installer==0.1.0
dnspython==2.8.0
email-validator==2.3.0
fastapi==0.141.1
fastapi-cli==0.0.32
fastapi-cloud-cli==0.23.0
fastar==0.11.0
greenlet==3.5.4
h11==0.16.0
httpcore==1.0.9
httpcore2==2.10.0
httptools==0.8.0
httpx==0.28.1
httpx2==2.10.0
idna==3.18
iniconfig==2.3.0
Jinja2==3.1.6
kombu==5.6.2
llvmlite==0.48.0
Mako==1.3.12
markdown-it-py==4.2.0
MarkupSafe==3.0.3
mdurl==0.1.2
numba==0.66.0
numpy==2.2.6
packaging==26.2
pandas==3.0.5
pluggy==1.6.0
prompt_toolkit==3.0.53
psycopg==3.3.4
psycopg-binary==3.3.4
pydantic==2.13.4
pydantic-extra-types==2.11.1
pydantic-settings==2.14.2
pydantic_core==2.46.4
Pygments==2.20.0
pytest==9.1.1
pytest-asyncio==1.4.0
pytest-cov==7.1.0
pythermalcomfort==4.4.0
python-dateutil==2.9.0.post0
python-dotenv==1.2.2
python-multipart==0.0.32
PyYAML==6.0.3
redis==6.4.0
requests==2.34.2
rich==15.0.0
rich-toolkit==0.20.3
rignore==0.8.0
scipy==1.18.0
sentry-sdk==2.66.1
setuptools==83.0.0
shellingham==1.5.4
six==1.17.0
SQLAlchemy==2.0.51
starlette==1.3.1
truststore==0.10.4
typer==0.27.0
typing-inspection==0.4.2
typing_extensions==4.16.0
tzdata==2026.3
tzlocal==5.4.4
urllib3==2.7.0
uvicorn==0.52.0
vine==5.1.0
watchfiles==1.2.0
wcwidth==0.8.2
websockets==17.0
wheel==0.47.0

```

### File: `backend/run-tests.sh`
```
#!/usr/bin/env bash

set -e

mkdir -p /c/nc
export NUMBA_CACHE_DIR="C:/nc"

PYTHON="./.venv/Scripts/python.exe"

if [ ! -f "$PYTHON" ]; then
  echo "Error: Not found $PYTHON"
  echo "Please create the .venv directory in the backend folder first"
  exit 1
fi

echo "Python:"
"$PYTHON" -c "import sys; print(sys.executable)"

echo "Numba cache:"
"$PYTHON" -c \
  "from numba.core import config; print(config.CACHE_DIR)"

echo "pythermalcomfort:"
"$PYTHON" -c \
  "import pythermalcomfort; print(pythermalcomfort.__file__)"

echo "Starting test execution..."
"$PYTHON" -m pytest -vv
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

### File: `backend/scripts/export_openapi.py`
```python
"""Snapshot the OpenAPI contract. Usage: python scripts/export_openapi.py OUT.json"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.main import app  # noqa: E402

Path(sys.argv[1]).write_text(
    json.dumps(app.openapi(), indent=2, sort_keys=True), encoding="utf-8"
)
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

### File: `backend/tests/__init__.py`
```python

```

### File: `backend/tests/conftest.py`
```python
import os
import tempfile
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import get_settings
from app.core.runtime import configure_runtime

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from app.schemas.weather import (
    CityResponse, WeatherPoint, WeatherSourceMetadata, WeatherTimeSeries,
)


_test_settings = get_settings()

configure_runtime(
    numba_cache_dir=_test_settings.numba_cache_dir,
)

NUMBA_CACHE_DIR = Path(
    os.environ.get(
        "NUMBA_CACHE_DIR",
        Path(tempfile.gettempdir())
        / "radiative-cooling-numba-cache",
    )
)

NUMBA_CACHE_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

os.environ["NUMBA_CACHE_DIR"] = str(
    NUMBA_CACHE_DIR
)


from app.core.config import settings
from app.db.session import get_db
from app.main import app
from app.schemas.simulation import (
    EnvironmentInput,
    MaterialInput,
    PersonInput,
    SimulationRequest,
)


@pytest.fixture
def db_session():
    engine = create_engine(
        settings.database_url,
        pool_pre_ping=True,
    )

    connection = engine.connect()
    transaction = connection.begin()

    TestingSessionLocal = sessionmaker(
        bind=connection,
        autoflush=False,
        expire_on_commit=False,
    )

    session = TestingSessionLocal()

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()
        engine.dispose()


@pytest.fixture
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = (
        override_get_db
    )

    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.pop(
            get_db,
            None,
        )


@pytest.fixture
def environment() -> EnvironmentInput:
    return EnvironmentInput(
        air_temperature_c=38.0,
        mean_radiant_temperature_c=45.0,
        sky_temperature_c=23.0,
        relative_humidity_percent=40.0,
        wind_speed_m_s=1.5,
        solar_radiation_w_m2=800.0,
        sky_view_factor=0.5,
    )


@pytest.fixture
def person() -> PersonInput:
    return PersonInput(
        met=2.6,
        body_surface_area_m2=1.8,
        initial_core_temperature_c=36.8,
        initial_skin_temperature_c=33.7,
    )


@pytest.fixture
def control_material() -> MaterialInput:
    return MaterialInput(
        name="Control",
        clothing_insulation_clo=0.5,
        solar_reflectance=0.4,
        solar_transmittance=0.0,
        infrared_emissivity=0.8,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
    )


@pytest.fixture
def rc_material() -> MaterialInput:
    return MaterialInput(
        name="Radiative Cooling",
        clothing_insulation_clo=0.4,
        solar_reflectance=0.92,
        solar_transmittance=0.0,
        infrared_emissivity=0.95,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
    )


@pytest.fixture
def simulation_request(
    environment: EnvironmentInput,
    person: PersonInput,
    control_material: MaterialInput,
    rc_material: MaterialInput,
) -> SimulationRequest:
    return SimulationRequest(
        city="Dubai",
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        control_material=control_material,
        rc_material=rc_material,
    )

@pytest.fixture
def hourly_weather() -> WeatherTimeSeries:
    """Five hourly points 11:00-15:00 Asia/Dubai; exposure 12:00-14:00."""
    tz = ZoneInfo("Asia/Dubai")
    start = datetime(2023, 7, 15, 12, tzinfo=tz)

    temperatures = [41.8, 43.4, 44.2, 44.9, 44.7]
    humidities = [29.0, 26.0, 25.0, 24.0, 24.0]
    winds = [6.17, 5.11, 4.32, 3.69, 3.62]
    ghis = [807.0, 901.0, 929.0, 892.0, 789.0]

    points = [
        WeatherPoint(
            timestamp=start + timedelta(hours=i - 1),
            air_temperature_c=temperatures[i],
            relative_humidity_percent=humidities[i],
            wind_speed_m_s=winds[i],
            ghi_w_m2=ghis[i],
            direct_radiation_w_m2=ghis[i] * 0.75,
            diffuse_radiation_w_m2=ghis[i] * 0.25,
            dni_w_m2=ghis[i] * 0.8,
        )
        for i in range(5)
    ]

    return WeatherTimeSeries(
        city=CityResponse(
            id="dubai", name="Dubai", country="United Arab Emirates",
            latitude=25.2048, longitude=55.2708, elevation_m=16.0,
            timezone="Asia/Dubai", climate_type="hot_dry",
        ),
        requested_start_time=start,
        requested_end_time=start + timedelta(hours=2),
        points=points,
        source=WeatherSourceMetadata(
            provider="test", dataset="test", model="test",
            latitude=25.2, longitude=55.3, elevation_m=16.0,
            timezone="Asia/Dubai", downloaded_at=start,
            from_cache=True, attribution="test",
        ),
    )
```

### File: `backend/tests/core/test_numba_cache_integration.py`
```python
"""Integration test for the Numba compilation cache."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


BACKEND_ROOT = Path(__file__).resolve().parents[2]


def test_numba_writes_cache_files_to_configured_directory(
    tmp_path: Path,
) -> None:
    module_directory = tmp_path / "module"
    module_directory.mkdir()

    target_module = (
        module_directory
        / "cached_kernel.py"
    )

    target_module.write_text(
        "\n".join(
            [
                '"""Temporary Numba integration target."""',
                "",
                "from numba import njit",
                "",
                "",
                "@njit(cache=True)",
                "def add(left: int, right: int) -> int:",
                "    return left + right",
                "",
            ]
        ),
        encoding="utf-8",
    )

    cache_directory = tmp_path / "numba-cache"

    environment = os.environ.copy()
    environment["NUMBA_CACHE_DIR"] = str(
        cache_directory
    )
    environment["NUMBA_DISABLE_JIT"] = "0"

    python_path_entries = [
        str(module_directory),
        str(BACKEND_ROOT),
    ]

    existing_python_path = environment.get(
        "PYTHONPATH"
    )

    if existing_python_path:
        python_path_entries.append(
            existing_python_path
        )

    environment["PYTHONPATH"] = os.pathsep.join(
        python_path_entries
    )

    command = "\n".join(
        [
            "from app.core.runtime import configure_numba_cache",
            "configure_numba_cache()",
            "from cached_kernel import add",
            "assert add(2, 3) == 5",
        ]
    )

    completed = subprocess.run(
        [
            sys.executable,
            "-c",
            command,
        ],
        cwd=BACKEND_ROOT,
        env=environment,
        capture_output=True,
        text=True,
        timeout=180,
        check=False,
    )

    assert completed.returncode == 0, (
        "The Numba subprocess failed.\n"
        f"stdout:\n{completed.stdout}\n"
        f"stderr:\n{completed.stderr}"
    )

    index_files = list(
        cache_directory.rglob("*.nbi")
    )
    object_files = list(
        cache_directory.rglob("*.nbc")
    )

    assert index_files, (
        "Numba did not create an .nbi cache index."
    )
    assert object_files, (
        "Numba did not create an .nbc cache object."
    )
```

### File: `backend/tests/core/test_runtime.py`
```python
"""Tests for process-level runtime configuration."""

from pathlib import Path

from app.core.runtime import configure_numba_cache


def test_uses_configured_cache_directory(
    monkeypatch,
    tmp_path: Path,
) -> None:
    monkeypatch.delenv("NUMBA_CACHE_DIR", raising=False)

    configured_directory = tmp_path / "configured-cache"

    result = configure_numba_cache(configured_directory)

    assert result == configured_directory.resolve()
    assert result.is_dir()
    assert result.exists()
    assert result.as_posix() in (
        Path(result).as_posix(),
    )


def test_environment_variable_takes_precedence(
    monkeypatch,
    tmp_path: Path,
) -> None:
    environment_directory = tmp_path / "environment-cache"
    configured_directory = tmp_path / "configured-cache"

    monkeypatch.setenv(
        "NUMBA_CACHE_DIR",
        str(environment_directory),
    )

    result = configure_numba_cache(configured_directory)

    assert result == environment_directory.resolve()
    assert result.is_dir()


def test_uses_cross_platform_temporary_default(
    monkeypatch,
    tmp_path: Path,
) -> None:
    monkeypatch.delenv("NUMBA_CACHE_DIR", raising=False)

    result = configure_numba_cache(
        temporary_root=tmp_path,
    )

    expected = (
        tmp_path
        / "radiative-cooling-platform"
        / "numba"
    ).resolve()

    assert result == expected
    assert result.is_dir()


def test_creates_missing_parent_directories(
    monkeypatch,
    tmp_path: Path,
) -> None:
    monkeypatch.delenv("NUMBA_CACHE_DIR", raising=False)

    configured_directory = (
        tmp_path
        / "first"
        / "second"
        / "numba"
    )

    assert not configured_directory.exists()

    result = configure_numba_cache(configured_directory)

    assert result.exists()
    assert result.is_dir()
```

### File: `backend/tests/fixtures/dubai_2h/expected_results.json`
```json
{
  "city": "Dubai",
  "control": [
    {
      "core_temperature_c": 36.8,
      "minute": 0.0,
      "skin_temperature_c": 33.7
    },
    {
      "core_temperature_c": 37.3154,
      "minute": 10.0,
      "skin_temperature_c": 36.8813
    },
    {
      "core_temperature_c": 37.7534,
      "minute": 20.0,
      "skin_temperature_c": 37.194
    },
    {
      "core_temperature_c": 38.1452,
      "minute": 30.0,
      "skin_temperature_c": 37.5355
    },
    {
      "core_temperature_c": 38.511,
      "minute": 40.0,
      "skin_temperature_c": 37.8548
    },
    {
      "core_temperature_c": 38.8528,
      "minute": 50.0,
      "skin_temperature_c": 38.1533
    },
    {
      "core_temperature_c": 39.1722,
      "minute": 60.0,
      "skin_temperature_c": 38.4329
    },
    {
      "core_temperature_c": 39.4699,
      "minute": 70.0,
      "skin_temperature_c": 38.6885
    },
    {
      "core_temperature_c": 39.7453,
      "minute": 80.0,
      "skin_temperature_c": 38.9242
    },
    {
      "core_temperature_c": 40.0003,
      "minute": 90.0,
      "skin_temperature_c": 39.1425
    },
    {
      "core_temperature_c": 40.2363,
      "minute": 100.0,
      "skin_temperature_c": 39.3447
    },
    {
      "core_temperature_c": 40.4549,
      "minute": 110.0,
      "skin_temperature_c": 39.5322
    },
    {
      "core_temperature_c": 40.6575,
      "minute": 120.0,
      "skin_temperature_c": 39.7062
    }
  ],
  "duration_minutes": 120,
  "model_version": "0.5.0",
  "parameter_fingerprint": "407990587a76b25896954f71012bcf4cb47f0fa3fb3a91dee211dda08529b1a5",
  "parameter_snapshot": {
    "environment_assumptions": {
      "fixed_sky_offset_k": 15.0,
      "mean_radiant_temperature_method": "air_plus_solar_linear",
      "sky_offset_base_k": 5.0,
      "sky_offset_humidity_range_k": 10.0,
      "sky_temperature_method": "humidity_offset",
      "sky_view_factor": 0.5,
      "solar_mrt_gain_cap_k": 15.0,
      "solar_mrt_gain_k_per_w_m2": 0.012,
      "wind_speed_scaling_factor": 1.0
    },
    "model_parameter_set_sha256": "5e0cbe090c73d0c64f563d0eee0001d268a9d85a2d9aa0b3d17dd353caa8bcb3",
    "model_parameter_set_version": "3.0.0",
    "model_parameters": {
      "blood_heat_capacity_per_flow": 1.163,
      "body_specific_heat": 3490.0,
      "clo_to_si": 0.155,
      "clothing_area_factor_slope": 0.15,
      "clothing_vapor_permeation_efficiency": 0.45,
      "core_setpoint_temperature": 36.8,
      "core_skin_conductance_basal": 5.28,
      "effective_radiation_area_ratio": 0.73,
      "exhaled_air_temperature": 34.0,
      "fallback_sky_temperature_offset": 15.0,
      "forced_convection_coefficient": 8.3,
      "latent_heat_of_sweat": 0.68,
      "lewis_relation": 16.5,
      "magnus_a": 0.61078,
      "magnus_b": 17.2694,
      "magnus_c": 237.3,
      "maximum_sweat_rate": 500.0,
      "maximum_wettedness_clothed_coefficient": 0.59,
      "maximum_wettedness_clothed_exponent": -0.08,
      "maximum_wettedness_nude_coefficient": 0.38,
      "maximum_wettedness_nude_exponent": -0.29,
      "metabolic_rate_per_met": 58.15,
      "natural_convection_minimum_coefficient": 3.1,
      "respiratory_latent_coefficient": 1.7e-05,
      "respiratory_reference_vapor_pressure": 5867.0,
      "respiratory_sensible_coefficient": 0.0014,
      "shivering_coefficient": 19.4,
      "skin_blood_flow_basal": 6.3,
      "skin_blood_flow_maximum": 90.0,
      "skin_blood_flow_minimum": 0.5,
      "skin_diffusion_fraction": 0.06,
      "skin_emissivity": 0.95,
      "skin_mass_fraction": 0.1,
      "skin_setpoint_temperature": 33.7,
      "stefan_boltzmann_constant": 5.670374419e-08,
      "sweating_gain_body": 170.0,
      "sweating_skin_signal_scale": 10.7,
      "swinbank_coefficient": 0.0552,
      "vasoconstriction_gain": 0.5,
      "vasodilation_gain": 120.0
    },
    "schema_version": 1
  },
  "radiative_cooling": [
    {
      "core_temperature_c": 36.8,
      "minute": 0.0,
      "skin_temperature_c": 33.7
    },
    {
      "core_temperature_c": 37.2525,
      "minute": 10.0,
      "skin_temperature_c": 36.5204
    },
    {
      "core_temperature_c": 37.5858,
      "minute": 20.0,
      "skin_temperature_c": 36.7421
    },
    {
      "core_temperature_c": 37.7897,
      "minute": 30.0,
      "skin_temperature_c": 36.8187
    },
    {
      "core_temperature_c": 37.9672,
      "minute": 40.0,
      "skin_temperature_c": 36.9749
    },
    {
      "core_temperature_c": 38.134,
      "minute": 50.0,
      "skin_temperature_c": 37.1226
    },
    {
      "core_temperature_c": 38.2911,
      "minute": 60.0,
      "skin_temperature_c": 37.2622
    },
    {
      "core_temperature_c": 38.4386,
      "minute": 70.0,
      "skin_temperature_c": 37.3911
    },
    {
      "core_temperature_c": 38.5764,
      "minute": 80.0,
      "skin_temperature_c": 37.5114
    },
    {
      "core_temperature_c": 38.7053,
      "minute": 90.0,
      "skin_temperature_c": 37.6242
    },
    {
      "core_temperature_c": 38.826,
      "minute": 100.0,
      "skin_temperature_c": 37.7304
    },
    {
      "core_temperature_c": 38.9393,
      "minute": 110.0,
      "skin_temperature_c": 37.8303
    },
    {
      "core_temperature_c": 39.0458,
      "minute": 120.0,
      "skin_temperature_c": 37.9247
    }
  ],
  "summary": {
    "average_skin_temperature_improvement_c": 1.0721,
    "final_core_temperature_improvement_c": 1.6117,
    "final_skin_temperature_improvement_c": 1.7815
  },
  "weather": {
    "payload_sha256": "b568200999e8bc079896b86d451e3c82213682d90698ef1f846100fcc863f9d3",
    "point_count": 5,
    "quality": {
      "duplicates_removed": 0,
      "expected_step_seconds": 3600,
      "first_timestamp": "2023-07-15T00:00:00+04:00",
      "gaps": [],
      "last_timestamp": "2023-07-15T23:00:00+04:00",
      "notes": [],
      "point_count": 24,
      "was_sorted": true
    }
  }
}
```

### File: `backend/tests/fixtures/dubai_2h/open_meteo_payload.json`
```json
{"elevation":16.0,"generationtime_ms":0.1323223114013672,"hourly":{"diffuse_radiation":[0.0,0.0,0.0,0.0,0.0,0.0,3.0,55.0,111.0,151.0,175.0,195.0,205.0,208.0,203.0,192.0,196.0,150.0,106.0,42.0,1.0,0.0,0.0,0.0],"direct_normal_irradiance":[0.0,0.0,0.0,0.0,0.0,0.0,0.0,184.1,396.8,539.4,638.7,686.0,716.3,724.2,716.1,683.2,569.0,459.4,318.5,130.9,0.0,0.0,0.0,0.0],"direct_radiation":[0.0,0.0,0.0,0.0,0.0,0.0,0.0,32.0,155.0,319.0,487.0,612.0,696.0,721.0,689.0,597.0,419.0,257.0,113.0,19.0,0.0,0.0,0.0,0.0],"relative_humidity_2m":[42,39,36,33,28,26,25,30,34,32,30,29,26,25,24,24,25,28,36,39,41,42,42,42],"shortwave_radiation":[0.0,0.0,0.0,0.0,0.0,0.0,3.0,87.0,266.0,470.0,662.0,807.0,901.0,929.0,892.0,789.0,615.0,407.0,219.0,61.0,1.0,0.0,0.0,0.0],"temperature_2m":[38.4,38.0,37.5,37.3,37.4,37.6,37.7,37.5,37.9,39.8,41.0,41.8,43.4,44.2,44.9,44.7,44.3,43.1,40.5,39.3,38.4,37.8,37.6,37.3],"time":["2023-07-15T00:00","2023-07-15T01:00","2023-07-15T02:00","2023-07-15T03:00","2023-07-15T04:00","2023-07-15T05:00","2023-07-15T06:00","2023-07-15T07:00","2023-07-15T08:00","2023-07-15T09:00","2023-07-15T10:00","2023-07-15T11:00","2023-07-15T12:00","2023-07-15T13:00","2023-07-15T14:00","2023-07-15T15:00","2023-07-15T16:00","2023-07-15T17:00","2023-07-15T18:00","2023-07-15T19:00","2023-07-15T20:00","2023-07-15T21:00","2023-07-15T22:00","2023-07-15T23:00"],"wind_speed_10m":[3.96,3.97,4.16,4.38,4.92,5.85,6.45,6.38,7.33,7.48,7.01,6.17,5.11,4.32,3.69,3.62,4.02,4.7,4.9,4.02,2.8,2.58,2.5,2.06]},"hourly_units":{"diffuse_radiation":"W/m\u00b2","direct_normal_irradiance":"W/m\u00b2","direct_radiation":"W/m\u00b2","relative_humidity_2m":"%","shortwave_radiation":"W/m\u00b2","temperature_2m":"\u00b0C","time":"iso8601","wind_speed_10m":"m/s"},"latitude":25.0,"longitude":55.25,"timezone":"Asia/Dubai","timezone_abbreviation":"GMT+4","utc_offset_seconds":14400}
```

### File: `backend/tests/fixtures/dubai_2h/open_meteo_payload.sha256`
```
b568200999e8bc079896b86d451e3c82213682d90698ef1f846100fcc863f9d3

```

### File: `backend/tests/fixtures/dubai_2h/request.json`
```json
{
  "city_id": "dubai",
  "start_time_local": "2023-07-15T12:00:00",
  "duration_minutes": 120,
  "output_interval_minutes": 10,
  "person": {
    "met": 2.6,
    "body_surface_area_m2": 1.8,
    "initial_core_temperature_c": 36.8,
    "initial_skin_temperature_c": 33.7
  },
  "control_material": {
    "name": "Control",
    "clothing_insulation_clo": 0.5,
    "solar_reflectance": 0.4,
    "solar_transmittance": 0.0,
    "infrared_emissivity": 0.8,
    "projected_solar_area_factor": 0.25,
    "absorbed_solar_to_body_fraction": 0.35
  },
  "rc_material": {
    "name": "Radiative Cooling",
    "clothing_insulation_clo": 0.4,
    "solar_reflectance": 0.92,
    "solar_transmittance": 0.0,
    "infrared_emissivity": 0.95,
    "projected_solar_area_factor": 0.25,
    "absorbed_solar_to_body_fraction": 0.35
  }
}
```

### File: `backend/tests/fixtures/dubai_2h/request_params.json`
```json
{
  "cell_selection": "land",
  "elevation": 16.0,
  "end_date": "2023-07-15",
  "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m,shortwave_radiation,direct_radiation,diffuse_radiation,direct_normal_irradiance",
  "latitude": 25.2048,
  "longitude": 55.2708,
  "models": "era5",
  "start_date": "2023-07-15",
  "temperature_unit": "celsius",
  "timezone": "Asia/Dubai",
  "wind_speed_unit": "ms"
}
```

### File: `backend/tests/test_api.py`
```python
import pytest


@pytest.mark.integration
def test_health_endpoint(client):
    response = client.get("/api/v1/health")

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "healthy"
    assert body["service"] == (
        "radiative-cooling-api"
    )


@pytest.mark.integration
def test_simulation_endpoint(
    client,
    simulation_request,
):
    response = client.post(
        "/api/v1/simulations/run",
        json=simulation_request.model_dump(),
    )

    assert response.status_code == 200

    body = response.json()

    assert body["city"] == "Dubai"
    assert "control" in body
    assert "radiative_cooling" in body
    assert "summary" in body

    assert len(
        body["control"]["time_series"]
    ) == 121

    assert (
        body["control"]["diagnostics"]
        ["normalized_residual_percent"]
        < 1.0
    )


@pytest.mark.integration
def test_invalid_material_is_rejected(
    client,
    simulation_request,
):
    payload = simulation_request.model_dump()

    payload["rc_material"][
        "solar_reflectance"
    ] = 0.8

    payload["rc_material"][
        "solar_transmittance"
    ] = 0.4

    response = client.post(
        "/api/v1/simulations/run",
        json=payload,
    )

    assert response.status_code == 422


@pytest.mark.integration
def test_identical_material_api_improvement_is_zero(
    client,
    simulation_request,
):
    payload = simulation_request.model_dump()

    payload["rc_material"] = payload[
        "control_material"
    ].copy()

    response = client.post(
        "/api/v1/simulations/run",
        json=payload,
    )

    assert response.status_code == 200

    summary = response.json()["summary"]

    assert abs(
        summary[
            "final_skin_temperature_improvement_c"
        ]
    ) < 1e-6

    assert abs(
        summary[
            "final_core_temperature_improvement_c"
        ]
    ) < 1e-6
```

### File: `backend/tests/test_body.py`
```python
import pytest

from app.schemas.simulation import PersonInput
from app.services.body import body_heat_capacities


@pytest.mark.unit
def test_default_person_reproduces_gagge_lumped_value():
    capacities = body_heat_capacities(PersonInput())

    # 3490 * 70 / 1.8 = 135 722 J/(m^2 K); alpha = 0.1
    assert capacities.total_j_m2k == pytest.approx(135_722.2, abs=0.5)
    assert capacities.skin_j_m2k == pytest.approx(13_572.2, abs=0.5)
    assert capacities.core_j_m2k == pytest.approx(122_150.0, abs=0.5)


@pytest.mark.unit
def test_heavier_person_has_larger_capacity_per_area():
    light = body_heat_capacities(PersonInput(body_mass_kg=55.0))
    heavy = body_heat_capacities(PersonInput(body_mass_kg=95.0))

    assert heavy.total_j_m2k > light.total_j_m2k


@pytest.mark.unit
def test_larger_surface_area_lowers_capacity_per_area():
    small = body_heat_capacities(PersonInput(body_surface_area_m2=1.6))
    large = body_heat_capacities(PersonInput(body_surface_area_m2=2.2))

    assert large.total_j_m2k < small.total_j_m2k
```

### File: `backend/tests/test_cities.py`
```python
import pytest

from app.core.cities import (
    CITIES,
    get_city,
)


@pytest.mark.unit
def test_get_city_returns_supported_city():
    city = get_city("dubai")

    assert city.id == "dubai"
    assert city.name == "Dubai"
    assert city.country == (
        "United Arab Emirates"
    )
    assert city.timezone == "Asia/Dubai"


@pytest.mark.unit
def test_get_city_normalizes_case_and_spaces():
    city = get_city("  DuBaI  ")

    assert city is CITIES["dubai"]


@pytest.mark.unit
@pytest.mark.parametrize(
    "city_id",
    [
        "dubai",
        "guangzhou",
        "lhasa",
    ],
)
def test_all_configured_cities_can_be_loaded(
    city_id,
):
    city = get_city(city_id)

    assert city.id == city_id
    assert city.latitude != 0
    assert city.longitude != 0
    assert city.timezone


@pytest.mark.unit
def test_get_city_rejects_unknown_city():
    with pytest.raises(
        ValueError,
        match="City not supported",
    ):
        get_city("hong-kong")


@pytest.mark.unit
def test_unknown_city_error_lists_supported_cities():
    with pytest.raises(ValueError) as error:
        get_city("unknown")

    message = str(error.value)

    assert "dubai" in message
    assert "guangzhou" in message
    assert "lhasa" in message
```

### File: `backend/tests/test_climate_adaptation.py`
```python
from app.schemas.global_batch import (
    GlobalBatchCreate,
)
from app.schemas.simulation import (
    MaterialInput,
    PersonInput,
)


def make_batch_request():
    return GlobalBatchCreate(
        city_ids=[
            "dubai",
            "guangzhou",
        ],
        year=2023,
        start_month=1,
        end_month=3,
        representative_day=15,
        local_start_hour=12,
        duration_minutes=120,
        output_interval_minutes=10,
        minimum_skin_improvement_c=0.2,
        person=PersonInput(
            met=2.0,
            body_surface_area_m2=1.8,
            initial_core_temperature_c=36.8,
            initial_skin_temperature_c=33.7,
        ),
        control_material=MaterialInput(
            name="Control",
            clothing_insulation_clo=0.5,
            solar_reflectance=0.3,
            solar_transmittance=0,
            infrared_emissivity=0.9,
            projected_solar_area_factor=0.25,
            absorbed_solar_to_body_fraction=0.35,
        ),
        rc_material=MaterialInput(
            name="RC",
            clothing_insulation_clo=0.4,
            solar_reflectance=0.92,
            solar_transmittance=0,
            infrared_emissivity=0.95,
            projected_solar_area_factor=0.25,
            absorbed_solar_to_body_fraction=0.35,
        ),
    )


def test_global_batch_month_range():
    request = make_batch_request()

    assert request.start_month == 1
    assert request.end_month == 3
    assert len(request.city_ids) == 2


def test_global_batch_rejects_duplicate_cities():
    request = make_batch_request().model_dump()
    request["city_ids"] = [
        "dubai",
        "dubai",
    ]

    try:
        GlobalBatchCreate.model_validate(
            request
        )
        assert False
    except ValueError as error:
        assert "duplicate" in str(error)
```

### File: `backend/tests/test_climate_scenarios.py`
```python
import pytest

from app.schemas.simulation import EnvironmentInput
from app.services.two_node import simulate_material


@pytest.mark.unit
@pytest.mark.parametrize(
    (
        "name",
        "air_temperature",
        "humidity",
        "wind_speed",
        "solar_radiation",
    ),
    [
        (
            "hot_dry",
            42.0,
            20.0,
            2.0,
            900.0,
        ),
        (
            "hot_humid",
            34.0,
            85.0,
            1.0,
            700.0,
        ),
        (
            "high_altitude_solar",
            24.0,
            25.0,
            2.5,
            1000.0,
        ),
        (
            "night",
            30.0,
            60.0,
            0.5,
            0.0,
        ),
    ],
)
def test_typical_climate_scenarios_run_successfully(
    name,
    air_temperature,
    humidity,
    wind_speed,
    solar_radiation,
    person,
    rc_material,
):
    environment = EnvironmentInput(
        air_temperature_c=air_temperature,
        mean_radiant_temperature_c=(
            air_temperature + 5.0
        ),
        sky_temperature_c=(
            air_temperature - 12.0
        ),
        relative_humidity_percent=humidity,
        wind_speed_m_s=wind_speed,
        solar_radiation_w_m2=solar_radiation,
        sky_view_factor=0.5,
    )

    result = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=rc_material,
    )

    assert len(result.time_series) == 121

    assert (
        result.diagnostics
        .normalized_residual_percent
        < 1.0
    ), f"{name} Excessive energy residual"
```

### File: `backend/tests/test_clothing.py`
```python
import pytest
from pydantic import ValidationError

from app.schemas.simulation import MaterialInput
from app.services.clothing import (
    derive_evaporative_resistance_m2pa_w,
    maximum_evaporation_w_m2,
    resolve_clothing,
)
from app.services.two_node import calculate_fluxes, simulate_material


@pytest.mark.unit
def test_derived_evaporative_resistance_matches_formula():
    # 0.155 * 0.5 / (16.5 * 0.45) * 1000
    assert derive_evaporative_resistance_m2pa_w(0.5) == pytest.approx(10.4377, abs=1e-3)


@pytest.mark.unit
def test_none_resistance_is_derived_and_flagged(control_material):
    clothing = resolve_clothing(control_material)

    assert clothing.evaporative_resistance_source == "derived_from_clo"
    assert clothing.evaporative_resistance_m2pa_w == pytest.approx(
        derive_evaporative_resistance_m2pa_w(control_material.clothing_insulation_clo)
    )


@pytest.mark.unit
def test_explicit_resistance_overrides_derivation(control_material):
    material = control_material.model_copy(update={"evaporative_resistance_m2pa_w": 30.0})
    clothing = resolve_clothing(material)

    assert clothing.evaporative_resistance_source == "material_input"
    assert clothing.evaporative_resistance_m2pa_w == pytest.approx(30.0)


@pytest.mark.unit
def test_higher_resistance_lowers_maximum_evaporation(control_material):
    low = resolve_clothing(control_material.model_copy(update={"evaporative_resistance_m2pa_w": 5.0}))
    high = resolve_clothing(control_material.model_copy(update={"evaporative_resistance_m2pa_w": 50.0}))

    e_low = maximum_evaporation_w_m2(low, 10.0, 5.6, 2.0)
    e_high = maximum_evaporation_w_m2(high, 10.0, 5.6, 2.0)

    assert e_high < e_low
    assert e_high > 0.0


@pytest.mark.unit
def test_explicit_derived_value_reproduces_none_result(environment, person, control_material):
    derived = derive_evaporative_resistance_m2pa_w(control_material.clothing_insulation_clo)
    explicit = control_material.model_copy(update={"evaporative_resistance_m2pa_w": derived})

    a = simulate_material(60, 1, environment, person, control_material)
    b = simulate_material(60, 1, environment, person, explicit)

    assert a.final_skin_temperature_c == pytest.approx(b.final_skin_temperature_c, abs=1e-8)
    assert a.clothing.evaporative_resistance_source == "derived_from_clo"
    assert b.clothing.evaporative_resistance_source == "material_input"

    # Stage 3: f_cl and the ADR 0003 solar note are always reported; only the
    # Re,cl derivation note must disappear when the value is supplied.
    assert any("evaporative_resistance" in note for note in a.assumptions_applied)
    assert not any("evaporative_resistance" in note for note in b.assumptions_applied)




@pytest.mark.unit
def test_impermeable_garment_ends_warmer(environment, person, control_material):
    permeable = control_material.model_copy(update={"evaporative_resistance_m2pa_w": 5.0})
    impermeable = control_material.model_copy(update={"evaporative_resistance_m2pa_w": 200.0})

    warm = simulate_material(120, 1, environment, person, impermeable)
    cool = simulate_material(120, 1, environment, person, permeable)

    assert warm.final_skin_temperature_c > cool.final_skin_temperature_c
    assert warm.time_series[-1].skin_wettedness >= cool.time_series[-1].skin_wettedness


@pytest.mark.unit
def test_infrared_transmittance_amplifies_longwave_exchange(
    environment, person, control_material
):
    opaque = control_material.model_copy(update={"infrared_emissivity": 0.5})
    transparent = opaque.model_copy(update={"infrared_transmittance": 0.4})

    # Cold radiant surroundings: the body loses heat; transmittance increases
    # the loss (more positive under the "positive = loss" convention).
    cold = environment.model_copy(
        update={"mean_radiant_temperature_c": 15.0, "sky_temperature_c": 0.0}
    )
    opaque_cold = calculate_fluxes(36.8, 33.7, cold, person, opaque)
    transparent_cold = calculate_fluxes(36.8, 33.7, cold, person, transparent)
    assert opaque_cold.longwave_radiation > 0
    assert transparent_cold.longwave_radiation > opaque_cold.longwave_radiation

    # Hot radiant surroundings well above any clothing surface temperature:
    # the body gains heat; transmittance increases the gain (more negative).
    hot = environment.model_copy(
        update={"mean_radiant_temperature_c": 60.0, "sky_temperature_c": 60.0}
    )
    opaque_hot = calculate_fluxes(36.8, 33.7, hot, person, opaque)
    transparent_hot = calculate_fluxes(36.8, 33.7, hot, person, transparent)
    assert opaque_hot.longwave_radiation < 0
    assert transparent_hot.longwave_radiation < opaque_hot.longwave_radiation

@pytest.mark.unit
def test_area_factor_is_derived_and_flagged(control_material):
    clothing = resolve_clothing(control_material)

    assert clothing.area_factor_source == "derived_from_clo"
    assert clothing.area_factor == pytest.approx(1.0 + 0.15 * 0.5)

@pytest.mark.unit
def test_explicit_area_factor_overrides_derivation(control_material):
    material = control_material.model_copy(update={"clothing_area_factor": 1.4})
    clothing = resolve_clothing(material)

    assert clothing.area_factor_source == "material_input"
    assert clothing.area_factor == pytest.approx(1.4)

@pytest.mark.unit
def test_clothing_surface_balance_is_consistent(environment, person, control_material):
    """Conduction through the textile equals what leaves its outer surface."""
    clothing = resolve_clothing(control_material)
    fluxes = calculate_fluxes(36.8, 33.7, environment, person, control_material, clothing)

    conduction = (33.7 - fluxes.clothing_surface_temperature_c) / clothing.dry_resistance_m2k_w
    surface_losses = fluxes.convection + fluxes.longwave_radiation - fluxes.longwave_transmitted

    assert conduction == pytest.approx(surface_losses, abs=1e-3)

@pytest.mark.unit
def test_nude_surface_temperature_equals_skin(environment, person, control_material):
    nude = control_material.model_copy(update={"clothing_insulation_clo": 0.0})
    fluxes = calculate_fluxes(36.8, 33.7, environment, person, nude)

    assert fluxes.clothing_surface_temperature_c == pytest.approx(33.7)
    
    
@pytest.mark.unit
def test_emissivity_plus_transmittance_above_one_is_rejected():
    with pytest.raises(ValidationError, match="infrared_emissivity"):
        MaterialInput(name="bad", infrared_emissivity=0.8, infrared_transmittance=0.3)


@pytest.mark.unit
def test_unknown_parameter_source_key_is_rejected():
    with pytest.raises(ValidationError, match="unknown material fields"):
        MaterialInput(name="bad", parameter_sources={"not_a_field": {"source_type": "measured"}})
```

### File: `backend/tests/test_cors.py`
```python
"""Tests for centralized CORS configuration."""

import pytest
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient

from app.core.cors import add_cors_middleware


ALLOWED_ORIGIN = "http://localhost:3000"
DISALLOWED_ORIGIN = "https://untrusted.example.com"


def create_test_application() -> FastAPI:
    application = FastAPI()

    @application.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    add_cors_middleware(
        application,
        origins=[ALLOWED_ORIGIN],
        methods=["GET", "POST", "OPTIONS"],
        headers=["Authorization", "Content-Type"],
        expose_headers=["Content-Disposition"],
        allow_credentials=True,
    )

    return application


def test_allows_configured_origin() -> None:
    client = TestClient(create_test_application())

    response = client.get(
        "/health",
        headers={"Origin": ALLOWED_ORIGIN},
    )

    assert response.status_code == 200
    assert (
        response.headers["access-control-allow-origin"]
        == ALLOWED_ORIGIN
    )
    assert (
        response.headers["access-control-allow-credentials"]
        == "true"
    )


def test_allows_configured_preflight_request() -> None:
    client = TestClient(create_test_application())

    response = client.options(
        "/health",
        headers={
            "Origin": ALLOWED_ORIGIN,
            "Access-Control-Request-Method": "GET",
            "Access-Control-Request-Headers": "Authorization",
        },
    )

    assert response.status_code == 200
    assert (
        response.headers["access-control-allow-origin"]
        == ALLOWED_ORIGIN
    )


def test_rejects_unknown_preflight_origin() -> None:
    client = TestClient(create_test_application())

    response = client.options(
        "/health",
        headers={
            "Origin": DISALLOWED_ORIGIN,
            "Access-Control-Request-Method": "GET",
        },
    )

    assert response.status_code == 400
    assert "access-control-allow-origin" not in response.headers


def test_rejects_duplicate_cors_registration() -> None:
    application = create_test_application()

    with pytest.raises(
        RuntimeError,
        match="CORS middleware has already been registered",
    ):
        add_cors_middleware(
            application,
            origins=[ALLOWED_ORIGIN],
            methods=["GET"],
            headers=["Authorization"],
            expose_headers=[],
            allow_credentials=True,
        )


def test_main_application_registers_cors_once() -> None:
    from app.main import app

    cors_middleware = [
        middleware
        for middleware in app.user_middleware
        if getattr(middleware, "cls", None) is CORSMiddleware
    ]

    assert len(cors_middleware) == 1
```

### File: `backend/tests/test_environment_model.py`
```python
import pytest

from app.schemas.environment import EnvironmentAssumptions
from app.services.environment_model import derive_environment


@pytest.mark.unit
def test_defaults_reproduce_stage_1_formulas():
    env = derive_environment(
        air_temperature_c=40.0, relative_humidity_percent=30.0,
        wind_speed_m_s=3.0, ghi_w_m2=800.0, assumptions=EnvironmentAssumptions(),
    )

    assert env.mean_radiant_temperature_c == pytest.approx(40.0 + 0.012 * 800.0)
    assert env.sky_temperature_c == pytest.approx(40.0 - (5.0 + 10.0 * 0.7))
    assert env.sky_view_factor == 0.5
    assert env.wind_speed_m_s == pytest.approx(3.0)


@pytest.mark.unit
def test_swinbank_clear_sky():
    env = derive_environment(
        air_temperature_c=30.0, relative_humidity_percent=50.0, wind_speed_m_s=1.0,
        ghi_w_m2=0.0, assumptions=EnvironmentAssumptions(sky_temperature_method="swinbank"),
    )
    # 0.0552 * 303.15^1.5 - 273.15
    assert env.sky_temperature_c == pytest.approx(18.2, abs=0.1)


@pytest.mark.unit
def test_wind_scaling_and_negative_inputs_are_clamped():
    env = derive_environment(
        air_temperature_c=30.0, relative_humidity_percent=120.0, wind_speed_m_s=-1.0,
        ghi_w_m2=-50.0,
        assumptions=EnvironmentAssumptions(wind_speed_scaling_factor=0.67),
    )
    assert env.wind_speed_m_s == 0.0
    assert env.solar_radiation_w_m2 == 0.0
    assert env.relative_humidity_percent == 100.0


@pytest.mark.unit
def test_describe_mentions_every_active_rule():
    lines = EnvironmentAssumptions(sky_temperature_method="fixed_offset").describe()
    text = " ".join(lines)
    assert "T_sky = T_air - 15.0 K" in text
    assert "Sky view factor = 0.5" in text
```

### File: `backend/tests/test_exposure_statistics.py`
```python
from datetime import datetime, timedelta, timezone

import pytest

from app.schemas.weather import (
    CityResponse,
    WeatherPoint,
    WeatherSourceMetadata,
    WeatherTimeSeries,
)
from app.services.exposure_statistics import (
    compute_exposure_window_statistics,
    time_weighted_mean,
)
from app.services.weather import slice_weather_time_series


def make_day_weather() -> WeatherTimeSeries:
    """24 hourly points with a non-linear temperature profile so that padded
    and un-padded averages differ."""
    start = datetime(2023, 7, 1, 0, tzinfo=timezone.utc)

    points = [
        WeatherPoint(
            timestamp=start + timedelta(hours=i),
            air_temperature_c=20.0 + 0.1 * i * i,
            relative_humidity_percent=50.0,
            wind_speed_m_s=2.0,
            ghi_w_m2=float(50 * i),
            direct_radiation_w_m2=0.0,
            diffuse_radiation_w_m2=0.0,
            dni_w_m2=0.0,
        )
        for i in range(24)
    ]

    city = CityResponse(
        id="test", name="Test", country="Test",
        latitude=0, longitude=0, elevation_m=0,
        timezone="UTC", climate_type="test",
    )

    return WeatherTimeSeries(
        city=city,
        requested_start_time=start,
        requested_end_time=start + timedelta(hours=23),
        points=points,
        source=WeatherSourceMetadata(
            provider="test", dataset="test", model="test",
            latitude=0, longitude=0, elevation_m=0, timezone="UTC",
            downloaded_at=start, from_cache=True, attribution="test",
        ),
    )


@pytest.mark.unit
def test_time_weighted_mean_matches_trapezoid():
    assert time_weighted_mean([0, 1, 2], [0, 2, 4]) == pytest.approx(2.0)
    assert time_weighted_mean([0, 1, 3], [0, 0, 6]) == pytest.approx(2.0)
    assert time_weighted_mean([5], [7]) == pytest.approx(7.0)


@pytest.mark.unit
def test_statistics_use_exposure_window_not_padded_points():
    weather = make_day_weather()

    sliced = slice_weather_time_series(
        weather=weather,
        start_time_local=datetime(2023, 7, 1, 12),
        duration_minutes=120,
        padding_hours=1,
    )

    stats = compute_exposure_window_statistics(sliced)

    # Knots 12:00 (34.4), 13:00 (36.9), 14:00 (39.6) -> trapezoid = 36.95
    assert stats.mean_air_temperature_c == pytest.approx(36.95)
    assert stats.maximum_air_temperature_c == pytest.approx(39.6)

    padded_arithmetic_mean = sum(
        p.air_temperature_c for p in sliced.points
    ) / len(sliced.points)  # 11:00..15:00 -> 37.5 (the old, wrong number)

    assert stats.mean_air_temperature_c != pytest.approx(padded_arithmetic_mean)


@pytest.mark.unit
@pytest.mark.parametrize("padding_hours", [1, 3, 6])
def test_statistics_are_invariant_to_padding(padding_hours):
    weather = make_day_weather()

    reference = compute_exposure_window_statistics(
        slice_weather_time_series(
            weather=weather,
            start_time_local=datetime(2023, 7, 1, 12),
            duration_minutes=120,
            padding_hours=1,
        )
    )

    candidate = compute_exposure_window_statistics(
        slice_weather_time_series(
            weather=weather,
            start_time_local=datetime(2023, 7, 1, 12),
            duration_minutes=120,
            padding_hours=padding_hours,
        )
    )

    assert candidate.mean_air_temperature_c == pytest.approx(
        reference.mean_air_temperature_c, abs=1e-9
    )
    assert candidate.maximum_air_temperature_c == pytest.approx(
        reference.maximum_air_temperature_c, abs=1e-9
    )
    assert candidate.mean_solar_radiation_w_m2 == pytest.approx(
        reference.mean_solar_radiation_w_m2, abs=1e-9
    )


@pytest.mark.unit
def test_half_hour_start_uses_interpolated_boundary():
    weather = make_day_weather()

    sliced = slice_weather_time_series(
        weather=weather,
        start_time_local=datetime(2023, 7, 1, 12, 30),
        duration_minutes=60,
        padding_hours=1,
    )

    stats = compute_exposure_window_statistics(sliced)

    # Linear between 12:00 (34.4) and 13:00 (36.9) and 13:00..14:00 (39.6)
    t_1230 = 35.65
    t_1330 = 38.25
    expected = ((t_1230 + 36.9) / 2 * 0.5 + (36.9 + t_1330) / 2 * 0.5) / 1.0

    assert stats.mean_air_temperature_c == pytest.approx(expected)
```

### File: `backend/tests/test_gagge_benchmark.py`
```python
import math

import pytest

from app.schemas.simulation import (
    GaggeBenchmarkRequest,
)
from app.services.gagge_benchmark import (
    run_gagge_benchmark,
)


@pytest.mark.benchmark
def test_gagge_benchmark_returns_finite_values(
    environment,
    person,
    control_material,
):
    request = GaggeBenchmarkRequest(
        duration_minutes=60,
        environment=environment,
        person=person,
        material=control_material,
    )

    result = run_gagge_benchmark(request)

    assert math.isfinite(
        result.gagge.core_temperature_c
    )

    assert math.isfinite(
        result.gagge.skin_temperature_c
    )

    assert math.isfinite(
        result.prototype.core_temperature_c
    )

    assert math.isfinite(
        result.prototype.skin_temperature_c
    )


@pytest.mark.benchmark
def test_gagge_output_is_in_broad_range(
    environment,
    person,
    control_material,
):
    request = GaggeBenchmarkRequest(
        duration_minutes=60,
        environment=environment,
        person=person,
        material=control_material,
    )

    result = run_gagge_benchmark(request)

    assert (
        34.0
        < result.gagge.core_temperature_c
        < 42.0
    )

    assert (
        15.0
        < result.gagge.skin_temperature_c
        < 45.0
    )

    assert result.gagge.skin_evaporation_w_m2 >= 0


@pytest.mark.integration
def test_gagge_benchmark_api(
    client,
    environment,
    person,
    control_material,
):
    response = client.post(
        "/api/v1/benchmarks/gagge",
        json={
            "duration_minutes": 60,
            "environment": (
                environment.model_dump()
            ),
            "person": person.model_dump(),
            "material": (
                control_material.model_dump()
            ),
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["reference_model"] == (
        "Gagge Two-Node"
    )

    assert "prototype" in body
    assert "gagge" in body

import pytest
from fastapi import HTTPException

from app.api import benchmarks


@pytest.mark.unit
def test_gagge_api_converts_service_error_to_500(
    monkeypatch,
):
    def fake_run_gagge_benchmark(request):
        raise ValueError(
            "invalid benchmark input"
        )

    monkeypatch.setattr(
        benchmarks,
        "run_gagge_benchmark",
        fake_run_gagge_benchmark,
    )

    with pytest.raises(
        HTTPException,
    ) as error:
        benchmarks.compare_with_gagge(
            object()
        )

    assert error.value.status_code == 500
    assert (
        "invalid benchmark input"
        in error.value.detail
    )
    
@pytest.mark.benchmark
def test_benchmark_returns_aligned_transient_series(environment, person, control_material):
    request = GaggeBenchmarkRequest(
        duration_minutes=90, environment=environment, person=person, material=control_material
    )

    result = run_gagge_benchmark(request)

    assert len(result.time_series) == 91
    assert result.time_series[0].minute == 0
    assert result.time_series[-1].minute == 90
    assert result.core_temperature.maximum_absolute_difference_c >= abs(
        result.core_temperature.final_difference_c
    )
    assert result.reference_port_parity.maximum_absolute_difference_c < 0.05
    assert any("solar_radiation" in note for note in result.alignment_applied)


@pytest.mark.benchmark
def test_default_case_is_within_stage_3_tolerances(environment, person, control_material):
    """Acceptance criterion of Stage 3 for the reference scenario."""
    result = run_gagge_benchmark(
        GaggeBenchmarkRequest(environment=environment, person=person, material=control_material)
    )

    assert result.core_temperature.passed, result.core_temperature
    assert result.skin_temperature.passed, result.skin_temperature
    assert result.passed
```

### File: `backend/tests/test_gagge_reference.py`
```python
import math

import pytest
from pythermalcomfort.models import two_nodes_gagge

from app.services.gagge_reference import run_gagge_reference


PARITY_TOLERANCE_C = 0.05

CASES = [
    # tdb, tr, v, rh, met, clo
    (38.0, 45.0, 1.5, 40.0, 2.6, 0.5),
    (30.0, 30.0, 0.3, 60.0, 1.2, 0.6),
    (42.0, 42.0, 2.0, 20.0, 2.0, 0.4),
    (34.0, 36.0, 1.0, 85.0, 1.8, 0.5),
    (25.0, 25.0, 0.1, 50.0, 1.0, 1.0),
]


@pytest.mark.benchmark
@pytest.mark.parametrize(("tdb", "tr", "v", "rh", "met", "clo"), CASES)
def test_port_matches_library_after_sixty_minutes(tdb, tr, v, rh, met, clo):
    library = two_nodes_gagge(
        tdb=tdb, tr=tr, v=v, rh=rh, met=met, clo=clo, wme=0,
        body_surface_area=1.8, p_atm=101325, position="standing",
        max_skin_blood_flow=90, max_sweating=500, round_output=False,
    )

    port = run_gagge_reference(
        tdb=tdb, tr=tr, v=v, rh=rh, met=met, clo=clo,
        body_surface_area=1.8, body_mass_kg=70.0, duration_minutes=60,
    ).final

    assert port.core_temperature_c == pytest.approx(
        float(library.t_core), abs=PARITY_TOLERANCE_C
    )
    assert port.skin_temperature_c == pytest.approx(
        float(library.t_skin), abs=PARITY_TOLERANCE_C
    )
    assert port.skin_wettedness == pytest.approx(float(library.w), abs=0.02)


@pytest.mark.unit
def test_port_returns_one_point_per_minute_plus_initial_state():
    result = run_gagge_reference(
        tdb=38.0, tr=45.0, v=1.5, rh=40.0, met=2.6, clo=0.5, duration_minutes=90
    )

    assert len(result.points) == 91
    assert result.points[0].minute == 0
    assert result.points[0].skin_temperature_c == 33.7
    assert result.points[-1].minute == 90
    assert all(math.isfinite(p.core_temperature_c) for p in result.points)


@pytest.mark.unit
def test_heavier_body_warms_more_slowly():
    light = run_gagge_reference(
        tdb=40.0, tr=40.0, v=0.5, rh=40.0, met=2.0, clo=0.5, body_mass_kg=55.0
    ).final
    heavy = run_gagge_reference(
        tdb=40.0, tr=40.0, v=0.5, rh=40.0, met=2.0, clo=0.5, body_mass_kg=95.0
    ).final

    assert heavy.core_temperature_c < light.core_temperature_c
```

### File: `backend/tests/test_global_batch_geojson.py`
```python
def test_geojson_structure():
    geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        55.2708,
                        25.2048,
                    ],
                },
                "properties": {
                    "city_id": "dubai",
                    "climate_adaptation_rate_percent": 75,
                },
            }
        ],
    }

    assert geojson["type"] == (
        "FeatureCollection"
    )

    assert (
        geojson["features"][0]
        ["geometry"]["type"]
        == "Point"
    )
```

### File: `backend/tests/test_golden_dubai_2h.py`
```python
"""Golden regression case: Dubai, 2023-07-15 12:00 local, two hours.

Offline: the Open-Meteo payload is a frozen fixture. First run (or
UPDATE_GOLDEN=1) writes expected_results.json; subsequent runs compare.
"""

import json
import os
from pathlib import Path

import pytest

from app.schemas.simulation import WeatherSimulationRequest
from app.services.reproducibility import (
    compare_regression_payloads,
    summarize_result_for_regression,
)
from app.services.weather_simulation import execute_weather_simulation


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "dubai_2h"
PAYLOAD_PATH = FIXTURE_DIR / "open_meteo_payload.json"
REQUEST_PATH = FIXTURE_DIR / "request.json"
EXPECTED_PATH = FIXTURE_DIR / "expected_results.json"


@pytest.mark.integration
@pytest.mark.asyncio
async def test_dubai_two_hour_golden_case(monkeypatch):
    if not PAYLOAD_PATH.exists():
        pytest.skip(
            "Fixture missing. Run: python scripts/capture_weather_fixture.py "
            "tests/fixtures/dubai_2h"
        )

    payload = json.loads(PAYLOAD_PATH.read_text(encoding="utf-8"))

    async def fake_request_open_meteo(params):
        return payload, True

    monkeypatch.setattr(
        "app.services.weather.request_open_meteo",
        fake_request_open_meteo,
    )

    request = WeatherSimulationRequest.model_validate(
        json.loads(REQUEST_PATH.read_text(encoding="utf-8"))
    )

    result = await execute_weather_simulation(request)
    actual = summarize_result_for_regression(result)

    if os.environ.get("UPDATE_GOLDEN") == "1" or not EXPECTED_PATH.exists():
        EXPECTED_PATH.write_text(
            json.dumps(actual, indent=2, sort_keys=True), encoding="utf-8"
        )
        pytest.fail(
            f"Wrote new golden file {EXPECTED_PATH}. Review, commit, and re-run."
        )

    expected = json.loads(EXPECTED_PATH.read_text(encoding="utf-8"))

    differences = compare_regression_payloads(expected, actual)

    assert not differences, "\n".join(differences)

    # Sanity: the fixture must be clean data, otherwise the case is not golden.
    quality = actual["weather"]["quality"]
    assert quality["gaps"] == []
    assert quality["duplicates_removed"] == 0
```

### File: `backend/tests/test_job_service.py`
```python
from datetime import datetime, timezone
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from app.models.simulation_job import (
    SimulationJob,
)
from app.services.job_service import (
    get_job_or_none,
    job_to_detail,
    job_to_response,
)


def make_job(
    *,
    simulation_request,
):
    now = datetime.now(timezone.utc)

    return SimpleNamespace(
        id="job-123",
        celery_task_id="task-456",
        status="completed",
        stage="completed",
        progress=100,
        city_id="dubai",
        summary_json={
            "final_skin_temperature_improvement_c": 1.2,
        },
        error_message=None,
        request_json={
            "city_id": "dubai",
            "start_time_local": (
                "2025-07-15T10:00:00"
            ),
            "duration_minutes": 120,
            "output_interval_minutes": 1,
            "person": (
                simulation_request
                .person.model_dump(
                    mode="json"
                )
            ),
            "control_material": (
                simulation_request
                .control_material.model_dump(
                    mode="json"
                )
            ),
            "rc_material": (
                simulation_request
                .rc_material.model_dump(
                    mode="json"
                )
            ),
        },
        created_at=now,
        updated_at=now,
        started_at=now,
        completed_at=now,
    )


@pytest.mark.unit
def test_job_to_response_maps_job_fields(
    simulation_request,
):
    job = make_job(
        simulation_request=simulation_request,
    )

    response = job_to_response(job)

    assert response.id == "job-123"
    assert response.celery_task_id == "task-456"
    assert response.status == "completed"
    assert response.stage == "completed"
    assert response.progress == 100
    assert response.city_id == "dubai"
    assert response.error_message is None
    assert response.summary == {
        "final_skin_temperature_improvement_c": 1.2,
    }


@pytest.mark.unit
def test_job_to_detail_validates_saved_request(
    simulation_request,
):
    job = make_job(
        simulation_request=simulation_request,
    )

    detail = job_to_detail(job)

    assert detail.id == "job-123"
    assert detail.request.city_id == "dubai"
    assert (
        detail.request.duration_minutes
        == 120
    )
    assert (
        detail.request.person.met
        == simulation_request.person.met
    )
    assert (
        detail.request.control_material.name
        == simulation_request
        .control_material.name
    )


@pytest.mark.unit
def test_get_job_or_none_uses_session_get():
    expected_job = object()
    session = Mock()
    session.get.return_value = expected_job

    result = get_job_or_none(
        session=session,
        job_id="job-123",
    )

    assert result is expected_job
    session.get.assert_called_once_with(
        SimulationJob,
        "job-123",
    )


@pytest.mark.unit
def test_get_job_or_none_returns_none():
    session = Mock()
    session.get.return_value = None

    result = get_job_or_none(
        session=session,
        job_id="missing-job",
    )

    assert result is None
```

### File: `backend/tests/test_material_fields.py`
```python
import pytest
from pydantic import ValidationError

from app.schemas.provenance import MATERIAL_PHYSICAL_FIELD_ORDER
from app.schemas.simulation import MaterialInput
from app.services.material_fields import build_material_field_manifest


@pytest.mark.unit
def test_manifest_covers_every_physical_field_in_order():
    manifest = build_material_field_manifest()
    assert [f.name for f in manifest.fields] == list(MATERIAL_PHYSICAL_FIELD_ORDER)
    assert manifest.parameter_set_version == "3.0.0"
    assert "measured" in manifest.source_types


@pytest.mark.unit
@pytest.mark.parametrize("name", MATERIAL_PHYSICAL_FIELD_ORDER)
def test_manifest_bounds_match_validation(name):
    descriptor = next(f for f in build_material_field_manifest().fields if f.name == name)

    assert descriptor.unit
    assert descriptor.description
    assert descriptor.minimum is not None and descriptor.maximum is not None

    # Sum constraints interfere for the optical pair; test the bound alone.
    base = {"name": "x", "solar_reflectance": 0.0, "infrared_emissivity": 0.0}
    MaterialInput(**{**base, name: descriptor.minimum})
    MaterialInput(**{**base, name: descriptor.maximum})

    with pytest.raises(ValidationError):
        MaterialInput(**{**base, name: descriptor.minimum - 1e-6})
    with pytest.raises(ValidationError):
        MaterialInput(**{**base, name: descriptor.maximum + 1e-6})


@pytest.mark.unit
def test_nullable_fields_declare_their_derivation():
    for field in build_material_field_manifest().fields:
        assert field.nullable == (field.derived_when_null is not None), field.name
```

### File: `backend/tests/test_material_resolution.py`
```python
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from app.schemas.simulation import MaterialInput, WeatherSimulationRequest
from app.services.material_resolution import (
    MaterialParameterConflictError,
    MaterialVersionInvalidError,
    MaterialVersionNotFoundError,
    material_input_from_version,
    resolve_material_input,
    resolve_request_materials,
)


def make_version(**overrides) -> SimpleNamespace:
    values = dict(
        id="ver-1",
        version_number=2,
        material=SimpleNamespace(name="Cool Fabric"),
        clothing_insulation_clo=0.4,
        evaporative_resistance_m2pa_w=18.0,
        clothing_area_factor=None,
        solar_reflectance=0.92,
        solar_transmittance=0.0,
        infrared_emissivity=0.95,
        infrared_transmittance=0.0,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
        source_type="measured",
        source_reference="Lab report 12",
        parameter_sources_json={"solar_reflectance": {"source_type": "measured"}},
    )
    values.update(overrides)
    return SimpleNamespace(**values)


def make_session(version) -> Mock:
    session = Mock()
    session.scalar.return_value = version
    return session


@pytest.mark.unit
def test_input_without_version_id_is_returned_untouched():
    material = MaterialInput(name="Control")
    session = Mock()

    assert resolve_material_input(session, material) is material
    session.scalar.assert_not_called()


@pytest.mark.unit
def test_omitted_fields_are_hydrated_from_the_version():
    resolved = resolve_material_input(
        make_session(make_version()),
        MaterialInput(name="RC", material_version_id="ver-1"),
    )

    assert resolved.name == "RC"
    assert resolved.clothing_insulation_clo == 0.4
    assert resolved.evaporative_resistance_m2pa_w == 18.0
    assert resolved.solar_reflectance == 0.92
    assert resolved.source_type == "measured"
    assert resolved.source_reference == "Lab report 12"
    assert resolved.parameter_sources["solar_reflectance"].source_type == "measured"


@pytest.mark.unit
def test_matching_explicit_values_are_accepted():
    resolved = resolve_material_input(
        make_session(make_version()),
        MaterialInput(
            name="RC", material_version_id="ver-1",
            clothing_insulation_clo=0.4, solar_reflectance=0.92,
        ),
    )
    assert resolved.material_version_id == "ver-1"


@pytest.mark.unit
def test_conflicting_explicit_value_is_rejected():
    with pytest.raises(MaterialParameterConflictError) as error:
        resolve_material_input(
            make_session(make_version()),
            MaterialInput(name="RC", material_version_id="ver-1", solar_reflectance=0.5),
        )

    detail = error.value.to_detail()
    assert detail["code"] == "MATERIAL_PARAMETER_CONFLICT"
    assert detail["conflicts"][0]["field"] == "solar_reflectance"


@pytest.mark.unit
def test_explicit_null_against_stored_value_is_a_conflict():
    with pytest.raises(MaterialParameterConflictError):
        resolve_material_input(
            make_session(make_version()),
            MaterialInput(name="RC", material_version_id="ver-1", evaporative_resistance_m2pa_w=None),
        )


@pytest.mark.unit
def test_unknown_version_raises():
    with pytest.raises(MaterialVersionNotFoundError):
        resolve_material_input(make_session(None), MaterialInput(name="RC", material_version_id="ghost"))


@pytest.mark.unit
def test_legacy_version_outside_bounds_is_reported():
    with pytest.raises(MaterialVersionInvalidError, match="cannot be used"):
        material_input_from_version(make_version(evaporative_resistance_m2pa_w=5000.0))


@pytest.mark.unit
def test_display_name_is_truncated_to_input_limit():
    version = make_version(material=SimpleNamespace(name="x" * 150))
    assert len(material_input_from_version(version).name) == 100


@pytest.mark.unit
def test_request_level_resolution_only_replaces_linked_materials(person, control_material):
    request = WeatherSimulationRequest(
        start_time_local="2023-07-15T12:00:00",
        person=person,
        control_material=control_material,
        rc_material=MaterialInput(name="RC", material_version_id="ver-1"),
    )

    resolved = resolve_request_materials(make_session(make_version()), request)

    assert resolved is not request
    assert resolved.control_material is control_material
    assert resolved.rc_material.solar_reflectance == 0.92
```

### File: `backend/tests/test_materials_api.py`
```python
from types import SimpleNamespace

import pytest

from app.api import simulations as simulations_api


@pytest.mark.integration
def test_material_library_round_trip(client, monkeypatch, simulation_request):
    created = client.post(
        "/api/v1/materials",
        json={
            "name": "PR-4 Test Fabric",
            "slug": "pr-4-test-fabric",
            "institution": "Test Lab",
            "initial_version": {
                "clothing_insulation_clo": 0.4,
                "evaporative_resistance_m2pa_w": 18.0,
                "solar_reflectance": 0.92,
                "infrared_emissivity": 0.95,
                "source_type": "measured",
                "parameter_sources": {
                    "solar_reflectance": {
                        "source_type": "measured",
                        "reference": "UV-Vis-NIR, 2024-03",
                    }
                },
            },
        },
    )
    assert created.status_code == 201, created.text
    version_id = created.json()["versions"][0]["id"]

    listing = client.get("/api/v1/materials/versions").json()
    assert any(item["id"] == version_id for item in listing["items"])

    simulation_input = client.get(
        f"/api/v1/materials/versions/{version_id}/simulation-input"
    ).json()
    assert simulation_input["name"] == "PR-4 Test Fabric v1"
    assert simulation_input["material_version_id"] == version_id

    # Hydration: only the id is sent.
    body = simulation_request.model_dump(mode="json")
    body["rc_material"] = {"name": "RC from library", "material_version_id": version_id}
    response = client.post("/api/v1/simulations/run", json=body)
    assert response.status_code == 200, response.text
    rc = response.json()["radiative_cooling"]
    assert rc["material_name"] == "RC from library"
    assert rc["clothing"]["evaporative_resistance_source"] == "material_input"
    assert rc["clothing"]["evaporative_resistance_m2pa_w"] == pytest.approx(18.0)

    # Conflict: id plus a different value.
    body["rc_material"] = {"name": "Edited", "material_version_id": version_id, "solar_reflectance": 0.5}
    response = client.post("/api/v1/simulations/run", json=body)
    assert response.status_code == 422
    assert response.json()["detail"]["code"] == "MATERIAL_PARAMETER_CONFLICT"

    # Unknown id.
    body["rc_material"] = {"name": "Ghost", "material_version_id": "does-not-exist"}
    response = client.post("/api/v1/simulations/run", json=body)
    assert response.status_code == 422
    assert response.json()["detail"]["code"] == "MATERIAL_VERSION_NOT_FOUND"

    # Job link is recorded and queryable.
    monkeypatch.setattr(
        simulations_api,
        "run_weather_simulation_task",
        SimpleNamespace(delay=lambda job_id: SimpleNamespace(id="celery-test-task")),
    )
    job = client.post(
        "/api/v1/simulations/jobs",
        json={
            "city_id": "dubai",
            "start_time_local": "2023-07-15T12:00:00",
            "duration_minutes": 120,
            "output_interval_minutes": 10,
            "person": body["person"],
            "control_material": body["control_material"],
            "rc_material": {"name": "RC", "material_version_id": version_id},
        },
    )
    assert job.status_code == 202, job.text
    assert job.json()["rc_material_version_id"] == version_id
    assert job.json()["control_material_version_id"] is None

    detail = client.get(f"/api/v1/simulations/jobs/{job.json()['id']}").json()
    assert detail["request"]["rc_material"]["solar_reflectance"] == pytest.approx(0.92)

    listed = client.get("/api/v1/simulations/jobs", params={"material_version_id": version_id}).json()
    assert any(item["id"] == job.json()["id"] for item in listed["items"])


@pytest.mark.integration
def test_version_with_unknown_provenance_key_is_rejected_on_write(client):
    response = client.post(
        "/api/v1/materials",
        json={
            "name": "Bad provenance",
            "slug": "bad-provenance",
            "initial_version": {"parameter_sources": {"not_a_field": {"source_type": "measured"}}},
        },
    )
    assert response.status_code == 422
```

### File: `backend/tests/test_model_parameters.py`
```python
import re

import pytest

from app.services import model_parameters as mp


@pytest.mark.unit
def test_every_parameter_has_unit_and_reference():
    for parameter in mp.list_model_parameters():
        assert parameter.unit, parameter.name
        assert parameter.reference, parameter.name


@pytest.mark.unit
def test_manifest_sha_is_stable_and_hex():
    first = mp.model_parameter_set_sha256()
    assert re.fullmatch(r"[0-9a-f]{64}", first)
    assert first == mp.model_parameter_set_sha256()


@pytest.mark.unit
def test_unknown_parameter_raises():
    with pytest.raises(KeyError, match="Unknown model parameter"):
        mp.get_parameter_value("does_not_exist")


@pytest.mark.api
def test_model_parameter_endpoint(client):
    response = client.get("/api/v1/model/parameters")
    assert response.status_code == 200
    body = response.json()
    assert body["parameter_set_version"] == mp.MODEL_PARAMETER_SET_VERSION
    assert len(body["parameters"]) == len(mp.MODEL_PARAMETERS)


@pytest.mark.api
def test_default_assumptions_endpoint(client):
    response = client.get("/api/v1/model/environment-assumptions/defaults")
    assert response.status_code == 200
    assert response.json()["sky_view_factor"] == 0.5
    
@pytest.mark.api
def test_model_metadata_endpoint(client):
    body = client.get("/api/v1/model/metadata").json()
    assert body["parameter_set_version"] == mp.MODEL_PARAMETER_SET_VERSION
    assert body["parameter_set_sha256"] == mp.model_parameter_set_sha256()


@pytest.mark.api
def test_single_parameter_endpoint(client):
    assert client.get("/api/v1/model/parameters/clo_to_si").json()["value"] == 0.155
    assert client.get("/api/v1/model/parameters/nope").status_code == 404


@pytest.mark.api
def test_material_fields_endpoint(client):
    body = client.get("/api/v1/model/material-fields").json()
    names = [f["name"] for f in body["fields"]]
    assert "evaporative_resistance_m2pa_w" in names
    assert body["fields"][0]["unit"] == "clo"
```

### File: `backend/tests/test_parameter_participation.py`
```python
"""Stage 2 definition of done: every input participates in the computation.

Each case perturbs exactly one input and requires the final skin temperature
to change. A parameter that is stored but never used fails here.
"""

import pytest

from app.schemas.environment import EnvironmentAssumptions
from app.services.two_node import (
    simulate_material,
    simulate_material_with_weather,
)


THRESHOLD_C = 1e-4


def final_skin(result) -> float:
    return result.final_skin_temperature_c


MATERIAL_PERTURBATIONS = {
    "clothing_insulation_clo": 0.9,
    "evaporative_resistance_m2pa_w": 40.0,
    "clothing_area_factor": 1.4,           # Stage 3
    "solar_reflectance": 0.7,
    "solar_transmittance": 0.2,
    "infrared_emissivity": 0.5,
    "infrared_transmittance": 0.15,
    "projected_solar_area_factor": 0.4,
    "absorbed_solar_to_body_fraction": 0.6,
}


@pytest.mark.unit
@pytest.mark.parametrize(("field", "value"), sorted(MATERIAL_PERTURBATIONS.items()))
def test_every_material_field_participates(
    environment, person, control_material, field, value
):
    baseline = simulate_material(60, 1, environment, person, control_material)
    perturbed = simulate_material(
        60, 1, environment, person, control_material.model_copy(update={field: value})
    )

    assert abs(final_skin(perturbed) - final_skin(baseline)) > THRESHOLD_C, (
        f"MaterialInput.{field} does not influence the result"
    )


PERSON_PERTURBATIONS = {
    "met": 1.2,
    "body_surface_area_m2": 2.4,           # Stage 3: was xfail (ADR 0001)
    "body_mass_kg": 95.0,                  # Stage 3
    "initial_core_temperature_c": 37.4,
    "initial_skin_temperature_c": 31.0,
}


@pytest.mark.unit
@pytest.mark.parametrize(("field", "value"), sorted(PERSON_PERTURBATIONS.items()))
def test_every_person_field_participates(
    environment, person, control_material, field, value
):
    baseline = simulate_material(60, 1, environment, person, control_material)
    perturbed = simulate_material(
        60, 1, environment, person.model_copy(update={field: value}), control_material
    )

    assert abs(final_skin(perturbed) - final_skin(baseline)) > THRESHOLD_C

# (baseline update, perturbed update). Method-dependent parameters are tested
# with the method that uses them switched on in both runs.
ASSUMPTION_PERTURBATIONS = [
    ({}, {"mean_radiant_temperature_method": "equal_to_air"}),
    ({}, {"solar_mrt_gain_k_per_w_m2": 0.02}),
    ({}, {"solar_mrt_gain_cap_k": 5.0}),
    ({}, {"sky_temperature_method": "swinbank"}),
    ({}, {"sky_temperature_method": "fixed_offset"}),
    ({}, {"sky_offset_base_k": 8.0}),
    ({}, {"sky_offset_humidity_range_k": 2.0}),
    (
        {"sky_temperature_method": "fixed_offset"},
        {"sky_temperature_method": "fixed_offset", "fixed_sky_offset_k": 25.0},
    ),
    ({}, {"sky_view_factor": 0.2}),
    ({}, {"wind_speed_scaling_factor": 0.67}),
]


@pytest.mark.unit
@pytest.mark.parametrize(("baseline_update", "perturbed_update"), ASSUMPTION_PERTURBATIONS)
def test_every_environment_assumption_participates(
    hourly_weather, person, rc_material, baseline_update, perturbed_update
):
    baseline = simulate_material_with_weather(
        120, 10, hourly_weather, person, rc_material,
        assumptions=EnvironmentAssumptions(**baseline_update),
    )
    perturbed = simulate_material_with_weather(
        120, 10, hourly_weather, person, rc_material,
        assumptions=EnvironmentAssumptions(**perturbed_update),
    )

    assert abs(final_skin(perturbed) - final_skin(baseline)) > THRESHOLD_C, (
        f"EnvironmentAssumptions {perturbed_update} does not influence the result"
    )
```

### File: `backend/tests/test_physics.py`
```python
import pytest
from pydantic import ValidationError

from app.schemas.simulation import MaterialInput
from app.services.two_node import (
    calculate_fluxes,
    saturation_vapor_pressure_kpa,
)


@pytest.mark.unit
def test_saturation_pressure_increases_with_temperature():
    pressure_20 = saturation_vapor_pressure_kpa(20.0)
    pressure_30 = saturation_vapor_pressure_kpa(30.0)
    pressure_40 = saturation_vapor_pressure_kpa(40.0)

    assert pressure_20 < pressure_30 < pressure_40


@pytest.mark.unit
def test_saturation_pressure_near_reference_value():
    pressure = saturation_vapor_pressure_kpa(30.0)

    assert pressure == pytest.approx(
        4.24,
        abs=0.08,
    )


@pytest.mark.unit
def test_invalid_optical_sum_is_rejected():
    with pytest.raises(ValidationError):
        MaterialInput(
            name="Invalid material",
            clothing_insulation_clo=0.5,
            solar_reflectance=0.8,
            solar_transmittance=0.4,
            infrared_emissivity=0.9,
            projected_solar_area_factor=0.25,
            absorbed_solar_to_body_fraction=0.35,
        )


@pytest.mark.unit
def test_higher_reflectance_reduces_solar_absorption(
    environment,
    person,
    control_material,
    rc_material,
):
    control_fluxes = calculate_fluxes(
        core_temperature_c=36.8,
        skin_temperature_c=33.7,
        environment=environment,
        person=person,
        material=control_material,
    )

    rc_fluxes = calculate_fluxes(
        core_temperature_c=36.8,
        skin_temperature_c=33.7,
        environment=environment,
        person=person,
        material=rc_material,
    )

    assert (
        rc_fluxes.absorbed_solar
        < control_fluxes.absorbed_solar
    )


@pytest.mark.unit
@pytest.mark.parametrize(
    "wind_speed",
    [0.0, 0.1, 1.0, 3.0, 8.0],
)
def test_flux_calculation_is_finite(
    wind_speed,
    environment,
    person,
    control_material,
):
    modified_environment = environment.model_copy(
        update={
            "wind_speed_m_s": wind_speed,
        }
    )

    fluxes = calculate_fluxes(
        core_temperature_c=36.8,
        skin_temperature_c=33.7,
        environment=modified_environment,
        person=person,
        material=control_material,
    )

    assert fluxes.metabolism > 0
    assert fluxes.evaporation >= 0
    assert fluxes.absorbed_solar >= 0
```

### File: `backend/tests/test_result_export.py`
```python
import csv
import io
import json
from types import SimpleNamespace

import pytest

from app.services.result_export import (
    CSV_HEADERS,
    export_result_csv,
    export_result_json,
)


EXPECTED_HEADERS = CSV_HEADERS  # single source of truth


def make_point(
    *,
    minute, core_temperature_c, skin_temperature_c, convection_w_m2,
    longwave_radiation_w_m2, evaporation_w_m2, absorbed_solar_w_m2,
    maximum_evaporation_w_m2=None, skin_wettedness=None,
    clothing_surface_temperature_c=None,
):
    return SimpleNamespace(
        minute=minute,
        core_temperature_c=core_temperature_c,
        skin_temperature_c=skin_temperature_c,
        convection_w_m2=convection_w_m2,
        longwave_radiation_w_m2=longwave_radiation_w_m2,
        evaporation_w_m2=evaporation_w_m2,
        absorbed_solar_w_m2=absorbed_solar_w_m2,
        maximum_evaporation_w_m2=maximum_evaporation_w_m2,
        skin_wettedness=skin_wettedness,
        clothing_surface_temperature_c=clothing_surface_temperature_c,
    )

@pytest.mark.unit
def test_missing_stage_3_diagnostics_export_as_blank_cells():
    rows = list(csv.reader(io.StringIO(export_result_csv(make_export_result()))))
    assert rows[1][13:] == [""] * 6

@pytest.mark.unit
def test_stage_3_diagnostics_are_exported_when_present():
    point = make_point(
        minute=0, core_temperature_c=36.8, skin_temperature_c=33.7,
        convection_w_m2=1.0, longwave_radiation_w_m2=1.0, evaporation_w_m2=1.0,
        absorbed_solar_w_m2=1.0, maximum_evaporation_w_m2=120.0,
        skin_wettedness=0.25, clothing_surface_temperature_c=35.1,
    )
    rows = list(csv.reader(io.StringIO(export_result_csv(
        make_export_result(control_points=[point], rc_points=[point])
    ))))
    assert float(rows[1][13]) == pytest.approx(120.0)
    assert float(rows[1][15]) == pytest.approx(0.25)
    assert float(rows[1][17]) == pytest.approx(35.1)

def make_export_result(
    *,
    control_points=None,
    rc_points=None,
):
    """Create the minimal result object needed for CSV export."""
    if control_points is None:
        control_points = [
            make_point(
                minute=0,
                core_temperature_c=36.8,
                skin_temperature_c=33.7,
                convection_w_m2=12.5,
                longwave_radiation_w_m2=8.1,
                evaporation_w_m2=20.0,
                absorbed_solar_w_m2=100.0,
            )
        ]

    if rc_points is None:
        rc_points = [
            make_point(
                minute=0,
                core_temperature_c=36.7,
                skin_temperature_c=32.9,
                convection_w_m2=13.5,
                longwave_radiation_w_m2=10.2,
                evaporation_w_m2=18.0,
                absorbed_solar_w_m2=25.0,
            )
        ]

    return SimpleNamespace(
        control=SimpleNamespace(time_series=control_points),
        radiative_cooling=SimpleNamespace(time_series=rc_points),
    )


@pytest.mark.unit
def test_result_csv_contains_expected_headers():
    result = make_export_result()

    csv_text = export_result_csv(result)
    rows = list(csv.reader(io.StringIO(csv_text)))

    assert rows[0] == EXPECTED_HEADERS
    assert "control_clothing_surface_temperature_c" in rows[0]
    assert len(rows[0]) == 1 + 2 * 9  # minute + 9 paired quantities


@pytest.mark.unit
def test_result_csv_contains_control_and_rc_values():
    result = make_export_result()

    csv_text = export_result_csv(result)
    rows = list(csv.reader(io.StringIO(csv_text)))

    assert len(rows) == 2

    data_row = rows[1]

    assert float(data_row[0]) == pytest.approx(0.0)

    assert float(data_row[1]) == pytest.approx(36.8)
    assert float(data_row[2]) == pytest.approx(33.7)

    assert float(data_row[3]) == pytest.approx(36.7)
    assert float(data_row[4]) == pytest.approx(32.9)

    assert float(data_row[5]) == pytest.approx(12.5)
    assert float(data_row[6]) == pytest.approx(13.5)

    assert float(data_row[7]) == pytest.approx(8.1)
    assert float(data_row[8]) == pytest.approx(10.2)

    assert float(data_row[9]) == pytest.approx(20.0)
    assert float(data_row[10]) == pytest.approx(18.0)

    assert float(data_row[11]) == pytest.approx(100.0)
    assert float(data_row[12]) == pytest.approx(25.0)


@pytest.mark.unit
def test_result_csv_with_empty_time_series_contains_only_headers():
    result = make_export_result(
        control_points=[],
        rc_points=[],
    )

    csv_text = export_result_csv(result)
    rows = list(csv.reader(io.StringIO(csv_text)))

    assert rows == [EXPECTED_HEADERS]


@pytest.mark.unit
def test_result_csv_rejects_different_time_series_lengths():
    result = make_export_result(
        control_points=[
            make_point(
                minute=0,
                core_temperature_c=36.8,
                skin_temperature_c=33.7,
                convection_w_m2=12.5,
                longwave_radiation_w_m2=8.1,
                evaporation_w_m2=20.0,
                absorbed_solar_w_m2=100.0,
            )
        ],
        rc_points=[],
    )

    with pytest.raises(ValueError):
        export_result_csv(result)


@pytest.mark.unit
def test_result_json_serializes_model_dump_as_unicode():
    payload = {
        "city": "dubai",
        "duration_minutes": 120,
        "warning": "warning",
    }

    result = SimpleNamespace(
        model_dump=lambda *, mode: payload,
    )

    json_text = export_result_json(result)
    decoded = json.loads(json_text)

    assert decoded == payload
    assert "dubai" in json_text
    assert "warning" in json_text
    assert "\\u" not in json_text
    assert "\n" in json_text
```

### File: `backend/tests/test_result_storage.py`
```python
import gzip
import json
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from app.services import result_storage


class FakeSimulationResult:
    """Provides the minimum interface required for save_simulation_result."""

    def __init__(self, payload):
        self.payload = payload
        self.requested_mode = None

    def model_dump(self, *, mode):
        self.requested_mode = mode
        return self.payload


@pytest.mark.unit
def test_save_simulation_result_creates_gzip_json_file(
    tmp_path,
    monkeypatch,
):
    result_directory = tmp_path / "results"

    monkeypatch.setattr(
        result_storage.settings,
        "result_directory",
        result_directory,
    )

    payload = {
        "city": "Dubai",
        "duration_minutes": 120,
        "warning": "warning",
    }
    result = FakeSimulationResult(payload)

    saved_path = result_storage.save_simulation_result(
        job_id="job-123",
        result=result,
    )

    assert saved_path == result_directory / "job-123.json.gz"
    assert saved_path.exists()
    assert saved_path.is_file()

    with gzip.open(
        saved_path,
        mode="rt",
        encoding="utf-8",
    ) as file:
        saved_payload = json.load(file)

    assert saved_payload == payload
    assert result.requested_mode == "json"


@pytest.mark.unit
def test_save_simulation_result_creates_missing_directory(
    tmp_path,
    monkeypatch,
):
    result_directory = (
        tmp_path
        / "nested"
        / "simulation"
        / "results"
    )

    assert not result_directory.exists()

    monkeypatch.setattr(
        result_storage.settings,
        "result_directory",
        result_directory,
    )

    result = FakeSimulationResult(
        {
            "city": "Dubai",
            "duration_minutes": 60,
        }
    )

    saved_path = result_storage.save_simulation_result(
        job_id="directory-test",
        result=result,
    )

    assert result_directory.exists()
    assert saved_path.exists()


@pytest.mark.unit
def test_save_simulation_result_removes_temporary_file(
    tmp_path,
    monkeypatch,
):
    monkeypatch.setattr(
        result_storage.settings,
        "result_directory",
        tmp_path,
    )

    result = FakeSimulationResult(
        {
            "city": "Tokyo",
            "warning": "",
        }
    )

    saved_path = result_storage.save_simulation_result(
        job_id="atomic-test",
        result=result,
    )

    temporary_path = tmp_path / "atomic-test.tmp.json.gz"

    assert saved_path.exists()
    assert not temporary_path.exists()


@pytest.mark.unit
def test_save_simulation_result_preserves_unicode(
    tmp_path,
    monkeypatch,
):
    monkeypatch.setattr(
        result_storage.settings,
        "result_directory",
        tmp_path,
    )

    payload = {
        "city": "taipei",
        "environment_model_note": "Simulation results test",
        "warning": "high temperature warning",
    }
    result = FakeSimulationResult(payload)

    saved_path = result_storage.save_simulation_result(
        job_id="unicode-test",
        result=result,
    )

    with gzip.open(
        saved_path,
        mode="rt",
        encoding="utf-8",
    ) as file:
        raw_json = file.read()

    assert "taipei" in raw_json
    assert "Simulation results test" in raw_json
    assert "high temperature warning" in raw_json
    assert "\\u81fa" not in raw_json

    assert json.loads(raw_json) == payload


@pytest.mark.unit
def test_save_simulation_result_replaces_existing_file(
    tmp_path,
    monkeypatch,
):
    monkeypatch.setattr(
        result_storage.settings,
        "result_directory",
        tmp_path,
    )

    old_result = FakeSimulationResult(
        {
            "city": "Old city",
            "duration_minutes": 30,
        }
    )
    new_result = FakeSimulationResult(
        {
            "city": "New city",
            "duration_minutes": 120,
        }
    )

    first_path = result_storage.save_simulation_result(
        job_id="same-job",
        result=old_result,
    )
    second_path = result_storage.save_simulation_result(
        job_id="same-job",
        result=new_result,
    )

    assert first_path == second_path

    with gzip.open(
        second_path,
        mode="rt",
        encoding="utf-8",
    ) as file:
        saved_payload = json.load(file)

    assert saved_payload == {
        "city": "New city",
        "duration_minutes": 120,
    }


@pytest.mark.unit
def test_load_simulation_result_reads_and_validates_payload(
    tmp_path,
    monkeypatch,
):
    result_path = tmp_path / "load-test.json.gz"

    payload = {
        "city": "Dubai",
        "duration_minutes": 120,
        "warning": "",
    }

    with gzip.open(
        result_path,
        mode="wt",
        encoding="utf-8",
    ) as file:
        json.dump(
            payload,
            file,
            ensure_ascii=False,
        )

    expected_result = object()
    model_validate = Mock(
        return_value=expected_result
    )

    fake_response_model = SimpleNamespace(
        model_validate=model_validate
    )

    monkeypatch.setattr(
        result_storage,
        "WeatherSimulationResponse",
        fake_response_model,
    )

    loaded_result = (
        result_storage.load_simulation_result(
            str(result_path)
        )
    )

    assert loaded_result is expected_result
    model_validate.assert_called_once_with(payload)


@pytest.mark.unit
def test_load_simulation_result_raises_for_missing_file(
    tmp_path,
):
    missing_path = (
        tmp_path / "does-not-exist.json.gz"
    )

    with pytest.raises(
        FileNotFoundError,
        match="The result file does not exist",
    ):
        result_storage.load_simulation_result(
            str(missing_path)
        )
```

### File: `backend/tests/test_route_registration.py`
```python
"""Tests for duplicate API route registration."""

from collections import Counter

from fastapi.routing import APIRoute

from app.main import app


def test_method_and_path_pairs_are_unique() -> None:
    route_pairs: list[tuple[str, str]] = []

    for route in app.routes:
        if not isinstance(route, APIRoute):
            continue

        for method in route.methods or set():
            if method in {"HEAD", "OPTIONS"}:
                continue

            route_pairs.append((method, route.path))

    counts = Counter(route_pairs)

    duplicates = sorted(
        route_pair
        for route_pair, count in counts.items()
        if count > 1
    )

    assert not duplicates, (
        f"Duplicate route registrations were found: {duplicates}"
    )
```

### File: `backend/tests/test_spectrum_parser.py`
```python
import pytest

from app.services.spectrum_parser import (
    parse_spectrum_csv,
)


@pytest.mark.unit
def test_parse_valid_spectrum_csv():
    content = (
        "wavelength_um,value\n"
        "0.3,0.91\n"
        "0.5,0.92\n"
        "1.0,0.93\n"
    ).encode("utf-8")

    result = parse_spectrum_csv(content)

    assert len(result.points) == 3
    assert (
        result.minimum_wavelength_um
        == pytest.approx(0.3)
    )
    assert (
        result.maximum_wavelength_um
        == pytest.approx(1.0)
    )


@pytest.mark.unit
def test_reject_value_above_one():
    content = (
        "wavelength_um,value\n"
        "0.3,0.9\n"
        "0.5,1.2\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="0 and 1",
    ):
        parse_spectrum_csv(content)


@pytest.mark.unit
def test_reject_unsorted_wavelengths():
    content = (
        "wavelength_um,value\n"
        "1.0,0.9\n"
        "0.5,0.8\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="strictly increasing",
    ):
        parse_spectrum_csv(content)

import hashlib

from app.services import spectrum_parser


@pytest.mark.unit
def test_parse_spectrum_returns_checksum():
    content = (
        "wavelength_um,value\n"
        "0.3,0.9\n"
        "0.5,0.8\n"
    ).encode("utf-8")

    result = parse_spectrum_csv(content)

    assert result.checksum_sha256 == (
        hashlib.sha256(content).hexdigest()
    )


@pytest.mark.unit
def test_parse_normalizes_header_names():
    content = (
        " Wavelength µm , Reflectance \n"
        "0.3,0.9\n"
        "0.5,0.8\n"
    ).encode("utf-8")

    result = parse_spectrum_csv(content)

    assert len(result.points) == 2


@pytest.mark.unit
def test_reject_empty_spectrum():
    with pytest.raises(
        ValueError,
        match="empty",
    ):
        parse_spectrum_csv(b"")


@pytest.mark.unit
def test_reject_non_utf8_spectrum():
    with pytest.raises(
        ValueError,
        match="UTF-8",
    ):
        parse_spectrum_csv(b"\xff\xfe\xfa")


@pytest.mark.unit
def test_reject_missing_wavelength_column():
    content = (
        "frequency,value\n"
        "1.0,0.9\n"
        "2.0,0.8\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="wavelength_um",
    ):
        parse_spectrum_csv(content)


@pytest.mark.unit
def test_reject_missing_value_column():
    content = (
        "wavelength_um,measurement\n"
        "0.3,0.9\n"
        "0.5,0.8\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="'value'",
    ):
        parse_spectrum_csv(content)


@pytest.mark.unit
@pytest.mark.parametrize(
    "row",
    [
        "not-a-number,0.8",
        "0.3,not-a-number",
    ],
)
def test_reject_invalid_numeric_values(row):
    content = (
        "wavelength_um,value\n"
        f"{row}\n"
        "0.5,0.7\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="invalid values",
    ):
        parse_spectrum_csv(content)


@pytest.mark.unit
@pytest.mark.parametrize(
    ("row", "message"),
    [
        ("nan,0.8", "wavelength"),
        ("0.3,nan", "spectrum value"),
        ("-0.3,0.8", "positive"),
        ("0.3,-0.1", "between 0 and 1"),
    ],
)
def test_reject_invalid_spectrum_ranges(
    row,
    message,
):
    content = (
        "wavelength_um,value\n"
        f"{row}\n"
        "0.5,0.7\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match=message,
    ):
        parse_spectrum_csv(content)


@pytest.mark.unit
def test_reject_single_data_point():
    content = (
        "wavelength_um,value\n"
        "0.3,0.9\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="at least two",
    ):
        parse_spectrum_csv(content)


@pytest.mark.unit
def test_reject_file_above_size_limit(
    monkeypatch,
):
    monkeypatch.setattr(
        spectrum_parser,
        "MAX_SPECTRUM_FILE_SIZE",
        10,
    )

    with pytest.raises(
        ValueError,
        match="2 MB",
    ):
        spectrum_parser.parse_spectrum_csv(
            b"x" * 11
        )


@pytest.mark.unit
def test_reject_too_many_points(
    monkeypatch,
):
    monkeypatch.setattr(
        spectrum_parser,
        "MAX_SPECTRUM_POINTS",
        2,
    )

    content = (
        "wavelength_um,value\n"
        "0.1,0.9\n"
        "0.2,0.8\n"
        "0.3,0.7\n"
    ).encode("utf-8")

    with pytest.raises(
        ValueError,
        match="cannot exceed",
    ):
        spectrum_parser.parse_spectrum_csv(
            content
        )
```

### File: `backend/tests/test_stage_4_2_export.py`
```python
import zipfile
from io import BytesIO
from types import SimpleNamespace

import pytest

from app.services.global_batch_export import (
    build_batch_export_zip,
)


@pytest.mark.unit
def test_export_contains_required_files():
    city_result = SimpleNamespace(
        city_id="dubai",
        city_name="Dubai",
        country="United Arab Emirates",
        status="completed",
        latitude=25.2048,
        longitude=55.2708,
        climate_adaptation_rate_percent=80.0,
        exposure_coverage_percent=75.0,
        annual_average_skin_improvement_c=0.5,
        annual_average_core_improvement_c=0.1,
        maximum_skin_improvement_c=1.2,
        effective_cooling_hours=400,
        sampled_day_count=36,
        eligible_sample_count=27,
        evaluated_weighted_days=274,
        beneficial_weighted_days=219,
        retry_count=0,
        error_message=None,
        monthly_json=[],
    )

    batch = SimpleNamespace(
        id="test-batch",
        status="completed",
        request_json={
            "year": 2023,
            "sample_days_per_month": 3,
        },
        summary_json={},
        city_results=[city_result],
    )

    archive_bytes = build_batch_export_zip(
        batch
    )

    with zipfile.ZipFile(
        BytesIO(archive_bytes)
    ) as archive:
        names = set(
            archive.namelist()
        )

    assert "city-summary.csv" in names
    assert "sample-results.csv" in names
    assert "results.geojson" in names
    assert "results.json" in names
```

### File: `backend/tests/test_stage_4_2_exposure.py`
```python
import pytest

from app.schemas.global_batch import (
    GlobalBatchCreate,
)
from app.schemas.simulation import (
    MaterialInput,
    PersonInput,
)
from app.services.climate_adaptation import (
    is_exposure_eligible,
)


def make_request(
    *,
    match_mode: str = "all",
) -> GlobalBatchCreate:
    person = PersonInput(
        met=2.0,
        body_surface_area_m2=1.8,
        initial_core_temperature_c=36.8,
        initial_skin_temperature_c=33.7,
    )

    control = MaterialInput(
        name="Control",
        clothing_insulation_clo=0.5,
        solar_reflectance=0.3,
        solar_transmittance=0,
        infrared_emissivity=0.9,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
    )

    radiative = MaterialInput(
        name="Radiative",
        clothing_insulation_clo=0.4,
        solar_reflectance=0.92,
        solar_transmittance=0,
        infrared_emissivity=0.95,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
    )

    return GlobalBatchCreate(
        city_ids=["dubai"],
        sample_days_per_month=3,
        minimum_air_temperature_c=30,
        minimum_solar_radiation_w_m2=300,
        exposure_match_mode=match_mode,
        person=person,
        control_material=control,
        rc_material=radiative,
    )


@pytest.mark.unit
def test_all_mode_requires_all_thresholds():
    request = make_request(
        match_mode="all",
    )

    assert is_exposure_eligible(
        mean_air_temperature_c=35,
        mean_solar_radiation_w_m2=200,
        request=request,
    ) is False


@pytest.mark.unit
def test_any_mode_requires_one_threshold():
    request = make_request(
        match_mode="any",
    )

    assert is_exposure_eligible(
        mean_air_temperature_c=35,
        mean_solar_radiation_w_m2=200,
        request=request,
    ) is True


@pytest.mark.unit
def test_no_threshold_means_all_samples_eligible():
    request = make_request()

    request.minimum_air_temperature_c = None
    request.minimum_solar_radiation_w_m2 = None

    assert is_exposure_eligible(
        mean_air_temperature_c=5,
        mean_solar_radiation_w_m2=0,
        request=request,
    ) is True
```

### File: `backend/tests/test_stage_4_2_sampling.py`
```python
import pytest

from app.services.climate_adaptation import (
    build_weighted_sample_days,
)


@pytest.mark.unit
def test_three_samples_cover_entire_month():
    samples = build_weighted_sample_days(
        days_in_month=31,
        sample_count=3,
    )

    assert len(samples) == 3

    assert sum(
        weight
        for _, weight in samples
    ) == 31

    assert samples == sorted(
        samples,
        key=lambda item: item[0],
    )


@pytest.mark.unit
def test_one_legacy_sample_uses_requested_day():
    samples = build_weighted_sample_days(
        days_in_month=30,
        sample_count=1,
        legacy_representative_day=15,
    )

    assert samples == [
        (15, 30),
    ]


@pytest.mark.unit
def test_sample_count_cannot_exceed_month_days():
    samples = build_weighted_sample_days(
        days_in_month=3,
        sample_count=7,
    )

    assert len(samples) == 3

    assert sum(
        weight
        for _, weight in samples
    ) == 3
```

### File: `backend/tests/test_stage_4_3_estimate.py`
```python
import pytest


@pytest.mark.api
def test_daily_batch_estimate(
    client,
    person,
    control_material,
    rc_material,
):
    response = client.post(
        "/api/v1/global-batches/estimate",
        json={
            "name": "Daily estimate",
            "city_ids": [
                "dubai",
                "singapore",
            ],
            "year": 2024,
            "start_month": 1,
            "end_month": 12,
            "analysis_resolution": "daily",
            "daily_stride_days": 1,
            "sample_days_per_month": 3,
            "local_start_hour": 12,
            "duration_minutes": 120,
            "output_interval_minutes": 10,
            "minimum_skin_improvement_c": 0.2,
            "minimum_air_temperature_c": 30,
            "minimum_solar_radiation_w_m2": 300,
            "exposure_match_mode": "all",
            "person": person.model_dump(mode="json"),
            "control_material": control_material.model_dump(mode="json"),
            "rc_material": rc_material.model_dump(mode="json"),
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["samples_per_city"] == 366
    assert data["total_samples"] == 732
    assert (
        data["thermal_simulation_count"]
        == 1464
    )
    assert (
        data["estimated_weather_requests"]
        == 24
    )
```

### File: `backend/tests/test_stage_4_3_sampling.py`
```python
import calendar

import pytest

from app.schemas.global_batch import (
    GlobalBatchCreate,
)
from app.schemas.simulation import (
    MaterialInput,
    PersonInput,
)
from app.services.annual_sampling import (
    build_daily_stride_sample_days,
    build_month_sampling_plan,
    estimate_sample_count,
)


def make_request(
    *,
    resolution: str,
    stride: int = 1,
) -> GlobalBatchCreate:
    person = PersonInput(
        met=2.0,
        body_surface_area_m2=1.8,
        initial_core_temperature_c=36.8,
        initial_skin_temperature_c=33.7,
    )

    control = MaterialInput(
        name="Control",
        clothing_insulation_clo=0.5,
        solar_reflectance=0.3,
        solar_transmittance=0,
        infrared_emissivity=0.9,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
    )

    radiative = MaterialInput(
        name="Radiative cooling",
        clothing_insulation_clo=0.4,
        solar_reflectance=0.92,
        solar_transmittance=0,
        infrared_emissivity=0.95,
        projected_solar_area_factor=0.25,
        absorbed_solar_to_body_fraction=0.35,
    )

    return GlobalBatchCreate(
        city_ids=["dubai"],
        year=2024,
        start_month=1,
        end_month=12,
        analysis_resolution=resolution,
        daily_stride_days=stride,
        person=person,
        control_material=control,
        rc_material=radiative,
    )


@pytest.mark.unit
def test_daily_stride_one_has_one_sample_per_day():
    samples = build_daily_stride_sample_days(
        days_in_month=31,
        stride_days=1,
    )

    assert len(samples) == 31

    assert all(
        weight == 1
        for _, weight in samples
    )

    assert sum(
        weight
        for _, weight in samples
    ) == 31


@pytest.mark.unit
def test_daily_stride_seven_covers_month():
    samples = build_daily_stride_sample_days(
        days_in_month=31,
        stride_days=7,
    )

    assert len(samples) == 5

    assert sum(
        weight
        for _, weight in samples
    ) == 31


@pytest.mark.unit
def test_leap_year_daily_plan_has_366_samples():
    request = make_request(
        resolution="daily",
        stride=1,
    )

    assert calendar.isleap(
        request.year
    )

    assert estimate_sample_count(
        request
    ) == 366


@pytest.mark.unit
def test_month_plan_returns_actual_dates():
    request = make_request(
        resolution="daily",
        stride=1,
    )

    plan = build_month_sampling_plan(
        request=request,
        month=2,
    )

    assert len(plan) == 29
    assert plan[0].date_local.day == 1
    assert plan[-1].date_local.day == 29
```

### File: `backend/tests/test_stage_4_3_weather_slice.py`
```python
from datetime import (
    datetime,
    timedelta,
    timezone,
)

import pytest

from app.schemas.weather import (
    CityResponse,
    WeatherPoint,
    WeatherSourceMetadata,
    WeatherTimeSeries,
)
from app.services.weather import (
    slice_weather_time_series,
)

from app.services.weather_quality import WeatherInsufficientCoverageError


def make_weather() -> WeatherTimeSeries:
    start = datetime(
        2023,
        7,
        1,
        0,
        tzinfo=timezone.utc,
    )

    points = [
        WeatherPoint(
            timestamp=start
            + timedelta(hours=index),
            air_temperature_c=30,
            relative_humidity_percent=60,
            wind_speed_m_s=2,
            ghi_w_m2=500,
            direct_radiation_w_m2=300,
            diffuse_radiation_w_m2=200,
            dni_w_m2=600,
        )
        for index in range(72)
    ]

    city = CityResponse(
        id="test",
        name="Test City",
        country="Test",
        latitude=0,
        longitude=0,
        elevation_m=0,
        timezone="UTC",
        climate_type="test",
    )

    return WeatherTimeSeries(
        city=city,
        requested_start_time=start,
        requested_end_time=(
            start + timedelta(hours=71)
        ),
        points=points,
        source=WeatherSourceMetadata(
            provider="test",
            dataset="test",
            model="test",
            latitude=0,
            longitude=0,
            elevation_m=0,
            timezone="UTC",
            downloaded_at=start,
            from_cache=True,
            attribution="test",
        ),
    )


@pytest.mark.unit
def test_slice_weather_includes_padding():
    weather = make_weather()

    sliced = slice_weather_time_series(
        weather=weather,
        start_time_local=datetime(
            2023,
            7,
            2,
            12,
        ),
        duration_minutes=120,
        padding_hours=1,
    )

    timestamps = [
        point.timestamp
        for point in sliced.points
    ]

    assert datetime(
        2023,
        7,
        2,
        11,
        tzinfo=timezone.utc,
    ) in timestamps

    assert datetime(
        2023,
        7,
        2,
        15,
        tzinfo=timezone.utc,
    ) in timestamps


@pytest.mark.unit
def test_slice_fails_when_range_not_covered():
    weather = make_weather()

    with pytest.raises(
        WeatherInsufficientCoverageError,
        match="does not cover",
    ):
        slice_weather_time_series(
            weather=weather,
            start_time_local=datetime(2023, 8, 1, 12),
            duration_minutes=120,
        )

```

### File: `backend/tests/test_stage_4_4_analytics.py`
```python
from datetime import (
    datetime,
    timedelta,
)

import pytest

from app.schemas.global_batch import (
    DailyAdaptationResult,
)
from app.services.climate_analytics import (
    detect_heatwave_events,
    weighted_percentile,
)


def make_sample(
    *,
    day: int,
    maximum_temperature_c: float,
    skin_improvement_c: float = 0.5,
) -> DailyAdaptationResult:
    return DailyAdaptationResult(
        sample_date_local=datetime(
            2025,
            7,
            day,
            12,
        ),
        weight_days=1,
        mean_air_temperature_c=(
            maximum_temperature_c - 3
        ),
        maximum_air_temperature_c=(
            maximum_temperature_c
        ),
        mean_solar_radiation_w_m2=500,
        maximum_solar_radiation_w_m2=800,
        exposure_eligible=True,
        beneficial=True,
        average_skin_improvement_c=(
            skin_improvement_c
        ),
        final_skin_improvement_c=(
            skin_improvement_c
        ),
        average_core_improvement_c=0.1,
        maximum_skin_improvement_c=(
            skin_improvement_c + 0.1
        ),
        weather_from_cache=True,
    )


@pytest.mark.unit
def test_weighted_percentile():
    values = [
        (0.1, 1),
        (0.2, 1),
        (0.3, 1),
        (0.4, 1),
        (0.5, 1),
    ]

    assert weighted_percentile(
        values,
        50,
    ) == 0.3

    assert weighted_percentile(
        values,
        90,
    ) == 0.5


@pytest.mark.unit
def test_weighted_percentile_uses_weights():
    values = [
        (0.1, 10),
        (1.0, 1),
    ]

    assert weighted_percentile(
        values,
        50,
    ) == 0.1


@pytest.mark.unit
def test_detects_consecutive_heatwave():
    samples = [
        make_sample(
            day=1,
            maximum_temperature_c=34,
        ),
        make_sample(
            day=2,
            maximum_temperature_c=36,
        ),
        make_sample(
            day=3,
            maximum_temperature_c=37,
        ),
        make_sample(
            day=4,
            maximum_temperature_c=38,
        ),
        make_sample(
            day=5,
            maximum_temperature_c=33,
        ),
    ]

    events = detect_heatwave_events(
        samples=samples,
        temperature_threshold_c=35,
        minimum_consecutive_days=3,
    )

    assert len(events) == 1
    assert events[0].duration_days == 3
    assert (
        events[0].peak_air_temperature_c
        == 38
    )


@pytest.mark.unit
def test_non_consecutive_hot_days_are_not_heatwave():
    samples = [
        make_sample(
            day=1,
            maximum_temperature_c=36,
        ),
        make_sample(
            day=3,
            maximum_temperature_c=37,
        ),
        make_sample(
            day=4,
            maximum_temperature_c=38,
        ),
    ]

    events = detect_heatwave_events(
        samples=samples,
        temperature_threshold_c=35,
        minimum_consecutive_days=3,
    )

    assert events == []
```

### File: `backend/tests/test_stage_4_4_checkpoint.py`
```python
from datetime import datetime
from types import SimpleNamespace
from uuid import uuid4

import pytest

from app.models.global_batch import (
    GlobalBatchJob,
    GlobalCityResult,
)
from app.schemas.global_batch import (
    DailyAdaptationResult,
    GlobalBatchCreate,
    MonthlyAdaptationResult,
)

@pytest.fixture
def completed_partial_batch(
    db_session,
    person,
    control_material,
    rc_material,
):
    request = GlobalBatchCreate(
        city_ids=["dubai"],
        year=2025,
        sample_days_per_month=1,
        resume_from_checkpoint=True,
        person=person,
        control_material=control_material,
        rc_material=rc_material,
    )
    
    batch = GlobalBatchJob(
        id=str(uuid4()),
        status="failed",
        request_json=request.model_dump(
            mode="json",
        ),
        summary_json={},
    )

    db_session.add(batch)
    db_session.flush()

    city_result = GlobalCityResult(
        id=str(uuid4()),
        batch_id=batch.id,
        city_id="dubai",
        city_name="Dubai",
        country="United Arab Emirates",
        latitude=25.2048,
        longitude=55.2708,
        status="failed",
        stage="failed",
        progress=25,
        monthly_json=[
            {
                "month": 1,
                "sampled_day_count": 1,
                "eligible_sample_count": 1,
                "total_weighted_days": 31,
                "evaluated_weighted_days": 31,
                "beneficial_weighted_days": 31,
                "exposure_coverage_percent": 100,
                "climate_adaptation_rate_percent": 100,
                "average_skin_improvement_c": 0.5,
                "average_core_improvement_c": 0.1,
                "maximum_skin_improvement_c": 0.8,
                "samples": [],
            }
        ],
        completed_month_count=1,
        last_checkpoint_month=1,
        resumed_from_checkpoint=False,
        retry_count=0,
        error_message="Simulated interruption",
    )

    db_session.add(city_result)
    db_session.commit()

    db_session.refresh(batch)
    db_session.refresh(city_result)

    return SimpleNamespace(
        id=batch.id,
        batch=batch,
        city_result=city_result,
        session=db_session,
    )


@pytest.mark.integration
def test_retry_preserves_checkpoint_when_enabled(
    client,
    completed_partial_batch,
):
    session = completed_partial_batch.session
    batch = completed_partial_batch.batch
    city_result = completed_partial_batch.city_result

    # 驗證 fixture 符合 retry endpoint 的前置條件。
    assert batch.status == "failed"
    assert city_result.status == "failed"
    assert city_result.monthly_json is not None
    assert len(city_result.monthly_json) == 1
    assert city_result.completed_month_count == 1
    assert city_result.last_checkpoint_month == 1

    original_monthly_json = (
        city_result.monthly_json.copy()
    )

    response = client.post(
        (
            "/api/v1/global-batches/"
            f"{batch.id}"
            "/retry-failed"
        )
    )

    assert response.status_code == 202, (
        response.text
    )

    session.expire_all()

    refreshed_result = session.get(
        GlobalCityResult,
        city_result.id,
    )

    assert refreshed_result is not None

    # Checkpoint 不應在 retry 時被刪除。
    assert refreshed_result.monthly_json is not None
    assert (
        refreshed_result.monthly_json
        == original_monthly_json
    )
    assert (
        refreshed_result.completed_month_count
        == 1
    )
    assert (
        refreshed_result.last_checkpoint_month
        == 1
    )
    assert (
        refreshed_result.resumed_from_checkpoint
        is True
    )


@pytest.mark.unit
def test_monthly_checkpoint_round_trip():
    sample = DailyAdaptationResult(
        sample_date_local=datetime(
            2025,
            1,
            15,
            12,
        ),
        weight_days=31,
        mean_air_temperature_c=32,
        maximum_air_temperature_c=36,
        mean_solar_radiation_w_m2=500,
        maximum_solar_radiation_w_m2=800,
        exposure_eligible=True,
        beneficial=True,
        average_skin_improvement_c=0.5,
        final_skin_improvement_c=0.6,
        average_core_improvement_c=0.1,
        maximum_skin_improvement_c=0.8,
        weather_from_cache=True,
    )

    result = MonthlyAdaptationResult(
        month=1,
        sampled_day_count=1,
        eligible_sample_count=1,
        total_weighted_days=31,
        evaluated_weighted_days=31,
        beneficial_weighted_days=31,
        exposure_coverage_percent=100,
        climate_adaptation_rate_percent=100,
        average_skin_improvement_c=0.5,
        average_core_improvement_c=0.1,
        maximum_skin_improvement_c=0.8,
        samples=[sample],
    )

    payload = result.model_dump(
        mode="json"
    )

    restored = (
        MonthlyAdaptationResult
        .model_validate(payload)
    )

    assert restored.month == 1
    assert restored.sampled_day_count == 1
    assert len(restored.samples) == 1
```

### File: `backend/tests/test_two_node.py`
```python
import math

import pytest

from app.services.two_node import simulate_material


@pytest.mark.unit
def test_simulation_returns_expected_number_of_points(
    environment,
    person,
    control_material,
):
    result = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    assert len(result.time_series) == 121
    assert result.time_series[0].minute == 0
    assert result.time_series[-1].minute == 120


@pytest.mark.unit
def test_initial_temperatures_are_preserved(
    environment,
    person,
    control_material,
):
    result = simulate_material(
        duration_minutes=60,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    initial = result.time_series[0]

    assert initial.core_temperature_c == pytest.approx(
        person.initial_core_temperature_c,
        abs=1e-4,
    )

    assert initial.skin_temperature_c == pytest.approx(
        person.initial_skin_temperature_c,
        abs=1e-4,
    )


@pytest.mark.unit
def test_all_temperatures_are_finite(
    environment,
    person,
    control_material,
):
    result = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    for point in result.time_series:
        assert math.isfinite(
            point.core_temperature_c
        )
        assert math.isfinite(
            point.skin_temperature_c
        )


@pytest.mark.unit
def test_temperature_stays_in_broad_physiological_range(
    environment,
    person,
    control_material,
):
    result = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    for point in result.time_series:
        assert 30.0 < point.core_temperature_c < 43.0
        assert 15.0 < point.skin_temperature_c < 45.0


@pytest.mark.unit
def test_energy_balance_residual_is_small(
    environment,
    person,
    control_material,
):
    result = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    assert (
        result.diagnostics
        .normalized_residual_percent
        < 1.0
    )


@pytest.mark.unit
def test_rc_material_reduces_skin_temperature(
    environment,
    person,
    control_material,
    rc_material,
):
    control = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    rc = simulate_material(
        duration_minutes=120,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=rc_material,
    )

    assert (
        rc.final_skin_temperature_c
        < control.final_skin_temperature_c
    )


@pytest.mark.unit
def test_identical_materials_produce_identical_results(
    environment,
    person,
    control_material,
):
    first = simulate_material(
        duration_minutes=60,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    second = simulate_material(
        duration_minutes=60,
        output_interval_minutes=1,
        environment=environment,
        person=person,
        material=control_material,
    )

    assert (
        first.final_core_temperature_c
        == pytest.approx(
            second.final_core_temperature_c,
            abs=1e-8,
        )
    )

    assert (
        first.final_skin_temperature_c
        == pytest.approx(
            second.final_skin_temperature_c,
            abs=1e-8,
        )
    )
```

### File: `backend/tests/test_weather_api.py`
```python
from datetime import datetime

import pytest

from app.api import weather as weather_api
from app.schemas.weather import (
    CityResponse,
    WeatherPoint,
    WeatherSourceMetadata,
    WeatherTimeSeries,
)

@pytest.fixture
def weather_series() -> WeatherTimeSeries:
    return WeatherTimeSeries(
        city=CityResponse(
            id="dubai",
            name="Dubai",
            country="United Arab Emirates",
            latitude=25.25,
            longitude=55.25,
            elevation_m=12.0,
            timezone="Asia/Dubai",
            climate_type="hot_arid",
        ),
        requested_start_time=datetime(
            2025,
            7,
            15,
            10,
            0,
        ),
        requested_end_time=datetime(
            2025,
            7,
            15,
            12,
            0,
        ),
        points=[
            WeatherPoint(
                timestamp=datetime(
                    2025,
                    7,
                    15,
                    10,
                    0,
                ),
                air_temperature_c=38.0,
                relative_humidity_percent=40.0,
                wind_speed_m_s=1.5,
                ghi_w_m2=700.0,
                direct_radiation_w_m2=520.0,
                diffuse_radiation_w_m2=180.0,
                dni_w_m2=750.0,
            ),
            WeatherPoint(
                timestamp=datetime(
                    2025,
                    7,
                    15,
                    11,
                    0,
                ),
                air_temperature_c=39.0,
                relative_humidity_percent=38.0,
                wind_speed_m_s=2.0,
                ghi_w_m2=800.0,
                direct_radiation_w_m2=620.0,
                diffuse_radiation_w_m2=180.0,
                dni_w_m2=820.0,
            ),
        ],
        source=WeatherSourceMetadata(
            provider="Open-Meteo",
            dataset="Historical Weather API",
            model="ERA5",
            latitude=25.25,
            longitude=55.25,
            elevation_m=12.0,
            timezone="Asia/Dubai",
            downloaded_at=datetime(
                2025,
                7,
                15,
                13,
                0,
            ),
            from_cache=False,
            attribution="Weather data by Open-Meteo",
        ),
    )

@pytest.mark.unit
def test_weather_cities_endpoint(client):
    response = client.get(
        "/api/v1/weather/cities"
    )

    assert response.status_code == 200

    payload = response.json()

    assert len(payload) >= 3

    city_ids = {
        city["id"]
        for city in payload
    }

    assert {
        "dubai",
        "guangzhou",
        "lhasa",
    }.issubset(city_ids)

@pytest.mark.unit
def test_weather_history_endpoint(
    client,
    monkeypatch,
    weather_series,
):
    async def fake_get_historical_weather(
        **kwargs,
    ):
        return weather_series

    monkeypatch.setattr(
        weather_api,
        "get_historical_weather",
        fake_get_historical_weather,
    )

    response = client.get(
        "/api/v1/weather/history",
        params={
            "city_id": "dubai",
            "start_time_local": (
                "2025-07-15T10:00:00"
            ),
            "duration_minutes": 120,
        },
    )

    assert response.status_code == 200

    payload = response.json()

    assert payload["city"]["id"] == "dubai"
    assert len(payload["points"]) == 2

    assert (
        payload["points"][0]["air_temperature_c"]
        == pytest.approx(38.0)
    )

    assert payload["source"]["from_cache"] is False

@pytest.mark.unit
def test_weather_history_rejects_unknown_city(
    client,
    monkeypatch,
):
    def fake_get_city(city_id):
        raise ValueError(
            f"City not supported: {city_id}"
        )

    monkeypatch.setattr(
        weather_api,
        "get_city",
        fake_get_city,
    )

    response = client.get(
        "/api/v1/weather/history",
        params={
            "city_id": "unknown",
            "start_time_local": (
                "2025-07-15T10:00:00"
            ),
            "duration_minutes": 120,
        },
    )

    assert response.status_code == 422

    assert (
        "City not supported"
        in response.json()["detail"]
    )


@pytest.mark.unit
def test_weather_history_converts_service_error_to_502(
    client,
    monkeypatch,
):
    async def fake_get_historical_weather(
        **kwargs,
    ):
        raise RuntimeError(
            "Open-Meteo unavailable"
        )

    monkeypatch.setattr(
        weather_api,
        "get_historical_weather",
        fake_get_historical_weather,
    )

    response = client.get(
        "/api/v1/weather/history",
        params={
            "city_id": "dubai",
            "start_time_local": (
                "2025-07-15T10:00:00"
            ),
            "duration_minutes": 120,
        },
    )

    assert response.status_code == 502
    assert response.json()["detail"] == (
        "Open-Meteo unavailable"
    )


@pytest.mark.unit
@pytest.mark.parametrize(
    "duration",
    [
        0,
        1441,
    ],
)
def test_weather_history_validates_duration(
    client,
    duration,
):
    response = client.get(
        "/api/v1/weather/history",
        params={
            "city_id": "dubai",
            "start_time_local": (
                "2025-07-15T10:00:00"
            ),
            "duration_minutes": duration,
        },
    )

    assert response.status_code == 422
```

### File: `backend/tests/test_weather_interpolation.py`
```python
from datetime import datetime
from zoneinfo import ZoneInfo

import pytest

from app.schemas.weather import (
    CityResponse,
    WeatherPoint,
    WeatherSourceMetadata,
    WeatherTimeSeries,
)
from app.services.weather_interpolation import (
    WeatherInterpolator,
)


@pytest.fixture
def weather_series():
    timezone = ZoneInfo("Asia/Dubai")

    start = datetime(
        2025,
        7,
        15,
        10,
        0,
        tzinfo=timezone,
    )

    return WeatherTimeSeries(
        city=CityResponse(
            id="dubai",
            name="Dubai",
            country="United Arab Emirates",
            latitude=25.2048,
            longitude=55.2708,
            elevation_m=16,
            timezone="Asia/Dubai",
            climate_type="hot_dry",
        ),
        requested_start_time=start,
        requested_end_time=start.replace(
            hour=12
        ),
        points=[
            WeatherPoint(
                timestamp=start.replace(hour=9),
                air_temperature_c=36,
                relative_humidity_percent=45,
                wind_speed_m_s=1,
                ghi_w_m2=500,
                direct_radiation_w_m2=400,
                diffuse_radiation_w_m2=100,
                dni_w_m2=700,
            ),
            WeatherPoint(
                timestamp=start.replace(hour=10),
                air_temperature_c=38,
                relative_humidity_percent=40,
                wind_speed_m_s=2,
                ghi_w_m2=700,
                direct_radiation_w_m2=550,
                diffuse_radiation_w_m2=150,
                dni_w_m2=800,
            ),
            WeatherPoint(
                timestamp=start.replace(hour=11),
                air_temperature_c=40,
                relative_humidity_percent=35,
                wind_speed_m_s=3,
                ghi_w_m2=900,
                direct_radiation_w_m2=700,
                diffuse_radiation_w_m2=200,
                dni_w_m2=900,
            ),
            WeatherPoint(
                timestamp=start.replace(hour=12),
                air_temperature_c=42,
                relative_humidity_percent=30,
                wind_speed_m_s=4,
                ghi_w_m2=1000,
                direct_radiation_w_m2=800,
                diffuse_radiation_w_m2=200,
                dni_w_m2=950,
            ),
        ],
        source=WeatherSourceMetadata(
            provider="test",
            dataset="test",
            model="test",
            latitude=25.2,
            longitude=55.2,
            elevation_m=16,
            timezone="Asia/Dubai",
            downloaded_at=start,
            from_cache=False,
            attribution="test",
        ),
    )


@pytest.mark.unit
def test_weather_interpolation_at_start(
    weather_series,
):
    interpolator = (
        WeatherInterpolator.from_series(
            weather_series
        )
    )

    environment = interpolator.environment_at(
        0
    )

    assert (
        environment.air_temperature_c
        == pytest.approx(38)
    )

    assert (
        environment.solar_radiation_w_m2
        == pytest.approx(700)
    )


@pytest.mark.unit
def test_weather_interpolation_at_half_hour(
    weather_series,
):
    interpolator = (
        WeatherInterpolator.from_series(
            weather_series
        )
    )

    environment = interpolator.environment_at(
        1800
    )

    assert (
        environment.air_temperature_c
        == pytest.approx(39)
    )

    assert (
        environment.wind_speed_m_s
        == pytest.approx(2.5)
    )

    assert (
        environment.solar_radiation_w_m2
        == pytest.approx(800)
    )

import numpy as np


@pytest.mark.unit
def test_environment_clamps_negative_wind_and_solar():
    interpolator = WeatherInterpolator(
        relative_seconds=np.array(
            [0.0, 3600.0]
        ),
        temperatures=np.array(
            [30.0, 30.0]
        ),
        humidities=np.array(
            [50.0, 50.0]
        ),
        wind_speeds=np.array(
            [-2.0, -1.0]
        ),
        ghi_values=np.array(
            [-100.0, -50.0]
        ),
    )

    environment = interpolator.environment_at(
        1800
    )

    assert environment.wind_speed_m_s == 0
    assert (
        environment.solar_radiation_w_m2
        == 0
    )
    assert (
        environment.mean_radiant_temperature_c
        == pytest.approx(30.0)
    )


@pytest.mark.unit
def test_mean_radiant_temperature_increase_is_capped():
    interpolator = WeatherInterpolator(
        relative_seconds=np.array(
            [0.0, 3600.0]
        ),
        temperatures=np.array(
            [30.0, 30.0]
        ),
        humidities=np.array(
            [50.0, 50.0]
        ),
        wind_speeds=np.array(
            [1.0, 1.0]
        ),
        ghi_values=np.array(
            [1500.0, 1500.0]
        ),
    )

    environment = interpolator.environment_at(
        0
    )
    
    assert (
        environment.solar_radiation_w_m2
        == pytest.approx(1500.0)
    )
    
    assert (
        environment.mean_radiant_temperature_c
        == pytest.approx(45.0)
    )

from app.services.weather_interpolation import (
    InterpolationOutOfRangeError,
    WeatherInterpolator,
)
from app.services.weather_quality import WeatherInsufficientCoverageError


@pytest.mark.unit
def test_interpolation_outside_range_raises(weather_series):
    interpolator = WeatherInterpolator.from_series(weather_series)

    with pytest.raises(InterpolationOutOfRangeError):
        interpolator.environment_at(24 * 60 * 60)

    with pytest.raises(InterpolationOutOfRangeError):
        interpolator.environment_at(-2 * 60 * 60)


@pytest.mark.unit
def test_interpolation_at_exact_boundaries_is_allowed(weather_series):
    interpolator = WeatherInterpolator.from_series(weather_series)

    first = interpolator.environment_at(-3600)   # 09:00 point
    last = interpolator.environment_at(7200)     # 12:00 point

    assert first.air_temperature_c == pytest.approx(36.0)
    assert last.air_temperature_c == pytest.approx(42.0)


@pytest.mark.unit
def test_from_series_rejects_series_not_covering_requested_window(
    weather_series,
):
    truncated = weather_series.model_copy(
        update={"points": weather_series.points[:-1]}  # ends 11:00, needs 12:00
    )

    with pytest.raises(WeatherInsufficientCoverageError):
        WeatherInterpolator.from_series(truncated)
```

### File: `backend/tests/test_weather_quality.py`
```python
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import pytest

from app.schemas.weather import WeatherPoint
from app.services.weather_quality import (
    WeatherDuplicateConflictError,
    WeatherGapInWindowError,
    WeatherInsufficientCoverageError,
    WeatherNaiveTimestampError,
    ensure_window_covered,
    normalize_timeline,
)


TZ = ZoneInfo("Asia/Dubai")
BASE = datetime(2023, 7, 15, 9, tzinfo=TZ)


def make_point(timestamp: datetime, temperature: float = 30.0) -> WeatherPoint:
    return WeatherPoint(
        timestamp=timestamp,
        air_temperature_c=temperature,
        relative_humidity_percent=40.0,
        wind_speed_m_s=2.0,
        ghi_w_m2=600.0,
        direct_radiation_w_m2=450.0,
        diffuse_radiation_w_m2=150.0,
        dni_w_m2=700.0,
    )


def hourly(count: int, *, skip: set[int] = frozenset()) -> list[WeatherPoint]:
    return [
        make_point(BASE + timedelta(hours=index), 30.0 + index)
        for index in range(count)
        if index not in skip
    ]


@pytest.mark.unit
def test_unsorted_input_is_sorted_and_noted():
    points = list(reversed(hourly(4)))

    cleaned, report = normalize_timeline(points)

    assert [p.timestamp for p in cleaned] == sorted(p.timestamp for p in points)
    assert report.was_sorted is False
    assert any("not sorted" in note for note in report.notes)


@pytest.mark.unit
def test_identical_duplicate_is_removed():
    points = hourly(3) + [make_point(BASE + timedelta(hours=1), 31.0)]

    cleaned, report = normalize_timeline(points)

    assert len(cleaned) == 3
    assert report.duplicates_removed == 1


@pytest.mark.unit
def test_conflicting_duplicate_is_rejected():
    points = hourly(3) + [make_point(BASE + timedelta(hours=1), 99.0)]

    with pytest.raises(WeatherDuplicateConflictError):
        normalize_timeline(points)


@pytest.mark.unit
def test_naive_timestamp_is_rejected():
    naive = make_point(datetime(2023, 7, 15, 9))

    with pytest.raises(WeatherNaiveTimestampError):
        normalize_timeline([naive])


@pytest.mark.unit
def test_gap_is_reported_but_not_raised_by_normalize():
    cleaned, report = normalize_timeline(hourly(6, skip={3}))

    assert len(cleaned) == 5
    assert len(report.gaps) == 1
    assert report.gaps[0].missing_steps == 1
    assert report.expected_step_seconds == 3600


@pytest.mark.unit
def test_window_with_gap_inside_is_rejected():
    cleaned, report = normalize_timeline(hourly(6, skip={3}))

    with pytest.raises(WeatherGapInWindowError):
        ensure_window_covered(
            cleaned,
            window_start=BASE + timedelta(hours=1),
            window_end=BASE + timedelta(hours=4),
            step_seconds=report.expected_step_seconds,
        )


@pytest.mark.unit
def test_window_outside_gap_is_accepted():
    cleaned, report = normalize_timeline(hourly(6, skip={5}))

    ensure_window_covered(
        cleaned,
        window_start=BASE + timedelta(hours=1),
        window_end=BASE + timedelta(hours=3),
        step_seconds=report.expected_step_seconds,
    )


@pytest.mark.unit
def test_missing_tail_is_rejected():
    cleaned, report = normalize_timeline(hourly(4))  # 09:00 .. 12:00

    with pytest.raises(WeatherInsufficientCoverageError, match="does not cover"):
        ensure_window_covered(
            cleaned,
            window_start=BASE + timedelta(hours=1),
            window_end=BASE + timedelta(hours=3, minutes=1),
            step_seconds=report.expected_step_seconds,
        )


@pytest.mark.unit
def test_exact_boundaries_are_accepted():
    cleaned, report = normalize_timeline(hourly(4))

    ensure_window_covered(
        cleaned,
        window_start=BASE,
        window_end=BASE + timedelta(hours=3),
        step_seconds=report.expected_step_seconds,
    )
```

### File: `backend/tests/test_weather_service.py`
```python
from datetime import datetime

import pytest

from app.core.cities import get_city
from app.services.weather import (
    get_historical_weather,
)


OPEN_METEO_RESPONSE = {
    "latitude": 25.25,
    "longitude": 55.25,
    "elevation": 12.0,
    "timezone": "Asia/Dubai",
    "hourly": {
        "time": [
            "2025-07-15T09:00",
            "2025-07-15T10:00",
            "2025-07-15T11:00",
            "2025-07-15T12:00",
            "2025-07-15T13:00",
        ],
        "temperature_2m": [
            36.0,
            38.0,
            39.0,
            40.0,
            40.5,
        ],
        "relative_humidity_2m": [
            45.0,
            40.0,
            38.0,
            35.0,
            34.0,
        ],
        "wind_speed_10m": [
            1.0,
            1.5,
            2.0,
            2.5,
            2.0,
        ],
        "shortwave_radiation": [
            500.0,
            700.0,
            800.0,
            900.0,
            850.0,
        ],
        "direct_radiation": [
            350.0,
            520.0,
            620.0,
            700.0,
            650.0,
        ],
        "diffuse_radiation": [
            150.0,
            180.0,
            180.0,
            200.0,
            200.0,
        ],
        "direct_normal_irradiance": [
            600.0,
            750.0,
            820.0,
            880.0,
            830.0,
        ],
    },
}


@pytest.mark.integration
@pytest.mark.asyncio
async def test_historical_weather_with_mock(
    monkeypatch,
):
    async def mock_request_open_meteo(
        params,
    ):
        return OPEN_METEO_RESPONSE, False

    monkeypatch.setattr(
        "app.services.weather.request_open_meteo",
        mock_request_open_meteo,
    )

    city = get_city("dubai")

    result = await get_historical_weather(
        city=city,
        start_time_local=datetime(
            2025,
            7,
            15,
            10,
            0,
        ),
        duration_minutes=120,
    )

    assert result.city.id == "dubai"
    assert len(result.points) >= 2
    assert result.source.from_cache is False
    assert (
        result.points[1]
        .air_temperature_c
        == pytest.approx(38.0)
    )
```

### File: `backend/tests/test_weather_simulation.py`
```python
from datetime import datetime
from types import SimpleNamespace

import pytest

from app.schemas.simulation import (
    WeatherSimulationRequest,
)
from app.services import weather_simulation


class FakeWeatherSimulationResponse(
    SimpleNamespace
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


@pytest.mark.unit
@pytest.mark.asyncio
async def test_execute_weather_simulation(
    monkeypatch,
    person,
    control_material,
    rc_material,
):
    request = WeatherSimulationRequest(
        city_id="dubai",
        start_time_local=datetime(
            2025,
            7,
            15,
            10,
            0,
        ),
        duration_minutes=120,
        output_interval_minutes=1,
        person=person,
        control_material=control_material,
        rc_material=rc_material,
    )

    city = SimpleNamespace(
        id="dubai",
        name="Dubai",
    )
    weather = object()

    control_result = SimpleNamespace(
        time_series=[
            SimpleNamespace(
                skin_temperature_c=35.0,
            ),
            SimpleNamespace(
                skin_temperature_c=36.0,
            ),
        ],
        final_skin_temperature_c=36.0,
        final_core_temperature_c=38.0,
    )

    rc_result = SimpleNamespace(
        time_series=[
            SimpleNamespace(
                skin_temperature_c=33.0,
            ),
            SimpleNamespace(
                skin_temperature_c=34.0,
            ),
        ],
        final_skin_temperature_c=34.0,
        final_core_temperature_c=37.5,
    )

    get_city_calls = []
    weather_calls = []
    simulation_calls = []
    assumption_calls = []
    
    def fake_get_city(city_id):
        get_city_calls.append(city_id)
        return city

    async def fake_get_historical_weather(
        *,
        city,
        start_time_local,
        duration_minutes,
    ):
        weather_calls.append(
            {
                "city": city,
                "start_time_local": (
                    start_time_local
                ),
                "duration_minutes": (
                    duration_minutes
                ),
            }
        )
        return weather

    def fake_simulate_material_with_weather(
        *,
        duration_minutes,
        output_interval_minutes,
        weather,
        person,
        material,
        assumptions=None,
    ):
        simulation_calls.append(material.name)
        assumption_calls.append(assumptions)
        
        if material.name == control_material.name:
            return control_result

        return rc_result

    monkeypatch.setattr(
        weather_simulation,
        "get_city",
        fake_get_city,
    )
    monkeypatch.setattr(
        weather_simulation,
        "get_historical_weather",
        fake_get_historical_weather,
    )
    monkeypatch.setattr(
        weather_simulation,
        "simulate_material_with_weather",
        fake_simulate_material_with_weather,
    )
    monkeypatch.setattr(
        weather_simulation,
        "WeatherSimulationResponse",
        FakeWeatherSimulationResponse,
    )

    progress_events = []

    result = await (
        weather_simulation
        .execute_weather_simulation(
            request,
            progress_callback=lambda progress, stage: (
                progress_events.append(
                    (progress, stage)
                )
            ),
        )
    )

    assert get_city_calls == ["dubai"]

    assert len(weather_calls) == 1
    assert (
        weather_calls[0]["duration_minutes"]
        == 120
    )

    assert simulation_calls == [
        control_material.name,
        rc_material.name,
    ]

    assert assumption_calls == [
        request.environment_assumptions,
        request.environment_assumptions,
    ]
    
    assert progress_events == [
        (10, "downloading_weather"),
        (
            30,
            "running_control_simulation",
        ),
        (
            65,
            "running_radiative_cooling_simulation",
        ),
        (90, "generating_summary"),
    ]

    assert result.city == "Dubai"
    assert result.control is control_result
    assert (
        result.radiative_cooling
        is rc_result
    )

    assert (
        result.summary
        .final_skin_temperature_improvement_c
        == pytest.approx(2.0)
    )
    assert (
        result.summary
        .final_core_temperature_improvement_c
        == pytest.approx(0.5)
    )
    assert (
        result.summary
        .average_skin_temperature_improvement_c
        == pytest.approx(2.0)
    )


@pytest.mark.unit
@pytest.mark.asyncio
async def test_execute_weather_simulation_without_callback(
    monkeypatch,
    person,
    control_material,
    rc_material,
):
    request = WeatherSimulationRequest(
        city_id="dubai",
        start_time_local=datetime(
            2025,
            7,
            15,
            10,
            0,
        ),
        duration_minutes=1,
        output_interval_minutes=1,
        person=person,
        control_material=control_material,
        rc_material=rc_material,
    )

    city = SimpleNamespace(
        id="dubai",
        name="Dubai",
    )
    weather = object()

    scenario = SimpleNamespace(
        time_series=[
            SimpleNamespace(
                skin_temperature_c=34.0,
            )
        ],
        final_skin_temperature_c=34.0,
        final_core_temperature_c=37.0,
    )

    monkeypatch.setattr(
        weather_simulation,
        "get_city",
        lambda city_id: city,
    )

    async def fake_weather(**kwargs):
        return weather

    monkeypatch.setattr(
        weather_simulation,
        "get_historical_weather",
        fake_weather,
    )
    monkeypatch.setattr(
        weather_simulation,
        "simulate_material_with_weather",
        lambda **kwargs: scenario,
    )
    monkeypatch.setattr(
        weather_simulation,
        "WeatherSimulationResponse",
        FakeWeatherSimulationResponse,
    )

    result = await (
        weather_simulation
        .execute_weather_simulation(
            request,
            progress_callback=None,
        )
    )

    assert result.city == "Dubai"
    assert (
        result.summary
        .final_skin_temperature_improvement_c
        == 0
    )
```

### File: `backend/tests/test_worker_tasks.py`
```python
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from app.models.simulation_job import (
    SimulationJob,
)
from app.worker import tasks


def make_session_context(session):
    context = MagicMock()
    context.__enter__.return_value = session
    context.__exit__.return_value = False

    return context


@pytest.mark.unit
def test_update_job_updates_fields_and_commits(
    monkeypatch,
):
    job = SimpleNamespace(
        status="queued",
        stage="queued",
        progress=0,
    )

    session = MagicMock()
    session.get.return_value = job

    session_context = make_session_context(
        session
    )

    monkeypatch.setattr(
        tasks,
        "SessionLocal",
        lambda: session_context,
    )

    tasks.update_job(
        "job-123",
        status="running",
        stage="initializing",
        progress=10,
    )

    session.get.assert_called_once_with(
        SimulationJob,
        "job-123",
    )

    assert job.status == "running"
    assert job.stage == "initializing"
    assert job.progress == 10

    session.commit.assert_called_once_with()


@pytest.mark.unit
def test_update_job_rejects_missing_job(
    monkeypatch,
):
    session = MagicMock()
    session.get.return_value = None

    session_context = make_session_context(
        session
    )

    monkeypatch.setattr(
        tasks,
        "SessionLocal",
        lambda: session_context,
    )

    with pytest.raises(
        RuntimeError,
        match="Simulation task not found:job-404",
    ):
        tasks.update_job(
            "job-404",
            status="running",
        )

    session.commit.assert_not_called()


@pytest.mark.unit
@pytest.mark.parametrize(
    "status",
    [
        "queued",
        "running",
        "completed",
        "failed",
    ],
)
def test_ensure_not_cancelled_accepts_active_status(
    monkeypatch,
    status,
):
    job = SimpleNamespace(
        status=status,
    )

    session = MagicMock()
    session.get.return_value = job

    session_context = make_session_context(
        session
    )

    monkeypatch.setattr(
        tasks,
        "SessionLocal",
        lambda: session_context,
    )

    tasks.ensure_not_cancelled("job-123")

    session.get.assert_called_once_with(
        SimulationJob,
        "job-123",
    )


@pytest.mark.unit
@pytest.mark.parametrize(
    "status",
    [
        "cancelling",
        "cancelled",
    ],
)
def test_ensure_not_cancelled_raises_for_cancelled_job(
    monkeypatch,
    status,
):
    job = SimpleNamespace(
        status=status,
    )

    session = MagicMock()
    session.get.return_value = job

    session_context = make_session_context(
        session
    )

    monkeypatch.setattr(
        tasks,
        "SessionLocal",
        lambda: session_context,
    )

    with pytest.raises(
        tasks.JobCancelledError,
    ):
        tasks.ensure_not_cancelled(
            "job-123"
        )


@pytest.mark.unit
def test_ensure_not_cancelled_rejects_missing_job(
    monkeypatch,
):
    session = MagicMock()
    session.get.return_value = None

    session_context = make_session_context(
        session
    )

    monkeypatch.setattr(
        tasks,
        "SessionLocal",
        lambda: session_context,
    )

    with pytest.raises(
        RuntimeError,
        match="Simulation task not found:job-404",
    ):
        tasks.ensure_not_cancelled(
            "job-404"
        )
```

