"""Tests for production-hardening additions.

Covers: fail-fast startup validation (insecure SECRET_KEY / wildcard CORS
in production), the liveness/readiness health endpoints, auth rate
limiting, and the global exception handler's leak-free error response.
"""
import importlib

import pytest
from fastapi.testclient import TestClient


def _reload_config_and_main(monkeypatch, **env):
    """Reload app.core.config and app.main with a patched environment so
    each test gets a fresh Settings() instance instead of the cached one.

    Every relevant var is explicitly set (with a safe default) on every
    call, not just the ones the test cares about -- otherwise a value left
    over in os.environ by a previous test's monkeypatch.setenv (reverted
    only at that test's teardown, i.e. *after* this function already ran
    for the next test in sequence) can leak into this reload.
    """
    defaults = {
        "ENVIRONMENT": "development",
        "SECRET_KEY": "your-secret-key-change-in-production",
        "ALLOWED_ORIGINS": '["*"]',
        "SKIP_AUTH": "true",
    }
    defaults.update(env)
    for key, value in defaults.items():
        monkeypatch.setenv(key, value)

    import app.core.config as config_module
    importlib.reload(config_module)

    import app.main as main_module
    importlib.reload(main_module)
    return main_module, config_module


def test_production_with_default_secret_key_refuses_to_start(monkeypatch):
    with pytest.raises(RuntimeError, match="SECRET_KEY"):
        _reload_config_and_main(
            monkeypatch,
            ENVIRONMENT="production",
            SECRET_KEY="your-secret-key-change-in-production",
            ALLOWED_ORIGINS='["https://app.example.com"]',
        )


def test_production_with_wildcard_cors_refuses_to_start(monkeypatch):
    with pytest.raises(RuntimeError, match="ALLOWED_ORIGINS"):
        _reload_config_and_main(
            monkeypatch,
            ENVIRONMENT="production",
            SECRET_KEY="a" * 40,
            ALLOWED_ORIGINS='["*"]',
        )


def test_production_with_safe_config_starts_and_hides_docs(monkeypatch):
    main_module, _ = _reload_config_and_main(
        monkeypatch,
        ENVIRONMENT="production",
        SECRET_KEY="a" * 40,
        ALLOWED_ORIGINS='["https://app.example.com"]',
        SKIP_AUTH="false",
    )
    assert main_module.app.docs_url is None
    assert main_module.app.openapi_url is None


def test_production_with_skip_auth_refuses_to_start(monkeypatch):
    with pytest.raises(RuntimeError, match="SKIP_AUTH"):
        _reload_config_and_main(
            monkeypatch,
            ENVIRONMENT="production",
            SECRET_KEY="a" * 40,
            ALLOWED_ORIGINS='["https://app.example.com"]',
            SKIP_AUTH="true",
        )


def test_development_mode_allows_insecure_defaults(monkeypatch):
    """The insecure defaults must stay usable in dev -- this only guards prod."""
    main_module, _ = _reload_config_and_main(monkeypatch, ENVIRONMENT="development")
    assert main_module.app.docs_url == "/docs"


@pytest.fixture
def client(monkeypatch):
    main_module, _ = _reload_config_and_main(monkeypatch, ENVIRONMENT="development")
    with TestClient(main_module.app, raise_server_exceptions=False) as test_client:
        yield test_client


def test_liveness_endpoint(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_readiness_endpoint_reports_database_ok(client):
    response = client.get("/api/v1/health/ready")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ready"
    assert body["database"] == "ok"


def test_global_exception_handler_hides_stack_trace(client):
    @client.app.get("/api/v1/__test_only_crash")
    def _crash():
        raise ValueError("should never reach the client")

    response = client.get("/api/v1/__test_only_crash")

    assert response.status_code == 500
    body = response.json()
    assert body["detail"] == "Internal server error."
    assert "request_id" in body
    assert "ValueError" not in response.text
    assert "should never reach the client" not in response.text


def test_login_is_rate_limited_after_repeated_attempts(client):
    statuses = [
        client.post(
            "/api/v1/auth/login",
            data={"username": "nouser", "password": "wrong"},
        ).status_code
        for _ in range(15)
    ]

    assert 401 in statuses  # normal failed-auth responses
    assert 429 in statuses  # then the rate limiter kicks in
    # once limited, it should stay limited for the rest of the burst
    assert statuses[-1] == 429
