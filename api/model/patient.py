from sqlalchemy import Column, Date, DateTime, String

from .base_model import BaseModel


class PatientModel(BaseModel):
    """
    Model representing patients in the medical system.

    This class defines the database model for patients who use medical services.

    Patients are characterized by attributes such as their name, surname, CPF
    (Brazilian Taxpayer Registry), birth date, register date, blood type, and
    optional notes.

    Attributes:
        id: The primary key of the model, representing its unique identifier.
        name: The first name of the patient.
        surname: The last name of the patient.
        cpf: The Brazilian Taxpayer Registry (CPF) of the patient, which is
        unique.
        birth_date: The birth date of the patient.
        register_date: The date the patient was registered in the system.
        blood_type: The blood type of the patient (e.g., 'A+', 'B-', etc.).
        notes: Additional notes or details about the patient (optional).
    """

    __tablename__ = "Patient"

    name = Column(String(32), nullable=False)
    surname = Column(String(32), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    birth_date = Column(Date, nullable=False)
    register_date = Column(DateTime, nullable=False)
    blood_type = Column(String(3), nullable=False)
    notes = Column(String(512))
