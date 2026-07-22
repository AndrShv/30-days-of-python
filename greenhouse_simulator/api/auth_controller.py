from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from greenhouse_simulator.auth.security import verify_password, create_access_token
from greenhouse_simulator.db.db_model import DBUser, get_db

router = APIRouter(prefix="/auth")

class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


# 1. Эндпоинт авторизации (Выдает токен)
@router.post("/auth/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    # Ищем пользователя в БД через SQLAlchemy
    user = db.query(DBUser).filter(DBUser.email == payload.email).first()

    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный email или пароль"
        )

    # Если всё ок, генерируем JWT токен
    access_token = create_access_token(data={"sub": user.id})
    return {"access_token": access_token, "token_type": "bearer"}

