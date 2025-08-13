import os
from dataclasses import dataclass

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@dataclass
class Employee:
    name: str
    job_title: str
    email: str
    phone: str


class EmployeesPage:
    __url = os.environ["FRONTEND_URL"] + "/odoo/employees"
    __employees_card_locator = By.TAG_NAME, "article"

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)

    def open(self):
        self._driver.get(self.__url)

    def click(self):
        element = self._wait.until(EC.element_to_be_clickable(self.__employees_card_locator))
        element.click()

    def get_list_of_employees(self) -> list[Employee]:
        employees: list[Employee] = []

        # Look for all <article> tags — they are Employee card.
        for el in self._driver.find_elements(*self.__employees_card_locator):
            # Looking for each element one by one.
            # See ./pages/sandbox/employee_card.html for example.
            name = el.find_element(By.TAG_NAME, "span").text.strip()            # Name is the first <span>
            job = el.find_element(By.CSS_SELECTOR, "main > span").text.strip()  # 1st <span> in <main>
            email = el.find_element(By.XPATH, "(//main/div)[2]").text.strip()   # 2nd <div> in <main>
            phone = el.find_element(By.XPATH, "(//main/div)[3]").text.strip()   # 3rd <div> in <main>

            employees.append(Employee(name=name, job_title=job, email=email, phone=phone))

        return employees
