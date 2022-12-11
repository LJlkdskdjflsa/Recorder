from beanie import PydanticObjectId
from pydantic import BaseModel, Field


class TagCreate(BaseModel):
    title: str = Field(..., title='Title', max_length=55, min_length=1)


class TagOut(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
    title: str
