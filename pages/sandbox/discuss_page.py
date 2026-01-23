from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class DiscussPage(BasePage):
    _path = "/odoo/discuss"

    __discuss_locator = (By.XPATH, "//a[@data-menu-xmlid='mail.menu_root_discuss']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._wait = WebDriverWait(driver, 10)

    def wait_page_is_present(self) -> None:
        #self._wait.until(EC.element_to_be_clickable(self.__discuss_locator))
        self._wait.until(EC.visibility_of_element_located(self.__discuss_locator))

    def get_relative_url(self) -> str:
        return self._path