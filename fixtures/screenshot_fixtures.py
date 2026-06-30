import os

import pytest


@pytest.fixture(autouse=True)
def capture_screenshot_on_failure(page, request):

    yield

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshot_dir = "screenshots"

        os.makedirs(screenshot_dir, exist_ok=True)

        screenshot_path = f"{screenshot_dir}/{request.node.name}.png"

        page.screenshot(path=screenshot_path, full_page=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)
