# Bug Register — api-quality-gate

## Bug Life Cycle States
New → Assigned → In Progress → Fixed → Verified → Closed

## Known Bugs

### BUG-001: DELETE /booking returns 201 instead of 204
- **Severity**: Minor
- **Priority**: P3
- **Status**: Closed (Documented API Quirk)
- **Description**: The DELETE endpoint successfully deletes a booking but incorrectly responds with an HTTP `201 Created` status code instead of the core REST standard HTTP `204 No Content` or `200 OK`.
- **Steps to Reproduce**:
  1. Generate a valid auth token from `POST /auth`.
  2. Create a new booking using `POST /booking` to obtain a valid `bookingid`.
  3. Send a `DELETE /booking/{id}` request with the `Cookie: token={token}` header.
- **Expected Result**: HTTP `204 No Content` indicating successful deletion with no return body.
- **Actual Result**: HTTP `201 Created` is returned.
- **Fixed In**: N/A (Test cases `test_delete_booking_returns_201_quirk` updated to accept 201 per API documentation).
