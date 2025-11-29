"""
Steps definitions for login feature
"""
import pytest
from playwright.sync_api import Page
from pytest_bdd import scenarios, given, when, then, parsers

from tests.pages.admin_page import AdminPage
from tests.pages.login_page import LoginPage

scenarios('../features/login.feature')


# Given
@given('the user is on login page')
def user_on_login_page(login_page: LoginPage, base_url: str):
    """ Check if user is in login page """
    login_page.open(base_url)
    login_page.isLoginPage()

# When
@when(parsers.parse('the user enters username as "{username}" with password "{password}"'))
def login_with_credentials(login_page: LoginPage, username: str, password: str):
    """ Enter user credentials and click login"""
    login_page.login(username, password)


@when('the user enters admin credentials')
def login_with_admin_credentials(login_page: LoginPage, admin_credentials):
    login_page.login(
        username=admin_credentials["user"],
        password=admin_credentials["pass"]
    )


# Then
@then('the user should be redirected to admin page')
def redirected_to_admin_page(admin_page: AdminPage):
    """ Verify if the user is in admin page"""
    admin_page.isAdminPage()


@then('the user is still in login page')
def is_still_in_login_page(login_page: LoginPage):
    """ Check if user still in login page """
    login_page.isLoginPage()