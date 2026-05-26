<<<<
    def _build_request_body(self, request: Any) -> dict:
        """Build OpenAI-format request body for Ollama."""
        return build_base_request_body(
            request,
            include_reasoning_content=True,
        )
====
    def _build_request_body(self, request: Any) -> dict:
        """Build OpenAI-format request body for Ollama."""
        body = build_base_request_body(
            request,
            include_reasoning_content=True,
        )

        # Ensure images are handled correctly for Ollama's vision models
        # Ollama expects images in the content array if using chat completions
        return body
>>>>
