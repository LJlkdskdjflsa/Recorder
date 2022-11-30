from uuid import UUID

from src.templates.models import Template
from src.templates.schemas import TemplateCreate, TemplateUpdate
from src.users.models import User


async def get_owned_template_by_id(template_id: str, user: User):
    return await Template.find_one(Template.template_id == template_id, Template.owner.id == user.id)


class TemplateService:
    @staticmethod
    async def list(user: User) -> list[Template]:
        templates = await Template.find(Template.owner.id == user.id).to_list()
        return templates

    @staticmethod
    async def retrieve(user: User, id: UUID) -> Template:
        template = await get_owned_template_by_id(id, user)
        return template

    @staticmethod
    async def create(user: User, data: TemplateCreate) -> Template:
        template = Template(**data.dict(), owner=user)
        return await template.insert()

    @staticmethod
    async def update(user: User, id: UUID, data: TemplateUpdate) -> Template:
        template = await get_owned_template_by_id(id, user)
        await template.update({"$set": data.dict(exclude_unset=True)})
        await template.save()
        return template

    @staticmethod
    async def delete(user: User, id: UUID) -> None:
        template = await get_owned_template_by_id(id, user)
        await template.delete()
        return None
