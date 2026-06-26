import uuid
from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database.database import Base


class BaseModelMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    created_by = Column(String, nullable=True)

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
    updated_by = Column(String, nullable=True)

    is_active = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)


class Task(Base, BaseModelMixin):
    __tablename__ = "tasks"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    title = Column(String(100), nullable=False)
    message = Column(String, nullable=True)
    completed = Column(Boolean, default=False)