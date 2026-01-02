import pytest

@pytest.mark.regression
def test_regression_add_product_to_cart_without_login(page):
    # Open home page (not logged in)
    page.goto("https://automationexercise.com")

    # Add a product to cart
    page.hover(".productinfo")
    page.click("a[data-product-id='2']")

    # Handle add-to-cart modal
    page.wait_for_selector("text=View Cart")
    page.click("text=View Cart")

    # Verify product is present in cart
    assert page.locator("tr[id^='product']").is_visible()

    # Verify cart quantity is 1
    cart_qty = page.locator(".cart_quantity").inner_text()
    assert cart_qty == "1"
