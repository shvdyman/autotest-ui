from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(email_input).to_be_visible()
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    expect(username_input).to_be_visible()
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(password_input).to_be_visible
    password_input.fill('password')

    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text('Dashboard')