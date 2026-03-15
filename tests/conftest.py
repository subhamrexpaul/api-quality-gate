import pytest
from src.api.base_client import BaseClient
from src.api.auth_api import AuthAPI
from src.api.booking_api import BookingAPI
from src.db.db_client import DBClient
from src.utils.data_factory import generate_booking


@pytest.fixture(scope="session")
def base_url() -> str:
    """Fixture returning the root Restful-Booker API URL."""
    return "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="session")
def booking_api(base_url) -> BookingAPI:
    """Fixture returning an initialized BookingAPI client."""
    return BookingAPI(base_url)


@pytest.fixture(scope="session")
def auth_api(base_url) -> AuthAPI:
    """Fixture returning an initialized AuthAPI client."""
    return AuthAPI(base_url)


@pytest.fixture(scope="session")
def auth_token(auth_api) -> str:
    """Fixture returning a valid authentication token."""
    token = auth_api.get_token()
    assert token is not None, "Failed to retrieve auth token"
    return token


@pytest.fixture(scope="function")
def db() -> DBClient:
    """
    Fixture creating the DBClient, initializing the 'bookings' table,
    yielding the DB instance, and closing it during teardown.
    Function scoped to ensure fresh interactions per test.
    """
    client = DBClient()
    # Ensure a fresh table for every test to avoid duplication across runs
    client.cursor.execute("DROP TABLE IF EXISTS bookings;")
    client.create_table()
    yield client
    client.close()



@pytest.fixture(scope="function")
def sample_booking(booking_api, auth_token) -> int:
    """
    Fixture generating a sample booking, creating it via the API,
    yielding its booking ID, and subsequently deleting it.
    """
    booking_data = generate_booking()
    response = booking_api.create_booking(booking_data)
    assert response.status_code == 200, "Fixture failed: Could not create booking"
    
    booking_id = response.json().get("bookingid")
    assert booking_id is not None, "Fixture failed: bookingid not returned"
    
    yield booking_id
    
    # Teardown logic
    booking_api.delete_booking(booking_id, auth_token)





