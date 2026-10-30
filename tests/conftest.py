from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from web_automation.pages.store_page import StorePage


@pytest.fixture
def store_page():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1440,1000")
    driver = webdriver.Chrome(options=options)
    try:
        page = StorePage(driver)
        fixture = Path(__file__).parent / "assets" / "storefront.html"
        page.open(fixture.resolve().as_uri())
        yield page
    finally:
        driver.quit()
