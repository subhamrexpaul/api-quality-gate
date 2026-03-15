# Requirements Traceability Matrix (RTM)

This document maps the core business requirements of the Restful-Booker API to the implemented test cases in the `api-quality-gate` project.

| REQ-ID  | Requirement                                             | Test Case ID | Test Name                                       | Status |
|---------|---------------------------------------------------------|--------------|-------------------------------------------------|--------|
| REQ-001 | System shall authenticate valid users with 200 OK       | TC-001       | test_valid_auth_returns_token                   | Pass   |
| REQ-002 | System shall generate unique token for valid auth       | TC-002       | test_valid_auth_response_has_token              | Pass   |
| REQ-003 | System shall return 200 OK for retrieving all bookings  | TC-003       | test_get_all_bookings_returns_200               | Pass   |
| REQ-004 | System shall allow booking creation with valid schema   | TC-004       | test_create_booking_returns_200                 | Pass   |
| REQ-005 | System shall correctly save firstname on creation       | TC-005       | test_create_booking_firstname_matches_request   | Pass   |
| REQ-006 | System shall return 200 OK for retrieving valid booking | TC-006       | test_get_booking_by_id_returns_200              | Pass   |
| REQ-007 | System shall update full booking details correctly      | TC-007       | test_update_full_booking                        | Pass   |
| REQ-008 | System shall allow partial booking updates (PATCH)      | TC-008       | test_partial_update_firstname                   | Pass   |
| REQ-009 | System shall allow booking deletion with valid token    | TC-009       | test_delete_booking_returns_201_quirk           | Pass   |
| REQ-010 | System shall strictly enforce POST response schema      | TC-010       | test_create_booking_response_matches_schema     | Pass   |
| REQ-011 | System shall reject authentication without valid token  | TC-011       | test_delete_without_token                       | Pass   |
| REQ-012 | System shall return 400/500 for missing mandatory fields| TC-012       | test_create_missing_firstname_field             | Pass   |
| REQ-013 | System shall reject non-numeric booking IDs (404)       | TC-013       | test_get_booking_with_string_id                 | Pass   |
| REQ-014 | Database shall save check-in dates chronologically      | TC-014       | test_db_checkin_before_checkout                 | Pass   |
| REQ-015 | Database shall not contain duplicated booking IDs       | TC-015       | test_db_no_duplicate_booking_ids                | Pass   |
