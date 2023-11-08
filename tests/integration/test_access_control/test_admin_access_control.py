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
def test_admin_can_access_endpoint_using_get_all_method(
    client: FlaskClient, admin_headers: dict[str, str], endpoint: str
):
    response = client.get(f"/api/{VER}/{endpoint}", headers=admin_headers)

    assert response.status_code == 200


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
def test_admin_can_access_endpoint_using_get_by_id_method(
    client: FlaskClient, admin_headers: dict[str, str], endpoint: str
):
    response = client.get(f"/api/{VER}/{endpoint}/1", headers=admin_headers)

    assert response.status_code == 200


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
def test_admin_can_access_endpoint_using_post_method(
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
def test_admin_can_access_endpoint_using_put_method(
    client: FlaskClient, admin_headers: dict[str, str], endpoint: str
):
    response = client.put(f"/api/{VER}/{endpoint}/1", headers=admin_headers, json={})

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
def test_admin_can_access_endpoint_using_delete_method(
    client: FlaskClient, admin_headers: dict[str, str], endpoint: str
):
    response = client.delete(f"/api/{VER}/{endpoint}/1", headers=admin_headers, json={})

    assert response.status_code == 204
