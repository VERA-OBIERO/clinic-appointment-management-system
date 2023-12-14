## CLINIC APPOINTMENT MANAGEMENT SYSTEM

Clinic Appointment Manager is a command-line application that manages appointments between doctors and patients. 

** Author: Vera O. **

## Features

- Create and list doctors.
- Create and list patients.
- Create, list, update, and delete appointments.

## Prerequisites

- Python 3.x
- SQLAlchemy
- Click

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/VERA-OBIERO/clinic-appointment-management-system-final-project-phase-3.git
    ```

2. Install dependencies:

    ```bash
    cd clinic-appointment-management-system-final-project-phase-3
    pipenv install
    pip install sqlalchemy, alembic, click 
    ```
## Usage

1. Navigate to the project directory.
2. Run the CLI commands using Python:

    ```bash
    python3 app.py <command> [options]
    ```

    Available commands:
    - `create_patient`: Create a new patient.
    - `create_doctor`: Create a new doctor.
    - `list_patients`: List all patients.
    - `list_doctors`: List all doctors.
    - `make_appointment`: Create a new appointment.
    - `list_appointments`: List all appointments.
    - `update_appointment`: Update an existing appointment.
    - `delete_appointment`: Delete an appointment.

3. Follow the prompts and provide necessary information when running the commands.

## Examples

### Create a Doctor
```bash
python3 app.py create_doctor --first-name John --last-name Doe --gender Male --specialty Cardiology --email johndoe@example.com --phone 1234567890 --availability True
```

## License

This project is licesed under the MIT terms and conditions.