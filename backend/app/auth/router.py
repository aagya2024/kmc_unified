from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.service import authenticate_user
from app.auth.jwt import create_access_token
from app.auth import dependencies
from app.users import schemas
from app.users.models import User

router = APIRouter()

@router.post("/login", response_model=schemas.Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Unified login for all users (Super Admin, Dept Admin, Ward Admin, User).
    Accepts username, email, or phone in the 'username' field.
    """
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username, email, phone or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(
        user_id=user.id,
        role=user.role,
        department_id=user.department_id,
        ward_id=user.ward_id
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/verify")
def verify_token(current_user: User = Depends(dependencies.get_current_user)):
    """
    Endpoint for frontend to verify if a token is still valid and get user details.
    """
    return {
        "status": "ok", 
        "user_id": current_user.id, 
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role,
        "department_id": current_user.department_id,
        "ward_id": current_user.ward_id
    }
