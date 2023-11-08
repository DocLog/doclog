import json

import pytest
from flask.testing import FlaskClient

from api import VER
from tests.common import get_test_parameters
from tests.integration.mock import get_occurrence


def test_cannot_process_post_request_with_unrecorded_patient_id(
    client: FlaskClient, admin_headers: dict, new_occurrence_data: dict
):
    new_occurrence_data["patient_id"] = 100
    response = client.post(
        f"/api/{VER}/occurrence", headers=admin_headers, json=new_occurrence_data
    )

    assert response.status_code == 422


def test_cannot_process_put_request_with_unrecorded_patient_id(
    client: FlaskClient, admin_headers: dict, new_occurrence_data: dict
):
    new_occurrence_data["patient_id"] = 100
    response = client.put(
        f"/api/{VER}/occurrence/1", headers=admin_headers, json=new_occurrence_data
    )

    assert response.status_code == 422


def test_cannot_process_post_request_with_unrecorded_healthcare_professional_id(
    client: FlaskClient, admin_headers: dict, new_occurrence_data: dict
):
    new_occurrence_data["healthcare_professional_id"] = 100
    response = client.post(
        f"/api/{VER}/occurrence", headers=admin_headers, json=new_occurrence_data
    )

    assert response.status_code == 422


def test_cannot_process_put_request_with_unrecorded_healthcare_professional_id(
    client: FlaskClient, admin_headers: dict, new_occurrence_data: dict
):
    new_occurrence_data["healthcare_professional_id"] = 100
    response = client.put(
        f"/api/{VER}/occurrence/1", headers=admin_headers, json=new_occurrence_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("datetime", get_test_parameters("future_dates"))
def test_cannot_process_post_request_with_invalid_datetime(
    client: FlaskClient, admin_headers: dict, new_occurrence_data: dict, datetime: str
):
    new_occurrence_data["datetime"] = datetime
    response = client.post(
        f"/api/{VER}/occurrence", headers=admin_headers, json=new_occurrence_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("datetime", get_test_parameters("future_dates"))
def test_cannot_process_put_request_with_invalid_datetime(
    client: FlaskClient, admin_headers: dict, new_occurrence_data: dict, datetime: str
):
    new_occurrence_data["datetime"] = datetime
    response = client.put(
        f"/api/{VER}/occurrence/1", headers=admin_headers, json=new_occurrence_data
    )

    assert response.status_code == 422


def test_successfully_process_post_request_with_valid_data(
    client: FlaskClient, admin_headers: dict, new_occurrence_data: dict
):
    response = client.post(
        f"/api/{VER}/occurrence", headers=admin_headers, json=new_occurrence_data
    )

    assert response.status_code == 201


def test_successfully_process_put_request_with_valid_data(
    client: FlaskClient, admin_headers: dict, new_occurrence_data: dict
):
    response = client.put(
        f"/api/{VER}/occurrence/1", headers=admin_headers, json=new_occurrence_data
    )

    assert response.status_code == 201


@pytest.mark.parametrize("id", list(range(1, 6)))
def test_successful_get_by_id_request_should_return_correct_data(
    client: FlaskClient, admin_headers: dict[str, str], id: int
):
    response = json.loads(
        client.get(f"/api/{VER}/occurrence/{id}", headers=admin_headers).data
    )
    expected = get_occurrence(id)
    expected["id"] = id

    assert response == expected


def test_successful_get_all_request_should_return_correct_data(
    client: FlaskClient, admin_headers: dict[str, str]
):
    response = json.loads(
        client.get(f"/api/{VER}/occurrence", headers=admin_headers).data
    )
    expected = get_occurrence("all")
    for i, expected_row in enumerate(expected):
        expected_row["id"] = i + 1

    assert response == expected
