import os

import pytest

from pages.sandbox.employee_profile_page import EmployeeProfilePage
from pages.sandbox.employees_page import EmployeesList
from pages.sandbox.login_page import LoginPage


class TestPositiveScenarios:
    @pytest.mark.employee
    @pytest.mark.positive
    def test_edit_profile_page(self, driver, signed_in_user):
        login_page = LoginPage(driver)
        employees_page = EmployeesList(driver)
        employee_profile_page = EmployeeProfilePage(driver)

        # login_page.open()
        # login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])

        employees_page.open()
        employees_page.click()

        random_title = employee_profile_page.generate_random_job_title()
        employee_profile_page.set_job_title(random_title)
        employee_profile_page.click_save()

        assert employee_profile_page.is_employee_job_title_displayed()
        assert employee_profile_page.get_job_title() == random_title
