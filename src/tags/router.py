from beanie import PydanticObjectId
from fastapi import APIRouter

from src.tags.schemas import TagOut, TagCreate
from src.tags.service import TagService

tag_router = APIRouter()


@tag_router.get("/", summary="Get all tags", response_model=list[TagOut])
async def list():
    return await TagService.list()


@tag_router.get("/{id}", summary="Get tag by id", response_model=TagOut | None)
async def retrieve(id: PydanticObjectId):
    return await TagService.retrieve(id=id)


@tag_router.post("/create", summary="Create Tag", response_model=TagOut)
async def create(data: TagCreate):
    return await TagService.create(data=data)


@tag_router.delete("/{id}", summary="Delete tag by id")
async def delete(id: PydanticObjectId):
    await TagService.delete(id=id)
    return None
