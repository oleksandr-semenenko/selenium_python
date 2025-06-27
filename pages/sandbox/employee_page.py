from dataclasses import dataclass, field
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


@dataclass
class Employee:
    name: str
    job_title: str = field(default="")

class EmployeePage:
    __url = "https://semenenko.sandbox.first.institute/odoo/employees"
    __employee_locator = (By.CSS_SELECTOR, "span.fw-bold.fs-5")

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)

    def open(self):
        self._driver.get(self.__url)

    def get_list_of_employees(self) -> List[Employee]:
        elements = self._driver.find_elements(*self.__employee_locator)
        return [Employee(name=el.text.strip()) for el in elements if el.text.strip()]