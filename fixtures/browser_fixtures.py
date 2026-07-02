import pytest
from playwright.sync_api import Playwright

from config.environment import BROWSER, HEADLESS, SLOW_MO


@pytest.fixture(scope="function")
def page(playwright: Playwright):

    browser_type = getattr(playwright, BROWSER)

    browser = browser_type.launch(
        headless=HEADLESS,
        slow_mo=SLOW_MO,
    )

    page = browser.new_page()

    yield page

    browser.close()
