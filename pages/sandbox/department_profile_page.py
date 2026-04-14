import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from pages.sandbox.base_page import BasePage


class DepartmentProfilePage(BasePage):
    __department_name_locator = (By.XPATH, "//label[@for='parent_id_0' and contains(@class, 'o_form_label')]")

    def __init__(self, driver: WebDriver, department_id: int):
        super().__init__(driver)
        self._department_id = department_id

    def wait_page_is_present(self) -> None:
        self._wait.until(EC.element_to_be_clickable(self.__department_name_locator))

    def is_department_name_displayed(self) -> bool:
        element = self._wait.until(EC.presence_of_element_located(self.__department_name_locator))
        return element is not None


    def get_relative_url(self) -> str:
        return f"/odoo/department/{self._department_id}"