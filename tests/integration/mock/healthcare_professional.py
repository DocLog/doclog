from typing import Literal

from api.schema import HealthcareProfessionalSchema
from tests.integration.mock.common import insert_fake_data


def generate_fake_healthcare_professionals():
    data = get_healthcare_professional("all")
    schema = HealthcareProfessionalSchema()
    insert_fake_data(schema, data)


def get_healthcare_professional(
    healthcare_professional_id: int | Literal["all"] = "all",
) -> dict | list[dict]:
    healthcare_professionals = [
        {
            "id": 1,
            "name": "Carlos",
            "surname": "Santos",
            "cpf": "56016703826",
            "crm": "CRM/SP 123456",
            "birth_date": "1978-04-15",
        },
        {
            "id": 2,
            "name": "Luisa",
            "surname": "Silva",
            "cpf": "94689044902",
            "crm": "CRM/SC 123456",
            "birth_date": "1985-07-20",
        },
        {
            "id": 3,
            "name": "Fernando",
            "surname": "Oliveira",
            "cpf": "54212246864",
            "crm": "CRM/SP 789101",
            "birth_date": "1972-12-30",
        },
        {
            "id": 4,
            "name": "Ana",
            "surname": "Garcia",
            "cpf": "93495739890",
            "crm": "CRM/RR 123456",
            "birth_date": "1980-02-05",
        },
        {
            "id": 5,
            "name": "Roberto",
            "surname": "Martins",
            "cpf": "79037078842",
            "crm": "CRM/BA 123456",
            "birth_date": "1989-09-10",
        },
    ]

    if healthcare_professional_id == "all":
        return healthcare_professionals

    return healthcare_professionals[healthcare_professional_id - 1]
