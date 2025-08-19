import os

import pytest

from pages.sandbox.employees_page import EmployeesList
from pages.sandbox.login_page import LoginPage


class TestPositiveScenarios:
    @pytest.mark.employee
    @pytest.mark.positive
    def test_get_list_employees(self, driver):
        login_page = LoginPage(driver)
        employees_page = EmployeesList(driver)

        login_page.open()
        login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])

        employees_page.open()
        employees = employees_page.get_list_of_employees()

        employees_name = [emp.name for emp in employees]

        assert employees_name == [
            "Abigail Peterson",
            "Anita Oliver",
            "Audrey Peterson",
            "Beth Evans",
            "Doris Cole",
            "Eli Lambert",
            "Ernest Reed",
            "Jeffrey Kelly",
            "Jennie Fletcher",
            "Keith Byrd",
            "Marc Demo",
            "Mitchell Admin",
            "Paul Williams",
            "Rachel Perry",
            "Randall Lewis",
            "Ronnie Hart",
            "Sharlene Rhodes",
            "Tina Williamson",
            "Toni Jimenez",
            "Walter Horton",
        ]