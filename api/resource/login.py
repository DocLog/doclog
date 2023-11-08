from flask_restful import Resource, request

from ..service import UserService


class LoginResource(Resource):
    """
    Resource class for handling user authentication and login.

    This class provides an HTTP POST method for user authentication and login.

    Attributes:
        service (UserService): The service class responsible for user authentication
        and login operations.
    """

    service = UserService()

    def post(self):
        """Sends user credentials to the API and expects a JWT in return.

        Returns:
            tuple: An HTTP status code and a message containing the JWT token and
            the user role if request is successful; otherwise, the error message.
        """

        data = request.get_json()
        return self.service.login(data)
