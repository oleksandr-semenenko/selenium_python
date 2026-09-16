import os

import pytest

from pages.sandbox import department_page
from pages.sandbox.department_page import DepartmentList
from pages.sandbox.login_page import LoginPage


class TestPositiveScenarios:
    @pytest.mark.department
    @pytest.mark.positive
    def test_get_list_departments(self, driver, signed_as_admin):
        department_page = DepartmentList(driver)

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

    @pytest.mark.department
    @pytest.mark.positive
    def test_filters_departments_by_archived(self, driver, signed_as_admin):
        department_page = DepartmentList(driver)  # noqa: F811

        department_page.open()
        department_page.wait_page_is_present()
        department_page.click_choose_filter_button()
        department_page.choose_filter_archived_menu()
        department_page.wait_page_is_present()
        archived_departments = department_page.get_list_filter_archeved_departments()

        archived_departments_name = [dep.name for dep in archived_departments]
        assert archived_departments_name == [
            "Dynamic Marketing",
            "Kirby and Sons Dept 5401",
            "Raven Mitchell",
            "test",
            "test",
            "test",
        ]