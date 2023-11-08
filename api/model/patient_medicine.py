from sqlalchemy import Column, ForeignKey, Integer, String

from .base_model import BaseModel


class PatientMedicineModel(BaseModel):
    """
    Model representing the relationship between patients and prescribed medicines.

    This class defines the database model for the relationship between patients
    and medicines that have been prescribed to them.

    It records which medicines are associated with a patient and may include additional
    notes about the patient's medication.

    Attributes:
        id: The primary key of the model, representing its unique identifier.
        patient_id: The unique identifier of the patient.
        medicine_id: The unique identifier of the prescribed medicine associated
        with the patient.
        notes: Additional notes or details about the patient's medication (optional).

    """

    __tablename__ = "PatientMedicine"

    patient_id = Column(Integer, ForeignKey("Patient.id"), nullable=False)
    medicine_id = Column(Integer, ForeignKey("Medicine.id"), nullable=False)
    notes = Column(String(512))
