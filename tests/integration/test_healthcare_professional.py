import pytest
from flask.testing import FlaskClient

from api import VER
from tests.common import get_test_parameters
from tests.integration.mock import get_healthcare_professional


@pytest.mark.parametrize("name", get_test_parameters("empty_texts"))
def test_cannot_process_post_request_with_empty_name(
    client: FlaskClient,
    admin_headers: dict[str, str],
    new_healthcare_professional_data: dict,
    name: str,
):
    new_healthcare_professional_data["name"] = name
    response = client.post(
        f"/api/{VER}/healthcare-professional",
        headers=admin_headers,
        json=new_healthcare_professional_data,
    )

    assert response.status_code == 422


@pytest.mark.parametrize("name", get_test_parameters("empty_texts"))
def test_cannot_process_put_request_with_empty_name(
    client: FlaskClient,
    admin_headers: dict[str, str],
    new_healthcare_professional_data: dict,
    name: str,
):
    new_healthcare_professional_data["name"] = name
    response = client.put(
        f"/api/{VER}/healthcare-professional/1",
        headers=admin_headers,
        json=new_healthcare_professional_data,
    )

    assert response.status_code == 422


@pytest.mark.parametrize("surname", get_test_parameters("empty_texts"))
def test_cannot_process_post_request_with_empty_surname(
    client: FlaskClient,
    admin_headers: dict[str, str],
    new_healthcare_professional_data: dict,
    surname: str,
):
    new_healthcare_professional_data["surname"] = surname
    response = client.post(
        f"/api/{VER}/healthcare-professional",
        headers=admin_headers,
        json=new_healthcare_professional_data,
    )

    assert response.status_code == 422


@pytest.mark.parametrize("surname", get_test_parameters("empty_texts"))
def test_cannot_process_put_request_with_empty_surname(
    client: FlaskClient,
    admin_headers: dict[str, str],
    new_healthcare_professional_data: dict,
    surname: str,
):
    new_healthcare_professional_data["surname"] = surname
    response = client.put(
        f"/api/{VER}/healthcare-professional/1",
        headers=admin_headers,
        json=new_healthcare_professional_data,
    )

    assert response.status_code == 422


@pytest.mark.parametrize("cpf", get_test_parameters("invalid_cpfs"))
def test_cannot_process_post_request_with_invalid_cpf(
    client: FlaskClient,
    admin_headers: dict,
    new_healthcare_professional_data: dict,
    cpf: str,
):
    new_healthcare_professional_data["cpf"] = cpf
    response = client.post(
        f"/api/{VER}/healthcare-professional",
        headers=admin_headers,
        json=new_healthcare_professional_data,
    )

    assert response.status_code == 422


@pytest.mark.parametrize("cpf", get_test_parameters("invalid_cpfs"))
def test_cannot_process_put_request_with_invalid_cpf(
    client: FlaskClient,
    admin_headers: dict,
    new_healthcare_professional_data: dict,
    cpf: str,
):
    new_healthcare_professional_data["cpf"] = cpf
    response = client.put(
        f"/api/{VER}/healthcare-professional/1",
        headers=admin_headers,
        json=new_healthcare_professional_data,
    )

    assert response.status_code == 422


@pytest.mark.parametrize("recorded_example", get_healthcare_professional("all"))
def test_cannot_process_post_request_with_non_unique_cpf(
    client: FlaskClient,
    admin_headers: dict,
    new_healthcare_professional_data: dict,
    recorded_example: dict,
):
    new_healthcare_professional_data["cpf"] = recorded_example["cpf"]
    response = client.post(
        f"/api/{VER}/healthcare-professional",
        headers=admin_headers,
        json=new_healthcare_professional_data,
    )

    assert response.status_code == 422


