import os

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class EmployeeProfilePage:
    __url = os.environ["FRONTEND_URL"] + "/odoo/employees/6"
    __employee_name_locator = (By.XPATH, "//label[@for='work_email_0']")

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)

    def open(self):
        self._driver.get(self.__url)

    def is_employee_name_displayed(self) -> bool:
        element = self._wait.until(EC.presence_of_element_located(self.__employee_name_locator))
        return element is not None

