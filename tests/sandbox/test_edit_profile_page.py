import pytest

from pages.sandbox.employee_profile_page import EmployeeProfilePage
from pages.sandbox.employees_page import EmployeesList
from utils import data_factory


class TestPositiveScenarios:
    @pytest.mark.employee
    @pytest.mark.positive
    def test_edit_profile_page(self, driver, signed_as_admin):
        employees_page = EmployeesList(driver)
        employee_profile_page = EmployeeProfilePage(driver, employee_id=6)
        employee_profile_page.open()

        employees_page.open()
        employees_page.click()

        employee_profile_page.set_job_title(data_factory.random_job_title())
        employee_profile_page.click_save()

        assert employee_profile_page.is_employee_job_title_displayed()