from config.environment import BASE_URL
from locators.login_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        print("LoginPage created")

    def open_application(self):
        self.open_url(BASE_URL)

    def enter_username(self, username):
        self.enter_text(LoginLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(LoginLocators.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(LoginLocators.LOGIN_BUTTON)

    def verify_inventory_page(self):
        return self.is_visible(LoginLocators.INVENTORY_CONTAINER)
