from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/contacts/", response_model = schemas.Contact)
def create_contact(contact : schemas.ContactCreate, db : Session = Depends(get_db)):
    db_contact = crud.get_contact_by_email(db, email = contact.email)
    if db_contact:
        raise HTTPException(status_code = 400, detail = "Email already registered")
    return crud.create_contact(db = db, contact = contact)

@app.get("/contacts/by-email", response_model = schemas.Contact)
def read_contacts(email : str, db : Session = Depends(get_db)):
    db_contact = crud.get_contact_by_email(db, email = email)
    if not db_contact:
        raise HTTPException(status_code = 404, detail = "Email not found")
    return db_contact

@app.get("/contacts/", response_model = list[schemas.Contact])
def read_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    contacts = crud.get_contacts(db, skip = skip, limit = limit)
    return contacts

@app.get("/contact/{contact_id}", response_model=schemas.Contact)
def read_contact(contact_id: int, db: Session = Depends(get_db)):
    db_contact = crud.get_contact(db, contact_id = contact_id)
    if not db_contact:
        raise HTTPException(status_code = 404, detail = "Contact not found")
    return db_contact

