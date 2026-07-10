from sqlalchemy.orm import Session
from model.auth.auth import Auth
from schema.auth.auth import SignUpRequestSchema


def create_auth_user(db: Session, payload: SignUpRequestSchema, hashed_password: str):
    new_auth_user = Auth(
        email=payload.email,
        password=hashed_password
    )
    db.add(new_auth_user)
    db.commit()
    db.refresh(new_auth_user)
    return new_auth_user

def get_auth_user_by_email(db: Session, email: str):
    return db.query(Auth).filter(Auth.email == email).first()