from datetime import datetime

from beanie import PydanticObjectId
from pydantic import BaseModel, Field


class CategoryCreate(BaseModel):
    title: str = Field(..., title='Title', max_length=55, min_length=1)
    description: str = Field(..., title='Title', max_length=755, min_length=1)


class CategoryUpdate(BaseModel):
    title: str | None = Field(..., title='Title', max_length=55, min_length=1)
    description: str | None = Field(..., title='Title', max_length=755, min_length=1)


class CategoryOut(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
    title: str
    description: str
    created_at: datetime
    updated_at: datetime
