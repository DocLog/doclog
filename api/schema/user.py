from marshmallow import post_load, validates

from ..common import password_hasher
from ..model import HealthcareProfessionalModel, PatientModel, RoleModel, UserModel
from .base_schema import BaseSchema
from .validation import (
    validate_email,
    validate_foreign_key,
    validate_required_text_field,
    validate_unique_value,
)


class UserSchema(BaseSchema):
    """
    Schema for serializing and deserializing user data.

    This class defines a schema for serializing and deserializing user data. It
    specifies how user-related data should be formatted when sending or receiving
    it from the API.

    Attributes:
        Meta (class): A nested class that defines metadata for the schema, including
        the associated database model (UserModel).
    """

    @validates("name")
    def validate_name_field(self, name: str):
        """
        Validate the 'name' field in user data.

        This function validates the 'name' field for user data, ensuring it is not
        empty and that the username is unique within the database.

        Args:
            name (str): The username to validate.

        Raises:
            EmptyTextFieldError: If 'name' is empty.
            UniquenessViolationError: If 'name' is not unique.
        """

        validate_required_text_field(name)
        validate_unique_value(UserModel.name, name)

    @validates("password")
    def validate_password_field(self, password: str):
        """
        Validate the 'password' field in user data.

        This function validates the 'password' field for user data, ensuring it
        is not empty.

        Args:
            password (str): The user's password to validate.

        Raises:
            EmptyTextFieldError: If 'password' is empty.
        """

        validate_required_text_field(password)

    @validates("email")
    def validate_email_field(self, email: str):
        """
        Validate the 'email' field in user data.

        This function validates the 'email' field for user data, ensuring it is
        not empty, is unique within the database, and has a valid email format.

        Args:
            email (str): The user's email to validate.

        Raises:
            EmptyTextFieldError: If 'email' is empty.
            UniquenessViolationError: If 'email' is not unique.
            InvalidEmailError: If the provided email address is not in the expected
            format.
        """

        validate_required_text_field(email)
        validate_unique_value(UserModel.email, email)
        validate_email(email)

    @validates("role_id")
    def validate_role_id_field(self, role_id: int):
        """
        Validate the 'role_id' field in user data.

        This function validates the 'role_id' field for user data, ensuring it is
        a valid foreign key referencing roles within the database.

        Args:
            role_id (int): The role ID to validate.

        Raises:
            ReferencedKeyNotFoundError: If 'role_id' is not a valid foreign key
            reference.
        """

        validate_foreign_key(RoleModel.id, role_id)

    @validates("patient_id")
    def validate_patient_id_field(self, patient_id: int | None):
        """
        Validate the 'patient_id' field in user data.

        This function validates the 'patient_id' field for user data, ensuring it
        is a valid foreign key referencing patients within the database or None
        if not provided.

        Args:
            patient_id (int | None): The patient ID to validate.

        Raises:
            ReferencedKeyNotFoundError: If 'patient_id' is not a valid foreign key
            reference.
        """

        if patient_id is not None:
            validate_foreign_key(PatientModel.id, patient_id)

    @validates("healthcare_professional_id")
    def validate_healthcare_professional_id_field(
        self, healthcare_professional_id: int | None
    ):
        """
        Validate the 'healthcare_professional_id' field in user data.

        This function validates the 'healthcare_professional_id' field for user
        data, ensuring it is a valid foreign key referencing healthcare professionals
        within the database or None if not provided.

        Args:
            healthcare_professional_id (int | None): The healthcare professional
            ID to validate.

        Raises:
            ReferencedKeyNotFoundError: If 'healthcare_professional_id' is not a
            valid foreign key reference.
        """
        if healthcare_professional_id is not None:
            validate_foreign_key(
                HealthcareProfessionalModel.id, healthcare_professional_id
            )

    class Meta:
        """
        Nested class that defines metadata for the schema.

        Contains the database model associated with the schema (UserModel).
        """

        model = UserModel
        include_fk = True

    @post_load
    def to_model(self, data: dict, **kwargs):
        """
        Deserialize data into a model instance based on the associated database model.

        Args:
            data (dict): Serialized data to be deserialized into a model instance.

        Returns:
            BaseModel: An instance of the associated database model with deserialized
            data.
        """

        data["password"] = password_hasher.hash_password(data["password"])
        return self.Meta.model(**data)
