from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.middleware.cors import CORSMiddleware

from src.categories.models import Category
from src.config import settings
from src.records.models import Record
from src.router import router
from src.tags.models import Tag
from src.templates.models import Template
from src.users.models import User

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def app_init():
    """
        initialize crucial application services
    """

    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).time_ledger

    await init_beanie(
        database=db_client,
        document_models=[User, Record, Tag, Category, Template],
    )


app.include_router(router, prefix=settings.API_V1_STR)
