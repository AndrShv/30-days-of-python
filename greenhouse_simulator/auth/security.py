from datetime import datetime, timedelta, timezone
from typing import Optional
from passlib.context import CryptContext
import jwt

# Настройки для хэширования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Настройки для JWT (в реальном проекте вынеси в .env)
SECRET_KEY = "SUPER_SECRET_KEY_DONT_SHARE_IT"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # Добавляем в payload время окончания действия токена
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt