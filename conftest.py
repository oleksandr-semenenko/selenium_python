from typing import Generator

import pytest
from selenium.webdriver.remote import webdriver
from selenium import webdriver

from utils.autowait import enable_autowait, disable_autowait
from webdriver_factory import get_driver


# @pytest.fixture(scope="module")
# def driver() -> Generator[WebDriver, None, None]:
#     """Returns initialized WedDriver instance."""
#     drv = get_driver()
#     yield drv
#     drv.quit()
#
#
# @pytest.fixture
# def autowait() -> Generator[None, None, None]:
#     enable_autowait()
#     yield
#     disable_autowait()






@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()