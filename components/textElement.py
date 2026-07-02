from components.base_component import BaseComponent


class Label(BaseComponent):

    def is_visible(self):
        self.logger.info(f"Verifying '{self.name}' is visible")
        return self.locator.is_visible()

    def get_text(self):
        self.wait_until_visible()
        self.logger.info(f"Reading text from '{self.name}'")
        return self.locator.inner_text()