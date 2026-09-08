"""Local policy retrieval with citations for grounded remediation reports.

This local TF-IDF implementation keeps the demo self-contained. The interface
can be replaced by pgvector without changing the Reporting Agent.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any


class PolicyRetriever:
    def __init__(self, policy_dir: str | Path = "policies"):
        self.policy_dir = Path(policy_dir)

    def retrieve(self, query: str, top_k: int = 3) -> list[dict[str, Any]]:
        documents = self._load_chunks()
        if not documents:
            return []
        try:
            from sklearn.feature_extraction.text import TfidfVectorizer
            from sklearn.metrics.pairwise import cosine_similarity

            vectorizer = TfidfVectorizer(stop_words="english")
            matrix = vectorizer.fit_transform([item["text"] for item in documents] + [query])
            scores = cosine_similarity(matrix[-1], matrix[:-1]).ravel()
            indices = scores.argsort()[::-1][:top_k]
            return [
                {**documents[index], "score": round(float(scores[index]), 4)}
                for index in indices if scores[index] > 0
            ]
        except ImportError:
            terms = set(re.findall(r"[a-z0-9]+", query.lower()))
            ranked = []
            for item in documents:
                words = set(re.findall(r"[a-z0-9]+", item["text"].lower()))
                ranked.append((len(terms & words), item))
            return [{**item, "score": score} for score, item in sorted(ranked, reverse=True)[:top_k] if score]

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
