from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from engine.database import get_db
from schema.user.user import UserCreateRequestSchema, UserResponseSchema
from service.user.user import create_user_service
router = APIRouter()
@router.get("/getform")
def get_form():
    return {
        "success": True,
        "message": "FastAPI server is running"
    }
@router.post(
    "/createform",
    response_model=UserResponseSchema,
    status_code=status.HTTP_201_CREATED
)
def create_form(user_data: UserCreateRequestSchema, db: Session = Depends(get_db)):
    try:
        return create_user_service(user_data, db)
    except HTTPException as error:
        raise error