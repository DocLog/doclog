from ..service import OccurrenceService
from .access_control import access_level
from .base_resource import BaseListResource, BaseResource


class OccurrenceResource(BaseResource):
    """
    Resource class for handling individual Occurrence records.

    This class provides HTTP methods for handling individual Occurrence records,
    such as GET, PUT, and DELETE.

    Attributes:
        service (OccurrenceService): The service class responsible for Occurrence
        data operations.
    """

    service = OccurrenceService()

    @access_level(3)
    def get(self, data_id: int):
        return super().get(data_id)

    @access_level(2)
    def put(self, data_id: int):
        return super().put(data_id)

    @access_level(2)
    def delete(self, data_id: int):
        return super().delete(data_id)


class OccurrenceListResource(BaseListResource):
    """
    List Resource class for handling collections of Occurrence records.

    This class provides HTTP methods for handling collections of Occurrence records,
    such as GET (all) and POST.

    Attributes:
        service (OccurrenceService): The service class responsible for Occurrence
        data operations.
    """

    service = OccurrenceService()

    @access_level(2)
    def get(self):
        return super().get()

    @access_level(2)
    def post(self):
        return super().post()
