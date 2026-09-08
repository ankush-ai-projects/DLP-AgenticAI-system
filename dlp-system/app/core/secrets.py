"""Credential helpers that keep plaintext passwords out of asset records."""
from __future__ import annotations

import base64
import hashlib
import json
import os
import re
from typing import Protocol

from cryptography.fernet import Fernet, InvalidToken

from app.core.config import settings


CREDENTIAL_CONFIG_KEY = "credential_ciphertext"


def _credential_cipher() -> Fernet:
    """Derive a stable Fernet key from the application's private secret."""
    digest = hashlib.sha256(settings.SECRET_KEY.encode("utf-8")).digest()
    return Fernet(base64.urlsafe_b64encode(digest))


def encrypt_credentials(username: str, password: str) -> str:
    """Encrypt database credentials before they are persisted."""
    payload = json.dumps(
        {"username": username, "password": password},
        separators=(",", ":"),
    ).encode("utf-8")
    return _credential_cipher().encrypt(payload).decode("ascii")


def decrypt_credentials(ciphertext: str) -> dict[str, str]:
    """Decrypt credentials saved by :func:`encrypt_credentials`."""
    try:
        raw = _credential_cipher().decrypt(ciphertext.encode("ascii"))
        value = json.loads(raw.decode("utf-8"))
    except (InvalidToken, ValueError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(
            "Stored database credentials cannot be decrypted. "
            "Confirm that SECRET_KEY has not changed."
        ) from exc

    if not isinstance(value, dict) or "username" not in value or "password" not in value:
        raise ValueError("Stored database credentials are invalid")

    return {
        "username": str(value["username"]),
        "password": str(value["password"]),
    }


class SecretProvider(Protocol):
    def resolve(self, secret_ref: str) -> dict[str, str]: ...


class EnvironmentSecretProvider:
    """Resolve a secret reference from DLP_SECRET_<NORMALIZED_REF> JSON."""

    def resolve(self, secret_ref: str) -> dict[str, str]:
        if not secret_ref:
            raise ValueError("A secret_ref is required for remote database assets")
        normalized = re.sub(r"[^A-Za-z0-9]", "_", secret_ref).upper()
        key = f"DLP_SECRET_{normalized}"
        raw = os.getenv(key)
        if not raw:
            raise ValueError(f"Credential reference is not configured: {secret_ref}")
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Secret {secret_ref} must contain JSON") from exc
        if not isinstance(value, dict) or "username" not in value or "password" not in value:
            raise ValueError(f"Secret {secret_ref} requires username and password")
        return {str(k): str(v) for k, v in value.items()}
