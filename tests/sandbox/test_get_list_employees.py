import os

import pytest

from pages.sandbox.employees_page import EmployeesList
from pages.sandbox.login_page import LoginPage


class TestPositiveScenarios:
    @pytest.mark.employee
    @pytest.mark.order(2)
    @pytest.mark.positive
    def test_get_list_employees(self, driver):
        login_page = LoginPage(driver)

        employees_page = EmployeesList(driver)

        login_page.open()
        login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])

        employees_page.open()
        employees = employees_page.get_list_of_employees()
        employees_page.wait_page_is_present()

        employees_name = [emp.name for emp in employees]

        expected = [
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

        missing = [name for name in expected if name not in employees_name]
        extra = [name for name in employees_name if name not in expected]

        if missing or extra:
            print("Employee list mismatch detected")
            if missing:
                print(f"Missing expected names: {missing}")
            if extra:
                print(f"Unexpected extra names: {extra}")
            print(f"Actual employees: {employees_name}")

        assert not missing, f"Missing employees: {missing}"


    @pytest.mark.employee
    @pytest.mark.positive
    def test_find_employee_by_name(self, driver):
        login_page = LoginPage(driver)

        employees_page = EmployeesList(driver)

        login_page.open()
        login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])

        employees_page.open()

        employee_name = "Marc Demo"
        employees = employees_page.get_list_of_employees()
        employee_names = [emp.name for emp in employees]

        try:
            employee_id = employees_page.get_employee_id_by_name(employee_name)
        except ValueError:
            print(f"Employee name not found: {employee_name}")
            print(f"Available employees: {employee_names}")
            raise

        assert isinstance(employee_id, int) and employee_id > 0
        assert employee_name in employee_names

