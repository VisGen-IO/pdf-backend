from fastapi import APIRouter
from .signup import router as signup_router
from .login import router as login_router

user_router = APIRouter(prefix='/user_auth', tags=["Auth"])

user_router.include_router(signup_router)
user_router.include_router(login_router)