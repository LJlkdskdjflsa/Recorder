from beanie import PydanticObjectId

from templates.models import Template
from templates.schemas import TemplateCreate, TemplateUpdate
from users.models import User


async def get_owned_template_by_id(id: str, user: User):
    return await Template.find_one(Template.id == id, Template.owner.id == user.id, fetch_links=True)


class TemplateService:
    @staticmethod
    async def list(user: User) -> list[Template]:
        templates = await Template.find(Template.owner.id == user.id, fetch_links=True).to_list()
        return templates

    @staticmethod
    async def retrieve(user: User, id: PydanticObjectId) -> Template:
        template = await get_owned_template_by_id(id, user)
        return template

    @staticmethod
    async def create(user: User, data: TemplateCreate) -> Template:
        template = await Template(**data.dict(), owner=user).save()
        return await get_owned_template_by_id(template.id, user)

    @staticmethod
    async def update(user: User, id: PydanticObjectId, data: TemplateUpdate) -> Template:
        template = await get_owned_template_by_id(id, user)
        await template.update({"$set": data.dict(exclude_unset=True)})
        await template.save()
        template = await get_owned_template_by_id(id, user)
        return template

    @staticmethod
    async def delete(user: User, id: PydanticObjectId) -> None:
        template = await get_owned_template_by_id(id, user)
        await template.delete()
        return None
