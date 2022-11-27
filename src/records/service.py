from uuid import UUID

from src.records.models import Record
from src.records.schemas import RecordCreate, RecordUpdate
from src.users.models import User


async def get_owned_record_by_id(record_id: str, user: User):
    return await Record.find_one(Record.record_id == record_id, Record.owner.id == user.id)


class RecordService:
    @staticmethod
    async def list(user: User) -> list[Record]:
        records = await Record.find(Record.owner.id == user.id).to_list()
        return records

    @staticmethod
    async def retrieve(user: User, id: UUID) -> Record:
        record = await get_owned_record_by_id(id, user)
        return record

    @staticmethod
    async def create(user: User, data: RecordCreate) -> Record:
        record = Record(**data.dict(), owner=user)
        return await record.insert()

    @staticmethod
    async def update(user: User, id: UUID, data: RecordUpdate) -> Record:
        record = await get_owned_record_by_id(id, user)
        await record.update({"$set": data.dict(exclude_unset=True)})
        await record.save()
        return record

    @staticmethod
    async def delete(user: User, id: UUID) -> None:
        record = await get_owned_record_by_id(id, user)
        await record.delete()
        return None
