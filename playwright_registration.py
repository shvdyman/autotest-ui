from playwright.sync_api import sync_playwright, expect
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    login_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(login_email_input).to_be_visible()
    login_email_input.fill('user.name@gmail.com')
    login_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    expect(login_username_input).to_be_visible()
    login_username_input.fill('username')
    login_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(login_password_input).to_be_visible
    login_password_input.fill('password')
    registration_link = page.get_by_test_id("registration-page-registration-button")
    registration_link.click()
    dashboard_view = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_view).to_have_text('Dashboard')
