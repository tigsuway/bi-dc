import pytest
from playwright.sync_api import Page

from tests.pages.admin_page import AdminPage
from tests.pages.login_page import LoginPage
from tests.utils.drupal_api import DrupalAPIUtils


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


@pytest.fixture
def admin_page(page: Page):
    """ Create login page instance """
    yield AdminPage(page)
    page.close()


@pytest.fixture()
def admin_credentials(pytestconfig):
    admin_user = pytestconfig.getini("admin_user")
    admin_pass = pytestconfig.getini("admin_pass")
    return {"user": admin_user, "pass": admin_pass}


@pytest.fixture()
def drupal_api(pytestconfig, admin_credentials):
    """ Create Drupal API instance """
    base_url = pytestconfig.getini("base_url")
    username = admin_credentials['user']
    password = admin_credentials['pass']

    yield DrupalAPIUtils(
        base_url=base_url,
        username=username,
        password=password,
    )



