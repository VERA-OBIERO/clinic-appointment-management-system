import click
from sqlalchemy.orm import sessionmaker
from models import engine, Patient, Doctor, Appointment, Base
from datetime import datetime

# Bind the engine to the Base class for metadata creation
Base.metadata.bind = engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

@click.group() # Define a Click command group
def cli():
    pass 

@cli.command() # Command to create a patient
@click.option('--first-name', prompt='First Name', help='First name of the patient')
@click.option('--last-name', prompt='Last Name', help='Last name of the patient')
@click.option('--age', prompt='Age', type=int, help='Age of the patient')
@click.option('--contact', prompt='Contact', help='Contact information of the patient')
def create_patient(first_name, last_name, age, contact): # Create a Patient object and add it to the session
    patient = Patient(first_name=first_name, last_name=last_name, age=age, contact=contact)
    session.add(patient)
    session.commit()
    click.echo('Patient created successfully!') 

@cli.command() #Command to create a doctor
@click.option('--first-name', prompt='First Name', help='First name of the doctor')
@click.option('--last-name', prompt='Last Name', help='Last name of the doctor')
@click.option('--gender', prompt='Gender', help='Gender of the doctor')
@click.option('--specialty', prompt='Specialty', help='Specialty of the doctor')
@click.option('--email', prompt='Email', help='Email of the doctor')
@click.option('--phone', prompt='Phone', help='Phone number of the doctor')
@click.option('--availability', prompt='Availability', type=bool, help='Doctor availability')
def create_doctor(first_name, last_name, gender, specialty, email, phone, availability): # Create a Doctor object and add it to the session
    doctor = Doctor(first_name=first_name, last_name=last_name, gender=gender, specialty=specialty,
                    email=email, phone=phone, is_available=availability)
    session.add(doctor)
    session.commit()
    click.echo('Doctor created successfully!')

@cli.command() #Command to list patients
def list_patients():
    patients = session.query(Patient).all()

    if patients:
        click.echo("List of Patients:")
        for patient in patients:
            click.echo(f"ID: {patient.id}, Name: {patient.first_name} {patient.last_name}, Age: {patient.age}, Contact: {patient.contact}")
    else:
        click.echo("No patients available.")

@cli.command() #Command to list doctors
def list_doctors():
    doctors = session.query(Doctor).all()

    if doctors:
        click.echo("List of Doctors:")
        for doctor in doctors:
            click.echo(f"ID: {doctor.id}, Name: {doctor.first_name} {doctor.last_name}, Specialty: {doctor.specialty}, Email: {doctor.email}, Phone: {doctor.phone}")
    else:
        click.echo("No doctors available.")

@cli.command() #Command to make an appointment
@click.option('--doctor-id', prompt='Doctor ID', type=int, help='ID of the doctor')
@click.option('--patient-id', prompt='Patient ID', type=int, help='ID of the patient')
@click.option('--appointment-time', prompt='Appointment Time', help='Date and time of the appointment (YYYY-MM-DD HH:MM)')
def make_appointment(doctor_id, patient_id, appointment_time):
    try:
        appointment_datetime = datetime.strptime(appointment_time, '%Y-%m-%d %H:%M')
    except ValueError:
        click.echo('Invalid date/time format. Please use YYYY-MM-DD HH:MM format.')
        return

    doctor = session.query(Doctor).get(doctor_id)
    patient = session.query(Patient).get(patient_id)

    if doctor and patient:
        appointment = Appointment(doctor_id=doctor_id, patient_id=patient_id, appointment_time=appointment_datetime)
        session.add(appointment)
        session.commit()
        click.echo('Appointment created successfully!')
    else:
        click.echo('Doctor or Patient ID not found. Please check and try again.')

# Define Merge Sort algorithm to sort appointments by date and time
def merge_sort(appointments):
    if len(appointments) <= 1:
        return appointments
    
    mid = len(appointments) // 2
    left_half = appointments[:mid]
    right_half = appointments[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index].appointment_time < right[right_index].appointment_time:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

@cli.command() #Command to list appointments
def list_appointments():
    appointments = session.query(Appointment).all()

    if appointments:
        appointments.sort(key=lambda x: x.appointment_time) 
        click.echo("List of Appointments:")
        for appointment in appointments:
            doctor_name = f"{appointment.doctor.first_name} {appointment.doctor.last_name}"
            patient_name = f"{appointment.patient.first_name} {appointment.patient.last_name}"
            click.echo(f"ID: {appointment.id}, Doctor: {doctor_name}, Patient: {patient_name}, Appointment Time: {appointment.appointment_time}")
    else:
        click.echo("No appointments available.")

@cli.command() #Command to edit appointment time
@click.option('--appointment-id', prompt='Appointment ID', type=int, help='ID of the appointment to update')
@click.option('--new-appointment-time', prompt='New Appointment Time', help='New date and time for the appointment (YYYY-MM-DD HH:MM)')
def update_appointment(appointment_id, new_appointment_time):
    try:
        appointment_datetime = datetime.strptime(new_appointment_time, '%Y-%m-%d %H:%M')
    except ValueError:
        click.echo('Invalid date/time format. Please use YYYY-MM-DD HH:MM format.')
        return

    appointment = session.query(Appointment).get(appointment_id)
    if appointment:
        appointment.appointment_time = appointment_datetime
        session.commit()
        click.echo(f'Appointment with ID {appointment_id} updated successfully!')
    else:
        click.echo('Appointment ID not found. Update failed.') 

@cli.command() # Command to delete an appointment
@click.option('--appointment-id', prompt='Appointment ID', type=int, help='ID of the appointment to delete')
def delete_appointment(appointment_id): # Deleting an appointment by ID
    appointment = session.query(Appointment).get(appointment_id)
    if appointment:
        session.delete(appointment)
        session.commit()
        click.echo(f'Appointment with ID {appointment_id} deleted successfully!')
    else:
        click.echo('Appointment ID not found. Deletion failed.')

# Execute the command line interface if the script is run directly
if __name__ == '__main__':
    cli()