@pytest.mark.parametrize("recorded_example", get_healthcare_professional("all"))
def test_cannot_process_put_request_with_non_unique_cpf(
    client: FlaskClient,
    admin_headers: dict,
    new_healthcare_professional_data: dict,
    recorded_example: dict,
):
    new_healthcare_professional_data["cpf"] = recorded_example["cpf"]
    response = client.put(
        f"/api/{VER}/healthcare-professional/1",
        headers=admin_headers,
        json=new_healthcare_professional_data,
    )

    assert response.status_code == 422


@pytest.mark.parametrize("recorded_example", get_healthcare_professional("all"))
def test_cannot_process_post_request_with_non_unique_crm(
    client: FlaskClient,
    admin_headers: dict,
    new_healthcare_professional_data: dict,
    recorded_example: dict,
):
    new_healthcare_professional_data["crm"] = recorded_example["crm"]
    response = client.post(
        f"/api/{VER}/healthcare-professional",
        headers=admin_headers,
        json=new_healthcare_professional_data,
    )

    assert response.status_code == 422


@pytest.mark.parametrize("recorded_example", get_healthcare_professional("all"))
def test_cannot_process_put_request_with_non_unique_crm(
    client: FlaskClient,
    admin_headers: dict,
    new_healthcare_professional_data: dict,
    recorded_example: dict,
):
    new_healthcare_professional_data["crm"] = recorded_example["crm"]
    response = client.put(
        f"/api/{VER}/healthcare-professional/1",
        headers=admin_headers,
        json=new_healthcare_professional_data,
    )

    assert response.status_code == 422


@pytest.mark.parametrize("crm", get_test_parameters("invalid_crms"))
def test_cannot_process_post_request_with_invalid_crm(
    client: FlaskClient,
    admin_headers: dict,
    new_healthcare_professional_data: dict,
    crm: str,
):
    new_healthcare_professional_data["crm"] = crm
    response = client.post(
        f"/api/{VER}/healthcare-professional",
        headers=admin_headers,
        json=new_healthcare_professional_data,
    )

    assert response.status_code == 422


@pytest.mark.parametrize("crm", get_test_parameters("invalid_crms"))
def test_cannot_process_put_request_with_invalid_crm(
    client: FlaskClient,
    admin_headers: dict,
    new_healthcare_professional_data: dict,
    crm: str,
):
    new_healthcare_professional_data["crm"] = crm
    response = client.put(
        f"/api/{VER}/healthcare-professional/1",
        headers=admin_headers,
        json=new_healthcare_professional_data,
    )

    assert response.status_code == 422


@pytest.mark.parametrize("birth_date", get_test_parameters("future_dates"))
def test_cannot_process_post_request_with_invalid_birth_date(
    client: FlaskClient,
    admin_headers: dict,
    new_healthcare_professional_data: dict,
    birth_date: str,
):
    new_healthcare_professional_data["birth_date"] = birth_date
    response = client.post(
        f"/api/{VER}/healthcare-professional",
        headers=admin_headers,
        json=new_healthcare_professional_data,
    )

    assert response.status_code == 422


@pytest.mark.parametrize("birth_date", get_test_parameters("future_dates"))
def test_cannot_process_put_request_with_invalid_birth_date(
    client: FlaskClient,
    admin_headers: dict,
    new_healthcare_professional_data: dict,
    birth_date: str,
):
    new_healthcare_professional_data["birth_date"] = birth_date
    response = client.put(
        f"/api/{VER}/healthcare-professional/1",
        headers=admin_headers,
        json=new_healthcare_professional_data,
    )

    assert response.status_code == 422


def test_successfully_process_post_request_with_valid_data(
    client: FlaskClient, admin_headers: dict, new_healthcare_professional_data: dict
):
    response = client.post(
        f"/api/{VER}/healthcare-professional",
        headers=admin_headers,
        json=new_healthcare_professional_data,
    )

    assert response.status_code == 201


def test_successfully_process_put_request_with_valid_data(
    client: FlaskClient, admin_headers: dict, new_healthcare_professional_data: dict
):
    response = client.put(
        f"/api/{VER}/healthcare-professional/1",
        headers=admin_headers,
        json=new_healthcare_professional_data,
    )

    assert response.status_code == 201
