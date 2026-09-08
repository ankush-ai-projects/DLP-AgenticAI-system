"""Small provider-neutral client for OpenAI-compatible JSON responses."""
from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any, Protocol

from app.core.config import settings


class ModelClient(Protocol):
    def generate_json(
        self, *, system: str, user: str, tools: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]: ...


class DisabledModelClient:
    def generate_json(
        self, *, system: str, user: str, tools: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        raise RuntimeError("LLM is not configured")


class OpenAICompatibleClient:
    def __init__(self, api_key: str, base_url: str, model: str, timeout: int = 30):
        self.api_key = api_key
        self.url = f"{base_url.rstrip('/')}/chat/completions"
        self.model = model
        self.timeout = timeout

    def generate_json(
        self, *, system: str, user: str, tools: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        body_payload: dict[str, Any] = {
            "model": self.model,
            "temperature": 0,
            "response_format": {"type": "json_object"},
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        }
        if tools:
            # Real function-calling schema, passed straight through. The
            # deterministic fallback stays authoritative for execution --
            # this only lets the model reason over the same tool contracts
            # a human engineer would see.
            body_payload["tools"] = tools
        payload = json.dumps(body_payload).encode("utf-8")
        request = urllib.request.Request(
            self.url,
            data=payload,
            method="POST",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                body = json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise RuntimeError("Configured LLM request failed") from exc
        content = body["choices"][0]["message"]["content"]
        result = json.loads(content)
        if not isinstance(result, dict):
            raise ValueError("LLM JSON response must be an object")
        return result


def build_model_client() -> ModelClient:
    if settings.LLM_API_KEY and settings.LLM_MODEL:
        return OpenAICompatibleClient(
            settings.LLM_API_KEY,
            settings.LLM_BASE_URL,
            settings.LLM_MODEL,
            settings.LLM_TIMEOUT_SECONDS,
        )
    return DisabledModelClient()
