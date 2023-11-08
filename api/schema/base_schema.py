from marshmallow import post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from ..model import BaseModel


class BaseSchema(SQLAlchemyAutoSchema):
    """
    Base schema for serializing and deserializing data.

    This class serves as a base schema for serializing and deserializing data.

    Attributes:
        Meta (class): A nested class that defines metadata for the schema, including
        the associated database model.

    Methods:
        to_model(self, data: dict): Deserialize data into a model instance based
        on the associated database model.
    """

    class Meta:
        """
        Nested class that defines metadata for the schema.

        Contains the database model associated to the schema.
        """

        model: BaseModel

    @post_load
    def to_model(self, data: dict, **kwargs):
        """
        Deserialize data into a model instance based on the associated database model.

        Args:
            data (dict): Serialized data to be deserialized into a model instance.

        Returns:
            BaseModel: An instance of the associated database model with deserialized
            data.
        """
        return self.Meta.model(**data)
