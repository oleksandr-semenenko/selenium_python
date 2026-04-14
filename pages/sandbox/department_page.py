import random
import string
from dataclasses import dataclass

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.sandbox.base_page import BasePage

@dataclass
class Department:
    name: str


class DepartmentList(BasePage):
    __department_locator = (By.XPATH, "//span[@class='min-w-0 text-truncate' and text()='Departments']")
    __department_card_locator = (By.XPATH, "/html/body/div[1]/div/div[2]/div/article")
    # I cannot find right locator for all this cards not only for Administarion
    __department_name_locator = (By.XPATH, "//a[.//span[normalize-space("
                                           ")='Administration']]")
    __new_department_button = (By.XPATH, "//button[normalize-space(text())='New']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._wait = WebDriverWait(driver, 10)

    def get_relative_url(self) -> str:
        return f'/odoo/departments'

    def wait_page_is_present(self) -> None:
        self._wait.until(EC.visibility_of_element_located(self.__department_locator))

    def get_list_of_departments(self) -> list[Department]:
        departments: list[Department] = []

        for el in self._driver.find_elements(*self.__department_name_locator):
            name = el.find_element(By.TAG_NAME,
                                   "span").text.strip()  # Name is the first <span>

            departments.append(Department(name=name))

        return departments

    def click_new_department_button(self):
        self._wait.until(EC.element_to_be_clickable(self.__new_department_button)).click()

    def click(self):
        self._wait.until(EC.element_to_be_clickable(
            self.__department_name_locator)).click()
        self._wait.until(EC.presence_of_element_located(self.__department_name_locator))