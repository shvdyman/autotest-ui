from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent

class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # Вложенный компонент меню
        self.menu = CourseViewMenuComponent(page)

        self.title = page.get_by_test_id('course-widget-title-text')
        self.image = page.get_by_test_id('course-preview-image')
        self.max_score_text = page.get_by_test_id('course-max-score-info-row-view-text')
        self.min_score_text = page.get_by_test_id('course-min-score-info-row-view-text')
        self.estimated_time_text = page.get_by_test_id('course-estimated-time-info-row-view-text')