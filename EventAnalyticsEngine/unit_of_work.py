from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from EventAnalyticsEngine.repository import UserRepository, LogRepository


class UnitOfWork:
    users: UserRepository
    logs: LogRepository

    def __init__(self, session_factory: async_sessionmaker[AsyncSession]):
        self.session_factory = session_factory

    async def __aenter__(self) -> "UnitOfWork":
        self.session: AsyncSession = self.session_factory()
        self.users = UserRepository(self.session)
        self.logs = LogRepository(self.session)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.session.rollback()
        else:
            await self.session.commit()
        await self.session.close()