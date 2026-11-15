"""Minimal Ollama adapter using only the Python standard library."""

import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class OllamaProvider:
    def __init__(self, base_url: str, model: str, timeout: float = 120):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout = timeout

    def generate(self, prompt: str, *, system: str = "") -> str:
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        body = json.dumps({"model": self.model, "messages": messages, "stream": False}).encode()
        request = Request(
            f"{self.base_url}/api/chat",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urlopen(request, timeout=self.timeout) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError) as exc:
            raise RuntimeError(f"Could not reach Ollama at {self.base_url}: {exc}") from exc
        except (ValueError, KeyError) as exc:
            raise RuntimeError("Ollama returned an invalid response") from exc
        message = payload.get("message", {})
        content = message.get("content")
        if not isinstance(content, str):
            raise RuntimeError("Ollama response did not contain message.content")
        return content
