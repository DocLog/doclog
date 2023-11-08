from datetime import date

from marshmallow import validates

from ..model import PatientModel
from .base_schema import BaseSchema
from .validation import (
    validate_blood_type,
    validate_cpf,
    validate_non_future_datetime,
    validate_required_text_field,
    validate_unique_value,
)


class PatientSchema(BaseSchema):
    """
    Schema for serializing and deserializing patient data.

    This class defines a schema for serializing and deserializing patient data.
    It specifies how patient-related data should be formatted when sending or
    receiving it from the API.

    Attributes:
        Meta (class): A nested class that defines metadata for the schema, including
        the associated database model (PatientModel).
    """

    @validates("name")
    def validate_name_field(self, name: str):
        """
        Validate the 'name' field in patient data.

        This function validates the 'name' field for patient data, ensuring it is
        not empty.

        Args:
            name (str): The name to validate.

        Raises:
            EmptyTextFieldError: If 'name' is empty.
        """
        validate_required_text_field(name)

    @validates("surname")
    def validate_surname_field(self, surname: str):
        """
        Validate the 'surname' field in patient data.

        This function validates the 'surname' field for patient data, ensuring it
        is not empty.

        Args:
            surname (str): The surname to validate.

        Raises:
            EmptyTextFieldError: If 'surname' is empty.
        """
        validate_required_text_field(surname)

    @validates("cpf")
    def validate_cpf_field(self, cpf: str):
        """
        Validate the 'cpf' field in patient data.

        This function validates the 'cpf' field for patient data, ensuring it is
        a valid CPF and that it is unique within the database.

        Args:
            cpf (str): The CPF to validate.

        Raises:
            InvalidCPFError: If the 'cpf' is missing, empty, or not a valid CPF
            format.
            UniquenessViolationError: If the 'cpf' already exists in the database.
        """
        validate_cpf(cpf)
        validate_unique_value(PatientModel.cpf, cpf)

    @validates("birth_date")
    def validate_birth_date_field(self, birth_date: date):
        """
        Validate the 'birth_date' field in patient data.

        This function validates the 'birth_date' field for patient data, ensuring
        it is not a future date.

        Args:
            birth_date (date): The birth_date to validate.

        Raises:
            FutureDateError: If 'birth_date' is in the future.
        """
        validate_non_future_datetime(birth_date)

    @validates("register_date")
    def validate_register_date_field(self, register_date: date):
        """
        Validate the 'register_date' field in patient data.

        This function validates the 'register_date' field for patient data, ensuring
        it is not a future date.

        Args:
            register_date (date): The register_date to validate.

        Raises:
            FutureDateError: If 'register_date' is in the future.
        """
        validate_non_future_datetime(register_date)

    @validates("blood_type")
    def validate_blood_type_field(self, blood_type: str):
        """
        Validate the 'blood_type' field in patient data.

        This function validates the 'blood_type' field for patient data, ensuring
        it matches the expected blood type format.

        Args:
            blood_type (str): The blood_type to validate.

        Raises:
            InvalidBloodTypeError: If 'blood_type' is not in the expected format.
        """
        validate_blood_type(blood_type)

    class Meta:
        """
        Nested class that defines metadata for the schema.

        Contains the database model associated with the schema (PatientModel).
        """

        model = PatientModel
