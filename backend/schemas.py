from pydantic import BaseModel, EmailStr
from datetime import date

class PatientCreate(BaseModel):

    full_name: str
    dob: date
    email: EmailStr

    glucose: float
    haemoglobin: float
    cholesterol: float