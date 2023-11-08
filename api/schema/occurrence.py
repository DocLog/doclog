from marshmallow import validates

from ..model import HealthcareProfessionalModel, OccurrenceModel, PatientModel
from .base_schema import BaseSchema
from .validation import validate_foreign_key, validate_non_future_datetime


class OccurrenceSchema(BaseSchema):
    """
    Schema for serializing and deserializing occurrence data.

    This class defines a schema for serializing and deserializing occurrence data. It specifies
    how occurrence-related data should be formatted when sending or receiving it from the API.

    Attributes:
        Meta (class): A nested class that defines metadata for the schema, including the
        associated database model (OccurrenceModel).
    """

    @validates("patient_id")
    def validate_patient_id_field(self, patient_id: int):
        """
        Validate the 'patient_id' field in occurrence data.

        This function validates the 'patient_id' field for occurrence data, ensuring
        it is a valid foreign key reference to a Patient.

        Args:
            patient_id (int): The patient_id to validate.

        Raises:
            ReferencedKeyNotFoundError: If 'patient_id' is not a valid foreign key
            reference.
        """

        validate_foreign_key(PatientModel.id, patient_id)

    @validates("healthcare_professional_id")
    def validate_healthcare_professional_id_field(
        self, healthcare_professional_id: int
    ):
        """
        Validate the 'healthcare_professional_id' field in occurrence data.

        This function validates the 'healthcare_professional_id' field for occurrence
        data, ensuring it is a valid foreign key reference to a HealthcareProfessional.

        Args:
            healthcare_professional_id (int): The healthcare_professional_id to
            validate.

        Raises:
            ReferencedKeyNotFoundError: If 'healthcare_professional_id' is not a
            valid foreign key reference.
        """
        validate_foreign_key(HealthcareProfessionalModel.id, healthcare_professional_id)

    @validates("datetime")
    def validate_datetime_field(self, datetime: int):
        """
        Validate the 'datetime' field in occurrence data.

        This function validates the 'datetime' field for occurrence data, ensuring
        it is not a future date.

        Args:
            datetime (int): The datetime to validate.

        Raises:
            FutureDateError: If 'datetime' is a future date.
        """
        validate_non_future_datetime(datetime)

    class Meta:
        """
        Nested class that defines metadata for the schema.

        Contains the database model associated with the schema (OccurrenceModel)
        and specifies that foreign keys should be included in the serialized data.
        """

        model = OccurrenceModel
        include_fk = True
