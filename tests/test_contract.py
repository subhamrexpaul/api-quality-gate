import pytest
from pathlib import Path
from src.utils.assertions import assert_valid_schema
from src.utils.data_factory import generate_booking

# Define schema paths
SCHEMA_DIR = Path("src/schemas")
BOOKING_SCHEMA = SCHEMA_DIR / "booking_schema.json"
CREATE_BOOKING_SCHEMA = SCHEMA_DIR / "create_booking_schema.json"
AUTH_SCHEMA = SCHEMA_DIR / "auth_schema.json"

@pytest.mark.contract
def test_get_booking_matches_schema(booking_api, sample_booking):
    """
    Test that the GET /booking/:id response matches the defined JSON schema.
    """
    response = booking_api.get_booking(sample_booking)
    assert response.status_code == 200
    assert_valid_schema(response.json(), str(BOOKING_SCHEMA))


@pytest.mark.contract
def test_create_booking_response_matches_schema(booking_api):
    """
    Test that the POST /booking response matches the wrapper schema.
    """
    booking_data = generate_booking()
    response = booking_api.create_booking(booking_data)
    assert response.status_code == 200
    assert_valid_schema(response.json(), str(CREATE_BOOKING_SCHEMA))


@pytest.mark.contract
def test_put_booking_response_matches_schema(booking_api, auth_token, sample_booking):
    """
    Test that the PUT /booking/:id response matches the booking schema.
    """
    updated_data = generate_booking()
    response = booking_api.update_booking(sample_booking, updated_data, auth_token)
    assert response.status_code == 200
    assert_valid_schema(response.json(), str(BOOKING_SCHEMA))


