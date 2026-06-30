from pytest_bdd import given, scenarios, then, when

from pages.login_page import LoginPage
from test_data.login_data import LoginData

scenarios("login.feature")


@given("The User Opens The Swag Labs Application")
def open_application(page):

    login_page = LoginPage(page)

    login_page.open_application()


@when("The User Enters Valid Login Credentials")
def enter_credentials(page):

    login_page = LoginPage(page)

    login_page.enter_username(LoginData.VALID_USERNAME)

    login_page.enter_password(LoginData.VALID_PASSWORD)


@when("The User Clicks The Login Button")
def click_login(page):

    login_page = LoginPage(page)

    login_page.click_login()


@then("The User Should See The Inventory Page")
def verify_inventory_page(page):

    login_page = LoginPage(page)

    assert login_page.verify_inventory_page()
