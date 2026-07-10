from sqlalchemy.orm import Session
from database.user.user import create_user
from schema.user.user import UserCreateRequestSchema


def create_user_service(payload: UserCreateRequestSchema, db: Session):
    new_user = create_user(db, payload)
    return new_user