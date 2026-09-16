import os
import re

import pytest

from pages.sandbox.department_page import DepartmentList
from pages.sandbox.department_profile_page import DepartmentProfilePage
from pages.sandbox.login_page import LoginPage
from pages.sandbox.new_department_page import NewDepartmentProfilePage
from utils.data_factory import generate_random_department_name


class TestPositiveScenarios:
    @pytest.mark.department
    @pytest.mark.positive
    def test_get_department_profile(self, driver, signed_as_admin):

        department_page = DepartmentList(driver)
        department_page.open()
        department_page.wait_page_is_present()

        departments = department_page.get_list_of_departments()
        assert departments, "No departments found on the departments page"

        department_name = departments[0].name
        department_page.click_department_by_name(department_name)

        department_id = DepartmentProfilePage.extract_department_id_from_current_url(driver)
        department_profile_page = DepartmentProfilePage(driver, department_id=department_id)
        department_profile_page.wait_page_is_present()

        assert department_profile_page.get_department_name() == department_name, (
            f"Department profile for {department_name} did not load"
        )


    @pytest.mark.department
    @pytest.mark.positive
    def test_create_department_profile(self, driver, signed_as_admin):

        department_page = DepartmentList(driver)
        department_page.open()
        department_page.wait_page_is_present()
        department_page.click_new_department_button()

        new_department_page = NewDepartmentProfilePage(driver)
        new_department_page.open()
        new_department_page.wait_page_is_present()

        set_department_name = generate_random_department_name()
        new_department_page.set_department_name(set_department_name)

        created_department_id = None
        try:
            new_department_page.click_save()
            assert new_department_page.is_upload_department_button_not_visible(), "Upload button is still visible"

            created_department_id = DepartmentProfilePage.extract_department_id_from_current_url(driver)
        finally:
            if created_department_id is not None:
                department_profile_page = DepartmentProfilePage(driver, department_id=created_department_id)
                department_profile_page.delete_department()

                department_list_page = DepartmentList(driver)
                department_list_page.wait_page_is_present()
                assert not department_list_page.has_department_with_name(set_department_name), (
                    f"Department {set_department_name!r} was not deleted from the department list"
                )


    @pytest.mark.department
    @pytest.mark.positive
    def test_edit_existing_department(self, driver, signed_as_admin):

        department_page = DepartmentList(driver)
        department_page.open()
        department_page.wait_page_is_present()

        departments = department_page.get_list_of_departments()
        assert departments, "No departments found on the departments page"

        original_name = departments[0].name
        renamed_department_name = f"{original_name} Updated"

        try:
            department_page.click_department_by_name(original_name)
            department_id = DepartmentProfilePage.extract_department_id_from_current_url(driver)
            department_profile_page = DepartmentProfilePage(driver, department_id=department_id)
            department_profile_page.wait_page_is_present()

            department_profile_page.set_department_name(renamed_department_name)
            department_profile_page.click_save()

            department_page.open()
            department_page.wait_page_is_present()
            assert department_page.has_department_with_name(renamed_department_name), (
                f"Department {renamed_department_name!r} was not updated in the department list"
            )
        finally:
            department_page.open()
            department_page.wait_page_is_present()

            if department_page.has_department_with_name(renamed_department_name):
                department_page.click_department_by_name(renamed_department_name)
                department_id = DepartmentProfilePage.extract_department_id_from_current_url(driver)
                department_profile_page = DepartmentProfilePage(driver, department_id=department_id)
                department_profile_page.wait_page_is_present()
                department_profile_page.set_department_name(original_name)
                department_profile_page.click_save()

            department_page.open()
            department_page.wait_page_is_present()
            assert department_page.has_department_with_name(original_name), (
                f"Department {original_name!r} was not restored after the edit"
            )
            assert not department_page.has_department_with_name(renamed_department_name), (
                f"Department {renamed_department_name!r} remains in the list after rollback"
            )
