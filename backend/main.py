from datetime import date
from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware
from database import engine,SessionLocal
from models import Base,Patient
from schemas import PatientCreate
from ai_service import predict_health


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# CREATE

@app.post("/patients")
def create_patient(data: PatientCreate):

    if data.dob > date.today():
        raise HTTPException(
            status_code=400,
            detail="Date of birth cannot be in the future"
        )

    db = SessionLocal()

    remark = predict_health(
        data.glucose,
        data.haemoglobin,
        data.cholesterol
    )

    patient = Patient(
        full_name=data.full_name,
        dob=str(data.dob),
        email=data.email,
        glucose=data.glucose,
        haemoglobin=data.haemoglobin,
        cholesterol=data.cholesterol,
        remarks=remark
    )

    db.add(patient)
    db.commit()

    return {
        "message":"Patient Added"
    }

# READ

@app.get("/patients")
def get_patients():

    db = SessionLocal()

    patients = db.query(Patient).all()

    return patients

# DELETE

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id:int):

    db = SessionLocal()

    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Not Found"
        )

    db.delete(patient)
    db.commit()

    return {
        "message":"Deleted"
    }

@app.put("/patients/{patient_id}")
def update_patient(patient_id: int, data: PatientCreate):

    if data.dob > date.today():
        raise HTTPException(
            status_code=400,
            detail="Date of birth cannot be in the future"
        )

    db = SessionLocal()

    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient Not Found"
        )

    patient.full_name = data.full_name
    patient.dob = str(data.dob)
    patient.email = data.email
    patient.glucose = data.glucose
    patient.haemoglobin = data.haemoglobin
    patient.cholesterol = data.cholesterol

   
    patient.remarks = predict_health(
        data.glucose,
        data.haemoglobin,
        data.cholesterol
    )

    db.commit()

    return {
        "message": "Patient Updated"
    }