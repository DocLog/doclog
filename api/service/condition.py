from sqlalchemy import String
from sqlalchemy.orm import Query

from ..model import ConditionModel, PatientConditionModel
from ..schema import ConditionSchema
from .base_service import BaseService


class ConditionService(BaseService):
    """
    Service class for performing CRUD operations on 'Condition' data resources.

    This class extends the BaseService and is specialized for handling CRUD operations
    on 'Condition' data resources. It specifies the 'ConditionModel' as the associated
    SQLAlchemy model and 'ConditionSchema' as the schema for serialization and
    deserialization.
    """

    model = ConditionModel
    schema = ConditionSchema()

    def _apply_query_filters(self, query: Query, filters: list[str]) -> Query:
        for filter_condition in filters:
            key, value = filter_condition.split(":")

            if key not in self.query_blacklist and hasattr(self.model, key):
                col = getattr(self.model, key)

                if isinstance(col.type, String):
                    query = query.filter(col.like(f"%{value}%"))
                else:
                    query = query.filter(col == value)

            elif key == "patient_id":
                query = query.join(
                    PatientConditionModel,
                    self.model.id == PatientConditionModel.condition_id,
                ).filter(PatientConditionModel.patient_id == int(value))

        return query
