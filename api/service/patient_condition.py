from ..model import PatientConditionModel
from ..schema import PatientConditionSchema
from .base_service import BaseService


class PatientConditionService(BaseService):
    """
    Service class for performing CRUD operations on 'PatientCondition' data resources.

    This class extends the BaseService and is specialized for handling CRUD operations
    on 'PatientCondition' data resources. It specifies the 'PatientConditionModel'
    as the associated SQLAlchemy model and 'PatientConditionSchema' as the schema
    for serialization and deserialization.
    """

    model = PatientConditionModel
    schema = PatientConditionSchema()
