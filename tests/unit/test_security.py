import hmac

import pytest

from api.security import PasswordHasher
from tests.common import get_test_parameters


@pytest.fixture(name="password_hasher")
def password_hasher_fixture():
    return PasswordHasher(
        r'\xf1\xba\xc2\xb9"ve\x148\x00d\xc3\x1d\xae\xaa\x98\xf5\xcfL\xffCH(\xe6"6\xba0B\xc9\x94\xcf',
        4,
    )


@pytest.mark.parametrize("password", get_test_parameters("passwords"))
def test_password_validation(password_hasher: PasswordHasher, password: str):
    hashed_password = password_hasher.hash_password(password)

    assert password_hasher.validate_password(password, hashed_password) is True


@pytest.mark.parametrize("password", get_test_parameters("passwords"))
def test_password_hashes_should_have_a_fixed_length_of_60(
    password_hasher: PasswordHasher, password: str
):
    hashed_password = password_hasher.hash_password(password)

    assert len(hashed_password) == 60


def test_password_generation_should_not_have_character_limit(
    password_hasher: PasswordHasher,
):
    pwd1 = "A very large password that definitely has more than 72 bytes and characters"
    pwd2 = (
        "A very large password that definitely has more than 72 bytes and characters."
    )

    hashed_pwd1 = password_hasher.hash_password(pwd1)
    hashed_pwd2 = password_hasher.hash_password(pwd2)

    assert hmac.compare_digest(hashed_pwd1, hashed_pwd2) is False
