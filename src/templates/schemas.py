from datetime import datetime

from beanie import PydanticObjectId
from pydantic import BaseModel, Field


class TemplateCreate(BaseModel):
    title: str = Field(..., title='Title', max_length=55, min_length=1)
    description: str = Field(..., title='Title', max_length=755, min_length=1)
    json_schema: dict = Field(..., title='JSON schema')
    ui_schema: dict = Field(..., title='UI schema')


class TemplateUpdate(BaseModel):
    title: str | None = Field(..., title='Title', max_length=55, min_length=1)
    description: str | None = Field(..., title='Title', max_length=755, min_length=1)
    json_schema: dict = Field(..., title='JSON schema')
    ui_schema: dict = Field(..., title='UI schema')


class TemplateOut(BaseModel):
    id: PydanticObjectId = Field(alias="_id")

    title: str
    description: str | None
    json_schema: dict | None
    ui_schema: dict | None
    created_at: datetime
    updated_at: datetime
