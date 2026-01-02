import pytest

@pytest.mark.regression
def test_regression_add_single_product_to_cart(page):
    page.goto("https://automationexercise.com")

    # Add first product to cart
    page.hover(".productinfo")
    page.click("a[data-product-id='1']")

    # Handle add-to-cart modal
    page.wait_for_selector("text=View Cart")
    page.click("text=View Cart")

    # Verify product is present in cart
    assert page.locator("tr[id^='product']").is_visible()

    # Verify cart quantity is 1
    cart_qty = page.locator(".cart_quantity").inner_text()
    assert cart_qty == "1"

