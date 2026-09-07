from uuid import UUID

from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql.expression import select

from PDF_generator.exceptions import FileNotFoundByIdException
from PDF_generator.models.db_models import DBPdfFile


class FileRepo:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_file_by_id(self, file_id: UUID):
        file = await self.db.scalar(
            select(DBPdfFile).where(DBPdfFile.id == file_id)
        )
        if file is None:
            raise FileNotFoundByIdException(f"File with id {file_id} not found")
        return file

    async def get_all_files(self):
        result = await self.db.scalars(select(DBPdfFile))
        return result.all()

    async def create_file(self, file: DBPdfFile):
        self.db.add(file)
        await self.db.flush()
        await self.db.refresh(file)
        await self.db.commit()
        return file

    async def delete_file(self, file_id: UUID):
        file = await self.db.scalar(
            select(DBPdfFile).where(DBPdfFile.id == file_id)
        )
        if file:
            await self.db.delete(file)
            await self.db.commit()
        else:
            raise FileNotFoundByIdException(f"File with id {file_id} not found")