import functools
from typing import Callable

from flask_jwt_extended import get_jwt, verify_jwt_in_request


def access_level(level: int) -> Callable:
    """
    A decorator to enforce role-based access control (RBAC) for API endpoints.

    This decorator checks the access level of the authenticated user against a
    specified access level requirement. If the user's access level is greater than
    or equal to the required level, the decorated function is executed. Otherwise,
    a 401 Unauthorized response is returned.

    Args:
        level (int): The minimum access level required to access the decorated
        endpoint.

    Returns:
        Callable: The decorated function, allowing access control based on access level.
    """

    def wrapper(func: Callable):
        @functools.wraps(func)
        def check_access_level(*args, **kwargs):
            verify_jwt_in_request()

            claims = get_jwt()
            if claims["access_level"] <= level:
                return func(*args, **kwargs)

            return {"message": "Higher access level required."}, 401

        return check_access_level

    return wrapper
