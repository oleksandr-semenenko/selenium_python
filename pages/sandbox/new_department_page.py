import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.sandbox.base_page import BasePage


class NewDepartmentProfilePage(BasePage):
    __new_department_locator = (By.XPATH, '//button[normalize-space(text())="New"]')
    __new_department_name_input = (By.XPATH, "//input[@id='name_0']")
    #__new_department_name_input = (By.ID, "name_0")
    __upload_department_button = (By.XPATH, "//i[contains(@class, 'fa-cloud-upload')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._wait = WebDriverWait(driver, 10)

    def get_relative_url(self) -> str:
        return f'/odoo/departments/new'

    def wait_page_is_present(self) -> None:
        self._wait.until(EC.visibility_of_element_located(
            self.__new_department_locator))


    def set_department_name(self, name: str) -> None:
        element = self._wait.until(EC.element_to_be_clickable(self.__new_department_name_input))
        element.send_keys(name)


    def click_save(self):
        self._wait.until(EC.presence_of_element_located(self.__upload_department_button)).click()
        self._wait.until(EC.invisibility_of_element(self.__upload_department_button))


    def is_upload_department_button_not_visible(self):
        return WebDriverWait(self._driver, 5).until(
            EC.invisibility_of_element_located(self.__upload_department_button)
        )