from datetime import date, datetime

import pytest

from api.exceptions import (
    EmptyTextFieldError,
    FutureDateError,
    InvalidBloodTypeError,
    InvalidCPFError,
    InvalidCRMError,
    InvalidEmailError,
    NegativeOrZeroValueError,
)
from api.schema.validation import (
    validate_blood_type,
    validate_cpf,
    validate_crm,
    validate_email,
    validate_non_future_datetime,
    validate_positive_value,
    validate_required_text_field,
)
from tests.common import get_test_parameters


@pytest.mark.parametrize("text_value", get_test_parameters("empty_texts"))
def test_should_raise_exception_when_text_field_is_empty(text_value: str):
    with pytest.raises(EmptyTextFieldError):
        validate_required_text_field(text_value)


@pytest.mark.parametrize("cpf", get_test_parameters("invalid_cpfs"))
def test_should_raise_exception_when_cpf_is_invalid(cpf: str):
    with pytest.raises(InvalidCPFError):
        validate_cpf(cpf)


@pytest.mark.parametrize("crm", get_test_parameters("invalid_crms"))
def test_should_raise_exception_when_crm_is_invalid(crm: str):
    with pytest.raises(InvalidCRMError):
        validate_crm(crm)


@pytest.mark.parametrize("date_value", get_test_parameters("future_dates"))
def test_should_raise_exception_when_date_is_in_the_future(date_value: datetime | date):
    with pytest.raises(FutureDateError):
        validate_non_future_datetime(date_value)


@pytest.mark.parametrize("value", get_test_parameters("non_positive_values"))
def test_should_raise_exception_when_value_is_not_positive(value: int | float):
    with pytest.raises(NegativeOrZeroValueError):
        validate_positive_value(value)


@pytest.mark.parametrize("blood_type", get_test_parameters("invalid_blood_types"))
def test_should_raise_exception_when_the_blood_type_is_invalid(blood_type: str):
    with pytest.raises(InvalidBloodTypeError):
        validate_blood_type(blood_type)


@pytest.mark.parametrize("email", get_test_parameters("invalid_emails"))
def test_should_raise_exception_when_email_is_invalid(email: str):
    with pytest.raises(InvalidEmailError):
        validate_email(email)


@pytest.mark.parametrize("text_value", get_test_parameters("filled_texts"))
def test_should_not_raise_exception_when_text_field_is_not_empty(text_value: str):
    try:
        validate_required_text_field(text_value)
    except EmptyTextFieldError as e:
        assert False, f"{text_value} raised {e}."


@pytest.mark.parametrize("cpf", get_test_parameters("valid_cpfs"))
def test_should_not_raise_exception_when_cpf_is_valid(cpf: str):
    try:
        validate_cpf(cpf)
    except InvalidCPFError as e:
        assert False, f"{cpf} raised {e}."


@pytest.mark.parametrize("crm", get_test_parameters("valid_crms"))
def test_should_not_raise_exception_when_crm_is_valid(crm: str):
    try:
        validate_crm(crm)
    except InvalidCRMError as e:
        assert False, f"{crm} raised {e}."


@pytest.mark.parametrize("date_value", get_test_parameters("past_dates"))
def test_should_not_raise_exception_when_date_is_not_in_the_future(
    date_value: date | datetime,
):
    try:
        validate_non_future_datetime(date_value)
    except FutureDateError as e:
        assert False, f"{date_value} raised {e}."


@pytest.mark.parametrize("value", get_test_parameters("positive_values"))
def test_should_not_raise_exception_when_value_is_positive(value: int | float):
    try:
        validate_positive_value(value)
    except NegativeOrZeroValueError as e:
        assert False, f"{value} raised {e}."


@pytest.mark.parametrize("blood_type", get_test_parameters("valid_blood_types"))
def test_should_not_raise_exception_when_blood_type_is_valid(blood_type: str):
    try:
        validate_blood_type(blood_type)
    except InvalidBloodTypeError as e:
        assert False, f"{blood_type} raised {e}."


@pytest.mark.parametrize("email", get_test_parameters("valid_emails"))
def test_should_not_raise_exception_when_email_is_valid(email: str):
    try:
        validate_email(email)
    except InvalidEmailError as e:
        assert False, f"{email} raised {e}."
