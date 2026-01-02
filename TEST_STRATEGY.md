Test Strategy

This document describes how test cases are classified and automated in this project.

Test Classification

Tests are divided into smoke, sanity, and regression suites to support selective execution and faster feedback.

Smoke Tests

Smoke tests validate that the application is accessible and core functionality is available.
These tests are designed to be fast and run after deployments.

Examples:
- Application launch
- Login page availability
- Basic login functionality

Sanity Tests

Sanity tests validate that recent changes have not broken related functionality.
These tests focus on key user flows affected by changes.

Examples:
- Login and logout flow
- Core navigation after login

Regression Tests

Regression tests cover end-to-end user journeys and edge cases.
These tests ensure that previously working functionality continues to work after changes.

Examples:
- Negative login scenarios
- Cart functionality with and without login
- Multiple product addition and price calculation validation

Execution Strategy

- Smoke tests can be executed independently for quick validation
- Sanity tests are executed after feature-level changes
- Regression tests are executed before releases or major updates
