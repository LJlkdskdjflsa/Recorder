from datetime import datetime

from beanie import PydanticObjectId
from pydantic import BaseModel, Field

from categories.models import Category
from tags.models import Tag
from templates.models import Template


class RecordCreate(BaseModel):
    title: str = Field(..., title='Title', max_length=55, min_length=1)
    data: dict = Field(..., title='Data')
    template: Template | None
    categories: list[Category] | None
    tags: list[Tag] | None


class RecordUpdate(BaseModel):
    title: str | None = Field(..., title='Title', max_length=55, min_length=1)
    data: dict = Field(..., title='Data')
    template: Template | None
    categories: list[Category] | None
    tags: list[Tag] | None


class RecordOut(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
    title: str
    data: dict | None
    created_at: datetime
    updated_at: datetime
    template: Template | None
    categories: list[Category] | None
    tags: list[Tag] | None
