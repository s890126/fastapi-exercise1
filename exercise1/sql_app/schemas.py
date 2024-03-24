from pydantic import BaseModel, EmailStr
from datetime import date
    
class ContactBase(BaseModel):
    name : str
    birthday : date
    address : str
    email : EmailStr
    age : int
    
    class Config:
        orm_mode = True
        
class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id : int

