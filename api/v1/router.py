from fastapi import APIRouter

from api.auth.jwt import auth_router
from api.v1.handlers import user, record

router = APIRouter()

router.include_router(user.user_router, prefix="/users", tags=["users"])
router.include_router(record.record_router, prefix="/record", tags=["record"])
router.include_router(auth_router, prefix="/auth", tags=["auth"])
