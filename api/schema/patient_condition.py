from marshmallow import validates

from ..model import ConditionModel, PatientConditionModel, PatientModel
from .base_schema import BaseSchema
from .validation import validate_foreign_key


class PatientConditionSchema(BaseSchema):
    """
    Schema for serializing and deserializing patient-condition data.

    This class defines a schema for serializing and deserializing patient-condition data.
    It specifies how patient-condition-related data should be formatted when sending
    or receiving it from the API.

    Attributes:
        Meta (class): A nested class that defines metadata for the schema, including
        the associated database model (PatientConditionModel).
    """

    @validates("patient_id")
    def validate_patient_id_field(self, patient_id: int):
        """
        Validate the 'patient_id' field in patient-condition data.

        This function validates the 'patient_id' field for patient-condition data,
        ensuring it is a valid foreign key reference to a Patient.

        Args:
            patient_id (int): The patient_id to validate.

        Raises:
            ReferencedKeyNotFoundError: If 'patient_id' is not a valid foreign key
            reference.
        """

        validate_foreign_key(PatientModel.id, patient_id)

    @validates("condition_id")
    def validate_condition_id_field(self, condition_id: int):
        """
        Validate the 'condition_id' field in patient-condition data.

        This function validates the 'condition_id' field for patient-condition data,
        ensuring it is a valid foreign key reference to a Condition.

        Args:
            condition_id (int): The condition_id to validate.

        Raises:
            ReferencedKeyNotFoundError: If 'condition_id' is not a valid foreign key reference.
        """

        validate_foreign_key(ConditionModel.id, condition_id)

    class Meta:
        """
        Nested class that defines metadata for the schema.

        Contains the database model associated with the schema (PatientConditionModel) and specifies
        that foreign keys should be included in the serialized data.
        """

        model = PatientConditionModel
        include_fk = True
