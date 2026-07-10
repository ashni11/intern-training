from fastapi import APIRouter
from routes.user.user import router as user_router
from routes.auth.auth import router as auth_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(user_router)
api_router.include_router(auth_router)
