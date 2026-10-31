from sqlalchemy.orm import Session
from fastapi import HTTPException
import re 
import models, schemas, crud


def validate_phone(phone: str):
    if not re.fullmatch(r"\d{10,15}", phone):
        raise HTTPException(status_code=400, detail="Invalid phone number")
    return phone

def create_doctor_service(db: Session, doctor: schemas.DoctorCreate):
    existing_email = db.query(models.Doctor).filter(models.Doctor.email == doctor.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")

    validate_phone(doctor.phone)

    existing_phone = db.query(models.Doctor).filter(models.Doctor.phone == doctor.phone).first()
    if existing_phone:
        raise HTTPException(
            status_code=400, 
            detail="Phone number already exists"
        )

    return crud.create_doctor(db=db, doctor=doctor)


def update_doctor_service(db: Session, doctor_id: int, doctor_update: schemas.DoctorUpdate):
    if doctor_update.email:
        raise HTTPException(
            status_code=400,
            detail="Email cannot be updated"
        )
    
    if doctor_update.phone:
        validate_phone(doctor_update.phone)
        existing_phone = db.query(models.Doctor).filter(
            models.Doctor.phone == doctor_update.phone,
            models.Doctor.id != doctor_id
        ).first()
        if existing_phone:
            raise HTTPException(
                status_code=400, 
                detail="Phone number already exists"
            )

    return crud.update_doctor(db=db, doctor_id=doctor_id, doctor_update=doctor_update)


def get_doctors_service(db: Session, page: int = 1, size: int = 10, search: str = ""):
    query = db.query(models.Doctor)
    if search:
        query = query.filter(models.Doctor.name.like(f"%{search}%"))

    total = query.count()
    doctors = query.offset((page - 1) * size).limit(size).all()

    return {"total": total, "page": page, "size": size, "data": doctors}

