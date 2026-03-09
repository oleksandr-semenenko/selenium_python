import os

import pytest
from selenium import webdriver

from pages.sandbox.login_page import LoginPage

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Choose browser to execute tests: chrome or firefox",
    )

# @pytest.fixture(params=["chrome", "firefox"])
@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param
    print(f"Creating selenium driver for {browser}")

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    else:
        raise TypeError(f"Expected 'chrome' or 'firefox' but got {browser}")

    #driver.maximize_window()

    yield driver
    print(f"Closing selenium driver for {browser}")
    driver.quit()

    driver.quit()


@pytest.fixture()
def signed_as_admin(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.execute_login(os.environ["LOGIN"], os.environ["PASSWORD"])
    return driver
