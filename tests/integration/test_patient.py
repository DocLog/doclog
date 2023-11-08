import json

import pytest
from flask.testing import FlaskClient

from api import VER
from tests.common import get_test_parameters
from tests.integration.mock import get_patient


@pytest.mark.parametrize("name", get_test_parameters("empty_texts"))
def test_cannot_process_post_request_with_empty_name(
    client: FlaskClient,
    admin_headers: dict[str, str],
    new_patient_data: dict,
    name: str,
):
    new_patient_data["name"] = name
    response = client.post(
        f"/api/{VER}/patient", headers=admin_headers, json=new_patient_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("name", get_test_parameters("empty_texts"))
def test_cannot_process_put_request_with_empty_name(
    client: FlaskClient,
    admin_headers: dict[str, str],
    new_patient_data: dict,
    name: str,
):
    new_patient_data["name"] = name
    response = client.put(
        f"/api/{VER}/patient/1", headers=admin_headers, json=new_patient_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("surname", get_test_parameters("empty_texts"))
def test_cannot_process_post_request_with_empty_surname(
    client: FlaskClient,
    admin_headers: dict[str, str],
    new_patient_data: dict,
    surname: str,
):
    new_patient_data["surname"] = surname
    response = client.post(
        f"/api/{VER}/patient", headers=admin_headers, json=new_patient_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("surname", get_test_parameters("empty_texts"))
def test_cannot_process_put_request_with_empty_surname(
    client: FlaskClient,
    admin_headers: dict[str, str],
    new_patient_data: dict,
    surname: str,
):
    new_patient_data["surname"] = surname
    response = client.put(
        f"/api/{VER}/patient/1", headers=admin_headers, json=new_patient_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("cpf", get_test_parameters("invalid_cpfs"))
def test_cannot_process_post_request_with_invalid_cpf(
    client: FlaskClient, admin_headers: dict, new_patient_data: dict, cpf: str
):
    new_patient_data["cpf"] = cpf
    response = client.post(
        f"/api/{VER}/patient", headers=admin_headers, json=new_patient_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("cpf", get_test_parameters("invalid_cpfs"))
def test_cannot_process_put_request_with_invalid_cpf(
    client: FlaskClient, admin_headers: dict, new_patient_data: dict, cpf: str
):
    new_patient_data["cpf"] = cpf
    response = client.put(
        f"/api/{VER}/patient/1", headers=admin_headers, json=new_patient_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("recorded_example", get_patient("all"))
def test_cannot_process_post_request_with_non_unique_cpf(
    client: FlaskClient,
    admin_headers: dict,
    new_patient_data: dict,
    recorded_example: dict,
):
    new_patient_data["cpf"] = recorded_example["cpf"]
    response = client.post(
        f"/api/{VER}/patient", headers=admin_headers, json=new_patient_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("recorded_example", get_patient("all"))
def test_cannot_process_put_request_with_non_unique_cpf(
    client: FlaskClient,
    admin_headers: dict,
    new_patient_data: dict,
    recorded_example: dict,
):
    new_patient_data["cpf"] = recorded_example["cpf"]
    response = client.put(
        f"/api/{VER}/patient/1", headers=admin_headers, json=new_patient_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("crm", get_test_parameters("invalid_crms"))
def test_cannot_process_post_request_with_invalid_crm(
    client: FlaskClient, admin_headers: dict, new_patient_data: dict, crm: str
):
    new_patient_data["crm"] = crm
    response = client.post(
        f"/api/{VER}/patient", headers=admin_headers, json=new_patient_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("crm", get_test_parameters("invalid_crms"))
def test_cannot_process_put_request_with_invalid_crm(
    client: FlaskClient, admin_headers: dict, new_patient_data: dict, crm: str
):
    new_patient_data["crm"] = crm
    response = client.put(
        f"/api/{VER}/patient/1", headers=admin_headers, json=new_patient_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("birth_date", get_test_parameters("future_dates"))
def test_cannot_process_post_request_with_invalid_birth_date(
    client: FlaskClient, admin_headers: dict, new_patient_data: dict, birth_date: str
):
    new_patient_data["birth_date"] = birth_date
    response = client.post(
        f"/api/{VER}/patient", headers=admin_headers, json=new_patient_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("birth_date", get_test_parameters("future_dates"))
def test_cannot_process_put_request_with_invalid_birth_date(
    client: FlaskClient, admin_headers: dict, new_patient_data: dict, birth_date: str
):
    new_patient_data["birth_date"] = birth_date
    response = client.put(
        f"/api/{VER}/patient/1", headers=admin_headers, json=new_patient_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("register_date", get_test_parameters("future_dates"))
def test_cannot_process_post_request_with_invalid_register_date(
    client: FlaskClient, admin_headers: dict, new_patient_data: dict, register_date: str
):
    new_patient_data["register_date"] = register_date
    response = client.post(
        f"/api/{VER}/patient", headers=admin_headers, json=new_patient_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("register_date", get_test_parameters("future_dates"))
def test_cannot_process_put_request_with_invalid_register_date(
    client: FlaskClient, admin_headers: dict, new_patient_data: dict, register_date: str
):
    new_patient_data["register_date"] = register_date
    response = client.put(
        f"/api/{VER}/patient/1", headers=admin_headers, json=new_patient_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("blood_type", get_test_parameters("invalid_blood_types"))
def test_cannot_process_post_request_with_invalid_blood_type(
    client: FlaskClient, admin_headers: dict, new_patient_data: dict, blood_type: str
):
    new_patient_data["blood_type"] = blood_type
    response = client.post(
        f"/api/{VER}/patient", headers=admin_headers, json=new_patient_data
    )

    assert response.status_code == 422


@pytest.mark.parametrize("blood_type", get_test_parameters("invalid_blood_types"))
def test_cannot_process_put_request_with_invalid_blood_type(
    client: FlaskClient, admin_headers: dict, new_patient_data: dict, blood_type: str
):
    new_patient_data["blood_type"] = blood_type
    response = client.put(
        f"/api/{VER}/patient/1", headers=admin_headers, json=new_patient_data
    )

    assert response.status_code == 422


def test_successfully_process_post_request_with_valid_data(
    client: FlaskClient, admin_headers: dict, new_patient_data: dict
):
    response = client.post(
        f"/api/{VER}/patient", headers=admin_headers, json=new_patient_data
    )

    assert response.status_code == 201


def test_successfully_process_put_request_with_valid_data(
    client: FlaskClient, admin_headers: dict, new_patient_data: dict
):
    response = client.put(
        f"/api/{VER}/patient/1", headers=admin_headers, json=new_patient_data
    )

    assert response.status_code == 201


@pytest.mark.parametrize("id", list(range(1, 6)))
def test_successful_get_by_id_request_should_return_correct_data(
    client: FlaskClient, admin_headers: dict[str, str], id: int
):
    response = json.loads(
        client.get(f"/api/{VER}/patient/{id}", headers=admin_headers).data
    )
    expected = get_patient(id)
    expected["id"] = id

    assert response == expected


def test_successful_get_all_request_should_return_correct_data(
    client: FlaskClient, admin_headers: dict[str, str]
):
    response = json.loads(client.get(f"/api/{VER}/patient", headers=admin_headers).data)
    expected = get_patient("all")
    for i, expected_row in enumerate(expected):
        expected_row["id"] = i + 1

    assert response == expected
