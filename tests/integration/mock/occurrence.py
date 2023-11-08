from typing import Literal

from api.schema import OccurrenceSchema
from tests.integration.mock.common import insert_fake_data


def generate_fake_occurrences():
    data = get_occurrence("all")
    schema = OccurrenceSchema()
    insert_fake_data(schema, data)


def get_occurrence(occurrence_id: int | Literal["all"] = "all") -> dict | list[dict]:
    occurrences = [
        {
            "patient_id": 1,
            "healthcare_professional_id": 1,
            "was_emergency": False,
            "datetime": "2023-10-15T09:00:00",
            "notes": "Regular check-up appointment.",
        },
        {
            "patient_id": 2,
            "healthcare_professional_id": 2,
            "was_emergency": False,
            "datetime": "2023-10-16T14:30:00",
            "notes": "Discussion of treatment options.",
        },
        {
            "patient_id": 3,
            "healthcare_professional_id": 3,
            "was_emergency": True,
            "datetime": "2023-10-17T17:45:00",
            "notes": "Emergency response for severe pain.",
        },
        {
            "patient_id": 4,
            "healthcare_professional_id": 4,
            "was_emergency": False,
            "datetime": "2023-10-18T11:15:00",
            "notes": "Follow-up appointment for surgery recovery.",
        },
        {
            "patient_id": 5,
            "healthcare_professional_id": 5,
            "was_emergency": False,
            "datetime": "2023-10-19T10:30:00",
            "notes": "Consultation for ongoing treatment plan.",
        },
    ]

    if occurrence_id == "all":
        return occurrences

    return occurrences[occurrence_id - 1]
