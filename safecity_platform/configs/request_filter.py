from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from security import SECRET_JWT_KEY, ALGORITHM

security_bearer = HTTPBearer()



async def filter_requests(credentials: HTTPAuthorizationCredentials = Depends(security_bearer)) -> str:
    token = credentials.credentials

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Не удалось валидировать токен",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_JWT_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        return user_id
    except jwt.PyJWTError:
        raise credentials_exception