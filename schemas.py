from pydantic import BaseModel, EmailStr
from typing import Optional

class DoctorBase(BaseModel):
    name: str
    dept: str
    email: EmailStr
    phone: str

class DoctorCreate(DoctorBase):
    pass

class DoctorUpdate(BaseModel):
    name: Optional[str] = None
    dept: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

class Doctor(DoctorBase):
    id: int

    class Config:
        from_attributes = True 