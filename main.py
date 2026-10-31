from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
import models, schemas, service

models.Base.metadata.create_all(bind=engine)

# Create FastAPI Obj
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome! Go to /docs to test the API."}

@app.post("/doctors/", response_model=schemas.Doctor)
def create_doctor(doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    return service.create_doctor_service(db=db, doctor=doctor)

@app.get("/doctors/{doctor_id}", response_model=schemas.Doctor)
def read_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = service.crud.get_doctor(db=db, doctor_id=doctor_id)
    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@app.get("/doctors/")
def read_doctors(page: int = 1, size: int = 10, search: str = "", db: Session = Depends(get_db)):
    return service.get_doctors_service(db=db, page=page, size=size, search=search)

@app.put("/doctors/{doctor_id}", response_model=schemas.Doctor)
def update_doctor(doctor_id: int, doctor_update: schemas.DoctorUpdate, db: Session = Depends(get_db)):
    doctor = service.update_doctor_service(db=db, doctor_id=doctor_id, doctor_update=doctor_update)
    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@app.delete("/doctors/{doctor_id}", response_model=schemas.Doctor)
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = service.crud.delete_doctor(db=db, doctor_id=doctor_id)
    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor
