from http.client import HTTPException


async def RecordNotFund():
    return HTTPException(status_code=404, detail="Record not found")


async def UserNotOwner():
    return HTTPException(status_code=403, detail="You don’t have permission to access this resource")
