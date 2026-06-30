import pytest
from playwright.sync_api import Playwright

from utils.logger import get_logger

logger = get_logger()
logger.info("Test execution started")


@pytest.fixture(scope="function")
def page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)

    page = browser.new_page()

    yield page

    browser.close()
