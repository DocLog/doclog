import pytest
from flask.testing import FlaskClient

from api import VER


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
def test_cannot_access_endpoint_using_get_by_invalid_id(
    client: FlaskClient, admin_headers: dict[str, str], endpoint: str
):
    response = client.get(f"/api/{VER}/{endpoint}/100", headers=admin_headers)

    assert response.status_code == 404


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
def test_cannot_access_endpoint_using_put_with_invalid_id(
    client: FlaskClient, admin_headers: dict[str, str], endpoint: str
):
    response = client.put(f"/api/{VER}/{endpoint}/100", headers=admin_headers, json={})

    assert response.status_code == 404


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
def test_cannot_access_endpoint_using_delete_with_invalid_id(
    client: FlaskClient, admin_headers: dict[str, str], endpoint: str
):
    response = client.delete(f"/api/{VER}/{endpoint}/100", headers=admin_headers)

    assert response.status_code == 404


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
def test_post_request_with_missing_fields_fails(
    client: FlaskClient, admin_headers: dict[str, str], endpoint: str
):
    response = client.post(f"/api/{VER}/{endpoint}", headers=admin_headers, json={})

    assert response.status_code == 422


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
def test_put_request_with_missing_fields_fails(
    client: FlaskClient, admin_headers: dict[str, str], endpoint: str
):
    response = client.put(f"/api/{VER}/{endpoint}/1", headers=admin_headers, json={})

    assert response.status_code == 422
