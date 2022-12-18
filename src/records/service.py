from beanie import PydanticObjectId

from records.models import Record
from records.schemas import RecordCreate, RecordUpdate
from users.models import User


async def get_owned_record_by_id(id: str, user: User):
    return await Record.find_one(Record.id == id, Record.owner.id == user.id, fetch_links=True)


class RecordService:
    @staticmethod
    async def list(user: User) -> list[Record]:
        records = await Record.find(Record.owner.id == user.id, fetch_links=True).to_list()
        return records

    @staticmethod
    async def retrieve(user: User, id: PydanticObjectId) -> Record:
        record = await get_owned_record_by_id(id, user)
        return record

    @staticmethod
    async def create(user: User, data: RecordCreate) -> Record:
        record = await Record(**data.dict(), owner=user).save()
        return await get_owned_record_by_id(record.id, user)

    @staticmethod
    async def update(user: User, id: PydanticObjectId, data: RecordUpdate) -> Record:
        record = await get_owned_record_by_id(id, user)
        await record.update({"$set": data.dict(exclude_unset=True)})
        await record.save()
        record = await get_owned_record_by_id(id, user)
        return record

    @staticmethod
    async def delete(user: User, id: PydanticObjectId) -> None:
        record = await get_owned_record_by_id(id, user)
        await record.delete()
        return None
