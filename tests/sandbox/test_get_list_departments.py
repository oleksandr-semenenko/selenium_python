import os

import pytest

from pages.sandbox.department_page import DepartmentList
from pages.sandbox.login_page import LoginPage


class TestPositiveScenarios:
    @pytest.mark.department
    @pytest.mark.positive
    #@pytest.mark.skip("Test under development")
    def test_get_list_employees(self, driver):
        login_page = LoginPage(driver)

        department_page = DepartmentList(driver)

        login_page.open()
        login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])

        department_page.open()
        department_page.wait_page_is_present()
        departments = department_page.get_list_of_departments()

        departments_name = [dep.name for dep in departments]

        assert departments_name == [
            "Administration",
            "Long Term Projects",
            "Management",
            "Professional Services",
            "R&D USA",
            "Research & Development",
            "Sales",
        ]