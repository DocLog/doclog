from typing import Literal

from api.schema import PatientSchema
from tests.integration.mock.common import insert_fake_data


def generate_fake_patients():
    data = get_patient("all")
    schema = PatientSchema()
    insert_fake_data(schema, data)


def get_patient(patient_id: int | Literal["all"] = "all") -> dict | list[dict]:
    patients = [
        {
            "id": 1,
            "name": "João",
            "surname": "Silva",
            "cpf": "41561355003",
            "birth_date": "1990-01-15",
            "register_date": "2023-01-20T08:30:00",
            "blood_type": "A+",
            "notes": "Paciente sem observações específicas.",
        },
        {
            "id": 2,
            "name": "Maria",
            "surname": "Santos",
            "cpf": "53109160080",
            "birth_date": "1985-05-02",
            "register_date": "2023-02-10T14:45:00",
            "blood_type": "B-",
            "notes": "Alergia a penicilina.",
        },
        {
            "id": 3,
            "name": "Lucas",
            "surname": "Ferreira",
            "cpf": "70700978089",
            "birth_date": "1988-09-22",
            "register_date": "2023-03-05T10:15:00",
            "blood_type": "O+",
            "notes": "Histórico de doença cardíaca.",
        },
        {
            "id": 4,
            "name": "Isabela",
            "surname": "Oliveira",
            "cpf": "11152995065",
            "birth_date": "1975-04-30",
            "register_date": "2023-04-15T09:00:00",
            "blood_type": "AB-",
            "notes": "Necessita de medicação regular para hipertensão.",
        },
        {
            "id": 5,
            "name": "Miguel",
            "surname": "Gonçalves",
            "cpf": "24882486067",
            "birth_date": "1995-11-10",
            "register_date": "2023-05-20T16:30:00",
            "blood_type": "A-",
            "notes": "Sem condições médicas conhecidas.",
        },
    ]

    if patient_id == "all":
        return patients

    return patients[patient_id - 1]
