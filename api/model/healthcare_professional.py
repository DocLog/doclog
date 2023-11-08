from sqlalchemy import Column, Date, String

from .base_model import BaseModel


class HealthcareProfessionalModel(BaseModel):
    """
    Model representing healthcare professionals.

    This class defines the database model for healthcare professionals, such as
    doctors and paramedics.

    Contains healthcare professionals' information, including their name, surname,
    CPF (Brazilian Taxpayer Registry), CRM (Medical Registry), and birth date.

    Attributes:
        id: The primary key of the model, representing its unique identifier.
        name: The first name of the healthcare professional.
        surname: The last name of the healthcare professional.
        cpf: The Brazilian Taxpayer Registry (CPF) of the healthcare professional,
        which is unique.
        crm: The Medical Registry (CRM) of the healthcare professional.
        birth_date: The birth date of the healthcare professional.
    """

    __tablename__ = "HealthcareProfessional"

    name = Column(String(32), nullable=False)
    surname = Column(String(32), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    crm = Column(String(13), nullable=False, unique=True)
    birth_date = Column(Date, nullable=False)
