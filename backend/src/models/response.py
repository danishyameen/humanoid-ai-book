from typing import List
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
import datetime

class ChatbotResponse(BaseModel):
    id: UUID = Field(default_factory=uuid4, description="Unique identifier for the chatbot response")
    query_id: UUID = Field(..., description="UUID of the corresponding UserQuery")
    answer_text: str = Field(..., min_length=1, description="The generated answer from the RAG system")
    source_references: List[str] = Field(default_factory=list, description="References to textbook content that informed the answer")
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.now, description="Timestamp of the response")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "e1f2g3h4-i5j6-7890-1234-567890abcdef",
                "query_id": "c1d2e3f4-a5b6-7890-1234-567890abcdef",
                "answer_text": "Physical AI is a branch of AI that focuses on embodied intelligence...",
                "source_references": ["Chapter 1, Section 1", "Introduction to Physical AI"],
                "timestamp": "2025-12-07T12:31:00Z"
            }
        }
