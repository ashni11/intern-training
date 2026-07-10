from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from engine.database import get_db
from schema.auth.auth import SignUpRequestSchema, SignInRequestSchema
from service.auth.auth import (
    signup_user_service,
    signin_user_service,
    logout_user_service
)

router = APIRouter()


@router.post("/signup")
def signup_user(payload: SignUpRequestSchema, db: Session = Depends(get_db)):
    try:
        new_user = signup_user_service(payload, db)

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "success": True,
                "message": "User registered successfully",
                "data": {
                    "id": str(new_user.id),
                    "email": new_user.email,
                    "created_at": str(new_user.created_at),
                    "created_by": new_user.created_by,
                    "updated_at": str(new_user.updated_at),
                    "updated_by": new_user.updated_by,
                    "is_active": new_user.is_active,
                    "is_deleted": new_user.is_deleted
                }
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
                "message": "Failed to register user",
                "error": str(error)
            }
        )


@router.post("/signin")
def signin_user(payload: SignInRequestSchema, db: Session = Depends(get_db)):
    try:
        token_data = signin_user_service(payload, db)

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


@router.post("/logout")
def logout_user():
    try:
        response = logout_user_service()

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "message": response["message"]
            }
        )

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": "Logout failed",
                "error": str(error)
            }
        )