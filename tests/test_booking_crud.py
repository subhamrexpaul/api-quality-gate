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


@pytest.mark.regression
def test_each_item_has_bookingid_key(booking_api):
    """
    Test that every object in the booking list contains the 'bookingid' key.
    """
    response = booking_api.get_all_bookings()
    data = response.json()
    
    for item in data[:10]:  # Testing first 10 items for efficiency
        assert "bookingid" in item, f"Item {item} is missing 'bookingid' key"


@pytest.mark.smoke
def test_create_booking_returns_200(booking_api):
    """
    Test that creating a new booking returns a 200 OK status code.
    (Note: API quirk uses 200 instead of 201).
    """
    booking_data = generate_booking()
    response = booking_api.create_booking(booking_data)
    assert_status_code(response, 200)


@pytest.mark.smoke
def test_create_booking_response_has_bookingid(booking_api):
    """
    Test that the response of creating a booking includes the 'bookingid' key.
    """
    booking_data = generate_booking()
    response = booking_api.create_booking(booking_data)
    assert_status_code(response, 200)
    
    data = response.json()
    assert "bookingid" in data, "Response JSON is missing 'bookingid' key"
    assert isinstance(data["bookingid"], int), f"Expected int for bookingid but got {type(data['bookingid'])}"




