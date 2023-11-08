from ..model import HealthcareProfessionalModel
from ..schema import HealthcareProfessionalSchema
from .base_service import BaseService


class HealthcareProfessionalService(BaseService):
    """
    Service class for performing CRUD operations on 'HealthcareProfessional' data
    resources.

    This class extends the BaseService and is specialized for handling CRUD operations
    on 'HealthcareProfessional' data resources. It specifies the 'HealthcareProfessionalModel'
    as the associated SQLAlchemy model and 'HealthcareProfessionalSchema' as the
    schema for serialization and deserialization.
    """

    model = HealthcareProfessionalModel
    schema = HealthcareProfessionalSchema()
