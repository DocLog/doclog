from typing import Literal

from api.schema import MedicineSchema
from tests.integration.mock.common import insert_fake_data


def generate_fake_medicines():
    data = get_medicine("all")
    schema = MedicineSchema()
    insert_fake_data(schema, data)


def get_medicine(medicine_id: int | Literal["all"] = "all") -> dict | list[dict]:
    medicines = [
        {
            "name": "Aspirin",
            "description": "Common pain reliever and anti-inflammatory drug.",
            "dosage": 500.0,
            "dosage_unit": "mg",
        },
        {
            "name": "Ibuprofen",
            "description": "Nonsteroidal anti-inflammatory drug (NSAID).",
            "dosage": 200.0,
            "dosage_unit": "mg",
        },
        {
            "name": "Amoxicillin",
            "description": "Antibiotic used to treat bacterial infections.",
            "dosage": 500.0,
            "dosage_unit": "mg",
        },
        {
            "name": "Paracetamol",
            "description": "Common pain reliever and fever reducer.",
            "dosage": 1000.0,
            "dosage_unit": "mg",
        },
        {
            "name": "Lisinopril",
            "description": "Angiotensin-converting enzyme (ACE) inhibitor used for hypertension.",
            "dosage": 10.0,
            "dosage_unit": "mg",
        },
    ]

    if medicine_id == "all":
        return medicines

    return medicines[medicine_id - 1]
