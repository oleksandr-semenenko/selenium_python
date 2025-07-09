import os

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import any_of

from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    __url = os.environ["FRONTEND_URL"] + "/web/login"
    __username_field = (By.ID, "login")
    __password_field = (By.ID, "password")
    __login_button = (By.XPATH, "//button[@class='btn btn-primary']")

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)

    def open(self):
        self._driver.get(self.__url)

    def execute_login(self, username: str, password: str):
        self._wait.until(
            EC.presence_of_element_located(self.__username_field)
        ).send_keys(username)
        self._driver.find_element(*self.__password_field).send_keys(password)
        self._driver.find_element(*self.__login_button).click()
        self._wait.until(
            any_of(
                EC.url_to_be(os.environ["FRONTEND_URL"] + "/odoo/discuss"),
                EC.text_to_be_present_in_element(
                    (By.XPATH, "//p[@class='alert alert-danger']"),
                    " Wrong login/password",
                ),
            )
        )
