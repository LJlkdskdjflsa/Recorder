from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class TemplateCreate(BaseModel):
    title: str = Field(..., title='Title', max_length=55, min_length=1)
    description: str = Field(..., title='Title', max_length=755, min_length=1)


class TemplateUpdate(BaseModel):
    title: str | None = Field(..., title='Title', max_length=55, min_length=1)
    description: str | None = Field(..., title='Title', max_length=755, min_length=1)


class TemplateOut(BaseModel):
    template_id: UUID
    title: str
    description: str
    created_at: datetime
    updated_at: datetime
