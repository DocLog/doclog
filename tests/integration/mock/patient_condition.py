from typing import Literal

from api.schema import PatientConditionSchema
from tests.integration.mock.common import insert_fake_data


def generate_fake_patient_conditions():
    data = get_patient_condition("all")
    schema = PatientConditionSchema()
    insert_fake_data(schema, data)


def get_patient_condition(
    patient_condition_id: int | Literal["all"] = "all",
) -> dict | list[dict]:
    patient_conditions = [
        {
            "patient_id": 1,
            "condition_id": 1,
        },
        {
            "patient_id": 2,
            "condition_id": 2,
            "notes": "",
        },
        {
            "patient_id": 3,
            "condition_id": 3,
            "notes": "Patient diagnosed with asthma.",
        },
        {
            "patient_id": 4,
            "condition_id": 4,
            "notes": "Patient diagnosed with arthritis.",
        },
        {
            "patient_id": 5,
            "condition_id": 5,
            "notes": "Patient diagnosed with migraines.",
        },
    ]

    if patient_condition_id == "all":
        return patient_conditions

    return patient_conditions[patient_condition_id - 1]
