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



