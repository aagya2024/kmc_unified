from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.users.models import User
from app.core.security import verify_password

def authenticate_user(db: Session, identifier: str, password: str):
    """
    Authenticate user by username, email, or phone.
    Returns the user object if successful, None otherwise.
    """
    user = db.query(User).filter(
        or_(
            User.username == identifier,
            User.email == identifier,
            User.phone == identifier
        )
    ).first()
    
    if not user:
        return None
        
    if not verify_password(password, user.hashed_password):
        return None
        
    return user
