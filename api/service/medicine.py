from sqlalchemy import String
from sqlalchemy.orm import Query

from ..model import MedicineModel, PatientMedicineModel
from ..schema import MedicineSchema
from .base_service import BaseService


class MedicineService(BaseService):
    """
    Service class for performing CRUD operations on 'Medicine' data resources.

    This class extends the BaseService and is specialized for handling CRUD operations
    on 'Medicine' data resources. It specifies the 'MedicineModel' as the associated
    SQLAlchemy model and 'MedicineSchema' as the schema for serialization and deserialization.
    """

    model = MedicineModel
    schema = MedicineSchema()

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
                    PatientMedicineModel,
                    self.model.id == PatientMedicineModel.medicine_id,
                ).filter(PatientMedicineModel.patient_id == int(value))

        return query
