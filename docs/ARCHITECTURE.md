# Nueraflow architecture (first milestone)

```text
User / Web UI
     |
     v
Nueraflow Backend API  ---- Auth, sessions, jobs, audit
     |
     v
AI Core / Orchestrator ---- Provider interface
     |                         |-- Ollama (local)
     |                         |-- future hosted providers
     |
     +---- Memory & Knowledge -- SQLite now; PostgreSQL/vector retrieval later
     |
     +---- Coding Agent -------- proposal/review now; isolated runner later
     |
     +---- Neuromorphic Lab ---- optional SNN experiments (not production inference)
```

## Learning loop

1. Ingest a source only through a permitted API, user-provided file, or allowed export.
2. Record provenance, license/usage constraints, and retrieval metadata.
3. Retrieve relevant passages when a task arrives.
4. Ask a selected model to reason over the context.
5. Capture user feedback and evaluate the result.
6. Improve retrieval/routing rules based on measured outcomes.

This is retrieval and system improvement, not automatic training of provider model weights.

## Next engineering increments

- Add OpenAI-compatible and hosted provider adapters with secrets supplied at runtime.
- Move durable shared memory to PostgreSQL; use Redis for queues/cache, not as the system of record.
- Add document parsers, GitHub ingestion, and caption import with source provenance.
- Add eval datasets and regression tests before changing routing/prompt policies.
- Implement code execution only in disposable containers with resource limits, no host mounts by default, and explicit network policy.
- Prototype spiking neural networks behind an optional interface and compare them against conventional baselines.
