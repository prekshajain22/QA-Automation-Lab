from pytest_bdd import given, parsers, scenarios, then, when

scenarios("login.feature")

@given("I Open The Application")
def open_application(login_page):
    login_page.open_application()


@when(parsers.parse('I Login Using User "{user_type}"'))
def login_using_user(login_page, users, user_type):
    user = users[user_type]
    login_page.login(user["username"], user["password"])


@then("I Should See The Inventory Page")
def verify_inventory_page(login_page):
    assert login_page.verify_inventory_page()
