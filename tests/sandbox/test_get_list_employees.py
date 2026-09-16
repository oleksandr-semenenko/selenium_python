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

    @pytest.mark.employee
    @pytest.mark.positive
    def test_filter_employees_by_myteam(self, driver):
        login_page = LoginPage(driver)
        employees_page = EmployeesList(driver)

        login_page.open()
        login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])

        employees_page.open()
        employees_page.wait_page_is_present()
        employees_page.click_choose_filter_button()
        employees_page.choose_filter_myteam()
        myteam_employees = employees_page.get_employees_filter_myteam()

        myteam_employees_name = [emp.name for emp in myteam_employees]
        assert myteam_employees_name == [
            'Jeffrey Kelly',
            'Marc Demo',
            'Tina Williamson',
        ]

    @pytest.mark.employee
    @pytest.mark.positive
    def test_filter_employees_by_mydepartment(self, driver):
        login_page = LoginPage(driver)
        employees_page = EmployeesList(driver)

        login_page.open()
        login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])

        employees_page.open()
        employees_page.wait_page_is_present()
        employees_page.click_choose_filter_button()
        employees_page.choose_filter_mydepartment()
        mydepartment_employees = employees_page.get_employees_filter_mydepartment()

        mydepartment_employees_name = [emp.name for emp in mydepartment_employees]
        assert mydepartment_employees_name == [
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

    @pytest.mark.employee
    @pytest.mark.positive
    def test_filter_employees_by_newlyhired(self, driver, signed_as_admin):
        employees_page = EmployeesList(driver)

        employees_page.open()
        employees_page.wait_page_is_present()
        employees_page.click_choose_filter_button()
        employees_page.choose_filter_newlyhired()
        newlyhired_employees = employees_page.get_employees_filter_newlyhired()

        newlyhired_employees_name = [emp.name for emp in newlyhired_employees]
        assert newlyhired_employees_name == ["Bethany Fisher"]

    @pytest.mark.employee
    @pytest.mark.positive
    def test_filter_employees_by_archived(self, driver, signed_as_admin):
        employees_page = EmployeesList(driver)

        employees_page.open()
        employees_page.wait_page_is_present()
        employees_page.click_choose_filter_button()
        employees_page.choose_filter_archived()
        archived_employees = employees_page.get_employees_filter_archived()

        archived_employees_name = [emp.name for emp in archived_employees]
        assert archived_employees_name == []

    @pytest.mark.employee
    @pytest.mark.positive
    def test_group_employees_by_manager(self, driver, signed_as_admin):
        employees_page = EmployeesList(driver)

        employees_page.open()
        employees_page.wait_page_is_present()
        employees_page.click_choose_filter_button()
        employees_page.choose_group_by_manager()
        employees_page.close_filter_menu()  # Close the menu and wait for it to disappear
        
        # Get employees grouped by manager
        manager_groups = employees_page.get_employees_grouped_by_manager()
        
        assert len(manager_groups) > 0, "No manager groups found"
        
        # Find the first non-None manager group
        from pages.sandbox.employee_profile_page import EmployeeProfilePage
        
        for manager_group in manager_groups:
            manager_name = manager_group.manager_name
            employees = manager_group.employees
            
            # Skip "None" groups (employees without managers)
            if manager_name.lower() == "none":
                continue
            
            # Verify at least one employee in the group
            assert len(employees) > 0, f"Manager group '{manager_name}' has no employees"
            
            # Click on the first employee card to open their profile
            first_employee = employees[0]
            employees_page.click_employee_by_name(first_employee)
            
            # Get the employee ID
            employee_id = employees_page.get_employee_id_by_name(first_employee)
            profile_page = EmployeeProfilePage(driver, employee_id)
            
            # Get the manager from the employee's profile (this has its own wait)
            profile_manager = profile_page.get_manager()
            
            # Verify the manager matches the group manager
            assert profile_manager == manager_name or profile_manager.strip() == manager_name.strip(), \
                f"Employee '{first_employee}' has manager '{profile_manager}' but is grouped under '{manager_name}'"
            
            print(f"✓ Verified: Employee '{first_employee}' manager '{profile_manager}' matches group '{manager_name}'")
            
            # Done - break after first valid group
            break


    @pytest.mark.employee
    @pytest.mark.positive
    def test_group_employees_by_department(self, driver, signed_as_admin):
        employees_page = EmployeesList(driver)

        employees_page.open()
        employees_page.wait_page_is_present()
        employees_page.click_choose_filter_button()
        employees_page.choose_group_by_department()
        employees_page.close_filter_menu()  # Close the menu and wait for it to disappear

        # Get employees grouped by department
        department_groups = employees_page.get_employees_grouped_by_department()

        assert len(department_groups) > 0, "No departments groups found"

        # Find the first non-None department group
        from pages.sandbox.employee_profile_page import EmployeeProfilePage

        for department_group in department_groups:
            department_name = department_group.department_name
            employees = department_group.employees

            # Skip "None" groups (employees without department)
            if department_name.lower() == "none":
                continue

            # Verify at least one employee in the group
            assert len(employees) > 0, (f"Department group '{department_name}' has no "
                                        f"employees")

            # Click on the first employee card to open their profile
            first_employee = employees[0]
            employees_page.click_employee_by_name(first_employee)

            # Get the employee ID
            employee_id = employees_page.get_employee_id_by_name(first_employee)
            profile_page = EmployeeProfilePage(driver, employee_id)

            # Get the department from the employee's profile (this has its own wait)
            profile_department = profile_page.get_department()

            # Verify the department matches the group manager
            assert (
                profile_department == department_name or profile_department.strip() ==
                department_name.strip()
            ), (
                f"Employee '{first_employee}' has department '{profile_department}' "
                f"but "
                f"is grouped under '{department_name}'"
            )

            print(
                f"✓ Verified: Employee '{first_employee}' department '"
                f"{profile_department}' matches group '{department_name}'"
            )

            # Done - break after first valid group
            break