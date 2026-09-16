import re
from dataclasses import dataclass

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from pages.sandbox.base_page import BasePage


@dataclass
class Employee:
    name: str

@dataclass
class MyteamEmployees:
    name: str

@dataclass
class MydepartmentEmployees:
    name: str

@dataclass
class NewlyHiredEmployees:
    name: str

@dataclass
class ArchivedEmployees:
    name: str

@dataclass
class ManagerGroup:
    manager_name: str
    employees: list[str]

@dataclass
class DepartmentGroup:
    department_name: str
    employees: list[str]


class EmployeesList(BasePage):
    __employees_card_locator = By.TAG_NAME, "article"
    __employee_name_locator = (By.XPATH, "//label[@for='work_email_0']")
    __new_employee_button = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[1]/div/button")
    __choose_filter_button = (By.XPATH, "//button[@title='Toggle Search Panel']")
    __filter_myteam = (By.XPATH, "//span[@role='menuitemcheckbox' and normalize-space()='My Team']")
    __filter_mydepartment = (By.XPATH, "//span[@role='menuitemcheckbox' and normalize-space()='My Department']")
    __filter_newlyhired = (By.XPATH, "//span[@role='menuitemcheckbox' and "
                                     "normalize-space()='Newly Hired']")
    __filter_archived = (By.XPATH, "//span[@role='menuitemcheckbox' and normalize-space()='Archived']")
    __group_by_manager = (By.XPATH, "//span[@role='menuitemcheckbox' and normalize-space()='Manager']")
    __group_by_department = (By.XPATH, "//span[@role='menuitemcheckbox' and "
                                       "normalize-space()='Department']")

    def wait_page_is_present(self) -> None:
        self._wait.until(EC.element_to_be_clickable(self.__employees_card_locator))

    def get_relative_url(self) -> str:
        return "/odoo/employees"

    def click(self):
        self._wait.until(EC.element_to_be_clickable(self.__employees_card_locator)).click()
        self._wait.until(EC.presence_of_element_located(self.__employee_name_locator))

    def get_list_of_employees(self) -> list[Employee]:
        employees: list[Employee] = []

        # Look for all <article> tags — they are Employee card.
        for el in self._driver.find_elements(*self.__employees_card_locator):
            # Looking for each element one by one.
            # See ./pages/sandbox/employee_card.html for example.
            name = el.find_element(By.TAG_NAME, "span").text.strip()  # Name is the first <span>

            employees.append(Employee(name=name))

        return employees

    def _find_employee_card_by_name(self, name: str):
        for el in self._driver.find_elements(*self.__employees_card_locator):
            try:
                if el.find_element(By.TAG_NAME, "span").text.strip() == name:
                    return el
            except Exception:
                continue
        raise ValueError(f"Employee card with name {name!r} not found")

    def get_employee_id_by_name(self, name: str) -> int:
        employee_card = self._find_employee_card_by_name(name)
        data_id = employee_card.get_attribute("data-id") or ""
        match = re.search(r"(\d+)$", data_id)
        if not match:
            raise ValueError(f"Cannot parse employee id from card data-id: {data_id}")
        return int(match.group(1))

    def click_employee_by_name(self, name: str) -> None:
        self._find_employee_card_by_name(name).click()

    def click_new_employee_button(self):
        self._wait.until(EC.element_to_be_clickable(self.__new_employee_button)).click()
    
    def click_choose_filter_button(self):
        self._wait.until(EC.element_to_be_clickable(self.__choose_filter_button)).click()
    
    def close_filter_menu(self):
        """Close the filter menu by clicking the filter button again or clicking the main content area."""
        try:
            # Try clicking the filter button again to toggle it closed
            self._wait.until(EC.element_to_be_clickable(self.__choose_filter_button)).click()
            import time
            time.sleep(1)
        except Exception:
            # If that doesn't work, try clicking somewhere in the main content area
            try:
                self._driver.find_element(By.CSS_SELECTOR, "main").click()
                import time
                time.sleep(0.5)
            except Exception:
                pass

    def choose_filter_myteam(self):
        self._wait.until(EC.element_to_be_clickable(self.__filter_myteam)).click()
        self._wait.until(
            lambda driver: (
                driver.find_element(*self.__filter_myteam).get_attribute("aria-checked") == "true"
                and len(driver.find_elements(*self.__employees_card_locator)) == 3
            )
        )

    def get_employees_filter_myteam(self) -> list[MyteamEmployees]:
        myteam_employees: list[MyteamEmployees] = []
        for el in self._driver.find_elements(*self.__employees_card_locator):
            try:
                name = el.find_element(By.TAG_NAME, "span").text.strip()
            except Exception:
                continue

            if name:
                myteam_employees.append(MyteamEmployees(name=name))

        return myteam_employees

    def choose_filter_mydepartment(self):
        self._wait.until(EC.element_to_be_clickable(self.__filter_mydepartment)).click()
        self._wait.until(
            lambda driver: (
                driver.find_element(*self.__filter_mydepartment).get_attribute(
                    "aria-checked") == "true"
                and len(driver.find_elements(*self.__employees_card_locator)) == 20
            )
        )

    def get_employees_filter_mydepartment(self) -> list[MydepartmentEmployees]:
        mydepartment_employees: list[MydepartmentEmployees] = []
        for el in self._driver.find_elements(*self.__employees_card_locator):
            try:
                name = el.find_element(By.TAG_NAME, "span").text.strip()
            except Exception:
                continue

            if name:
                mydepartment_employees.append(MydepartmentEmployees(name=name))

        return mydepartment_employees

    def choose_filter_newlyhired(self):
        initial_names = [employee.name for employee in self.get_list_of_employees()]
        self._wait.until(EC.element_to_be_clickable(self.__filter_newlyhired)).click()
        self._wait.until(
            lambda driver: [
                employee.name for employee in self.get_employees_filter_newlyhired()
            ] != initial_names
        )

    def get_employees_filter_newlyhired(self) -> list[NewlyHiredEmployees]:
        newlyhired_employees: list[NewlyHiredEmployees] = []
        for el in self._driver.find_elements(*self.__employees_card_locator):
            try:
                name = el.find_element(By.TAG_NAME, "span").text.strip()
            except Exception:
                continue

            if name:
                newlyhired_employees.append(NewlyHiredEmployees(name=name))

        return newlyhired_employees

    def choose_filter_archived(self):
        self._wait.until(EC.element_to_be_clickable(self.__filter_archived)).click()
        self._wait.until(
            lambda driver: (
                driver.find_element(*self.__filter_archived).get_attribute(
                    "aria-checked") == "true"
                and len(driver.find_elements(*self.__employees_card_locator)) == 0
            )
        )

    def get_employees_filter_archived(self) -> list[ArchivedEmployees]:
        archived_employees: list[ArchivedEmployees] = []
        for el in self._driver.find_elements(*self.__employees_card_locator):
            try:
                name = el.find_element(By.TAG_NAME, "span").text.strip()
            except Exception:
                continue

            if name:
                archived_employees.append(ArchivedEmployees(name=name))

        return archived_employees

    def choose_group_by_manager(self):
        self._wait.until(EC.element_to_be_clickable(self.__group_by_manager)).click()
        self._wait.until(
            lambda driver: (
                driver.find_element(*self.__group_by_manager).get_attribute(
                    "aria-checked") == "true"
            )
        )
    
    def get_employees_grouped_by_manager(self) -> list[ManagerGroup]:
        """Get employees grouped by manager.
        
        Returns a list of ManagerGroup objects, each containing a manager name
        and their list of employees.
        """
        manager_groups = []
        
        # Find all group headers (which contain manager names)
        group_headers = self._driver.find_elements(
            By.XPATH, "//div[contains(@class, 'o_kanban_group')]/div[contains(@class, 'o_kanban_header')]"
        )
        
        for header in group_headers:
            try:
                # Extract manager name from the header
                # Header text format is "Manager Name\n(ID)" or "None\n(ID)"
                header_text = header.text.strip()
                if not header_text:
                    continue
                
                # Parse the header to extract just the manager name (remove the ID part)
                # Split by newline and take the first part, then strip any leading/trailing whitespace
                manager_name = header_text.split('\n')[0].strip()
                
                # Find the parent group container
                group_container = header.find_element(By.XPATH, "./ancestor::div[contains(@class, 'o_kanban_group')]")
                
                # Find all employee cards within this group
                employee_cards = group_container.find_elements(*self.__employees_card_locator)
                
                employees = []
                for card in employee_cards:
                    try:
                        name = card.find_element(By.TAG_NAME, "span").text.strip()
                        if name:
                            employees.append(name)
                    except Exception:
                        continue
                
                manager_groups.append(ManagerGroup(manager_name=manager_name, employees=employees))
            except Exception:
                continue
        
        return manager_groups
    
    def choose_group_by_department(self):
        self._wait.until(EC.element_to_be_clickable(self.__group_by_department)).click()
        self._wait.until(
            lambda driver: (
                driver.find_element(*self.__group_by_department).get_attribute(
                    "aria-checked") == "true"
            )
        )

    def get_employees_grouped_by_department(self) -> list[DepartmentGroup]:
        """Get employees grouped by department.

        Returns a list of DepartmentGroup objects, each containing a department name
        and their list of employees.
        """
        department_groups = []

        # Find all group headers (which contain department names)
        group_headers = self._driver.find_elements(
            By.XPATH,
            "//div[contains(@class, 'o_kanban_group')]/div[contains(@class, 'o_kanban_header')]",
        )

        for header in group_headers:
            try:
                # Extract department name from the header
                # Header text format is "Department Name" or "None"
                header_text = header.text.strip()
                if not header_text:
                    continue

                # Parse the header to extract just the department name (remove the ID
                # part)
                # Split by newline and take the first part, then strip any leading/trailing whitespace
                department_name = header_text.split("\n")[0].strip()

                # Find the parent group container
                group_container = header.find_element(
                    By.XPATH, "./ancestor::div[contains(@class, 'o_kanban_group')]"
                )

                # Find all employee cards within this group
                employee_cards = group_container.find_elements(*self.__employees_card_locator)

                employees = []
                for card in employee_cards:
                    try:
                        name = card.find_element(By.TAG_NAME, "span").text.strip()
                        if name:
                            employees.append(name)
                    except Exception:
                        continue

                department_groups.append(DepartmentGroup(
                    department_name=department_name,
                    employees=employees,
                ))
            except Exception:
                continue

        return department_groups