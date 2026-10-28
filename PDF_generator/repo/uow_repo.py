import logging
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from PDF_generator.configs.db_config import AsyncSessionLocal
from PDF_generator.repo.file_repo import FileRepo

logger = logging.getLogger(__name__)


class AsyncSqlAlchemyUnitOfWork:
    def __init__(self, session_factory: async_sessionmaker[AsyncSession] = AsyncSessionLocal):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session: AsyncSession = self.session_factory()
        self.files = FileRepo(self.session)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        try:
            if exc_type is not None:
                logger.warning(f"Ошибка в транзакции: {exc_val}. Выполняется rollback...")
                await self.session.rollback()
            else:
                await self.session.commit()
        finally:
            await self.session.close()