from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.jwt import decode_access_token
from app.users.models import User, UserRole
from app.core import config

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception
        
    user_id: str = payload.get("user_id")
    if user_id is None:
        raise credentials_exception
        
    user = db.query(User).filter(User.id == int(user_id)).first()
    if user is None:
        raise credentials_exception
        
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
        
    return user

def require_super_admin(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role != UserRole.SUPER_ADMIN.value:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Super Admin access required"
        )
    return current_user

def require_department_admin(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role not in [UserRole.SUPER_ADMIN.value, UserRole.DEPARTMENT_ADMIN.value]:
         raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Department Admin or Super Admin access required"
        )
    return current_user

def require_ward_admin(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role not in [UserRole.SUPER_ADMIN.value, UserRole.WARD_ADMIN.value]:
         raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Ward Admin or Super Admin access required"
        )
    return current_user

def require_user(current_user: User = Depends(get_current_user)) -> User:
    # All authenticated users have access to their own services.
    # We can explicitly allow any valid role here.
    return current_user
