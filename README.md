# Nueraflow AI Core

The Python intelligence layer for **Nueraflow**, Nueraqon Technologies' personal AI development workstation.

## First milestone

- Provider-neutral chat orchestration and local Ollama support.
- SQLite-backed notes and keyword retrieval.
- Explicit research-source records; no unrestricted scraping.
- Coding proposals without arbitrary code execution.
- An optional neuromorphic research area.
- FastAPI service for the Nueraflow backend.

## Quick start

Requires Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev,api]"
ollama serve
ollama pull qwen2.5-coder:7b
NUERAFLOW_MODEL=qwen2.5-coder:7b python -m nueraflow_ai
```

Run the HTTP service: `uvicorn nueraflow_ai.api:app --host 127.0.0.1 --port 8100`.

Set `OLLAMA_BASE_URL` if Ollama is not running at `http://127.0.0.1:11434`.

## Design principles

1. Hybrid and learning-first: use existing local/API models; do not train a foundation model from scratch.
2. Retrieval is not model training: saved sources and feedback improve context and evaluation, not model weights.
3. Provider independence: model access sits behind a small interface.
4. Generated code is untrusted; execution requires a disposable sandbox and explicit permissions.
5. Neuromorphic work remains experimental and separate from the dependable assistant path.

See `docs/ARCHITECTURE.md` for system boundaries.
