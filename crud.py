from sqlalchemy.orm import Session
import models, schemas

def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    db_doctor = models.Doctor(
        name = doctor.name,
        dept = doctor.dept,
        email = doctor.email,
        phone = doctor.phone
    )
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def get_doctor(db: Session, doctor_id: int):
    return db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()

def update_doctor(db: Session, doctor_id: int, doctor_update: schemas.DoctorUpdate):
    db_doctor = get_doctor(db, doctor_id)
    if not db_doctor:
        return None

    update_data = doctor_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_doctor, key, value)

    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def delete_doctor(db: Session, doctor_id: int):
    db_doctor = get_doctor(db, doctor_id)
    if not db_doctor:
        return None
    
    db.delete(db_doctor)
    db.commit()
    return db_doctor