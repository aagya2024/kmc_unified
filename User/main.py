from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models, schemas
from jose import jwt

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Website Access Backend")

SECRET_KEY = "SECRET123"
ALGORITHM = "HS256"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🔑 MOCK USER AUTH (assume user already logged in)
def get_current_user(token: str, db: Session):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user or not user.is_active:
        raise HTTPException(status_code=403, detail="Inactive user")
    return user


# 🌐 USER DASHBOARD – SHOW WEBSITES (matches image)
@app.get("/user/my-websites")
def my_websites(token: str, db: Session = Depends(get_db)):
    user = get_current_user(token, db)

    return [
        {"name": uw.website.name}
        for uw in user.websites
    ]


# 🔒 PROTECTED WEBSITE ACCESS
@app.get("/website/{website_name}")
def access_website(website_name: str, token: str, db: Session = Depends(get_db)):
    user = get_current_user(token, db)

    allowed = any(
        uw.website.name.lower() == website_name.lower()
        for uw in user.websites
    )

    if not allowed:
        raise HTTPException(
            status_code=403,
            detail="You do not have access to this website"
        )

    return {
        "message": f"Welcome to {website_name}"
    }
