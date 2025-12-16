from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
import datetime

class UserQuery(BaseModel):
    id: UUID = Field(default_factory=uuid4, description="Unique identifier for the user query")
    text: str = Field(..., min_length=1, description="The user's natural language question")
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.now, description="Timestamp of the query")
    context_text: Optional[str] = Field(None, description="Optional text selected by the user to provide additional context")
    session_id: Optional[UUID] = Field(None, description="Optional session ID to link queries for conversational context")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "c1d2e3f4-a5b6-7890-1234-567890abcdef",
                "text": "What is physical AI?",
                "timestamp": "2025-12-07T12:30:00Z",
                "context_text": "Physical AI refers to...",
                "session_id": "s1e2s3s4-i5d6-7890-1234-567890abcdef"
            }
        }
