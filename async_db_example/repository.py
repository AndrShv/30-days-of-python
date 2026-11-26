from __future__ import annotations

from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from async_db_example.models import User


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, user_id: int) -> User | None:
        """Получить пользователя по ID."""
        result = await self.session.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> User | None:
        """Получить пользователя по Email."""
        result = await self.session.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def create(self, username: str, email: str) -> User:
        user = User(username=username, email=email)
        self.session.add(user)
        await self.session.flush()
        return user

    async def get_all(self, limit: int = 100, offset: int = 0) -> Sequence[User]:
        """Получить список пользователей с пагинацией."""
        result = await self.session.execute(
            select(User).offset(offset).limit(limit)
        )
        return result.scalars().all()