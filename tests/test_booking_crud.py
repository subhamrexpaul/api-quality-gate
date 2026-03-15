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


@pytest.mark.regression
def test_create_booking_firstname_matches_request(booking_api):
    """
    Test that the firstname of the created booking matches the request data.
    """
    booking_data = generate_booking()
    response = booking_api.create_booking(booking_data)
    assert_status_code(response, 200)
    
    data = response.json()
    actual_firstname = data["booking"]["firstname"]
    expected_firstname = booking_data["firstname"]
    assert actual_firstname == expected_firstname, (
        f"Expected firstname '{expected_firstname}' but got '{actual_firstname}'"
    )


@pytest.mark.smoke
def test_get_booking_by_id_returns_200(booking_api, sample_booking):
    """
    Test that retrieving a specific booking by its ID returns a 200 OK.
    Uses the sample_booking fixture for setup and cleanup.
    """
    response = booking_api.get_booking(sample_booking)
    assert_status_code(response, 200)


@pytest.mark.regression
def test_get_booking_returns_correct_data(booking_api, sample_booking):
    """
    Test that retrieving a booking by ID returns the correct data keys.
    """
    response = booking_api.get_booking(sample_booking)
    assert_status_code(response, 200)
    
    data = response.json()
    expected_keys = ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates"]
    for key in expected_keys:
        assert key in data, f"Response JSON is missing expected key: {key}"


@pytest.mark.regression
def test_get_nonexistent_booking_returns_404(booking_api):
    """
    Test that retrieving a non-existent booking ID returns a 404 Not Found.
    """
    response = booking_api.get_booking(9999999)
    assert_status_code(response, 404)


@pytest.mark.regression
def test_full_update_booking(booking_api, auth_token, sample_booking):
    """
    Test that a full update (PUT) of a booking correctly modifies labels.
    """
    updated_data = generate_booking()
    updated_data["firstname"] = "Antigravity"
    
    response = booking_api.update_booking(sample_booking, updated_data, auth_token)
    assert_status_code(response, 200)
    
    data = response.json()
    assert data["firstname"] == "Antigravity", f"Expected 'Antigravity' but got '{data['firstname']}'"


@pytest.mark.regression
def test_partial_update_firstname(booking_api, auth_token, sample_booking):
    """
    Test that a partial update (PATCH) of only the firstname field works correctly.
    """
    patch_data = {"firstname": "PartialUpdate"}
    response = booking_api.partial_update(sample_booking, patch_data, auth_token)
    assert_status_code(response, 200)
    
    data = response.json()
    assert data["firstname"] == "PartialUpdate", f"Expected 'PartialUpdate' but got '{data['firstname']}'"


@pytest.mark.regression
def test_partial_update_totalprice(booking_api, auth_token, sample_booking):
    """
    Test that a partial update (PATCH) of only the totalprice field works correctly.
    """
    patch_data = {"totalprice": 777}
    response = booking_api.partial_update(sample_booking, patch_data, auth_token)
    assert_status_code(response, 200)
    
    data = response.json()
    assert data["totalprice"] == 777, f"Expected 777 but got {data['totalprice']}"


@pytest.mark.regression
def test_delete_booking_returns_201(booking_api, auth_token):
    """
    Test that deleting a booking returns a 201 Created status code.
    (Note: API quirk uses 201 instead of 204).
    """
    # Create a temporary booking to delete
    booking_data = generate_booking()
    create_res = booking_api.create_booking(booking_data)
    temp_id = create_res.json()["bookingid"]
    
    response = booking_api.delete_booking(temp_id, auth_token)
    assert_status_code(response, 201)


@pytest.mark.regression
def test_deleted_booking_returns_404(booking_api, auth_token):
    """
    Test that a deleted booking cannot be retrieved and returns 404.
    """
    # 1. Create
    booking_data = generate_booking()
    create_res = booking_api.create_booking(booking_data)
    temp_id = create_res.json()["bookingid"]
    
    # 2. Delete
    booking_api.delete_booking(temp_id, auth_token)
    
    # 3. Verify GET 404
    response = booking_api.get_booking(temp_id)
    assert_status_code(response, 404)


@pytest.mark.regression
def test_create_and_persist_to_db(booking_api, db):
    """
    Test that a created booking can be successfully inserted into and 
    retrieved from the local SQLite database.
    """
    # 1. Create booking via API
    booking_data = generate_booking()
    response = booking_api.create_booking(booking_data)
    assert_status_code(response, 200)
    
    booking_id = response.json()["bookingid"]
    
    # 2. Persist to DB
    # Adding booking_id into the dict to match insert_booking expectation
    db_data = booking_data.copy()
    db_data["booking_id"] = booking_id
    db.insert_booking(db_data)

    
    # 3. Run query to verify persistence
    sql = f"SELECT * FROM bookings WHERE booking_id = {booking_id}"
    results = db.run_query(sql)
    
    assert len(results) == 1, f"Expected 1 database record but found {len(results)}"
    assert results[0]["firstname"] == booking_data["firstname"], "DB firstname mismatch"














