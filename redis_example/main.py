from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI

from redis_example.redis_db import init_redis, close_redis
from redis_example.rest_controller import app_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🟢 Инициализация Redis...")
    await init_redis()

    yield

    print("🔴 Закрытие соединений с Redis...")
    await close_redis()


app = FastAPI(title="Redis Only Demo", lifespan=lifespan)
app.include_router(app_router)

if __name__ == "__main__":
    uvicorn.run("redis_example.main:app", host="127.0.0.1", port=8001, reload=True)