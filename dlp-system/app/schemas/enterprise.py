"""Validated API and workflow schemas for the enterprise scanner."""
from __future__ import annotations

from typing import Any, Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    SecretStr,
    field_serializer,
    field_validator,
    model_validator,
)

from app.core.secrets import CREDENTIAL_CONFIG_KEY


AssetTypeValue = Literal["database", "system"]


class AssetCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    asset_type: AssetTypeValue
    platform: Literal["mysql", "mssql", "windows", "linux", "sqlite"]
    tenant_key: str = Field(default="default", min_length=1, max_length=80)
    host: str | None = None
    port: int | None = Field(default=None, ge=1, le=65535)
    database_name: str | None = None
    root_path: str | None = None
    secret_ref: str | None = None
    config: dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def validate_target(self):
        if self.asset_type == "database":
            if self.platform not in {"mysql", "mssql", "sqlite"}:
                raise ValueError("Database asset platform must be mysql, mssql, or sqlite")
            if self.platform != "sqlite" and not self.host:
                raise ValueError("Database host is required")
        else:
            if self.platform not in {"windows", "linux"}:
                raise ValueError("System asset platform must be windows or linux")
            if not self.root_path:
                raise ValueError("System root_path is required")
        return self


class AssetResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    asset_type: str
    platform: str
    host: str | None
    port: int | None
    database_name: str | None
    root_path: str | None
    secret_ref: str | None
    config: dict[str, Any]
    is_active: bool

    @field_serializer("config")
    def hide_private_config(self, value: dict[str, Any]) -> dict[str, Any]:
        """Never return stored credential material to the browser."""
        return {
            key: item
            for key, item in value.items()
            if key != CREDENTIAL_CONFIG_KEY
        }


class DatabaseDiscoveryRequest(BaseModel):
    platform: Literal["mysql", "mssql"]
    host: str = Field(min_length=1, max_length=255)
    port: int = Field(ge=1, le=65535)
    username: str = Field(min_length=1, max_length=255)
    password: SecretStr
    driver: str = Field(default="ODBC Driver 18 for SQL Server", max_length=255)
    encrypt: bool = True
    trust_server_certificate: bool = False
    include_system_databases: bool = False


class DatabaseDiscoveryResponse(BaseModel):
    platform: Literal["mysql", "mssql"]
    databases: list[str] = Field(default_factory=list)


class DatabaseBulkCreateRequest(DatabaseDiscoveryRequest):
    asset_name: str = Field(min_length=2, max_length=120)
    database_names: list[str] = Field(min_length=1, max_length=100)
    tenant_key: str = Field(default="default", min_length=1, max_length=80)

    @field_validator("database_names")
    @classmethod
    def normalize_database_names(cls, value: list[str]) -> list[str]:
        names = list(dict.fromkeys(name.strip() for name in value if name.strip()))
        if not names:
            raise ValueError("Select at least one database")
        if any(len(name) > 255 for name in names):
            raise ValueError("Database names cannot exceed 255 characters")
        return names


class DatabaseBulkCreateResponse(BaseModel):
    registered: list[AssetResponse] = Field(default_factory=list)
    skipped_databases: list[str] = Field(default_factory=list)


class ScanGoalRequest(BaseModel):
    asset_id: int
    goal: str = Field(min_length=10, max_length=2000)
    entities: list[str] = Field(
        default_factory=lambda: ["CREDIT_CARD", "AADHAAR", "PAN", "EMAIL", "PHONE"]
    )
    # Restricts a SYSTEM scan to specific extensions, e.g. [".csv", ".pdf"].
    # Ignored for database scans. Empty/omitted = every supported
    # extension (SUPPORTED_EXTENSIONS in app/tools/filesystem_tools.py).
    file_extensions: list[str] | None = None
    batch_size: int = Field(default=1000, ge=1, le=10000)
    sample_limit_per_table: int = Field(default=5000, ge=1, le=100000)
    require_human_review_for_critical: bool = True
    dry_run: bool = True
    execute_async: bool = False


class ApprovalRequest(BaseModel):
    approved: bool
    note: str = Field(default="", max_length=1000)


class AgenticScanResponse(BaseModel):
    scan_id: int
    status: str
    plan: dict[str, Any] = Field(default_factory=dict)
    summary: dict[str, Any] = Field(default_factory=dict)
    approval_required: bool = False
    error: str | None = None
    runtime: str = "langgraph"
    thread_id: str | None = None 