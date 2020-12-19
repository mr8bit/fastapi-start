from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.config.settings import APPS_MODELS, DATABASE_URI
from src.config import settings
from starlette.middleware.sessions import SessionMiddleware
from tortoise.contrib.fastapi import register_tortoise
from src.app import routers

app = FastAPI(title="FastApi Start Template",
              description="Author - mr8bit",
              version="0.0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)
app.include_router(routers.api_router, prefix=settings.API_V1_STR)

register_tortoise(
    app,
    db_url=DATABASE_URI,
    modules={"models": APPS_MODELS},
    add_exception_handlers=True,
)
