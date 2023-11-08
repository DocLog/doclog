from datetime import datetime

import pytest
from flask import Flask
from sqlalchemy import Column

from api.exceptions import ReferencedKeyNotFoundError, UniquenessViolationError
from api.model import (
    ConditionModel,
    MedicineModel,
    OccurrenceModel,
    PatientConditionModel,
    PatientModel,
    UserModel,
)
from api.schema.validation import (
    validate_foreign_key,
    validate_unique_value,
    value_exists,
)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        (UserModel.name, "sysadmin"),
        (PatientModel.register_date, datetime(2023, 3, 5, 10, 15)),
        (PatientModel.birth_date, "1995-11-10"),
        (OccurrenceModel.was_emergency, True),
        (MedicineModel.dosage, 500.0),
        (ConditionModel.id, 2),
    ],
)
def test_should_return_true_when_value_exists_in_the_database(
    app: Flask, field: Column, value
):
    with app.app_context():
        assert value_exists(field, value) is True


@pytest.mark.parametrize(
    ("field", "value"),
    [
        (UserModel.name, "Gabriel"),
        (PatientModel.register_date, datetime(2034, 1, 1)),
        (MedicineModel.dosage, -400),
    ],
)
def test_should_return_false_when_value_does_not_exist_in_the_database(
    app: Flask, field: Column, value
):
    with app.app_context():
        assert value_exists(field, value) is False


@pytest.mark.parametrize(
    ("field", "value"),
    [
        (UserModel.name, "sysadmin"),
        (PatientModel.register_date, datetime(2023, 3, 5, 10, 15)),
        (PatientModel.birth_date, "1995-11-10"),
        (OccurrenceModel.was_emergency, True),
        (MedicineModel.dosage, 500.0),
        (ConditionModel.id, 2),
    ],
)
def test_should_raise_exception_when_the_value_already_exists_in_the_database(
    app: Flask, field: Column, value
):
    with app.app_context(), pytest.raises(UniquenessViolationError):
        validate_unique_value(field, value)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        (UserModel.name, "Gabriel"),
        (PatientModel.register_date, datetime(2034, 1, 1)),
        (MedicineModel.dosage, -400),
    ],
)
def test_should_not_raise_exception_when_the_value_does_not_exist_in_the_database(
    app: Flask, field: Column, value
):
    try:
        with app.app_context():
            validate_unique_value(field, value)
    except UniquenessViolationError:
        assert False


@pytest.mark.parametrize(
    ("fk_field", "fk_value"),
    [
        (OccurrenceModel.patient_id, 200),
        (OccurrenceModel.healthcare_professional_id, 150),
        (PatientConditionModel.patient_id, 60),
        (UserModel.role_id, 0),
    ],
)
def test_should_raise_exception_when_referenced_key_does_not_exist(
    app: Flask, fk_field: Column, fk_value
):
    with app.app_context(), pytest.raises(ReferencedKeyNotFoundError):
        validate_foreign_key(fk_field, fk_value)


@pytest.mark.parametrize(
    ("fk_field", "fk_value"),
    [
        (UserModel.patient_id, 2),
        (PatientConditionModel.condition_id, 3),
        (OccurrenceModel.healthcare_professional_id, 5),
    ],
)
def test_should_not_raise_exception_when_referenced_key_exists(
    app: Flask, fk_field: Column, fk_value
):
    try:
        with app.app_context():
            validate_foreign_key(fk_field, fk_value)
    except ReferencedKeyNotFoundError:
        assert False
