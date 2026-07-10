from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from engine.database import get_db
from schema.auth.auth import (
    SignUpRequestSchema,
    SignUpResponseDataSchema,
    SignInRequestSchema,
    SignInResponseDataSchema,
    LogOutResponseSchema,
)
from service.auth.auth import (
    signup_user_service,
    signin_user_service,
    logout_user_service,
)
router = APIRouter()
@router.post(
    "/signup",
    response_model=SignUpResponseDataSchema,
    status_code=status.HTTP_201_CREATED,
)
def signup_user(
    signup_data: SignUpRequestSchema,
    db: Session = Depends(get_db),
):
    return signup_user_service(signup_data, db)
@router.post(
    "/signin",
    response_model=SignInResponseDataSchema,
    status_code=status.HTTP_200_OK,
)
def signin_user(
    signin_data: SignInRequestSchema,
    db: Session = Depends(get_db),
):
    return signin_user_service(signin_data, db)
@router.post(
    "/logout",
    response_model=LogOutResponseSchema,
    status_code=status.HTTP_200_OK,
)
def logout_user():
    return logout_user_service()