import pytest

from playwright.sync_api import sync_playwright, Page, playwright, Playwright


@pytest.fixture(scope="session",autouse=True)
def initialize_browser_state(playwright: Playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.fixture(scope="session",autouse=True)
def chromium_page_with_state(initialize_browser_state, playwright: Playwright): -> Page:
        browser = initialize_browser_state