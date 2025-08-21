from playwright.sync_api import Locator, expect
from elements.base_element import BaseElement
import allure

class Textarea(BaseElement):
    @property
    def type_of(self) -> str:
        return
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator('textarea').first

    def fill(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f'Fill {self.type_of} "{self.name}" to value "{value}"'):            
            locator = self.get_locator(nth, **kwargs)
            locator.fill(value)

    def check_value(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" has a value "{value}"'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_text(value)  # Заменили to_have_value() на to_have_text()