from api import create_app

app = create_app()

# setup database

# from api.common import db
# from tests.integration.mock import generate_fake_data

# with app.app_context():
#     db.create_all()
#     generate_fake_data()
    
@app.route("/")
def index():
    return app.send_static_file("index.html")


if __name__ == "__main__":
    app.run()
