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
        **request.initial_version.model_dump(),
    )

    material.versions.append(version)
    session.add(material)

    try:
        session.commit()
    except IntegrityError as error:
        session.rollback()

        raise HTTPException(
            status_code=409,
            detail="材料 slug 已存在",
        ) from error

    created = load_material(
        session,
        material.id,
    )

    if created is None:
        raise HTTPException(
            status_code=500,
            detail="材料建立後無法重新讀取",
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
            detail="找不到材料",
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
            detail="找不到材料",
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
            detail="找不到材料",
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
        **request.model_dump(),
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
    version = session.scalar(
        select(MaterialVersion)
        .options(
            selectinload(
                MaterialVersion.material
            )
        )
        .where(
            MaterialVersion.id == version_id
        )
    )

    if version is None:
        raise HTTPException(
            status_code=404,
            detail="找不到材料版本",
        )

    return MaterialInput(
        name=(
            f"{version.material.name} "
            f"v{version.version_number}"
        ),
        clothing_insulation_clo=(
            version.clothing_insulation_clo
        ),
        solar_reflectance=(
            version.solar_reflectance
        ),
        solar_transmittance=(
            version.solar_transmittance
        ),
        infrared_emissivity=(
            version.infrared_emissivity
        ),
        projected_solar_area_factor=(
            version.projected_solar_area_factor
        ),
        absorbed_solar_to_body_fraction=(
            version.absorbed_solar_to_body_fraction
        ),
    )


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
            detail="不支持的光譜類型",
        )

    version = session.get(
        MaterialVersion,
        version_id,
    )

    if version is None:
        raise HTTPException(
            status_code=404,
            detail="找不到材料版本",
        )

    if not file.filename:
        raise HTTPException(
            status_code=422,
            detail="缺少文件名稱",
        )

    if not file.filename.lower().endswith(
        ".csv"
    ):
        raise HTTPException(
            status_code=422,
            detail="只接受 CSV 文件",
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
            detail="找不到光譜資料",
        )

    return SpectrumResponse(
        summary=SpectrumSummary.model_validate(
            spectrum
        ),
        points=spectrum.points_json,
    )