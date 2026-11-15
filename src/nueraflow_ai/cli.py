"""Interactive local CLI."""

from .assistant import Assistant
from .config import Settings
from .memory import MemoryStore
from .providers.ollama import OllamaProvider


def main() -> None:
    settings = Settings()
    assistant = Assistant(
        OllamaProvider(settings.ollama_base_url, settings.model, settings.request_timeout),
        MemoryStore(settings.memory_path),
    )
    print(f"Nueraflow ready — provider={settings.provider}, model={settings.model}")
    print("Type /quit to exit or /remember <note> to save a note.")
    while True:
        try:
            prompt = input("\nYou> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break
        if prompt in {"/quit", "/exit"}:
            break
        if prompt.startswith("/remember "):
            print(f"Saved memory #{assistant.memory.add(prompt[10:])}")
            continue
        if not prompt:
            continue
        try:
            print("\nNueraflow> " + assistant.ask(prompt))
        except Exception as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
