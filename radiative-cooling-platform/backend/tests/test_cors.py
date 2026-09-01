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