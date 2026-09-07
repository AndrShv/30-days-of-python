from datetime import datetime
from uuid import uuid4

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.sqltypes import String, UUID, DateTime


class Base(DeclarativeBase):
    pass


class DBPdfFile(Base):
    __tablename__ = "pdf_files"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        nullable=False,
        as_uuid=True,
        default=uuid4
    )
    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    file_path: Mapped[str] = mapped_column(
        String(255), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )


