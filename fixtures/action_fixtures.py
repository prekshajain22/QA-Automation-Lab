import pytest

from actions.inventory_actions import InventoryActions
from actions.login_actions import LoginActions


@pytest.fixture
def login_actions(login_page, users):
    return LoginActions(login_page, users)


@pytest.fixture
def inventory_actions(inventory_page):
    return InventoryActions(inventory_page)
