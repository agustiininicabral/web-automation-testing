# Web Automation Testing Framework

A browser-based functional and regression testing project built with Selenium, pytest and the Page Object Model. It tests a small accessible demo storefront in a real headless Chromium browser.

## What it demonstrates

- Selenium WebDriver setup and deterministic browser lifecycle.
- Page Object Model with reusable locators and actions.
- Functional tests for search, category filters, cart updates and checkout validation.
- Assertions on visible content, empty states and accessible labels.
- Headless Chrome execution in GitHub Actions across Python 3.11–3.13.
- No external website dependency: tests run against a local HTML fixture.

## Run locally

Install Google Chrome, then:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

Selenium Manager resolves a compatible ChromeDriver. On CI, the workflow provisions Chrome before running the suite.

## Test scenarios

1. Storefront loads with the expected page title and products.
2. Search filters products and displays an empty state for no matches.
3. Category filtering works and can be reset.
4. Adding products updates the cart count.
5. Checkout requires a valid email and displays a confirmation after submission.
6. Form controls expose accessible labels.

## Structure

- `tests/assets/storefront.html`: self-contained demo web app used as the test target.
- `src/web_automation/pages/store_page.py`: Page Object Model.
- `tests/conftest.py`: browser fixture and teardown.
- `tests/test_storefront.py`: functional regression tests.
- `.github/workflows/ci.yml`: browser-based CI matrix.

## Limitations

The demo app is a local test fixture, not a production commerce application. The suite demonstrates browser automation patterns; selectors and test data would be adapted to the real application under test.

## License

MIT. See [LICENSE](LICENSE).
