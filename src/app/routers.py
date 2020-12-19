from fastapi import APIRouter
from src.app.users.views import fastapi_auth

api_router = APIRouter()

api_router.include_router(fastapi_auth, tags=["user"])
