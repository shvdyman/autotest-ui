import pytest

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(dashboard_page: DashboardPage, registration_page: RegistrationPage):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(
        email="User.name@gmail.com",
        username="Username",
        password="Password"
    )
    registration_page.click_registration_button()

    dashboard_page.check_visible_dashboard_title()