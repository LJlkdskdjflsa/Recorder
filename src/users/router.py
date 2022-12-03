import pymongo.errors
from fastapi import APIRouter, Depends
from fastapi import HTTPException, status

from src.users.schemas import UserAuth, UserOut
from src.users.service import UserService
from users.dependencies import get_current_user
from users.models import User

user_router = APIRouter()


@user_router.get("test")
async def test():
    return {"message": "user router worked"}


@user_router.post("/create", summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or Email already exists"
        )


@user_router.get('/me', summary='Get details of currently logged in user', response_model=UserOut)
async def get_me(user: User = Depends(get_current_user)):
    return user
