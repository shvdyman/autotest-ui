from playwright.sync_api import Page, expect # Импортируем класс Page
from typing import Pattern

class BasePage:
     # Конструктор класса, принимающий объект Page
    def __init__(self, page: Page):
        self.page = page # Присваиваем объект page атрибуту класса

    def visit (self, url: str):
        self.page.goto(url, wait_until='networkidle')

    def reload(self):
        self.page.reload(wait_until='networkidle')

    def check_current_url(self, expected_url: Pattern[str]):
        expect(self.page).to_have_url(expected_url)