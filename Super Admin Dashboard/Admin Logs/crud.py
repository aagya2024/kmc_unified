from sqlalchemy.orm import Session
from models import AdminLog
from schemas import AdminCreate, AdminUpdate

def create_admin(db: Session, admin: AdminCreate):
    new_admin = AdminLog(
        name=admin.name,
        role=admin.role,
        status=admin.status
    )
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin

def get_admin_logs(db: Session):
    return db.query(AdminLog).all()

def update_admin(db: Session, admin_id: int, admin: AdminUpdate):
    db_admin = db.query(AdminLog).filter(AdminLog.id == admin_id).first()
    if not db_admin:
        return None

    db_admin.name = admin.name
    db_admin.role = admin.role
    db_admin.status = admin.status
    db.commit()
    db.refresh(db_admin)
    return db_admin

def delete_admin(db: Session, admin_id: int):
    db_admin = db.query(AdminLog).filter(AdminLog.id == admin_id).first()
    if not db_admin:
        return None

    db.delete(db_admin)
    db.commit()
    return db_admin
