from uuid import UUID

from fastapi import APIRouter, Depends

from src.records.exceptions import RecordNotFund
from src.records.models import Record
from src.records.schemas import RecordOut, RecordCreate, RecordUpdate
from src.records.service import RecordService
from src.users.dependencies import get_current_user
from src.users.models import User

record_router = APIRouter()


async def get_record_by_id(record_id: UUID) -> Record:
    record = await Record.find_one(Record.record_id == record_id)
    if not record:
        raise await RecordNotFund()
    return record


async def validate_ownership(
        record: Record = Depends(get_record_by_id),
        user: User = Depends(get_current_user),
) -> Record:
    # if record.owner.id != user.user_id:
    #     raise UserNotOwner()
    print(record.owner)
    owner = record.owner
    return record


@record_router.get("/", summary="Get all record of the user", response_model=list[RecordOut])
async def list(user: User = Depends(get_current_user)):
    return await RecordService.list(user)


# @record_router.get("/one/", summary="Get record of the user by id", response_model=RecordOut)
# async def retrieve(record: Record = Depends(validate_ownership)):
#     return await RecordService.update(user=user, id=id, data=data)
@record_router.get("/{id}", summary="Get record of the user by id", response_model=RecordOut)
async def retrieve(id: UUID, user: User = Depends(get_current_user)):
    return await RecordService.retrieve(user=user, id=id)


@record_router.post("/create", summary="Create Record", response_model=RecordOut)
async def create(data: RecordCreate, user: User = Depends(get_current_user)):
    return await RecordService.create(user=user, data=data)


@record_router.put("/{id}", summary="Update record by id", response_model=RecordOut)
async def update(id: UUID, data: RecordUpdate, user: User = Depends(get_current_user)):
    return await RecordService.update(user=user, id=id, data=data)


@record_router.delete("/{id}", summary="Delete record by id")
async def update(id: UUID, user: User = Depends(get_current_user)):
    await RecordService.delete(user=user, id=id)
    return None
