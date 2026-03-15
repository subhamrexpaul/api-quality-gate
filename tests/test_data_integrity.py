import pytest
from src.utils.data_factory import generate_booking

@pytest.mark.regression
def test_booking_persisted_after_create(booking_api, db):
    """
    Test that a booking created via API and inserted into DB is correctly persisted.
    """
    # 1. Create via API
    booking_data = generate_booking()
    response = booking_api.create_booking(booking_data)
    booking_id = response.json()["bookingid"]
    
    # 2. Insert into DB
    db_data = booking_data.copy()
    db_data["booking_id"] = booking_id
    db.insert_booking(db_data)
    
    # 3. Verify via SQL (Query 6)
    results = db.run_query("SELECT * FROM bookings ORDER BY created_at DESC LIMIT 1;")
    assert len(results) == 1
    assert results[0]["booking_id"] == booking_id
    assert results[0]["firstname"] == booking_data["firstname"]


@pytest.mark.regression
def test_db_firstname_not_null(db):
    """
    Test that no bookings in the database have a NULL firstname.
    Uses Query 1.
    """
    results = db.run_query("SELECT * FROM bookings WHERE firstname IS NULL;")
    assert len(results) == 0, f"Found {len(results)} records with NULL firstname"

