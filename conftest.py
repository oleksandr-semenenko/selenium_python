from collections.abc import Generator

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