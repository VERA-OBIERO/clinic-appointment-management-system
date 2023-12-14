import click
from sqlalchemy.orm import sessionmaker
from models import engine, Patient, Base

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

if __name__ == '__main__':
    cli()