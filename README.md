# 🧪 REST API Quality Gate — Python Test Automation Suite

A professional, production-ready **Automated Testing** framework for high-stakes API verification, designed to validate core business logic and data persistence.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)
![PyTest](https://img.shields.io/badge/PyTest-7.4.3-0A9EDC?style=flat&logo=pytest&logoColor=white)
![GitHub Actions CI](https://img.shields.io/badge/GitHub%20Actions-CI-2088FF?style=flat&logo=github-actions&logoColor=white)
![MIT License](https://img.shields.io/badge/License-MIT-green?style=flat)

📊 **Live Test Report**: https://subhamrexpaul.github.io/api-quality-gate/

## 🏢 About This Project
This project simulates a high-assurance **Automated Testing** engagement for an Oracle consulting partner. It targets the **Restful-Booker** hotel booking API to ensure zero-defect releases for critical reservation workflows. By implementing a "Quality Gate," this suite prevents breaking changes from reaching production through rigorous validation of auth tokens, booking lifecycles, and financial data integrity.

What sets this suite apart is its adherence to professional **Testing methodologies (STLC)**. Unlike basic scripts, this project includes a full suite of **STLC Documentation** (Test Plan, RTM, Bug Register), a dedicated **SQL** data validation layer, and **Continuous integration tools** to automate the quality audit on every commit. This demonstrates a deep **SDLC understanding** and advanced **problem-solving** skills in handling API quirks and boundary conditions.

## 🛠️ Tech Stack
| Technology | Version | Purpose |
|:---|:---|:---|
| **Python** | 3.11+ | Primary programming language for the framework |
| **PyTest** | 7.4.3 | Core **Automated Testing** framework and test runner |
| **Requests** | 2.31.0 | HTTP client for REST API interactions |
| **SQL (SQLite)** | 3.x | Local data persistence layer for integrity assertions |
| **JSON Schema** | 4.21.1 | **Contract Testing** and response shape validation |
| **GitHub Actions** | N/A | **Continuous integration tools** for automated pipeline runs |
| **Faker** | 21.0.0 | Dynamic test data generation for robust coverage |

## 🏗️ Architecture
```text
api-quality-gate/
├── .github/workflows/      # Continuous Integration (GitHub Actions)
├── docs/                   # STLC Documentation (Test Plan, RTM, Bug Register)
├── src/
│   ├── api/               # API Client Wrappers (Base, Auth, Booking)
│   ├── db/                # SQL Client & Prepared Queries
│   ├── schemas/           # JSON Schema definitions for Contract Testing
│   └── utils/             # Assertions & Data Factories
├── tests/
│   ├── conftest.py        # Shared PyTest Fixtures
│   └── test_*.py          # Functional, Negative, & Contract Test Suites
├── pytest.ini             # Test runner configuration & markers
└── requirements.txt       # Project dependencies
```

## 📋 Test Suite Overview
| Module | Tests | Type | Marker |
|:---|:---|:---|:---|
| `test_auth.py` | 2 | Functional | `smoke` |
| `test_booking_crud.py` | 15 | Functional / Regression | `smoke`, `regression` |
| `test_contract.py` | 8 | **Contract Testing** | `contract` |
| `test_negative.py` | 10 | **Negative Testing** | `negative` |
| `test_data_integrity.py` | 6 | **Data Integrity** (SQL) | `regression` |

## 🚀 Getting Started
### Prerequisites
- **Python 3.11+**
- **Version control (Git)**

### Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/api-quality-gate.git
   cd api-quality-gate
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Execution
- **Run Smoke Tests (Sanity):**
  ```bash
  pytest -m smoke
  ```
- **Run Full Regression Suite:**
  ```bash
  pytest -m regression
  ```
- **Run All Tests with Report:**
  ```bash
  pytest --html=reports/report.html
  ```

## 📑 STLC Documentation
Comprehensive documentation mapping to the **Bug life cycle** and requirements:
- [**TEST_PLAN.md**](docs/TEST_PLAN.md): Detailed strategy, scope, environment, and risk mitigation.
- [**RTM.md**](docs/RTM.md): Requirements Traceability Matrix mapping tests to business needs.
- [**BUG_REGISTER.md**](docs/BUG_REGISTER.md): Formal log of discovered API defects and quirks.

## 💎 Key Features
- **SQL Data Validation**: Direct database assertions using `sqlite3` to ensure API actions persist correctly.
- **Contract Testing**: Strict JSON Schema validation to prevent breaking upstream API changes.
- **GitHub Actions CI**: Automated **Continuous integration** pipeline with multi-job smoke/regression gates.
- **Negative Testing**: Robust coverage for boundary values, invalid auth, and edge-case "problem solving".
- **Full STLC Documentation**: Professional-grade audit trails for every requirement and bug discovered.

---
*Schema design compatible with Oracle Database 19c*
