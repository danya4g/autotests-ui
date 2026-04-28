from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list(initialize_browser_state, Page):
        initialize_browser_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = initialize_browser_state.get_by_test_id("registration-form-email-input").locator("input")
        email_input.hover()
        email_input.click()
        email_input.fill("user@gmail.com")

        username_input = initialize_browser_state.get_by_test_id("registration-form-username-input").locator("input")
        username_input.hover()
        username_input.click()
        username_input.fill("username")

        password_input = initialize_browser_state.get_by_test_id("registration-form-password-input").locator("input")
        password_input.hover()
        password_input.click()
        password_input.fill("password")

        registration_button = initialize_browser_state.get_by_test_id("registration-page-registration-button")
        registration_button.click()

        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        header_courses = page.get_by_test_id("courses-list-toolbar-title-text")
        expect(header_courses).to_be_visible()
        expect(header_courses).to_have_text("Courses")

        icon = page.get_by_test_id("courses-list-empty-view-icon")
        expect(icon).to_be_visible()

        result_block = page.get_by_test_id("courses-list-empty-view-title-text")
        expect(result_block).to_be_visible()
        expect(result_block).to_have_text("There is no results")

        pipeline_result = page.get_by_test_id("courses-list-empty-view-description-text")
        expect(pipeline_result).to_be_visible()
        expect(pipeline_result).to_have_text("Results from the load test pipeline will be displayed here")