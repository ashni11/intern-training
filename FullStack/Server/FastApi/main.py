from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from DataBase.database import get_db
from DataBase.models import User
from DataBase.schemas import UserCreateSchema

app = FastAPI(title="Full Stack Practice API")
# CORS configuration for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/api/v1/getform")
def root():
    """
    Root endpoint to check if API is running.
    """
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "message": "FastAPI server is running"
        }
    )
@app.post("/api/v1/createform")
def create_user(payload: UserCreateSchema, db: Session = Depends(get_db)):
    try:
        new_user = User(
            username=payload.username,
            dob=payload.dob,
            phone_number=payload.phoneNumber
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "success": True,
                "message": "User created successfully",
                "data": {
                    "id": str(new_user.id),
                    "username": new_user.username,
                    "dob": new_user.dob,
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