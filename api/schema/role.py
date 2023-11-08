from marshmallow import validates

from ..model import RoleModel
from .base_schema import BaseSchema
from .validation import validate_required_text_field, validate_unique_value


class RoleSchema(BaseSchema):
    """
    Schema for serializing and deserializing roles.

    This class defines a schema for serializing and deserializing role data. It
    specifies how role-related data should be formatted when sending or receiving
    it from the API.

    Attributes:
        Meta (class): A nested class that defines metadata for the schema, including
        the associated database model (RoleModel).
    """

    @validates("name")
    def validate_name_field(self, name: str):
        """
        Validate the 'name' field in role data.

        This function validates the 'name' field for role data, ensuring it is not
        empty and that the role name is unique within the database.

        Args:
            name (str): The name to validate.

        Raises:
            EmptyTextFieldError: If 'name' is empty.
            UniquenessViolationError: If 'name' is not unique.
        """
        validate_required_text_field(name)
        validate_unique_value(RoleModel.name, name)

    @validates("description")
    def validate_description_field(self, description: str):
        """
        Validate the 'description' field in role data.

        This function validates the 'description' field for role data, ensuring
        it is not empty.

        Args:
            description (str): The description to validate.

        Raises:
            EmptyTextFieldError: If 'description' is empty.
        """
        validate_required_text_field(description)

    class Meta:
        """
        Nested class that defines metadata for the schema.

        Contains the database model associated with the schema (RoleModel).
        """

        model = RoleModel
