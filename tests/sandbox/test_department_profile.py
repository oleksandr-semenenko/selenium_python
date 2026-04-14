import os

import pytest

from pages.sandbox.department_page import DepartmentList
from pages.sandbox.department_profile_page import DepartmentProfilePage
from pages.sandbox.login_page import LoginPage
from pages.sandbox.new_department_page import NewDepartmentProfilePage
from utils.data_factory import generate_random_name, generate_random_department_name


class TestPositiveScenarios:
    @pytest.mark.department
    @pytest.mark.positive
    #@pytest.mark.skip("Test under development, not work yet")
    def test_get_department_profile(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])

        department_page = DepartmentList(driver)
        department_page.open()
        department_page.click()


        department_profile_page = DepartmentProfilePage(driver, department_id=1)
        # department_profile_page.open()
        #
        # department_page.open()
        # department_page.click()
        department_profile_page.wait_page_is_present()

        assert department_profile_page.is_department_name_displayed(), "Department does not exist"

    # New test about creat new department profile
    @pytest.mark.department
    @pytest.mark.positive
    @pytest.mark.skip("Test under development")
    def test_create_department_profile(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])

        department_page = DepartmentList(driver)
        department_page.open()
        department_page.wait_page_is_present()
        department_page.click_new_department_button()

        new_department_page = NewDepartmentProfilePage(driver)
        new_department_page.open()
        new_department_page.wait_page_is_present()

        set_department_name = generate_random_department_name()
        new_department_page.set_department_name(set_department_name)
        new_department_page.click_save()

        assert new_department_page.is_upload_department_button_not_visible(), "Upload button is still visible"



