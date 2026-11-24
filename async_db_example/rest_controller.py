import logging

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from async_db_example.database import get_db_session
from async_db_example.dto import UserResponse, UserCreate
from async_db_example.repository import UserRepository
logger = logging.getLogger(__name__)

app_router = APIRouter()


def get_user_repository(session: AsyncSession = Depends(get_db_session)) -> UserRepository:
    return UserRepository(session)


@app_router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
        user_data: UserCreate,
        user_repo: UserRepository = Depends(get_user_repository),
):
    logger.info(f"Создание нового пользователя: {user_data.username} ({user_data.email})")
    existing_user = await user_repo.get_by_email(user_data.email)

    logger.info(f"Проверка существования пользователя с email: {user_data.email}")
    if existing_user:
        logger.warning(f"Пользователь с email {user_data.email} уже существует")
        raise HTTPException(
            status_code=400,
            detail="Пользователь с таким email уже существует"
        )

    logger.info(f"Пользователь с email {user_data.email} не найден, продолжаем создание")
    return await user_repo.create(
        username=user_data.username,
        email=user_data.email
    )


@app_router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
        user_id: int,
        user_repo: UserRepository = Depends(get_user_repository),
):
    logger.info(f"Получение пользователя с ID: {user_id}")
    user = await user_repo.get_by_id(user_id)
    if not user:
        logger.warning(f"Пользователь с ID {user_id} не найден")
        raise HTTPException(status_code=404, detail="Пользователь не найден")


    logger.info(f"Пользователь с ID {user_id} найден: {user.username} ({user.email})")
    return user