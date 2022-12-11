from beanie import PydanticObjectId

from src.tags.models import Tag
from src.tags.schemas import TagCreate


async def get_tag_by_id(id) -> Tag:
    return await Tag.find_one(Tag.id == id)


class TagService:
    @staticmethod
    async def list() -> list[Tag]:
        tags = await Tag.find().to_list()
        return tags

    @staticmethod
    async def retrieve(id: PydanticObjectId) -> Tag:
        tag = await get_tag_by_id(id)
        print(tag)
        return tag

    @staticmethod
    async def delete(id: PydanticObjectId) -> None:
        tag = await get_tag_by_id(id)
        await tag.delete()
        return None

    @staticmethod
    async def create(data: TagCreate) -> Tag:
        tag = Tag(**data.dict())
        return await tag.insert()
