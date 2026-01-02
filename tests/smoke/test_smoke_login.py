import pytest

import os
import pytest

@pytest.mark.smoke
def test_smoke_open_login_page(page):
    page.goto("https://automationexercise.com/login")
    assert page.locator("text=Login to your account").is_visible()


@pytest.mark.smoke
def test_smoke_valid_login(page):
    page.goto("https://automationexercise.com/login")

    page.fill("input[data-qa='login-email']", os.getenv("AE_TEST_EMAIL"))
    page.fill("input[data-qa='login-password']", os.getenv("AE_TEST_PASSWORD"))
    page.click("button[data-qa='login-button']")

    assert page.locator("text=Logged in as").is_visible()



