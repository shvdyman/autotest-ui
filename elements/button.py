from playwright.sync_api import expect
import allure
from elements.base_element import BaseElement


class Button(BaseElement):
    def type_of(self) -> str:
        return "button"
    
    @property
    def check_enabled(self, nth: int = 0, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" is enabled'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_enabled()
    
    def check_disabled(self, nth: int = 0, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" is disabled'):
            # Добавили аргумент nth и передеаем его в get_locator
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_disabled()