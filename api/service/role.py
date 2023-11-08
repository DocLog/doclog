from ..model import RoleModel
from ..schema import RoleSchema
from .base_service import BaseService


class RoleService(BaseService):
    """
    Service class for performing CRUD operations on 'Role' data resources.

    This class extends the BaseService and is specialized for handling CRUD operations
    on 'Role' data resources. It specifies the 'RoleModel' as the associated SQLAlchemy
    model and 'RoleSchema' as the schema for serialization and deserialization.
    """

    model = RoleModel
    schema = RoleSchema()
