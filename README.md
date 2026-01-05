[![Playwright UI Tests](https://github.com/Samiksha-Ghimire/automationexercise-ui-tests/actions/workflows/playwright-tests.yml/badge.svg)](https://github.com/Samiksha-Ghimire/automationexercise-ui-tests/actions/workflows/playwright-tests.yml)

# UI and API Automation Project
UI tests are automatically executed on every push using GitHub Actions CI.
This repository contains UI automation tests and API automation tests implemented as part of QA automation practice.

## Tools and Technologies

### UI Automation:
- Python
- Playwright
- Pytest

### API Automation:
- Postman
- JavaScript (Postman test scripts)

## UI Automation Structure

- Page Object Model is used for UI automation
- Tests are classified into smoke, sanity, and regression
- Smoke tests validate basic availability
- Sanity tests validate core flows after changes
- Regression tests cover end-to-end scenarios and edge cases

## API Automation Structure

- CRUD API testing using Postman
- Positive and negative scenarios
- Environment variables used for base URL
- Collections and environments are stored under the postman folder

## How to Run UI Tests

``` bash
pip install -r requirements.txt
pytest -m smoke
pytest -m sanity
pytest -m regression
``` 

## API Tests
API tests include positive and negative scenarios for GET, POST, PUT, and DELETE endpoints with response validation using Postman test scripts.

1. Import Postman collection from postman/collections
2. Import environment from postman/environments
3. Select environment
4. Run requests individually or using Collection Runner
