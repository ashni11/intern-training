from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from database.user.user import create_user, get_user_by_username
from schema.user.user import UserCreateRequestSchema

def create_user_service(payload: UserCreateRequestSchema, db: Session):
    existing_user = get_user_by_username(db, payload.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )
    new_user = create_user(db, payload)
    return new_user