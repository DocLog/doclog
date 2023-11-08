from ..service import PatientService
from .access_control import access_level
from .base_resource import BaseListResource, BaseResource


class PatientResource(BaseResource):
    """
    Resource class for handling individual Patient records.

    This class provides HTTP methods for handling individual Patient records, such as GET,
    PUT, and DELETE.

    Attributes:
        service (PatientService): The service class responsible for Patient data operations.
    """

    service = PatientService()

    @access_level(3)
    def get(self, data_id: int):
        return super().get(data_id)

    @access_level(2)
    def put(self, data_id: int):
        return super().put(data_id)

    @access_level(1)
    def delete(self, data_id: int):
        return super().delete(data_id)


class PatientListResource(BaseListResource):
    """
    List Resource class for handling collections of Patient records.

    This class provides HTTP methods for handling collections of Patient records,
    such as GET (all) and POST.

    Attributes:
        service (PatientService): The service class responsible for Patient data
        operations.
    """

    service = PatientService()

    @access_level(2)
    def get(self):
        return super().get()

    @access_level(1)
    def post(self):
        return super().post()
