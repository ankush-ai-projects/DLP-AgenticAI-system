"""Aggregate all version-one API endpoint routers."""

from fastapi import APIRouter

from app.api.v1.endpoints import (
    agentic_scan,
    assets,
    auth,
    dashboard,
    health,
    remediation,
    scan,
    user,
)


api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health.router)
api_router.include_router(auth.router)
api_router.include_router(user.router)
api_router.include_router(scan.router)
api_router.include_router(assets.router)
api_router.include_router(agentic_scan.router)
api_router.include_router(dashboard.router)
api_router.include_router(remediation.router)
