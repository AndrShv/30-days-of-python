import uuid
from datetime import datetime
from typing import Dict, Any, List
from sqlalchemy import String, Integer, JSON, func, ForeignKey, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
AsyncSession = AsyncSession

class Base(DeclarativeBase):
    pass


class DBUser(Base):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        server_default=func.gen_random_uuid()
    )
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    logs: Mapped[List["DBLog"]] = relationship(back_populates="user")


class DBLog(Base):
    __tablename__ = "logs"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid()
    )
    event_id: Mapped[int] = mapped_column(Integer, nullable=False)
    payload: Mapped[str] = mapped_column(String(255), nullable=False)
    log_metadata: Mapped[Dict[str, Any]] = mapped_column(JSON, nullable=True)

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    user: Mapped["DBUser"] = relationship(back_populates="logs")
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id"), nullable=False
    )




