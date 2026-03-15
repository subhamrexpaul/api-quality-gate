import pytest
from src.utils.assertions import assert_status_code, assert_valid_schema
from src.utils.data_factory import generate_booking


@pytest.mark.smoke
def test_get_all_bookings_returns_200(booking_api):
    """
    Test that retrieving all booking IDs returns a 200 OK status code.
    """
    response = booking_api.get_all_bookings()
    assert_status_code(response, 200)


@pytest.mark.smoke
def test_get_all_bookings_returns_list(booking_api):
    """
    Test that retrieving all booking IDs returns a non-empty list.
    """
    response = booking_api.get_all_bookings()
    assert_status_code(response, 200)
    
    data = response.json()
    assert isinstance(data, list), f"Expected list but got {type(data)}"
    assert len(data) > 0, "Expected non-empty list of bookings"

