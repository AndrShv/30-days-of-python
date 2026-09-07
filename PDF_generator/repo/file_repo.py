from uuid import UUID
from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from PDF_generator.models.db_models import DBPdfFile
from PDF_generator.exceptions import FileNotFoundByIdException


class FileRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, file_id: UUID) -> DBPdfFile:
        file = await self.session.scalar(
            select(DBPdfFile).where(DBPdfFile.id == file_id)
        )
        if file is None:
            raise FileNotFoundByIdException(f"File with id {file_id} not found")
        return file

    async def get_all(self) -> Sequence[DBPdfFile]:
        result = await self.session.scalars(select(DBPdfFile))
        return result.all()

    async def add(self, file: DBPdfFile) -> DBPdfFile:
        self.session.add(file)
        await self.session.flush()
        await self.session.refresh(file)
        return file

    async def delete(self, file_id: UUID) -> None:
        file = await self.get_by_id(file_id)
        await self.session.delete(file)