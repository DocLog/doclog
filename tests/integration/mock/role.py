from typing import Literal

from api.schema import RoleSchema
from tests.integration.mock.common import insert_fake_data


def generate_fake_roles():
    data = get_role("all")
    schema = RoleSchema()
    insert_fake_data(schema, data)


def get_role(role_id: int | Literal["all"] = "all") -> dict | list[dict]:
    roles = [
        {
            "id": 1,
            "name": "Admin",
            "description": "System Administrator",
        },
        {
            "id": 2,
            "name": "Professional",
            "description": "Healthcare Professional",
        },
        {
            "id": 3,
            "name": "Patient",
            "description": "Patient",
        },
    ]

    if role_id == "all":
        return roles

    return roles[role_id - 1]
