import pytest

@pytest.mark.regression
def test_regression_invalid_login(page):
    page.goto("https://automationexercise.com/login")

    page.fill("input[data-qa='login-email']", "invalid_user@test.com")
    page.fill("input[data-qa='login-password']", "wrongpassword")
    page.click("button[data-qa='login-button']")

    assert page.locator("text=Your email or password is incorrect!").is_visible()

