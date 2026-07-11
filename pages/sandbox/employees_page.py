import re
from dataclasses import dataclass

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.sandbox.base_page import BasePage


@dataclass
class Employee:
    name: str


class EmployeesList(BasePage):
    __employees_card_locator = By.TAG_NAME, "article"
    __employee_name_locator = (By.XPATH, "//label[@for='work_email_0']")
    __new_employee_button = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[1]/div/button")

    # def __init__(self, driver: WebDriver):
    #     super().__init__(driver)
    #     self._wait = WebDriverWait(driver, 10)

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