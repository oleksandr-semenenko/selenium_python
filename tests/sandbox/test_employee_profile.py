import os

import pytest

from pages.sandbox.employee_profile_page import EmployeeProfilePage
from pages.sandbox.employees_page import EmployeesPage
from pages.sandbox.login_page import LoginPage


class TestPositiveScenarios:
    @pytest.mark.employee
    @pytest.mark.positive
    def test_get_employee_profile(self, driver):
        login_page = LoginPage(driver)
        employees_page = EmployeesPage(driver)
        employee_profile_page = EmployeeProfilePage(driver)

        login_page.open()
        login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])

        employees_page.open()
        employees_page.click()

        assert employee_profile_page.is_employee_name_displayed()