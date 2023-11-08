import pytest
from flask.testing import FlaskClient

from api import VER


@pytest.mark.parametrize(
    ("user_name", "password"),
    [
        ("sysadmin", "adm"),
        ("carlos_santos", "password123"),
        ("luisa_silva", "password456"),
        ("fernando_oliveira", "password789"),
        ("ana_garcia", "password101112"),
        ("roberto_martins", "password131415"),
        ("joao_silva", "password123"),
        ("maria_santos", "password456"),
        ("lucas_ferreira", "password789"),
        ("isabela_oliveira", "password101112"),
        ("miguel_goncalves", "password131415"),
    ],
)
def test_successful_user_login_with_correct_credentials(
    client: FlaskClient, user_name: str, password: str
):
    response = client.post(
        f"/api/{VER}/login", json={"name": user_name, "password": password}
    )

    assert response.status_code == 200


@pytest.mark.parametrize(
    ("user_name", "password"),
    [
        ("admin", "admin"),
        ("sysadmin", "incorrect_password"),
        ("carlos_santos", "123456"),
        ("luisa_silva", "abc123"),
        ("fernado_oliveiraa", "password789"),
        ("ana_garcia", "123456"),
        ("robertoMartins", "password131415"),
        ("joao_silva", "incorrect_password"),
        ("maria_santos", "123456"),
        ("lucas_ferreira", "abc123"),
        ("isabela_oliveira", "incorrect_password"),
        ("miguel_goncalves", "123456"),
    ],
)
def test_failed_user_login_with_incorrect_credentials(
    client: FlaskClient, user_name: str, password: str
):
    response = client.post(
        f"/api/{VER}/login", json={"name": user_name, "password": password}
    )

    assert response.status_code == 401


@pytest.mark.parametrize(
    ("user_name", "password"),
    [
        ("sysadmin", ""),
        ("", "adm"),
        ("", ""),
        ("sysadmin", None),
        (None, "adm"),
        (None, None),
    ],
)
def test_fail_user_login_with_missing_credentials(
    client: FlaskClient, user_name: str, password: str
):
    response = client.post(
        f"/api/{VER}/login", json={"name": user_name, "password": password}
    )

    assert response.status_code == 401
