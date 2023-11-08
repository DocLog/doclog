from sqlalchemy import Column, String

from .base_model import BaseModel


class ConditionModel(BaseModel):
    """
    Model representing a medical condition.

    This class defines the database model for medical conditions that patients may
    have.

    Attributes:
        id: The primary key of the model, representing its unique identifier.
        description: A description of the medical condition.
    """

    __tablename__ = "Condition"

    name = Column(String(32), nullable=False)
    description = Column(String(512), nullable=False)
