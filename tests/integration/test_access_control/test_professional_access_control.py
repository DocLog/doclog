import json

import pytest
from flask.testing import FlaskClient

from api import VER
from tests.integration.test_access_control.common import get_access_denied_response


@pytest.mark.parametrize(
    "endpoint",
    [
        "healthcare-professional",
        "user",
    ],
)
def test_professional_cannot_access_endpoint_using_get_all_method(
    client: FlaskClient, professional_headers: dict[str, str], endpoint: str
):
    response = json.loads(
        client.get(f"/api/{VER}/{endpoint}", headers=professional_headers).data
    )
    expected = get_access_denied_response()

    assert response == expected


@pytest.mark.parametrize(
    "endpoint",
    [
        "healthcare-professional",
        "patient",
        "role",
        "user",
    ],
)
def test_professional_cannot_access_endpoint_using_post_method(
    client: FlaskClient, professional_headers: dict[str, str], endpoint: str
):
    response = json.loads(
        client.post(
            f"/api/{VER}/{endpoint}", headers=professional_headers, json={}
        ).data
    )
    expected = get_access_denied_response()

    assert response == expected


@pytest.mark.parametrize(
    "endpoint",
    [
        "healthcare-professional",
        "role",
    ],
)
def test_professional_cannot_access_endpoint_using_put_method(
    client: FlaskClient, professional_headers: dict[str, str], endpoint: str
):
    response = json.loads(
        client.put(
            f"/api/{VER}/{endpoint}/1", headers=professional_headers, json={}
        ).data
    )
    expected = get_access_denied_response()

    assert response == expected


@pytest.mark.parametrize(
    "endpoint",
    [
        "healthcare-professional",
        "patient",
        "role",
        "user",
    ],
)
def test_professional_cannot_access_endpoint_using_delete_method(
    client: FlaskClient, professional_headers: dict[str, str], endpoint: str
):
    response = json.loads(
        client.delete(f"/api/{VER}/{endpoint}/1", headers=professional_headers).data
    )
    expected = get_access_denied_response()

    assert response == expected


@pytest.mark.parametrize(
    "endpoint",
    [
        "condition",
        "medicine",
        "occurrence",
        "patient-condition",
        "patient-medicine",
        "patient",
        "role",
    ],
)
def test_professional_can_access_endpoint_using_get_all_method(
    client: FlaskClient, professional_headers: dict[str, str], endpoint: str
):
    response = client.get(f"/api/{VER}/{endpoint}", headers=professional_headers)

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
def test_professional_can_access_endpoint_using_get_by_id_method(
    client: FlaskClient, professional_headers: dict[str, str], endpoint: str
):
    response = client.get(f"/api/{VER}/{endpoint}/1", headers=professional_headers)

    assert response.status_code == 200


@pytest.mark.parametrize(
    "endpoint",
    [
        "condition",
        "medicine",
        "occurrence",
        "patient-condition",
        "patient-medicine",
    ],
)
def test_professional_can_access_endpoint_using_post_method(
    client: FlaskClient, professional_headers: dict[str, str], endpoint: str
):
    response = client.post(
        f"/api/{VER}/{endpoint}", headers=professional_headers, json={}
    )

    assert response.status_code == 422


@pytest.mark.parametrize(
    "endpoint",
    [
        "condition",
        "medicine",
        "occurrence",
        "patient-condition",
        "patient-medicine",
        "user",
    ],
)
def test_professional_can_access_endpoint_using_put_method(
    client: FlaskClient, professional_headers: dict[str, str], endpoint: str
):
    response = client.put(
        f"/api/{VER}/{endpoint}/1", headers=professional_headers, json={}
    )

    assert response.status_code == 422


@pytest.mark.parametrize(
    "endpoint",
    [
        "condition",
        "medicine",
        "occurrence",
        "patient-condition",
        "patient-medicine",
    ],
)
def test_professional_can_access_endpoint_using_delete_method(
    client: FlaskClient, professional_headers: dict[str, str], endpoint: str
):
    response = client.delete(f"/api/{VER}/{endpoint}/1", headers=professional_headers)

    assert response.status_code == 204
