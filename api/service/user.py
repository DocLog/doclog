from flask_jwt_extended import create_access_token
from marshmallow import ValidationError

from ..common import password_hasher
from ..exceptions import AuthenticationError
from ..model import UserModel
from ..schema import UserSchema
from .base_service import BaseService


class UserService(BaseService):
    """
    Service class for performing CRUD operations on 'User' data resources.

    This class extends the BaseService and is specialized for handling CRUD operations
    on 'User' data resources. It specifies the 'UserModel' as the associated SQLAlchemy
    model and 'UserSchema' as the schema for serialization and deserialization.
    """

    model = UserModel
    schema = UserSchema()

    def login(self, data: dict) -> tuple[dict | list[dict], int]:
        """
        Authenticate a user and provide an access token upon successful login.

        This method attempts to authenticate a user based on the provided credentials.
        If the credentials are correct, an access token is generated and returned
        in the response. If the credentials are incorrect, an error message is
        returned.

        Args:
            data (dict): A dictionary containing 'name' and 'password' fields for
            user authentication.

        Returns:
            tuple[dict | list[dict], int]: A tuple containing a response message
            or error message and the HTTP status code.

        Raises:
            AuthenticationError: If the provided username or password is incorrect.
            ValidationError: If there's a validation error in the provided data.
        """

        try:
            login_name = data.get("name")
            login_password = data.get("password")

            if login_name is None or login_password is None:
                raise AuthenticationError("Incorrect username or password.")

            user = UserModel.query.filter(UserModel.name == data.get("name")).first()

            if user is None or not password_hasher.validate_password(
                login_password, user.password
            ):
                raise AuthenticationError("Incorrect username or password.")

            access_token = create_access_token(
                identity=user.name,
                additional_claims={"access_level": user.role_id, "user_id": user.id},
            )

            return {
                "access_token": access_token,
                "user_role": user.role_id,
                "user_id": user.id,
            }, 200

        except AuthenticationError as e:
            return e.messages, 401

        except ValidationError as e:
            return e.messages, 422
