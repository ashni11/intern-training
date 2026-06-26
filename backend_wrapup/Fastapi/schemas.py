from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    message: str = Field(..., min_length=5)
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    message: str = Field(..., min_length=5)
    completed: bool


class TaskResponse(BaseModel):
    id: UUID
    title: str
    message: str
    completed: bool

    created_at: datetime
    created_by: str | None = None

    updated_at: datetime
    updated_by: str | None = None

    is_active: bool
    is_deleted: bool

    class Config:
        from_attributes = True