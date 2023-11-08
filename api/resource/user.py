from ..service import UserService
from .access_control import access_level
from .base_resource import BaseListResource, BaseResource


class UserResource(BaseResource):
    """
    Resource class for handling individual User records.

    This class provides HTTP methods for handling individual User records, such
    as GET, PUT, and DELETE.

    Attributes:
        service (UserService): The service class responsible for User data operations.
    """

    service = UserService()

    @access_level(3)
    def get(self, data_id: int):
        return super().get(data_id)

    @access_level(3)
    def put(self, data_id: int):
        return super().put(data_id)

    @access_level(1)
    def delete(self, data_id: int):
        return super().delete(data_id)


class UserListResource(BaseListResource):
    """
    List Resource class for handling collections of User records.

    This class provides HTTP methods for handling collections of User records, such
    as GET (all) and POST.

    Attributes:
        service (UserService): The service class responsible for User data operations.
    """

    service = UserService()

    @access_level(1)
    def get(self):
        return super().get()

    @access_level(1)
    def post(self):
        return super().post()
