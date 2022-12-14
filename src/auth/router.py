from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from pydantic import ValidationError

from auth.service import create_access_token, create_refresh_token
from auth.schemas import TokenSchema, TokenPayload
from config import settings
from users.dependencies import get_current_user
from users.models import User
from users.schemas import UserOut
from users.service import UserService

auth_router = APIRouter()


@auth_router.post("/login", summary="Create access and refresh token for user", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = await UserService.authenticate(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")
    return {"access_token": create_access_token(user.id), "refresh_token": create_refresh_token(user.id)}


@auth_router.post("/test-token", summary="Test if the access token is valid", response_model=UserOut)
async def test_token(user: User = Depends(get_current_user)):
    return user


@auth_router.post("/refresh", summary="Refresh Token", response_model=TokenSchema)
async def refresh_token(refresh_token: str = Body()):
    try:
        payload = jwt.decode(
            refresh_token,
            settings.JWT_REFRESH_SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        token_data = TokenPayload(**payload)

    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"}
        )
    user = await UserService.get_user_by_id(token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid token for user",
        )
    return {"access_token": create_access_token(user.id), "refresh_token": create_refresh_token(user.id)}
