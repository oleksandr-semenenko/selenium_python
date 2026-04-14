import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.sandbox.base_page import BasePage


class NewEmployeeProfilePage(BasePage):
    __new_employee_locator = (By.XPATH, '//span[text()="New"]')
    __new_employee_name_input = (By.ID, "name_0")
    __new_employee_job_title_input = (By.XPATH, "/html//input[@id='job_title_0']")
    __upload_employee_button = (By.XPATH, "//i[contains(@class, 'fa-cloud-upload')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._wait = WebDriverWait(driver, 10)

    def get_relative_url(self) -> str:
        return f'/odoo/employees/new'

    def wait_page_is_present(self) -> None:
        self._wait.until(EC.visibility_of_element_located(self.__new_employee_locator))


    def set_employee_name(self, name: str) -> None:
        element = self._wait.until(EC.element_to_be_clickable(self.__new_employee_name_input))
        element.send_keys(name)


    def set_job_title(self, title: str) -> None:
        element = self._wait.until(EC.element_to_be_clickable(
            self.__new_employee_job_title_input))
        element.send_keys(title)


    def click_save(self):
        self._wait.until(EC.presence_of_element_located(self.__upload_employee_button)).click()
        self._wait.until(EC.invisibility_of_element(self.__upload_employee_button))


    def is_upload_button_not_visible(self):
        return WebDriverWait(self._driver, 5).until(
            EC.invisibility_of_element_located(self.__upload_employee_button)
        )