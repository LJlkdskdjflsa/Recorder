from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

USER_LOGIN_END_POINT = "/api/v1/auth/login"


class TestUserLogin:
    """TestUserLogin tests /users/auth"""

    def test_get_request_returns_405(self):
        """login endpoint does only expect a post request"""
        response = client.get(USER_LOGIN_END_POINT)
        assert response.status_code == 405

    def test_post_request_without_body_returns_422(self):
        """body should have username, password """
        response = client.post(USER_LOGIN_END_POINT)
        assert response.status_code == 422

    def test_post_request_with_improper_body_returns_422(self):
        """both username and password is required"""
        response = client.post(
            USER_LOGIN_END_POINT,
            json={"username": "santosh"}
        )
        assert response.status_code == 422

    def test_post_request_with_proper_body_returns_200_with_jwt_token(self):
        response = client.post(
            USER_LOGIN_END_POINT,
            json={"username": "santosh", "password": "sntsh"}
        )
        assert response.status_code == 200
        assert len(response.json()) == 2
