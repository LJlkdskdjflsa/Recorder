from fastapi import APIRouter

from auth.router import auth_router
from categories.router import category_router
from records.router import record_router
from tags.router import tag_router
from templates.router import template_router
from users.router import user_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(record_router, prefix="/records", tags=["record"])
router.include_router(tag_router, prefix="/tags", tags=["tag"])
router.include_router(template_router, prefix="/templates", tags=["template"])
router.include_router(category_router, prefix="/categories", tags=["category"])
router.include_router(auth_router, prefix="/auth", tags=["auth"])
