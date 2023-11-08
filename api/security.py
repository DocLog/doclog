import hashlib

import bcrypt


class PasswordHasher:
    """
    A class for securely hashing and validating passwords using bcrypt.
    """

    def __init__(self, pepper: str = ".", rounds: int = 12):
        self.pepper = pepper
        self.rounds = rounds

    @property
    def pepper(self) -> bytes:
        """bytes: The current pepper value as bytes."""

        return self._pepper

    @pepper.setter
    def pepper(self, value: str):
        """
        Set the pepper used for password hashing.

        Args:
            value (str): The new pepper value as a string.

        Raises:
            TypeError: If the provided value is not a string.
            ValueError: If the provided value is an empty string.
        """

        if not isinstance(value, str):
            raise TypeError("expected pepper value to be of type 'str'.")

        if value.strip() == "":
            raise ValueError("passed empty string as pepper")

        self._pepper = value.encode()

    @property
    def rounds(self) -> int:
        """int: The current number of rounds."""

        return self._rounds

    @rounds.setter
    def rounds(self, value: int):
        """
        Set the number of rounds for the bcrypt algorithm.

        Args:
            value (int): The new number of rounds.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is outside the [4, 31] interval.
        """

        if not isinstance(value, int):
            raise TypeError("expected rounds value to be of type int.")

        if value < 4 or value > 31:
            raise ValueError(
                "invalid rounds value. Must be within the [4, 31] interval."
            )

        self._rounds = value

    def hash_password(self, password: str) -> bytes:
        """
        Hash a password using bcrypt with the configured settings.

        Args:
            password (str): The password to be hashed.

        Returns:
            bytes: The hashed password.

        Raises:
            TypeError: If the password is not a string.
        """

        pre_hashed_password = self._pre_hash(password)
        salt = bcrypt.gensalt(self.rounds)
        hashed_password = bcrypt.hashpw(pre_hashed_password, salt)

        return hashed_password

    def validate_password(
        self, tested_password: str, expected_password: bytes
    ) -> bytes:
        """
        Validate a password against a hashed password.

        Args:
            tested_password (str): The password to be tested.
            expected_password (bytes): The expected hashed password.

        Returns:
            bool: True if the tested password matches the expected password, False
            otherwise.

        Raises:
            TypeError: If the tested_password is not a string.
        """

        pre_hashed_tested_password = self._pre_hash(tested_password)

        return bcrypt.checkpw(pre_hashed_tested_password, expected_password)

    def _pre_hash(self, password: str) -> bytes:
        """
        Pre-hash a password by adding the pepper and hashing it using SHA-256.

        Pre-hash a password by adding the pepper and hashing it using SHA-256. This
        is necessary in order to bypass bcrypt's 72-byte length limit for hashing
        values.

        Args:
            password (str): The password to be pre-hashed.

        Returns:
            bytes: The pre-hashed password.

        Raises:
            TypeError: If the password is not a string.
        """

        if not isinstance(password, str):
            raise TypeError("expected password value to be of type 'str'.")

        password = password.encode()
        pre_hashed_password = hashlib.sha256(self.pepper + password).digest()

        return pre_hashed_password

    def update_config(self, new_config: dict):
        """
        Update the configuration of the PasswordHasher instance.

        Args:
            new_config (dict): A dictionary containing configuration updates as key-value pairs.
        """

        for key, value in new_config.items():
            setattr(self, key, value)
