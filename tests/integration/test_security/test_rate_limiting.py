# import pytest
# from flask.testing import FlaskClient

# from api import VER


# def test_rate_limiting_on_login(client: FlaskClient):
#     endpoint = f"/api/{VER}/login"
#     data = {"name": "sysadmin", "password": "adm"}

#     for _ in range(20):
#         response = client.post(endpoint, json=data)
#         assert response.status_code == 200  # Successful the first 20 requests

#     response = client.post(endpoint, json=data)
#     assert response.status_code == 429


# @pytest.mark.parametrize(
#     "endpoint",
#     [
#         "condition",
#         "healthcare-professional",
#         "medicine",
#         "occurrence",
#         "patient-condition",
#         "patient-medicine",
#         "patient",
#         "role",
#         "user",
#     ],
# )
# def test_rate_limiting_on_unauthorized_get_request(client: FlaskClient, endpoint: str):
#     for _ in range(20):
#         response = client.get(f"/api/{VER}/{endpoint}")
#         assert response.status_code == 401  # Unauthorized for the first 20 requests

#     response = client.get(f"/api/{VER}/{endpoint}")
#     assert response.status_code == 429


# @pytest.mark.parametrize(
#     "endpoint",
#     [
#         "condition",
#         "healthcare-professional",
#         "medicine",
#         "occurrence",
#         "patient-condition",
#         "patient-medicine",
#         "patient",
#         "role",
#         "user",
#     ],
# )
# def test_rate_limiting_on_authorized_get_request(
#     client: FlaskClient, admin_headers: dict[str, str], endpoint: str
# ):
#     for _ in range(20):
#         response = client.get(f"/api/{VER}/{endpoint}", headers=admin_headers)
#         assert response.status_code == 200  # Success for the first 20 requests

#     response = client.get(f"/api/{VER}/{endpoint}")
#     assert response.status_code == 429
