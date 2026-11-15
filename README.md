# Nueraflow AI Core

The Python intelligence layer for **Nueraflow**, Nueraqon Technologies' personal AI development workstation.

## First milestone

- Provider-neutral chat orchestration.
- Local Ollama support through its HTTP API.
- SQLite-backed notes and retrieval for a small, inspectable memory store.
- Explicit research-source records (URLs and notes; no unrestricted scraping).
- A safe coding-agent boundary: this milestone proposes code and plans; it does **not** execute arbitrary generated commands.
- An isolated neuromorphic research package placeholder for later SNN experiments.

## Quick start

Requires Python 3.11+.

```bash
cd neuroflow-ai
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
ollama serve
ollama pull qwen2.5-coder:7b
NUERAFLOW_MODEL=qwen2.5-coder:7b python -m nueraflow_ai
```

Set `OLLAMA_BASE_URL` if Ollama is not running at `http://localhost:11434`.

## Design principles

1. **Hybrid, learning-first:** use existing local/API models first; do not train a foundation model from scratch.
2. **Retrieval is not model training:** saved sources and feedback improve context and evaluation, not the model's weights.
3. **Provider independence:** model access sits behind a small interface.
4. **Safety:** generated code is untrusted. Execution must later happen in a disposable sandbox with explicit permissions.
5. **Neuromorphic work is experimental:** SNN experiments stay optional and separate from the dependable assistant path.

## Tests

```bash
pip install -e ".[dev]"
pytest
```

See `docs/ARCHITECTURE.md` for the system boundaries.
