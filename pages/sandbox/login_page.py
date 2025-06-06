import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    __url = "https://semenenko.sandbox.first.institute/web/login"
    __username_field = (By.ID, "login")
    __password_field = (By.ID, "password")
    __login_button = (By.XPATH, "//button[@class='btn btn-primary']")

    def __inint__(self, driver: WebDriver):
        self._driver = driver

    def open(self, _driver):
        self._driver.get(self.__url)

    def execute_login(self, username: str, password: str):
        self._driver.find_element(self.__username_field).send_keys(username)

        self._driver.find_element(self.__password_field).send_keys(password)

        self._driver.find_element(self.__login_button).click()
        time.sleep(5)