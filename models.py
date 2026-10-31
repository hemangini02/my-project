from sqlalchemy import Column, Integer, String
from database import Base

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(100), nullable = False)
    dept = Column(String(50), nullable = True)
    email = Column(String(50), unique = True, index = True, nullable = False)
    phone = Column(String(15), unique = True, index = True, nullable = False)


