import os
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
    _path = "/odoo/employees"

    __employees_card_locator = By.TAG_NAME, "article"
    __employee_name_locator = (By.XPATH, "//label[@for='work_email_0']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._wait = WebDriverWait(driver, 10)

    def wait_page_is_present(self) -> None:
        self._wait.until(EC.element_to_be_clickable(self.__employees_card_locator))

    def get_relative_url(self) -> str:
        return self._path

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