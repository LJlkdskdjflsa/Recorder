from uuid import UUID

from src.categories.models import Category
from src.categories.schemas import CategoryCreate, CategoryUpdate
from src.users.models import User


async def get_owned_category_by_id(category_id: str, user: User):
    return await Category.find_one(Category.category_id == category_id, Category.owner.id == user.id)


class CategoryService:
    @staticmethod
    async def list(user: User) -> list[Category]:
        categories = await Category.find(Category.owner.id == user.id).to_list()
        return categories

    @staticmethod
    async def retrieve(user: User, id: UUID) -> Category:
        category = await get_owned_category_by_id(id, user)
        return category

    @staticmethod
    async def create(user: User, data: CategoryCreate) -> Category:
        category = Category(**data.dict(), owner=user)
        return await category.insert()

    @staticmethod
    async def update(user: User, id: UUID, data: CategoryUpdate) -> Category:
        category = await get_owned_category_by_id(id, user)
        await category.update({"$set": data.dict(exclude_unset=True)})
        await category.save()
        return category

    @staticmethod
    async def delete(user: User, id: UUID) -> None:
        category = await get_owned_category_by_id(id, user)
        await category.delete()
        return None
