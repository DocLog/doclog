from datetime import date

from marshmallow import validates

from ..model import HealthcareProfessionalModel
from .base_schema import BaseSchema
from .validation import (
    validate_cpf,
    validate_crm,
    validate_non_future_datetime,
    validate_required_text_field,
    validate_unique_value,
)


class HealthcareProfessionalSchema(BaseSchema):
    """
    Schema for serializing and deserializing data of healthcare professionals.

    This class defines a schema for serializing and deserializing data related to
    healthcare professionals.

    Attributes:
        Meta (class): A nested class that defines metadata for the schema, including
        the associated database model (HealthcareProfessionalModel).
    """

    @validates("name")
    def validate_name_field(self, name: str):
        """
        Validate the 'name' field for a healthcare professional.

        Args:
            name (str): The 'name' field value to validate.

        Raises:
            EmptyTextFieldError: If the 'name' is missing or empty.
        """

        validate_required_text_field(name)

    @validates("surname")
    def validate_surname_field(self, surname: str):
        """
        Validate the 'surname' field for a healthcare professional.

        Args:
            surname (str): The 'surname' field value to validate.

        Raises:
            EmptyTextFieldError: If the 'surname' is missing or empty.
        """

        validate_required_text_field(surname)

    @validates("cpf")
    def validate_cpf_field(self, cpf: str):
        """
        Validate the 'cpf' field for a healthcare professional.

        Args:
            cpf (str): The 'cpf' field value to validate.

        Raises:
            InvalidCPFError: If the 'cpf' is missing, empty, or not a valid CPF
            format.
            UniquenessViolationError: If the 'cpf' already exists in the database.
        """

        validate_cpf(cpf)
        validate_unique_value(HealthcareProfessionalModel.cpf, cpf)

    @validates("crm")
    def validate_crm_field(self, crm: str):
        """
        Validate the 'crm' field for a healthcare professional.

        Args:
            crm (str): The 'crm' field value to validate.

        Raises:
            InvalidCRMError: If the 'crm' is missing, empty, or not a valid CRM
            format.
            UniquenessViolationError: If the 'crm' already exists in the database.
        """

        validate_crm(crm)
        validate_unique_value(HealthcareProfessionalModel.crm, crm)

    @validates("birth_date")
    def validate_birth_date_field(self, birth_date: date):
        """
        Validate the 'birth_date' field for a healthcare professional.

        Args:
            birth_date (date): The 'birth_date' field value to validate.

        Raises:
            FutureDateError: If the 'birth_date' is in the future.
        """

        validate_non_future_datetime(birth_date)

    class Meta:
        """
        Nested class that defines metadata for the schema.

        Contains the database model associated with the schema (HealthcareProfessionalModel).
        """

        model = HealthcareProfessionalModel
