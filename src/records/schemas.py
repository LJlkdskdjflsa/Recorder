from datetime import datetime

from beanie import PydanticObjectId
from pydantic import BaseModel, Field


class RecordCreate(BaseModel):
    title: str = Field(..., title='Title', max_length=55, min_length=1)
    data: dict = Field(..., title='Data')


class RecordUpdate(BaseModel):
    title: str | None = Field(..., title='Title', max_length=55, min_length=1)
    data: dict = Field(..., title='Data')


class RecordOut(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
    title: str
    data: dict | None
    created_at: datetime
    updated_at: datetime
