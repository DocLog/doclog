from sqlalchemy import Column, String

from .base_model import BaseModel


class RoleModel(BaseModel):
    """
    Model representing roles in the medical system.

    This class defines the database model for roles, which are used to define
    access permissions for users within the system.

    Roles play a crucial role in controlling and managing access to various parts
    of the system, ensuring that different user types have the appropriate level
    of access and permissions.

    Attributes:
        id: The primary key of the model, representing the unique identifier
            for each role.
        name: The name of the role, which is a short, descriptive identifier
            (e.g., 'Admin', 'Doctor', 'Patient').
        description: A more detailed description of the role and its associated
            access permissions.
    """

    __tablename__ = "Role"

    name = Column(String(32), nullable=False)
    description = Column(String(512), nullable=False)
