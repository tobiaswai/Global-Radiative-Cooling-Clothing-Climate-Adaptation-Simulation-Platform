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