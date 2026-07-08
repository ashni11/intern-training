from fastapi import APIRouter
from routes.user.form import router as form_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(form_router)