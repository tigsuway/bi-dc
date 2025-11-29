from typing import Optional

from playwright.sync_api import Page
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class BasePage:
    """ Base class for all page objects """

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str) -> None:
        """Navigate to a URL"""
        logger.info(f"Navigating to: {url}")
        self.page.goto(url)

    def click(self, selector: str) -> None:
        """Click an element"""
        logger.info(f"Clicking element: {selector}")
        self.page.click(selector)

    def fill(self, selector: str, text: str) -> None:
        """Fill input field"""
        logger.info(f"Filling '{selector}' with: {text}")
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        """Get text content of an element"""
        logger.info(f"Getting text from: {selector}")
        return self.page.locator(selector).text_content()

    def is_visible(self, selector: str) -> bool:
        """Check if element is visible"""
        return self.page.locator(selector).is_visible()

    def wait_for_selector(self, selector: str, timeout: Optional[int] = None) -> None:
        """Wait for element to be visible"""
        logger.info(f"Waiting for selector: {selector}")
        self.page.wait_for_selector(selector, timeout=timeout)

    def wait_for_url(self, url: str, timeout: Optional[int] = None) -> None:
        """Wait for URL to match"""
        logger.info(f"Waiting for URL: {url}")
        self.page.wait_for_url(url, timeout=timeout)

    def wait_for_load_state(self, state: str = "load") -> None:
        """Wait for page to reach a specific load state"""
        logger.info(f"Waiting for load state: {state}")
        self.page.wait_for_load_state(state)

    def get_current_url(self) -> str:
        """Get current page URL"""
        return self.page.url

    def get_title(self) -> str:
        """Get page title"""
        return self.page.title()

    def take_screenshot(self, name: str) -> None:
        """Take a screenshot"""
        logger.info(f"Taking screenshot: {name}")
        self.page.screenshot(path=f"reports/screenshots/{name}.png")

    def press_key(self, selector: str, key: str) -> None:
        """Press a key on an element"""
        logger.info(f"Pressing key '{key}' on: {selector}")
        self.page.locator(selector).press(key)

    def select_option(self, selector: str, value: str) -> None:
        """Select option from dropdown"""
        logger.info(f"Selecting option '{value}' from: {selector}")
        self.page.select_option(selector, value)

    def check_checkbox(self, selector: str) -> None:
        """Check a checkbox"""
        logger.info(f"Checking checkbox: {selector}")
        self.page.check(selector)

    def uncheck_checkbox(self, selector: str) -> None:
        """Uncheck a checkbox"""
        logger.info(f"Unchecking checkbox: {selector}")
        self.page.uncheck(selector)

    def hover(self, selector: str) -> None:
        """Hover over an element"""
        logger.info(f"Hovering over: {selector}")
        self.page.hover(selector)

    def get_attribute(self, selector: str, attribute: str) -> Optional[str]:
        """Get attribute value of an element"""
        return self.page.locator(selector).get_attribute(attribute)

