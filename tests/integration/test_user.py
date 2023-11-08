import json

import pytest
from flask.testing import FlaskClient

from api import VER
from tests.common import get_test_parameters
from tests.integration.mock import get_user


@pytest.mark.parametrize("name", get_test_parameters("empty_texts"))
def test_cannot_process_post_request_with_empty_name(
    client: FlaskClient,
    admin_headers: dict[str, str],
    new_user_data: dict,
    name: str,
):
    new_user_data["name"] = name
    response = client.post(
        f"/api/{VER}/user", headers=admin_headers, json=new_user_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("name", get_test_parameters("empty_texts"))
def test_cannot_process_put_request_with_empty_name(
    client: FlaskClient,
    admin_headers: dict[str, str],
    new_user_data: dict,
    name: str,
):
    new_user_data["name"] = name
    response = client.put(
        f"/api/{VER}/user/1", headers=admin_headers, json=new_user_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("recorded_example", get_user("all"))
def test_cannot_process_post_request_with_non_unique_name(
    client: FlaskClient,
    admin_headers: dict,
    new_user_data: dict,
    recorded_example: dict,
):
    new_user_data["name"] = recorded_example["name"]
    response = client.post(
        f"/api/{VER}/user", headers=admin_headers, json=new_user_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("recorded_example", get_user("all"))
def test_cannot_process_put_request_with_non_unique_name(
    client: FlaskClient,
    admin_headers: dict,
    new_user_data: dict,
    recorded_example: dict,
):
    new_user_data["name"] = recorded_example["name"]
    response = client.put(
        f"/api/{VER}/user/1", headers=admin_headers, json=new_user_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("password", get_test_parameters("empty_texts"))
def test_cannot_process_post_request_with_empty_password(
    client: FlaskClient,
    admin_headers: dict[str, str],
    new_user_data: dict,
    password: str,
):
    new_user_data["password"] = password
    response = client.post(
        f"/api/{VER}/user", headers=admin_headers, json=new_user_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("password", get_test_parameters("empty_texts"))
def test_cannot_process_put_request_with_empty_password(
    client: FlaskClient,
    admin_headers: dict[str, str],
    new_user_data: dict,
    password: str,
):
    new_user_data["password"] = password
    response = client.put(
        f"/api/{VER}/user/1", headers=admin_headers, json=new_user_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("email", get_test_parameters("empty_texts"))
def test_cannot_process_post_request_with_empty_email(
    client: FlaskClient,
    admin_headers: dict[str, str],
    new_user_data: dict,
    email: str,
):
    new_user_data["email"] = email
    response = client.post(
        f"/api/{VER}/user", headers=admin_headers, json=new_user_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("email", get_test_parameters("empty_texts"))
def test_cannot_process_put_request_with_empty_email(
    client: FlaskClient,
    admin_headers: dict[str, str],
    new_user_data: dict,
    email: str,
):
    new_user_data["email"] = email
    response = client.put(
        f"/api/{VER}/user/1", headers=admin_headers, json=new_user_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("recorded_example", get_user("all"))
def test_cannot_process_post_request_with_non_unique_email(
    client: FlaskClient,
    admin_headers: dict,
    new_user_data: dict,
    recorded_example: dict,
):
    new_user_data["email"] = recorded_example["email"]
    response = client.post(
        f"/api/{VER}/user", headers=admin_headers, json=new_user_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("recorded_example", get_user("all"))
def test_cannot_process_put_request_with_non_unique_email(
    client: FlaskClient,
    admin_headers: dict,
    new_user_data: dict,
    recorded_example: dict,
):
    new_user_data["email"] = recorded_example["email"]
    response = client.put(
        f"/api/{VER}/user/1", headers=admin_headers, json=new_user_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("email", get_test_parameters("invalid_emails"))
def test_cannot_process_post_request_with_invalid_email(
    client: FlaskClient, admin_headers: dict, new_user_data: dict, email: str
):
    new_user_data["email"] = email
    response = client.post(
        f"/api/{VER}/user", headers=admin_headers, json=new_user_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("email", get_test_parameters("invalid_emails"))
def test_cannot_process_put_request_with_invalid_email(
    client: FlaskClient, admin_headers: dict, new_user_data: dict, email: str
):
    new_user_data["email"] = email
    response = client.put(
        f"/api/{VER}/user/1", headers=admin_headers, json=new_user_data
    )

    assert response.status_code == 422


def test_cannot_process_post_request_with_unrecorded_role_id(
    client: FlaskClient, admin_headers: dict, new_user_data: dict
):
    new_user_data["role_id"] = 100
    response = client.post(
        f"/api/{VER}/user", headers=admin_headers, json=new_user_data
    )

    assert response.status_code == 422


def test_cannot_process_put_request_with_unrecorded_role_id(
    client: FlaskClient, admin_headers: dict, new_user_data: dict
):
    new_user_data["role_id"] = 100
    response = client.put(
        f"/api/{VER}/user/1", headers=admin_headers, json=new_user_data
    )

    assert response.status_code == 422


def test_cannot_process_post_request_with_unrecorded_patient_id(
    client: FlaskClient, admin_headers: dict, new_user_data: dict
):
    new_user_data["patient_id"] = 100
    response = client.post(
        f"/api/{VER}/user", headers=admin_headers, json=new_user_data
    )

    assert response.status_code == 422


def test_cannot_process_put_request_with_unrecorded_patient_id(
    client: FlaskClient, admin_headers: dict, new_user_data: dict
):
    new_user_data["patient_id"] = 100
    response = client.put(
        f"/api/{VER}/user/1", headers=admin_headers, json=new_user_data
    )

    assert response.status_code == 422


def test_cannot_process_post_request_with_unrecorded_healthcare_professional_id(
    client: FlaskClient, admin_headers: dict, new_user_data: dict
):
    new_user_data["healthcare_professional_id"] = 100
    response = client.post(
        f"/api/{VER}/user", headers=admin_headers, json=new_user_data
    )

    assert response.status_code == 422


def test_cannot_process_put_request_with_unrecorded_healthcare_professional_id(
    client: FlaskClient, admin_headers: dict, new_user_data: dict
):
    new_user_data["healthcare_professional_id"] = 100
    response = client.put(
        f"/api/{VER}/user/1", headers=admin_headers, json=new_user_data
    )

    assert response.status_code == 422


def test_successfully_process_post_request_with_valid_data(
    client: FlaskClient, admin_headers: dict, new_user_data: dict
):
    response = client.post(
        f"/api/{VER}/user", headers=admin_headers, json=new_user_data
    )

    assert response.status_code == 201


def test_successfully_process_put_request_with_valid_data(
    client: FlaskClient, admin_headers: dict, new_user_data: dict
):
    response = client.put(
        f"/api/{VER}/user/1", headers=admin_headers, json=new_user_data
    )

    assert response.status_code == 201


@pytest.mark.parametrize("id", list(range(1, 6)))
def test_successful_get_by_id_request_should_return_correct_data(
    client: FlaskClient, admin_headers: dict[str, str], id: int
):
    response = json.loads(
        client.get(f"/api/{VER}/user/{id}", headers=admin_headers).data
    )
    expected = get_user(id)
    expected["id"] = id

    if "patient_id" not in expected.keys():
        expected["patient_id"] = None

    if "healthcare_professional_id" not in expected.keys():
        expected["healthcare_professional_id"] = None

    # has to disconsider password because of hashing
    response.pop("password", None)
    expected.pop("password", None)

    assert response == expected


def test_successful_get_all_request_should_return_correct_data(
    client: FlaskClient, admin_headers: dict[str, str]
):
    response = json.loads(client.get(f"/api/{VER}/user", headers=admin_headers).data)
    expected = get_user("all")

    for i, expected_row in enumerate(expected):
        expected_row["id"] = i + 1

        if "patient_id" not in expected_row.keys():
            expected_row["patient_id"] = None

        if "healthcare_professional_id" not in expected_row.keys():
            expected_row["healthcare_professional_id"] = None

        # has to disconsider password because of hashing
        expected_row.pop("password", None)

    for response_row in response:
        response_row.pop("password", None)

    assert response == expected
