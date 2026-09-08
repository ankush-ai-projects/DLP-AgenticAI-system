"""Production RAG adapter: pgvector-backed policy retrieval.

Same `.retrieve()` contract as PolicyRetriever (TF-IDF/local demo version),
so the Reporting Agent never needs to know which backend is active. This
adapter embeds policy chunks once (on `sync()`), stores them in a Postgres
table with a `vector` column, and retrieves by cosine distance at query
time -- the standard pattern for moving a local RAG demo to production
without touching the calling code.

Requires `pgvector` installed as a Postgres extension and the `pgvector`
Python package. Falls back with a clear error if either is missing so the
caller can catch it and use PolicyRetriever instead.
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any

from sqlalchemy import Column, Integer, String, Text, text
from sqlalchemy.orm import Session

from app.models.base import Base


class PolicyChunkEmbedding(Base):
    __tablename__ = "policy_chunk_embeddings"

    id = Column(Integer, primary_key=True)
    citation = Column(String(255), nullable=False, unique=True)
    text = Column(Text, nullable=False)
    content_hash = Column(String(64), nullable=False)
    # embedding column is added via raw SQL in ensure_schema() because the
    # `vector(N)` type is only valid once the pgvector extension exists.


class Embedder:
    """Minimal interface any embedding provider must satisfy."""

    dimensions: int

    def embed(self, texts: list[str]) -> list[list[float]]:
        raise NotImplementedError


class HashingEmbedder(Embedder):
    """Deterministic, dependency-free embedder for local/dev/testing.

    Swap this for a real embeddings API (OpenAI, Cohere, local sentence-
    transformers, etc.) in production -- the retriever only depends on the
    `Embedder` interface above, not on this implementation.
    """

    def __init__(self, dimensions: int = 256):
        self.dimensions = dimensions

    def embed(self, texts: list[str]) -> list[list[float]]:
        vectors = []
        for item in texts:
            vector = [0.0] * self.dimensions
            for token in re.findall(r"[a-z0-9]+", item.lower()):
                index = int(hashlib.sha256(token.encode()).hexdigest(), 16) % self.dimensions
                vector[index] += 1.0
            norm = sum(v * v for v in vector) ** 0.5 or 1.0
            vectors.append([v / norm for v in vector])
        return vectors


class PgVectorPolicyRetriever:
    def __init__(self, db: Session, embedder: Embedder | None = None, policy_dir: str | Path = "policies"):
        self.db = db
        self.embedder = embedder or HashingEmbedder()
        self.policy_dir = Path(policy_dir)

    def ensure_schema(self) -> None:
        self.db.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        self.db.execute(text(f"""
            ALTER TABLE policy_chunk_embeddings
            ADD COLUMN IF NOT EXISTS embedding vector({self.embedder.dimensions})
        """))
        self.db.commit()

    def sync(self) -> int:
        """Embed and upsert every policy chunk. Returns chunk count synced."""
        chunks = self._load_chunks()
        if not chunks:
            return 0
        vectors = self.embedder.embed([c["text"] for c in chunks])
        for chunk, vector in zip(chunks, vectors):
            content_hash = hashlib.sha256(chunk["text"].encode()).hexdigest()
            self.db.execute(
                text("""
                    INSERT INTO policy_chunk_embeddings (citation, text, content_hash, embedding)
                    VALUES (:citation, :text, :content_hash, :embedding)
                    ON CONFLICT (citation) DO UPDATE
                    SET text = EXCLUDED.text,
                        content_hash = EXCLUDED.content_hash,
                        embedding = EXCLUDED.embedding
                """),
                {
                    "citation": chunk["citation"],
                    "text": chunk["text"],
                    "content_hash": content_hash,
                    "embedding": str(vector),
                },
            )
        self.db.commit()
        return len(chunks)

    def retrieve(self, query: str, top_k: int = 3) -> list[dict[str, Any]]:
        query_vector = self.embedder.embed([query])[0]
        rows = self.db.execute(
            text("""
                SELECT citation, text, 1 - (embedding <=> :query_vector) AS score
                FROM policy_chunk_embeddings
                ORDER BY embedding <=> :query_vector
                LIMIT :top_k
            """),
            {"query_vector": str(query_vector), "top_k": top_k},
        ).fetchall()
        return [
            {"citation": row.citation, "text": row.text, "score": round(float(row.score), 4)}
            for row in rows
        ]

    def _load_chunks(self) -> list[dict[str, str]]:
        chunks: list[dict[str, str]] = []
        if not self.policy_dir.exists():
            return chunks
        for path in sorted(self.policy_dir.glob("*.md")):
            text_content = path.read_text(encoding="utf-8")
            sections = re.split(r"(?m)^##\s+", text_content)
            for index, section in enumerate(sections):
                cleaned = section.strip()
                if cleaned:
                    chunks.append(
                        {"citation": f"{path.name}#section-{index + 1}", "text": cleaned[:1800]}
                    )
        return chunks
