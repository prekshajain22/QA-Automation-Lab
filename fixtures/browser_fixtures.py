import pytest
from playwright.sync_api import Playwright

from constants.browser_constants import HEADLESS, SLOW_MO


@pytest.fixture(scope="function")
def page(playwright: Playwright):

    browser = playwright.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)

    page = browser.new_page()

    yield page

    browser.close()
