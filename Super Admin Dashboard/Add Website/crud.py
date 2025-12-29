from sqlalchemy.orm import Session
from models import Website
from schemas import WebsiteCreate, WebsiteUpdate

def create_website(db: Session, website: WebsiteCreate):
    db_site = Website(
        name=website.name,
        url=website.url,
        status=website.status
    )
    db.add(db_site)
    db.commit()
    db.refresh(db_site)
    return db_site

def get_websites(db: Session):
    return db.query(Website).all()

def update_website(db: Session, site_id: int, website: WebsiteUpdate):
    site = db.query(Website).filter(Website.id == site_id).first()
    if not site:
        return None

    site.name = website.name
    site.url = website.url
    site.status = website.status
    db.commit()
    db.refresh(site)
    return site

def delete_website(db: Session, site_id: int):
    site = db.query(Website).filter(Website.id == site_id).first()
    if not site:
        return None

    db.delete(site)
    db.commit()
    return site
