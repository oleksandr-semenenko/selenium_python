from typing import Generator

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from webdriver_factory import get_driver


@pytest.fixture(scope="module")
def driver() -> Generator[WebDriver, None, None]:
    """Returns initialized WedDriver instance."""
    drv = get_driver()
    drv.implicitly_wait(1)
    yield drv
    drv.quit()

# My block of code
# @pytest.fixture()
# def driver():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(1)
#     yield driver
#     driver.quit()
#
#
# @pytest.fixture
# def autowait() -> Generator[None, None, None]:
#     enable_autowait()
#     yield
#     disable_autowait()
