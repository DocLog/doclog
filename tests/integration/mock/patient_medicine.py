from typing import Literal

from api.schema import PatientMedicineSchema
from tests.integration.mock.common import insert_fake_data


def generate_fake_patient_medicines():
    data = get_patient_medicine("all")
    schema = PatientMedicineSchema()
    insert_fake_data(schema, data)


def get_patient_medicine(
    patient_medicine_id: int | Literal["all"] = "all",
) -> dict | list[dict]:
    patient_medicines = [
        {
            "patient_id": 1,
            "medicine_id": 1,
        },
        {
            "patient_id": 2,
            "medicine_id": 2,
            "notes": "",
        },
        {
            "patient_id": 3,
            "medicine_id": 3,
            "notes": "Prescribed Amoxicillin for infection treatment.",
        },
        {
            "patient_id": 4,
            "medicine_id": 4,
            "notes": "Prescribed Paracetamol for fever relief.",
        },
        {
            "patient_id": 5,
            "medicine_id": 5,
            "notes": "Prescribed Lisinopril for hypertension management.",
        },
    ]

    if patient_medicine_id == "all":
        return patient_medicines

    return patient_medicines[patient_medicine_id - 1]
