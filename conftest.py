import os

from dotenv import load_dotenv

from pages.sandbox.employees_page import EmployeesList
from pages.sandbox.login_page import LoginPage
from pages.sandbox.new_employee_profile_page import NewEmployeeProfilePage
from utils.data_factory import generate_random_name, generate_random_job_title


def pytest_configure():
    load_dotenv()

from collections.abc import Generator

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from webdriver_factory import get_driver
from utils.autowait import enable_autowait, disable_autowait


@pytest.fixture(scope="module")
def driver() -> Generator[WebDriver, None, None]:
    """Returns initialized WedDriver instance."""
    drv = get_driver()
    drv.implicitly_wait(1)
    yield drv
    drv.quit()


@pytest.fixture
def autowait():
    """Enable global autowait for WebElement actions during a test."""
    enable_autowait(timeout=2.0)
    yield
    try:
        disable_autowait()
    except Exception:
        # if autowait was already disabled or something went wrong, ignore
        pass