from pydantic import BaseModel
from typing import Optional
class UserCreateRequestSchema(BaseModel):
    username: str
    dob: str
    phoneNumber: str

class UserResponseSchema(BaseModel):
    id: str
    username: str
    dob: str
    phone_number: str
    created_at: str
    created_by: Optional[str] = None
    updated_at: str
    updated_by: Optional[str] = None
    is_active: bool
    is_deleted: bool