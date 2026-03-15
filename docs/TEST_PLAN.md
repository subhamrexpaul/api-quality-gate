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

## 5. Entry Criteria
- The Restful-Booker API is accessible at the base URL (`https://restful-booker.herokuapp.com`)
- The `/auth` endpoint successfully returns a valid token with functional credentials
- Python environment (version 3.11+) is set up locally or in CI
- All project dependencies are installed successfully via `requirements.txt`
- Test environment components (SQLite mock database) are initialized without errors

## 6. Exit Criteria
- 100% of defined smoke tests and regression tests are passing execution
- 0 Priority-1 (Critical) or Priority-2 (Major) bugs remaining open
- Requirements Traceability Matrix (RTM) is 100% complete, mapping tests to requirements
- CI pipeline (GitHub Actions) returns a green build on the `main` branch
- Test execution reports (HTML) are successfully generated and attached as workflow artifacts

## 7. Test Environment
- **Programming Language**: Python 3.11+
- **Test Framework**: PyTest 7.4.3
- **OS**: Windows / Linux (Ubuntu) / macOS
- **Target API**: Restful-Booker (`https://restful-booker.herokuapp.com`)
- **Database**: SQLite (local mock DB, `test_results.db`)
- **CI/CD**: GitHub Actions (Ubuntu latest runner)
- **Reporting**: pytest-html

## 8. Test Schedule
This project execution follows a 2-week structured testing timeline.

| Week   | Activity                                                                 |
|--------|--------------------------------------------------------------------------|
| Week 1 | Environment Setup, Auth endpoints, CRUD Functional Test Cases            |
| Week 2 | Contract Validation, Negative Scenarios, SQL Assertions, CI integration, Documentation |

## 9. Risks & Mitigations
| Risk                                    | Mitigation                                                               |
|-----------------------------------------|--------------------------------------------------------------------------|
| Restful-Booker API is down              | Retry logic in test execution; pipeline fails gracefully                 |
| Authentication token expires mid-run    | `session`-scoped PyTest fixture ensures token is valid for test run      |
| Flaky network or intermittent 500s      | Integration of robust assertions; clear failure logs in HTML artifacts   |
| API schema changes without notice       | Contract tests strictly enforce schemas to catch changes immediately     |


