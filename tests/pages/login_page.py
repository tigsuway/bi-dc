from playwright.sync_api import Page
from tests.pages.base_page import BasePage


class LoginPage(BasePage):
    """ Login page object """

    def __init__(self, page: Page):
        super().__init__(page)

        # Locators
        self.username_input = "input[id='edit-name']"
        self.password_input = "input[id='edit-pass']"
        self.login_button = "input[id='edit-submit']"
        self.username_label = "label[id='edit-name--label'] span"
        self.password_label = "label[id='edit-pass--label'] span"

    def open(self, base_url: str) -> None:
        """ Open login page """
        self.navigate(f"{base_url}/user/login")


    def isLoginPage(self) -> None:
        """ Check if in Login page"""
        self.is_visible(self.username_label)
        self.is_visible(self.password_label)


    def login(self, username: str, password: str) -> None:
        """ Perform login action """
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)









