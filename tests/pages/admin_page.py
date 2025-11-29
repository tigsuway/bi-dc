from playwright.sync_api import Page
from tests.pages.base_page import BasePage


class AdminPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        #Locator
        self.manage_admin_toolbar_link = "a[id='toolbar-item-administration']"
        self.user_link = "a[id='toolbar-item-user']"


    def isAdminPage(self) -> None:
        """ Check if in Homepage """
        self.wait_for_load_state()
        self.is_visible(self.manage_admin_toolbar_link)


    def isUser(self, user: str) -> str:
        """ Get login user """
        return self.get_text(self.user_link)



