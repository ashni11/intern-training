from fastapi import APIRouter
from routes.form import router as form_router
api_router = APIRouter()
api_router.include_router(form_router)