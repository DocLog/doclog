from marshmallow import validates

from ..model import MedicineModel, PatientMedicineModel, PatientModel
from .base_schema import BaseSchema
from .validation import validate_foreign_key


class PatientMedicineSchema(BaseSchema):
    """
    Schema for serializing and deserializing patient-medicine data.

    This class defines a schema for serializing and deserializing patient-medicine
    data. It specifies how patient-medicine-related data should be formatted when
    sending or receiving it from the API.

    Attributes:
        Meta (class): A nested class that defines metadata for the schema, including
        the associated database model (PatientMedicineModel).
    """

    @validates("patient_id")
    def validate_patient_id_field(self, patient_id: int):
        """
        Validate the 'patient_id' field in patient-medicine data.

        This function validates the 'patient_id' field for patient-medicine data,
        ensuring it is a valid foreign key reference to a Patient.

        Args:
            patient_id (int): The patient_id to validate.

        Raises:
            ReferencedKeyNotFoundError: If 'patient_id' is not a valid foreign key
            reference.
        """
        validate_foreign_key(PatientModel.id, patient_id)

    @validates("medicine_id")
    def validate_medicine_id_field(self, medicine_id: int):
        """
        Validate the 'medicine_id' field in patient-medicine data.

        This function validates the 'medicine_id' field for patient-medicine data,
        ensuring it is a valid foreign key reference to a Medicine.

        Args:
            medicine_id (int): The medicine_id to validate.

        Raises:
            ReferencedKeyNotFoundError: If 'medicine_id' is not a valid foreign
            key reference.
        """

        validate_foreign_key(MedicineModel.id, medicine_id)

    class Meta:
        """
        Nested class that defines metadata for the schema.

        Contains the database model associated with the schema (PatientMedicineModel) and specifies
        that foreign keys should be included in the serialized data.
        """

        model = PatientMedicineModel
        include_fk = True
