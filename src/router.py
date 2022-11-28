from fastapi import APIRouter

from auth.router import auth_router
from records.router import record_router
from users.router import user_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(record_router, prefix="/records", tags=["record"])
router.include_router(auth_router, prefix="/auth", tags=["auth"])
