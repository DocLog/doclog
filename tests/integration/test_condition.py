import json

import pytest
from flask.testing import FlaskClient

from api import VER
from tests.common import get_test_parameters
from tests.integration.mock import get_condition


@pytest.mark.parametrize("name", get_test_parameters("empty_texts"))
def test_cannot_process_post_request_with_empty_name(
    client: FlaskClient,
    admin_headers: dict[str, str],
    name: str,
    new_condition_data: dict,
):
    new_condition_data["name"] = name
    response = client.post(
        f"/api/{VER}/condition", headers=admin_headers, json=new_condition_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("name", get_test_parameters("empty_texts"))
def test_cannot_process_put_request_with_empty_name(
    client: FlaskClient,
    admin_headers: dict[str, str],
    name: str,
    new_condition_data: dict,
):
    new_condition_data["name"] = name
    response = client.put(
        f"/api/{VER}/condition/1", headers=admin_headers, json=new_condition_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("description", get_test_parameters("empty_texts"))
def test_cannot_process_post_request_with_empty_description(
    client: FlaskClient,
    admin_headers: dict[str, str],
    description: str,
    new_condition_data: dict,
):
    new_condition_data["description"] = description
    response = client.post(
        f"/api/{VER}/condition", headers=admin_headers, json=new_condition_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("description", get_test_parameters("empty_texts"))
def test_cannot_process_put_request_with_empty_description(
    client: FlaskClient,
    admin_headers: dict[str, str],
    description: str,
    new_condition_data: dict,
):
    new_condition_data["description"] = description
    response = client.put(
        f"/api/{VER}/condition/1", headers=admin_headers, json=new_condition_data
    )

    assert response.status_code == 422


def test_successfully_process_post_request_with_valid_data(
    client: FlaskClient, admin_headers: dict, new_condition_data: dict
):
    response = client.post(
        f"/api/{VER}/condition", headers=admin_headers, json=new_condition_data
    )

    assert response.status_code == 201


def test_successfully_process_put_request_with_valid_data(
    client: FlaskClient, admin_headers: dict, new_condition_data: dict
):
    response = client.put(
        f"/api/{VER}/condition/1", headers=admin_headers, json=new_condition_data
    )

    assert response.status_code == 201


@pytest.mark.parametrize("id", list(range(1, 6)))
def test_successful_get_by_id_request_should_return_correct_data(
    client: FlaskClient, admin_headers: dict[str, str], id: int
):
    response = json.loads(
        client.get(f"/api/{VER}/condition/{id}", headers=admin_headers).data
    )
    expected = get_condition(id)
    expected["id"] = id

    assert response == expected


def test_successful_get_all_request_should_return_correct_data(
    client: FlaskClient, admin_headers: dict[str, str]
):
    response = json.loads(
        client.get(f"/api/{VER}/condition", headers=admin_headers).data
    )
    expected = get_condition("all")
    for i, expected_row in enumerate(expected):
        expected_row["id"] = i + 1

    assert response == expected


@pytest.mark.parametrize("patient_id", list(range(1, 6)))
def test_response_should_filter_results_by_patient_id_when_specified(
    client: FlaskClient, admin_headers: dict[str, str], patient_id: int
):
    response = json.loads(
        client.get(
            f"/api/{VER}/condition?filter=patient_id:{patient_id}",
            headers=admin_headers,
        ).data
    )[0]
    expected = get_condition(patient_id)
    expected["id"] = patient_id

    assert response == expected
