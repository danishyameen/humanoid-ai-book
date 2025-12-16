from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, conint, Json
import datetime

class TextbookContent(BaseModel):
    id: UUID = Field(default_factory=uuid4, description="Unique identifier for the content section")
    chapter_number: conint(ge=1, le=6) = Field(..., description="Main chapter number (1-6)")
    section_id: str = Field(..., min_length=1, description="Unique slug for the section")
    title: str = Field(..., min_length=1, description="Human-readable title of the section")
    markdown_content: str = Field(..., min_length=1, description="Raw Markdown text for the section")
    metadata: Json[dict] = Field(default_factory=dict, description="JSONB metadata (author, tags, dates, etc.)")
    version: str = Field("1.0.0", description="Version of the content")
    parent_section_id: Optional[str] = Field(None, description="Parent section ID for hierarchical content")
    urdu_translation_id: Optional[UUID] = Field(None, description="UUID of the corresponding Urdu translation content")
    embedding_ids: List[UUID] = Field(default_factory=list, description="List of UUIDs for associated embeddings")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "chapter_number": 1,
                "section_id": "introduction-to-physical-ai",
                "title": "Introduction to Physical AI",
                "markdown_content": "# Introduction\nThis is the introduction to Physical AI.",
                "metadata": {"author": "AI-Native", "tags": ["AI", "Physical AI"], "created_at": "2025-12-07T12:00:00Z"},
                "version": "1.0.0",
                "parent_section_id": None,
                "urdu_translation_id": None,
                "embedding_ids": ["f1e2d3c4-b5a6-7890-1234-567890abcdef"]
            }
        }
