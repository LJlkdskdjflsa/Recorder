from beanie import PydanticObjectId
from pydantic import BaseModel


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    sub: PydanticObjectId | None = None
    exp: int | None = None
