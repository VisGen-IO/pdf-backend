from fastapi import APIRouter
from .theme import router as theme_router

user_router = APIRouter(prefix='/theme', tags=["Theme"])

user_router.include_router(theme_router)