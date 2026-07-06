from pydantic import BaseModel, Field
class UserCreateSchema(BaseModel):
    username: str = Field(..., min_length=1, max_length=100)
    dob: str
    phoneNumber: str = Field(..., min_length=10, max_length=15)
    
class UserResponseSchema(BaseModel):
    id: str
    username: str
    dob: str
    phone_number: str
    created_at: str | None = None
    created_by: str | None = None
    updated_at: str | None = None
    updated_by: str | None = None
    is_active: bool
    is_deleted: bool

    class Config:
        from_attributes = True