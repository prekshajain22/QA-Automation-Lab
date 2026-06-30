from utils.logger import get_logger


class BasePage:
    def __init__(self, page):

        self.page = page
        self.logger = get_logger()

    def open_url(self, url):

        self.logger.info(f"Opening URL: {url}")

        self.page.goto(url)

    def click(self, locator):

        self.logger.info(f"Clicking element: {locator}")

        self.page.locator(locator).click()

    def enter_text(self, locator, text):

        self.logger.info(f"Entering text in: {locator}")

        self.page.locator(locator).fill(text)

    def is_visible(self, locator):

        self.logger.info(f"Checking visibility: {locator}")

        return self.page.locator(locator).is_visible()
