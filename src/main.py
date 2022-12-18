import logging

from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.middleware.cors import CORSMiddleware

from categories.models import Category
from config import settings
from records.models import Record
from router import router
from tags.models import Tag
from templates.models import Template
from users.models import User

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


@app.on_event('startup')
async def startup_event():
    """
        initialize crucial application services
    """
    logging.critical('=================== Application start ===================')

    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).time_ledger

    await init_beanie(
        database=db_client,
        document_models=[User, Record, Tag, Category, Template],
    )


@app.on_event('shutdown')
def shutdown_event():
    logging.critical('=================== Application shutdown ===================')


app.include_router(router, prefix=settings.API_V1_STR)
