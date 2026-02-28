import os

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import any_of
from selenium.webdriver.support.wait import WebDriverWait

from pages.sandbox.base_page import BasePage


class LoginPage(BasePage):
    __username_field = (By.ID, "login")
    __password_field = (By.ID, "password")
    __login_button = (By.XPATH, "//button[@class='btn btn-primary']")
    __error_message_locator = (
        By.XPATH,
        "//p[@class='alert alert-danger']",
    )

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._wait = WebDriverWait(driver, 10)

    def wait_page_is_present(self) -> None:
        self._wait.until(EC.element_to_be_clickable(self.__login_button))

    def get_relative_url(self) -> str:
        return "/web/login"

    def execute_login(self, username: str, password: str) -> "None":
        # use BasePage helpers instead of direct find_element
        self._type(self.__username_field, username)
        self._type(self.__password_field, password)
        self._click(self.__login_button)

        self._wait.until(
            any_of(
                EC.url_to_be(os.environ["FRONTEND_URL"] + "/odoo/discuss"),
                EC.text_to_be_present_in_element(
                    self.__error_message_locator, "Wrong login/password"
                ),
            )
        )

    def is_login_error_displayed(self) -> bool:
        return self._wait.until(
            EC.text_to_be_present_in_element(
                self.__error_message_locator,
                "Wrong login/password",
            )
        )
