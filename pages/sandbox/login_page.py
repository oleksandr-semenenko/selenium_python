import os

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    __url = "https://semenenko.sandbox.first.institute/web/login"
    __username_field = (By.ID, "login")
    __password_field = (By.ID, "password")
    __login_button = (By.XPATH, "//button[@class='btn btn-primary']")

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)

    def open(self):
        self._driver.get(self.__url)

    def execute_login(self, username: str, password: str):

        self._wait.until(EC.presence_of_element_located(self.__username_field)).send_keys(username)
        self._driver.find_element(*self.__password_field).send_keys(password)
        self._driver.find_element(*self.__login_button).click()

    def login_with_env_credentials(self):
        username = os.environ["LOGIN"]
        password = os.environ["PASSWORD"]
        self.execute_login(username, password)