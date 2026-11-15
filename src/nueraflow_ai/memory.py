"""Small transparent SQLite memory store; retrieval is keyword-based for v0.1."""

from pathlib import Path
import sqlite3
from typing import Iterable


class MemoryStore:
    def __init__(self, path: str):
        self.path = path
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with self._connect() as db:
            db.execute("""
                CREATE TABLE IF NOT EXISTS memories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL,
                    source TEXT NOT NULL DEFAULT 'user',
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def _connect(self):
        return sqlite3.connect(self.path)

    def add(self, content: str, source: str = "user") -> int:
        content = content.strip()
        if not content:
            raise ValueError("Memory content cannot be empty")
        with self._connect() as db:
            cursor = db.execute(
                "INSERT INTO memories(content, source) VALUES (?, ?)",
                (content, source),
            )
            return int(cursor.lastrowid)

    def search(self, query: str, limit: int = 5) -> list[dict]:
        terms = [term for term in query.split() if len(term) > 2][:8]
        if not terms:
            return []
        clauses = " OR ".join("content LIKE ?" for _ in terms)
        params: Iterable[str] = [f"%{term}%" for term in terms]
        with self._connect() as db:
            db.row_factory = sqlite3.Row
            rows = db.execute(
                f"SELECT id, content, source, created_at FROM memories WHERE {clauses} ORDER BY id DESC LIMIT ?",
                (*params, max(1, min(limit, 20))),
            ).fetchall()
        return [dict(row) for row in rows]
