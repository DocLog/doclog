import os

from flask import Flask

# from api import create_app

# app = create_app()
app = Flask(__name__)


@app.route("/")
def index_page():
    secret_message = os.environ.get("SECRET_MESSAGE")
    return f"<h1>{secret_message}</h1>"


if __name__ == "__main__":
    app.run()
