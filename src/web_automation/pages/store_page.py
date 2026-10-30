from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class StorePage:
    TITLE = (By.CSS_SELECTOR, "h1")
    SEARCH = (By.ID, "product-search")
    CATEGORY = (By.ID, "category-filter")
    PRODUCT_CARDS = (By.CSS_SELECTOR, "[data-testid='product-card']")
    EMPTY_STATE = (By.ID, "empty-state")
    CART_COUNT = (By.ID, "cart-count")
    CHECKOUT_EMAIL = (By.ID, "checkout-email")
    CHECKOUT_SUBMIT = (By.CSS_SELECTOR, "#checkout-form button[type='submit']")
    CHECKOUT_STATUS = (By.ID, "checkout-status")

    def __init__(self, driver, timeout: int = 5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, file_url: str) -> "StorePage":
        self.driver.get(file_url)
        self.wait.until(EC.visibility_of_element_located(self.TITLE))
        return self

    @property
    def title(self) -> str:
        return self.driver.find_element(*self.TITLE).text

    def search(self, term: str) -> None:
        field = self.driver.find_element(*self.SEARCH)
        field.clear()
        field.send_keys(term)

    def select_category(self, category: str) -> None:
        from selenium.webdriver.support.ui import Select

        Select(self.driver.find_element(*self.CATEGORY)).select_by_value(category)

    def visible_products(self) -> list[str]:
        return [
            card.find_element(By.CSS_SELECTOR, "h2").text
            for card in self.driver.find_elements(*self.PRODUCT_CARDS)
            if card.is_displayed()
        ]

    def empty_state_visible(self) -> bool:
        return self.driver.find_element(*self.EMPTY_STATE).is_displayed()

    def add_product_to_cart(self, product_name: str) -> None:
        cards = self.driver.find_elements(*self.PRODUCT_CARDS)
        for card in cards:
            if card.find_element(By.CSS_SELECTOR, "h2").text == product_name:
                card.find_element(By.CSS_SELECTOR, "button.add-to-cart").click()
                return
        raise AssertionError(f"Product not found: {product_name}")

    @property
    def cart_count(self) -> str:
        return self.driver.find_element(*self.CART_COUNT).text

    def checkout(self, email: str) -> None:
        self.driver.find_element(*self.CHECKOUT_EMAIL).send_keys(email)
        self.driver.find_element(*self.CHECKOUT_SUBMIT).click()

    @property
    def checkout_status(self) -> str:
        return self.wait.until(
            EC.visibility_of_element_located(self.CHECKOUT_STATUS)
        ).text

    def checkout_email_is_required(self) -> bool:
        return self.driver.find_element(*self.CHECKOUT_EMAIL).get_attribute("required") is not None
