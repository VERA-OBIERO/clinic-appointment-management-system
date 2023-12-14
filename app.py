import click
from sqlalchemy.orm import sessionmaker
from models import engine, Patient, Doctor, Base

# Bind the engine to the Base class for metadata creation
Base.metadata.bind = engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass 

@cli.command()
@click.option('--first-name', prompt='First Name', help='First name of the patient')
@click.option('--last-name', prompt='Last Name', help='Last name of the patient')
@click.option('--age', prompt='Age', type=int, help='Age of the patient')
@click.option('--contact', prompt='Contact', help='Contact information of the patient')
def create_patient(first_name, last_name, age, contact):
    patient = Patient(first_name=first_name, last_name=last_name, age=age, contact=contact)
    session.add(patient)
    session.commit()
    click.echo('Patient created successfully!') 

@cli.command()
@click.option('--first-name', prompt='First Name', help='First name of the doctor')
@click.option('--last-name', prompt='Last Name', help='Last name of the doctor')
@click.option('--gender', prompt='Gender', help='Gender of the doctor')
@click.option('--specialty', prompt='Specialty', help='Specialty of the doctor')
@click.option('--email', prompt='Email', help='Email of the doctor')
@click.option('--phone', prompt='Phone', help='Phone number of the doctor')
@click.option('--availability', prompt='Availability', type=bool, help='Doctor availability')
def create_doctor(first_name, last_name, gender, specialty, email, phone, availability):
    doctor = Doctor(first_name=first_name, last_name=last_name, gender=gender, specialty=specialty,
                    email=email, phone=phone, is_available=availability)
    session.add(doctor)
    session.commit()
    click.echo('Doctor created successfully!')

@cli.command()
def list_patients():
    patients = session.query(Patient).all()

    if patients:
        click.echo("List of Patients:")
        for patient in patients:
            click.echo(f"ID: {patient.id}, Name: {patient.first_name} {patient.last_name}, Age: {patient.age}, Contact: {patient.contact}")
    else:
        click.echo("No patients available.")

if __name__ == '__main__':
    cli()