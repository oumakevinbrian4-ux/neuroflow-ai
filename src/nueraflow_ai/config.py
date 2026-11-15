"""Environment-based configuration with safe local defaults."""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    provider: str = os.getenv("NUERAFLOW_PROVIDER", "ollama")
    model: str = os.getenv("NUERAFLOW_MODEL", "qwen2.5-coder:7b")
    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434")
    memory_path: str = os.getenv("NUERAFLOW_MEMORY_PATH", "data/memory.sqlite3")
    request_timeout: float = float(os.getenv("NUERAFLOW_TIMEOUT", "120"))
