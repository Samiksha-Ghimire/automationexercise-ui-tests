import pytest
import re

@pytest.mark.regression
def test_regression_add_multiple_products_and_verify_total(page):
    page.goto("https://automationexercise.com")

    def add_product(product_id):
        page.hover(".productinfo")
        page.click(f"a[data-product-id='{product_id}']")
        page.wait_for_selector("text=View Cart")
        page.click("text=Continue Shopping")

    # Add products
    add_product("1")
    add_product("3")
    add_product("5")

    # Open cart
    page.click("a[href='/view_cart']")

    # Get cart rows
    cart_rows = page.locator("tr[id^='product']")
    assert cart_rows.count() == 3

    # Row-level validation
    for i in range(cart_rows.count()):
        price_text = cart_rows.nth(i).locator(".cart_price p").inner_text()
        quantity_text = cart_rows.nth(i).locator(".cart_quantity").inner_text()
        total_text = cart_rows.nth(i).locator(".cart_total_price").inner_text()

        price = int(re.sub(r"\D", "", price_text))
        quantity = int(quantity_text)
        row_total = int(re.sub(r"\D", "", total_text))

        assert row_total == price * quantity


