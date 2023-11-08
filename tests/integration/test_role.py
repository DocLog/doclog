import json

import pytest
from flask.testing import FlaskClient

from api import VER
from tests.common import get_test_parameters
from tests.integration.mock import get_role


@pytest.mark.parametrize("name", get_test_parameters("empty_texts"))
def test_cannot_process_post_request_with_empty_name(
    client: FlaskClient,
    admin_headers: dict[str, str],
    new_role_data: dict,
    name: str,
):
    new_role_data["name"] = name
    response = client.post(
        f"/api/{VER}/role", headers=admin_headers, json=new_role_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("name", get_test_parameters("empty_texts"))
def test_cannot_process_put_request_with_empty_name(
    client: FlaskClient,
    admin_headers: dict[str, str],
    new_role_data: dict,
    name: str,
):
    new_role_data["name"] = name
    response = client.put(
        f"/api/{VER}/role/1", headers=admin_headers, json=new_role_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("description", get_test_parameters("empty_texts"))
def test_cannot_process_post_request_with_empty_description(
    client: FlaskClient,
    admin_headers: dict[str, str],
    new_role_data: dict,
    description: str,
):
    new_role_data["description"] = description
    response = client.post(
        f"/api/{VER}/role", headers=admin_headers, json=new_role_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("description", get_test_parameters("empty_texts"))
def test_cannot_process_put_request_with_empty_description(
    client: FlaskClient,
    admin_headers: dict[str, str],
    new_role_data: dict,
    description: str,
):
    new_role_data["description"] = description
    response = client.put(
        f"/api/{VER}/role/1", headers=admin_headers, json=new_role_data
    )

    assert response.status_code == 422


def test_successfully_process_post_request_with_valid_data(
    client: FlaskClient, admin_headers: dict, new_role_data: dict
):
    response = client.post(
        f"/api/{VER}/role", headers=admin_headers, json=new_role_data
    )

    assert response.status_code == 201


def test_successfully_process_put_request_with_valid_data(
    client: FlaskClient, admin_headers: dict, new_role_data: dict
):
    response = client.put(
        f"/api/{VER}/role/1", headers=admin_headers, json=new_role_data
    )

    assert response.status_code == 201


@pytest.mark.parametrize("id", list(range(1, 4)))
def test_successful_get_by_id_request_should_return_correct_data(
    client: FlaskClient, admin_headers: dict[str, str], id: int
):
    response = json.loads(
        client.get(f"/api/{VER}/role/{id}", headers=admin_headers).data
    )
    expected = get_role(id)
    expected["id"] = id

    assert response == expected


def test_successful_get_all_request_should_return_correct_data(
    client: FlaskClient, admin_headers: dict[str, str]
):
    response = json.loads(client.get(f"/api/{VER}/role", headers=admin_headers).data)
    expected = get_role("all")
    for i, expected_row in enumerate(expected):
        expected_row["id"] = i + 1

    assert response == expected
