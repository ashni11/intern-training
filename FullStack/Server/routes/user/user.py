from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from engine.database import get_db
from schema.user.user import UserCreateRequestSchema, LoginRequestSchema
from service.user.user import create_user_service, login_user_service

router = APIRouter()

@router.get("/getform")
def get_form():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "message": "FastAPI server is running"
        }
    )


@router.post("/createform")
def create_form(payload: UserCreateRequestSchema, db: Session = Depends(get_db)):
    try:
        new_user = create_user_service(payload, db)

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "success": True,
                "message": "User created successfully",
                "data": {
                    "id": str(new_user.id),
                    "username": new_user.username,
                    "dob": str(new_user.dob),
                    "phone_number": new_user.phone_number,
                    "created_at": str(new_user.created_at),
                    "created_by": new_user.created_by,
                    "updated_at": str(new_user.updated_at),
                    "updated_by": new_user.updated_by,
                    "is_active": new_user.is_active,
                    "is_deleted": new_user.is_deleted
                }
            }
        )

    except Exception as error:
        db.rollback()
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": "Failed to create user",
                "error": str(error)
            }
        )


@router.post("/login")
def login_user(payload: LoginRequestSchema, db: Session = Depends(get_db)):
    try:
        token_data = login_user_service(payload, db)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "message": "Login successful",
                "data": token_data
            }
        )

    except HTTPException as error:
        raise error

    except Exception as error:
        db.rollback()
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": "Login failed",
                "error": str(error)
            }
        )