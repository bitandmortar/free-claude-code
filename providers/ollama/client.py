"""Ollama provider implementation."""

from typing import Any
from providers.base import ProviderConfig
from providers.openai_compat import OpenAICompatibleProvider
from providers.common.message_converter import build_base_request_body

class OllamaProvider(OpenAICompatibleProvider):
    """Ollama provider using OpenAI-compatible chat completions."""

    def __init__(self, config: ProviderConfig):
        super().__init__(
            config,
            provider_name="OLLAMA",
            base_url=config.base_url,
            api_key="ollama", # Ollama doesn't require an API key by default
        )

    def _build_request_body(self, request: Any) -> dict:
        """Build OpenAI-format request body for Ollama."""
        return build_base_request_body(
            request,
            include_reasoning_content=True,
        )
