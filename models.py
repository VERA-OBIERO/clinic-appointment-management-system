from sqlalchemy import create_engine 
from sqlalchemy import Column, Integer, String, Boolean
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

    def __repr__(self):
        return f"<Dr(name='{self.last_name}', specialty='{self.specialty}')>"

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    age = Column(Integer)
    contact = Column(String(25))

    def __repr__(self):
        return f"<Patient(name='{self.last_name}')>"
    
    

