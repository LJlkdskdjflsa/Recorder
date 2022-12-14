from beanie import PydanticObjectId
from fastapi import APIRouter, Depends

from exceptions import raise_item_not_fund_exception
from templates.models import Template
from templates.schemas import TemplateOutFull, TemplateCreate, TemplateUpdate
from templates.service import TemplateService
from users.dependencies import get_current_user
from users.models import User

template_router = APIRouter()


async def get_template_by_id(id: PydanticObjectId) -> Template:
    template = await Template.find_one(Template.id == id)
    if not template:
        raise_item_not_fund_exception()
    return template


async def validate_ownership(
        template: Template = Depends(get_template_by_id),
) -> Template:
    return template


@template_router.get("/", summary="Get all template of the user", response_model=list[TemplateOutFull])
async def list(user: User = Depends(get_current_user)):
    return await TemplateService.list(user)


@template_router.get("/{id}", summary="Get template of the user by id", response_model=TemplateOutFull)
async def retrieve(id: PydanticObjectId, user: User = Depends(get_current_user)):
    return await TemplateService.retrieve(user=user, id=id)


@template_router.post("/create", summary="Create Template", response_model=TemplateOutFull)
async def create(data: TemplateCreate, user: User = Depends(get_current_user)):
    return await TemplateService.create(user=user, data=data)


@template_router.put("/{id}", summary="Update template by id", response_model=TemplateOutFull)
async def update(id: PydanticObjectId, data: TemplateUpdate, user: User = Depends(get_current_user)):
    return await TemplateService.update(user=user, id=id, data=data)


@template_router.delete("/{id}", summary="Delete template by id")
async def delete(id: PydanticObjectId, user: User = Depends(get_current_user)):
    await TemplateService.delete(user=user, id=id)
    return None
