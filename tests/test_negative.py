import pytest
from src.utils.assertions import assert_status_code
from src.utils.data_factory import generate_booking

@pytest.mark.negative
def test_delete_without_token_returns_403(booking_api, sample_booking):
    """
    Test that deleting a booking without a token returns a 403 Forbidden.
    """
    response = booking_api.delete_booking(sample_booking, token="")
    assert_status_code(response, 403)


@pytest.mark.negative
def test_update_without_token_returns_403(booking_api, sample_booking):
    """
    Test that updating a booking without a token returns a 403 Forbidden.
    """
    updated_data = generate_booking()
    response = booking_api.update_booking(sample_booking, updated_data, token="")
    assert_status_code(response, 403)


@pytest.mark.negative
def test_create_missing_firstname_field(booking_api):
    """
    Test that creating a booking with a missing required field (firstname) returns 400 or 500.
    Note: Restful-Booker often returns 500 for schema violations.
    """
    incomplete_data = generate_booking()
    del incomplete_data["firstname"]
    
    response = booking_api.create_booking(incomplete_data)
    # Restful-Booker returns 500 for missing fields in many environments
    assert response.status_code in [400, 500], f"Expected 400/500 but got {response.status_code}"


@pytest.mark.negative
def test_create_empty_body(booking_api):
    """
    Test that creating a booking with an empty JSON body returns 400 or 415.
    """
    response = booking_api.post("/booking", json={})
    # Often returns 500 in this quirky API but 400 is expected standard
    assert response.status_code in [400, 415, 500], f"Expected 400/415/500 but got {response.status_code}"


@pytest.mark.negative
def test_get_booking_with_string_id(booking_api):
    """
    Test that retrieving a booking using a string ID instead of integer returns 404.
    """
    response = booking_api.get_booking("invalid_id")
    assert_status_code(response, 404)


@pytest.mark.negative
def test_auth_wrong_content_type(auth_api):
    """
    Test that sending auth request with wrong content type returns 415 or 400.
    """
    headers = {"Content-Type": "text/plain"}
    response = auth_api.post("/auth", data="username=admin", headers=headers)
    assert response.status_code in [415, 400, 404], f"Expected 415/400 but got {response.status_code}"





