from fastapi import Depends, HTTPException, APIRouter
from starlette import status
from redis.asyncio import Redis

from redis_example.dto import UserResponse, UserCreate
from redis_example.redis_db import get_redis

app_router = APIRouter()


@app_router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
        user_data: UserCreate,
        redis: Redis = Depends(get_redis),
):
    email_exists = await redis.sismember("users:emails", user_data.email)
    if email_exists:
        raise HTTPException(
            status_code=400,
            detail="Пользователь с таким email уже существует"
        )

    user_id = await redis.incr("users:next_id")

    user_response = UserResponse(
        id=user_id,
        username=user_data.username,
        email=user_data.email,
    )

    user_key = f"user:{user_id}"
    await redis.hset(user_key, mapping=user_response.model_dump())
    await redis.sadd("users:emails", user_data.email)

    return user_response


@app_router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
        user_id: int,
        redis: Redis = Depends(get_redis),
):
    user_key = f"user:{user_id}"

    user_data = await redis.hgetall(user_key)
    if not user_data:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    return UserResponse(
        id=int(user_data["id"]),
        username=user_data["username"],
        email=user_data["email"],
    )