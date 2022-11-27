from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="user email")
    username: str = Field(..., min_length=5, max_length=50, description="user name")
    password: str = Field(..., min_length=5, max_length=24, description="user password")


class UserOut(BaseModel):
    user_id: UUID
    username: str


class UserUpdate(BaseModel):
    username: str
