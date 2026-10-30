"""Independent Playwright smoke checks for the local demo storefront."""
from pathlib import Path

import pytest

playwright = pytest.importorskip("playwright.sync_api")
from playwright.sync_api import sync_playwright


def test_playwright_storefront_search_and_checkout():
    page_file = Path(__file__).parent / "assets" / "storefront.html"
    with sync_playwright() as p:
        browser = p.chromium.launch()
        try:
            page = browser.new_page()
            page.goto(page_file.resolve().as_uri())
            assert page.locator("h1").inner_text() == "Demo Storefront"
            page.locator("#product-search").fill("laptop")
            assert page.locator("[data-testid='product-card']:visible h2").all_inner_texts() == ["Laptop Pro"]
            page.locator("#product-search").fill("")
            page.locator("#checkout-email").fill("qa@example.test")
            page.locator("#checkout-form button[type='submit']").click()
            assert page.locator("#checkout-status").inner_text() == "Order placed successfully."
        finally:
            browser.close()
