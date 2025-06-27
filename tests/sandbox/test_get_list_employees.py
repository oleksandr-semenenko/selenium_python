import os

import pytest

from pages.sandbox.employee_page import EmployeePage
from pages.sandbox.login_page import LoginPage


class TestPositiveScenarios:
    @pytest.mark.employee
    @pytest.mark.positive
    def test_get_list_employee(self, driver):
        login_page = LoginPage(driver)
        employee_page = EmployeePage(driver)

        login_page.open()
        login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])

        employee_page.open()
        employees = employee_page.get_list_of_employees()

        employee_names = [emp.name for emp in employees]

        actual_employees = [
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

        assert (
            actual_employees == employee_names
        ), f"The lists do not match!\nExpected: {actual_employees}\nActual: {employees}"
