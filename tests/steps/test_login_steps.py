"""
Steps definitions for login feature
"""
import pytest
from playwright.sync_api import Page
from pytest_bdd import scenarios, given, when, then, parsers

from tests.pages.admin_page import AdminPage
from tests.pages.login_page import LoginPage

scenarios('../features/login.feature')


# Fixtures for page objects
@pytest.fixture
def login_page(page: Page):
    """ Create login page instance """
    return LoginPage(page)

@pytest.fixture
def admin_page(page: Page):
    """ Create login page instance """
    return AdminPage(page)

# Given
@given('the user is on login page')
def user_on_login_page(login_page: LoginPage, base_url: str):
    """ Check if user is in login page """
    login_page.open(f"{base_url}")
    login_page.isLoginPage()

# When
@when(parsers.parse('the user enters username as "{username}" with password "{password}"'))
def login_with_credentials(login_page: LoginPage, username: str, password: str):
    """ Enter user credentials and click login"""
    login_page.login(username, password)


# Then
@then('the user should be redirected to admin page')
def redirected_to_admin_page(admin_page: AdminPage):
    """ Verify if the user is in admin page"""
    admin_page.isAdminPage()


@then('the user is still in login page')
def is_still_in_login_page(login_page: LoginPage):
    """ Check if user still in login page """
    login_page.isLoginPage()