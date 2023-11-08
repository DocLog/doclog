from ..service import RoleService
from .access_control import access_level
from .base_resource import BaseListResource, BaseResource


class RoleResource(BaseResource):
    """
    Resource class for handling individual Role records.

    This class provides HTTP methods for handling individual Role records, such
    as GET, PUT, and DELETE.

    Attributes:
        service (RoleService): The service class responsible for Role data operations.
    """

    service = RoleService()

    @access_level(3)
    def get(self, data_id: int):
        return super().get(data_id)

    @access_level(1)
    def put(self, data_id: int):
        return super().put(data_id)

    @access_level(1)
    def delete(self, data_id: int):
        return super().delete(data_id)


class RoleListResource(BaseListResource):
    """
    List Resource class for handling collections of Role records.

    This class provides HTTP methods for handling collections of Role records, such
    as GET (all) and POST.

    Attributes:
        service (RoleService): The service class responsible for Role data operations.
    """

    service = RoleService()

    @access_level(3)
    def get(self):
        return super().get()

    @access_level(1)
    def post(self):
        return super().post()
