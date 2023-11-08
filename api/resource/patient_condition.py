from ..service import PatientConditionService
from .access_control import access_level
from .base_resource import BaseListResource, BaseResource


class PatientConditionResource(BaseResource):
    """
    Resource class for handling individual PatientCondition records.

    This class provides HTTP methods for handling individual PatientCondition records,
    such as GET, PUT, and DELETE.

    Attributes:
        service (PatientConditionService): The service class responsible for PatientCondition
        data operations.
    """

    service = PatientConditionService()

    @access_level(3)
    def get(self, data_id: int):
        return super().get(data_id)

    @access_level(2)
    def put(self, data_id: int):
        return super().put(data_id)

    @access_level(2)
    def delete(self, data_id: int):
        return super().delete(data_id)


class PatientConditionListResource(BaseListResource):
    """
    List Resource class for handling collections of PatientCondition records.

    This class provides HTTP methods for handling collections of PatientCondition
    records, such as GET (all) and POST.

    Attributes:
        service (PatientConditionService): The service class responsible for PatientCondition
        data operations.
    """

    service = PatientConditionService()

    @access_level(2)
    def get(self):
        return super().get()

    @access_level(2)
    def post(self):
        return super().post()
