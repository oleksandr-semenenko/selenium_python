import re

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.sandbox.base_page import BasePage


class DepartmentProfilePage(BasePage):
    __department_name_locator = (By.XPATH, "//label[@for='parent_id_0' and contains(@class, 'o_form_label')]")
    __department_name_input = (By.ID, "name_0")
    __upload_button = (By.CSS_SELECTOR, "i.fa-cloud-upload")
    __action_button = (By.CSS_SELECTOR, ".o_cp_action_menus button.o-dropdown.dropdown-toggle")
    __delete_menu_item = (By.XPATH, "//span[contains(@class,'o-dropdown-item') and normalize-space()='Delete']")
    __confirm_delete_button = (By.XPATH, "//footer[contains(@class,'modal-footer')]//button[normalize-space()='Delete']")

    def __init__(self, driver: WebDriver, department_id: int):
        super().__init__(driver)
        self._department_id = department_id

    def wait_page_is_present(self) -> None:
        self._wait.until(EC.element_to_be_clickable(self.__department_name_input))

    def is_department_name_displayed(self) -> bool:
        element = self._wait.until(EC.presence_of_element_located(self.__department_name_locator))
        return element is not None

    def set_department_name(self, name: str) -> None:
        element = self._wait.until(EC.element_to_be_clickable(self.__department_name_input))
        element.clear()
        element.send_keys(name)

    def click_save(self):
        self._wait.until(EC.presence_of_element_located(self.__upload_button)).click()
        self._wait.until(EC.invisibility_of_element(self.__upload_button))

    def get_department_name(self) -> str:
        element = self._wait.until(EC.visibility_of_element_located(self.__department_name_input))
        return element.get_attribute("value")

    @classmethod
    def extract_department_id_from_current_url(cls, driver: WebDriver) -> int:
        match = re.search(r"/odoo/departments/(\d+)$", driver.current_url)
        if not match:
            raise ValueError(f"Department id was not found in current url: {driver.current_url}")
        return int(match.group(1))

    def get_relative_url(self) -> str:
        return f"/odoo/departments/{self._department_id}"

    def delete_department(self) -> None:
        self.wait_page_is_present()
        self._wait.until(EC.element_to_be_clickable(self.__action_button)).click()
        self._wait.until(EC.element_to_be_clickable(self.__delete_menu_item)).click()
        confirm_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(self.__confirm_delete_button)
        )
        confirm_button.click()
        WebDriverWait(self._driver, 10).until(
            EC.invisibility_of_element_located(self.__confirm_delete_button)
        )
        WebDriverWait(self._driver, 10).until(
            EC.url_matches(r".*/odoo/departments$")
        )