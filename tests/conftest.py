import pytest

from playwright.sync_api import sync_playwright, Page, playwright

@pytest.fixture
def chromium_page(playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()