"""Local policy retrieval with citations for grounded remediation reports.

This implementation uses ChromaDB with local sentence-transformer embeddings.
The interface can be replaced by pgvector without changing the Reporting Agent.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import chromadb
from chromadb.utils import embedding_functions


class PolicyRetriever:
    def __init__(self, policy_dir: str | Path = "policies"):
        self.policy_dir = Path(policy_dir)

        self.embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )

        self.client = chromadb.PersistentClient(path="./chroma_data")

        self.collection = self.client.get_or_create_collection(
            name="dlp_policies",
            embedding_function=self.embedding_fn
        )

        self._index_if_needed()

    def retrieve(self, query: str, top_k: int = 3) -> list[dict[str, Any]]:
        results = self.collection.query(
            query_texts=[query],
            n_results=top_k,
        )

        if not results["ids"][0]:
            return []

        output = []
        for i in range(len(results["ids"][0])):
            output.append({
                "citation": results["ids"][0][i],
                "text": results["documents"][0][i],
                "score": round(1 - results["distances"][0][i], 4),
            })
        return output

    def _load_chunks(self) -> list[dict[str, str]]:
        chunks: list[dict[str, str]] = []
        if not self.policy_dir.exists():
            return chunks
        for path in sorted(self.policy_dir.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            sections = re.split(r"(?m)^##\s+", text)
            for index, section in enumerate(sections):
                cleaned = section.strip()
                if cleaned:
                    chunks.append(
                        {
                            "citation": f"{path.name}#section-{index + 1}",
                            "text": cleaned[:1800],
                        }
                    )
        return chunks

    def _index_if_needed(self) -> None:
        existing_count = self.collection.count()
        if existing_count > 0:
            return

        documents = self._load_chunks()
        if not documents:
            return

        self.collection.add(
            ids=[item["citation"] for item in documents],
            documents=[item["text"] for item in documents],
        )