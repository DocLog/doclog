import re
from datetime import date, datetime

from sqlalchemy import Column

from ..common import db
from ..exceptions import (
    EmptyTextFieldError,
    FutureDateError,
    InvalidBloodTypeError,
    InvalidCPFError,
    InvalidCRMError,
    InvalidEmailError,
    NegativeOrZeroValueError,
    ReferencedKeyNotFoundError,
    UniquenessViolationError,
)

# database related


def value_exists(field: Column, value):
    """
    Check if a specific value exists in a given database column.

    This function queries the database to check whether a given value exists in a specified
    database column. It returns True if the value is found and False otherwise.

    Args:
        field (Column): The SQLAlchemy column to check for the value.
        value: The value to search for in the column.

    Returns:
        bool: True if the value exists, False if it does not.
    """

    return db.session.query(field).where(field == value).first() is not None


def validate_unique_value(field: Column, value):
    """
    Validate that a value is unique within a given database column.

    This function checks whether a value is unique within a specified database column.
    If the value is not unique, it raises a ValidationError indicating that the value is already
    recorded in the database.

    Args:
        field (Column): The SQLAlchemy column to check for the uniqueness of the value.
        value: The value to validate for uniqueness.

    Raises:
        UniquenessViolationError: If the value is not unique in the specified column.
    """

    if value_exists(field, value):
        raise UniquenessViolationError()


def validate_foreign_key(fk_field: Column, fk_value):
    """
    Validate the existence of a referenced foreign key in a database column.

    This function checks whether a referenced foreign key exists in the specified
    database column. If it does not exist, it raises a `ReferencedKeyNotFoundError`
    indicating that the referenced foreign key is not found in the database.

    Args:
        fk_field (Column): The SQLAlchemy column representing the foreign key reference.
        fk_value: The value of the foreign key to validate.

    Raises:
        ReferencedKeyNotFoundError: If the referenced foreign key does not exist
        in the specified column.
    """

    fk_exists = value_exists(fk_field, fk_value)
    if not fk_exists:
        raise ReferencedKeyNotFoundError()


# data consistency


def validate_required_text_field(field_value: str):
    """
    Validate that a text field is not empty or contains only whitespace characters.

    This function checks whether a text field contains non-empty content. If the
    field is empty or consists of only whitespace characters, it raises an EmptyTextFieldError.

    Args:
        field_value (str): The value of the text field to validate.

    Raises:
        EmptyTextFieldError: If the field is empty or contains only whitespace characters.
    """

    if re.match(r"^\s*$", field_value) is not None:
        raise EmptyTextFieldError()


def validate_cpf(cpf: str):
    """
    Validate the format and correctness of a Brazilian CPF (Individual Taxpayer Registry) number.

    This function checks whether a CPF is in the correct format and validates its correctness
    using the calculation of verification digits. If the CPF is not in the correct format or
    is invalid, it raises an InvalidCPFError.

    Args:
        cpf (str): The CPF number to validate.

    Raises:
        InvalidCPFError: If the CPF is not in the correct format or is invalid.
    """

    if not re.match(r"^[0-9]{11}$", cpf):
        # checks if CPF fits into the right format
        raise InvalidCPFError("Incorrect CPF format.")

    if len(cpf.replace(cpf[0], "")) == 0:
        raise InvalidCPFError("Not a valid CPF.")

    mirror_cpf = cpf[:9]

    first_digit = sum((10 - i) * int(digit) for i, digit in enumerate(mirror_cpf)) % 11
    if first_digit < 2:
        first_digit = 0
    else:
        first_digit = 11 - first_digit

    mirror_cpf += str(first_digit)

    second_digit = sum((11 - i) * int(digit) for i, digit in enumerate(mirror_cpf)) % 11
    if second_digit < 2:
        second_digit = 0
    else:
        second_digit = 11 - second_digit

    mirror_cpf += str(second_digit)

    if mirror_cpf != cpf:
        raise InvalidCPFError()


def validate_crm(crm: str):
    """
    Validate the format and state code of a Brazilian CRM (Medical Council Registration) number.

    This function checks whether a CRM is in the correct format and validates its state code
    against a list of Brazilian states. If the CRM is not in the correct format or the state code
    is invalid, it raises an InvalidCRMError.

    Args:
        crm (str): The CRM number to validate.

    Raises:
        InvalidCRMError: If the CRM is not in the correct format or the state code is invalid.
    """

    if not re.match(r"^CRM/[A-Z]{2} [0-9]{6}$", crm):
        raise InvalidCRMError("Invalid CRM format.")

    brazilian_states = {
        "AC",
        "AL",
        "AP",
        "AM",
        "BA",
        "CE",
        "DF",
        "ES",
        "GO",
        "MA",
        "MT",
        "MS",
        "MG",
        "PA",
        "PB",
        "PR",
        "PE",
        "PI",
        "RJ",
        "RN",
        "RS",
        "RO",
        "RR",
        "SC",
        "SP",
        "SE",
        "TO",
    }

    crm_state = crm[4:6]

    if crm_state not in brazilian_states:
        raise InvalidCRMError()


def validate_non_future_datetime(date_value: date | datetime):
    """
    Validate that a date or datetime value is not in the future.

    This function checks if the provided date or datetime value is not a date in
    the future. It raises a `FutureDateError` if the provided date is in the future.

    Args:
        date_value (date | datetime): A date or datetime value to validate.

    Raises:
        FutureDateError: If the provided date or datetime is in the future.
    """
    if isinstance(date_value, date):
        date_value = datetime(
            year=date_value.year, month=date_value.month, day=date_value.day
        )

    if datetime.now() < date_value:
        raise FutureDateError()


def validate_positive_value(value: int | float):
    """
    Validate that a value is positive (higher than 0).

    This function checks if the provided value is a positive integer or float. It
    raises a `NegativeOrZeroValueError` if the value is less than or equal to 0.

    Args:
        value (int | float): The value to validate.

    Raises:
        NegativeOrZeroValueError: If the provided value is not positive (<= 0).
    """
    if value <= 0:
        raise NegativeOrZeroValueError("Value should be higher than 0.")


def validate_blood_type(blood_type: str):
    """
    Validate a blood type string.

    This function checks if the provided blood type string is valid according to the
    common ABO and RhD blood type system. The expected format is "A+", "B-", "AB+",
    "O-", or similar, where 'A', 'B', 'AB', or 'O' represent the ABO blood group
    and '+' or '-' represents the RhD factor. It raises an `InvalidBloodTypeError`
    if the provided blood type does not match the expected format.

    Args:
        blood_type (str): The blood type string to validate.

    Raises:
        InvalidBloodTypeError: If the provided blood type is not in the expected
        format.
    """
    if not re.match(r"^(AB|B|A|O)[+-]$", blood_type):
        raise InvalidBloodTypeError("Invalid blood type.")


def validate_email(email: str):
    """
    Validate an email address.

    This function checks if the provided email address is a valid email format.
    It uses a basic regular expression to verify that the email address follows
    the pattern of "local_part@domain". It raises an `InvalidEmailError` if the
    provided email address is not in the expected format.

    Args:
        email (str): The email address to validate.

    Raises:
        InvalidEmailError: If the provided email address is not in the expected
        format.
    """
    if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
        raise InvalidEmailError("Invalid email.")
