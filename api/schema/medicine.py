from marshmallow import validates

from ..model import MedicineModel
from .base_schema import BaseSchema
from .validation import validate_positive_value, validate_required_text_field


class MedicineSchema(BaseSchema):
    """
    Schema for serializing and deserializing medicine data.

    This class defines a schema for serializing and deserializing medicine data. It specifies
    how medicine-related data should be formatted when sending or receiving it from the API.

    Attributes:
        Meta (class): A nested class that defines metadata for the schema, including the
        associated database model (MedicineModel).
    """

    @validates("name")
    def validate_name_field(self, name: str):
        """
        Validate the 'name' field in medicine data.

        This function validates the 'name' field for medicine data, ensuring it
        is a non-empty text field.

        Args:
            name (str): The name to validate.

        Raises:
            EmptyTextFieldError: If 'name' is empty.
        """

        validate_required_text_field(name)

    @validates("description")
    def validate_description_field(self, description: str):
        """
        Validate the 'description' field in medicine data.

        This function validates the 'description' field for medicine data, ensuring
        it is a non-empty text field.

        Args:
            description (str): The description to validate.

        Raises:
            EmptyTextFieldError: If 'description' is empty.
        """
        validate_required_text_field(description)

    @validates("dosage")
    def validate_dosage_field(self, dosage: float):
        """
        Validate the 'dosage' field in medicine data.

        This function validates the 'dosage' field for medicine data, ensuring it
        is a positive numeric value.

        Args:
            dosage (float): The dosage value to validate.

        Raises:
            NegativeOrZeroValueError: If 'dosage' is not a positive value.
        """
        validate_positive_value(dosage)

    @validates("dosage_unit")
    def validate_dosage_unit_field(self, dosage_unit: str):
        """
        Validate the 'dosage_unit' field in medicine data.

        This function validates the 'dosage_unit' field for medicine data, ensuring
        it is a non-empty text field.

        Args:
            dosage_unit (str): The dosage unit to validate.

        Raises:
            EmptyTextFieldError: If 'dosage_unit' is empty.
        """

        validate_required_text_field(dosage_unit)

    class Meta:
        """
        Nested class that defines metadata for the schema.

        Contains the database model associated with the schema (MedicineModel).
        """

        model = MedicineModel
