"""Application Configuration"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


_INSECURE_DEFAULT_SECRET = "your-secret-key-change-in-production"


class Settings(BaseSettings):
    """Application settings from environment variables"""

    # API Configuration
    API_TITLE: str = "DLP System API"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "Data Loss Prevention System API"
    DEBUG: bool = False
    ENVIRONMENT: str = "development"

    # Database Configuration
    DATABASE_URL: str = "sqlite:///./dlp.db"
    SQLALCHEMY_ECHO: bool = False

    # Security
    SECRET_KEY: str = _INSECURE_DEFAULT_SECRET
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    ALLOWED_ORIGINS: list = ["*"]

    # Redis/Cache
    REDIS_URL: Optional[str] = None

    # Celery
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/0"

    # Agentic runtime
    MAX_AGENT_ITERATIONS: int = 8
    MAX_AGENT_RETRIES: int = 3
    DEFAULT_SCAN_BATCH_SIZE: int = 1000
    MAX_SCAN_BATCH_SIZE: int = 10000
    MAX_FILE_SIZE_MB: int = 25
    SYSTEM_SCAN_ALLOWED_ROOTS: str = "./test_data"
    SYSTEM_SCAN_ALLOW_ANY_PATH: bool = True
    LANGGRAPH_CHECKPOINTER: str = "auto"
    LANGGRAPH_SQLITE_PATH: str = "./langgraph_checkpoints.sqlite"
    LANGGRAPH_POSTGRES_URL: Optional[str] = None

    RAG_BACKEND: str = "local"

    SKIP_AUTH: bool = True

    LLM_API_KEY: Optional[str] = None
    LLM_BASE_URL: str = "https://api.openai.com/v1"
    LLM_MODEL: Optional[str] = None
    LLM_TIMEOUT_SECONDS: int = 30
    SEND_MASKED_METADATA_ONLY: bool = True

    REMEDIATION_BACKUP_ROOT: str = "./remediation_backups"
    REMEDIATION_MASTER_KEY: Optional[str] = None
    REMEDIATION_DELETE_RETENTION_DAYS: int = 30

    AUTH_RATE_LIMIT_ATTEMPTS: int = 10
    AUTH_RATE_LIMIT_WINDOW_SECONDS: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )

    @property
    def is_production(self) -> bool:
        return self.ENVIRONMENT.lower() in {"production", "prod"}

    @property
    def has_insecure_secret_key(self) -> bool:
        return self.SECRET_KEY == _INSECURE_DEFAULT_SECRET or len(self.SECRET_KEY) < 32


settings = Settings() 