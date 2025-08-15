import os
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class EmployeeProfilePage:
    __url = os.environ["FRONTEND_URL"] + "/odoo/employees/6"
    __employee_name_locator = (By.XPATH, "//label[@for='work_email_0']")
    __employee_job_title_input = (By.ID, "job_title_0")
    __upload_button = (By.CSS_SELECTOR, "i.fa-cloud-upload")

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)

    def open(self):
        self._driver.get(self.__url)

    def set_job_title(self, title: str):
        element = self._driver.find_element(*self.__employee_job_title_input)
        element.clear()
        element.send_keys(title)

    def click_save(self):
        self._wait.until(EC.presence_of_element_located(self.__upload_button)).click()

    def is_employee_name_displayed(self) -> bool:
        element = self._wait.until(EC.presence_of_element_located(self.__employee_name_locator))
        return element is not None

    def get_job_title(self) -> str:
        element = self._wait.until(
            EC.visibility_of_element_located(self.__employee_job_title_input)
        )
        return element.get_attribute("value")

    def is_employee_job_title_displayed(self) -> bool:
        try:
            self._wait.until(EC.visibility_of_element_located(self.__employee_job_title_input))
            return True
        except:
            return False

    def generate_random_job_title(self, prefix: str = "Consultant") -> str:
        return f"{prefix}{random.randint(1, 1000)}"
