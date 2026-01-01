from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine
from auth import super_admin_only

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Admin Logs & Role Assignment API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Admin Logs API Running"}

# ➕ Add Ward / Department Admin
@app.post("/admin-logs", response_model=schemas.AdminResponse,
          dependencies=[Depends(super_admin_only)])
def add_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    return crud.create_admin(db, admin)

# 📄 View Admin Logs Table
@app.get("/admin-logs", response_model=list[schemas.AdminResponse],
         dependencies=[Depends(super_admin_only)])
def list_admins(db: Session = Depends(get_db)):
    return crud.get_admin_logs(db)

# ✏ Edit Role / Status
@app.put("/admin-logs/{admin_id}", response_model=schemas.AdminResponse,
         dependencies=[Depends(super_admin_only)])
def edit_admin(admin_id: int, admin: schemas.AdminUpdate, db: Session = Depends(get_db)):
    updated = crud.update_admin(db, admin_id, admin)
    if not updated:
        raise HTTPException(status_code=404, detail="Admin not found")
    return updated

# 🗑 Delete Admin
@app.delete("/admin-logs/{admin_id}",
            dependencies=[Depends(super_admin_only)])
def remove_admin(admin_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_admin(db, admin_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Admin not found")
    return {"message": "Admin removed successfully"}
