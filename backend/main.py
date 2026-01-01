from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import engine, Base, get_db
from app.auth import router as auth_router
from app.auth import dependencies
from app.users import models
from app.core import security, config

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=config.settings.PROJECT_NAME)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Auth Router
app.include_router(auth_router.router, prefix="/api/v1/auth", tags=["Auth"])

# Seed Data on Startup
@app.on_event("startup")
def startup_db_client():
    # This is a good place to seed default users if they don't exist
    # For now, we rely on manual seeding or a separate script, 
    # but I will inject a simplified seed logic for verification if strictly needed.
    # To keep main.py clean, I won't inline 50 lines of seed code unless requested.
    # But validation checklist says "Super Admin login works".
    # I'll create a helper function to seed if empty.
    from app.database import SessionLocal
    db = SessionLocal()
    try:
        check_and_seed_users(db)
    finally:
        db.close()

def check_and_seed_users(db: Session):
    if db.query(models.User).first():
        return
        
    users_to_create = [
        {
            "username": "superadmin", "email": "admin@kmc.com", "phone": "9800000000",
            "password": "password123", "role": models.UserRole.SUPER_ADMIN
        },
        {
            "username": "deptadmin", "email": "dept@kmc.com", "phone": "9800000001",
            "password": "password123", "role": models.UserRole.DEPARTMENT_ADMIN,
            "department_id": "DEPT_01"
        },
        {
            "username": "wardadmin", "email": "ward@kmc.com", "phone": "9800000002",
            "password": "password123", "role": models.UserRole.WARD_ADMIN,
            "ward_id": "WARD_01"
        },
        {
            "username": "user", "email": "user@kmc.com", "phone": "9800000003",
            "password": "password123", "role": models.UserRole.USER
        }
    ]
    
    for u in users_to_create:
        db_user = models.User(
            username=u["username"],
            email=u["email"],
            phone=u["phone"],
            hashed_password=security.get_password_hash(u["password"]),
            role=u["role"].value,
            department_id=u.get("department_id"),
            ward_id=u.get("ward_id")
        )
        db.add(db_user)
    
    db.commit()
    print("Seed data created.")

# Protected Routes for Verification
@app.get("/api/v1/protected/super-admin", dependencies=[Depends(dependencies.require_super_admin)])
def super_admin_only():
    return {"message": "Hello Super Admin"}

@app.get("/api/v1/protected/dept-admin", dependencies=[Depends(dependencies.require_department_admin)])
def dept_admin_only():
    return {"message": "Hello Department Admin"}

@app.get("/api/v1/protected/ward-admin", dependencies=[Depends(dependencies.require_ward_admin)])
def ward_admin_only():
    return {"message": "Hello Ward Admin"}

@app.get("/api/v1/protected/user", dependencies=[Depends(dependencies.require_user)])
def user_only():
    return {"message": "Hello User"}

@app.get("/")
def root():
    return {"message": "KMC Unified Auth System is Running"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
