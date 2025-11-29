import pytest
from playwright.sync_api import Page

from tests.pages.admin_page import AdminPage
from tests.pages.login_page import LoginPage


# Registering options
def pytest_addoption(parser):
    parser.addini("admin_user", "Admin user for tests")
    parser.addini("admin_pass", "Admin password for tests")


# Fixtures for page objects
@pytest.fixture
def login_page(page: Page):
    """ Create login page instance """
    yield LoginPage(page)
    page.close()
    print(page.is_closed())

@pytest.fixture
def admin_page(page: Page):
    """ Create login page instance """
    yield AdminPage(page)
    page.close()
    print(page.is_closed())


@pytest.fixture(scope="function")
def admin_credentials(pytestconfig):
    admin_user = pytestconfig.getini("admin_user")
    admin_pass = pytestconfig.getini("admin_pass")
    return {"user": admin_user, "pass": admin_pass}