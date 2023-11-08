import os
from datetime import timedelta

from flask import Flask

from .common import db, jwt, ma, password_hasher, rate_limiter
from .log import setup_logging_system


def create_app() -> Flask:
    app = Flask("doclog")

    setup_logging_system()
    _apply_app_settings(app)
    _setup_password_hasher(app)
    _setup_jwt(app)
    _setup_rate_limiter(app)
    _setup_database_interface(app)
    _setup_serializer(app)

    return app


def _apply_app_settings(app: Flask):
    """
    Apply settings to the Flask application.

    This function applies various settings to the Flask application, including JWT
    configuration, database connection, and error handling settings.

    Args:
        app (Flask): The Flask application instance.
    """

    app.logger.debug("Applying app settings...")
    db_conn_str = _get_database_connection_string()
    access_token_expiration_limit = int(
        os.environ.get("ACCESS_TOKEN_EXPIRATION_TIME_IN_MINUTES")
    )
    app.config.update(
        {
            "JWT_SECRET_KEY": os.environ.get("JWT_KEY"),
            "JWT_ACCESS_TOKEN_EXPIRES": timedelta(
                minutes=access_token_expiration_limit
            ),
            "PROPAGATE_EXCEPTIONS": True,
            "SQLALCHEMY_DATABASE_URI": db_conn_str,
        }
    )


def _get_database_connection_string() -> str:
    """
    Generate the database connection string for the SQL Server.

    This function constructs the database connection string by reading environment
    variables for the database server, name, user ID, and password.

    Returns:
        str: The database connection string.
    """

    server = os.environ.get("DB_SERVER")
    database = os.environ.get("DB_NAME")
    uid = os.environ.get("DB_UID")
    password = os.environ.get("DB_PWD")

    return (
        "mssql+pyodbc:///?odbc_connect="
        "driver={SQL Server};"
        f"server={server};"
        f"database={database};"
        f"uid={uid};"
        f"pwd={password};"
        "encrypt=yes;"
        "connection timeout=30;"
    )


def _setup_password_hasher(app: Flask):
    """
    Initialize the password hashing system for the application.

    Args:
        app (Flask): The Flask application instance.
    """

    app.logger.debug("Initializing Password Hashing system...")
    password_hasher.update_config(
        {
            "pepper": os.environ.get("PEPPER"),
            "rounds": 12,
        }
    )


def _setup_jwt(app: Flask):
    """
    Initialize the JWT management system for the application.

    This function initializes the JWTManager for handling JSON Web Tokens (JWT)
    in the application.

    Args:
        app (Flask): The Flask application instance.
    """

    app.logger.debug("Initializing JWT Management System...")
    jwt.init_app(app)


def _setup_database_interface(app: Flask):
    """
    Initialize the database interface for the application.

    This function initializes the database interface using the Flask-SQLAlchemy
    extension.

    Args:
        app (Flask): The Flask application instance.
    """

    app.logger.debug("Initializing database...")
    db.init_app(app)


def _setup_serializer(app: Flask):
    """
    Initialize the data serializer for the application.

    This function initializes the data serializer using the Flask-Marshmallow extension.

    Args:
        app (Flask): The Flask application instance.
    """

    app.logger.debug("Initializing serializer...")
    ma.init_app(app)


def _setup_rate_limiter(app: Flask):
    """
    Initialize the rate limiter for the application.

    This function initializes the rate limiter for controlling access to the API
    endpoints.

    Args:
        app (Flask): The Flask application instance.
    """

    app.logger.debug("Initializing rate limiter...")
    rate_limiter.init_app(app)
