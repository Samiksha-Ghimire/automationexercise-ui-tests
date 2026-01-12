# Test Strategy

This document describes how test cases are classified, automated, and executed in this project for both UI and API testing.

## Test Scope

The project includes:
- UI automation for critical user workflows
- API testing for core backend endpoints

## Test Classification

Tests are divided into smoke, sanity, and regression suites to support selective execution and faster feedback.

## UI Testing Strategy

### Smoke Tests
Smoke tests validate that the application is accessible and core functionality is available. These tests are designed to be fast and run frequently in CI.

**Examples:**
- Application launch
- Login page availability
- Basic login functionality

### Sanity Tests
Sanity tests validate that recent changes have not broken related functionality. These tests focus on key user flows affected by changes.

**Examples:**
- Login and logout flow
- Core navigation after login

### Regression Tests
Regression tests cover end-to-end user journeys and edge cases. These tests ensure that previously working functionality continues to work after changes.

**Examples:**
- Negative login scenarios
- Cart functionality with and without login
- Multiple product addition and price calculation validation

## API Testing Strategy

API tests validate backend functionality independently of the UI. These tests ensure correct request handling, response validation, and error handling.

**Examples:**
- GET, POST, PUT, DELETE endpoint validation
- Positive and negative API scenarios
- Response status code and payload validation

## Execution Strategy

- Smoke UI tests run on every push using GitHub Actions CI
- Sanity tests are executed after feature-level changes
- Regression tests are executed before releases or major updates
- API tests are executed independently using Postman and can be run alongside UI tests
