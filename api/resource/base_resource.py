from flask_restful import Resource, request

from ..service import BaseService


class BaseResource(Resource):
    """
    Base Resource class for handling individual records.

    This class provides common HTTP methods for handling individual records, such
    as GET, PUT, and DELETE. It serves as a base class for specific Resource classes
    that handle records associated with different database models.

    Attributes:
        service (BaseService): The service class responsible for data operations.
    """

    service = BaseService()

    def get(self, data_id: int):
        """Get the record with the specified ID.

        Args:
            data_id (int): The specified record ID.

        Returns:
            tuple: The corresponding Service response.
        """

        return self.service.read(data_id)

    def put(self, data_id: int):
        """Update the record with the specified ID.

        Args:
            data_id (int): The specified record ID.

        Returns:
            tuple: The corresponding Service response.
        """

        data = request.get_json()
        return self.service.update(data_id, data)

    def delete(self, data_id: int):
        """Delete the record with the specified ID.

        Args:
            data_id (int): The specified record ID.

        Returns:
            tuple: The corresponding Service response.
        """

        return self.service.delete(data_id)


class BaseListResource(Resource):
    """
    Base List Resource class for handling collections of records.

    This class provides common HTTP methods for handling collections of records,
    such as GET (all) and POST. It serves as a base class for specific List Resource
    classes that handle collections of records associated with different database
    models.

    Attributes:
        service (BaseService): The service class responsible for data operations.
    """

    service = BaseService()

    def get(self):
        """Get a list of all records.

        Returns:
            tuple: The corresponding Service response.
        """

        query_args = dict(request.args)
        return self.service.read_all(query_args)

    def post(self):
        """Create a new record.

        Returns:
            tuple: The corresponding Service response.
        """

        data = request.get_json()
        return self.service.create(data)
