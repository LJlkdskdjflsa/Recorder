from uuid import UUID

from fastapi import APIRouter, Depends

from exceptions import ItemNotFund
from src.categories.models import Category
from src.categories.schemas import CategoryOut, CategoryCreate, CategoryUpdate
from src.categories.service import CategoryService
from src.users.dependencies import get_current_user
from src.users.models import User

category_router = APIRouter()


async def get_category_by_id(category_id: UUID) -> Category:
    category = await Category.find_one(Category.category_id == category_id)
    if not category:
        raise await ItemNotFund()
    return category


async def validate_ownership(
        category: Category = Depends(get_category_by_id),
) -> Category:
    print(category.owner)
    return category


@category_router.get("/", summary="Get all category of the user", response_model=list[CategoryOut])
async def list(user: User = Depends(get_current_user)):
    return await CategoryService.list(user)


@category_router.get("/{id}", summary="Get category of the user by id", response_model=CategoryOut)
async def retrieve(id: UUID, user: User = Depends(get_current_user)):
    return await CategoryService.retrieve(user=user, id=id)


@category_router.post("/create", summary="Create Category", response_model=CategoryOut)
async def create(data: CategoryCreate, user: User = Depends(get_current_user)):
    return await CategoryService.create(user=user, data=data)


@category_router.put("/{id}", summary="Update category by id", response_model=CategoryOut)
async def update(id: UUID, data: CategoryUpdate, user: User = Depends(get_current_user)):
    return await CategoryService.update(user=user, id=id, data=data)


@category_router.delete("/{id}", summary="Delete category by id")
async def delete(id: UUID, user: User = Depends(get_current_user)):
    await CategoryService.delete(user=user, id=id)
    return None
