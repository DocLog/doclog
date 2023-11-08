from typing import Literal

from api.schema import UserSchema
from tests.integration.mock.common import insert_fake_data


def generate_fake_users():
    data = get_user("all")
    schema = UserSchema()
    insert_fake_data(schema, data)


def get_user(user_id: int | Literal["all"] = "all") -> dict | list[dict]:
    users = [
        {
            "id": 1,
            "name": "sysadmin",
            "email": "admin@system.com",
            "password": "adm",
            "role_id": 1,
        },
        {
            "id": 2,
            "name": "carlos_santos",
            "email": "carlos@example.com",
            "password": "password123",
            "role_id": 2,
            "healthcare_professional_id": 1,
        },
        {
            "id": 3,
            "name": "luisa_silva",
            "email": "luisa@example.com",
            "password": "password456",
            "role_id": 2,
            "healthcare_professional_id": 2,
        },
        {
            "id": 4,
            "name": "fernando_oliveira",
            "email": "fernando@example.com",
            "password": "password789",
            "role_id": 2,
            "healthcare_professional_id": 3,
        },
        {
            "id": 5,
            "name": "ana_garcia",
            "email": "ana@example.com",
            "password": "password101112",
            "role_id": 2,
            "healthcare_professional_id": 4,
        },
        {
            "id": 6,
            "name": "roberto_martins",
            "email": "roberto@example.com",
            "password": "password131415",
            "role_id": 2,
            "healthcare_professional_id": 5,
        },
        {
            "id": 7,
            "name": "joao_silva",
            "email": "joao@example.com",
            "password": "password123",
            "patient_id": 1,
            "role_id": 3,
        },
        {
            "id": 8,
            "name": "maria_santos",
            "email": "maria@example.com",
            "password": "password456",
            "patient_id": 2,
            "role_id": 3,
        },
        {
            "id": 9,
            "name": "lucas_ferreira",
            "email": "lucas@example.com",
            "password": "password789",
            "patient_id": 3,
            "role_id": 3,
        },
        {
            "id": 10,
            "name": "isabela_oliveira",
            "email": "isabela@example.com",
            "password": "password101112",
            "patient_id": 4,
            "role_id": 3,
        },
        {
            "id": 11,
            "name": "miguel_goncalves",
            "email": "miguel@example.com",
            "password": "password131415",
            "patient_id": 5,
            "role_id": 3,
        },
    ]

    if user_id == "all":
        return users

    return users[user_id - 1]
