import os
import time

import pytest

from pages.sandbox.employee_profile_page import EmployeeProfilePage
from pages.sandbox.employees_page import EmployeesPage
from pages.sandbox.login_page import LoginPage


class TestPositiveScenarios:
    @pytest.mark.employee
    @pytest.mark.positive
    def test_edit_profile_page(self, driver):
        login_page = LoginPage(driver)
        employee_page = EmployeesPage(driver)
        employee_profile_page = EmployeeProfilePage(driver)

        login_page.open()
        login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])

        employee_page.open()
        employee_page.click()

        random_title = employee_profile_page.generate_random_job_title()
        employee_profile_page.set_job_title(random_title)
        time.sleep(5)
        employee_profile_page.click_save()

        assert employee_profile_page.is_employee_job_title_displayed()
        assert employee_profile_page.get_job_title() == random_title