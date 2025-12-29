from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ward Admin Backend")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ➕ Add User (Ward Admin)
@app.post("/users/")
def add_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


# 📋 List Users (Table View)
@app.get("/users/", response_model=list[schemas.UserResponse])
def list_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    response = []

    for u in users:
        response.append({
            "id": u.id,
            "name": u.name,
            "access_details": len(u.websites),   # ← Access Details column
            "status": "Active" if u.is_active else "—",
            "created_at": u.created_at
        })

    return response


# ✏️ Edit User
@app.put("/users/{user_id}")
def edit_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    updated = crud.update_user(db, user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated successfully"}


# ❌ Delete User
@app.delete("/users/{user_id}")
def remove_user(user_id: int, db: Session = Depends(get_db)):
    success = crud.delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
