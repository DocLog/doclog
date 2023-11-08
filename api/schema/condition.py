from marshmallow import validates

from ..model import ConditionModel
from .base_schema import BaseSchema
from .validation import validate_required_text_field


class ConditionSchema(BaseSchema):
    """
    Schema for serializing and deserializing medical condition data.

    This class defines a schema for serializing and deserializing data related to
    medical conditions.

    Attributes:
        Meta (class): A nested class that defines metadata for the schema, including
        the associated database model (ConditionModel).
    """

    @validates("name")
    def validate_name_field(self, name: str):
        """
        Validate the 'name' field for a condition.

        Args:
            name (str): The 'name' field value to validate.

        Raises:
            EmptyTextFieldError: If the 'name' is missing or empty.
        """
        validate_required_text_field(name)

    @validates("description")
    def validate_description_field(self, description: str):
        """
        Validate the 'description' field for a condition.

        Args:
            description (str): The 'description' field value to validate.

        Raises:
            EmptyTextFieldError: If the 'description' is missing or empty.
        """

        validate_required_text_field(description)

    class Meta:
        """
        Nested class that defines metadata for the schema.

        Contains the database model associated to the schema (ConditionModel).
        """

        model = ConditionModel
