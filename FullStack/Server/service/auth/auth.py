from datetime import datetime, timedelta, timezone
from jose import jwt
import bcrypt
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from engine.config import settings
from schema.auth.auth import SignUpRequestSchema, SignInRequestSchema
from database.auth.auth import create_auth_user, get_auth_user_by_email


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def signup_user_service(payload: SignUpRequestSchema, db: Session):
    existing_user = get_auth_user_by_email(db, payload.email)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    hashed_password = hash_password(payload.password)
    new_user = create_auth_user(db, payload, hashed_password)

    return new_user


def signin_user_service(payload: SignInRequestSchema, db: Session):
    user = get_auth_user_by_email(db, payload.email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not verify_password(payload.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token(data={"sub": user.email})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


def logout_user_service():
    return {"message": "Logout successful"}