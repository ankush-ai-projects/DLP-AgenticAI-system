import logging
import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.connectors import discover_databases
from app.core.dependencies import get_current_user
from app.core.secrets import CREDENTIAL_CONFIG_KEY, encrypt_credentials
from app.db.session import get_db
from app.models.user import User
from app.repositories.enterprise_repo import EnterpriseRepository
from app.schemas.enterprise import (
    AssetCreate,
    AssetResponse,
    DatabaseBulkCreateRequest,
    DatabaseBulkCreateResponse,
    DatabaseDiscoveryRequest,
    DatabaseDiscoveryResponse,
)


router = APIRouter(prefix="/assets", tags=["enterprise-assets"])
logger = logging.getLogger(__name__)


def _discovery_config(payload: DatabaseDiscoveryRequest) -> dict:
    config = {
        "host": payload.host.strip(),
        "port": payload.port,
        "username": payload.username,
        "password": payload.password.get_secret_value(),
        "include_system": payload.include_system_databases,
    }
    if payload.platform == "mssql":
        config.update(
            {
                "driver": payload.driver,
                "encrypt": payload.encrypt,
                "trust_server_certificate": payload.trust_server_certificate,
            }
        )
    return config


def _fetch_databases(payload: DatabaseDiscoveryRequest) -> list[str]:
    try:
        return discover_databases(payload.platform, _discovery_config(payload))
    except (ValueError, RuntimeError) as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
    except Exception as error:
        logger.warning(
            "Database discovery failed: platform=%s host=%s error_type=%s",
            payload.platform,
            payload.host,
            type(error).__name__,
        )
        message = str(error).lower()
        if any(token in message for token in ("access denied", "login failed", "authentication")):
            detail = "Database authentication failed. Check the username and password."
        elif any(token in message for token in ("timeout", "timed out", "refused", "unreachable")):
            detail = "Unable to reach the database server. Check host, port, and network access."
        else:
            detail = "Database connection failed. Check the connection settings and server logs."
        raise HTTPException(status_code=400, detail=detail) from error


@router.post(
    "/discover-databases",
    response_model=DatabaseDiscoveryResponse,
)
def list_available_databases(
    payload: DatabaseDiscoveryRequest,
    current_user: User = Depends(get_current_user),
):
    """Test credentials and list databases visible to the current login."""
    del current_user
    return DatabaseDiscoveryResponse(
        platform=payload.platform,
        databases=_fetch_databases(payload),
    )


@router.post(
    "/register-databases",
    response_model=DatabaseBulkCreateResponse,
    status_code=201,
)
def register_databases(
    payload: DatabaseBulkCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Verify a selection and register multiple databases with encrypted credentials."""
    discovered = set(_fetch_databases(payload))
    unavailable = [name for name in payload.database_names if name not in discovered]
    if unavailable:
        raise HTTPException(
            status_code=400,
            detail=f"These databases are not accessible: {', '.join(unavailable)}",
        )

    repository = EnterpriseRepository(db)
    existing = repository.existing_database_names(
        current_user.id,
        platform=payload.platform,
        host=payload.host.strip(),
        port=payload.port,
        database_names=payload.database_names,
    )
    selected = [name for name in payload.database_names if name not in existing]
    secret_ref = f"database_{uuid.uuid4().hex}"
    private_config = {
        CREDENTIAL_CONFIG_KEY: encrypt_credentials(
            payload.username,
            payload.password.get_secret_value(),
        )
    }
    if payload.platform == "mssql":
        private_config.update(
            {
                "driver": payload.driver,
                "encrypt": payload.encrypt,
                "trust_server_certificate": payload.trust_server_certificate,
            }
        )

    multiple = len(payload.database_names) > 1
    asset_payloads = [
        AssetCreate(
            name=(
                f"{payload.asset_name} - {database_name}"[:120]
                if multiple
                else payload.asset_name
            ),
            asset_type="database",
            platform=payload.platform,
            tenant_key=payload.tenant_key,
            host=payload.host.strip(),
            port=payload.port,
            database_name=database_name,
            secret_ref=secret_ref,
            config=private_config,
        )
        for database_name in selected
    ]
    registered = (
        repository.create_assets(current_user.id, asset_payloads)
        if asset_payloads
        else []
    )
    return DatabaseBulkCreateResponse(
        registered=registered,
        skipped_databases=sorted(existing, key=str.casefold),
    )


@router.post("", response_model=AssetResponse, status_code=201)
def create_asset(
    payload: AssetCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return EnterpriseRepository(db).create_asset(current_user.id, payload)


@router.get("", response_model=list[AssetResponse])
def list_assets(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return EnterpriseRepository(db).list_assets(current_user.id)


@router.get("/{asset_id}", response_model=AssetResponse)
def get_asset(
    asset_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    asset = EnterpriseRepository(db).get_asset(asset_id, current_user.id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset
