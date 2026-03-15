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


@pytest.mark.smoke
def test_invalid_password_returns_bad_credentials(auth_api):
    """
    Test that providing a valid username but an incorrect password
    returns a 200 OK containing 'Bad credentials' message.
    """
    response = auth_api.post("/auth", json={"username": "admin", "password": "wrongpassword"})
    assert_status_code(response, 200)
    
    data = response.json()
    assert "reason" in data, "Response is missing 'reason' key"
    assert data["reason"] == "Bad credentials"


@pytest.mark.smoke
def test_empty_username_returns_bad_credentials(auth_api):
    """
    Test that providing an empty username returns a 200 OK 
    containing 'Bad credentials' message.
    """
    response = auth_api.post("/auth", json={"username": "", "password": "password123"})
    assert_status_code(response, 200)
    
    data = response.json()
    assert "reason" in data, "Response is missing 'reason' key"
    assert data["reason"] == "Bad credentials"


@pytest.mark.smoke
def test_empty_password_returns_bad_credentials(auth_api):
    """
    Test that providing an empty password returns a 200 OK 
    containing 'Bad credentials' message.
    """
    response = auth_api.post("/auth", json={"username": "admin", "password": ""})
    assert_status_code(response, 200)
    
    data = response.json()
    assert "reason" in data, "Response is missing 'reason' key"
    assert data["reason"] == "Bad credentials"



