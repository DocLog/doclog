from sqlalchemy import Column, Integer

from ..common import db


class BaseModel(db.Model):
    """
    Base model class for database models.

    This class serves as the base for all database models in the application.

    Attributes:
        id: The primary key of the model, representing its unique identifier.
    """

    __abstract__ = True
    __tablename__ = "Base"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    @property
    def table_name(self):
        """
        Get the name of the associated database table.

        Returns:
            str: The name of the database table.
        """
        return self.__tablename__
