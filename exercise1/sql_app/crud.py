from sqlalchemy.orm import Session

from . import models, schemas

def get_contact(db : Session, contact_id : int):
    return db.query(models.Contact).filter(models.Contact.id == contact_id).first()

def get_contact_by_email(db : Session, email : str):
    return db.query(models.Contact).filter(models.Contact.email == email).first()

def get_contacts(db : Session, skip : int = 0, limit : int = 100):
    return db.query(models.Contact).offset(skip).limit(limit).all()

def create_contact(db : Session, contact : schemas.ContactCreate):
    db_contact = models.Contact(name = contact.name, birthday = contact.birthday, address = contact.address, email = contact.email, age = contact.age)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

