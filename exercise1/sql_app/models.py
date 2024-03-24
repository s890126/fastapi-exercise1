from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    email = Column(String, unique = True, index = True)
    address = Column(String)
    birthday = Column(Date)
    age = Column(Integer)


