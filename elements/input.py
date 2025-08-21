from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement
import allure

class Input(BaseElement):
    @property
    def type_of(self) -> str:
        return "input"
    
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        # Добавили аргумент nth и передаем его в get_locator
        return super().get_locator(nth, **kwargs).locator('input')

    def fill(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f'Fill {self.type_of} "{self.name}" to value "{value}"'):    
            # Добавили аргумент nth и передаем его в get_locator
            locator = self.get_locator(nth, **kwargs)
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" has a value "{value}"'):
            # Добавили аргумент nth и передаем его в get_locator
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_value(value)