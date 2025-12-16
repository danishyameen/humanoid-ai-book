import os
from typing import List
from qdrant_client.models import PointStruct, VectorStruct
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer
from backend.src.db.qdrant import get_qdrant_client
from uuid import UUID

class EmbeddingService:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.qdrant_client: QdrantClient = get_qdrant_client()
        self.collection_name = "textbook_embeddings" # Define a default collection name

    def _ensure_collection_exists(self, vector_size: int):
        """Ensures the Qdrant collection exists or creates it."""
        try:
            self.qdrant_client.get_collection(collection_name=self.collection_name)
        except Exception: # Qdrant raises an exception if collection not found
            self.qdrant_client.recreate_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
            )

    def generate_embedding(self, text: str) -> List[float]:
        """Generates an embedding for a given text."""
        embedding = self.model.encode(text).tolist()
        return embedding

    def store_embedding(self, text: str, textbook_content_id: UUID, embedding_id: UUID) -> UUID:
        """Generates an embedding and stores it in Qdrant."""
        embedding_vector = self.generate_embedding(text)
        
        self._ensure_collection_exists(vector_size=len(embedding_vector))

        point = PointStruct(
            id=str(embedding_id), # Qdrant uses string IDs
            vector=embedding_vector,
            payload={
                "textbook_content_id": str(textbook_content_id),
                "source_text_chunk": text,
                "embedding_model_info": self.model.model_name_or_path
            }
        )
        self.qdrant_client.upsert(
            collection_name=self.collection_name,
            points=[point]
        )
        return embedding_id

    def search_embeddings(self, query_text: str, top_k: int = 5) -> List[dict]:
        """Searches for similar embeddings in Qdrant."""
        query_vector = self.generate_embedding(query_text)
        search_result = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=top_k,
            query_filter=None # Optional: add filtering if needed
        )
        results = []
        for hit in search_result:
            results.append({
                "score": hit.score,
                "textbook_content_id": UUID(hit.payload["textbook_content_id"]),
                "source_text_chunk": hit.payload["source_text_chunk"],
                "id": UUID(hit.id)
            })
        return results