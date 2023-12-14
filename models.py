from sqlalchemy import create_engine 
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base 

engine = create_engine('sqlite:///clinic_appointment_manager.db')

Base = declarative_base()

class Doctor(Base):

    __tablename__ = 'doctors'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    gender = Column(String(100))
    specialty = Column(String(100))
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(15))
    is_available = Column(Boolean, default=True)

    appointments = relationship("Appointment", back_populates="doctor")

    def __repr__(self):
        return f"<Dr(name='{self.last_name}', specialty='{self.specialty}')>"

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    age = Column(Integer)
    contact = Column(String(25))

    appointments = relationship("Appointment", back_populates="patient")

    def __repr__(self):
        return f"<Patient(name='{self.last_name}')>"
    

class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    appointment_time = Column(DateTime, nullable=False)

    doctor = relationship("Doctor", back_populates="appointments")
    patient = relationship("Patient", back_populates="appointments")

    def __repr__(self):
        return f"<Appointment(doctor='{self.doctor_id}', patient='{self.patient_id}', time='{self.appointment_time}')>"
