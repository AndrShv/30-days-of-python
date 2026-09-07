from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from async_db_example.database import init_db, close_db, create_tables
from async_db_example.rest_controller import app_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🟢 Инициализация пула соединений с БД...")
    await init_db()

    print("🛠️ Создание таблиц в БД...")
    await create_tables()

    yield

    print("🔴 Закрытие пула соединений с БД...")
    await close_db()


app = FastAPI(title="Async DB + Repository Demo", lifespan=lifespan)
app.include_router(app_router)

if __name__ == "__main__":
    uvicorn.run("async_db_example.main:app", host="127.0.0.1", port=8001, reload=True)