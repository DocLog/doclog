from flask import Flask

from .log import setup_logging_system


def create_app() -> Flask:
    app = Flask("doclog")

    setup_logging_system()

    return app
