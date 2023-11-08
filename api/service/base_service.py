from marshmallow import ValidationError
from sqlalchemy import String
from sqlalchemy.orm import Query

from ..common import db
from ..model import BaseModel
from ..schema import BaseSchema


class BaseService:
    """
    Base service class for performing CRUD operations on data resources.

    This class provides methods for creating, reading, updating, and deleting data
    records. It is intended to be subclassed by specific resource services.
    """

    model = BaseModel
    schema = BaseSchema()
    query_blacklist = ["password"]

    def create(self, data: dict) -> tuple[str | dict | list[dict], int]:
        """
        Create a new data record.

        Args:
            data (dict): The data to be created.

        Returns:
            tuple: A tuple containing a message or data and an HTTP status code.
        """

        try:
            data = self.schema.load(data, session=db.session)
            db.session.add(data)
            db.session.commit()

            return self.schema.dump(data), 201

        except ValidationError as e:
            return e.messages, 422

    def read_all(self, query_args: dict) -> tuple[list[dict], int]:
        """
        Read multiple data records.

        Args:
            query_args (dict): Query parameters for filtering and sorting.

        Returns:
            tuple: A tuple containing a list of data records and an HTTP status
            code.
        """

        try:
            query = db.session.query(self.model)
            query = self._apply_query_arguments(query, query_args)
            data = query.all()

            return self.schema.dump(data, many=True), 200
        except ValueError:
            return {"message": "Invalid query argument passed."}, 400

    def read(self, data_id: int) -> tuple[str | dict, int]:
        """
        Read a specific data record.

        Args:
            data_id (int): The ID of the data record to read.

        Returns:
            tuple: A tuple containing a message or data and an HTTP status code.
        """

        data = self.model.query.get_or_404(
            data_id, f"Record with id '{data_id}' not found."
        )

        return self.schema.dump(data), 200

    def update(self, data_id: int, data: dict) -> tuple[dict | list[dict], int]:
        """
        Update a data record.

        Args:
            data_id (int): The ID of the data record to update.
            data (dict): The updated data.

        Returns:
            tuple: A tuple containing a message or data and an HTTP status code.
        """

        try:
            self.model.query.get_or_404(
                data_id, f"Record with id '{data_id}' not found."
            )

            new_data = self.schema.load(data, session=db.session)
            new_data.id = data_id

            db.session.merge(new_data)
            db.session.commit()

            return self.schema.dump(new_data), 201

        except ValidationError as e:
            return e.messages, 422

    def delete(self, data_id: int) -> tuple[str, int]:
        """
        Delete a data record.

        Args:
            data_id (int): The ID of the data record to delete.

        Returns:
            tuple: A tuple containing a message and an HTTP status code.
        """

        existing_data = self.model.query.get_or_404(
            data_id, f"Record with id '{data_id}' not found."
        )

        db.session.delete(existing_data)
        db.session.commit()

        return {"message": f"Successfully deleted '{data_id}'."}, 204

    def _apply_query_arguments(self, query: Query, query_args: dict) -> Query:
        """
        Apply query parameters to the query object.

        Args:
            query (Query): The SQLAlchemy query object.
            query_args (dict): Query parameters for filtering and sorting.

        Returns:
            Query: The modified SQLAlchemy query object.
        """

        filter_param = query_args.get("filter")
        sort_param = query_args.get("sort_by")

        if filter_param:
            filters = filter_param.split(";")
            query = self._apply_query_filters(query, filters)

        if sort_param:
            sort_cols = sort_param.split(";")
            query = self._apply_query_sort(query, sort_cols)

        return query

    def _apply_query_filters(self, query: Query, filters: list[str]) -> Query:
        """
        Apply query filters to the query object.

        Args:
            query (Query): The SQLAlchemy query object.
            filters (list[str]): List of filter conditions.

        Returns:
            Query: The modified SQLAlchemy query object.
        """

        for filter_condition in filters:
            key, value = filter_condition.split(":")
            if key not in self.query_blacklist and hasattr(self.model, key):
                col = getattr(self.model, key)

                if isinstance(col.type, String):
                    query = query.filter(col.like(f"%{value}%"))
                else:
                    query = query.filter(col == value)

        return query

    def _apply_query_sort(self, query: Query, cols: list[str]) -> Query:
        """
        Apply sorting to the query object.

        Args:
            query (Query): The SQLAlchemy query object.
            cols (list[str]): List of columns to sort by.

        Returns:
            Query: The modified SQLAlchemy query object.
        """

        for col in cols:
            if hasattr(self.model, col):
                query = query.order_by(getattr(self.model, col))

        return query
