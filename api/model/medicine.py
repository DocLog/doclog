from sqlalchemy import Column, Float, String

from .base_model import BaseModel


class MedicineModel(BaseModel):
    """
    Model representing medicines.

    This class defines the database model for medicines that can be prescribed to
    patients.

    Medicines have attributes such as name, description, dosage, and dosage unit,
    which are stored in the database.

    Attributes:
        id: The primary key of the model, representing its unique identifier.
        name: The name of the medicine.
        description: A description of the medicine.
        dosage: The dosage of the medicine.
        dosage_unit: The unit of measurement for the medicine dosage.
    """

    __tablename__ = "Medicine"

    name = Column(String(32), nullable=False)
    description = Column(String(512), nullable=False)
    dosage = Column(Float, nullable=False)
    dosage_unit = Column(String(10), nullable=False)
