from selenium.webdriver.common.by import By


def test_storefront_loads_with_expected_products(store_page):
    assert store_page.title == "Demo Storefront"
    assert store_page.visible_products() == [
        "Laptop Pro", "Wireless Mouse", "Desk Lamp", "SQL Handbook"
    ]


def test_search_filters_products_and_shows_empty_state(store_page):
    store_page.search("laptop")
    assert store_page.visible_products() == ["Laptop Pro"]
    store_page.search("not-a-product")
    assert store_page.visible_products() == []
    assert store_page.empty_state_visible()


def test_category_filter_can_be_combined_with_search(store_page):
    store_page.select_category("electronics")
    assert store_page.visible_products() == ["Laptop Pro", "Wireless Mouse"]
    store_page.search("mouse")
    assert store_page.visible_products() == ["Wireless Mouse"]
    store_page.select_category("all")
    assert store_page.visible_products() == ["Wireless Mouse"]


def test_add_to_cart_updates_live_count(store_page):
    store_page.add_product_to_cart("Laptop Pro")
    store_page.add_product_to_cart("SQL Handbook")
    assert store_page.cart_count == "2"


def test_checkout_requires_email_and_confirms_valid_submission(store_page):
    assert store_page.checkout_email_is_required()
    store_page.checkout("")
    assert store_page.checkout_status == ""
    store_page.checkout("customer@example.test")
    assert store_page.checkout_status == "Order placed successfully."


def test_form_controls_have_accessible_labels(store_page):
    assert store_page.driver.find_element(By.CSS_SELECTOR, "label[for='product-search']").is_displayed()
    assert store_page.driver.find_element(By.CSS_SELECTOR, "label[for='checkout-email']").is_displayed()
