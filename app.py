from api import create_app

app = create_app()


@app.route("/")
def index_page():
    return "<h1>Still working!</h1>"


if __name__ == "__main__":
    app.run()
