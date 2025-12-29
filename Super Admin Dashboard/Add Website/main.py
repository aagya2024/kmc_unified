from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine
from auth import super_admin_only

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Super Admin Website Management API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/websites", response_model=schemas.WebsiteResponse,
          dependencies=[Depends(super_admin_only)])
def add_website(website: schemas.WebsiteCreate, db: Session = Depends(get_db)):
    return crud.create_website(db, website)

@app.get("/websites", response_model=list[schemas.WebsiteResponse],
         dependencies=[Depends(super_admin_only)])
def list_websites(db: Session = Depends(get_db)):
    return crud.get_websites(db)

@app.put("/websites/{site_id}", response_model=schemas.WebsiteResponse,
         dependencies=[Depends(super_admin_only)])
def edit_website(site_id: int, website: schemas.WebsiteUpdate, db: Session = Depends(get_db)):
    updated = crud.update_website(db, site_id, website)
    if not updated:
        raise HTTPException(status_code=404, detail="Website not found")
    return updated

@app.delete("/websites/{site_id}",
            dependencies=[Depends(super_admin_only)])
def remove_website(site_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_website(db, site_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Website not found")
    return {"message": "Website deleted successfully"}
