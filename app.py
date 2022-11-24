from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from api.v1.router import router
from core.config import settings
from models.record_model import Record
from models.user_model import User

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


@app.on_event("startup")
async def app_init():
    """
        initialize crucial application services
    """

    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).time_ledger

    await init_beanie(
        database=db_client,
        document_models=[User, Record],
    )


app.include_router(router, prefix=settings.API_V1_STR)
