from datetime import datetime

from beanie import PydanticObjectId
from pydantic import BaseModel, Field

from categories.schemas import CategoryOut
from tags.schemas import TagOut
from templates.schemas import TemplateOutMin


class RecordCreate(BaseModel):
    title: str = Field(..., title='Title', max_length=55, min_length=1)
    data: dict = Field(..., title='Data')
    template: str | None
    categories: list[str] | None
    tags: list[str] | None


class RecordUpdate(BaseModel):
    title: str | None = Field(..., title='Title', max_length=55, min_length=1)
    data: dict = Field(..., title='Data')
    template: TemplateOutMin | None
    categories: list[CategoryOut] | None
    tags: list[TagOut] | None


class RecordOut(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
    title: str
    data: dict | None
    created_at: datetime
    updated_at: datetime
    template: TemplateOutMin | None
    categories: list[CategoryOut] | None
    tags: list[TagOut] | None
