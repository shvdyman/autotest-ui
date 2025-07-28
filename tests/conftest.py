import pytest
from playwright.sync_api import sync_playwright, Page

@pytest.fixture(scope="function")
def chromium_page() -> Page:
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page