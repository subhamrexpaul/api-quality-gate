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
