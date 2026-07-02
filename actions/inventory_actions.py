class InventoryActions:

    def __init__(self, inventory_page):
        self.inventory_page = inventory_page

    def add_product_to_cart(self, product_name):
        """Add a specific product to the cart"""
        return self.inventory_page.add_product_by_name(product_name)

    def remove_product_from_cart(self, product_name):
        """Remove a specific product from the cart"""
        return self.inventory_page.remove_product_by_name(product_name)

    def verify_cart_count(self, expected):
        """Verify cart has expected number of items"""
        actual = self.inventory_page.get_cart_count()
        assert actual == expected, f"Expected {expected} items, but got {actual}"

    def get_cart_count(self):
        """Get current cart count"""
        return self.inventory_page.get_cart_count()

    def verify_inventory_loaded(self):
        """Verify inventory page is loaded"""
        return self.inventory_page.verify_inventory_loaded()

    def get_product_count(self):
        """Get total number of products"""
        return self.inventory_page.get_product_count()