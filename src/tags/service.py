from uuid import UUID

from src.tags.models import Tag
from src.tags.schemas import TagCreate


async def get_tag_by_id(tag_id) -> Tag:
    return await Tag.find_one(Tag.tag_id == tag_id)


class TagService:
    @staticmethod
    async def list() -> list[Tag]:
        tags = await Tag.find().to_list()
        return tags

    @staticmethod
    async def retrieve(id: UUID) -> Tag:
        tag = await get_tag_by_id(id)
        print(tag)
        return tag

    @staticmethod
    async def delete(id: UUID) -> None:
        tag = await get_tag_by_id(id)
        await tag.delete()
        return None

    @staticmethod
    async def create(data: TagCreate) -> Tag:
        tag = Tag(**data.dict())
        return await tag.insert()
