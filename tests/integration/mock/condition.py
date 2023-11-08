from typing import Literal

from api.schema import ConditionSchema
from tests.integration.mock.common import insert_fake_data


def generate_fake_conditions():
    data = get_condition("all")
    schema = ConditionSchema()
    insert_fake_data(schema, data)


def get_condition(condition_id: int | Literal["all"] = "all") -> dict | list[dict]:
    conditions = [
        {
            "name": "Hypertension",
            "description": "A common medical condition characterized by high blood pressure.",
        },
        {
            "name": "Diabetes",
            "description": "A chronic condition that affects how your body processes glucose (blood sugar).",
        },
        {
            "name": "Asthma",
            "description": "A respiratory condition that can cause breathing difficulties and wheezing.",
        },
        {
            "name": "Arthritis",
            "description": "Inflammation and swelling of the joints, leading to pain and stiffness.",
        },
        {
            "name": "Migraine",
            "description": "A type of headache characterized by severe pain, often accompanied by nausea and sensitivity to light and sound.",
        },
    ]

    if condition_id == "all":
        return conditions

    return conditions[condition_id - 1]
