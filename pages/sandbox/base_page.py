import os
from abc import abstractmethod, ABC

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(ABC):
    # _path: str

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)

    @abstractmethod
    def wait_page_is_present(self) -> None:
        ...

    @abstractmethod
    def get_relative_url(self) -> str:
        ...

    def open(self) -> None:
        base_url = os.environ["FRONTEND_URL"]
        full_url = f"{base_url}{self.get_relative_url()}"
        self._driver.get(full_url)

        self.wait_page_is_present()
        return self


    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple[str, str], text: str, timeout: float = 10.0) -> None:
        self._wait_until_element_is_visible(locator, timeout)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple[str, str], timeout: float = 10.0) -> None:
        self._wait_until_element_is_visible(locator, timeout)
        self._find(locator).click()

    def _wait_until_element_is_visible(self, locator: tuple[str, str], timeout: float = 10.0):
        wait = WebDriverWait(self._driver, timeout)
        wait.until(EC.visibility_of_element_located(locator))
