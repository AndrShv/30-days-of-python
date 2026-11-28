from typing import Optional, Any, Sequence
from sqlalchemy import UUID, select
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import selectinload

from EventAnalyticsEngine.db_models import DBUser, DBLog


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user: DBUser) -> DBUser:
        self.db.add(user)
        return user


    async def get_user_by_id(self, user_id: UUID) -> Optional[DBUser]:
        result = await self.db.scalars(select(DBUser).where(DBUser.id == user_id))
        return result.first()


    async def get_all_with_logs(self) -> Sequence[DBUser]:
        stmt = select(DBUser).options(selectinload(DBUser.logs))
        result = await self.db.scalars(stmt)
        return result.unique().all()


class LogRepository:
    def __init__(self, db: AsyncSession):
        self.db = db


    async def create_log(self, log: DBLog) -> DBLog:
        self.db.add(log)
        print(f"Log {log.id} created")
        return log


    async def get_log_by_id(self, log_id: UUID) -> Optional[DBLog]:
        result = await self.db.scalars(select(DBLog).where(DBLog.id == log_id))
        return result.first()

    async def get_all_logs_by_user_id(self, user_id: UUID) -> Sequence[Any]:
        result = await self.db.scalars(select(DBLog).where(DBLog.user_id == user_id))
        return result.unique().all()