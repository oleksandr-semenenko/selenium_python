import re

import pytest

from pages.sandbox.employee_profile_page import EmployeeProfilePage
from pages.sandbox.employees_page import EmployeesList
from pages.sandbox.new_employee_profile_page import NewEmployeeProfilePage
from utils.data_factory import generate_random_name, generate_random_job_title


class TestPositiveScenarios:
    @pytest.mark.employee
    @pytest.mark.order(3)
    @pytest.mark.positive
    def test_get_employee_profile(self, driver, signed_as_admin):

        employees_page = EmployeesList(driver)
        employee_profile_page = EmployeeProfilePage(driver, employee_id=6)
        employee_profile_page.open()

        employees_page.open()
        employees_page.click()
        employee_profile_page.wait_page_is_present()

        assert employee_profile_page.is_employee_name_displayed()


    @pytest.mark.employee
    @pytest.mark.order(4)
    @pytest.mark.positive
    def test_create_employee_profile(self, driver, signed_as_admin):

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

        created_employee_id = None
        try:
            assert new_employee_page.is_upload_button_not_visible(), "Upload button is still visible"

            try:
                created_employee_id = _extract_employee_id_from_current_url(driver)
            except ValueError:
                employees_page.open()
                created_employee_id = employees_page.get_employee_id_by_name(set_name_employee)
        finally:
            if created_employee_id is None:
                try:
                    created_employee_id = _extract_employee_id_from_current_url(driver)
                except ValueError:
                    try:
                        employees_page.open()
                        created_employee_id = employees_page.get_employee_id_by_name(set_name_employee)
                    except Exception:
                        created_employee_id = None

            if created_employee_id is not None:
                employee_profile_page = EmployeeProfilePage(driver, employee_id=created_employee_id)
                employee_profile_page.open()
                employee_profile_page.delete_employee()
                print(f"Employee profile page {created_employee_id} deleted")


def _extract_employee_id_from_current_url(driver):
    match = re.search(r"/odoo/employees/(\d+)", driver.current_url)
    if not match:
        raise ValueError(f"Employee id was not found in current url: {driver.current_url}")
    return int(match.group(1))

