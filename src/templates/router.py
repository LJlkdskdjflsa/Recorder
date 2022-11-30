from uuid import UUID

from fastapi import APIRouter, Depends

from src.templates.models import Template
from src.templates.schemas import TemplateOut, TemplateCreate, TemplateUpdate
from src.templates.service import TemplateService
from src.users.dependencies import get_current_user
from src.users.models import User

template_router = APIRouter()


async def get_template_by_id(template_id: UUID) -> Template:
    template = await Template.find_one(Template.template_id == template_id)
    if not template:
        raise await ItemNotFund()
    return template


async def validate_ownership(
        template: Template = Depends(get_template_by_id),
) -> Template:
    return template


@template_router.get("/", summary="Get all template of the user", response_model=list[TemplateOut])
async def list(user: User = Depends(get_current_user)):
    return await TemplateService.list(user)


@template_router.get("/{id}", summary="Get template of the user by id", response_model=TemplateOut)
async def retrieve(id: UUID, user: User = Depends(get_current_user)):
    return await TemplateService.retrieve(user=user, id=id)


@template_router.post("/create", summary="Create Template", response_model=TemplateOut)
async def create(data: TemplateCreate, user: User = Depends(get_current_user)):
    return await TemplateService.create(user=user, data=data)


@template_router.put("/{id}", summary="Update template by id", response_model=TemplateOut)
async def update(id: UUID, data: TemplateUpdate, user: User = Depends(get_current_user)):
    return await TemplateService.update(user=user, id=id, data=data)


@template_router.delete("/{id}", summary="Delete template by id")
async def delete(id: UUID, user: User = Depends(get_current_user)):
    await TemplateService.delete(user=user, id=id)
    return None
