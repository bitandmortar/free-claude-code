"""NVIDIA NIM settings (fixed values, no env config)."""

from pydantic import BaseModel, ConfigDict, Field, field_validator


class NimSettings(BaseModel):
    """Fixed NVIDIA NIM settings (not configurable via env)."""

    temperature: float = Field(1.0, ge=0.0)
    top_p: float = Field(1.0, ge=0.0, le=1.0)
    top_k: int = -1
    max_tokens: int = Field(81920, ge=1)
    presence_penalty: float = Field(0.0, ge=-2.0, le=2.0)
    frequency_penalty: float = Field(0.0, ge=-2.0, le=2.0)

    min_p: float = Field(0.0, ge=0.0, le=1.0)
    repetition_penalty: float = Field(1.0, ge=0.0)

    seed: int | None = None
    stop: str | None = None

    parallel_tool_calls: bool = True
    ignore_eos: bool = False

    min_tokens: int = Field(0, ge=0)
    chat_template: str | None = None
    request_id: str | None = None

    model_config = ConfigDict(extra="forbid")

    @field_validator("top_k")
    @classmethod
    def validate_top_k(cls, v):
        if v < -1:
            raise ValueError("top_k must be -1 or >= 0")
        return v

    @field_validator("seed", mode="before")
    @classmethod
    def parse_optional_int(cls, v):
        if v == "" or v is None:
            return None
        return int(v)

    @field_validator("stop", "chat_template", "request_id", mode="before")
    @classmethod
    def parse_optional_str(cls, v):
        if v == "":
            return None
        return v
    def to_openai_params(self) -> dict:
        """Convert to OpenAI-compatible parameters."""
        params = {
            "temperature": self.temperature,
            "top_p": self.top_p,
            "max_tokens": self.max_tokens,
            "presence_penalty": self.presence_penalty,
            "frequency_penalty": self.frequency_penalty,
            "seed": self.seed,
            "stop": self.stop,
        }

        # Add extra NIM-specific parameters to extra_body
        extra_body = {
            "top_k": self.top_k,
            "min_p": self.min_p,
            "repetition_penalty": self.repetition_penalty,
            "ignore_eos": self.ignore_eos,
            "min_tokens": self.min_tokens,
        }
        
        if self.chat_template:
            extra_body["chat_template"] = self.chat_template
            
        params["extra_body"] = extra_body
        return {k: v for k, v in params.items() if v is not None}
