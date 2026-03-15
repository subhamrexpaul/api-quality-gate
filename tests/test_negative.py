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

