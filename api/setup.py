import os
from datetime import timedelta

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from .common import db, jwt, ma, password_hasher, rate_limiter
from .log import setup_logging_system
from .route import set_routes


def create_app() -> Flask:
    """
    Initialize and return the DocLog Flask API.

    Returns:
        Flask: DocLog API Flask object.
    """
    app = Flask("doclog", static_folder="build", static_url_path="/")

    setup_logging_system()
    _apply_app_settings(app)
    _setup_password_hasher(app)
    _setup_jwt(app)
    # _setup_rate_limiter(app)
    _setup_database_interface(app)
    _setup_serializer(app)
    _setup_cors_policy(app)
    _estabilish_routes(app)

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
    db_conn_str = os.environ.get("DB_CONN_STR")
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


def _setup_cors_policy(app: Flask):
    """
    Setup CORS policy for the application.

    This function sets up the Cross Origin Resource Sharing policy for for the
    application.

    Args:
        app (Flask): The Flask application instance.
    """

    app.logger.debug("Setting up CORS...")
    CORS(app)


def _estabilish_routes(app: Flask):
    """
    Establish API routes for the application.

    This function establishes the API routes by creating an instance of the Flask-RESTful
    Api class and setting up the available routes using the set_routes function.

    Args:
        app (Flask): The Flask application instance.
    """

    app.logger.debug("Estabilishing routes...")
    api = Api(app)
    set_routes(api)
