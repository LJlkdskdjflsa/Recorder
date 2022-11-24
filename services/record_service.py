from uuid import UUID

from models.record_model import Record
from models.user_model import User
from schemas.record_schema import RecordCreate, RecordUpdate


class RecordService:
    @staticmethod
    async def list(user: User) -> list[Record]:
        records = await Record.find(Record.owner.id == user.id).to_list()
        return records

    @staticmethod
    async def retrieve(user: User, id: UUID) -> Record:
        record = await Record.find_one(Record.record_id == id, Record.owner.id == user.id)
        return record

    @staticmethod
    async def create(user: User, data: RecordCreate) -> Record:
        record = Record(**data.dict(), owner=user)
        return await record.insert()

    @staticmethod
    async def update(user: User, id: UUID, data: RecordUpdate) -> Record:
        record = await Record.find_one(Record.record_id == id, Record.owner.id == user.id)
        await record.update({"$set": data.dict(exclude_unset=True)})
        await record.save()
        return record

    @staticmethod
    async def delete(user: User, id: UUID) -> None:
        record = await Record.find_one(Record.record_id == id, Record.owner.id == user.id)
        await record.delete()
        return None
