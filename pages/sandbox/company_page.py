from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.sandbox.base_page import BasePage


class CompanyPage(BasePage):
    __company_locator = (By.XPATH, "/html/body/header/nav/div[4]/div[11]/button/img")
    __documentation_button = (By.XPATH, "//a[contains(., 'Documentation')] | //button[contains(., 'Documentation')]" )
    __support_button = (By.XPATH, "//a[contains(., 'Support')]" )

    def wait_page_is_present(self) -> None:
        self._wait.until(EC.element_to_be_clickable(self.__company_locator))

    def get_relative_url(self) -> str:
        return "/odoo/discuss"

    def click(self):
        self.wait_page_is_present()
        self._click(self.__company_locator)

    def click_documentation(self):
        self._wait.until(EC.element_to_be_clickable(self.__documentation_button)).click()

    def click_support(self):
        self._wait.until(EC.element_to_be_clickable(self.__support_button)).click()


