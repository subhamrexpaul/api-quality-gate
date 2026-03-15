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

### BUG-002: POST /booking returns 200 instead of 201
- **Severity**: Minor
- **Priority**: P3
- **Status**: Closed (Documented API Quirk)
- **Description**: When a new booking is successfully created, the API responds with `200 OK` rather than the `201 Created` status expected for a resource creation operation.
- **Steps to Reproduce**:
  1. Send a `POST /booking` request with a valid JSON booking payload.
- **Expected Result**: HTTP `201 Created` with the new booking details.
- **Actual Result**: HTTP `200 OK` with the new booking details.
- **Fixed In**: N/A (Tests accept 200 OK for this endpoint).

### BUG-003: PATCH empty body returns 200 (should be 400)
- **Severity**: Minor
- **Priority**: P3
- **Status**: New
- **Description**: The PATCH `/booking/{id}` endpoint incorrectly returns `200 OK` when provided an empty JSON body `{}`, despite no operations being performed on the underlying resource.
- **Steps to Reproduce**:
  1. Generate an authentication token from `/auth`.
  2. Create a new booking via POST `/booking`.
  3. Send `PATCH /booking/{id}` with an empty payload `{}` and include the generated auth cookie.
- **Expected Result**: HTTP `400 Bad Request` indicating missing or invalid structure.
- **Actual Result**: HTTP `200 OK` is incorrectly returned alongside the unmodified original data.
- **Fixed In**: Pending

### BUG-004: No rate limiting on auth endpoint
- **Severity**: Major
- **Priority**: P2
- **Status**: In Progress
- **Description**: The `/auth` endpoint allows an unlimited number of login attempts without enforcing rate limits or account lockouts. This exposes the system to brute-force credential attacks.
- **Steps to Reproduce**:
  1. Write an automated loop to send 100+ requests to `POST /auth`.
  2. Provide random user credentials in the JSON payload rapidly.
- **Expected Result**: HTTP `429 Too Many Requests` after a specific threshold (e.g., 5 attempts/minute).
- **Actual Result**: All requests are processed normally (returning HTTP 200).
- **Fixed In**: Under investigation by the backend security team.

### BUG-005: Negative totalprice accepted without validation
- **Severity**: Minor
- **Priority**: P3
- **Status**: New
- **Description**: The API permits the creation of reservations where `totalprice` is less than zero. The database stores these negative financial values without validation checks.
- **Steps to Reproduce**:
  1. Send a `POST /booking` request or `PUT /booking/{id}` request using payload with `"totalprice": -500`.
  2. Review the resulting response or perform a `GET /booking/{id}` fetch.
- **Expected Result**: HTTP `400 Bad Request` or `422 Unprocessable Entity` due to invalid business logic.
- **Actual Result**: HTTP `200 OK` is returned, and negative prices display correctly in the system.
- **Fixed In**: Pending




