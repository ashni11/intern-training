from pydantic import BaseModel
from typing import Optional


class SignUpRequestSchema(BaseModel):
    email: str
    password: str


class SignUpResponseDataSchema(BaseModel):
    id: str
    email: str
    created_at: str
    created_by: Optional[str] = None
    updated_at: str
    updated_by: Optional[str] = None
    is_active: bool
    is_deleted: bool


class SignInRequestSchema(BaseModel):
    email: str
    password: str


class SignInResponseDataSchema(BaseModel):
    access_token: str
    token_type: str


class LogOutResponseSchema(BaseModel):
    message: str