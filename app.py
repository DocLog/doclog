from flask import Flask

app = Flask("doclog")


@app.route("/")
def index_page():
    return "<h1>Hello, world!</h1>"


if __name__ == "__main__":
    app.run()
