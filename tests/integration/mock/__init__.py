from .condition import generate_fake_conditions, get_condition
from .healthcare_professional import (
    generate_fake_healthcare_professionals,
    get_healthcare_professional,
)
from .medicine import generate_fake_medicines, get_medicine
from .occurrence import generate_fake_occurrences, get_occurrence
from .patient import generate_fake_patients, get_patient
from .patient_condition import generate_fake_patient_conditions, get_patient_condition
from .patient_medicine import generate_fake_patient_medicines, get_patient_medicine
from .role import generate_fake_roles, get_role
from .user import generate_fake_users, get_user


def generate_fake_data():
    generate_fake_roles()
    generate_fake_patients()
    generate_fake_healthcare_professionals()
    generate_fake_users()
    generate_fake_conditions()
    generate_fake_medicines()
    generate_fake_occurrences()
    generate_fake_patient_conditions()
    generate_fake_patient_medicines()
