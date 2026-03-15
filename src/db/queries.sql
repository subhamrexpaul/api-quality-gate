-- Query 1: Get all bookings with NULL firstname
-- Used in test_db_no_null_firstnames
SELECT * FROM bookings WHERE firstname IS NULL;

-- Query 2: Find duplicate booking_ids
-- Used in test_db_no_duplicate_booking_ids
SELECT booking_id, COUNT(*) as count
FROM bookings
GROUP BY booking_id
HAVING COUNT(*) > 1;

-- Query 3: Get bookings where totalprice is zero or negative
-- Used in test_db_totalprice_is_positive
SELECT * FROM bookings WHERE totalprice <= 0;

-- Query 4: Count total bookings inserted
-- Used to verify data persistence after API calls
SELECT COUNT(*) as total_bookings FROM bookings;

-- Query 5: Get bookings where checkin date is on or after checkout (invalid dates)
-- Used in test_db_checkin_before_checkout
SELECT * FROM bookings WHERE checkin >= checkout;

-- Query 6: Get the most recently inserted booking
-- Used to verify the latest insert matches the API response
SELECT * FROM bookings ORDER BY created_at DESC LIMIT 1;
