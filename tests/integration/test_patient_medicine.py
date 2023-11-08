import json

import pytest
from flask.testing import FlaskClient

from api import VER
from tests.integration.mock import get_patient_medicine


def test_cannot_process_post_request_with_unrecorded_patient_id(
    client: FlaskClient, admin_headers: dict, new_patient_medicine_data: dict
):
    new_patient_medicine_data["patient_id"] = 100
    response = client.post(
        f"/api/{VER}/patient-medicine",
        headers=admin_headers,
        json=new_patient_medicine_data,
    )

    assert response.status_code == 422


def test_cannot_process_put_request_with_unrecorded_patient_id(
    client: FlaskClient, admin_headers: dict, new_patient_medicine_data: dict
):
    new_patient_medicine_data["patient_id"] = 100
    response = client.put(
        f"/api/{VER}/patient-medicine/1",
        headers=admin_headers,
        json=new_patient_medicine_data,
    )

    assert response.status_code == 422


def test_cannot_process_post_request_with_unrecorded_medicine_id(
    client: FlaskClient, admin_headers: dict, new_patient_medicine_data: dict
):
    new_patient_medicine_data["medicine_id"] = 100
    response = client.post(
        f"/api/{VER}/patient-medicine",
        headers=admin_headers,
        json=new_patient_medicine_data,
    )

    assert response.status_code == 422


def test_cannot_process_put_request_with_unrecorded_medicine_id(
    client: FlaskClient, admin_headers: dict, new_patient_medicine_data: dict
):
    new_patient_medicine_data["medicine_id"] = 100
    response = client.put(
        f"/api/{VER}/patient-medicine/1",
        headers=admin_headers,
        json=new_patient_medicine_data,
    )

    assert response.status_code == 422


def test_successfully_process_post_request_with_valid_data(
    client: FlaskClient, admin_headers: dict, new_patient_medicine_data: dict
):
    response = client.post(
        f"/api/{VER}/patient-medicine",
        headers=admin_headers,
        json=new_patient_medicine_data,
    )

    assert response.status_code == 201


def test_successfully_process_put_request_with_valid_data(
    client: FlaskClient, admin_headers: dict, new_patient_medicine_data: dict
):
    response = client.put(
        f"/api/{VER}/patient-medicine/1",
        headers=admin_headers,
        json=new_patient_medicine_data,
    )

    assert response.status_code == 201


@pytest.mark.parametrize("id", list(range(1, 6)))
def test_successful_get_by_id_request_should_return_correct_data(
    client: FlaskClient, admin_headers: dict[str, str], id: int
):
    response = json.loads(
        client.get(f"/api/{VER}/patient-medicine/{id}", headers=admin_headers).data
    )
    expected = get_patient_medicine(id)
    expected["id"] = id

    if not "notes" in expected.keys():
        expected["notes"] = None

    assert response == expected


def test_successful_get_all_request_should_return_correct_data(
    client: FlaskClient, admin_headers: dict[str, str]
):
    response = json.loads(
        client.get(f"/api/{VER}/patient-medicine", headers=admin_headers).data
    )
    expected = get_patient_medicine("all")
    for i, expected_row in enumerate(expected):
        expected_row["id"] = i + 1

        if not "notes" in expected_row.keys():
            expected_row["notes"] = None

    assert response == expected
