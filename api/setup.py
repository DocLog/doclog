from flask import Flask


def create_app() -> Flask:
    app = Flask("doclog")

    return app
