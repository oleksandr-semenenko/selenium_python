import os

import pytest

from pages.sandbox.employees_page import EmployeesPage
from pages.sandbox.login_page import LoginPage


class TestPositiveScenarios:
    @pytest.mark.employee
    @pytest.mark.positive
    def test_get_list_employees(self, driver):
        login_page = LoginPage(driver)
        employees_page = EmployeesPage(driver)

        login_page.open()
        login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])

        employees_page.open()
        employees = employees_page.get_list_of_employees()

        employees_name = [emp.name for emp in employees]
        job_titles = [emp.job_title for emp in employees]

        # expected_names = [
        #     "Abigail Peterson",
        #     "Anita Oliver",
        #     "Audrey Peterson",
        #     "Beth Evans",
        #     "Doris Cole",
        #     "Eli Lambert",
        #     "Ernest Reed",
        #     "Jeffrey Kelly",
        #     "Jennie Fletcher",
        #     "Keith Byrd",
        #     "Marc Demo",
        #     "Mitchell Admin",
        #     "Paul Williams",
        #     "Rachel Perry",
        #     "Randall Lewis",
        #     "Ronnie Hart",
        #     "Sharlene Rhodes",
        #     "Tina Williamson",
        #     "Toni Jimenez",
        #     "Walter Horton",
        # ]
        #
        # expected_titles = [
        #     "Consultant",
        #     "Experienced Developer",
        #     "Consultant",
        #     "Experienced Developer",
        #     "Consultant",
        #     "Marketing and Community Manager",
        #     "Consultant",
        #     "Marketing and Community Manager",
        #     "Experienced Developer",
        #     "Experienced Developer",
        #     "Experienced Developer",
        #     "Chief Executive Officer",
        #     "Experienced Developer",
        #     "Marketing and Community Manager",
        #     "Experienced Developer",
        #     "Team Leader",
        #     "Experienced Developer",
        #     "Human Resources Manager",
        #     "Consultant",
        #     "Experienced Developer",
        # ]
        #
        # assert employees_name == expected_names
        # assert job_titles == expected_titles

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

        assert job_titles == [
            "Consultant",
            "Experienced Developer",
            "Consultant",
            "Experienced Developer",
            "Consultant",
            "Marketing and Community Manager",
            "Consultant",
            "Marketing and Community Manager",
            "Experienced Developer",
            "Experienced Developer",
            "Experienced Developer",
            "Chief Executive Officer",
            "Experienced Developer",
            "Marketing and Community Manager",
            "Experienced Developer",
            "Team Leader",
            "Experienced Developer",
            "Human Resources Manager",
            "Consultant",
            "Experienced Developer",
        ]


        # employee_names = [emp.name for emp in employees]
        #
        #
        # actual_employees = [
        #     "Abigail Peterson",
        #     "Anita Oliver",
        #     "Audrey Peterson",
        #     "Beth Evans",
        #     "Doris Cole",
        #     "Eli Lambert",
        #     "Ernest Reed",
        #     "Jeffrey Kelly",
        #     "Jennie Fletcher",
        #     "Keith Byrd",
        #     "Marc Demo",
        #     "Mitchell Admin",
        #     "Paul Williams",
        #     "Rachel Perry",
        #     "Randall Lewis",
        #     "Ronnie Hart",
        #     "Sharlene Rhodes",
        #     "Tina Williamson",
        #     "Toni Jimenez",
        #     "Walter Horton",
        # ]
        #
        # assert (
        #     actual_employees == employee_names
        # )
