from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from app.core.config import settings
from typing import Optional

def create_access_token(
    user_id: int | str,
    role: str,
    department_id: Optional[str] = None,
    ward_id: Optional[str] = None,
    expires_delta: Optional[timedelta] = None
) -> str:
    """
    Creates a JWT token with the strictly required structure.
    """
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {
        "user_id": str(user_id),
        "sub": str(user_id), # Standard claim for compatibility
        "role": role,
        "department_id": department_id,
        "ward_id": ward_id,
        "exp": expire
    }
    
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None
