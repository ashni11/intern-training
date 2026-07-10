from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime
class UserCreateRequestSchema(BaseModel):
    username: str
    dob: str
    phoneNumber: str
class UserResponseSchema(BaseModel):
    id: UUID
    username: str
    dob: str
    phone_number: str
    created_at: datetime
    created_by: Optional[str] = None
    updated_at: datetime
    updated_by: Optional[str] = None
    is_active: bool
    is_deleted: bool

    model_config = ConfigDict(from_attributes=True)