import pytest
from flask.testing import FlaskClient

from api import VER


@pytest.mark.parametrize(
    "credentials",
    [
        {"user": "sysadmin'; select true; --", "password": "adm123"},
        {"user": "sysadmin", "password": "adm123'; select true; --"},
    ],
)
def test_sql_injection_through_request_body_should_fail(
    client: FlaskClient, credentials: dict[str, str]
):
    response = client.post(f"/api/{VER}/login", json=credentials)

    assert response.status_code == 401


@pytest.mark.parametrize(
    "endpoint",
    [
        "condition",
        "healthcare-professional",
        "medicine",
        "occurrence",
        "patient-condition",
        "patient-medicine",
        "patient",
        "role",
        "user",
    ],
)
def test_sql_injection_through_unauthorized_request_query_parameters_should_fail(
    client: FlaskClient, endpoint: str
):
    response = client.get(f"/api/{VER}/{endpoint}?filter=id:1'; select true --")

    assert response.status_code == 401


@pytest.mark.parametrize(
    "endpoint",
    [
        "condition",
        "healthcare-professional",
        "medicine",
        "occurrence",
        "patient-condition",
        "patient-medicine",
        "patient",
        "role",
        "user",
    ],
)
def test_sql_injection_through_authorized_request_query_parameters_should_fail(
    client: FlaskClient, admin_headers: dict[str, str], endpoint: str
):
    response = client.get(
        f"/api/{VER}/{endpoint}?filter=id:1'; select true --", headers=admin_headers
    )

    assert response.status_code == 400
