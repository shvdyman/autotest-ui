from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration():
    with sync_playwright() as playwright:
        # Launch browser and create context
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to registration page
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        # Fill registration form
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        # Click registration button and wait for navigation
        with page.expect_navigation():
            registration_button = page.get_by_test_id('registration-page-registration-button')
            registration_button.click()

        # Verify we're on dashboard page
        expect(page).to_have_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
        
        # Save state
        context.storage_state(path='browser_state.json')
        
        # Close context
        context.close()

    # Second part - verify saved state works
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        # Navigate to dashboard and verify
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
        expect(page).to_have_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
        
        # Add any additional assertions for dashboard content
        # For example:
        # expect(page.get_by_text('Welcome')).to_be_visible()
        
        # Close context
        context.close()