from http.client import HTTPException


async def raise_item_not_fund_exception():
    return HTTPException(status_code=404, detail="Item not found")


async def raise_no_permission_exception():
    return HTTPException(status_code=403, detail="You don’t have permission to access this resource")
