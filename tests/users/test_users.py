from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

USER_REGISTRATION_END_POINT = "/api/v1/users/create"


def mock_post(endpoint, json):
    field_names = json.keys()

    good_mock_response = {'status_code': 201}
    bad_mock_response = {'status_code': 500}

    if endpoint == "/api/v1/users/create":
        if all(field in field_names for field in ['email', 'username', 'password']):
            return good_mock_response

    return bad_mock_response


class TestUserRegistration:
    """TestUserRegistration tests /users/register"""

    def test_get_request_returns_405(self):
        """registration endpoint does only expect a post request"""
        response = client.get(USER_REGISTRATION_END_POINT)
        assert response.status_code == 405

    def test_post_request_without_body_returns_422(self):
        """body should have username, password and fullname"""
        response = client.post(USER_REGISTRATION_END_POINT)
        assert response.status_code == 422

    def test_post_request_with_improper_body_returns_422(self):
        """all of username, password is required"""
        response = client.post(
            USER_REGISTRATION_END_POINT,
            json={"username": "santosh"}
        )
        assert response.status_code == 422

    @patch('fastapi.testclient.TestClient.post', side_effect=mock_post)
    def test_post_request_with_proper_body_returns_201(self, post):
        response = post(
            USER_REGISTRATION_END_POINT,
            json={"email": "santosh@gmail.com", "password": "snasdfasdtsh", "username": "Santosh Kumar"}
        )
        assert response['status_code'] == 201
