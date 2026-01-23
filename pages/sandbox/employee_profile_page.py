import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.sandbox.base_page import BasePage


class EmployeeProfilePage(BasePage):
    _path = "/odoo/employees/6"

    __employee_name_locator = (By.XPATH, "//label[@for='work_email_0']")
    __employee_job_title_input = (By.ID, "job_title_0")
    __upload_button = (By.CSS_SELECTOR, "i.fa-cloud-upload")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._wait = WebDriverWait(driver, 10)

    def wait_page_is_present(self) -> None:
        self._wait.until(EC.element_to_be_clickable(self.__employee_job_title_input))

    def get_relative_url(self) -> str:
        return self._path

    def set_job_title(self, title: str):
        element = self._driver.find_element(*self.__employee_job_title_input)
        element.clear()
        element.send_keys(title + "\n")

    def click_save(self):
        self._wait.until(EC.presence_of_element_located(self.__upload_button)).click()
        self._wait.until(EC.invisibility_of_element(self.__upload_button))

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
            element = self._driver.find_element(*self.__employee_job_title_input)
            return element.is_displayed()
        except:
            return False

    def generate_random_job_title(self, prefix: str = "Consultant") -> str:
        return "".join(random.choices(string.ascii_letters, k=10))
