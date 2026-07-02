from pytest_bdd import parsers, scenarios, then, when

scenarios("add_to_cart.feature")


@when(parsers.parse('I Add "{product_name}" To Cart'))
def add_to_cart(inventory_actions, product_name):
    inventory_actions.add_product_to_cart(product_name)


@then(parsers.parse('I Should See Cart Count As "{expected_count}"'))
def verify_cart_count(inventory_actions, expected_count):
    inventory_actions.verify_cart_count(int(expected_count))
