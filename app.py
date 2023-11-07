import os

from api import create_app

app = create_app()


@app.route("/")
def index_page():
    secret_message = os.environ.get("SECRET-MESSAGE")
    return f"<h1>{secret_message}</h1>"


if __name__ == "__main__":
    app.run()
