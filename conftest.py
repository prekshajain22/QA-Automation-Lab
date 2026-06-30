from utils.logger import get_logger


def pytest_sessionstart(session):
    logger = get_logger()
    logger.info("Test execution started")


pytest_plugins = [
    "fixtures.browser_fixtures",
    "fixtures.data_fixtures",
    "fixtures.pages_fixtures",
    "fixtures.screenshot_fixtures",
]
