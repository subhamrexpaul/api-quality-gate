import pytest
from src.utils.assertions import assert_status_code, assert_valid_schema


@pytest.mark.smoke
def test_valid_auth_returns_token(auth_api):
    """
    Test that providing valid credentials returns 200 OK and a token string.
    """
    response = auth_api.post("/auth", json={"username": "admin", "password": "password123"})
    assert_status_code(response, 200)
    
    data = response.json()
    assert "token" in data, "Response JSON is missing the 'token' key"
    assert len(data["token"]) > 0, "Returned token is empty"
