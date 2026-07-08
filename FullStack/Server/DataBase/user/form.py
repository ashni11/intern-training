from sqlalchemy.orm import Session
from model.user.form import User
from schema.user.form import UserCreateSchema


def create_user(db: Session, payload: UserCreateSchema):
    new_user = User(
        username=payload.username,
        dob=payload.dob,
        phone_number=payload.phoneNumber
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user