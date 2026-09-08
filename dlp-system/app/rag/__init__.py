from typing import Any

from app.core.config import settings
from app.rag.policy_retriever import PolicyRetriever

__all__ = ["PolicyRetriever", "get_policy_retriever"]


def get_policy_retriever(db: Any = None) -> Any:
    """Return the configured RAG backend for policy retrieval.

    Local TF-IDF (`PolicyRetriever`) is the default and needs no
    infrastructure. Setting `RAG_BACKEND=pgvector` and passing a live db
    session switches to the pgvector production adapter without any
    change required in callers -- both expose the same `.retrieve()`
    contract.
    """
    if getattr(settings, "RAG_BACKEND", "local") == "pgvector" and db is not None:
        from app.rag.pgvector_retriever import PgVectorPolicyRetriever

        return PgVectorPolicyRetriever(db)
    return PolicyRetriever()
