from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "SECRET123"
ALGORITHM = "HS256"

def create_token(user_id: int):
    payload = {
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(hours=2)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
