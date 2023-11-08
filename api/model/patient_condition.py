from sqlalchemy import Column, ForeignKey, Integer, String

from .base_model import BaseModel


class PatientConditionModel(BaseModel):
    """
    Model representing the relationship between patients and medical conditions.

    This class defines the database model for the relationship between patients
    and medical conditions.

    It records which medical conditions are associated with a patient and may include
    additional notes about the patient's condition.

    Attributes:
        id: The primary key of the model, representing its unique identifier.
        patient_id: The unique identifier of the patient.
        condition_id: The unique identifier of the medical condition associated
        with the patient.
        notes: Additional notes or details about the patient's condition (optional).
    """

    __tablename__ = "PatientCondition"

    patient_id = Column(Integer, ForeignKey("Patient.id"), nullable=False)
    condition_id = Column(Integer, ForeignKey("Condition.id"), nullable=False)
    notes = Column(String(512))
