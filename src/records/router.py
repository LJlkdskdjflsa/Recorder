from beanie import PydanticObjectId
from fastapi import APIRouter, Depends

from exceptions import raise_item_not_fund_exception
from records.models import Record
from records.schemas import RecordOut, RecordCreate, RecordUpdate
from records.service import RecordService
from users.dependencies import get_current_user
from users.models import User

record_router = APIRouter()


async def get_record_by_id(id: PydanticObjectId) -> Record:
    record = await Record.find_one(Record.id == id)
    if not record:
        raise_item_not_fund_exception()
    return record


@record_router.get("/", summary="Get all record of the user", response_model=list[RecordOut])
async def list(user: User = Depends(get_current_user)):
    return await RecordService.list(user)


@record_router.get("/{id}", summary="Get record of the user by id", response_model=RecordOut)
async def retrieve(id: PydanticObjectId, user: User = Depends(get_current_user)):
    return await RecordService.retrieve(user=user, id=id)


@record_router.post("/create", summary="Create Record", response_model=RecordOut)
async def create(data: RecordCreate, user: User = Depends(get_current_user)):
    return await RecordService.create(user=user, data=data)


@record_router.put("/{id}", summary="Update record by id", response_model=RecordOut)
async def update(id: PydanticObjectId, data: RecordUpdate, user: User = Depends(get_current_user)):
    return await RecordService.update(user=user, id=id, data=data)


@record_router.delete("/{id}", summary="Delete record by id")
async def delete(id: PydanticObjectId, user: User = Depends(get_current_user)):
    await RecordService.delete(user=user, id=id)
    return None
