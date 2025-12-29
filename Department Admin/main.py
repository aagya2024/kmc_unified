from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine
import models
from schemas import UserCreate, UserUpdate, UserResponse

# Create DB tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Department Admin User Access System")

# ---------------- DB Dependency ----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------- Add User ----------------
@app.post("/users/", response_model=UserResponse)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    for website_id in user.website_ids:
        db.add(models.UserWebsite(
            user_id=db_user.id,
            website_id=website_id
        ))

    db.commit()

    return UserResponse(
        id=db_user.id,
        name=db_user.name,
        access_details=len(user.website_ids),
        status=db_user.status,
        created_at=db_user.created_at
    )

# ---------------- List Users ----------------
@app.get("/users/", response_model=List[UserResponse])
def list_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()

    return [
        UserResponse(
            id=user.id,
            name=user.name,
            access_details=len(user.websites),
            status=user.status,
            created_at=user.created_at
        ) for user in users
    ]

# ---------------- Update User ----------------
@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if data.status:
        user.status = data.status

    if data.website_ids is not None:
        db.query(models.UserWebsite).filter(
            models.UserWebsite.user_id == user_id
        ).delete()

        for wid in data.website_ids:
            db.add(models.UserWebsite(
                user_id=user_id,
                website_id=wid
            ))

    db.commit()

    return UserResponse(
        id=user.id,
        name=user.name,
        access_details=len(user.websites),
        status=user.status,
        created_at=user.created_at
    )

# ---------------- Delete User ----------------
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
