import os
import pytest

@pytest.mark.sanity
def test_sanity_login_and_logout(page):
    page.goto("https://automationexercise.com/login")

    # Login
    page.fill("input[data-qa='login-email']", os.getenv("AE_TEST_EMAIL"))
    page.fill("input[data-qa='login-password']", os.getenv("AE_TEST_PASSWORD"))
    page.click("button[data-qa='login-button']")

    assert page.locator("text=Logged in as").is_visible()

    # Logout
    page.click("a[href='/logout']")

    assert page.locator("text=Login to your account").is_visible()

