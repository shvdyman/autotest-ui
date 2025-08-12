from playwright.sync_api import Page

from components.base_component import BaseComponent


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = page.get_by_test_id('course-view-menu-button')
        self.edit_menu_item = page.get_by_test_id('course-view-edit-menu-item')
        self.delete_menu_item = page.get_by_test_id('course-view-delete-menu-item')