from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from conftest import driver


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str):
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple):
        self._find(locator).click()