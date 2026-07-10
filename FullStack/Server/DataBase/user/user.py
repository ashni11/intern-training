from sqlalchemy.orm import Session
from model.user.user import User
from schema.user.user import UserCreateRequestSchema


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()
def create_user(db: Session, payload: UserCreateRequestSchema):
    new_user = User(
        username=payload.username,
        dob=payload.dob,
        phone_number=payload.phoneNumber
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user