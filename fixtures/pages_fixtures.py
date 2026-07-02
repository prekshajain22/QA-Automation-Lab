import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)
