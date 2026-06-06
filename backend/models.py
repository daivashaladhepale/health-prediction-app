from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)

    full_name = Column(String)
    dob = Column(String)
    email = Column(String)

    glucose = Column(Float)
    haemoglobin = Column(Float)
    cholesterol = Column(Float)

    remarks = Column(String)