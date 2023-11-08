from ..service import MedicineService
from .access_control import access_level
from .base_resource import BaseListResource, BaseResource


class MedicineResource(BaseResource):
    """
    Resource class for handling individual Medicine records.

    This class provides HTTP methods for handling individual Medicine records, such
    as GET, PUT, and DELETE.

    Attributes:
        service (MedicineService): The service class responsible for Medicine data
        operations.
    """

    service = MedicineService()

    @access_level(3)
    def get(self, data_id: int):
        return super().get(data_id)

    @access_level(2)
    def put(self, data_id: int):
        return super().put(data_id)

    @access_level(2)
    def delete(self, data_id: int):
        return super().delete(data_id)


class MedicineListResource(BaseListResource):
    """
    List Resource class for handling collections of Medicine records.

    This class provides HTTP methods for handling collections of Medicine records,
    such as GET (all) and POST.

    Attributes:
        service (MedicineService): The service class responsible for Medicine data
        operations.
    """

    service = MedicineService()

    @access_level(2)
    def get(self):
        return super().get()

    @access_level(2)
    def post(self):
        return super().post()
