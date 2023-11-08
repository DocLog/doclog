from ..model import OccurrenceModel
from ..schema import OccurrenceSchema
from .base_service import BaseService


class OccurrenceService(BaseService):
    """
    Service class for performing CRUD operations on 'Occurrence' data resources.

    This class extends the BaseService and is specialized for handling CRUD operations
    on 'Occurrence' data resources. It specifies the 'OccurrenceModel' as the associated
    SQLAlchemy model and 'OccurrenceSchema' as the schema for serialization and deserialization.
    """

    model = OccurrenceModel
    schema = OccurrenceSchema()
