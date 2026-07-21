from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from safecity_platform.db.db_model import get_db, DBUser
from safecity_platform.configs.security import verify_password, create_access_token, hash_password
from safecity_platform.dto.data_transf_obj import (
    LoginRequest,
    LoginResponse,
    RegisterRequest,
    RegisterResponse
)

auth_router = APIRouter()


@auth_router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(DBUser).filter(DBUser.email == payload.email).first()

    if not user or not verify_password(payload.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный email или пароль"
        )
    jwt_token = create_access_token(data={"sub": user.id})
    return {"access_token": jwt_token, "token_type": "bearer"}


@auth_router.post("/register", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    db_user = db.query(DBUser).filter(DBUser.email == payload.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь с таким email уже существует"
        )

    hashed_password = hash_password(payload.password)

    new_user = DBUser(
        email=payload.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user