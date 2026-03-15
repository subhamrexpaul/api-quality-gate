# Test Plan — api-quality-gate

## 1. Project Overview
This project, `api-quality-gate`, serves as a robust automated verification suite for the Restful-Booker hotel booking API (https://restful-booker.herokuapp.com). The primary objective is to validate authentication, booking lifecycles, and backend data integrity using Python, PyTest, SQLite, and GitHub Actions CI. This automation suite verifies API responses, schema adherence, error handling, and SQL data persistence, conforming with professional Testing methodologies (STLC).

## 2. Test Objectives
- Validate all REST API endpoints return correct responses under various conditions
- Ensure API contracts (JSON schemas) are strictly adhered to by responses
- Verify error handling for invalid inputs (Negative Testing)
- Confirm data integrity via direct SQL assertions against a mocked data layer

## 3. Scope
### In Scope
- `/auth` endpoint (Token generation, validation)
- `/booking` CRUD endpoints (Create, Read, Update, Delete)
- JSON Schema contract validation for all responses
- SQL data persistence and integrity checks
- Negative/boundary scenarios (e.g., empty bodies, missing tokens, invalid data types)

### Out of Scope
- UI/Frontend testing
- Load/performance testing
- Security penetration testing

## 4. Test Types
| Type              | Tool          | Count | Description                                      |
|-------------------|---------------|-------|--------------------------------------------------|
| Functional        | PyTest        | 20    | Verifies the core business logic of all endpoints|
| Contract          | jsonschema    | 8     | Ensures API responses match defined JSON schemas |
| Negative          | PyTest        | 10    | Validates error handling for invalid/bad requests|
| Data Integrity    | SQLite + PyTest | 6   | Confirms logical correctness within the database |

