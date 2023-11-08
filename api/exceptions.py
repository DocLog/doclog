from marshmallow import ValidationError


class InvalidDataFormatError(ValidationError):
    """
    Exception case raised when data comes or gets desserialized incorrectly.
    """

    def __init__(self, message: str = "Incorrect data format"):
        super().__init__(message)


class EmptyTextFieldError(ValidationError):
    """
    Exception case raised when a text field that should not be empty is passed as
    an empty string.
    """

    def __init__(self, message: str = "Missing data for required field."):
        super().__init__(message)


class InvalidCPFError(ValidationError):
    """
    Exception case raised when invalid CPF (Brazilian Taxpayer Registry) numbers
    are passed.
    """

    def __init__(self, message: str = "Not a valid CPF."):
        super().__init__(message)


class InvalidCRMError(ValidationError):
    """
    Exception case raised when invalid CRM (Brazilian Medical Certificate) numbers
    are passed.
    """

    def __init__(self, message: str = "Not a valid CRM."):
        super().__init__(message)


class FutureDateError(ValidationError):
    """
    Exception case raised when a future date is passed on a field that expected a past date.
    """

    def __init__(self, message: str = "Date is in the future."):
        super().__init__(message)


class NegativeOrZeroValueError(ValidationError):
    """
    Exception case raised when a negative or zero value is passed when a positive one was expected.
    """

    def __init__(self, message: str = "Value should be higher than 0."):
        super().__init__(message)


class InvalidBloodTypeError(ValidationError):
    """
    Exception case raised when the blood type passed is invalid (must be AB, A, B or
    O, positive or negative).
    """

    def __init__(self, message: str = "Invalid blood type."):
        super().__init__(message)


class InvalidEmailError(ValidationError):
    """
    Exception case raised when the e-mail passed is invalid.
    """

    def __init__(self, message: str = "Invalid e-mail."):
        super().__init__(message)


class AuthenticationError(ValidationError):
    """
    Exception raised when the user name, password or both are wrong.
    """

    def __init__(self, message: str = "Incorrect user name or password."):
        super().__init__(message)


class UniquenessViolationError(ValidationError):
    """
    Exception raised when an attempt is made to add a value to the database that
    already exists, violating uniqueness constraints.
    """

    def __init__(self, message: str = "Value is already exists in the database."):
        super().__init__(message)


class ReferencedKeyNotFoundError(ValidationError):
    """
    Exception raised when an attempt is made to reference a foreign key that does
    not exist in the database.
    """

    def __init__(self, message: str = "Referenced foreign key does not exist."):
        super().__init__(message)
