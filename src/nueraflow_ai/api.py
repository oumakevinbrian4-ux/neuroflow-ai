"""Small HTTP service exposing the AI core to the Nueraflow backend."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .assistant import Assistant
from .config import Settings
from .memory import MemoryStore
from .providers.ollama import OllamaProvider

settings = Settings()
assistant = Assistant(
    OllamaProvider(settings.ollama_base_url, settings.model, settings.request_timeout),
    MemoryStore(settings.memory_path),
)
app = FastAPI(title="Nueraflow AI Core", version="0.1.0")


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=20000)


class ChatResponse(BaseModel):
    response: str


@app.get("/health")
def health():
    return {"status": "ok", "service": "nueraflow-ai", "model": settings.model}


@app.post("/v1/chat", response_model=ChatResponse)
def chat(payload: ChatRequest):
    try:
        return ChatResponse(response=assistant.ask(payload.message))
    except (RuntimeError, ValueError) as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
