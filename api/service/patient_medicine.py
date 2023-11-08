from ..model import PatientMedicineModel
from ..schema import PatientMedicineSchema
from .base_service import BaseService


class PatientMedicineService(BaseService):
    """
    Service class for performing CRUD operations on 'PatientMedicine' data resources.

    This class extends the BaseService and is specialized for handling CRUD operations
    on 'PatientMedicine' data resources. It specifies the 'PatientMedicineModel'
    as the associated SQLAlchemy model and 'PatientMedicineSchema' as the schema
    for serialization and deserialization.
    """

    model = PatientMedicineModel
    schema = PatientMedicineSchema()
