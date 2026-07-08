from sqlalchemy.orm import Session
from schema.user.form import UserCreateSchema
from database.user.form import create_user


def create_user_service(payload: UserCreateSchema, db: Session):
    new_user = create_user(db, payload)
    return new_user