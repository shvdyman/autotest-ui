from playwright.sync_api import expect, Page

def test_wrong_email_or_password_authorization(chromium_page: Page):
    # Переходим на страницу авторизации
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    
    # Заполняем форму неверными данными
    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")
    
    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill("password")
    
    # Нажимаем кнопку входа
    login_button = chromium_page.get_by_test_id('login-page-login-button')
    login_button.click()
    
    # Проверяем сообщение об ошибке
    wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")