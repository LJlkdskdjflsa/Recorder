import logging

from beanie import Link
from beanie import PydanticObjectId
from beanie import WriteRules

from categories.models import Category
from categories.service import get_category_by_id
from src.templates.models import Template
from src.templates.schemas import TemplateCreate, TemplateUpdate
from src.users.models import User


async def get_owned_template_by_id(id: str, user: User):
    return await Template.find_one(Template.id == id, Template.owner.id == user.id)


class TemplateService:
    @staticmethod
    async def list(user: User) -> list[Template]:
        templates = await Template.find(Template.owner.id == user.id).to_list()
        return templates

    @staticmethod
    async def retrieve(user: User, id: PydanticObjectId) -> Template:
        template = await get_owned_template_by_id(id, user)
        return template

    @staticmethod
    async def create(user: User, data: TemplateCreate) -> Template:
        logging.critical('=================== TemplateCreate ===================')
        print(data.dict())
        if data.dict()['categories'] == [] or data.dict()['categories'] == None:
            logging.critical('=================== None or [] ===================')
        else:
            logging.critical('=================== value===================')
            category = (await get_category_by_id(PydanticObjectId("638df7713f4b52cf4e8974f2")))
            data.categories = [Link(ref=category, model_class=Category)]

        template = Template(**data.dict(), owner=user)
        saved_template = await template.save(link_rule=WriteRules.WRITE)
        return saved_template

    @staticmethod
    async def update(user: User, id: PydanticObjectId, data: TemplateUpdate) -> Template:
        template = await get_owned_template_by_id(id, user)
        await template.update({"$set": data.dict(exclude_unset=True)})
        await template.save()
        return template

    @staticmethod
    async def delete(user: User, id: PydanticObjectId) -> None:
        template = await get_owned_template_by_id(id, user)
        await template.delete()
        return None
