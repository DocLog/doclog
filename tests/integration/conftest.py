from datetime import timedelta

import pytest
from flask import Flask
from flask_jwt_extended import JWTManager, create_access_token
from flask_restful import Api

from api.common import db, ma, password_hasher, rate_limiter
from api.route import set_routes
from tests.integration.mock import generate_fake_data

# app and client


@pytest.fixture(name="app")
def app_fixture():
    app = Flask(__name__)
    app.config.update(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite://",
            "JWT_SECRET_KEY": "TEST-SECRET-KEY",
            "JWT_ACCESS_TOKEN_EXPIRES": timedelta(minutes=5),
        }
    )
    JWTManager(app)

    rate_limiter.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    password_hasher.update_config(
        {
            "pepper": r'\xf1\xba\xc2\xb9"ve\x148\x00d\xc3\x1d\xae\xaa\x98\xf5\xcfL\xffCH(\xe6"6\xba0B\xc9\x94\xcf',
            "rounds": 4,
        }
    )

    with app.app_context():
        db.create_all()
        generate_fake_data()

    api = Api(app)
    set_routes(api)

    return app


@pytest.fixture(name="client")
def client_fixture(app: Flask):
    return app.test_client()


# headers


def get_request_headers_for_access_level(access_level: int):
    mocked_users = ["sysadmin", "carlos_santos", "joao_silva"]

    identity = mocked_users[access_level - 1]
    claims = {"access_level": access_level}

    access_token = create_access_token(identity=identity, additional_claims=claims)
    headers = {"Authorization": f"Bearer {access_token}"}

    return headers


@pytest.fixture(name="admin_headers")
def admin_headers_fixture(app: Flask):
    with app.app_context():
        headers = get_request_headers_for_access_level(1)

    return headers


@pytest.fixture(name="professional_headers")
def professional_headers_fixture(app: Flask):
    with app.app_context():
        headers = get_request_headers_for_access_level(2)

    return headers


@pytest.fixture(name="patient_headers")
def patient_headers_fixture(app: Flask):
    with app.app_context():
        headers = get_request_headers_for_access_level(3)

    return headers


# valid data values


@pytest.fixture(name="new_condition_data")
def new_condition_data_fixture() -> dict[str, str]:
    return {
        "name": "Cancer",
        "description": "A group of diseases involving abnormal cell growth and spread.",
    }


@pytest.fixture(name="new_healthcare_professional_data")
def new_healthcare_professional_data_fixture() -> dict:
    return {
        "id": 6,
        "name": "Helena",
        "surname": "Luckmann",
        "cpf": "45555949910",
        "crm": "CRM/SC 200210",
        "birth_date": "1985-03-24",
    }


@pytest.fixture(name="new_medicine_data")
def new_medicine_data_fixture() -> dict:
    return {
        "name": "Sertraline",
        "description": "Antidepressant drug.",
        "dosage": 50.0,
        "dosage_unit": "mg",
    }


@pytest.fixture(name="new_occurrence_data")
def new_occurrence_data_fixture() -> dict:
    return {
        "patient_id": 1,
        "healthcare_professional_id": 3,
        "was_emergency": True,
        "datetime": "2021-09-11T08:55:00",
        "notes": "Emergency response for heart attack.",
    }


@pytest.fixture(name="new_patient_condition_data")
def new_patient_condition_data_fixture() -> dict:
    return {
        "patient_id": 3,
        "condition_id": 2,
    }


@pytest.fixture(name="new_patient_medicine_data")
def new_patient_medicine_data() -> dict:
    return {"patient_id": 5, "medicine_id": 1}


@pytest.fixture(name="new_patient_data")
def new_patient_data_fixture() -> dict:
    return {
        "id": 6,
        "name": "Caio",
        "surname": "Rodrigues",
        "cpf": "32738283071",
        "birth_date": "2001-04-28",
        "register_date": "2023-06-11T10:45:00",
        "blood_type": "O+",
    }


@pytest.fixture(name="new_role_data")
def new_role_data_fixture() -> dict:
    return {"id": 4, "name": "Expectator", "description": "Random expectator"}


@pytest.fixture(name="new_user_data")
def new_user_data_fixture() -> dict:
    return {
        "id": 12,
        "name": "caio_rodrigues",
        "email": "caio_rodrigues@doclog.com",
        "password": "pwd12345",
        "role_id": 1,
    }
