"""Provider interface; implementations must return plain assistant text."""

from typing import Protocol


class ChatProvider(Protocol):
    def generate(self, prompt: str, *, system: str = "") -> str:
        """Generate a response to prompt."""
