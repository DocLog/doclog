from ..service import HealthcareProfessionalService
from .access_control import access_level
from .base_resource import BaseListResource, BaseResource


class HealthcareProfessionalResource(BaseResource):
    """
    Resource class for handling individual HealthcareProfessional records.

    This class provides HTTP methods for handling individual HealthcareProfessional records,
    such as GET, PUT, and DELETE.

    Attributes:
        service (HealthcareProfessionalService): The service class responsible for
        HealthcareProfessional data operations.
    """

    service = HealthcareProfessionalService()

    @access_level(3)
    def get(self, data_id: int):
        return super().get(data_id)

    @access_level(1)
    def put(self, data_id: int):
        return super().put(data_id)

    @access_level(1)
    def delete(self, data_id: int):
        return super().delete(data_id)


class HealthcareProfessionalListResource(BaseListResource):
    """
    List Resource class for handling collections of HealthcareProfessional records.

    This class provides HTTP methods for handling collections of HealthcareProfessional records,
    such as GET (all) and POST.

    Attributes:
        service (HealthcareProfessionalService): The service class responsible for
        HealthcareProfessional data operations.
    """

    service = HealthcareProfessionalService()

    @access_level(1)
    def get(self):
        return super().get()

    @access_level(1)
    def post(self):
        return super().post()
