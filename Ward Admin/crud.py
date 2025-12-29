from sqlalchemy.orm import Session
import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    for site in user.websites:
        access = models.WebsiteAccess(
            website_name=site.website_name,
            user_id=db_user.id
        )
        db.add(access)

    db.commit()
    return db_user


def get_users(db: Session):
    return db.query(models.User).all()


def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        return None

    db_user.name = user.name
    db_user.is_active = user.is_active

    # remove old websites
    db.query(models.WebsiteAccess).filter(
        models.WebsiteAccess.user_id == user_id
    ).delete()

    for site in user.websites:
        db.add(models.WebsiteAccess(
            website_name=site.website_name,
            user_id=user_id
        ))

    db.commit()
    return db_user


def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return False
    db.delete(user)
    db.commit()
    return True
