# Web Automation Testing Framework

A browser-based functional and regression testing project built with Selenium, Playwright, pytest and the Page Object Model. It tests a self-contained demo storefront in real Chromium browsers.

## What it demonstrates

- Selenium WebDriver setup and deterministic browser lifecycle.
- Page Object Model with reusable locators and actions.
- Functional and regression scenarios for search, category filters, cart updates, checkout and accessibility labels.
- A separate Playwright Chromium E2E smoke test for rendering, search and checkout.
- Headless Chrome execution in GitHub Actions across Python 3.11–3.13.
- Playwright Chromium execution in a dedicated CI job.
- No external website dependency: tests run against a local HTML fixture.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -e ".[dev]"
python -m playwright install chromium
pytest
```

Selenium Manager resolves a compatible ChromeDriver. Playwright installs its own Chromium browser. Both suites use the same local fixture.

## Test scenarios

1. Storefront renders the expected title and products.
2. Search filters products and displays an empty state.
3. Category filtering works and combines with search.
4. Adding products updates the cart count.
5. Checkout rejects invalid/empty email and confirms valid submission.
6. Form controls expose accessible labels.
7. Playwright independently verifies browser rendering, search and checkout.

## Structure

- `tests/assets/storefront.html`: self-contained demo app.
- `src/web_automation/pages/store_page.py`: Selenium Page Object Model.
- `tests/test_storefront.py`: Selenium functional/regression suite.
- `tests/test_playwright_smoke.py`: Playwright E2E smoke.
- `PLAYWRIGHT.md`: separate setup instructions.
- `.github/workflows/ci.yml`: Selenium matrix and Playwright CI.

## Limitations

The demo app is a local test fixture, not a production commerce application. The suite demonstrates browser automation patterns; selectors and test data must be adapted to the real application under test. Tests do not claim to validate a live third-party site.

## License

MIT. See [LICENSE](LICENSE).
