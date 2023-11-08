from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String

from .base_model import BaseModel


class OccurrenceModel(BaseModel):
    """
    Model representing medical occurrences.

    This class defines the database model for medical occurrences, which can be
    appointments or emergency calls.

    Medical occurrences are associated with a patient and a healthcare professional.
    They include information about whether the occurrence was an emergency, the date
    and time, and optional notes.

    Attributes:
        id: The primary key of the model, representing its unique identifier.
        patient_id: The unique identifier of the patient associated with the occurrence.
        healthcare_professional_id: The unique identifier of the healthcare
        professional associated with the occurrence.
        was_emergency: Indicates whether the occurrence was an emergency (True)
        or a regular appointment (False).
        datetime: The date and time of the occurrence.
        notes: Additional notes or details about the occurrence (optional).
    """

    __tablename__ = "Occurrence"

    patient_id = Column(Integer, ForeignKey("Patient.id"), nullable=False)
    healthcare_professional_id = Column(
        Integer, ForeignKey("HealthcareProfessional.id"), nullable=False
    )
    was_emergency = Column(Boolean, nullable=False, default=False)
    datetime = Column(DateTime, nullable=False)
    notes = Column(String(512))
