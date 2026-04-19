from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login", wait_until="networkidle")

    # unknown = page.locator("#unknown")
    # expect(unknown).to_be_visible()
    #
    # login_button = page.get_by_test_id("login-page-registration-link")
    # login_button.fill("unknown")

    text = "ChangeText"

    page.evaluate(
        """
        const titleReplace = (text) => {
        const title = document.getElementById('authentication-ui-course-title-text')
        title.textContent = text
    }
        """
    )

    page.wait_for_timeout(5000)