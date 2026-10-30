# Playwright E2E extension

The primary regression suite remains Selenium + pytest. An additional independent Playwright smoke test covers storefront rendering, search and checkout.

Install and run:

```bash
pip install -e ".[dev]"
pip install playwright
python -m playwright install chromium
pytest -q tests/test_playwright_smoke.py
```

The Playwright test uses the same local HTML fixture as Selenium; it does not depend on a third-party website. Chromium must be installed with the Playwright command above.
