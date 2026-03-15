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


@pytest.mark.negative
def test_create_negative_totalprice(booking_api):
    """
    BUG-005 — API accepts negative price without validation.
    Testing that the API allows creating a booking with a negative totalprice.
    """
    bad_data = generate_booking()
    bad_data["totalprice"] = -500
    
    response = booking_api.create_booking(bad_data)
    # This is a documented bug, so we assert it currently returns 200
    assert response.status_code == 200, f"Expected 200 (Bug-005) but got {response.status_code}"
    assert response.json()["booking"]["totalprice"] == -500



@pytest.mark.negative
def test_delete_nonexistent_booking(booking_api, auth_token):
    """
    Test that deleting a non-existent booking ID returns 405 Method Not Allowed.
    Note: Industry standard is 404, but this API quirky.
    """
    response = booking_api.delete_booking(9999999, auth_token)
    assert response.status_code in [405, 404], f"Expected 405/404 but got {response.status_code}"


@pytest.mark.negative
def test_partial_update_empty_body(booking_api, auth_token, sample_booking):
    """
    BUG-003 — PATCH with empty body returns 200, should be 400.
    """
    response = booking_api.partial_update(sample_booking, {}, auth_token)
    # Documented bug: returns 200 instead of 400
    assert response.status_code == 200, f"Expected 200 (Bug-003) but got {response.status_code}"








