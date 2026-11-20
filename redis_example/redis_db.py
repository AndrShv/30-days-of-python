from __future__ import annotations

import os
from typing import AsyncGenerator
from redis.asyncio import Redis, ConnectionPool

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

redis_pool: ConnectionPool | None = None
redis_client: Redis | None = None


async def init_redis() -> None:
    global redis_pool, redis_client
    redis_pool = ConnectionPool.from_url(
        REDIS_URL,
        decode_responses=True,
        max_connections=20,
    )
    redis_client = Redis(connection_pool=redis_pool)
    print("🟢 Пул соединений Redis инициализирован")


async def close_redis() -> None:
    global redis_client, redis_pool
    if redis_client is not None:
        await redis_client.aclose()
        print("🔴 Соединение с Redis закрыто")
    if redis_pool is not None:
        await redis_pool.disconnect()


async def get_redis() -> AsyncGenerator[Redis, None]:
    if redis_client is None:
        raise RuntimeError("Redis не инициализирован!")
    yield redis_client