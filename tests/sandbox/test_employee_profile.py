import os

import pytest

from pages.sandbox import new_employee_profile_page, employee_profile_page
from pages.sandbox.employee_profile_page import EmployeeProfilePage
from pages.sandbox.employees_page import EmployeesList
from pages.sandbox.login_page import LoginPage
from pages.sandbox.new_employee_profile_page import NewEmployeeProfilePage
from utils.data_factory import generate_random_name, generate_random_job_title


class TestPositiveScenarios:
    @pytest.mark.employee
    @pytest.mark.positive
    def test_get_employee_profile(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])

        employees_page = EmployeesList(driver)
        employee_profile_page = EmployeeProfilePage(driver, employee_id=6)
        employee_profile_page.open()

        employees_page.open()
        employees_page.click()
        employee_profile_page.wait_page_is_present()

        assert employee_profile_page.is_employee_name_displayed()

    # New test about creat new employee profile
    @pytest.mark.employee
    @pytest.mark.positive
    @pytest.mark.skip("Test under development")
    def test_create_employee_profile(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])

        employees_page = EmployeesList(driver)
        employees_page.open()
        employees_page.click_new_employee_button()

        new_employee_page = NewEmployeeProfilePage(driver)
        new_employee_page.open()
        new_employee_page.wait_page_is_present()

        set_name_employee = generate_random_name()
        new_employee_page.set_employee_name(set_name_employee)

        job_title = generate_random_job_title()
        new_employee_page.set_job_title(job_title)
        new_employee_page.click_save()

        assert new_employee_page.is_upload_button_not_visible(), "Upload button is still visible"


    @pytest.mark.employee
    @pytest.mark.positive
    @pytest.mark.skip("Test under development")
    def test_delete_employee_profile(self, driver):
        login_page = LoginPage(driver)
        pass



