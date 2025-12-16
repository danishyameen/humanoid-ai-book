from typing import List
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, conlist

class Embedding(BaseModel):
    id: UUID = Field(default_factory=uuid4, description="Unique identifier for the embedding")
    vector: conlist(float, min_length=1) = Field(..., description="High-dimensional vector embedding")
    source_text_chunk: str = Field(..., min_length=1, description="Exact text segment from which the embedding was generated")
    textbook_content_id: UUID = Field(..., description="UUID of the original TextbookContent section")
    embedding_model_info: str = Field(..., min_length=1, description="Model used for generating the embedding (e.g., 'all-MiniLM-L6-v2')")
    chunk_order: int = Field(0, description="Order of this chunk within its parent TextbookContent")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "f1e2d3c4-b5a6-7890-1234-567890abcdef",
                "vector": [0.1, 0.2, 0.3, ...], # Placeholder for actual vector values
                "source_text_chunk": "This is a sentence from the textbook about AI.",
                "textbook_content_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "embedding_model_info": "all-MiniLM-L6-v2",
                "chunk_order": 0
            }
        }
