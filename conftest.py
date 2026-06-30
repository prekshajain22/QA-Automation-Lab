import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="function")
def page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)

    page = browser.new_page()

    yield page

    browser.close()