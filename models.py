from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime

Base = declarative_base()

class Patient(Base):
    __tablename__ = "patients"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    blood_type = Column(String)
    waiting_time = Column(Integer)  # in days
    urgency_status = Column(String)
    is_active = Column(Boolean, default=True)

