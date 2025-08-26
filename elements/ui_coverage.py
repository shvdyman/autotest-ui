from playwright.sync_api import sync_playwright

# Импортируем основные компоненты инструмента:
# - UICoverageTracker — основной класс для трекинга
# - SelectorType — тип селектора (CSS, XPATH и другие)
# - ActionType — тип действия (CLICK, FILL, CHECK_VISIBLE и другие)
from ui_coverage_tool import UICoverageTracker, SelectorType, ActionType

# Создаём экземпляр трекера. 
# Значение `app` — это ключ приложения (должно совпадать с ключом в конфиге UI_COVERAGE_APPS)
tracker = UICoverageTracker(app="ui-course")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("https://my-ui-app.com/login")
    
    # Вводим логин
    username_input = page.locator("#username-input")
    username_input.fill('user@example.com')

    # Фиксируем это действие в трекере
    tracker.track_coverage(
        selector='#username-input',  # CSS-селектор
        action_type=ActionType.FILL,  # Тип действия: ввод текста (FILL)
        selector_type=SelectorType.CSS  # Тип селектора: CSS
    )
    
    # Нажимаем на кнопку входа
    login_button = page.locator('//button[@id="login-button"]')
    login_button.click()

    # И снова фиксируем это действие
    tracker.track_coverage(
        selector='//button[@id="login-button"]',  # XPath-селектор
        action_type=ActionType.CLICK,  # Тип действия: клик
        selector_type=SelectorType.XPATH  # Тип селектора: XPath
    )
