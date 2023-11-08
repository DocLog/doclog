from ..model import PatientModel
from ..schema import PatientSchema
from .base_service import BaseService


class PatientService(BaseService):
    """
    Service class for performing CRUD operations on 'Patient' data resources.

    This class extends the BaseService and is specialized for handling CRUD operations
    on 'Patient' data resources. It specifies the 'PatientModel' as the associated
    SQLAlchemy model and 'PatientSchema' as the schema for serialization and deserialization.
    """

    model = PatientModel
    schema = PatientSchema()
