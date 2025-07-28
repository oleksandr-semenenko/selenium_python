import os
from dataclasses import dataclass, field
from typing import List

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


@dataclass
class Employees:
    name: str
    job_title: str


class EmployeesPage:
    __url = os.environ["FRONTEND_URL"] + "/odoo/employees"
    __employee_locator = (By.CSS_SELECTOR, "span.fw-bold.fs-5")
    __job_title_locator = (By.XPATH, "//span[not(@class)]")

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)

    def open(self):
        self._driver.get(self.__url)

    def click(self):
        element = self._wait.until(EC.element_to_be_clickable(self.__employee_locator))
        element.click()

    # def click(self):
    #     self._driver.click(self.__employee_locator)



    # Previous code
    # def get_list_of_employees(self) -> List[Employee]:
    #     elements = self._driver.find_elements(*self.__employee_locator)
    #     return [Employee(name=el.text) for el in elements if el.text]
    #----------

    # New block of code
    def get_list_of_employees(self) -> List[Employees]:
        name_elements = self._driver.find_elements(*self.__employee_locator)
        job_title_elements = self._driver.find_elements(*self.__job_title_locator)


        #assert len(name_elements) == len(job_title_elements), "Mismatch between names and job titles"

        employees = [
            Employees(name=name.text, job_title=job.text)
            for name, job in zip(name_elements, job_title_elements)
        ]
        return employees